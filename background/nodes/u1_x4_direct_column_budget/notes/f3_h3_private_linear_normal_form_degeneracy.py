#!/usr/bin/env python3
"""Verify degeneracy conditions in the h=3 private-linear normal form."""

from __future__ import annotations


def trim(poly: list[int], p: int) -> list[int]:
    out = [x % p for x in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out, p)


def proportional(a: list[int], b: list[int], p: int) -> bool:
    a = trim(a, p)
    b = trim(b, p)
    if len(a) != len(b):
        return False
    scalar = None
    for x, y in zip(a, b):
        if y % p == 0:
            if x % p:
                return False
            continue
        ratio = x * pow(y, -1, p) % p
        if scalar is None:
            scalar = ratio
        elif scalar != ratio:
            return False
    return scalar is not None


def linear_root(root: int, p: int) -> list[int]:
    return [(-root) % p, 1]


def constant_ratio(
    f_num: list[int],
    f_den: list[int],
    g_num: list[int],
    g_den: list[int],
    p: int,
) -> bool:
    return proportional(mul(f_num, g_den, p), mul(f_den, g_num, p), p)


def private_open(lam: int, eta: int, theta: int, p: int) -> bool:
    values = [lam % p, eta % p, theta % p]
    return all(value not in (0, 1) for value in values) and len(set(values)) == 3


def check_field(p: int) -> dict[str, int]:
    total = 0
    open_count = 0
    open_collapsed = 0
    r23_collapsed = 0
    r23_formula_count = 0
    for lam in range(p):
        for eta in range(p):
            for theta in range(p):
                total += 1
                r1_num, r1_den = linear_root(0, p), [1]
                r2_num, r2_den = linear_root(1, p), linear_root(lam, p)
                r3_num, r3_den = linear_root(eta, p), linear_root(theta, p)

                cr12 = constant_ratio(r1_num, r1_den, r2_num, r2_den, p)
                cr13 = constant_ratio(r1_num, r1_den, r3_num, r3_den, p)
                cr23 = constant_ratio(r2_num, r2_den, r3_num, r3_den, p)
                if cr12 or cr13:
                    raise AssertionError((p, lam, eta, theta, cr12, cr13))

                formula = (lam == 1 and eta == theta) or (eta == 1 and lam == theta)
                if cr23 != formula:
                    raise AssertionError((p, lam, eta, theta, cr23, formula))
                r23_collapsed += int(cr23)
                r23_formula_count += int(formula)

                if private_open(lam, eta, theta, p):
                    open_count += 1
                    if cr23:
                        open_collapsed += 1
    if open_collapsed:
        raise AssertionError((p, open_collapsed))
    if r23_collapsed != r23_formula_count:
        raise AssertionError((p, r23_collapsed, r23_formula_count))
    return {
        "total": total,
        "private_open": open_count,
        "r23_collapsed": r23_collapsed,
        "open_collapsed": open_collapsed,
    }


def main() -> None:
    print("h=3 private-linear normal-form degeneracy chart")
    for p in (17, 19, 23):
        row = check_field(p)
        print(
            f"p={p} total={row['total']} private_open={row['private_open']} "
            f"r23_collapsed={row['r23_collapsed']} "
            f"open_collapsed={row['open_collapsed']}"
        )
    print("private-divisor normal-form open set excludes constant-ratio collapse")
    print("H3_PRIVATE_LINEAR_NORMAL_FORM_DEGENERACY_PASS")


if __name__ == "__main__":
    main()
