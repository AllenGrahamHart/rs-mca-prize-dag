#!/usr/bin/env python3
"""qra_anchor: replay the banked (path-repaired) qrl_verify.py and compare its
stdout and regenerated coverage table byte-for-byte against the packet copies.
Runs in /work with all files flat."""
import subprocess
import sys

banked_table = open("qrl_coverage_table.md").read()   # packet copy (pre-read)
banked_out = open("qrl_verify_output.txt").read()

r = subprocess.run(["python3", "qrl_verify.py"], capture_output=True, text=True)
print(r.stdout, end="")
if r.stderr:
    print("--- verifier stderr ---\n" + r.stderr)

fresh_table = open("qrl_coverage_table.md").read()    # overwritten by S3
same_out = (r.stdout == banked_out)
same_tab = (fresh_table == banked_table)
print(f"ANCHOR: verifier exit={r.returncode}; stdout identical to banked: {same_out};"
      f" regenerated coverage table identical to banked: {same_tab}")
sys.exit(0 if (r.returncode == 0 and same_out and same_tab) else 1)
