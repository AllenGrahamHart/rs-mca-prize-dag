#!/usr/bin/env python3
"""dli_norm_gate -- THE SPLITTING STATISTIC, at scale.

For a ternary alpha in Z[zeta_n] (n = 2^s), q == 1 mod n prime, put

    Z(alpha) = { j odd mod n : alpha(zeta^j) = 0 in F_q }   (the annihilated
                                                             primitive roots
                                                             = the primes above
                                                             q dividing alpha)
    m(alpha) = |Z(alpha)|,
    H_U(alpha) = { a in (Z/n)^* : a.U subset Z(alpha) }     (U = U_0 = the
                                                             junction's odd
                                                             exponent block)

C2'' junction-0 solution at the CANONICAL root  <=>  1 in H_U(alpha).

LAW S1 (proved in the report): Galois acts on ternary weight-w elements by
signed basis permutation, and simply transitively on the phi(n) roots, so

    phi(n) * #{alpha in W_w : 1 in H_U(alpha)} = sum_{alpha in W_w} |H_U(alpha)|.

LAW S2: ratio_w = #sol_w / #{H_U != empty}_w = mean|H_U| / phi(n) >= 1/phi(n),
equality iff |H_U| <= 1 throughout.
LAW S3: |Z(alpha)| >= 2 forces q^2 | Norm(alpha) <= w^{phi(n)/2}, so
q^2 > maxnorm(phi(n),w) makes the equality in S2 automatic.
"""

from __future__ import annotations

import json
import sys
from itertools import combinations, product as iproduct
from math import comb
from pathlib import Path

sys.dont_write_bytecode = True

import numpy as np

from core import admissible_primes, get_zeta

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# banked C1 maxnorm table, indexed by 2N = n then weight (= support size)
MAXNORM = {
    16: {1: 1, 2: 16, 3: 81, 4: 196, 5: 529, 6: 1154, 7: 2401, 8: 2176},
    32: {1: 1, 2: 256, 3: 6561, 4: 38416, 5: 279841, 6: 1331716, 7: 5764801,
         8: 14760962, 9: 38950081, 10: 84580802, 11: 184497889, 12: 342386306,
         13: 777684769, 14: 1040410946, 15: 1612931233, 16: 2311094272},
    64: {1: 1, 2: 65536, 3: 43046721, 4: 1475789056, 5: 78310985281,
         6: 1773467504656, 7: 33232930569601},
}


def root_powers(q, n):
    """P[i,k] = (zeta^{j_k})^i mod q, j_k = 2k+1 the odd residues."""
    h = n // 2
    z = get_zeta(q, n)
    return np.array([[pow(pow(z, 2 * k + 1, q), i, q) for k in range(h)]
                     for i in range(h)], dtype=np.int64)


def u_masks(n, U):
    """mask[a_index] = bitmask over odd-root indices of the set a.U."""
    h = n // 2
    idx = {(2 * k + 1): k for k in range(h)}
    out = []
    for k in range(h):
        a = 2 * k + 1
        mk = 0
        for u in U:
            mk |= 1 << idx[(a * u) % n]
        out.append(mk)
    return np.array(out, dtype=np.uint64)


