#!/usr/bin/env python3
"""Verifier for dli_norm_gate_splitting_law.

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 verify.py
Pure python integers / Fractions; no third-party imports.

Exact integer replay:
  A  S0  sigma_a is a SIGNED PERMUTATION of the basis {zeta^i}_{i<h}, hence
         maps W_w bijectively to W_w                        (the S1 engine)
  B  S1  phi(n) * #Sol_U = sum_{alpha in W_w} |H_U(alpha)|  (exact identity)
     plus the corollary that #Sol_U does not depend on which primitive
     n-th root of F_q is chosen
  C  S2  ratio = mbar/phi(n) >= 1/phi(n), with equality iff max|H_U| <= 1;
         deviation is upward only
  D  S3  q^{o+1} > maxnorm(phi(n),w)  =>  ratio EXACTLY 1/phi(n)
         (positive instances fire; S3 correctly abstains on every
         deviating row)
  E  banked-row reproduction: every scanned row matches the pilot's
     persisted counts exactly
  F  the S3 stabilizer hypothesis is load-bearing and its two proved
     sufficient conditions hold on the blocks used

Scanned subset of the pilot grid (the full 1960-row record is provenance:
notes/pilots_20260802/dli_norm_gate/results/splitting_*.json + analysis.json).
"""
from __future__ import annotations

import sys
from fractions import Fraction
from itertools import combinations, product

sys.dont_write_bytecode = True

FAILURES = []


