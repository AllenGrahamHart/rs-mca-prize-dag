#!/usr/bin/env python3
"""w7 audit Modal wrapper: rebuild the node tree in /work and run the
weight-4 verifiers (ledger and/or primes) from their tree positions.

Files arrive flat in cwd (/work): verify_ledger.py, verify_primes.py,
dli_wcl_weight4_section_result.json.gz, dli_wcl_weight4_prime_cert_result.json.gz.
argv[1] in {ledger, primes, both}.
"""
import os
import shutil
import subprocess
import sys

WHICH = sys.argv[1] if len(sys.argv) > 1 else "both"
NODE = "background/nodes/dli_wcl_weight4_ambient_exclusion"
EXP = "experiments/prize_resolution"
os.makedirs(NODE, exist_ok=True)
os.makedirs(EXP, exist_ok=True)
for name, dest in (
    ("verify_ledger.py", NODE),
    ("verify_primes.py", NODE),
    ("dli_wcl_weight4_section_result.json.gz", EXP),
    ("dli_wcl_weight4_prime_cert_result.json.gz", EXP),
):
    if os.path.exists(name):
        shutil.copy(name, os.path.join(dest, name))

rc = 0
if WHICH in ("ledger", "both"):
    r = subprocess.run(["python3", os.path.join(NODE, "verify_ledger.py")],
                       capture_output=True, text=True)
    print(r.stdout, end="")
    if r.stderr:
        print(r.stderr[-4000:], end="")
    rc |= r.returncode
if WHICH in ("primes", "both"):
    r = subprocess.run(["python3", os.path.join(NODE, "verify_primes.py")],
                       capture_output=True, text=True)
    print(r.stdout, end="")
    if r.stderr:
        print(r.stderr[-4000:], end="")
    rc |= r.returncode
print(f"W7_WRAP_DONE which={WHICH} rc={rc}")
sys.exit(rc)
