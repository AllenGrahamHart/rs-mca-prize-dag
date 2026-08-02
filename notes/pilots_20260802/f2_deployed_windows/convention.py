#!/usr/bin/env python3
"""Which findings survive the ORIENTATION-LABELLING convention?

The banked pilots pick the pair representative by b_y in [1,(p-1)/2]
(f2_carry_reachability/f2model.py `pair_reps`).  Flipping the representative
of coordinate i sends Delta_i -> -Delta_i (and permutes the slice index b),
so any Delta-statistic that is not invariant under independent sign flips is
a MODELLING convention, not a tower fact.

  * PARITY of Delta_i is invariant  ->  "all Delta even", hence the death of
    mode k = p and the 1/p slice floor, is convention-INDEPENDENT.
  * |R_k| for k != p is NOT invariant.  On the deployed (K1) window
    Delta_i = 2 sigma_i and the phases theta_i = 2 pi s_i / p all lie in the
    UPPER half plane under the banked convention, so |R_1| -> |E e^{i U}| with
    U uniform on (0, pi), i.e. 2/pi = 0.63662 -- an artefact of the interval
    half-system, reproduced below and then dissolved by random flips.
"""
from __future__ import annotations
import json, math, os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np                       # noqa: E402
import deployed as DP, tower as TW, census as CS   # noqa: E402

rng = np.random.default_rng(99)
rows = []
for e in (5, 6, 7, 8, 9, 10, 11):
    p = TW.official_shaped_prime(e)
    n1 = 1 << (e + 1)
    ra = CS.reps_arrays(p, n1)
    if ra is None:
        continue
    F, ay, by = ra
    m = len(ay)
    banked, flipped, parity_ok = [], [], True
    for _ in range(12):
        c = (int(rng.integers(p)), int(rng.integers(1, p)))
        # banked convention
        two_p = 2 * p
        A = (2 * c[0]) % p
        B = (2 * F.N * c[1]) % p
        sp = ((A * ay) % p + (B * by) % p) % p
        sm = ((A * ay) % p - (B * by) % p) % p
        sg_p = sp + p * (2 * sp > p)
        sg_m = sm + p * (2 * sm > p)
        D = (sg_p - sg_m) % two_p
        if int(np.bincount(D, minlength=two_p)[1::2].sum()) != 0:
            parity_ok = False
        cnt = np.bincount(D, minlength=two_p)
        banked.append(CS.maxR_excluding_p(p, cnt, m)[0])
        # random independent orientation flips
        s = rng.integers(0, 2, size=m) * 2 - 1
        D2 = (D * s) % two_p
        cnt2 = np.bincount(D2, minlength=two_p)
        if int(cnt2[1::2].sum()) != 0:
            parity_ok = False
        flipped.append(CS.maxR_excluding_p(p, cnt2, m)[0])
    rows.append({"p": p, "e": e, "m": m,
                 "banked_max_absR_k_ne_p_med": float(np.median(banked)),
                 "flipped_max_absR_k_ne_p_med": float(np.median(flipped)),
                 "two_over_pi": 2 / math.pi,
                 "parity_invariant_under_flips": parity_ok})
    print(f"e={e:2d} p={p:7d} m={m:5d}  banked med |R_{{k!=p}}| = "
          f"{np.median(banked):.5f}  (2/pi = {2/math.pi:.5f})   "
          f"random-flip med = {np.median(flipped):.5f}   "
          f"all-Delta-even survives flips: {parity_ok}")
DP.dump("E9_convention.json", {"rows": rows})
