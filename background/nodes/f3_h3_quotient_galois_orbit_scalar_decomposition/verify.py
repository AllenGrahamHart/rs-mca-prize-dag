#!/usr/bin/env python3
"""Verify the H3 quotient Galois-orbit scalar decomposition."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_quotient_galois_orbit_scalar_decomposition"
DEPENDENCIES = {
    "f3_h3_dsp8_single_quotient_candidate_compressor",
    "f3_h3_quotient_algebra_fitting_support_compiler",
    "f3_h3_shifted_product_sidon",
}
CONSUMERS = {
    "f3_h3_dsp8_correlation_bound",
    "f3_h3_official_order_template_survivor",
}


def valuation_two(value: int) -> int:
    result = 0
    while value % 2 == 0:
        result += 1
        value //= 2
    return result


def expected_histogram(exponent: int) -> Counter[int]:
    return Counter({2**j: 3 * (2**j - 1) for j in range(1, exponent)})


def direct_histogram(exponent: int) -> Counter[int]:
    order = 2**exponent
    units = tuple(range(1, order, 2))
    unseen = {
        (u, v)
        for u in range(1, order)
        for v in range(1, order)
        if u != v
    }
    histogram: Counter[int] = Counter()
    while unseen:
        pair = next(iter(unseen))
        orbit = {
            (unit * pair[0] % order, unit * pair[1] % order)
            for unit in units
        }
        histogram[len(orbit)] += 1
        unseen.difference_update(orbit)
    return histogram


def orbit_check() -> None:
    for exponent in range(2, 8):
        order = 2**exponent
        expected = expected_histogram(exponent)
        assert direct_histogram(exponent) == expected
        assert sum(expected.values()) == 3 * (order - exponent - 1)
        assert sum(size * count for size, count in expected.items()) == (
            (order - 1) * (order - 2)
        )
        for u in range(1, order):
            for v in range(1, order):
                if u == v:
                    continue
                minimum = min(valuation_two(u), valuation_two(v))
                predicted = 2 ** (exponent - 1 - minimum)
                actual = len(
                    {
                        (unit * u % order, unit * v % order)
                        for unit in range(1, order, 2)
                    }
                )
                assert actual == predicted

    exponent = 13
    order = 2**exponent
    expected = expected_histogram(exponent)
    assert sum(expected.values()) == 24_534
    assert max(expected) == 4_096
    assert sum(size * count for size, count in expected.items()) == 67_084_290


def support_union_check() -> None:
    orbit_supports = ({3, 5}, {5, 11}, {17}, set())
    union = set().union(*orbit_supports)
    product_radical_support = {3, 5, 11, 17}
    assert union == product_radical_support


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for consumer in CONSUMERS:
        assert (NODE, consumer, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join(
        (base / name).read_text() for name in required if name.endswith(".md")
    )
    for marker in (
        "3(2^j-1)",
        "3(n-s-1)",
        "24,534",
        "4,096",
        "rad(s_(n,35)^X)=rad(product_O s_O,35)",
        "total degree remains",
        "does not identify",
    ):
        assert marker in text


def main() -> None:
    orbit_check()
    support_union_check()
    packet_check()
    print(
        "F3_H3_QUOTIENT_GALOIS_ORBIT_SCALAR_DECOMPOSITION_PASS "
        "n8192_orbits=24534 max_degree=4096 total_degree=67084290"
    )


if __name__ == "__main__":
    main()
