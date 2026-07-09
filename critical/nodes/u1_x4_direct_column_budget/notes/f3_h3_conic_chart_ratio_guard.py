#!/usr/bin/env python3
"""Verify the h=3 conic-chart constant-ratio guard."""

from __future__ import annotations


def trim(poly: list[int], p: int) -> list[int]:
    out = [x % p for x in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def sub(a: list[int], b: list[int], p: int) -> list[int]:
    n = max(len(a), len(b))
    return trim(
        [((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % p for i in range(n)],
        p,
    )


def scale(a: list[int], c: int, p: int) -> list[int]:
    return trim([(c * x) % p for x in a], p)


def constant_ratio(a: list[int], b: list[int], p: int) -> int | None:
    a = trim(a, p)
    b = trim(b, p)
    if b == [0]:
        raise ValueError("zero denominator polynomial")
    if a == [0]:
        return 0
    pivot = next((i for i, coeff in enumerate(b) if coeff % p), None)
    if pivot is None:
        raise ValueError("zero denominator polynomial")
    lam = (a[pivot] if pivot < len(a) else 0) * pow(b[pivot], -1, p) % p
    if sub(a, scale(b, lam, p), p) == [0]:
        return lam
    return None


def g_value(u: int, v: int, a: int, b: int, p: int) -> int:
    return (u * u + u * v + v * v + a * (u + v) + b) % p


def case_b(p: int, a: int, u0: int, v0: int) -> int:
    return (-(u0 * u0 + u0 * v0 + v0 * v0 + a * (u0 + v0))) % p


def chart_numerators(p: int, a: int, u0: int, v0: int) -> dict[str, list[int]]:
    a0 = (2 * u0 + v0 + a) % p
    b0 = (u0 + 2 * v0 + a) % p
    u_num = [(u0 - a0) % p, (u0 - b0) % p, u0 % p]
    v_num = [v0 % p, (v0 - a0) % p, (v0 - b0) % p]
    q_coeffs = [1, 1, 1]
    w_num = [((-a) * q_coeffs[i] - u_num[i] - v_num[i]) % p for i in range(3)]
    return {"U": trim(u_num, p), "V": trim(v_num, p), "W": trim(w_num, p)}


def find_cube_root(p: int) -> int:
    for x in range(2, p):
        if (x * x + x + 1) % p == 0:
            return x
    raise AssertionError(("no primitive cube root", p))


def verify_nondegenerate_case(p: int, a: int, u0: int, v0: int) -> dict[str, int | None]:
    b = case_b(p, a, u0, v0)
    if g_value(u0, v0, a, b, p) != 0:
        raise AssertionError(("base point not on conic", p, a, b, u0, v0))
    if (a * a - 3 * b) % p == 0:
        raise AssertionError(("degenerate case selected", p, a, b))
    nums = chart_numerators(p, a, u0, v0)
    ratios = {
        "U/V": constant_ratio(nums["U"], nums["V"], p),
        "U/W": constant_ratio(nums["U"], nums["W"], p),
        "V/W": constant_ratio(nums["V"], nums["W"], p),
    }
    if any(value is not None for value in ratios.values()):
        raise AssertionError((p, a, b, u0, v0, nums, ratios))
    return {"b": b, **ratios}


def verify_toral_positive_control(p: int) -> dict[str, int | None]:
    omega = find_cube_root(p)
    a = 0
    b = 0
    u0 = 1
    v0 = omega
    if g_value(u0, v0, a, b, p) != 0:
        raise AssertionError(("bad toral point", p, omega))
    nums = chart_numerators(p, a, u0, v0)
    ratios = {
        "U/V": constant_ratio(nums["U"], nums["V"], p),
        "U/W": constant_ratio(nums["U"], nums["W"], p),
        "V/W": constant_ratio(nums["V"], nums["W"], p),
    }
    if all(value is None for value in ratios.values()):
        raise AssertionError(("positive control did not collapse", p, omega, nums, ratios))
    return ratios


def main() -> None:
    cases = (
        (17, 4, 2, 5),
        (97, 11, 7, 19),
        (193, 23, 41, 72),
        (769, 37, 101, 333),
    )
    print("h=3 conic-chart constant-ratio guard")
    for p, a, u0, v0 in cases:
        row = verify_nondegenerate_case(p, a, u0, v0)
        print(
            f"nondegenerate p={p} a={a} b={row['b']} base=({u0},{v0}) "
            "ratios=none"
        )
    control = verify_toral_positive_control(193)
    print(f"toral positive control p=193 ratios={control}")
    print("nondegenerate conic charts have no internal constant-ratio collapse")
    print("H3_CONIC_CHART_RATIO_GUARD_PASS")


if __name__ == "__main__":
    main()
