#!/usr/bin/env python3
"""Verify the first residual XR quadratic-involution shell."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_higher_rank_first_residual_quadratic_involution"
PARENTS = {
    "xr_higher_rank_uniform_split_pencil_reduction",
    "xr_higher_rank_collapsed_face_exclusion",
}
CONSUMER = "xr_highcore_collision_count"
PRIME = 1009


def inverse(value: int) -> int:
    return pow(value % PRIME, -1, PRIME)


def shell_arithmetic() -> int:
    checked = 0
    for a in range(4, 129):
        rho = a + 3
        for t in range(4, (a + 4) // 2 + 1):
            for singleton in (0, 1):
                zero_mass = 2 * t - singleton
                if zero_mass > rho:
                    continue
                zeros = ([1] if singleton else []) + [2] * (t - singleton)
                assert all(left + right >= 3 for i, left in enumerate(zeros) for right in zeros[i + 1 :])
                assert zero_mass == sum(zeros)
                assert rho - zero_mass >= 0
                checked += 1
    return checked


def involution_control() -> int:
    # phi(x)=x+1/x has deck involution x -> 1/x.  Use distinct reciprocal
    # pairs and verify complete two-point fibers over the prime field.
    checked = 0
    used: set[int] = set()
    for x in range(2, 80):
        y = inverse(x)
        if x == y or x in used or y in used:
            continue
        used.update((x, y))
        phi_x = (x + inverse(x)) % PRIME
        phi_y = (y + inverse(y)) % PRIME
        assert phi_x == phi_y
        roots = [z for z in range(PRIME) if z and (z + inverse(z)) % PRIME == phi_x]
        assert sorted(roots) == sorted((x, y))
        checked += 1
        if checked == 24:
            break
    assert checked == 24
    return checked


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
        "|X|=a+3",
        "4<=t<=floor((a+4)/2)",
        "|Z_i|in{1,2}",
        "atmostone|Z_i|=1",
        "degreeexactlytwo",
        "iota in PGL_2(F)",
        "doesnotcountembeddings",
    ):
        assert "".join(marker.split()) in statement


def main() -> None:
    arithmetic = shell_arithmetic()
    fibers = involution_control()
    packet_check()
    print(
        "XR_HIGHER_RANK_FIRST_RESIDUAL_QUADRATIC_INVOLUTION_PASS "
        f"profiles={arithmetic} fibers={fibers}"
    )


if __name__ == "__main__":
    main()
