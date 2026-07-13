#!/usr/bin/env python3
"""Node-level verifier for petal_g1_layer_maps (clause (P), PROVED
2026-07-13). Fail-closed wrapper: runs the banked packet verifier
(cp_verify.py, 62 checks incl. 4 required-to-trip mutations and the
#174 nonemptiness repair) and the independent audit battery
(cpa_checks.py, 37 checks incl. mutations NM1-NM3). Exit 0 iff both
suites pass in full."""
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
PACKET = HERE / "notes" / "cp_packet_20260713"
SUITES = [("cp_verify.py", "TOTAL: 62 PASS, 0 FAIL"),
          ("cpa_checks.py", "AUDIT TOTAL: 37 PASS, 0 FAIL")]


def main() -> int:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    for name, want in SUITES:
        r = subprocess.run([sys.executable, str(PACKET / name)],
                           capture_output=True, text=True, env=env)
        tail = "\n".join(r.stdout.strip().splitlines()[-3:])
        if r.returncode != 0 or want not in r.stdout:
            print(f"[FAIL] {name}: exit {r.returncode}; expected "
                  f"'{want}'\n{tail}\n{r.stderr[-2000:]}")
            return 1
        print(f"[PASS] {name}: {want}")
    print("petal_g1_layer_maps: ALL SUITES PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
