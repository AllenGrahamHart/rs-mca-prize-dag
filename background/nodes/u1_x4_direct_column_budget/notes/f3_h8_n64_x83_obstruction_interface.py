#!/usr/bin/env python3
"""Validate the h=8 n=64 x83 obstruction-key interface.

This is a structural interface check, not a full h=8 n64 certificate.  It
verifies that the x83 forced square-root obstruction vector sees the already
paid antipodal square-lift branch, then applies the same key to deterministic
non-antipodal support samples.
"""

from __future__ import annotations

from itertools import combinations
import random


def prime_factors(n: int) -> list[int]:
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def primitive_root(p: int) -> int:
    factors = prime_factors(p - 1)
    g = 2
    while any(pow(g, (p - 1) // r, p) == 1 for r in factors):
        g += 1
    return g


def root_table(p: int, n: int) -> list[int]:
    z = pow(primitive_root(p), (p - 1) // n, p)
    if pow(z, n, p) != 1 or pow(z, n // 2, p) == 1:
        raise AssertionError((p, n, z))
    return [pow(z, i, p) for i in range(n)]


def elementary_signature(exponents: tuple[int, ...], vals: list[int], p: int) -> tuple[int, ...]:
    coeffs = [1]
    for exponent in exponents:
        x = vals[exponent]
        coeffs.append(0)
        for i in range(len(coeffs) - 1, 0, -1):
            coeffs[i] = (coeffs[i] + coeffs[i - 1] * x) % p
    return tuple(coeffs[1:])


def is_toral(exponents: tuple[int, ...], n: int, h: int) -> bool:
    if n % h:
        return False
    step = n // h
    residue = exponents[0] % step
    seen = set()
    for exponent in exponents:
        if exponent % step != residue:
            return False
        seen.add((exponent - residue) // step)
    return len(seen) == h


def h4_anchored_trades(p: int, n: int = 32) -> list[tuple[tuple[int, ...], tuple[int, ...], bool]]:
    vals = root_table(p, n)
    lefts: dict[tuple[int, int, int], list[tuple[tuple[int, ...], int, bool]]] = {}
    for tail in combinations(range(1, n), 3):
        left = (0,) + tail
        sig = elementary_signature(left, vals, p)
        lefts.setdefault(sig[:3], []).append((left, sig[3], is_toral(left, n, 4)))

    out = []
    for right in combinations(range(1, n), 4):
        sig = elementary_signature(right, vals, p)
        right_toral = is_toral(right, n, 4)
        for left, last, left_toral in lefts.get(sig[:3], []):
            if set(left) & set(right):
                continue
            if last == sig[3]:
                continue
            out.append((left, right, left_toral and right_toral))
    return out


def poly_mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return out


def locator_from_exponents(exponents: tuple[int, ...], vals: list[int], p: int) -> list[int]:
    coeffs = [1]
    for exponent in exponents:
        root = vals[exponent]
        nxt = [0] * (len(coeffs) + 1)
        for i, coeff in enumerate(coeffs):
            nxt[i] = (nxt[i] - coeff * root) % p
            nxt[i + 1] = (nxt[i + 1] + coeff) % p
        coeffs = nxt
    return coeffs


def square_shift_root(L: list[int], p: int, h: int) -> list[int]:
    inv2 = pow(2, -1, p)
    s = [0] * (h + 1)
    s[h] = 1
    for degree in range(2 * h - 1, h - 1, -1):
        unknown = degree - h
        known = 0
        lo = max(0, degree - h)
        hi = min(h, degree)
        for i in range(lo, hi + 1):
            j = degree - i
            if not (0 <= j <= h):
                continue
            if i == unknown or j == unknown:
                continue
            known = (known + s[i] * s[j]) % p
        s[unknown] = ((L[degree] - known) * inv2) % p
    return s


def forced_obstructions(L: list[int], p: int, h: int) -> tuple[list[int], list[int], int]:
    S = square_shift_root(L, p, h)
    S2 = poly_mul(S, S, p)
    obs = [(S2[i] - L[i]) % p for i in range(1, h)]
    lam = (S2[0] - L[0]) % p
    return S, obs, lam


def is_square_mod(a: int, p: int) -> bool:
    return a % p == 0 or pow(a, (p - 1) // 2, p) == 1


def antipodal_lift(side: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted(side + tuple(e + 32 for e in side)))


def is_antipodal_support(support: tuple[int, ...], n: int = 64) -> bool:
    s = set(support)
    return all(((e + n // 2) % n) in s for e in s)


def verify_lifted_branch(p: int) -> dict[str, int]:
    vals64 = root_table(p, 64)
    h4_trades = h4_anchored_trades(p)
    total = 0
    toral = 0
    zero_obstruction = 0
    for left4, right4, toral_trade in h4_trades:
        left8 = antipodal_lift(left4)
        right8 = antipodal_lift(right4)
        sig_left = elementary_signature(left8, vals64, p)
        sig_right = elementary_signature(right8, vals64, p)
        if sig_left[:7] != sig_right[:7] or sig_left[7] == sig_right[7]:
            raise AssertionError(("bad lifted h8 trade", p, left4, right4))
        support = tuple(sorted(set(left8) | set(right8)))
        if len(support) != 16 or not is_antipodal_support(support):
            raise AssertionError(("bad lifted support", p, support))
        L = locator_from_exponents(support, vals64, p)
        _, obs, lam = forced_obstructions(L, p, 8)
        if all(v == 0 for v in obs) and lam != 0 and is_square_mod(lam, p):
            zero_obstruction += 1
        else:
            raise AssertionError(("x83 missed lifted trade", p, left4, right4, obs, lam))
        total += 1
        toral += int(toral_trade)
    return {"total": total, "toral": toral, "zero_obstruction": zero_obstruction}


def verify_h8_sensitivity(p: int) -> None:
    vals64 = root_table(p, 64)
    left4, right4, _ = h4_anchored_trades(p)[0]
    support = tuple(sorted(set(antipodal_lift(left4)) | set(antipodal_lift(right4))))
    L = locator_from_exponents(support, vals64, p)
    _, obs0, _ = forced_obstructions(L, p, 8)
    Lp = list(L)
    Lp[7] = (Lp[7] + 1) % p
    _, obs1, _ = forced_obstructions(Lp, p, 8)
    if (obs1[-1] - obs0[-1]) % p != p - 1:
        raise AssertionError(("first obstruction insensitive", p, obs0, obs1))
    if obs0[:-1] != obs1[:-1]:
        raise AssertionError(("lower obstruction changed", p, obs0, obs1))


def sample_nonantipodal(p: int, samples: int = 4096) -> dict[str, int]:
    vals64 = root_table(p, 64)
    rng = random.Random(880064 + p)
    full_zero = 0
    first_zero = 0
    accepted = 0
    while accepted < samples:
        support = tuple(sorted((0,) + tuple(rng.sample(range(1, 64), 15))))
        if is_antipodal_support(support):
            continue
        L = locator_from_exponents(support, vals64, p)
        _, obs, lam = forced_obstructions(L, p, 8)
        accepted += 1
        first_zero += int(obs[-1] == 0)
        full_zero += int(all(v == 0 for v in obs) and lam != 0 and is_square_mod(lam, p))
    if full_zero:
        raise AssertionError(("sampled non-antipodal x83 zero", p, full_zero))
    return {"samples": samples, "full_zero": full_zero, "first_zero": first_zero}


def main() -> None:
    expected = {
        193: {"total": 15, "toral": 7},
        4289: {"total": 7, "toral": 7},
        262337: {"total": 7, "toral": 7},
    }
    for p, exp in expected.items():
        row = verify_lifted_branch(p)
        if row["total"] != exp["total"] or row["toral"] != exp["toral"]:
            raise AssertionError((p, row, exp))
        if row["zero_obstruction"] != row["total"]:
            raise AssertionError((p, row))
        verify_h8_sensitivity(p)
        print(
            f"p={p} lifted h8 branch: total={row['total']} toral={row['toral']} "
            f"x83_zero={row['zero_obstruction']}"
        )

    for p in (4289, 262337):
        row = sample_nonantipodal(p)
        print(
            f"p={p} nonantipodal x83 sample: samples={row['samples']} "
            f"full_zero={row['full_zero']} first_obstruction_zero={row['first_zero']}"
        )

    print("H8_N64_X83_INTERFACE_PASS")


if __name__ == "__main__":
    main()
