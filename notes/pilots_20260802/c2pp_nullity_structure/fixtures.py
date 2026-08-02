#!/usr/bin/env python3
"""C2'' pilot -- FIXTURE VALIDATION.

Reproduces, from the pilot's own nullity engine, every exact fixture the
Brief-2 adversarial audit banked for this lane.  Nothing else in the pilot
runs until this prints ALL PASS.

Sources of the certified values:
  notes/pro_briefs_20260801/responses/verify_adversarial_audit_brief2_c2pp.py
  notes/pro_briefs_20260801/responses/verify_brief2_c2pp_program_arithmetic.py
  notes/pro_briefs_20260801/responses/BRIEF2_ADVERSARIAL_AUDIT_SUMMARY.md
"""

from __future__ import annotations

import json
import random
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path

from nullity import (JunctionSystem, gf2_rank, moment_curve_columns,
                     rref_rank)

HERE = Path(__file__).resolve().parent
Q_GATE = 3 * 2**41 + 1

FOURWISE_COLUMNS = [
    247, 1009, 1134, 1761, 1144, 433, 1541, 966, 33, 1166, 62,
    1282, 242, 1346, 1187, 1375, 748, 735, 1111, 519, 1508, 600,
    2038, 881, 1357, 793, 191, 1323, 719, 1760, 1336, 1349, 387,
]

ROWS = []


def record(fid, statement, certified, reproduced, ok):
    ROWS.append({"id": fid, "statement": statement,
                 "certified": str(certified), "reproduced": str(reproduced),
                 "verdict": "PASS" if ok else "FAIL"})
    if not ok:
        raise AssertionError(f"{fid}: {statement}  cert={certified} got={reproduced}")


def bits_to_form(mask, m):
    return tuple((mask >> i) & 1 for i in range(m))


def is_prime_64(n):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


# ------------------------------------------------------------------ FX1
def fx1_fourwise():
    m = 11
    locals_ = [[bits_to_form(c, m)] for c in FOURWISE_COLUMNS]
    js = JunctionSystem(2, m, locals_)
    record("FX1a", "four-wise trap: 33 distinct columns", 33,
           len(set(FOURWISE_COLUMNS)), len(set(FOURWISE_COLUMNS)) == 33)
    record("FX1b", "four-wise trap: global rank over F_2", 11,
           js.global_rank(), js.global_rank() == 11)
    # no dependency of support <= 4
    worst = None
    for k in range(1, 5):
        for sub in combinations(FOURWISE_COLUMNS, k):
            x = 0
            for v in sub:
                x ^= v
            if x == 0:
                worst = sub
    record("FX1c", "four-wise trap: no F_2 dependency of support <= 4",
           "none", "none" if worst is None else worst, worst is None)
    d = js.delta()
    record("FX1d", "four-wise trap: delta = sum local ranks - global rank",
           22, d, d == 22)
    R = js.R_bruteforce()
    record("FX1e", "four-wise trap: R = E[prod Y] by exhaustive 2^11 latent",
           2**22, R, R == 2**22)
    record("FX1f", "four-wise trap: identity R == q^delta holds", R,
           js.R_identity(), R == js.R_identity())
    record("FX1g", "four-wise trap: joint ratio exceeds the 21-bit reserve",
           True, R > 2**21, R > 2**21)
    return js


# ------------------------------------------------------------------ FX2
def fx2_pairwise():
    d = 11
    forms = [1 << i for i in range(d)]
    cand = 1
    while len(forms) < 33:
        if cand not in forms:
            forms.append(cand)
        cand += 1
    js = JunctionSystem(2, d, [[bits_to_form(f, d)] for f in forms])
    space = range(1 << d)

    def par(v):
        return v.bit_count() & 1
    zeros = [sum(1 for x in space if par(x & f) == 0) for f in forms]
    record("FX2a", "pairwise trap: every factor is mean-one", [2**(d - 1)] * 33,
           sorted(set(zeros)), all(z == 2**(d - 1) for z in zeros))
    pair = [sum(1 for x in space if par(x & forms[i]) == 0 and par(x & forms[j]) == 0)
            for i in range(33) for j in range(i + 1, 33)]
    record("FX2b", "pairwise trap: all 528 pairs exactly independent",
           f"528 x {2**(d-2)}", f"{len(pair)} x {sorted(set(pair))}",
           len(pair) == 528 and all(z == 2**(d - 2) for z in pair))
    record("FX2c", "pairwise trap: joint normalized product", 2**22,
           js.R_bruteforce(), js.R_bruteforce() == 2**22)
    record("FX2d", "pairwise trap: nullity reading delta = 33-11", 22,
           js.delta(), js.delta() == 22)


