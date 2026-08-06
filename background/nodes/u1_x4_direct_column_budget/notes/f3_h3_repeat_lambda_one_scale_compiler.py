#!/usr/bin/env python3
"""Lambda=1 scale compiler for h=3 repeat-boundary active edges."""

from __future__ import annotations

from f3_h3_pair_count_from_charts_compiler import root_table
from f3_h3_repeat_edge_cubic_gcd_form import edge_cubic_data
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def primitive_cube_roots(p: int) -> tuple[int, int] | tuple[()]:
    if (p - 1) % 3:
        return ()
    for a in range(2, p):
        omega = pow(a, (p - 1) // 3, p)
        if omega != 1:
            other = omega * omega % p
            if other == 1 or (omega * other) % p != 1:
                raise AssertionError((p, omega, other))
            return (omega, other)
    raise AssertionError((p, "no primitive cube root found"))


def lambda_one_scale_edges(p: int, n: int) -> dict[frozenset[int], frozenset[int]]:
    h = root_table(p, n)
    hset = set(h)
    omegas = primitive_cube_roots(p)
    if not omegas:
        return {}
    omega = omegas[0]
    omega2 = omegas[1]
    out: dict[frozenset[int], frozenset[int]] = {}
    for u in h:
        if u == 1:
            continue
        x = (u - 1) % p
        scale_orbit = frozenset((x, omega * x % p, omega2 * x % p))
        edge = frozenset((1 + x, 1 + omega * x % p, 1 + omega2 * x % p))
        if len(edge) != 3:
            continue
        if edge <= hset:
            if sum(edge) % p != 3 % p:
                raise AssertionError((p, n, edge, "lambda sum mismatch"))
            out[edge] = scale_orbit
    return out


def active_lambda_one_edges(p: int, n: int) -> dict[frozenset[int], tuple[int, int]]:
    return {edge: data for edge, data in edge_cubic_data(p, n).items() if data[0] == 1}


def verify_row(p: int, n: int) -> dict[str, int]:
    scale_edges = lambda_one_scale_edges(p, n)
    active_edges = active_lambda_one_edges(p, n)
    if set(scale_edges) != set(active_edges):
        raise AssertionError((p, n, set(scale_edges), set(active_edges)))
    scale_orbits = set(scale_edges.values())
    if len(scale_orbits) != len(scale_edges):
        raise AssertionError((p, n, "scale orbit collision", scale_edges))
    return {
        "active_lambda_one_edges": len(active_edges),
        "scale_orbits": len(scale_orbits),
        "has_cube_roots": int(bool(primitive_cube_roots(p))),
    }


def main() -> None:
    print("h=3 repeat lambda=1 scale compiler")
    print("lambda=1 branch: {1+x,1+omega*x,1+omega^2*x} subset H")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} has_cube_roots={row['has_cube_roots']} "
            f"active_lambda_one_edges={row['active_lambda_one_edges']} "
            f"scale_orbits={row['scale_orbits']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["active_lambda_one_edges"] == 0:
            raise AssertionError((p, n, "contrast row should have lambda=1 scale edge"))
        print(
            f"contrast p={p} n={n} has_cube_roots={row['has_cube_roots']} "
            f"active_lambda_one_edges={row['active_lambda_one_edges']} "
            f"scale_orbits={row['scale_orbits']}"
        )
    print("Lambda=1 uniqueness is uniqueness of a primitive-cube scale orbit")
    print("H3_REPEAT_LAMBDA_ONE_SCALE_COMPILER_PASS")


if __name__ == "__main__":
    main()
