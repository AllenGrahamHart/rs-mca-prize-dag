#!/usr/bin/env python3
"""The MULTI-CONDITION (moment-map) deployed window -- the escape route.

The banked pilots (f2_carry_reachability/f2model.py, f2_slice_coefficients/
slicecore.py) instantiate the census character with a SINGLE power-sum
condition:  x -> psi(c x),  c in F_{q}^*.  The official object
(PRO_FLOOR_2_F2_SUMMIT_V4.md:12-27) has t conditions:

    s_x = Tr( c . xbar(x) ) = Tr( sum_{l=1..t} c_l x^l )   in F_p.

Restricted to the rung-j sector (elements of order exactly n_j = 2^{e+j}),
x^l depends only on l mod n_j, so the frequency acts through the FOLDED
polynomial  f(x) = sum_{l mod n_j} C_l x^l.  The rung's Frobenius pairs are
antipodal ({y,-y}, tower.py), so with

    f_odd(x) = (f(x) - f(-x))/2   (the odd-l part),
    f_even(x)= (f(x) + f(-x))/2   (the even-l part),

    s^+ = Tr(f_even(y)) + Tr(f_odd(y)),    s^- = Tr(f_even(y)) - Tr(f_odd(y)).

THREE EXACT FREQUENCY CLASSES, and both degenerate ones are banked killers:

  (K1) f_even = 0 (support on ODD l only -- this is the pilots' j=1 model):
       s^- = -s^+  =>  Delta_i = 2 sigma_i^+ EVEN for every i
       =>  mode k = p slice-DEAD, flat = 0, slice floor 1/p.
  (K2) f_odd  = 0 (support on EVEN l only):
       s^- = s^+  =>  Delta_i = 0 for every i
       =>  coset_trivial: TOTAL death, rho_b = 1 exactly at every b.
  (G)  both parts nonzero: generic; measured here.

So the (H-flat) danger at the DEPLOYED window is not a coordinate-subset
phenomenon at all -- it is a FREQUENCY-SUPPORT phenomenon, and the two killer
classes are exactly the two parity-pure linear subspaces of frequency space.
"""
from __future__ import annotations

import math
import os
import sys

sys.dont_write_bytecode = True
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import numpy as np  # noqa: E402
from slicecore import Fp2, pair_reps  # noqa: E402
import census as CS  # noqa: E402


def sector_reps(p: int, n_ord: int):
    """Pair representatives of the rung-1 sector (order exactly n_ord)."""
    F = Fp2.make(p)
    mu = F.subgroup(n_ord)
    reps = pair_reps(F, mu)
    return F, reps


def powers_table(F: Fp2, reps, n_ord: int, ls):
    """Tr(y^l) is not enough -- we need y^l itself.  Return {l: [y^l]}."""
    out = {}
    for l in ls:
        out[l] = [F.pow(y, l % n_ord) for y in reps]
    return out


def deltas_moment(F: Fp2, reps, n_ord: int, coeffs: dict[int, tuple[int, int]]):
    """Delta_i for the frequency polynomial f(x) = sum_l c_l x^l.  EXACT ints.

    Uses f(-y) = sum_l (-1)^l c_l y^l -- no second field evaluation needed.
    """
    p = F.p
    two_p = 2 * p
    n = len(reps)
    accP = [(0, 0)] * n          # sum over l of c_l y^l
    accM = [(0, 0)] * n          # sum over l of (-1)^l c_l y^l
    for l, cl in coeffs.items():
        sgn = 1 if (l % 2 == 0) else -1
        for i, y in enumerate(reps):
            term = F.mul(cl, F.pow(y, l % n_ord))
            accP[i] = ((accP[i][0] + term[0]) % p, (accP[i][1] + term[1]) % p)
            if sgn == 1:
                accM[i] = ((accM[i][0] + term[0]) % p,
                           (accM[i][1] + term[1]) % p)
            else:
                accM[i] = ((accM[i][0] - term[0]) % p,
                           (accM[i][1] - term[1]) % p)
    D = []
    for i in range(n):
        sp = F.trace(accP[i])
        sm = F.trace(accM[i])
        sig_p = (sp + p * (1 if 2 * sp > p else 0)) % two_p
        sig_m = (sm + p * (1 if 2 * sm > p else 0)) % two_p
        D.append((sig_p - sig_m) % two_p)
    return D


def counts_of(p: int, D):
    return np.bincount(np.array(D, dtype=np.int64), minlength=2 * p)


def window_stats(p: int, D):
    cnt = counts_of(p, D)
    m = int(cnt.sum())
    mr, kk = CS.maxR(p, cnt, m)
    odd = int(sum(int(cnt[v]) for v in range(1, 2 * p, 2)))
    return {"m": m, "n_values": int((cnt > 0).sum()),
            "max_absR_float": mr, "argmax_k": kk, "flat_float": 1.0 - mr,
            "beta_min": min(odd, m - odd) / m,
            "defect_D": CS.defect_from_counts(p, cnt),
            "all_delta_zero": int((cnt > 0).sum()) == 1 and int(cnt[0]) == m,
            "all_delta_even": odd == 0}
