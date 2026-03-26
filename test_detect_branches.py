import torch, gc, time
from iron.common import AIEContext
from iron.applications.yolov8n.detect import DetectBranch
from aie.utils import DefaultNPURuntime

torch.manual_seed(42)

def cleanup():
    DefaultNPURuntime._context_cache.clear()
    DefaultNPURuntime._insts_cache.clear()
    gc.collect()

branches = [
    ('reg_p3', 64, 64, 64, 80, 80),
    ('reg_p4', 128, 64, 64, 40, 40),
    ('reg_p5', 256, 64, 64, 20, 20),   # IC streaming on cv1
    ('cls_p3', 64, 80, 80, 80, 80),    # IC streaming on cv2
    ('cls_p4', 128, 80, 80, 40, 40),
    ('cls_p5', 256, 80, 80, 20, 20),   # IC streaming on cv1
]

results = {}

for name, c_in, c_mid, c_out, h, w in branches:
    print(f'\n--- {name} ({c_in}->{c_mid}->{c_out} {h}x{w}) ---')
    try:
        ctx = AIEContext()
        branch = DetectBranch(c_in, c_mid, c_out, h, w, context=ctx)
        t0 = time.time()
        ctx.compile_all()
        tc = time.time() - t0
        print(f'  Compiled: {tc:.1f}s')

        # Random weights
        branch.load_weights(
            torch.randn(c_mid, c_in, 3, 3, dtype=torch.bfloat16) * 0.01,
            torch.randn(c_mid, dtype=torch.bfloat16) * 0.01,
            torch.randn(c_mid, c_mid, 3, 3, dtype=torch.bfloat16) * 0.01,
            torch.randn(c_mid, dtype=torch.bfloat16) * 0.01,
            torch.randn(c_out, c_mid, 1, 1, dtype=torch.bfloat16) * 0.01,
            torch.randn(c_out, dtype=torch.bfloat16) * 0.01,
        )
        ctx.prepare_runtime()

        x = torch.randn(1, c_in, h, w, dtype=torch.bfloat16)
        t0 = time.time()
        out = branch.forward(x)
        te = time.time() - t0

        ok = out.shape == (1, c_out, h, w) and torch.isfinite(out).all().item()
        print(f'  Output: {out.shape} finite={torch.isfinite(out).all().item()} exec={te:.3f}s')
        status = "PASS" if ok else "FAIL"
        print(f'  {status}')
        results[name] = status
        cleanup()
    except Exception as e:
        print(f'  FAIL: {e}')
        import traceback; traceback.print_exc()
        results[name] = "FAIL"
        cleanup()

print('\n=== DETECT HEAD SUMMARY ===')
for name, status in results.items():
    ic_note = ""
    if name in ('reg_p5', 'cls_p5'):
        ic_note = " (IC streaming cv1)"
    elif name == 'cls_p3':
        ic_note = " (IC streaming cv2)"
    print(f'  {name}: {status}{ic_note}')

all_pass = all(s == "PASS" for s in results.values())
print(f'\nAll branches: {"PASS" if all_pass else "SOME FAILED"}')