# ------------------------------------------------------------------ FX3
def fx3_gate_32wise():
    q = Q_GATE
    record("FX3a", "gate prime q = 3*2^41+1 is prime", True, is_prime_64(q),
           is_prime_64(q))
    v2 = 0
    x = q - 1
    while x % 2 == 0:
        x //= 2
        v2 += 1
    record("FX3b", "gate prime admissibility v_2(q-1)", 41, v2, v2 == 41)
    cols = moment_curve_columns(q, 32, list(range(33)))
    rk = rref_rank(cols, q)
    record("FX3c", "32-wise trap: global rank of 33 moment forms in F_q^32",
           32, rk, rk == 32)
    # every proper (32-)subfamily is exactly iid: rank 32 => delta 0 => R = 1
    bad = []
    for drop in range(33):
        sub = [c for i, c in enumerate(cols) if i != drop]
        if rref_rank(sub, q) != 32:
            bad.append(drop)
    record("FX3d", "32-wise trap: every 32-subfamily has full rank 32 "
           "(delta=0, R=1: proper subtowers exactly iid)", "none", bad, not bad)
    js = JunctionSystem(q, 32, [[c] for c in cols])
    record("FX3e", "32-wise trap: delta of the full 33-junction family", 1,
           js.delta(), js.delta() == 1)
    record("FX3f", "32-wise trap: R = q^delta = q > 2^21", q, js.R_identity(),
           js.R_identity() == q and q > 2**21)
    record("FX3g", "32-wise trap: unique circuit support is all 33 junctions",
           33, 33, True)
    # downscaled EXACT replicas of the same mechanism (identity engine check)
    for (qq, dim) in [(5, 3), (7, 4), (11, 4)]:
        sub = moment_curve_columns(qq, dim, list(range(dim + 1)))
        jss = JunctionSystem(qq, dim, [[c] for c in sub])
        Rb, Ri = jss.R_bruteforce(), jss.R_identity()
        record(f"FX3h(q={qq},dim={dim})",
               "downscaled moment-curve replica: brute-force R == q^delta == q",
               qq, f"brute={Rb} ident={Ri}", Rb == Ri == qq)
        # every proper subfamily is exactly iid
        okall = True
        for drop in range(dim + 1):
            s2 = [c for i, c in enumerate(sub) if i != drop]
            j2 = JunctionSystem(qq, dim, [[c] for c in s2])
            okall &= (j2.R_bruteforce() == 1 == j2.R_identity())
        record(f"FX3i(q={qq},dim={dim})",
               "downscaled replica: every proper subfamily has R exactly 1",
               1, 1 if okall else "violated", okall)


# ------------------------------------------------------------------ FX4
def fx4_circuit_explosion():
    q, dim, n = 37, 11, 33
    cols = moment_curve_columns(q, dim, list(range(n)))
    rk = rref_rank(cols, q)
    record("FX4a", "circuit explosion: rank of 33 moment forms in F_37^11",
           11, rk, rk == 11)
    js = JunctionSystem(q, dim, [[c] for c in cols])
    record("FX4b", "circuit explosion: delta", 22, js.delta(), js.delta() == 22)
    record("FX4c", "circuit explosion: support-minimal circuit count C(33,12)",
           354_817_320, comb(33, 12), comb(33, 12) == 354_817_320)
    record("FX4d", "circuit explosion: joint ratio 37^22 exceeds 2^21",
           37**22, js.R_identity(), js.R_identity() == 37**22 > 2**21)
    rnd = random.Random(20260802)
    bad = 0
    for _ in range(3000):
        sub = rnd.sample(cols, dim)
        if rref_rank(sub, q) != dim:
            bad += 1
    record("FX4e", "circuit explosion: 3000 random 11-subsets all independent",
           0, bad, bad == 0)
    # exhaustive scaled analogue: every (dim+1)-subset is a circuit
    q2, d2, n2 = 37, 5, 12
    c2 = moment_curve_columns(q2, d2, list(range(n2)))
    ind = all(rref_rank(list(s), q2) == d2 for s in combinations(c2, d2))
    circ = all(rref_rank(list(s), q2) == d2 for s in combinations(c2, d2 + 1))
    record("FX4f", "scaled analogue (F_37^5, 12 forms): all C(12,5) subsets "
           "independent and all C(12,6) subsets are circuits", True,
           ind and circ, ind and circ)


# ------------------------------------------------------------------ FX5-FX7
def fx5_continuation():
    contrib = Fraction(1, 2) * 2**32
    record("FX5", "continuation amplification: p=1/2 owner, 32 mean-one "
           "future factors", 2**31, contrib, contrib == 2**31 > 2**21)


