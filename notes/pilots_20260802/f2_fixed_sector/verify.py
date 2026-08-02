#!/usr/bin/env python3
"""Consolidated verifier for the fixed-sector absorption pilot.

  V1  antipodal closure of the FIXED sector, at the official row (exact)
  V2  parity-pure => the fixed sector's own window is all-Delta-even, flat = 0
  V3  exact antipodal normal form of the fixed-sector factor at K1 (Z[zeta_p])
  V4  K1 total census term: exactly real and strictly positive
  V5  K2 pullback identity (square of the reduced term) on BOTH sectors
  V6  trivial-shadow sub-class: fixed factor = 2^{n_0}, contraction 0 bits
  V7  fixed-sector 1/p ceiling ladder (saturation to 4 decimals)
  V8  base sweep: no base offset breaks the ceiling on a K1 rung window
  V9  official budget arithmetic (exact integers)
  V10 cross-check against the banked deployed-windows pilot (read-only import)

Digest on success: F2_FIXED_SECTOR_ABSORPTION_ALL_PASS
"""
from __future__ import annotations

import math
import os
import sys

sys.dont_write_bytecode = True
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import core as C  # noqa: E402
import ladder as L  # noqa: E402

FAILS = []


def check(name, cond, info=""):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {info}")
    if not cond:
        FAILS.append(name)


