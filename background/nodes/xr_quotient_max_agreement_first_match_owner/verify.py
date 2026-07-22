#!/usr/bin/env python3
"""Verify the XR maximum-agreement quotient first-match owner."""

from __future__ import annotations

from itertools import combinations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_quotient_max_agreement_first_match_owner"
DEPENDENCY = "xr_quotient_boundary_agreement_raise_owner"
CONSUMER = "xr_tangent_support_mismatch_bridge"


def contained(
    left: tuple[int, ...],
    right: tuple[int, ...],
    support: frozenset[int],
) -> bool:
    return (
        len({left[index] for index in support}) <= 1
        and len({right[index] for index in support}) <= 1
    )


def line_roots(
    prime: int,
    left: tuple[int, ...],
    right: tuple[int, ...],
    support: frozenset[int],
) -> frozenset[int]:
    return frozenset(
        slope
        for slope in range(prime)
        if len(
            {
                (left[index] + slope * right[index]) % prime
                for index in support
            }
        )
        <= 1
    )


def quotient_roots(
    prime: int,
    left: tuple[int, ...],
    right: tuple[int, ...],
    support: frozenset[int],
) -> frozenset[int]:
    if contained(left, right, support):
        return frozenset()
    return line_roots(prime, left, right, support)


def exhaustive_fixture() -> tuple[int, int, int]:
    prime = 3
    length = 4
    agreement = 2
    exact_supports = (frozenset((0, 1)), frozenset((2, 3)))
    threshold_supports = {
        2: exact_supports,
        3: tuple(
            frozenset(indices) for indices in combinations(range(length), 3)
        ),
        4: (frozenset(range(length)),),
    }
    raised_supports = threshold_supports[3]

    pairs = 0
    maximum_occurrences = 0
    omitted_exact_failures = 0
    vectors = tuple(product(range(prime), repeat=length))
    for left in vectors:
        for right in vectors:
            exact = frozenset().union(
                *(
                    quotient_roots(prime, left, right, support)
                    for support in exact_supports
                )
            )
            threshold = frozenset().union(
                *(
                    quotient_roots(prime, left, right, support)
                    for size in range(agreement, length + 1)
                    for support in threshold_supports[size]
                )
            )
            raised = frozenset().union(
                *(
                    line_roots(prime, left, right, support)
                    for support in raised_supports
                )
            )
            maximum = exact - raised
            assert threshold <= maximum | raised

            for support in exact_supports:
                for slope in quotient_roots(prime, left, right, support) - raised:
                    anchor = next(iter(support))
                    value = (left[anchor] + slope * right[anchor]) % prime
                    full = frozenset(
                        index
                        for index in range(length)
                        if (left[index] + slope * right[index]) % prime == value
                    )
                    assert full == support
                    maximum_occurrences += 1

            omitted_exact_failures += len(threshold - raised)
            pairs += 1

    assert maximum_occurrences > 0
    assert omitted_exact_failures > 0
    return pairs, maximum_occurrences, omitted_exact_failures


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "Q_c^max(A)=Q_c(A)\\B_(A+1)(u,v)",
        "{xinD:u(x)+zv(x)=p_z(x)}=S",
        "fullagreementset,notanarbitrarysubset",
        "doesnotboundthenumberoffull-agreementquotientimages",
    ):
        assert marker in statement


def main() -> None:
    pairs, maximum, exact_required = exhaustive_fixture()
    packet_check()
    print(
        "XR_QUOTIENT_MAX_AGREEMENT_FIRST_MATCH_OWNER_PASS "
        f"pairs={pairs} maximum={maximum} exact_required={exact_required}"
    )


if __name__ == "__main__":
    main()
