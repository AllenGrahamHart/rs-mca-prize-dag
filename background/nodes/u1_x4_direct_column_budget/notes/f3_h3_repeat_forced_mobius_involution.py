#!/usr/bin/env python3
"""Forced-coordinate Mobius involution for h=3 repeat-boundary support."""

from __future__ import annotations

import sympy as sp

from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_support_forced_point_reduction import active_ordered_triples


def symbolic_summary() -> dict[str, int]:
    a, x = sp.symbols("a x")
    shift_a, shift_x = sp.symbols("A X")

    w = sp.cancel(1 - (a - 1) * (x - 1) / (a + x - 2))
    shifted_w = sp.cancel(w.subs({a: shift_a + 1, x: shift_x + 1}) - 1)
    involution = sp.cancel(-shift_a * shift_x / (shift_a + shift_x))
    if sp.factor(shifted_w - involution) != 0:
        raise AssertionError((shifted_w, involution))

    second = sp.cancel(involution.subs(shift_x, involution))
    second_num, _ = sp.together(second - shift_x).as_numer_denom()
    if sp.factor(second_num) != 0:
        raise AssertionError(sp.factor(second_num))

    fixed_num, _ = sp.together(involution - shift_x).as_numer_denom()
    if sp.factor(fixed_num + shift_x * (shift_x + 2 * shift_a)) != 0:
        raise AssertionError(sp.factor(fixed_num))

    lam = sp.cancel(a + x + w - 2)
    lam_after_w = sp.cancel(lam.subs(x, w))
    lam_num, _ = sp.together(lam_after_w - lam).as_numer_denom()
    if sp.factor(lam_num) != 0:
        raise AssertionError(sp.factor(lam_num))

    w_at_two = sp.cancel(w.subs(a, 2))
    lam_at_two = sp.cancel(lam.subs(a, 2))
    if sp.factor(w_at_two - 1 / x) != 0:
        raise AssertionError(w_at_two)
    if sp.factor(lam_at_two - x - 1 / x) != 0:
        raise AssertionError(lam_at_two)

    return {
        "shifted_degree_num": sp.degree(sp.fraction(involution)[0], shift_x),
        "shifted_degree_den": sp.degree(sp.fraction(involution)[1], shift_x),
        "fixed_factors": 2,
    }


def forced_w(p: int, a: int, x: int) -> int:
    denom = (a + x - 2) % p
    if denom == 0:
        raise AssertionError((p, a, x, "pole"))
    return (1 - (a - 1) * (x - 1) * pow(denom, -1, p)) % p


def verify_row(p: int, n: int) -> dict[str, int]:
    triples = active_ordered_triples(p, n)
    checks = 0
    fixed_hits = 0
    for u, v, w, lam in triples:
        for a, x, y in ((u, v, w), (v, u, w), (w, u, v)):
            image = forced_w(p, a, x)
            if image != y:
                raise AssertionError((p, n, (u, v, w), a, x, y, image))
            if forced_w(p, a, image) != x:
                raise AssertionError((p, n, a, x, image))
            if (a + x + image - 2) % p != lam:
                raise AssertionError((p, n, a, x, image, lam))
            if x == image:
                fixed_hits += 1
            checks += 1
    if fixed_hits:
        raise AssertionError((p, n, fixed_hits))
    return {
        "b_line": len(triples),
        "mobius_checks": checks,
    }


def main() -> None:
    print("h=3 repeat forced-coordinate Mobius involution")
    summary = symbolic_summary()
    print(
        "shifted normal form: "
        f"degree={summary['shifted_degree_num']}/{summary['shifted_degree_den']} "
        "T_A(X)=-A*X/(A+X)"
    )
    print("T_A is an involution; fixed factors are X and X+2A")
    print("lambda_a is invariant under the involution")
    print("a=2 special cell: w_2(v)=v^-1 and lambda_2(v)=v+v^-1")
    total_checks = 0
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        total_checks += row["mobius_checks"]
        print(
            f"p={p} n={n} B_line={row['b_line']} "
            f"mobius_checks={row['mobius_checks']}"
        )
    print(f"finite active-triple Mobius checks: {total_checks}")
    print("H3_REPEAT_FORCED_MOBIUS_INVOLUTION_PASS")


if __name__ == "__main__":
    main()