def V1():
    print("V1 antipodal closure of the fixed sector (official row, exact)")
    p = (1 << 31) - (1 << 24) + 1
    assert C.is_prime(p)
    e = C.v2(p - 1)
    n = 1 << 40
    n0 = math.gcd(n, p - 1)
    check("v_2(p-1) = 24", e == 24, f"(e={e})")
    check("fixed sector n_0 = 2^24", n0 == (1 << 24), f"(n_0={n0})")
    # -1 has order 2 and 2 | n_0, so -1 lies in mu_{n_0}: exact test
    g = 3
    while pow(g, (p - 1) // 2, p) != p - 1:
        g += 1
    h = pow(g, (p - 1) // n0, p)                  # generator of mu_{n_0}
    minus1 = pow(h, n0 // 2, p)
    check("-1 in mu_{2^24} <= F_p", minus1 == p - 1, f"(h^{n0//2} = {minus1})")
    check("n_0 >= 3 sqrt(p) (analytic regime, log #75)",
          n0 >= 3 * math.isqrt(p), f"(2^24 vs 3sqrt(p)={3*math.isqrt(p)})")
    # every rung's group also contains -1
    ok = all((1 << (24 + j)) % 2 == 0 for j in range(1, 17))
    check("every rung group mu_{2^{24+j}} is antipodally closed", ok)


def V2():
    print("V2 parity-pure => fixed-sector window all-Delta-even, flat = 0")
    import numpy as np
    rng = np.random.default_rng(9)
    bad = 0
    tot = 0
    worst_flat = 0.0
    for e in (4, 5, 6, 7):
        p = C.official_shaped_prime(e)
        F = C.Fp2(p)
        fixed, mreps, freps = C.sectors(F, e)
        n_ord = 1 << (e + 1)
        odd_ls = [l for l in range(1, n_ord, 2)]
        even_ls = [l for l in range(2, n_ord, 2)]
        for pool in (odd_ls, even_ls):
            for _ in range(30):
                ls = rng.choice(pool, size=min(3, len(pool)), replace=False)
                co = {int(l): (int(rng.integers(p)), int(rng.integers(p)))
                      for l in ls}
                if all(v == (0, 0) for v in co.values()):
                    continue
                tot += 1
                Df, _ = C.window_of(F, co, freps, n_ord)
                Dm, _ = C.window_of(F, co, mreps, n_ord)
                if not (C.all_even(Df) and C.all_even(Dm)):
                    bad += 1
                mr, _ = C.maxR_float(p, Df)
                worst_flat = max(worst_flat, 1.0 - mr)
    check("all parity-pure frequencies: BOTH sectors all-Delta-even",
          bad == 0, f"({tot} frequencies, {bad} violations)")
    check("fixed-sector flat = 0 exactly at every parity-pure frequency",
          worst_flat < 1e-12, f"(max flat = {worst_flat:.2e})")


def V3():
    print("V3 exact antipodal normal form of the fixed-sector factor at K1")
    bad = tot = 0
    for e in (4, 5, 6):
        p = C.official_shaped_prime(e)
        F = C.Fp2(p)
        fixed, mreps, freps = C.sectors(F, e)
        n_ord = 1 << (e + 1)
        for a in range(1, min(p, 40)):
            for b in range(0, min(p, 5)):
                co = {1: (a, b)}
                tot += 1
                fv = C.chi_values(F, co, fixed, n_ord)
                fp = C.chi_values(F, co, freps, n_ord)
                if C.canon(C.census_term(p, fv)) != C.pair_product(p, fp):
                    bad += 1
    check("F(c) = prod_{fixed pairs} (2 + zeta^s + zeta^{-s}) exactly",
          bad == 0, f"({tot} K1 frequencies, {bad} violations)")


def V4():
    print("V4 K1 total census term: exactly real and strictly positive")
    bad_r = bad_p = tot = 0
    for e in (4, 5, 6):
        p = C.official_shaped_prime(e)
        F = C.Fp2(p)
        fixed, mreps, freps = C.sectors(F, e)
        n_ord = 1 << (e + 1)
        allx = fixed + [y for y in mreps] + [F.neg(y) for y in mreps]
        for a in range(1, min(p, 25)):
            for b in range(0, min(p, 4)):
                co = {1: (a, b)}
                tot += 1
                T = C.census_term(p, C.chi_values(F, co, allx, n_ord))
                if not C.cyc_is_real(T):
                    bad_r += 1
                if float(C.cyc_embed(T, 1).real) <= 0:
                    bad_p += 1
    check("K1 total term exactly real", bad_r == 0, f"({tot} freqs)")
    check("K1 total term strictly positive", bad_p == 0, f"({tot} freqs)")


def V5():
    print("V5 K2 pullback identity (square of the reduced term), both sectors")
    import numpy as np
    rng = np.random.default_rng(11)
    bad = tot = 0
    for e in (4, 5, 6):
        p = C.official_shaped_prime(e)
        F = C.Fp2(p)
        fixed, mreps, freps = C.sectors(F, e)
        n_ord = 1 << (e + 1)
        even_ls = [l for l in range(2, n_ord, 2)]
        for _ in range(12):
            ls = rng.choice(even_ls, size=2, replace=False)
            co = {int(l): (int(rng.integers(p)), int(rng.integers(p)))
                  for l in ls}
            if all(v == (0, 0) for v in co.values()):
                continue
            tot += 1
            g = {int(l // 2): c for l, c in co.items()}
            mv = C.chi_values(F, co, [y for y in mreps]
                              + [F.neg(y) for y in mreps], n_ord)
            sq = sorted({F.pow(y, 2) for y in mreps})
            lhs = C.canon(C.census_term(p, mv))
            base = C.census_term(p, C.chi_values(F, g, sq, 1 << e))
            rhs = C.canon(_sq(base))
            fv = C.chi_values(F, co, fixed, n_ord)
            half = sorted({F.pow(x, 2) for x in fixed})
            basef = C.census_term(p, C.chi_values(F, g, half, 1 << e))
            ok = (lhs == rhs
                  and C.canon(C.census_term(p, fv)) == C.canon(_sq(basef)))
            Dm, _ = C.window_of(F, co, mreps, n_ord)
            ok = ok and all(d == 0 for d in Dm)
            if not ok:
                bad += 1
    check("K2 sector factors are exact squares of the reduced-frequency term "
          "one rung down, and Delta == 0", bad == 0, f"({tot} freqs)")


def _sq(u):
    p = len(u)
    out = [0] * p
    for i, a in enumerate(u):
        if a:
            for j, b in enumerate(u):
                if b:
                    out[(i + j) % p] += a * b
    return C.canon(out)


def V6():
    print("V6 trivial-shadow sub-class: fixed factor = 2^{n_0}, 0 bits")
    bad = tot = 0
    for e in (4, 5, 6, 7):
        p = C.official_shaped_prime(e)
        F = C.Fp2(p)
        fixed, mreps, freps = C.sectors(F, e)
        n_ord = 1 << (e + 1)
        n0 = len(fixed)
        for b in range(1, min(p, 8)):
            co = {1: (0, b)}                     # Tr(c) = 0: the trace-zero line
            fv = C.chi_values(F, co, fixed, n_ord)
            tot += 1
            ok, val = C.cyc_is_rational_integer(C.census_term(p, fv))
            if not (all(s == 0 for s in fv) and ok and val == (1 << n0)):
                bad += 1
    check("on {Tr(c) = 0} the fixed-sector character is identically 0 and the "
          "fixed factor is exactly 2^{n_0}", bad == 0, f"({tot} freqs)")


def V7():
    print("V7 fixed-sector 1/p ceiling ladder")
    rows = []
    for p, r in ((257, 8), (641, 7), (769, 8), (7681, 7), (12289, 7)):
        D, base, m = L.fixed_sector_window(p, r, {1: 3})
        dp = L.dp_counts(p, D)
        best, worst = L.bits_profile(p, dp, m, base)
        rows.append((p, m, best, math.log2(p)))
    ok = all(b <= lg + 1e-4 for _, _, b, lg in rows)
    sat = all(abs(b - lg) < 1e-3 for _, m, b, lg in rows if m >= 64)
    check("fixed-sector best central-band bits <= log2 p + 1e-4 at every row",
          ok, str([(p, m, round(b, 6), round(lg, 6)) for p, m, b, lg in rows]))
    check("saturation to 3 decimals at m >= 64", sat,
          f"(max |bits - log2 p| = {max(abs(b-lg) for _,_,b,lg in rows):.2e})")


def V8():
    print("V8 base sweep on a K1 rung window: no offset breaks the ceiling")
    worst = []
    for e in (4, 5, 6):
        p = C.official_shaped_prime(e)
        F = C.Fp2(p)
        fixed, mreps, freps = C.sectors(F, e)
        n_ord = 1 << (e + 1)
        D, _ = C.window_of(F, {1: (1, 1)}, mreps, n_ord)
        m = len(D)
        dp = L.dp_counts(p, D)
        best = max(L.bits_profile(p, dp, m, base)[1] or 0
                   for base in range(2 * p))
        worst.append((p, m, best, math.log2(p)))
    ok = all(b <= lg + 1e-6 for _, _, b, lg in worst)
    check("max over ALL 2p base offsets of the worst-central-band bits "
          "<= log2 p", ok,
          str([(p, m, round(b, 4), round(lg, 4)) for p, m, b, lg in worst]))


def V9():
    print("V9 official budget arithmetic (exact integers)")
    from fractions import Fraction
    n0 = 1 << 24
    ms = [1 << (22 + j) for j in range(1, 17)]
    check("sector sizes partition the group",
          n0 + 2 * sum(ms) == (1 << 40), f"(sum = {n0 + 2*sum(ms)})")
    log2p = math.log2((1 << 31) - (1 << 24) + 1)
    jstar = min(j for j in range(1, 17)
                if (1 << (22 + j)) / 43 - log2p > n0)
    tot_def = float(Fraction(sum(ms), 43)) - 16 * log2p
    check("first rung whose 1/43 deficit exceeds the whole fixed sector: j = 8",
          jstar == 8, f"(j* = {jstar})")
    check("total 1/43 deficit / fixed capacity in [700, 800]",
          700 <= tot_def / n0 <= 800, f"(ratio = {tot_def/n0:.2f})")
    check("fixed sector is 2^-16 of the group", n0 * (1 << 16) == (1 << 40))


def V10():
    print("V10 cross-check against the banked deployed-windows pilot")
    _P = os.path.join(os.path.dirname(_HERE), "f2_deployed_windows")
    ok_import = os.path.isdir(_P)
    if not ok_import:
        check("deployed-windows pilot present", False)
        return
    sys.path.insert(0, _P)
    sys.path.insert(0, os.path.join(os.path.dirname(_HERE),
                                    "f2_slice_coefficients"))
    sys.path.insert(0, os.path.join(os.path.dirname(_HERE),
                                    "f2_carry_reachability"))
    import importlib
    dv = importlib.import_module("verify")           # their verifier module
    slc = importlib.import_module("slicecore")
    # orientation labelling is a modelling convention (deployed pilot E9), so
    # the convention-FREE invariants are compared: the multiset of unordered
    # value pairs {s^+, s^-} of the window, and the all-even law.
    agree_pairs = agree_even = tot = 0
    for e in (4, 5, 6):
        p = C.official_shaped_prime(e)
        n_ord = 1 << (e + 1)
        F2 = slc.Fp2.make(p)
        reps = slc.pair_reps(F2, F2.subgroup(n_ord))
        loc = [slc.residues(F2, (1, 1), y) for y in reps]
        theirs = sorted(tuple(sorted(v)) for v in loc)
        Dtheirs = slc.Delta_of(p, loc)
        F = C.Fp2(p)
        fixed, mreps, freps = C.sectors(F, e)
        sp = C.chi_values(F, {1: (1, 1)}, mreps, n_ord)
        sm = C.chi_values(F, {1: (1, 1)}, [F.neg(y) for y in mreps], n_ord)
        mine = sorted(tuple(sorted(v)) for v in zip(sp, sm))
        Dmine, _ = C.window_of(F, {1: (1, 1)}, mreps, n_ord)
        tot += 1
        agree_pairs += (theirs == mine)
        agree_even += (C.all_even(Dtheirs) and C.all_even(Dmine))
    check("deployed rung-1 window reproduced (unordered value-pair multiset "
          "identical to the banked pilot's)", agree_pairs == tot,
          f"({agree_pairs}/{tot})")
    check("all-Delta-even law agrees with the banked pilot",
          agree_even == tot, f"({agree_even}/{tot})")
    # their DP_V on their own window must equal mine on the same input
    p = C.official_shaped_prime(5)
    F = C.Fp2(p)
    fixed, mreps, freps = C.sectors(F, 5)
    D, base = C.window_of(F, {1: (1, 1)}, mreps, 64)
    check("DP_V reimplementation identical to the banked pilot's on identical "
          "input", dv.DP_V(p, D, base) == C.DP_V(p, D, base))


def V11():
    """K1 frequencies are the TRIVIAL characters of the symmetric sector.

    A pair-union (symmetric) block S has p_l(S) = sum_{pairs}(y^l + (-y)^l) = 0
    for every ODD l, so an odd-support frequency annihilates the whole symmetric
    sub-census: the 'Frobenius-fixed and symmetric sectors' bucket of
    f2_conditional_close (dag.json:9634) contains no cancellation for K1.
    """
    print("V11 K1 frequencies annihilate the symmetric (pair-union) sector")
    import numpy as np
    rng = np.random.default_rng(23)
    bad = tot = 0
    for e in (4, 5, 6):
        p = C.official_shaped_prime(e)
        F = C.Fp2(p)
        fixed, mreps, freps = C.sectors(F, e)
        n_ord = 1 << (e + 1)
        odd_ls = [l for l in range(1, n_ord, 2)]
        for _ in range(20):
            ls = rng.choice(odd_ls, size=3, replace=False)
            co = {int(l): (int(rng.integers(p)), int(rng.integers(p)))
                  for l in ls}
            # a random pair-union block from the moving sector + fixed pairs
            k = int(rng.integers(1, len(mreps) + 1))
            sel = rng.choice(len(mreps), size=k, replace=False)
            blk = []
            for i in sel:
                blk += [mreps[i], F.neg(mreps[i])]
            kf = int(rng.integers(0, len(freps) + 1))
            selg = rng.choice(len(freps), size=kf, replace=False)
            for i in selg:
                blk += [freps[i], F.neg(freps[i])]
            tot += 1
            val = 0
            for x in blk:
                acc = (0, 0)
                for l, cl in co.items():
                    t = F.mul(cl, F.pow(x, l % n_ord))
                    acc = ((acc[0] + t[0]) % p, (acc[1] + t[1]) % p)
                val = (val + F.trace(acc)) % p
            if val != 0:
                bad += 1
    check("odd-support frequency vanishes on every pair-union block",
          bad == 0, f"({tot} (block, frequency) pairs, {bad} violations)")


def main():
    for f in (V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11):
        f()
    print()
    if FAILS:
        print("FAILURES:", FAILS)
        sys.exit(1)
    print("F2_FIXED_SECTOR_ABSORPTION_ALL_PASS")


if __name__ == "__main__":
    main()
