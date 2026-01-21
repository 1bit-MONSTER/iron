# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This file implements a simple Python-based build system. You specify what you
want to compile (*artifacts*) through subclasses of `CompilationArtifact`.
Each artifact can have a list of depenencies of other artifacts that it relies
on. Each artifact corresponds to exactly one file. If a file with a matching
name already exists, and all its dependencies are built and older than the file,
then the existing file will be reused.

For each file name, artifacts are singletons. You create artifacts by calling
the `new` class method of the appropriate class. This ensures that artifact
objects are uniqued, i.e., calling `new` twice with the same file name will
return the same object.

There is a special artifact for source files that do not need to get generated,
`SourceArtifact`. It is likely that in your compilation dependency graph,
the leaf nodes will be `SourceArtifact`s.

You specify how to generate (compile) an artifact through *rules*, which are
expressed as subclasses of `CompilationRule`. This class requires you to
implement two methods: `matches` and `compile`. During compilation, we will
call `matches` on the set of remaining artifacts to see if the given rule is
able to produce any of the artifacts not available yet. If this function
returns `True`, we will call `compile` on the rule to generate the artifact.
`compile` returns a new list of artifacts, which may be the same one as
before; however, if `matches()==True`, at least one of the artifacts in the
list must be made available after calling `compile()`.
"""

from abc import ABC, abstractmethod
from pathlib import Path
import os.path
import zlib
import logging
import subprocess
import importlib.util
from contextlib import nullcontext
from aie.extras.context import mlir_mod_ctx


# Global Functions
# ##########################################################################


def plan(rules, graph: CompilationArtifactGraph):
    if all(artifact.is_available() for artifact in graph):
        return []  # Everything has been compiled
    for rule in rules:
        if rule.matches(graph):
            commands, new_graph = rule.compile(graph)
            break
    else:
        raise RuntimeError(
            f"No matching rule to compile target(s): {', '.join(artifact.filename for artifact in graph)}"
        )
    return [(rule, commands, graph)] + plan(rules, new_graph)


def execute(plan):
    for rule, commands, _ in plan:
        logging.debug(f"Executing rule: {rule.__class__.__name__}")
        for command in commands:
            logging.debug(f"  Executing command: {command}")
            success = command.run()
            if not success:
                raise RuntimeError(f"Command failed: {command}")


def compile(rules, artifacts):
    plan_steps = plan(rules, artifacts)
    print(plan_steps)
    execute(plan_steps)


# Compilation Artifact Graph
# ##########################################################################


class CompilationArtifactGraph:
    def __init__(self, artifacts=None):
        self.artifacts = artifacts if artifacts is not None else []
    
    def __iter__(self):
        return iter(self.artifacts)
    
    def dfs(self):
        return self._traverse(True)
    
    def bfs(self):
        return self._traverse(False)
    
    def _traverse(self, dfs):
        visited = set()
        todo = self.artifacts.copy()
        while todo:
            artifact = todo.pop() if dfs else todo.pop(0)
            if artifact in visited:
                continue
            visited.add(artifact)
            todo.extend(artifact.dependencies)
            yield artifact

    def copy(self):
        return CompilationArtifactGraph(artifacts=self.artifacts.copy())
    
    def replace(self, old_artifact, new_artifact):
        for i, artifact in enumerate(self.artifacts):
            if artifact == old_artifact:
                self.artifacts[i] = new_artifact
            else:
                artifact.dependencies.replace(old_artifact, new_artifact)
        return self
    
    def populate_availability_from_filesystem(self):
        for artifact in self.artifacts:
            artifact.available = artifact.is_available_in_filesystem()
        
    def get_worklist(self, kind):
        """Return a list of artifacts of the given kind that can be built in the next step (dependencies available)."""
        return [
            artifact
            for artifact in self.artifacts.bfs()
            if isinstance(artifact, kind) 
            and not artifact.is_available() 
            and artifact.dependencies_available()
        ]


# Compilation Artifacts
# ##########################################################################


class CompilationArtifact(ABC):
    def __init__(self, filename, dependencies=None, available=False):
        self.filename = filename
        self.dependencies: CompilationArtifactGraph = CompilationArtifactGraph(artifacts=dependencies if dependencies is not None else [])
        self.available = available
        return self

    def __repr__(self):
        return f"{self.__class__.__name__}({self.filename})"

    def is_available(self):
        """'Conceptual' availability: during a dry-run or in the planning stage, available may be True even if the underlying file does not exist yet."""
        # If any of our dependencies' dependencies are outdated, this artifact is also outdated
        return self.available and self.dependencies_available()
    
    def dependencies_available(self):
        return all(d.is_available() for d in self.dependencies)
    
    def is_available_in_filesystem(self):
        """'Real' availability: checks if the underlying file exists and is up-to-date with respect to dependencies."""
        if not os.path.exists(self.filename):
            return False
        file_mtime = os.path.getmtime(self.filename)
        for dependency in self.dependencies:
            if not dependency.is_available_in_filesystem() or os.path.getmtime(dependency.filename) > file_mtime:
                return False
        return True


class SourceArtifact(CompilationArtifact):
    """Artifact representing a source file that does not need to be generated, is assumed to be there."""
    pass


class XclbinArtifact(CompilationArtifact):
    def __init__(
        self, filename, dependencies, kernel_name="MLIR_AIE", extra_flags=None, xclbin_input=None
    ):
        super().__init__(filename, dependencies)
        self.kernel_name = kernel_name
        self.extra_flags = extra_flags if extra_flags is not None else []
        self.xclbin_input = xclbin_input


class InstsBinArtifact(CompilationArtifact):
    def __init__(self, filename, dependencies, extra_flags=None):
        super().__init__(filename, dependencies)
        self.extra_flags = extra_flags if extra_flags is not None else []


class KernelObjectArtifact(CompilationArtifact):
    def __init__(self, filename, dependencies, extra_flags=None, rename_symbols=None):
        super().__init__(filename, dependencies)
        self.extra_flags = extra_flags if extra_flags is not None else []
        self.rename_symbols = rename_symbols if rename_symbols is not None else {}


class KernelArchiveArtifact(CompilationArtifact):
    pass


class PythonGeneratedMLIRArtifact(CompilationArtifact):
    def __init__(
        self,
        filename,
        import_path,
        callback_fn,
        callback_args=None,
        callback_kwargs=None,
        requires_context=False,
    ):
        self.callback_fn = callback_fn
        self.callback_args = callback_args if callback_args is not None else []
        self.callback_kwargs = callback_kwargs if callback_kwargs is not None else {}
        self.requires_context = requires_context
        super().__init__(filename, dependencies=[])


# Compilation Command
# ##########################################################################


class CompilationCommand(ABC):
    """An abstraction for anything that can be executed to physically produce artifacts."""
    @abstractmethod
    def run(self) -> bool:
        pass
    
    @abstractmethod
    def __repr__(self):
        pass


class ShellCompilationCommand(CompilationCommand):
    def __init__(self, command: list[str], cwd=None, env='copy'):
        self.command = command
        self.cwd = cwd
        if env == 'copy':
            env = os.environ.copy()
        self.env = env

    def run(self) -> bool:
        result = subprocess.run(
            self.command,
            capture_output=True,
            text=True,
            cwd=self.cwd,
            env=self.env,
        )
        return 0 == result.returncode

    def __repr__(self):
        return f"Shell({self.command})"


class PythonCallbackCompilationCommand(CompilationCommand):
    def __init__(self, callback):
        self.callback = callback

    def run(self) -> bool:
        return bool(self.callback())

    def __repr__(self):
        return f"PythonCallback({self.callback})"


# Compilation Rules
# ##########################################################################


class CompilationRule(ABC):
    """A compilation rule is applied to a artifact graph, producing compilation commands and a transformed artifact graph."""

    @abstractmethod
    def matches(self, artifact: CompilationArtifactGraph) -> bool:
        """Return true if this rule can be applied to any artifact in the artifact graph."""
        pass
    
    @abstractmethod
    def compile(
        self, artifacts: CompilationArtifactGraph
    ) -> list[CompilationCommand]:
        """Apply this rule to the artifact graph, returning compilation commands. This should modify the artifact graph in-place to reflect the newly generated artifacts."""
        pass


class GenerateMLIRFromPythonCompilationRule(CompilationRule):
    def matches(self, graph):
        return any(
            isinstance(artifact, PythonGeneratedMLIRArtifact)
            and len(artifact.dependencies) == 1
            and isinstance(artifact.dependencies[0], SourceArtifact)
            and artifact.dependencies_available()
            for artifact in graph.bfs(only_unavailable=True)
        )

    def compile(self, graph):
        """Generate MLIR from a Python callback that uses the MLIR bindings"""
        commands = []
        for i, artifact in enumerate(graph.bfs(only_unavailable=True)):
            if not isinstance(artifact, PythonGeneratedMLIRArtifact):
                continue
            assert len(artifact.dependencies) == 1 and isinstance(artifact.dependencies[0], SourceArtifact), "PythonGeneratedMLIRArtifact must depend on exactly one SourceArtifact"
            import_path = Path(artifact.dependencies[0].filename)
            new_artifact = SourceArtifact.new(artifact.filename)
            callback = lambda: self.generate_mlir(new_artifact, import_path, artifact.callback_fn, artifact.callback_args, artifact.callback_kwargs, artifact.requires_context)
            commands.append(PythonCallbackCompilationCommand(callback))
            new_artifact.available = True
            graph.replace(artifact, new_artifact)
        return commands
    
    @staticmethod 
    def generate_mlir(output_artifact, import_path, callback_fn, callback_args=None, callback_kwargs=None, requires_context=False):
        # Import the Python source file
        spec = importlib.util.spec_from_file_location(
            Path(import_path).name, import_path
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # We only initiate an MLIR context if requested; otherwise, it is expected that the callback creates the context
        ctx_callback = lambda: (
            mlir_mod_ctx() if requires_context else nullcontext()
        )
        with ctx_callback() as ctx:
            callback_function = getattr(module, callback_fn)
            mlir_code = callback_function(
                *callback_args, **callback_kwargs
            )
        # Stringify the generated MLIR
        if requires_context:
            mlir_code = str(ctx.module)
        else:
            mlir_code = str(mlir_code)

        with open(output_artifact.filename, "w") as f:
            f.write(mlir_code)


class AieccXclbinInstsCompilationRule(CompilationRule):
    def __init__(self, build_dir, peano_dir, mlir_aie_dir, *args, **kwargs):
        self.build_dir = build_dir
        self.aiecc_path = Path(mlir_aie_dir) / "bin" / "aiecc.py"
        self.peano_dir = peano_dir
        super().__init__(*args, **kwargs)

    def matches(self, graph):
        return any(graph.get_worklist((XclbinArtifact, InstsBinArtifact)))

    def compile(self, graph):
        # If there are both xclbin and insts.bin targets based on the same source MLIR code, we can combine them into one single `aiecc.py` invocation.
        mlir_sources = set()
        mlir_sources_to_xclbins = {}
        mlir_sources_to_insts = {}
        worklist = graph.get_worklist((XclbinArtifact, InstsBinArtifact))
        for artifact in worklist:
            mlir_dependency = artifact.mlir_input
            if isinstance(artifact, XclbinArtifact):
                mlir_sources_to_xclbins.setdefault(mlir_dependency, []).append(artifact)
            elif isinstance(artifact, InstsBinArtifact):
                mlir_sources_to_insts.setdefault(mlir_dependency, []).append(artifact)

        commands = []
        # Now we know for each mlir source if we need to generate an xclbin, an insts.bin or both for it
        for mlir_source in mlir_sources:
            compile_cmd = [
                "python",
                str(self.aiecc_path),
                "--no-compile-host",
                "--no-xchesscc",
                "--no-xbridge",
                "--peano",
                str(self.peano_dir),
                "--dynamic-objFifos",
            ]
            do_compile_xclbin = mlir_source in mlir_sources_to_xclbins
            do_compile_insts_bin = mlir_source in mlir_sources_to_insts
            if do_compile_xclbin:
                first_xclbin = mlir_sources_to_xclbins[mlir_source][
                    0
                ]  # TODO: this does not handle the case of multiple xclbins with different kernel names or flags from the same MLIR
                compile_cmd += first_xclbin.extra_flags + [
                    "--aie-generate-xclbin",
                    "--xclbin-name=" + first_xclbin.filename,
                    "--xclbin-kernel-name=" + first_xclbin.kernel_name,
                ]
                if first_xclbin.xclbin_input is not None:
                    compile_cmd += [
                        "--xclbin-input=" + first_xclbin.xclbin_input.filename
                    ]
            if do_compile_insts_bin:
                first_insts_bin = mlir_sources_to_insts[mlir_source][
                    0
                ]  # TODO: this does not handle the case of multiple insts.bins with different flags from the same MLIR
                if not do_compile_xclbin:
                    compile_cmd += ["--no-compile"]
                compile_cmd += first_insts_bin.extra_flags + [
                    "--aie-generate-npu",
                    "--npu-insts-name=" + first_insts_bin.filename,
                ]
            compile_cmd += [mlir_source.filename]

            ShellCompilationCommand(compile_cmd, cwd=str(self.build_dir))

            # There may be multiple targets that require an xclbin/insts.bin from the same MLIR with different names; copy them
            for sources_to in [mlir_sources_to_xclbins, mlir_sources_to_insts]:
                if sources_to.get(mlir_source, [])[1:]:
                    copy_src = sources_to[mlir_source][0]
                    for copy_dest in sources_to[mlir_source][1:]:
                        shutil.copy(copy_src.filename, copy_dest.filename)
        
        # Update graph
        for artifact in worklist:
            artifact.available = True

        return artifacts


class PeanoCompilationRule(CompilationRule):
    def __init__(self, peano_dir, mlir_aie_dir, *args, **kwargs):
        self.peano_dir = peano_dir
        self.mlir_aie_dir = mlir_aie_dir
        super().__init__(*args, **kwargs)

    def matches(self, artifacts):
        return any(
            isinstance(artifact, KernelObjectArtifact)
            and all(
                isinstance(dependency, SourceArtifact) and dependency.is_available()
                for dependency in artifact.dependencies
            )
            for artifact in artifacts
        )

    def compile(self, artifacts):
        clang_path = Path(self.peano_dir) / "bin" / "clang++"
        include_path = Path(self.mlir_aie_dir) / "include"

        for artifact in artifacts:
            if not isinstance(artifact, KernelObjectArtifact):
                continue

            if len(artifact.dependencies) != 1:
                raise RuntimeError(
                    "Expected exactly one dependency (the C source code) for KernelObjectArtifact"
                )
            source_file = artifact.dependencies[0]
            if not isinstance(source_file, SourceArtifact):
                raise RuntimeError(
                    "Expected KernelObject dependency to be a C source file"
                )

            cmd = (
                [
                    str(clang_path),
                    "-O2",
                    "-std=c++20",
                    "--target=aie2p-none-unknown-elf",
                    "-Wno-parentheses",
                    "-Wno-attributes",
                    "-Wno-macro-redefined",
                    "-Wno-empty-body",
                    "-Wno-missing-template-arg-list-after-template-kw",
                    f"-I{str(include_path)}",
                ]
                + artifact.extra_flags
                + ["-c", source_file.filename, "-o", artifact.filename]
            )
            logging.debug(f"Running compilation command: {' '.join(cmd)}")

            if self.dry_run is None:
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode != 0:
                    raise RuntimeError(f"Compilation failed: {result.stderr}")
                logging.debug(f"Successfully compiled: {artifact.filename}")
            else:
                artifact.fake_available = True
                self.dry_run.append(" ".join(cmd))

            if artifact.rename_symbols:
                self._rename_symbols(artifact)

        return artifacts

    def _rename_symbols(self, artifact):
        objcopy_path = "llvm-objcopy-18"
        cmd = [
            objcopy_path,
        ]
        for old_sym, new_sym in artifact.rename_symbols.items():
            cmd += [
                "--redefine-sym",
                f"{old_sym}={new_sym}",
            ]
        cmd += [artifact.filename]

        logging.debug(f"Running renaming command: {' '.join(cmd)}")
        if self.dry_run is None:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                logging.info(f"Successfully renamed symbols in: {artifact.filename}")
            else:
                raise RuntimeError(f"Symbol renaming failed: {result.stderr}")
        else:
            artifact.fake_available = True
            self.dry_run.append(" ".join(cmd))


class ArchiveCompilationRule(CompilationRule):
    def __init__(self, peano_dir, *args, **kwargs):
        self.peano_dir = peano_dir
        super().__init__(*args, **kwargs)

    def matches(self, artifacts):
        return any(
            isinstance(artifact, KernelArchiveArtifact) and len(artifact.dependencies) > 0
            for artifact in artifacts
        )

    def compile(self, artifacts):
        """Create an archive (.a) from compiled object files"""
        for artifact in artifacts:
            if not isinstance(artifact, KernelArchiveArtifact):
                continue

            # Get archive filename from method
            archive_path = artifact.filename
            object_files = [
                dep.filename
                for dep in artifact.dependencies
                if isinstance(dep, KernelObjectArtifact)
            ]

            # Try to find ar tool from PEANO, then system
            ar_path = None

            if self.peano_dir:
                # Peano has llvm-ar for archiving
                peano_ar = Path(self.peano_dir) / "bin" / "llvm-ar"
                if os.path.exists(peano_ar):
                    ar_path = peano_ar

            if ar_path is None:
                raise RuntimeError(
                    "Could not find 'ar' tool in PEANO installation or system PATH"
                )

            cmd = [str(ar_path), "rcs", archive_path] + object_files

            if self.dry_run is None:
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode == 0:
                    logging.debug(
                        f"Successfully created archive: {Path(archive_path).name}"
                    )
                else:
                    raise RuntimeError(f"Archive creation failed: {result.stderr}")
            else:
                artifact.fake_available = True
                self.dry_run.append(" ".join(cmd))

        return artifacts
