"""Test all 6 detect head branches together, simulating full detect head with neck outputs."""
import torch, gc, time
from iron.common import AIEContext
from iron.applications.yolov8n.detect import DetectBranch
from aie.utils import DefaultNPURuntime

torch.manual_seed(42)

def cleanup():
    DefaultNPURuntime._context_cache.clear()
    DefaultNPURuntime._insts_cache.clear()
    gc.collect()

# Neck output shapes for YOLOv8n at 640x640
# P3: 64ch 80x80, P4: 128ch 40x40, P5: 256ch 20x20
neck_outputs = {
    'p3': torch.randn(1, 64, 80, 80, dtype=torch.bfloat16),
    'p4': torch.randn(1, 128, 40, 40, dtype=torch.bfloat16),
    'p5': torch.randn(1, 256, 20, 20, dtype=torch.bfloat16),
}

# All 6 detect branches
branch_configs = [
    # (name, c_in, c_mid, c_out, h, w, neck_key)
    ('reg_p3', 64, 64, 64, 80, 80, 'p3'),
    ('reg_p4', 128, 64, 64, 40, 40, 'p4'),
    ('reg_p5', 256, 64, 64, 20, 20, 'p5'),
    ('cls_p3', 64, 80, 80, 80, 80, 'p3'),
    ('cls_p4', 128, 80, 80, 40, 40, 'p4'),
    ('cls_p5', 256, 80, 80, 20, 20, 'p5'),
]

results = {}
all_outputs = {}

print("=== FULL DETECT HEAD TEST (all 6 branches, neck-shaped inputs) ===\n")

for name, c_in, c_mid, c_out, h, w, neck_key in branch_configs:
    print(f'--- {name} ({c_in}->{c_mid}->{c_out} {h}x{w}) ---')
    try:
        ctx = AIEContext()
        branch = DetectBranch(c_in, c_mid, c_out, h, w, context=ctx)
        t0 = time.time()
        ctx.compile_all()
        tc = time.time() - t0
        print(f'  Compiled: {tc:.1f}s')

        branch.load_weights(
            torch.randn(c_mid, c_in, 3, 3, dtype=torch.bfloat16) * 0.01,
            torch.randn(c_mid, dtype=torch.bfloat16) * 0.01,
            torch.randn(c_mid, c_mid, 3, 3, dtype=torch.bfloat16) * 0.01,
            torch.randn(c_mid, dtype=torch.bfloat16) * 0.01,
            torch.randn(c_out, c_mid, 1, 1, dtype=torch.bfloat16) * 0.01,
            torch.randn(c_out, dtype=torch.bfloat16) * 0.01,
        )
        ctx.prepare_runtime()

        x = neck_outputs[neck_key]
        t0 = time.time()
        out = branch.forward(x)
        te = time.time() - t0

        ok = out.shape == (1, c_out, h, w) and torch.isfinite(out).all().item()
        print(f'  Output: {out.shape} finite={torch.isfinite(out).all().item()} exec={te:.3f}s')
        status = "PASS" if ok else "FAIL"
        print(f'  {status}')
        results[name] = status
        all_outputs[name] = out
        cleanup()
    except Exception as e:
        print(f'  FAIL: {e}')
        import traceback; traceback.print_exc()
        results[name] = "FAIL"
        cleanup()

# Summarize detect head outputs (what would be concatenated for post-processing)
print('\n=== DETECT HEAD OUTPUT SUMMARY ===')
for scale in ['p3', 'p4', 'p5']:
    reg_name = f'reg_{scale}'
    cls_name = f'cls_{scale}'
    reg_ok = results.get(reg_name, 'FAIL')
    cls_ok = results.get(cls_name, 'FAIL')
    reg_shape = all_outputs[reg_name].shape if reg_name in all_outputs else 'N/A'
    cls_shape = all_outputs[cls_name].shape if cls_name in all_outputs else 'N/A'
    print(f'  {scale}: reg={reg_ok} {reg_shape}  cls={cls_ok} {cls_shape}')

all_pass = all(s == "PASS" for s in results.values())
print(f'\nFull detect head: {"PASS" if all_pass else "SOME FAILED"} ({sum(1 for s in results.values() if s == "PASS")}/6)')
