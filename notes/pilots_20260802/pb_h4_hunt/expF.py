#!/usr/bin/env python3
"""EXPERIMENT F -- the sub-family trick, and why it is void.

EXPERIMENT E found q-INDEPENDENT collinear block systems of block size
m = 4 >= h+1 = 4 at n=24: 66 of them, exactly C(12,2) -- the blocks are
PAIRS OF mu_2-COSETS, whose moment vectors are (0, 2(lam_i+lam_j), 0), all
on one line through the origin.  Such a block family IS spread: adjacent
label sets differ in a whole 4-block, so |S ^ S'| = A - 4 = K - 1.

The catch: the adversary does not choose the planted family, the PENCIL
does, and the pencil that carries the 4-block family is exactly the
split-fibre pencil for the underlying coset width m' = 2.  Its witness set
E^{-1}(L) therefore also contains every SINGLE-coset variation, and those
meet in A - m' = A - 2 >= K.  This script verifies that closure exactly.

Run:  tools/ramguard local -- python3 expF.py
"""
from __future__ import annotations

import json
import os
import sys
from itertools import combinations

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import core

HERE = os.path.dirname(os.path.abspath(__file__))


def run(n=24, q=241, mp=2, g=3, ap=4, K=8, h=3):
    A = K + h
    assert g + mp * ap == A and mp <= h < 2 * mp
    D = core.domain(q, n)
    nf = n // mp                                     # cosets of mu_mp
    fib = [[j + t * nf for t in range(mp)] for j in range(nf)]
    lab = [pow(D[j], mp, q) for j in range(nf)]
    corei = [nf - 1, 2 * nf - 1, nf - 2][:g]         # not a coset union
    used = {i % nf for i in corei}
    pool = [j for j in range(nf) if j not in used]
    # the full split-fibre family
    fam = []
    for J in combinations(pool, ap):
        S = tuple(sorted(set(corei) | {i for j in J for i in fib[j]}))
        assert len(S) == A, (len(S), A)
        z = sum(lab[j] for j in J) % q
        fam.append((J, S, z))
    E = {core.moment_vector([D[i] for i in S], h, q) for _, S, _ in fam}
    Es = sorted(E)
    d0 = tuple((Es[1][t] - Es[0][t]) % q for t in range(h))
    f = next(t for t in range(h) if d0[t])
    iv = pow(d0[f], q - 2, q)
    cd = tuple(x * iv % q for x in d0)
    collinear = True
    for P in Es[2:]:
        d = tuple((P[t] - Es[0][t]) % q for t in range(h))
        if not any(d):
            continue
        ff = next(t for t in range(h) if d[t])
        if ff != f or tuple(x * pow(d[ff], q - 2, q) % q for x in d) != cd:
            collinear = False
            break
    masks = [core.mask_of(S) for _, S, _ in fam]
    full_max = core.max_pair_core(masks)
    full_lo = len(core.gamma_lo(masks, K))

    # the paired-coset SUB-family (blocks = fixed pairs of cosets)
    pairs = [(pool[2 * i], pool[2 * i + 1]) for i in range(len(pool) // 2)]
    sub = []
    for J2 in combinations(range(len(pairs)), ap // 2):
        J = tuple(sorted(x for i in J2 for x in pairs[i]))
        S = tuple(sorted(set(corei) | {i for j in J for i in fib[j]}))
        sub.append((J, S, sum(lab[j] for j in J) % q))
    smasks = [core.mask_of(S) for _, S, _ in sub]
    sub_max = core.max_pair_core(smasks)
    sub_lo = len(core.gamma_lo(smasks, K))
    sub_in_full = all(m in set(masks) for m in smasks)

    # every sub-family member has a FULL-family neighbour at core >= K
    killed = 0
    fullset = list(zip(masks, [z for _, _, z in fam]))
    for m1, (J, S, z) in zip(smasks, sub):
        if any(core.popcount(m1 & m2) >= K and m1 != m2
               for m2, _ in fullset):
            killed += 1
    # ... and that neighbour sits at a DIFFERENT slope (so the kill is a
    # statement about the SELECTED family, not about the identity alone)
    diff_slope = 0
    zsub = {core.mask_of(S): z for _, S, z in sub}
    for m1, (J, S, z) in zip(smasks, sub):
        for m2, z2 in fullset:
            if m1 != m2 and core.popcount(m1 & m2) >= K:
                if z2 != z:
                    diff_slope += 1
                break

    res = dict(n=n, q=q, m=mp, g=g, a=ap, K=K, h=h, A=A,
               full_family=len(fam), collinear=collinear,
               full_distinct_moment_points=len(E),
               full_max_pair_core=full_max, K_threshold=K,
               full_gamma_lo=full_lo,
               sub_family=len(sub), sub_max_pair_core=sub_max,
               sub_gamma_lo_within_subfamily=sub_lo,
               sub_is_subset_of_full=sub_in_full,
               sub_members_killed_by_full=killed,
               killers_at_a_different_slope=diff_slope)
    print(f"  split-fibre m={mp} g={g} a={ap} at n={n} q={q}: "
          f"family={len(fam)} collinear={collinear} maxcore={full_max} "
          f"(K={K}) Gamma_lo={full_lo}")
    print(f"  paired-coset SUB-family: {len(sub)} members, maxcore={sub_max} "
          f"(<=K-1={K-1}: {sub_max <= K-1}) Gamma_lo within itself={sub_lo}")
    print(f"  but it sits inside the SAME pencil: subset={sub_in_full}; "
          f"{killed}/{len(sub)} of its members have a witness partner at "
          f"core >= K, and {diff_slope}/{len(sub)} of those partners live at "
          f"a DIFFERENT slope")
    p = os.path.join(HERE, "EXPF.json")
    with open(p, "w") as fh:
        json.dump(res, fh, indent=1, sort_keys=True)
    print(f"-> {p}")
    return res


if __name__ == "__main__":
    run()
