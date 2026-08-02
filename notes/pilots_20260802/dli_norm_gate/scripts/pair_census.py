#!/usr/bin/env python3
"""dli_norm_gate -- the o>1 (ell-fold) skew census, and its AM-GM fence.

A junction with exponent block U (|U| = o) needs alpha(zeta^{ua}) = 0 for all
u in U at a = 1.  By LN2 that forces q^o | Norm(alpha), so by LN4

    q > E^{phi(n)/(2o)}   =>   no o-fold solution of energy E.

The candidate primes for an o-fold solution at weight w are therefore only the
admissible q with q^o | Norm(alpha) for some ternary weight-w alpha -- a FINITE,
cheaply enumerable set (q <= maxnorm(phi(n),w)^{1/o}).  This script builds that
census exactly at n = 32 (phi = 16) for U = {1,3} (the DLI ell = 2 block, the
same shape as the banked order-1024 weight-5/6 exclusions) and confirms the
fence.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

sys.dont_write_bytecode = True

import numpy as np
import sympy

from core import get_zeta
from bridge import norms_batch, ternary_weight_block, spf_sieve, factor_with

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def pair_census(n=32, wmax=8, U=(1, 3)):
    """chunked: never materialises a whole weight class at once."""
    from splitting import weight_blocks
    h = n // 2
    o = len(U)
    per_w = {}
    census = {}
    idx = {(2 * k + 1): k for k in range(h)}
    for w in range(1, wmax + 1):
        # pass 1: candidate primes q with q^o | Norm(alpha) for some alpha
        cand = defaultdict(int)
        mx = 0
        seen = set()
        for A in weight_blocks(h, w):
            Nz = norms_batch(A.astype(np.int64))
            mx = max(mx, int(Nz.max()))
            for v in np.unique(Nz):
                v = int(v)
                if v <= 1 or v in seen:
                    continue
                seen.add(v)
                for p, c in sympy.factorint(v).items():
                    if c >= o and p % n == 1:
                        cand[p] = max(cand[p], c)
        # pass 2: verify each candidate directly
        confirmed = {}
        for q in sorted(cand):
            z = get_zeta(q, n)
            P = np.array([[pow(pow(z, 2 * k + 1, q), i, q) for k in range(h)]
                          for i in range(h)], dtype=np.int64)
            cols_by_a = [[idx[((2 * k + 1) * u) % n] for u in U]
                         for k in range(h)]
            tot = 0
            wit = None
            for A in weight_blocks(h, w):
                V = (A.astype(np.int64) @ P) % q
                Zb = (V == 0)
                ok = np.zeros(len(A), dtype=bool)
                for cols in cols_by_a:
                    m = Zb[:, cols[0]].copy()
                    for c in cols[1:]:
                        m &= Zb[:, c]
                    ok |= m
                if ok.any():
                    tot += int(ok.sum())
                    if wit is None:
                        r = int(np.nonzero(ok)[0][0])
                        wit = [int(v) for v in A[r]]
                        wnorm = int(norms_batch(A[r:r + 1].astype(np.int64))[0])
            if tot:
                confirmed[q] = {"n_vectors_with_pair": tot, "witness": wit,
                                "witness_norm": wnorm,
                                "q^o_divides_norm": wnorm % q**o == 0}
        per_w[w] = {"maxnorm": mx,
                    "AMGM_fence_q_gt": int(round(mx ** (1.0 / o))),
                    "n_candidate_primes(q^o | some norm)": len(cand),
                    "candidates": sorted(cand),
                    "n_confirmed": len(confirmed),
                    "confirmed": {str(k): v for k, v in confirmed.items()}}
        for q in confirmed:
            census.setdefault(q, w)
        print(f"  w={w}: maxnorm={mx} candidates={sorted(cand)} "
              f"confirmed={sorted(confirmed)}", flush=True)
    return {"n": n, "U": list(U), "o": o, "per_w": per_w,
            "census_min_weight": {str(k): v for k, v in sorted(census.items())},
            "largest_census_prime": max(census) if census else None}


def amgm_dictionary():
    """AM-GM fence q > w^{phi/(2o)} at the banked settings."""
    rows = []
    for (label, n, phi) in [("2N=16 (C2'' n=16)", 16, 8),
                            ("2N=32 (C2'' n=32)", 32, 16),
                            ("2N=64", 64, 32),
                            ("order-1024 WCL block", 1024, 512),
                            ("official junction 0 (n=2^41)", 2**41, 2**40)]:
        for o in (1, 2, 3):
            for w in (3, 4, 5, 6):
                fence_log2 = (phi / (2 * o)) * np.log2(w)
                rows.append({"setting": label, "phi": phi, "o(ell)": o, "w": w,
                             "fence_q_gt_log2": round(float(fence_log2), 3),
                             "beats_official_2^256": bool(fence_log2 < 256)})
    return rows


def main():
    print("ell=2 (U={1,3}) skew census at n=32:")
    out = {"pair_census_n32": pair_census(), "amgm_dictionary": amgm_dictionary()}
    print("\nAM-GM fence log2 thresholds (q must EXCEED 2^value to be excluded):")
    for r in out["amgm_dictionary"]:
        if r["o(ell)"] == 2:
            print(f"  {r['setting']:<32} o=2 w={r['w']}: "
                  f"q > 2^{r['fence_q_gt_log2']}  "
                  f"(free at official q<2^256: {r['beats_official_2^256']})")
    (ROOT / "results" / "pair_census.json").write_text(
        json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
