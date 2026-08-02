#!/usr/bin/env python3
"""Complete finite router for LOW-weight ternary relations at 2N = 32.

Enumerates every ternary polynomial f of degree < N = 16 and weight w <= wmax
(normalised to leading nonzero coefficient +1), computes the exact integer
Norm(f) = Res(f, x^16 + 1) by fraction-free elimination, and factors it.
A prime q = 1 (mod 32) carries a weight-w relation iff q divides one of these
norms; the union over w <= wmax is therefore a COMPLETE, q-independent, finite
list of the rows whose C1 excess has a weight-<= wmax owner.

This is the exact analogue -- computed rather than assumed -- of the three
short-relation exclusion dependencies wired into
background/nodes/dli_c1_l1_block_owner_ledger.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations, product

from sympy import factorint

from relation_certificates import norm_mod_xN_plus_1


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--twoN", type=int, default=32)
    ap.add_argument("--wmax", type=int, default=4)
    ap.add_argument("--qmax", type=int, default=3000000)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    N = args.twoN // 2
    hits: dict[int, dict] = {}
    n_poly = 0
    zero_norm = 0
    max_norm = 0
    for w in range(1, args.wmax + 1):
        for pos in combinations(range(N), w):
            for signs in product((1, -1), repeat=w - 1):
                d = [0] * N
                d[pos[0]] = 1
                for p, sg in zip(pos[1:], signs):
                    d[p] = sg
                n_poly += 1
                nrm = norm_mod_xN_plus_1(d)
                if nrm == 0:
                    zero_norm += 1
                    continue
                a = abs(nrm)
                max_norm = max(max_norm, a)
                for p, _ in factorint(a).items():
                    if p % args.twoN == 1 and p <= args.qmax:
                        rec = hits.setdefault(int(p), {"q": int(p), "min_w": w,
                                                       "witness": None,
                                                       "norms": []})
                        if w < rec["min_w"]:
                            rec["min_w"] = w
                        if rec["witness"] is None or w <= rec["min_w"]:
                            rec["witness"] = list(d)
                        rec["norms"].append(str(a))
    out = {"twoN": args.twoN, "wmax": args.wmax, "qmax": args.qmax,
           "n_polynomials": n_poly, "n_zero_norm": zero_norm,
           "max_abs_norm": str(max_norm),
           "n_primes_hit": len(hits),
           "primes": sorted(hits.values(), key=lambda r: r["q"])}
    with open(args.out, "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != "primes"}))
    print("primes with a weight<=%d relation (q = 1 mod %d, q <= %d): %s"
          % (args.wmax, args.twoN, args.qmax,
             [r["q"] for r in out["primes"]]))


if __name__ == "__main__":
    main()
