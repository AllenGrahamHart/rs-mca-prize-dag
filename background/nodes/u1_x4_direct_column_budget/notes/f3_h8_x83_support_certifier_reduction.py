#!/usr/bin/env python3
"""Verify the h=8 x83 support-to-trade reduction on banked rows.

The x83 obstruction gate is support-level: for a 16-support R it recovers a
forced monic degree-8 polynomial S and tests whether

    L_R(X) = S(X)^2 - lambda

with lambda a nonzero square.  This script verifies, on the banked h=8 n=64
rows, that every such full-zero support canonically splits into the two h=8
trade sides S(X)-alpha and S(X)+alpha.  Thus a future support-level x83
certifier is sufficient; it does not need to store or join all left/right
signature records.
"""

from __future__ import annotations

from f3_h8_n64_x83_obstruction_interface import (
    antipodal_lift,
    elementary_signature,
    forced_obstructions,
    h4_anchored_trades,
    is_square_mod,
    locator_from_exponents,
    root_table,
)


def sqrt_mod(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    if pow(a, (p - 1) // 2, p) != 1:
        raise ValueError((a, p, "not a square"))
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    q = p - 1
    s = 0
    while q % 2 == 0:
        s += 1
        q //= 2
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m = s
    c = pow(z, q, p)
    t = pow(a, q, p)
    r = pow(a, (q + 1) // 2, p)
    while t != 1:
        i = 1
        t2i = (t * t) % p
        while t2i != 1:
            t2i = (t2i * t2i) % p
            i += 1
            if i >= m:
                raise AssertionError((a, p, "tonelli-shanks failed"))
        b = pow(c, 1 << (m - i - 1), p)
        m = i
        c = (b * b) % p
        t = (t * c) % p
        r = (r * b) % p
    return r


def poly_eval(coeffs: list[int], x: int, p: int) -> int:
    acc = 0
    for coeff in reversed(coeffs):
        acc = (acc * x + coeff) % p
    return acc


def classify_x83_support(
    support: tuple[int, ...], vals: list[int], p: int
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    locator = locator_from_exponents(support, vals, p)
    square_root, obstructions, lam = forced_obstructions(locator, p, 8)
    if any(obstructions) or lam == 0 or not is_square_mod(lam, p):
        raise ValueError((support, "not x83 full-zero"))
    alpha = sqrt_mod(lam, p)
    plus = []
    minus = []
    for exponent in support:
        value = poly_eval(square_root, vals[exponent], p)
        if value == alpha:
            plus.append(exponent)
        elif value == (-alpha) % p:
            minus.append(exponent)
        else:
            raise AssertionError((p, exponent, value, alpha, support))
    if len(plus) != 8 or len(minus) != 8:
        raise AssertionError((p, plus, minus, support))
    plus_t = tuple(sorted(plus))
    minus_t = tuple(sorted(minus))
    sig_plus = elementary_signature(plus_t, vals, p)
    sig_minus = elementary_signature(minus_t, vals, p)
    if sig_plus[:7] != sig_minus[:7] or sig_plus[7] == sig_minus[7]:
        raise AssertionError((p, plus_t, minus_t, sig_plus, sig_minus))
    return plus_t, minus_t


def paid_lift_supports(p: int) -> list[tuple[int, ...]]:
    supports = []
    for left4, right4, _ in h4_anchored_trades(p):
        left8 = antipodal_lift(left4)
        right8 = antipodal_lift(right4)
        supports.append(tuple(sorted(set(left8) | set(right8))))
    return sorted(set(supports))


def verify_prime(p: int, expected_supports: int) -> dict[str, int]:
    vals = root_table(p, 64)
    supports = paid_lift_supports(p)
    if len(supports) != expected_supports:
        raise AssertionError((p, len(supports), expected_supports))
    recovered = 0
    for support in supports:
        plus, minus = classify_x83_support(support, vals, p)
        if set(plus) | set(minus) != set(support):
            raise AssertionError((p, support, plus, minus))
        recovered += 1
    return {"supports": len(supports), "recovered_trade_pairs": recovered}


def verify_nonzero_control(p: int) -> None:
    vals = root_table(p, 64)
    support = tuple(range(16))
    try:
        classify_x83_support(support, vals, p)
    except ValueError:
        return
    raise AssertionError((p, "nonzero control unexpectedly classified"))


def main() -> None:
    expected = {
        193: 15,
        4289: 7,
        262337: 7,
    }
    total = 0
    for p, expected_count in expected.items():
        row = verify_prime(p, expected_count)
        verify_nonzero_control(p)
        total += row["recovered_trade_pairs"]
        print(
            f"p={p} x83 full-zero supports={row['supports']} "
            f"recovered_trade_pairs={row['recovered_trade_pairs']}"
        )
    print(f"total recovered trade pairs: {total}")
    print("H8_X83_SUPPORT_CERTIFIER_REDUCTION_PASS")


if __name__ == "__main__":
    main()
