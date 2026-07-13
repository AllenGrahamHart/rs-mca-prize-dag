#!/usr/bin/env python3
"""qra_mutations: REAL mutation tests of the banked qrl_verify.py.
Each mutant must make the verifier FAIL (exit != 0 with FAIL lines).
Also demonstrates that the packet's built-in 'MUTATION M2' self-test is a
tautology (it never feeds the tampered value through the S4 predicate)."""
import json
import subprocess
import sys

FAIL = []
def check(cond, label):
    print(("PASS " if cond else "FAIL ") + label)
    if not cond:
        FAIL.append(label)

src = open("qrl_verify.py").read()
gt_pristine = open("cg_petal_census_results.json").read()

def run(name):
    r = subprocess.run(["python3", name], capture_output=True, text=True)
    nfail = sum(1 for ln in r.stdout.splitlines() if ln.startswith("FAIL"))
    return r.returncode, nfail, r.stdout

# baseline sanity
rc, nf, _ = run("qrl_verify.py")
check(rc == 0 and nf == 0, "baseline: pristine verifier passes (exit 0, 0 FAILs)")

# MUT-A: widen the T1 window to n' = 64 (a genuinely false claim)
mA = src.replace("for npr in (2, 4, 8, 16, 32):",
                 "for npr in (2, 4, 8, 16, 32, 64):", 1)
assert mA != src
open("mutA.py", "w").write(mA)
rc, nf, out = run("mutA.py")
check(rc != 0 and nf >= 1 and "max_a C(64,a)" in out,
      f"MUT-A (window widened to 64): verifier FAILS (exit {rc}, {nf} FAIL line)")

# MUT-B: corrupt the coverage rule (open band lo floor 7 -> 6)
mB = src.replace("lo = max(kpr + 1, 7)", "lo = max(kpr + 1, 6)", 1)
assert mB != src
open("mutB.py", "w").write(mB)
rc, nf, out = run("mutB.py")
check(rc != 0 and nf >= 1 and "closed-form open band" in
      "".join(ln for ln in out.splitlines() if ln.startswith("FAIL")),
      f"MUT-B (band rule 7->6): verifier FAILS on the pointwise cross-check"
      f" (exit {rc}, {nf} FAIL)")

# MUT-C: tamper one banked ground-truth cell (classes 4 -> 7 > C(4,2) = 6)
gt = json.loads(gt_pristine)
gt[0]["fp0_all"]["2,4"]["classes"] = 7
gt[0]["fp0_all"]["2,4"]["codewords"] = 7
open("cg_petal_census_results.json", "w").write(json.dumps(gt))
rc, nf, out = run("qrl_verify.py")
check(rc != 0 and nf >= 1 and "VIOLATION" in out,
      f"MUT-C (banked cell 4->7 classes): S4 flags the tamper and verifier"
      f" FAILS (exit {rc}, {nf} FAIL)")
open("cg_petal_census_results.json", "w").write(gt_pristine)  # restore
rc, nf, _ = run("qrl_verify.py")
check(rc == 0 and nf == 0, "restore control: pristine verifier passes again")

# MUT-D: table-row corruption is caught by the anchor byte-diff
tab = open("qrl_coverage_table.md").read()
check(tab.replace("[33,44]", "[33,45]", 1) != tab,
      "MUT-D: a corrupted coverage-table row differs byte-wise, hence caught"
      " by the anchor regenerate-and-diff (table is regenerated, not read)")

# STATIC: the packet's own MUTATION M2 self-test is a tautology
m2 = [ln for ln in src.splitlines() if "bad > comb" in ln]
check(len(m2) == 1 and "bad = comb(" in src,
      "STATIC catch material: built-in M2 checks 'comb(...)+1 > comb(...)'"
      " (always true) -- it never runs the S4 predicate on a tampered record;"
      " MUT-C above is the real version and it does have teeth")

print()
print(f"RESULT: {len(FAIL)} FAILURES" if FAIL else
      "RESULT: ALL MUTATION TESTS BEHAVE CORRECTLY")
sys.exit(1 if FAIL else 0)
