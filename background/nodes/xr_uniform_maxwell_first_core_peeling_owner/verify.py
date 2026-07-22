#!/usr/bin/env python3
"""Verify the combinatorial XR first-core peeling owner."""

from __future__ import annotations

import itertools
import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_uniform_maxwell_first_core_peeling_owner"
PARENTS = {
    "xr_higher_rank_uniform_split_pencil_reduction",
    "xr_rank_two_fundamental_circuit_owner",
}
CONSUMER = "xr_highcore_collision_count"


@dataclass(frozen=True)
class Certificate:
    core: tuple[int, ...]
    relation_rank: int
    pivot: int
    circuit: tuple[int, ...] | None


def first_core(
    family: tuple[int, ...], blocks: tuple[frozenset[int], ...], a: int, h: int
) -> tuple[int, ...]:
    """Use cardinality/lex order; the first dense set is inclusion-minimal."""
    for size in range(1, len(family) + 1):
        for candidate in itertools.combinations(family, size):
            union = set().union(*(blocks[index] for index in candidate))
            if h * size >= 2 * len(union) - 2 * a:
                return candidate
    raise AssertionError("global density promised a core")


def canonical_certificate(core: tuple[int, ...], step: int) -> Certificate:
    """Exercise both algebraic branches after the parents supply a relation."""
    assert len(core) >= 2
    if len(core) >= 4 and step % 2 == 0:
        coefficient_rank = 3 if len(core) == 4 else 4
        anchors = core[:coefficient_rank]
        nonanchors = core[coefficient_rank:]
        assert nonanchors
        pivot = nonanchors[0]
        circuit = anchors + (pivot,)
        assert len(circuit) in (4, 5)
        return Certificate(core, 2, pivot, circuit)
    pivot = core[0]
    return Certificate(core, 3, pivot, None)


def peel(
    blocks: tuple[frozenset[int], ...], n_points: int, a: int, h: int
) -> tuple[tuple[int, ...], tuple[Certificate, ...]]:
    family = tuple(range(len(blocks)))
    certificates: list[Certificate] = []
    while h * len(family) >= 2 * n_points - 2 * a:
        core = first_core(family, blocks, a, h)
        certificate = canonical_certificate(core, len(certificates))
        assert certificate.pivot in core
        assert certificate.pivot in family
        certificates.append(certificate)
        family = tuple(index for index in family if index != certificate.pivot)
    return family, tuple(certificates)


def affine_plane_three() -> tuple[frozenset[int], ...]:
    """The twelve affine lines in F_3^2, encoded by integers 3*x+y."""
    lines: list[frozenset[int]] = []
    for intercept in range(3):
        lines.append(frozenset(3 * intercept + y for y in range(3)))
    for slope in range(3):
        for intercept in range(3):
            lines.append(
                frozenset(3 * x + ((slope * x + intercept) % 3) for x in range(3))
            )
    assert len(lines) == len(set(lines)) == 12
    return tuple(lines)


def fano_plane() -> tuple[frozenset[int], ...]:
    return tuple(
        frozenset(block)
        for block in (
            (0, 1, 3),
            (0, 2, 6),
            (0, 4, 5),
            (1, 2, 4),
            (1, 5, 6),
            (2, 3, 5),
            (3, 4, 6),
        )
    )


def fixture_check(
    blocks: tuple[frozenset[int], ...], n_points: int, a: int, h: int
) -> tuple[int, int]:
    assert all(len(block) == a + h for block in blocks)
    assert all(
        len(blocks[i] & blocks[j]) <= a
        for i in range(len(blocks))
        for j in range(i + 1, len(blocks))
    )
    first = peel(blocks, n_points, a, h)
    second = peel(blocks, n_points, a, h)
    assert first == second
    residual, certificates = first
    bound = (2 * n_points - 2 * a - 1) // h
    assert len(residual) <= bound
    assert len(residual) + len(certificates) == len(blocks)
    assert len({certificate.pivot for certificate in certificates}) == len(certificates)
    assert len(set(certificates)) == len(certificates)
    assert all(certificate.pivot not in residual for certificate in certificates)
    assert h * len(residual) < 2 * n_points - 2 * a
    return len(certificates), len(residual)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in PARENTS:
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "h|F_j|>=2N-2a",
        "h|G_j|>=2|unionG_j|-2a",
        "rankLambda_j=2",
        "firstactivenon-anchorblock",
        "F_(j+1)=F_j\\{p_j}",
        "|F_terminal|<=B_0:=floor((2N-2a-1)/h)",
        "B_0<2N/h<=2n<=8n^3",
        "numberofproducedpointedcertificates",
    ):
        assert marker in statement


def main() -> None:
    fixtures = (
        (fano_plane(), 7, 1, 2),
        (affine_plane_three(), 9, 1, 2),
        (tuple(frozenset(edge) for edge in itertools.combinations(range(6), 2)), 6, 1, 1),
    )
    results = [fixture_check(*fixture) for fixture in fixtures]
    assert any(removed >= 2 for removed, _ in results)
    packet_check()
    print(
        "XR_UNIFORM_MAXWELL_FIRST_CORE_PEELING_OWNER_PASS "
        f"fixtures={len(results)} removed={sum(row[0] for row in results)} "
        f"residual={sum(row[1] for row in results)}"
    )


if __name__ == "__main__":
    main()
