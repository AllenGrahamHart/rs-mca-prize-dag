#!/usr/bin/env python3
"""Verify h=3 conic base-point equivalence for bridge bookkeeping."""

from __future__ import annotations

from f3_h3_conic_chart_hpoint_coverage import (
    chart_point,
    ordered_fibers,
    root_table,
    vertical_point,
)
from f3_h3_conic_degree2_chart import (
    case_b,
    chart_point as conic_chart_point,
    g_value,
    infinity_point,
)


def conic_points(p: int, a: int, b: int) -> set[tuple[int, int]]:
    return {
        (u, v)
        for u in range(p)
        for v in range(p)
        if g_value(u, v, a, b, p) == 0
    }


def projective_chart_image(
    p: int, a: int, b: int, u0: int, v0: int
) -> set[tuple[int, int]]:
    image = set()
    for t in range(p):
        point = conic_chart_point(p, a, b, u0, v0, t)
        if point is not None:
            image.add(point[:2])
    image.add(infinity_point(p, a, u0, v0))
    return image


def verify_projective_case(p: int, a: int, u0: int, v0: int) -> dict[str, int]:
    b = case_b(p, a, u0, v0)
    if (a * a - 3 * b) % p == 0:
        raise AssertionError(("degenerate conic", p, a, b))
    points = sorted(conic_points(p, a, b))
    if (u0 % p, v0 % p) not in points:
        raise AssertionError(("base point not on conic", p, a, b, u0, v0))
    basepoints = [points[0], points[len(points) // 2], points[-1]]
    reference = projective_chart_image(p, a, b, *basepoints[0])
    if reference != set(points):
        raise AssertionError(("reference coverage failed", p, a, b))
    for base in basepoints[1:]:
        image = projective_chart_image(p, a, b, *base)
        if image != reference:
            missing = sorted(reference - image)[:5]
            extra = sorted(image - reference)[:5]
            raise AssertionError(("basepoint image mismatch", p, a, b, base, missing, extra))
    return {"b": b, "conic_points": len(points), "basepoints": len(basepoints)}


def recovered_h_triples(
    p: int,
    hset: set[int],
    key: tuple[int, int],
    base: tuple[int, int, int],
) -> set[tuple[int, int, int]]:
    s1, _ = key
    a = (-s1) % p
    u0, v0, _ = base
    recovered: set[tuple[int, int, int]] = set()
    for t in range(p):
        point = chart_point(p, a, u0, v0, t)
        if point is not None and len(set(point)) == 3 and all(x in hset for x in point):
            recovered.add(point)
    vertical = vertical_point(p, a, u0, v0)
    if len(set(vertical)) == 3 and all(x in hset for x in vertical):
        recovered.add(vertical)
    return recovered


def verify_h_fiber_row(p: int, n: int, max_fibers: int = 8) -> dict[str, int]:
    hset = set(root_table(p, n))
    fibers = ordered_fibers(p, n)
    selected = sorted(
        ((len(ordered), key, ordered) for key, ordered in fibers.items()),
        reverse=True,
    )[:max_fibers]
    checked = 0
    basepoint_checks = 0
    skipped_degenerate = 0
    for _, key, ordered in selected:
        s1, s2 = key
        a = (-s1) % p
        b = s2
        if (a * a - 3 * b) % p == 0:
            skipped_degenerate += 1
            continue
        bases = sorted(ordered)[:3]
        for base in bases:
            recovered = recovered_h_triples(p, hset, key, base)
            if recovered != ordered:
                missing = sorted(ordered - recovered)[:5]
                extra = sorted(recovered - ordered)[:5]
                raise AssertionError((p, n, key, base, missing, extra))
            basepoint_checks += 1
        checked += 1
    return {
        "fibers": checked,
        "basepoint_checks": basepoint_checks,
        "skipped_degenerate": skipped_degenerate,
    }


def main() -> None:
    print("h=3 conic base-point equivalence")
    for p, a, u0, v0 in ((17, 4, 2, 5), (97, 11, 7, 19), (193, 23, 41, 72)):
        row = verify_projective_case(p, a, u0, v0)
        print(
            f"projective p={p} a={a} b={row['b']} "
            f"conic_points={row['conic_points']} basepoints={row['basepoints']}"
        )
    for p, n in ((97, 16), (97, 32), (193, 64)):
        row = verify_h_fiber_row(p, n)
        print(
            f"H-fibers p={p} n={n} fibers={row['fibers']} "
            f"basepoint_checks={row['basepoint_checks']} "
            f"skipped_degenerate={row['skipped_degenerate']}"
        )
    print("same-fiber conic charts from different base points have the same image")
    print("H3_CONIC_BASEPOINT_EQUIVALENCE_PASS")


if __name__ == "__main__":
    main()
