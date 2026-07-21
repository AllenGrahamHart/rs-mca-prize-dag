#!/usr/bin/env python3
"""Verify the XR rank-two shell and Maxwell router."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_higher_rank_rank_two_shell_maxwell_router"
PARENTS = {
    "xr_higher_rank_uniform_split_pencil_reduction",
    "xr_higher_rank_collapsed_face_exclusion",
}
CONSUMER = "xr_highcore_collision_count"


def minimum_zero_mass(d: int, t: int) -> int:
    if d % 2:
        return t * (d + 1) // 2
    return t * (d // 2 + 1) - 1


def row_ceiling(a: int, d: int) -> int:
    if d % 2:
        return 2 * (a + d + 1) // (d + 1)
    return 2 * (a + d + 2) // (d + 2)


def profile_checks() -> int:
    checked = 0
    for d in range(1, 9):
        for t in range(4, 9):
            admissible = [
                values
                for values in itertools.combinations_with_replacement(range(1, d + 1), t)
                if values[0] + values[1] >= d + 1
            ]
            assert admissible
            observed = min(sum(values) for values in admissible)
            assert observed == minimum_zero_mass(d, t)
            minimizers = [values for values in admissible if sum(values) == observed]
            if d % 2:
                assert minimizers == [((d + 1) // 2,) * t]
            else:
                assert minimizers == [(d // 2,) + (d // 2 + 1,) * (t - 1)]
            checked += len(admissible)

    for a in range(2, 80):
        for d in range(1, a):
            ceiling = row_ceiling(a, d)
            assert minimum_zero_mass(d, ceiling) <= a + d + 1
            assert minimum_zero_mass(d, ceiling + 1) > a + d + 1
            if d == a - 1 and a % 2:
                assert ceiling == 3
            if d == a - 1 and not a % 2:
                assert ceiling == 4
    return checked


def deficit(a: int, h: int, d: int, t: int, zero_mass: int) -> int:
    return (
        2 * (d + 1)
        + t * (h - 2 * d - 2)
        + (d + 1) * t * (t - 1)
        - 2 * (t - 2) * zero_mass
    )


def deficit_checks() -> int:
    checked = 0
    for a in range(4, 50):
        for d in range(1, a):
            rho = a + d + 1
            for t in range(4, min(8, row_ceiling(a, d)) + 1):
                candidates = {tuple([d] * t)}
                for smallest in range(1, (d + 1) // 2 + 1):
                    candidates.add(
                        (smallest,) + (d + 1 - smallest,) * (t - 1)
                    )
                for zeros in candidates:
                    if (
                        zeros[0] + zeros[1] < d + 1
                        or sum(zeros) > rho
                        or any(rho - zero > a + 17 for zero in zeros)
                    ):
                        continue
                    zero_mass = sum(zeros)
                    i_0 = t * rho - zero_mass
                    p_0 = t * (t - 1) // 2 * rho - (t - 1) * zero_mass
                    extension = t * (a + 17) - i_0
                    slack = a * t * (t - 1) // 2 - p_0
                    union_lower = rho + extension - slack
                    direct = 2 * union_lower - 2 * a - 17 * t
                    assert direct == deficit(a, 17, d, t, zero_mass)
                    worst = deficit(a, 17, d, t, min(t * d, rho))
                    assert direct >= worst
                    checked += 1
    return checked


def official_checks() -> int:
    # First shell, RowC.
    for a in range(4, 8):
        for t in range(4, row_ceiling(a, 2) + 1):
            assert 6 + t * (5 - t - 1) > 0
    assert deficit(4, 3, 2, 4, 7) == 2

    # First shell, prize endpoints.
    for h in (2**33 + 1, 2**32 + 1):
        a_max = 2 * h - 5
        assert row_ceiling(a_max, 2) == h - 1
        assert 6 + (h - 1) * (h - (h - 1) - 1) == 6
        assert row_ceiling(a_max + 1, 2) == h

    # Second shell, prize endpoints; all printed h are odd.
    for h in (2**33 + 1, 2**32 + 1):
        a_max = h - 4
        t_max = row_ceiling(a_max, 3)
        assert t_max == h // 2
        assert 8 + t_max * (h - 2 * t_max) > 0


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert all(nodes[parent]["status"] == "PROVED" for parent in PARENTS)
    assert all((parent, NODE, "req") in edges for parent in PARENTS)
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "1<=z_i<=d",
        "z_i+z_j>=d+1",
        "M_d(t)<=a+d+1",
        "Delta_J>=2(d+1)",
        "D_min>0",
        "a<=2^34-3",
        "top shell `d=a-1` is empty",
        "Proper local rank-two circuits",
    ):
        assert "".join(marker.split()) in statement


def main() -> None:
    profiles = profile_checks()
    deficits = deficit_checks()
    official_checks()
    packet_check()
    print(
        "XR_HIGHER_RANK_RANK_TWO_SHELL_MAXWELL_ROUTER_PASS "
        f"profiles={profiles} deficits={deficits}"
    )


if __name__ == "__main__":
    main()
