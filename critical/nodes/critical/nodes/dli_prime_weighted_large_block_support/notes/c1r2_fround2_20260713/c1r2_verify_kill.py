#!/usr/bin/env python3
"""INDEPENDENT verification of the C1' F-round-2 KILL rows, using the VERBATIM
banked kernels (m1 signed_all_census + m2 primitive_orbit_count), a second E
path (asum), a DP total-mass invariant, brute-force weight-3 orbit witness, and
sympy primality. Runs on Modal (single worker). Exact-rational verdict.

Verbatim-copied (attributed):
  * signed_all_census, fiber_contribs, get_zeta, least_primitive_root
    <- critical/.../notes/m1_dli_m1_tower_census_modal.py
  * primitive_orbit_count, primitive_root, orbit_key
    <- critical/.../notes/m2_c1prime_level_scaled_modal.py
"""
from __future__ import annotations
import itertools
from fractions import Fraction
import numpy as np
from sympy import isprime

N = 32
NPRIME = 64


# ===== VERBATIM from m1_dli_m1_tower_census_modal.py =====
def least_primitive_root(q):
    x, d, fac = q - 1, 2, []
    while d * d <= x:
        while x % d == 0:
            fac.append(d); x //= d
        d += 1
    if x > 1:
        fac.append(x)
    fac = sorted(set(fac))
    return next(c for c in range(2, q) if all(pow(c, (q - 1) // r, q) != 1 for r in fac))


def get_zeta(q, n):
    assert (q - 1) % n == 0
    z = pow(least_primitive_root(q), (q - 1) // n, q)
    assert pow(z, n, q) == 1 and pow(z, n // 2, q) != 1
    return z


def fiber_contribs(q, n, t):
    h, e, o = n // 2, t // 2, (t + 1) // 2
    zeta = get_zeta(q, n)
    out = []
    for i in range(h):
        w = [pow(zeta, (2 * s * i) % n, q) for s in range(1, e + 1)]
        v = [pow(zeta, ((2 * s + 1) * i) % n, q) for s in range(o)]
        cN = tuple([0] * t)
        cB = tuple([2 * x % q for x in w] + [0] * o)
        cP = tuple(w + v)
        cM = tuple(w + [(q - x) % q for x in v])
        out.append((cN, cB, cP, cM))
    return out


def signed_all_census(q, n, t):
    h, e, o = n // 2, t // 2, (t + 1) // 2
    fib = fiber_contribs(q, n, t)
    axes = tuple(range(o))
    dp = np.zeros((q,) * o + (h + 1,), dtype=np.int64)
    dp[(0,) * o + (0,)] = 1
    for (cN, cB, cP, cM) in fib:
        new = 2 * dp
        tp = np.roll(dp, cP[e:], axis=axes)
        new[..., 1:] += tp[..., :-1]
        tm = np.roll(dp, cM[e:], axis=axes)
        new[..., 1:] += tm[..., :-1]
        dp = new
        assert int(dp.max()) < (1 << 61)
    return [int(x) for x in dp[(0,) * o]]


# ===== VERBATIM from m2_c1prime_level_scaled_modal.py =====
def primitive_root(q):
    remaining = q - 1
    factors = set()
    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors.add(divisor); remaining //= divisor
        divisor += 1
    if remaining > 1:
        factors.add(remaining)
    candidate = 2
    while any(pow(candidate, (q - 1) // factor, q) == 1 for factor in factors):
        candidate += 1
    return candidate


def orbit_key(vector):
    best = None
    for shift in range(2 * N):
        moved = [0] * N
        for exponent, coefficient in enumerate(vector):
            if coefficient == 0:
                continue
            target = (exponent + shift) % (2 * N)
            if target >= N:
                moved[target - N] -= coefficient
            else:
                moved[target] += coefficient
        key = tuple(moved)
        if best is None or key < best:
            best = key
    return best


def primitive_orbit_count(payload):
    q, level, weight = payload
    omega = pow(primitive_root(q), (q - 1) // NPRIME, q)
    odd_powers = [
        np.array([pow(omega, (2 * ell - 1) * exponent, q) for exponent in range(N)], dtype=np.int64)
        for ell in range(1, level + 1)
    ]
    signs = np.array(list(itertools.product((1, -1), repeat=weight - 1)), dtype=np.int64)
    signs = np.hstack([np.ones((len(signs), 1), dtype=np.int64), signs])
    combinations = itertools.combinations(range(N), weight)
    representatives = set()
    chunk_size = 100_000
    while True:
        chunk = list(itertools.islice(combinations, chunk_size))
        if not chunk:
            break
        supports = np.asarray(chunk, dtype=np.int64)
        hit_mask = np.ones((len(supports), len(signs)), dtype=bool)
        for powers in odd_powers:
            hit_mask &= (powers[supports] @ signs.T) % q == 0
        for support_index, sign_index in np.argwhere(hit_mask):
            support = tuple(int(value) for value in supports[support_index])
            signed = tuple(int(value) for value in signs[sign_index])
            primitive = True
            for subset_mask in range(1, (1 << weight) - 1):
                if all(sum(signed[index] * pow(omega, (2 * ell - 1) * support[index], q)
                           for index in range(weight) if (subset_mask >> index) & 1) % q != 0
                       for ell in range(1, level + 1)):
                    continue
                if all(sum(signed[index] * pow(omega, (2 * ell - 1) * support[index], q)
                           for index in range(weight) if (subset_mask >> index) & 1) % q == 0
                       for ell in range(1, level + 1)):
                    primitive = False
                    break
            if not primitive:
                continue
            vector = [0] * N
            for exponent, coefficient in zip(support, signed):
                vector[exponent] = coefficient
            representatives.add(orbit_key(tuple(vector)))
    return len(representatives)


# ===== independent A_total DP (my c1r2 path) with total-mass invariant =====
def a_total_and_invariant(q, L):
    z = get_zeta(q, NPRIME)
    dp = np.zeros((q,) * L, dtype=np.int64)
    dp[(0,) * L] = 1
    axes = tuple(range(L))
    for i in range(N):
        vp = tuple(pow(z, ((2 * ell - 1) * i) % NPRIME, q) for ell in range(1, L + 1))
        vm = tuple((q - x) % q for x in vp)
        dp = 2 * dp + np.roll(dp, vp, axis=axes) + np.roll(dp, vm, axis=axes)
    total = int(np.sum(dp, dtype=object))   # object dtype: 4^32=2^64 overflows int64
    assert total == 4 ** N, f"MASS INVARIANT FAIL q={q}: {total} != 4^{N}"
    return int(dp[(0,) * L])


def brute_weight3_orbits(q):
    """Independent pure-Python enumeration of weight-3 primitive vanisher orbits (L=1)."""
    omega = get_zeta(q, NPRIME)
    pw = [pow(omega, i, q) for i in range(N)]
    reps = set()
    for a in range(N):
        for b in range(a + 1, N):
            for c in range(b + 1, N):
                for sb in (1, -1):
                    for sc in (1, -1):
                        if (pw[a] + sb * pw[b] + sc * pw[c]) % q == 0:
                            # primitive: no proper nonempty subvector vanishes (weight>=2 needed;
                            # weight-1 can't vanish, weight-2 pairs:)
                            prim = True
                            pairs = [(1, sb, a, b), (1, sc, a, c), (sb, sc, b, c)]
                            for (s1, s2, x, y) in pairs:
                                if (s1 * pw[x] + s2 * pw[y]) % q == 0:
                                    prim = False
                            if not prim:
                                continue
                            vec = [0] * N
                            vec[a] = 1; vec[b] = sb; vec[c] = sc
                            reps.add(orbit_key(tuple(vec)))
    return len(reps)


def main():
    KILLS = [63361, 65921, 204353, 48449, 128833]
    L = 1
    print("row       prime? q%64  A_total(==signed_all?)  orbits{2..6}         W_cl   E-1(exact)                 K'(exact)               verdict  w3(brute)")
    for q in KILLS:
        assert isprime(q), f"{q} not prime!"
        assert q % NPRIME == 1, f"{q} not 1 mod 64"
        assert 2 ** N >= q ** L and N >= 16 * L
        A = a_total_and_invariant(q, L)
        asum = signed_all_census(q, NPRIME, 2)   # t=2 -> o=L=1
        A2 = sum(asum)
        assert A == A2, f"A_total mismatch q={q}: DP={A} signed_all={A2}"
        em1 = Fraction(q ** L * A, 4 ** N) - 1
        r = Fraction(q ** L, 2 ** N)
        counts = {w: primitive_orbit_count((q, L, w)) for w in range(2, 7)}
        ledger = sum(Fraction(counts[w] * NPRIME, 2 ** w) for w in counts)
        kprime = em1 / (r * (1 + ledger))
        lit = em1 > 4 * r * (1 + ledger)
        w3b = brute_weight3_orbits(q)
        assert w3b == counts[3], f"brute w3 {w3b} != enum {counts[3]} at q={q}"
        verdict = "LITERAL-KILL" if lit else ("AMBER" if kprime >= 1 else "survives")
        print(f"q={q:>7}  {str(isprime(q)):>5} {q%64:>4}   A={A} (match={A==A2})  {counts}  "
              f"{ledger}   {em1.numerator}/{em1.denominator}  {float(kprime):.6f}  {verdict}  w3={w3b}")
        if q == 63361:
            assert lit and float(kprime) > 4, "TOP KILL did not reproduce!"
    print("\nINDEPENDENT VERIFICATION COMPLETE: banked signed_all_census E == A_total DP E,"
          " banked primitive_orbit_count == counts, mass invariant + brute w3 all consistent.")


if __name__ == "__main__":
    main()
