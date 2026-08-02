#!/usr/bin/env python3
"""Brute-force validation of the F2 first-descent carry model (F2A.2).

Run:  tools/ramguard tiny -- python3 \
        notes/pilots_20260802/f2_carry_reachability/validate.py

Every VERDICT-relevant check (integrality of K, the delta identity, the
sumset recursion, Myhill-Nerode) is exact integer arithmetic.  The two
complex-analytic checks (sign factorisation, carry-DFT product identity)
are floating point with an explicit tolerance and are labelled NUMERIC.
"""

from __future__ import annotations

import cmath
import math
import os
import sys
from itertools import product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from f2model import (  # noqa: E402
    Fp2,
    carry_dft_abs,
    carry_mask,
    carry_sign,
    deltas,
    describe_structure,
    divisors,
    half_flag,
    is_prime,
    myhill_nerode_classes,
    pair_reps,
    residues,
    rot,
    suffix_sumsets,
    sumset_curve,
)

TOL = 1e-9


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def small_primes(lo: int, hi: int) -> list[int]:
    return [q for q in range(lo, hi + 1) if is_prime(q)]


def admissible_orders(p: int) -> list[int]:
    """Even n | p^2-1 with n not dividing p-1."""
    return [n for n in divisors(p * p - 1)
            if n % 2 == 0 and (p - 1) % n != 0]


# ------------------------------------------------------------- checks -----


