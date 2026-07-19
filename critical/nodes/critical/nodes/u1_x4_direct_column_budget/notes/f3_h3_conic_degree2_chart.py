#!/usr/bin/env python3
"""Verify the h=3 same-fiber conic degree-2 chart."""

from __future__ import annotations


def inv(x: int, p: int) -> int:
    return pow(x % p, -1, p)


def g_value(u: int, v: int, a: int, b: int, p: int) -> int:
    return (u * u + u * v + v * v + a * (u + v) + b) % p


def f0_value(x: int, a: int, b: int, p: int) -> int:
    return (x * x * x + a * x * x + b * x) % p


def e2_value(u: int, v: int, w: int, p: int) -> int:
    return (u * v + u * w + v * w) % p


def case_b(p: int, a: int, u0: int, v0: int) -> int:
    return (-(u0 * u0 + u0 * v0 + v0 * v0 + a * (u0 + v0))) % p


def q_value(t: int, p: int) -> int:
    return (t * t + t + 1) % p


def chart_point(p: int, a: int, b: int, u0: int, v0: int, t: int) -> tuple[int, int, int] | None:
    q = q_value(t, p)
    if q == 0:
        return None
    a0 = (2 * u0 + v0 + a) % p
    b0 = (u0 + 2 * v0 + a) % p
    s = (-(a0 + b0 * t) * inv(q, p)) % p
    u = (u0 + s) % p
    v = (v0 + t * s) % p
    w = (-a - u - v) % p
    return u, v, w


def infinity_point(p: int, a: int, u0: int, v0: int) -> tuple[int, int]:
    return u0 % p, (-a - u0 - v0) % p


def numerator_coefficients(p: int, a: int, u0: int, v0: int) -> dict[str, tuple[int, int, int]]:
    a0 = (2 * u0 + v0 + a) % p
    b0 = (u0 + 2 * v0 + a) % p
    # Coefficients are in increasing powers of t, with Q=t^2+t+1.
    u_num = ((u0 - a0) % p, (u0 - b0) % p, u0 % p)
    v_num = (v0 % p, (v0 - a0) % p, (v0 - b0) % p)
    w_num = tuple(((-a) * c - u_num[i] - v_num[i]) % p for i, c in enumerate((1, 1, 1)))
    return {"U": u_num, "V": v_num, "W": w_num}


def eval_quad(coeffs: tuple[int, int, int], t: int, p: int) -> int:
    return (coeffs[0] + coeffs[1] * t + coeffs[2] * t * t) % p


def verify_chart_identities(p: int, a: int, u0: int, v0: int) -> dict[str, int]:
    b = case_b(p, a, u0, v0)
    if (a * a - 3 * b) % p == 0:
        raise AssertionError(("degenerate case selected", p, a, b, u0, v0))
    if g_value(u0, v0, a, b, p) != 0:
        raise AssertionError(("base point not on conic", p, a, b, u0, v0))

    coeffs = numerator_coefficients(p, a, u0, v0)
    checked = 0
    skipped_poles = 0
    for t in range(p):
        point = chart_point(p, a, b, u0, v0, t)
        if point is None:
            skipped_poles += 1
            continue
        u, v, w = point
        q = q_value(t, p)
        if (eval_quad(coeffs["U"], t, p) * inv(q, p)) % p != u:
            raise AssertionError(("U numerator mismatch", p, t))
        if (eval_quad(coeffs["V"], t, p) * inv(q, p)) % p != v:
            raise AssertionError(("V numerator mismatch", p, t))
        if (eval_quad(coeffs["W"], t, p) * inv(q, p)) % p != w:
            raise AssertionError(("W numerator mismatch", p, t))
        if g_value(u, v, a, b, p) != 0:
            raise AssertionError(("chart left conic", p, t, u, v))
        if (u + v + w + a) % p != 0:
            raise AssertionError(("bad e1", p, t, u, v, w))
        if e2_value(u, v, w, p) != b:
            raise AssertionError(("bad e2", p, t, u, v, w, b))
        f = f0_value(u, a, b, p)
        if f0_value(v, a, b, p) != f or f0_value(w, a, b, p) != f:
            raise AssertionError(("not same fiber", p, t, u, v, w))
        checked += 1

    u_inf, v_inf = infinity_point(p, a, u0, v0)
    if g_value(u_inf, v_inf, a, b, p) != 0:
        raise AssertionError(("infinity mate not on conic", p, u_inf, v_inf))

    return {"b": b, "checked_t": checked, "skipped_poles": skipped_poles}


def verify_coverage(p: int, a: int, u0: int, v0: int) -> dict[str, int]:
    b = case_b(p, a, u0, v0)
    conic_points = {
        (u, v)
        for u in range(p)
        for v in range(p)
        if g_value(u, v, a, b, p) == 0
    }
    image_points: set[tuple[int, int]] = set()
    for t in range(p):
        point = chart_point(p, a, b, u0, v0, t)
        if point is not None:
            image_points.add(point[:2])
    image_points.add(infinity_point(p, a, u0, v0))
    if image_points != conic_points:
        missing = sorted(conic_points - image_points)[:5]
        extra = sorted(image_points - conic_points)[:5]
        raise AssertionError(("coverage mismatch", p, missing, extra))
    return {"conic_points": len(conic_points), "image_points": len(image_points)}


def main() -> None:
    cases = (
        (17, 4, 2, 5),
        (97, 11, 7, 19),
        (193, 23, 41, 72),
        (769, 37, 101, 333),
    )
    print("h=3 conic degree-2 chart")
    for p, a, u0, v0 in cases:
        row = verify_chart_identities(p, a, u0, v0)
        coverage = verify_coverage(p, a, u0, v0) if p <= 193 else None
        coverage_text = ""
        if coverage is not None:
            coverage_text = (
                f" conic_points={coverage['conic_points']} "
                f"image_points={coverage['image_points']}"
            )
        print(
            f"p={p} a={a} b={row['b']} base=({u0},{v0}) "
            f"checked_t={row['checked_t']} skipped_poles={row['skipped_poles']}"
            f"{coverage_text}"
        )
    print("degree check: U,V,W have numerator degree <= 2 and denominator Q=t^2+t+1")
    print("H3_CONIC_DEGREE2_CHART_PASS")


if __name__ == "__main__":
    main()
