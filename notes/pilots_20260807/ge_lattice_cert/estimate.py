#!/usr/bin/env python3
"""Cost projection from the MEASURED Gram-Schmidt profile (not the GSA
idealisation).  Named functional:

  FPEST(cell) = sum_k V_k(R) / prod_{i>=n-k} ||b*_i||

with ||b*_i|| taken from the actual reduced basis in state/CELL.lll.json.
This is the standard Gaussian-heuristic node count for a COMPLETE
Fincke-Pohst enumeration and is what the run should be compared against.
"""
import json
import math
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import latlib as LL                                       # noqa: E402

STATE = os.path.join(HERE, "state")


def log2V(k, R):
    return ((k / 2.0) * math.log(math.pi) + k * math.log(R)
            - math.lgamma(k / 2.0 + 1.0)) / math.log(2.0)


def est(prof, R):
    """prof = [log2 ||b*_i||^2]; returns (log2 total, peak k, per-k list)."""
    n = len(prof)
    tot = -1e18
    peak = (0, -1e18)
    per = []
    for k in range(1, n + 1):
        s = sum(prof[i] / 2.0 for i in range(n - k, n))
        hk = log2V(k, R) - s
        per.append(hk)
        if hk > peak[1]:
            peak = (k, hk)
        tot = max(tot, hk) + math.log2(1 + 2 ** (min(tot, hk) - max(tot, hk)))
    return tot, peak, per


def main():
    for cid in sys.argv[1:]:
        f = os.path.join(STATE, "%s.lll.json" % cid)
        if not os.path.exists(f):
            print("%s: no LLL state yet" % cid)
            continue
        B = json.load(open(f))["B"]
        n = len(B)
        d, lam = LL.integral_gso(B)
        prof = [math.log2(d[i + 1]) - math.log2(d[i]) for i in range(n)]
        R = math.sqrt(4 * n)
        tot, peak, per = est(prof, R)
        print("%-14s n=%d  R=%.1f  FPEST = 2^%.2f  (peak depth k=%d at 2^%.2f)"
              % (cid, n, R, tot, peak[0], peak[1]))
        ef = os.path.join(STATE, "%s.enum.json" % cid)
        if os.path.exists(ef):
            st = json.load(open(ef))
            print("     measured so far: FPNODES=%d (2^%.2f) lev=%s secs=%.0f "
                  "found=%d"
                  % (st["nodes"], math.log2(max(st["nodes"], 1)), st["lev"],
                     st["secs"], len(st["found"])))
            if st["secs"] > 0:
                rate = st["nodes"] / st["secs"]
                rem = 2 ** tot - st["nodes"]
                print("     rate=%.0f nodes/s -> projected remaining %.0f s "
                      "(%.1f ramguard-local rounds)"
                      % (rate, max(rem, 0) / rate, max(rem, 0) / rate / 235.0))


if __name__ == "__main__":
    main()