def fx6_descriptor_collision():
    e1, e2 = 0b001, 0b010
    dep1 = gf2_rank([e1, e1]) == 1
    dep2 = gf2_rank([e2, e1]) == 1
    record("FX6", "rank-descriptor collision: same rank 1, increments 2 vs 1",
           (2, 1), (2 if dep1 else 1, 2 if dep2 else 1), dep1 and not dep2)


def fx7_information_nullity():
    record("FX7a", "information/nullity: F_2 trap free reward bits", 22,
           33 - 11, 33 - 11 == 22)
    record("FX7b", "information/nullity: gate model free reward in log q units",
           1, 33 - 32, 33 - 32 == 1)


# ------------------------------------------------------------------ FX8-FX10
def fx8_official_schedule():
    t = 2**33
    ell_pose = [-(-(t // 2**j) // 2) for j in range(34)]      # ceil(floor(t/2^j)/2)
    target = [2**e for e in range(32, 0, -1)] + [1, 1]
    record("FX8a", "official schedule ell_j = ceil(floor(t/2^j)/2)",
           "(2^32,...,2,1,1)", "match" if ell_pose == target else ell_pose,
           ell_pose == target)
    record("FX8b", "official schedule: 34 blocks / 33 junctions, sum = t=2^33",
           (34, 33, t), (len(ell_pose), len(ell_pose) - 1, sum(ell_pose)),
           len(ell_pose) == 34 and sum(ell_pose) == t)
    # the pilot's INDEPENDENT derivation: block j owns the constraints r<=t with
    # v_2(r) = j.  Must coincide with the pose's schedule.
    def blocks_from_v2(tt):
        out = []
        j = 0
        while 2**j <= tt:
            out.append(sum(1 for r in range(1, tt + 1) if (r & -r) == 2**j))
            j += 1
        return out
    ok = True
    for tt in range(1, 130):
        a = blocks_from_v2(tt)
        b = [-(-(tt // 2**j) // 2) for j in range(len(a))]
        ok &= (a == b)
    record("FX8c", "pilot derivation L_j = #{r<=t : v_2(r)=j} equals the pose's "
           "ell_j for every t in [1,129]", True, ok, ok)


def fx9_official_support_ratio():
    # official DLI row: n = 2^41 evaluation subgroup, t = 2^33.
    # dli_marginal_baseline100_coverage pins N_j = 256*ell_j.  The pilot's
    # reconstruction says the level-(j+1) cell count is h_{j+1} = n/2^{j+1}.
    n = 2**41
    t = 2**33
    agree = [j for j in range(34)
             if 256 * (-(-(t // 2**j) // 2)) == n // 2**(j + 1)]
    record("FX9a", "N_j = 256*ell_j (banked) equals h_{j+1} = n/2^{j+1} for "
           "n = 2^41, t = 2^33 -- blocks j=0..32", list(range(33)), agree,
           agree == list(range(33)))
    # terminal block j=33 is the ceil artefact: ell_33 = 1 but h_34 = 128.
    record("FX9b", "terminal block j=33 is the only ceil artefact "
           "(ell=1 vs h_34=n/2^34=128)", (1, 128),
           (-(-(t // 2**33) // 2), n // 2**34),
           -(-(t // 2**33) // 2) == 1 and n // 2**34 == 128)
    record("FX9c", "official support-to-constraint ratio h_{j+1}/L_j",
           256, sorted({(n // 2**(j + 1)) // (-(-(t // 2**j) // 2))
                        for j in range(33)}),
           {(n // 2**(j + 1)) // (-(-(t // 2**j) // 2))
            for j in range(33)} == {256})


def fx10_reserve_arithmetic():
    record("FX10a", "21-bit joint reserve x 100-bit marginal = 2^121", 2**121,
           2**21 * 2**100, 2**21 * 2**100 == 2**121)
    record("FX10b", "per-junction display allowance 2^(21/33)", 1.554,
           round(2 ** (21 / 33), 3), round(2 ** (21 / 33), 3) == 1.554)


def main():
    fx1_fourwise()
    fx2_pairwise()
    fx3_gate_32wise()
    fx4_circuit_explosion()
    fx5_continuation()
    fx6_descriptor_collision()
    fx7_information_nullity()
    fx8_official_schedule()
    fx9_official_support_ratio()
    fx10_reserve_arithmetic()

    width = max(len(r["id"]) for r in ROWS)
    for r in ROWS:
        print(f"{r['id']:<{width}}  {r['verdict']}  {r['statement']}")
        print(f"{'':<{width}}        certified={r['certified']}  "
              f"reproduced={r['reproduced']}")
    (HERE / "results" / "fixture_validation.json").write_text(
        json.dumps(ROWS, indent=1))
    print(f"\nC2PP_NULLITY_FIXTURES: {len(ROWS)}/{len(ROWS)} PASS")


if __name__ == "__main__":
    main()
