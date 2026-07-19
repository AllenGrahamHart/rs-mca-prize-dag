#!/usr/bin/env python3
"""Unit-test the M4 verifier's catch-#162 detector on the two states that
cannot be exercised against the live (read-only) repo: the post-surgery
clean state and a malformed half-deleted state."""
import importlib.util
import json
import sys
from pathlib import Path

SC = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "m4", SC / "m4_assembly_verifier.py")
m4 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m4)

real_dag = json.loads((m4.REPO / "dag.json").read_text())
node = next(n for n in real_dag["nodes"]
            if n["id"] == "dli_prime_weighted_large_block_support")
stmt = node["statement"]

# reproduce the spec'd deletion
start, end = 6673, 7286
frag = stmt[start:end]
assert frag.startswith("==gridDP PASS; full log banked")
assert frag.endswith("pending maintainer review. ")
clean = stmt[:start] + stmt[end:]
# malformed: tail marker of the DUPLICATE destroyed but head kept
malformed = stmt[:end - 40] + "XX" + stmt[end:]
# also destroy the ORIGINAL's tail marker so no tail exists after the
# duplicate head (the truly inconsistent state)
malformed = malformed.replace("PROMOTION-ELIGIBLE pending maintainer review.",
                              "PROMOTION-ELIGIBLE pending review-X.")


def with_statement(s: str, tmp: Path) -> None:
    d = json.loads(json.dumps(real_dag))
    n = next(x for x in d["nodes"]
             if x["id"] == "dli_prime_weighted_large_block_support")
    n["statement"] = s
    tmp.mkdir(parents=True, exist_ok=True)
    (tmp / "dag.json").write_text(json.dumps(d))


fails = 0

# state 1: current (duplicate present) -> PASS with deletion-owed info
m4._failures.clear()
m4.check_catch_162()
if m4._failures:
    print("FAIL: current-state detector failed", m4._failures)
    fails += 1
else:
    print("OK: current state detected as spec-matching duplicate")

# state 2: post-surgery clean
tmp = SC / "m4_tmp_repo_clean"
with_statement(clean, tmp)
m4.REPO = tmp
m4._failures.clear()
m4.check_catch_162()
if m4._failures:
    print("FAIL: clean-state invariants rejected", m4._failures)
    fails += 1
else:
    print("OK: post-surgery clean state passes its invariants")

# state 3: malformed half-surgery -> must raise M4Reject
tmp2 = SC / "m4_tmp_repo_malformed"
with_statement(malformed, tmp2)
m4.REPO = tmp2
m4._failures.clear()
try:
    m4.check_catch_162()
    print("FAIL: malformed state not rejected", m4._failures)
    fails += 1
except m4.M4Reject as e:
    print(f"OK: malformed state rejected fail-closed ({e})")

print("RESULT:", "ALL OK" if fails == 0 else f"{fails} FAILURES")
sys.exit(1 if fails else 0)
