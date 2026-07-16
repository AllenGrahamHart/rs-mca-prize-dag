#!/usr/bin/env python3
"""w8 audit driver: replays every verifier audited in wave-8 from the pinned mini-tree.

Usage: tools/ramguard tiny -- python3 w8_checks.py  (run with cwd anywhere; paths absolute)
Pin: ae2e5dd54bdcf2b6b5c7b3d8a031184196720962 (v4). Mini-tree: w8_tree/ beside this script,
populated via `git show <pin>:<path>` only. Standalone verifier copies in w8_pma_verifiers/.
"""
import subprocess, sys, pathlib

SCR = pathlib.Path(__file__).resolve().parent
TREE = SCR / "w8_tree"
STANDALONE = sorted((SCR / "w8_pma_verifiers").glob("*.py"))
TREE_VERIFIERS = [
    "background/nodes/petal_reserve_rich_fiber_reduction/verify.py",
    "background/nodes/pma_petal_pattern_root_pinning_ledger/verify.py",
    "background/nodes/pma_saturated_mixed_support_kernel/verify.py",
    "background/nodes/pma_sigma_one_post_top_allowance/verify.py",
    "background/nodes/pma_sigma_one_variable_defect_exact_hit_floor/verify.py",
    "critical/nodes/rate_half_cyclic_rotated_prefix_floor/verify.py",
    "critical/nodes/rate_half_cyclic_rotated_prefix_floor/verify_audit.py",
    "background/nodes/rate_half_fixed_tail_prefix_floor/verify.py",
    "critical/nodes/imgfib/verify_scope_repair.py",
]
EXTRA = [SCR / "w8_ratehalf_crosscheck.py"]

def run(path, cwd):
    r = subprocess.run([sys.executable, str(path)], cwd=str(cwd),
                       capture_output=True, text=True, timeout=280)
    tail = (r.stdout + r.stderr).strip().splitlines()[-1:] or [""]
    return r.returncode, tail[0]

def main():
    failures = 0
    for p in STANDALONE:
        # skip the 5 that need the tree (they are re-run from TREE below)
        if p.name.split("__")[0] in {v.split("/")[2] for v in TREE_VERIFIERS}:
            continue
        rc, line = run(p, SCR)
        print(("PASS" if rc == 0 else "FAIL"), p.name, "|", line)
        failures += rc != 0
    for v in TREE_VERIFIERS:
        rc, line = run(TREE / v, TREE)
        print(("PASS" if rc == 0 else "FAIL"), v, "|", line)
        failures += rc != 0
    for p in EXTRA:
        rc, line = run(p, SCR)
        print(("PASS" if rc == 0 else "FAIL"), p.name, "|", line)
        failures += rc != 0
    print("W8_CHECKS", "ALL_PASS" if failures == 0 else f"FAILURES={failures}")
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