def weight_blocks(h, w, chunk_supports=None):
    """yield (K,h) int8 arrays covering every ternary vector of weight w."""
    signs = np.array(list(iproduct((1, -1), repeat=w)), dtype=np.int8)
    ns = len(signs)
    if chunk_supports is None:                    # keep K*h ~ 2^22 entries
        chunk_supports = max(1, (1 << 22) // (ns * h))
    buf_S = []
    for S in combinations(range(h), w):
        buf_S.append(S)
        if len(buf_S) == chunk_supports:
            yield _build(buf_S, signs, h, ns)
            buf_S = []
    if buf_S:
        yield _build(buf_S, signs, h, ns)


def _build(supports, signs, h, ns):
    A = np.zeros((len(supports) * ns, h), dtype=np.int8)
    for a, S in enumerate(supports):
        A[a * ns:(a + 1) * ns][:, list(S)] = signs
    return A


def scan(n, q, w, U, want_hist=True):
    """exact counts for weight-w ternary alpha at (n,q) with block U."""
    h = n // 2
    P = root_powers(q, n)
    UM = u_masks(n, U)
    bits = np.array([np.uint64(1) << np.uint64(k) for k in range(h)],
                    dtype=np.uint64)
    tot = 0
    n_sol = 0
    n_hit = 0            # H_U non-empty
    sum_H = 0
    n_normdiv = 0        # m >= 1
    sum_m = 0
    mhist = np.zeros(h + 1, dtype=np.int64)
    Hhist = np.zeros(h + 1, dtype=np.int64)
    for A in weight_blocks(h, w):
        V = (A.astype(np.int64) @ P) % q          # (K,h)
        Zb = (V == 0)
        m = Zb.sum(axis=1)
        Zm = np.zeros(len(A), dtype=np.uint64)
        for k in range(h):
            Zm |= Zb[:, k].astype(np.uint64) << np.uint64(k)
        Hc = np.zeros(len(A), dtype=np.int64)
        for k in range(h):
            mk = UM[k]
            Hc += ((Zm & mk) == mk)
        sol = (Zm & UM[0]) == UM[0]
        tot += len(A)
        n_sol += int(sol.sum())
        n_hit += int((Hc > 0).sum())
        sum_H += int(Hc.sum())
        n_normdiv += int((m > 0).sum())
        sum_m += int(m.sum())
        if want_hist:
            mhist += np.bincount(m, minlength=h + 1)
            Hhist += np.bincount(Hc, minlength=h + 1)
    return {"n": n, "q": q, "w": w, "U": list(U), "phi": h,
            "n_vectors": tot, "n_solutions": n_sol,
            "n_H_nonempty": n_hit, "sum_H": sum_H,
            "n_norm_divisible": n_normdiv, "sum_m": sum_m,
            "S1_identity_holds": h * n_sol == sum_H,
            "S1_lhs": h * n_sol, "S1_rhs": sum_H,
            "max_m": int(np.nonzero(mhist)[0].max()) if mhist.any() else 0,
            "max_H": int(np.nonzero(Hhist)[0].max()) if Hhist.any() else 0,
            "m_hist": {str(i): int(c) for i, c in enumerate(mhist) if c},
            "H_hist": {str(i): int(c) for i, c in enumerate(Hhist) if c},
            "ratio_num": n_sol, "ratio_den": n_hit,
            "ratio_times_phi": (h * n_sol / n_hit) if n_hit else None,
            "predicted_1_over_phi_exact": (n_hit == h * n_sol) if n_hit else None}


def s3_regime(n, w, q):
    mx = MAXNORM.get(n, {}).get(w)
    if mx is None:
        return None
    return {"maxnorm": mx, "q^2": q * q, "S3_sufficient": q * q > mx}


def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else "n16"
    out = []
    if stage == "n16":
        n = 16
        qs = admissible_primes(n, 2, 4000)
        for q in qs:
            for w in range(1, 9):
                r = scan(n, q, w, [1])
                r["S3"] = s3_regime(n, w, q)
                out.append(r)
    elif stage == "n16_o":
        n = 16
        qs = admissible_primes(n, 2, 4000)
        for q in qs:
            for U in ([1, 3], [1, 3, 5]):
                for w in range(1, 9):
                    r = scan(n, q, w, U)
                    r["S3"] = s3_regime(n, w, q)
                    out.append(r)
    elif stage == "n32":
        n = 32
        qs = [97, 193, 257, 353, 449, 577, 641, 673, 929, 1153, 1409, 2113,
              3457, 7937, 12289, 40961, 65537, 786433, 1179649, 5767169]
        for q in qs:
            for w in range(1, 9):
                r = scan(n, q, w, [1])
                r["S3"] = s3_regime(n, w, q)
                out.append(r)
                print(f"n=32 q={q} w={w}: sol={r['n_solutions']} "
                      f"hit={r['n_H_nonempty']} S1={r['S1_identity_holds']} "
                      f"maxm={r['max_m']} ratio*phi={r['ratio_times_phi']}")
    elif stage == "n32_o":
        n = 32
        qs = [97, 193, 257, 353, 449, 641, 1153, 3457, 7937, 65537, 786433]
        for q in qs:
            for U in ([1, 3], [1, 3, 5]):
                for w in range(1, 9):
                    r = scan(n, q, w, U)
                    r["S3"] = s3_regime(n, w, q)
                    out.append(r)
    elif stage == "n64":
        n = 64
        qs = [193, 257, 449, 641, 7937, 65537]
        for q in qs:
            for w in range(1, 6):
                r = scan(n, q, w, [1])
                r["S3"] = s3_regime(n, w, q)
                out.append(r)
                print(f"n=64 q={q} w={w}: sol={r['n_solutions']} "
                      f"hit={r['n_H_nonempty']} S1={r['S1_identity_holds']} "
                      f"maxm={r['max_m']}")
    elif stage == "n128":
        n = 128
        qs = [257, 641, 769, 3329, 12289, 40961, 65537]
        for q in qs:
            for w in range(1, 5):
                r = scan(n, q, w, [1])
                out.append(r)
                print(f"n=128 q={q} w={w}: sol={r['n_solutions']} "
                      f"hit={r['n_H_nonempty']} S1={r['S1_identity_holds']} "
                      f"maxm={r['max_m']}")
    else:
        raise SystemExit(f"unknown stage {stage}")

    bad_S1 = [r for r in out if not r["S1_identity_holds"]]
    dev = [r for r in out if r["n_H_nonempty"] and not r["predicted_1_over_phi_exact"]]
    s3_viol = [r for r in out if r.get("S3") and r["S3"]["S3_sufficient"]
               and r["n_H_nonempty"] and not r["predicted_1_over_phi_exact"]]
    summ = {"stage": stage, "n_rows": len(out),
            "S1_violations": len(bad_S1),
            "rows_with_H_nonempty": sum(1 for r in out if r["n_H_nonempty"]),
            "rows_deviating_from_1_over_phi": len(dev),
            "S3_predicted_exact_but_deviating": len(s3_viol),
            "deviating_rows": [{k: r[k] for k in
                                ("n", "q", "w", "U", "n_solutions",
                                 "n_H_nonempty", "max_m", "max_H",
                                 "ratio_times_phi")} | {"S3": r.get("S3")}
                               for r in dev]}
    (ROOT / "results" / f"splitting_{stage}.json").write_text(
        json.dumps({"summary": summ, "rows": out}, indent=1))
    print(json.dumps(summ, indent=1)[:4000])


if __name__ == "__main__":
    main()