def check_field_axioms() -> None:
    for p in small_primes(3, 41):
        F = Fp2.make(p)
        require(pow(F.N, (p - 1) // 2, p) == p - 1, f"N nonresidue p={p}")
        require(F.mul((0, 1), (0, 1)) == (F.N % p, 0), f"w^2=N p={p}")
        g = F.generator()
        require(F.order(g) == p * p - 1, f"generator order p={p}")
        # Frobenius is the nontrivial automorphism, fixes exactly F_p
        for a in range(p):
            for b in range(p):
                x = (a, b)
                require(F.frob(F.frob(x)) == x, "frob^2 = id")
                require(F.pow(x, p) == F.frob(x), f"x^p = frob p={p}")
        fixed = sum(1 for a in range(p) for b in range(p)
                    if F.frob((a, b)) == (a, b))
        require(fixed == p, f"frobenius fixed field size p={p}")
    print("F2A2_V1_FIELD_PASS  exact_Fp2_arithmetic_and_frobenius")


def check_subgroups_and_pairs() -> None:
    for p in small_primes(3, 31):
        F = Fp2.make(p)
        for n in admissible_orders(p)[:6]:
            mu = F.subgroup(n)
            require(len(set(mu)) == n, f"subgroup size p={p} n={n}")
            for x in mu:
                require(F.pow(x, n) == (1, 0), "subgroup exponent")
                require(F.frob(x) in set(mu), "frobenius stable")
            g0 = math.gcd(n, p - 1)
            fixed = [x for x in mu if x[1] == 0]
            require(len(fixed) == g0, f"|mu_n cap F_p| p={p} n={n}")
            reps = pair_reps(F, mu)
            require(len(reps) == (n - g0) // 2, "pair count")
            seen = set()
            for y in reps:
                require(y[1] != 0, "moving rep")
                require(F.frob(y) != y, "genuine pair")
                key = frozenset((y, F.frob(y)))
                require(key not in seen, "one rep per pair")
                seen.add(key)
            if n > 1:
                tot = (0, 0)
                for x in mu:
                    tot = ((tot[0] + x[0]) % p, (tot[1] + x[1]) % p)
                require(tot == (0, 0), f"sum over mu_n = 0 p={p} n={n}")
    print("F2A2_V2_SUBGROUP_PASS  pair_decomposition_and_vanishing_sum")


def check_carry_integrality_and_sign() -> None:
    """K integral (exact) + eps_c = (-1)^{K+U} against the complex product."""
    max_err = 0.0
    rows = 0
    for p in small_primes(5, 23):
        F = Fp2.make(p)
        for n in admissible_orders(p)[:4]:
            mu = F.subgroup(n)
            for c in [(1, 0), (0, 1), (1, 1), (2, 3)]:
                c = (c[0] % p, c[1] % p)
                if c == (0, 0):
                    continue
                svals = [F.trace(F.mul(c, x)) for x in mu]
                total = sum(svals)
                require(total % p == 0, f"K integral p={p} n={n} c={c}")
                K = total // p
                U = sum(half_flag(p, s) for s in svals)
                eps = (-1) ** ((K + U) % 2)
                # carry parity only depends on the sum mod 2p
                require(carry_sign(p, total % (2 * p)) == (-1) ** (K % 2),
                        "carry sign from residue mod 2p")
                prod = 1 + 0j
                mag = 1.0
                for s in svals:
                    prod *= 1 + cmath.exp(2j * math.pi * s / p)
                    mag *= 2 * abs(math.cos(math.pi * s / p))
                require(abs(prod.imag) < 1e-6 * max(1.0, abs(prod)),
                        "product is real")
                max_err = max(max_err, abs(prod.real - eps * mag)
                              / max(1.0, mag))
                rows += 1
    require(max_err < 1e-9, f"sign factorisation err {max_err}")
    print(f"F2A2_V3_SIGN_PASS  rows={rows} NUMERIC max_rel_err={max_err:.2e}")


def check_delta_identity() -> None:
    """delta_i = 4 N b_c b_y (mod p); and delta in {D, D+p} mod 2p."""
    for p in small_primes(5, 47):
        F = Fp2.make(p)
        for n in admissible_orders(p)[:5]:
            mu = F.subgroup(n)
            reps = pair_reps(F, mu)
            for c in [(1, 0), (0, 1), (1, 1), (3, 2), (0, 2)]:
                c = (c[0] % p, c[1] % p)
                if c == (0, 0):
                    continue
                ds = deltas(F, c, reps)
                for y, d in zip(reps, ds):
                    D = (4 * F.N * c[1] * y[1]) % p
                    require(d % p == D, f"delta mod p p={p} c={c}")
                    require(d % (2 * p) in (D, (D + p) % (2 * p)),
                            "delta lift")
                    sp, sm = residues(F, c, y)
                    require((sp + sm) % p == (4 * c[0] * y[0]) % p,
                            "conjugate residue sum identity")
                    if c[1] == 0:
                        require(d == 0, "c in F_p => delta = 0")
                    if c[0] == 0:
                        require(d % 2 == 1, "trace-zero c => delta odd")
    print("F2A2_V4_DELTA_PASS  algebraic_delta_identity_exact")


def check_sumset_bruteforce() -> None:
    """Bitmask sumset recursion == brute-force orientation enumeration."""
    checked = 0
    for p in small_primes(5, 29):
        F = Fp2.make(p)
        two_p = 2 * p
        for n in admissible_orders(p)[:5]:
            mu = F.subgroup(n)
            reps = pair_reps(F, mu)
            if len(reps) > 13:
                reps = reps[:13]
            for c in [(0, 1), (1, 1), (2, 1)]:
                c = (c[0] % p, c[1] % p)
                ds = deltas(F, c, reps)
                sizes, S, _ = sumset_curve(ds, two_p)
                for k in range(len(sizes)):
                    brute = set()
                    for choice in product((0, 1), repeat=k):
                        brute.add(sum(d for d, ch in zip(ds[:k], choice)
                                      if ch) % two_p)
                    require(len(brute) == sizes[k],
                            f"sumset size p={p} n={n} c={c} k={k}")
                    if k == len(sizes) - 1:
                        mask = 0
                        for r in brute:
                            mask |= 1 << r
                        require(mask == S, "terminal mask")
                checked += 1
                # reachable partial sums == base + sumset
                base = 0
                for y in reps:
                    base += residues(F, c, y)[1]
                brute = set()
                for choice in product((0, 1), repeat=len(reps)):
                    tot = 0
                    for y, ch in zip(reps, choice):
                        sp, sm = residues(F, c, y)
                        tot += sp if ch else sm
                    brute.add(tot % two_p)
                shifted = {(r - base) % two_p for r in brute}
                require({i for i in range(two_p) if (S >> i) & 1} == shifted,
                        "partial sums = base + sumset")
    print(f"F2A2_V5_SUMSET_PASS  bruteforce_cases={checked}")


def check_myhill_nerode_full() -> None:
    """Re-verify the audit: with FULL continuations all 2p states differ."""
    for p in (3, 5, 7, 11, 13):
        two_p = 2 * p
        full = (1 << two_p) - 1
        q = myhill_nerode_classes(p, full, full)
        require(q == two_p, f"full-continuation MN classes p={p}")
        # equivalently: h has no nontrivial translation stabiliser
        H = carry_mask(p)
        for t in range(1, two_p):
            require(rot(H, t, two_p, full) != H, "translation stabiliser")
    print("F2A2_V6_MYHILL_NERODE_PASS  all_2p_states_distinct_under_full_C")


def check_suffix_and_quotient() -> None:
    """Suffix sumsets and the reachable-continuation quotient, brute forced."""
    for p in (5, 7, 11):
        F = Fp2.make(p)
        two_p = 2 * p
        for n in admissible_orders(p)[:3]:
            mu = F.subgroup(n)
            reps = pair_reps(F, mu)[:10]
            ds = deltas(F, (1, 1), reps)
            C = suffix_sumsets(ds, two_p)
            m = len(ds)
            for k in range(m + 1):
                brute = set()
                for choice in product((0, 1), repeat=m - k):
                    brute.add(sum(d for d, ch in zip(ds[k:], choice)
                                  if ch) % two_p)
                mask = 0
                for r in brute:
                    mask |= 1 << r
                require(mask == C[k], f"suffix mask p={p} k={k}")
            # quotient count by direct signature comparison
            for k in range(m + 1):
                pre_sizes, Pmask, _ = sumset_curve(ds[:k], two_p)
                pre = [i for i in range(two_p) if (Pmask >> i) & 1]
                suf = [i for i in range(two_p) if (C[k] >> i) & 1]
                sigs = {tuple(carry_sign(p, r + t) for t in suf) for r in pre}
                require(len(sigs) == myhill_nerode_classes(p, Pmask, C[k]),
                        f"quotient p={p} k={k}")
    print("F2A2_V7_QUOTIENT_PASS  suffix_sets_and_MN_quotient_bruteforced")


def check_carry_dft_formula() -> None:
    for p in (5, 11, 23):
        two_p = 2 * p
        h = [1.0 if r < p else -1.0 for r in range(two_p)]
        H = [sum(h[r] * cmath.exp(-2j * math.pi * k * r / two_p)
                 for r in range(two_p)) for k in range(two_p)]
        pred = carry_dft_abs(p)
        for k in range(two_p):
            require(abs(abs(H[k]) - pred[k]) < 1e-8,
                    f"|hhat| formula p={p} k={k}")
            if k % 2 == 0:
                require(abs(H[k]) < 1e-9, "even mode vanishes")
    print("F2A2_V8_DFT_PASS  |hhat_p(k)|=2/|sin(pi k/2p)|_on_odd_modes")


def check_product_identity_real_model() -> None:
    """The state-free carry-DFT product identity, on the ACTUAL F_{p^2} model."""
    worst = 0.0
    cases = 0
    for p in (5, 7, 11, 13):
        F = Fp2.make(p)
        two_p = 2 * p
        for n in admissible_orders(p)[:3]:
            mu = F.subgroup(n)
            reps = pair_reps(F, mu)[:9]
            if not reps:
                continue
            for c in [(0, 1), (1, 1), (1, 0)]:
                c = (c[0] % p, c[1] % p)
                locals_ = []
                for y in reps:
                    sp, sm = residues(F, c, y)
                    ap = 2 * abs(math.cos(math.pi * sp / p))
                    am = 2 * abs(math.cos(math.pi * sm / p))
                    locals_.append(((sp, half_flag(p, sp), ap),
                                    (sm, half_flag(p, sm), am)))
                direct = 0.0
                for choice in product((0, 1), repeat=len(locals_)):
                    r = 0
                    par = 0
                    wt = 1.0
                    for i, ch in enumerate(choice):
                        s, u, a = locals_[i][ch]
                        r += s
                        par ^= u
                        wt *= a
                    direct += carry_sign(p, r) * ((-1) ** par) * wt
                H = [sum((1.0 if r < p else -1.0)
                         * cmath.exp(-2j * math.pi * k * r / two_p)
                         for r in range(two_p)) for k in range(two_p)]
                spectral = 0j
                for k in range(two_p):
                    prod = 1 + 0j
                    for rec in locals_:
                        loc = 0j
                        for s, u, a in rec:
                            loc += ((-1) ** u) * a * cmath.exp(
                                2j * math.pi * k * s / two_p)
                        prod *= loc
                    spectral += H[k] * prod
                spectral /= two_p
                scale = max(1.0, abs(direct))
                worst = max(worst, abs(direct - spectral.real) / scale,
                            abs(spectral.imag) / scale)
                cases += 1
    require(worst < 1e-6, f"product identity error {worst}")
    print(f"F2A2_V9_PRODUCT_IDENTITY_PASS  cases={cases} "
          f"NUMERIC max_rel_err={worst:.2e}")


def check_structure_classifier() -> None:
    two_p = 10
    require(describe_structure(0b1, two_p)["size"] == 1, "trivial")
    even = 0
    for i in range(0, two_p, 2):
        even |= 1 << i
    d = describe_structure(even, two_p)
    require(d["is_subgroup"] and d["index"] == 2, "even subgroup")
    d = describe_structure((1 << two_p) - 1, two_p)
    require(d["is_full"] and d["index"] == 1, "full group")
    print("F2A2_V10_CLASSIFIER_PASS  subgroup_classifier")


def main() -> None:
    check_field_axioms()
    check_subgroups_and_pairs()
    check_carry_integrality_and_sign()
    check_delta_identity()
    check_sumset_bruteforce()
    check_myhill_nerode_full()
    check_suffix_and_quotient()
    check_carry_dft_formula()
    check_product_identity_real_model()
    check_structure_classifier()
    print("F2A2_VALIDATION_ALL_PASS")


if __name__ == "__main__":
    main()