def check(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
    if not ok:
        FAILURES.append(label)


# ----------------------------------------------------------------- arithmetic
def prime_factors(m):
    out, d = [], 2
    while d * d <= m:
        if m % d == 0:
            out.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        out.append(m)
    return out


def primitive_root(q):
    fs = prime_factors(q - 1)
    for g in range(2, q):
        if all(pow(g, (q - 1) // r, q) != 1 for r in fs):
            return g
    raise AssertionError("no primitive root")


def zeta_of_order(q, n, c=1):
    """c-th power of the deterministic root; c odd => another primitive root."""
    z = pow(pow(primitive_root(q), (q - 1) // n, q), c, q)
    assert pow(z, n, q) == 1 and pow(z, n // 2, q) != 1
    return z


def root_table(q, n, c=1):
    """P[k][i] = (zeta^{2k+1})^i mod q for the h odd residues."""
    h = n // 2
    z = zeta_of_order(q, n, c)
    return [[pow(pow(z, 2 * k + 1, q), i, q) for i in range(h)] for k in range(h)]


def u_masks(n, U):
    """mask[k] = bitmask of the set (2k+1)*U inside the odd-residue indexing."""
    h = n // 2
    idx = {2 * j + 1: j for j in range(h)}
    out = []
    for k in range(h):
        a = 2 * k + 1
        mk = 0
        for u in U:
            mk |= 1 << idx[(a * u) % n]
        out.append(mk)
    return out


def scan(n, q, w, U, c=1):
    """Exact counts over the ternary weight-w vectors supported in [0,h)."""
    h = n // 2
    P = root_table(q, n, c)
    UM = u_masks(n, U)
    n_vec = n_sol = n_hit = sum_H = n_div = max_m = max_H = 0
    for S in combinations(range(h), w):
        # per root: the 2^w signed sums, built by doubling (2^w adds, not 2^w*w)
        zmask = [0] * (1 << w)
        for k, row in enumerate(P):
            sums = [0]
            for i in S:
                pi = row[i]
                sums = [s + pi for s in sums] + [s - pi for s in sums]
            bit = 1 << k
            for t, s in enumerate(sums):
                if s % q == 0:
                    zmask[t] |= bit
        n_vec += 1 << w
        for Z in zmask:
            if not Z:
                continue
            n_div += 1
            m = bin(Z).count("1")
            if m > max_m:
                max_m = m
            hc = 0
            for mk in UM:
                if Z & mk == mk:
                    hc += 1
            if hc:
                n_hit += 1
                sum_H += hc
                if hc > max_H:
                    max_H = hc
            if Z & UM[0] == UM[0]:
                n_sol += 1
    return {"n": n, "q": q, "w": w, "U": tuple(U), "phi": h, "n_vectors": n_vec,
            "n_solutions": n_sol, "n_H_nonempty": n_hit, "sum_H": sum_H,
            "n_norm_divisible": n_div, "max_m": max_m, "max_H": max_H}


# ----------------------------------------------- banked tables and expectations
# banked C1 maxnorm(phi(n), w), indexed by n then w
# (dli_c1_ternary_relation_norm_sandwich + notes/.../dli_norm_gate/scripts)
MAXNORM = {
    16: {1: 1, 2: 16, 3: 81, 4: 196, 5: 529, 6: 1154, 7: 2401, 8: 2176},
    32: {1: 1, 2: 256, 3: 6561, 4: 38416, 5: 279841, 6: 1331716, 7: 5764801,
         8: 14760962},
    64: {1: 1, 2: 65536, 3: 43046721, 4: 1475789056},
}

# banked scan rows: (n, q, U, w) -> (n_solutions, n_H_nonempty, sum_H, max_m,
# max_H).  Source: notes/pilots_20260802/dli_norm_gate/results/
# splitting_n16.json, splitting_n16_o.json, splitting_n32.json,
# splitting_n64.json.
BANKED = {
    (16, 17, (1,), 1): (0, 0, 0, 0, 0),
    (16, 17, (1,), 2): (0, 0, 0, 0, 0),
    (16, 17, (1,), 3): (32, 256, 256, 1, 1),
    (16, 17, (1,), 4): (80, 640, 640, 1, 1),
    (16, 17, (1,), 5): (96, 640, 768, 2, 2),
    (16, 17, (1,), 6): (96, 576, 768, 2, 2),
    (16, 17, (1,), 7): (64, 320, 512, 2, 2),
    (16, 17, (1,), 8): (16, 128, 128, 1, 1),
    (16, 97, (1,), 3): (0, 0, 0, 0, 0),
    (16, 97, (1,), 4): (16, 128, 128, 1, 1),
    (16, 97, (1,), 5): (16, 128, 128, 1, 1),
    (16, 97, (1,), 6): (16, 128, 128, 1, 1),
    (16, 97, (1,), 7): (16, 128, 128, 1, 1),
    (16, 97, (1,), 8): (0, 0, 0, 0, 0),
    (16, 113, (1,), 5): (32, 256, 256, 1, 1),
    (16, 113, (1,), 6): (16, 128, 128, 1, 1),
    (16, 113, (1,), 7): (16, 128, 128, 1, 1),
    (16, 17, (1, 3), 5): (0, 0, 0, 2, 0),
    (16, 17, (1, 3), 6): (16, 128, 128, 2, 1),
    (16, 17, (1, 3), 7): (0, 0, 0, 2, 0),
    (16, 17, (1, 3), 8): (0, 0, 0, 1, 0),
    (32, 97, (1,), 3): (64, 1024, 1024, 1, 1),
    (32, 97, (1,), 4): (288, 4096, 4608, 2, 2),
    (32, 97, (1,), 5): (1280, 15872, 20480, 2, 2),
    (32, 97, (1, 3), 5): (64, 1024, 1024, 2, 1),
    (32, 193, (1,), 3): (32, 512, 512, 1, 1),
    (32, 193, (1,), 4): (128, 2048, 2048, 1, 1),
    (32, 193, (1,), 5): (640, 8704, 10240, 2, 2),
    (64, 257, (1,), 3): (128, 3072, 4096, 2, 2),
    (64, 449, (1,), 3): (64, 1024, 2048, 2, 2),
}


def main():
    # ---------------- A: S0, the signed-permutation lemma
    bad = tot = 0
    for h in (4, 8, 16, 32):
        n = 2 * h
        for a in range(1, n, 2):
            tot += 1
            images = []
            for i in range(h):
                e = (a * i) % n
                images.append((e % h, -1 if e >= h else 1))
            if sorted(p for p, _ in images) != list(range(h)):
                bad += 1
            if any(s not in (1, -1) for _, s in images):
                bad += 1
    check("A: S0 -- sigma_a: zeta^i -> zeta^{ai} is a SIGNED PERMUTATION of "
          "the basis {zeta^i}_{i<h} (h = 4,8,16,32), so it preserves ternary "
          "support size and coefficients up to sign", bad == 0,
          f"{tot} (h, a) pairs, {bad} violations")

    # ---------------- B/C/D/E: the scan grid
    rows = []
    for (n, q, U, w) in sorted(BANKED):
        rows.append(scan(n, q, w, list(U)))

    # E: banked reproduction
    bad = 0
    for r in rows:
        key = (r["n"], r["q"], r["U"], r["w"])
        got = (r["n_solutions"], r["n_H_nonempty"], r["sum_H"],
               r["max_m"], r["max_H"])
        if got != BANKED[key]:
            bad += 1
    check("E: banked-row reproduction -- independent recomputation matches the "
          "pilot's persisted counts (n_solutions, n_H_nonempty, sum_H, max_m, "
          "max_H) exactly", bad == 0,
          f"{len(rows)} rows across n = 16, 32, 64 and o = 1, 2; "
          f"{bad} mismatches")

    # B: S1 identity
    bad = 0
    for r in rows:
        if r["phi"] * r["n_solutions"] != r["sum_H"]:
            bad += 1
    check("B: S1 identity  phi(n) * #Sol_U = sum_{alpha in W_w} |H_U(alpha)|",
          bad == 0, f"{len(rows)} rows, {bad} violations")

    # B: S1 corollary -- #Sol is independent of the primitive root chosen
    base = scan(16, 97, 5, [1])
    bad = 0
    variants = []
    for c in range(1, 16, 2):
        r = scan(16, 97, 5, [1], c=c)
        variants.append(r["n_solutions"])
        if (r["n_solutions"], r["n_H_nonempty"], r["sum_H"]) != (
                base["n_solutions"], base["n_H_nonempty"], base["sum_H"]):
            bad += 1
    check("B: S1 corollary -- #Sol_U, #{H_U != 0} and sum|H_U| are the same "
          "for ALL phi(n) choices of the primitive n-th root at (n,q,w) = "
          "(16,97,5)", bad == 0, f"counts {variants}")

    # C: S2 -- ratio = mbar/phi, >= 1/phi, equality iff max|H| <= 1
    bad_id = bad_ineq = bad_eq = 0
    dev = []
    for r in rows:
        if not r["n_H_nonempty"]:
            continue
        ratio = Fraction(r["n_solutions"], r["n_H_nonempty"])
        mbar = Fraction(r["sum_H"], r["n_H_nonempty"])
        if ratio != mbar / r["phi"]:
            bad_id += 1
        if ratio < Fraction(1, r["phi"]):
            bad_ineq += 1
        exact = (ratio == Fraction(1, r["phi"]))
        if exact != (r["max_H"] <= 1):
            bad_eq += 1
        if not exact:
            dev.append(f"(n={r['n']},q={r['q']},w={r['w']},U={r['U']}) "
                       f"ratio*phi={ratio * r['phi']}")
    nz = sum(1 for r in rows if r["n_H_nonempty"])
    check("C: S2 identity  #Sol/#{H_U != 0} = mbar/phi(n)", bad_id == 0,
          f"{nz} nonempty rows, {bad_id} violations")
    check("C: S2 inequality  ratio >= 1/phi(n) -- deviation is UPWARD only",
          bad_ineq == 0, f"{nz} nonempty rows, {bad_ineq} violations")
    check("C: S2 equality condition  ratio = 1/phi(n)  <=>  max|H_U| <= 1",
          bad_eq == 0,
          f"{nz} nonempty rows, {len(dev)} deviating: " + "; ".join(dev))

    # D: S3
    fired = abstained = bad = 0
    for r in rows:
        if not r["n_H_nonempty"]:
            continue
        mx = MAXNORM.get(r["n"], {}).get(r["w"])
        if mx is None:
            continue
        o = len(r["U"])
        exact = (Fraction(r["n_solutions"], r["n_H_nonempty"])
                 == Fraction(1, r["phi"]))
        if r["q"] ** (o + 1) > mx:
            fired += 1
            if not exact:
                bad += 1
        else:
            abstained += 1
            if exact:
                pass          # allowed: S3 is sufficient, not necessary
    check("D: S3  q^{o+1} > maxnorm(phi(n),w)  =>  ratio EXACTLY 1/phi(n)",
          bad == 0, f"{fired} rows satisfy S3's condition (all exact), "
                    f"{abstained} rows do not (S3 abstains); {bad} violations")
    # every deviating row must FAIL S3's condition
    bad = 0
    for r in rows:
        if not r["n_H_nonempty"]:
            continue
        mx = MAXNORM.get(r["n"], {}).get(r["w"])
        exact = (Fraction(r["n_solutions"], r["n_H_nonempty"])
                 == Fraction(1, r["phi"]))
        if not exact and mx is not None and r["q"] ** (len(r["U"]) + 1) > mx:
            bad += 1
    check("D: every deviating row fails S3's condition (no exception)",
          bad == 0, f"{len(dev)} deviating rows, {bad} that should have been "
                    "exact")
    # and every deviating row has max_m >= o+1, which is the mechanism
    bad = 0
    for r in rows:
        if r["n_H_nonempty"] and r["max_H"] > 1 and r["max_m"] < len(r["U"]) + 1:
            bad += 1
    check("D: mechanism -- max|H_U| >= 2 forces m(alpha) >= o+1 on every "
          "deviating row", bad == 0, f"{bad} violations")

    # ---------------- F: the S3 stabilizer hypothesis
    def stab(n, U):
        Us = frozenset(U)
        return [b for b in range(1, n, 2)
                if frozenset((b * u) % n for u in Us) == Us]

    ok = all(stab(n, U) == [1] for (n, q, U, w) in BANKED)
    check("F: Stab(U) = {1} for every block used in the scan (the S3 "
          "hypothesis holds where S3 is applied)", ok,
          "U = {1} and U = {1,3} at n = 16, 32, 64")

    # proved sufficient condition: max(U)^2 < n
    ok = True
    for n in (16, 32, 64, 128):
        for L in range(1, n // 2 + 1):
            U = list(range(1, 2 * L, 2))
            if (2 * L - 1) ** 2 < n and stab(n, U) != [1]:
                ok = False
    check("F: proved sufficient condition max(U)^2 < n implies Stab(U) = {1} "
          "(spot-checked at n = 16,32,64,128 over all L)", ok)

    # the hypothesis is LOAD-BEARING: the two exceptional block sizes
    exc = []
    for n in (16, 32, 64, 128):
        for L in range(1, n // 2 + 1):
            s = stab(n, list(range(1, 2 * L, 2)))
            if s != [1]:
                exc.append((n, L, tuple(s)))
    expected = [(n, L, (1, n // 2 - 1) if L == n // 4 else
                 tuple(range(1, n, 2)))
                for n in (16, 32, 64, 128) for L in (n // 4, n // 2)]
    check("F: S3's stabilizer hypothesis is LOAD-BEARING -- for the block "
          "family U = {1,3,...,2L-1} it fails exactly at L = n/4 (Stab = "
          "{1, n/2-1}, the reflection u -> n/2-u) and L = n/2 (Stab = all), "
          "and nowhere else (exhaustive at n = 16,32,64,128)",
          exc == expected, f"{len(exc)} exceptional (n,L) pairs, as predicted")

    if FAILURES:
        print("FAILED CHECKS:", FAILURES)
        sys.exit(1)
    print("DLI_NORM_GATE_SPLITTING_LAW_ALL_PASS")


if __name__ == "__main__":
    main()
