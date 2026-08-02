#!/usr/bin/env python3
"""Which structure do the slice coefficients actually have?  (F2A.5)

Run:  tools/ramguard local -- python3 \
        notes/pilots_20260802/f2_slice_coefficients/structure.py

Three pre-registered candidates:
 (a) KRAWTCHOUK -- small support / fast decay of the degree profile D_j,
     using the exact identity A_b = sum_j D_j K_j(n-b; n) (verify_slice V6).
 (b) PRODUCT / multiplicative across mode factors.
 (c) RECURSION in b (three-term / hypergeometric / P-recursive of low order).

Everything algebraic is exact in Z[zeta_p]; singular values and recurrence
residuals are EXPLORATORY float renderings of exactly computed inputs and
are labelled as such.
"""

from __future__ import annotations

import json
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np  # noqa: E402  (exploratory numerics only)

from slicecore import (  # noqa: E402
    Cyc, RESULTS, abs_pairs, degree_profile_modes, elem_sym, hhat, instance,
    krawtchouk_matrix, mode_pairs, slice_coeffs_carrydp,
)


def cvec(xs):
    return np.array([complex(x.tocomplex()) for x in xs])


# --------------------------------------------------------------- (a) -------

def krawtchouk_profile(rows):
    print("[S1] (a) KRAWTCHOUK: normalised degree profile |D_j| / max_j |D_j|")
    print("     (A_b = sum_j D_j K_j(n-b;n) exactly -- verify_slice V6)")
    for p, c, n in rows:
        _, _, loc = instance(p, c=c, n=n)
        if len(loc) < n:
            continue
        D = cvec(degree_profile_modes(p, loc))       # = 2^n * 2p * D_j
        m = np.abs(D).max()
        prof = np.abs(D) / m
        eff = float(np.sum(prof) / prof.max())       # participation ratio
        big = int(np.sum(prof > 1e-3))
        print(f"  p={p:3d} c={c} n={n}: nonzero_j={int(np.sum(prof>0)):2d}/{n+1}"
              f"  |D_j|>1e-3*max: {big:2d}  participation={eff:6.2f}")
        print("     " + " ".join(f"{v:.3f}" for v in prof))


# --------------------------------------------------------------- (b) -------

def product_structure(rows):
    print("\n[S2] (b) PRODUCT: the mode matrix M[k][b] = e_b(A(k);B(k)).")
    print("     Per mode the slice coefficient IS an elementary symmetric "
          "polynomial (exact).  The question is whether the k-sum collapses:")
    print(f"{'p':>4} {'n':>4} {'odd modes':>10} {'rank':>6} "
          f"{'sv_2/sv_1':>10} {'sv_r/sv_1':>10} {'eff rank(1e-8)':>15}")
    out = []
    for p, c, n in rows:
        _, _, loc = instance(p, c=c, n=n)
        if len(loc) < n:
            continue
        M = []
        W = []
        for k in range(1, 2 * p, 2):
            M.append(cvec(elem_sym(mode_pairs(p, k, loc))))
            W.append(complex(hhat(p, k).tocomplex()))
        M = np.array(M)
        # weight each mode row by its DFT mass and normalise
        Mw = np.array([w * r for w, r in zip(W, M)])
        Mw = Mw / np.abs(Mw).max()
        sv = np.linalg.svd(Mw, compute_uv=False)
        eff = int(np.sum(sv > 1e-8 * sv[0]))
        out.append({"p": p, "n": n, "sv": [float(x) for x in sv[:12]],
                    "rank": int(np.linalg.matrix_rank(Mw)), "eff": eff})
        print(f"{p:4d} {n:4d} {p:10d} {out[-1]['rank']:6d} "
              f"{sv[1]/sv[0]:10.3e} {sv[min(len(sv)-1, p-1)]/sv[0]:10.3e} "
              f"{eff:15d}")
    return out


# --------------------------------------------------------------- (c) -------

def recurrence_test(seq, name, maxL=3, maxd=3):
    """Smallest normalised singular value of the P-recursive ansatz matrix.

    sum_{l=0..L} q_l(b) A_{b+l} = 0 with deg q_l <= d.  A genuine recurrence
    gives a machine-zero smallest singular value.
    """
    A = np.array(seq, dtype=complex)
    A = A / np.abs(A).max()
    n1 = len(A)
    best = []
    for L in range(1, maxL + 1):
        for d in range(0, maxd + 1):
            unk = (L + 1) * (d + 1)
            eqs = n1 - L
            if eqs <= unk:
                continue
            rowsm = []
            for b in range(eqs):
                row = []
                for l in range(L + 1):
                    for e in range(d + 1):
                        row.append((b ** e) * A[b + l])
                rowsm.append(row)
            Mx = np.array(rowsm)
            Mx = Mx / np.abs(Mx).max()
            sv = np.linalg.svd(Mx, compute_uv=False)
            best.append((L, d, float(sv[-1] / sv[0])))
    return best


def recursion_structure(rows):
    print("\n[S3] (c) RECURSION in b: smallest normalised singular value of the")
    print("     P-recursive ansatz sum_l q_l(b) A_{b+l} = 0, deg q_l <= d.")
    print("     A true recurrence => ~1e-16.  CONTROL: binomial C(n,b).")
    ctrl = [float(math.comb(40, b)) for b in range(41)]
    cb = recurrence_test(ctrl, "binom")
    print("  CONTROL C(40,b):  " + "  ".join(
        f"L={L},d={d}:{v:.1e}" for L, d, v in cb if L <= 2 and d <= 1))
    out = []
    for p, c, n in rows:
        _, _, loc = instance(p, c=c, n=n)
        if len(loc) < n:
            continue
        A = cvec(slice_coeffs_carrydp(p, loc)).real
        res = recurrence_test(list(A), f"p{p}n{n}")
        out.append({"p": p, "n": n, "res": res})
        s = "  ".join(f"L={L},d={d}:{v:.1e}" for L, d, v in res
                      if (L, d) in ((1, 0), (1, 1), (2, 1), (2, 2), (3, 2)))
        print(f"  p={p:3d} n={n}: {s}")
    # single-mode control: is ONE mode's slice sequence low-order?
    p, c, n = rows[-1]
    _, _, loc = instance(p, c=c, n=n)
    e1 = cvec(elem_sym(mode_pairs(p, 1, loc)))
    r1 = recurrence_test(list(e1), "mode1")
    print("  single mode k=1 (pure elementary symmetric): " + "  ".join(
        f"L={L},d={d}:{v:.1e}" for L, d, v in r1
        if (L, d) in ((1, 0), (1, 1), (2, 1), (2, 2))))
    return out


def main():
    os.makedirs(RESULTS, exist_ok=True)
    rows = [(7, (1, 1), 10), (11, (1, 1), 12), (13, (1, 1), 12),
            (13, (2, 3), 14), (19, (1, 1), 12)]
    krawtchouk_profile(rows)
    prod = product_structure(rows)
    rec = recursion_structure(rows)
    with open(os.path.join(RESULTS, "slice_structure.json"), "w") as f:
        json.dump({"product_svd": prod, "recurrence": rec,
                   "note": "singular values / residuals are float renderings "
                           "of exactly computed Z[zeta_p] inputs"}, f, indent=1)


if __name__ == "__main__":
    main()
