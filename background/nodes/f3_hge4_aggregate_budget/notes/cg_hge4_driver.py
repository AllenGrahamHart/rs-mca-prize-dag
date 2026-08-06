#!/usr/bin/env python3
"""cg_hge4_driver: FIRST falsification attempt on f3_hge4_aggregate_budget.

Runs the C enumerator over the row/width grid, shards big cells to respect
the state cap, collects exact per-(n,p,h) anchored trade counts and the full
non-toral trade dumps for stripping.

Grid:
  n=16 (H_max = n/2 = 8): h = 4..8, boundary primes 257,337,353,401,433,449
       -> COMPLETE h>=4 band aggregates (H_max = 8), plus control p=17.
  n=32 (H_max = 16): h = 4..8 at 1153 (SP-CENSUS-2 row), 1217, 1249, 1409,
       32801 (far prime ~ n^3); h = 9..16 out of state-cap -> certified
       sub-band slice per A4 semantics.
  n=64 (H_max = 32): h = 4,5 at 4289, 4481, 4673, 4801 (boundary);
       h >= 6 out of state-cap -> slice.
"""
from __future__ import annotations

import json
import subprocess

SCRATCH = ("/tmp/claude-1000/-home-u2470931-smooth-read-solomin/"
           "d53e6c57-2281-4b35-b085-8a669b4db5f5/scratchpad")


def shards(n, h):
    """Probe-side shards [lo,hi] keeping hash+probe states < 10^7 per run."""
    from math import comb
    hashed = comb(n - 1, h - 1)
    total_hi = n - h
    out = []
    lo = 1
    budget = 10**7 - hashed
    assert budget > 0, (n, h)
    while lo <= total_hi:
        acc = 0
        hi = lo
        while hi <= total_hi:
            nxt = comb(n - 1 - hi, h - 1)
            if acc + nxt > budget and hi > lo:
                break
            acc += nxt
            hi += 1
        out.append((lo, hi - 1))
        lo = hi
    return out


def run_cell(n, p, h):
    total = {"trades": 0, "toral": 0, "nontoral": 0, "hashed": 0, "probed": 0}
    dumps = []
    plan = shards(n, h)
    for lo, hi in plan:
        r = subprocess.run([f"{SCRATCH}/cg_trades", str(n), str(p), str(h),
                            str(lo), str(hi), "2000000"],
                           capture_output=True, text=True, check=True)
        s = r.stderr
        for key in ("trades", "toral", "nontoral", "hashed", "probed"):
            total[key] += int(s.split(f"{key}=")[1].split()[0])
        assert "dumpcap=ok" in s, (n, p, h, s)
        for ln in r.stdout.splitlines():
            if ln.startswith("T "):
                a, b = ln[2:].split()
                dumps.append([list(map(int, a.split(","))),
                              list(map(int, b.split(",")))])
    total["shards"] = len(plan)
    return total, dumps


def main():
    grid = []
    for p in (17, 257, 337, 353, 401, 433, 449):
        for h in (4, 5, 6, 7, 8):
            grid.append((16, p, h))
    for p in (1153, 1217, 1249, 1409, 32801):
        for h in (4, 5, 6, 7, 8):
            grid.append((32, p, h))
    for p in (4289, 4481, 4673, 4801):
        for h in (4, 5):
            grid.append((64, p, h))

    results = []
    for n, p, h in grid:
        total, dumps = run_cell(n, p, h)
        rec = {"n": n, "p": p, "h": h, **total, "nontoral_trades": dumps}
        results.append(rec)
        print(f"n={n} p={p} h={h} shards={total['shards']} "
              f"trades={total['trades']} toral={total['toral']} "
              f"nontoral={total['nontoral']}", flush=True)
    with open(f"{SCRATCH}/cg_hge4_results.json", "w") as f:
        json.dump(results, f)
    print("banked to cg_hge4_results.json")


if __name__ == "__main__":
    main()
