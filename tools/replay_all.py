#!/usr/bin/env python3
"""Replay every verifier in the tree. The machine layer of the full audit:
a certificate that no longer passes is a status lie. Sequential (RAM-safe),
per-script timeout, honest TIMEOUT reporting. Writes nodes/REPLAY_LEDGER.md;
exit 1 on any FAIL."""
import glob, os, subprocess, sys, time

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
TIMEOUT = 600
scripts = sorted(set(
    glob.glob(os.path.join(ROOT, "nodes", "*", "verify*.py")) +
    glob.glob(os.path.join(ROOT, "nodes", "*", "notes", "verify*.py")) +
    glob.glob(os.path.join(ROOT, "tools", "verify_*.py"))))
rows, failed = [], 0
for s in scripts:
    rel = os.path.relpath(s, ROOT)
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, s], capture_output=True,
                           text=True, timeout=TIMEOUT, cwd=ROOT)
        ok = r.returncode == 0
        verdict = "PASS" if ok else "FAIL"
    except subprocess.TimeoutExpired:
        ok, verdict = False, "TIMEOUT"
    dt = time.time() - t0
    if not ok:
        failed += 1
    rows.append(f"| {rel} | {verdict} | {dt:.1f}s |")
    print(f"{verdict:8} {dt:7.1f}s  {rel}", flush=True)
with open(os.path.join(ROOT, "nodes", "REPLAY_LEDGER.md"), "w") as f:
    f.write("# Replay ledger (machine audit layer)\n\n"
            f"{len(scripts)} verifiers, {failed} not passing.\n\n"
            "| script | verdict | time |\n|---|---|---|\n" + "\n".join(rows) + "\n")
print(f"\n{len(scripts)} verifiers, {failed} not passing")
sys.exit(1 if failed else 0)
