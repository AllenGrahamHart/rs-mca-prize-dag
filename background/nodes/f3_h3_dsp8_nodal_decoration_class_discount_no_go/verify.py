#!/usr/bin/env python3
"""Verify the DSP8 nodal decoration class-discount counterexample."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_nodal_decoration_class_discount_no_go"
DEPENDENCIES = {
    "f3_h3_dsp8_unit_product_trace_normal_form",
    "f3_h3_dsp8_nodal_target_divisor_pruning",
}
CONSUMERS = {"f3_h3_dsp8_correlation_bound"}
PRIME = 769
ORDER = 256
GENERATOR = 562
LEFT = (218, 643, 680)
RIGHT = (94, 679, 768)
EXPECTED_TARGETS = ((83, 611, 258), (50, 411, 539), (187, 205, 183))
EXPECTED_PRODUCTS = ((86, 96, 88), (72, 74, 98), (80, 78, 74))
EXPECTED_QUOTIENTS = ((84, 84, 79), (84, 84, 79), (90, 79, 89))
EXPECTED_ANTIPODAL = (
    (True, False, True),
    (True, True, True),
    (False, True, True),
)


def subgroup() -> set[int]:
    return {pow(GENERATOR, exponent, PRIME) for exponent in range(ORDER)}


def matrix_fixture() -> dict:
    group = subgroup()
    assert len(group) == ORDER
    assert pow(GENERATOR, ORDER, PRIME) == 1
    assert pow(GENERATOR, ORDER // 2, PRIME) == PRIME - 1

    for triple in (LEFT, RIGHT):
        assert set(triple) <= group
        assert sum(triple) % PRIME == 3
        product = 1
        for value in triple:
            product = product * value % PRIME
        assert product == 1
    signed = set(LEFT + RIGHT) | {(-value) % PRIME for value in LEFT + RIGHT}
    assert len(signed) == 12

    shifted = [(1 - value) % PRIME for value in group if value != 1]
    product_counts = Counter(
        left * right % PRIME for left in shifted for right in shifted
    )
    quotient_counts = Counter(
        right * pow(left, -1, PRIME) % PRIME
        for left in shifted
        for right in shifted
    )
    squares = {value * value % PRIME for value in group}

    targets: list[tuple[int, ...]] = []
    products: list[tuple[int, ...]] = []
    quotients: list[tuple[int, ...]] = []
    antipodal: list[tuple[bool, ...]] = []
    for left in LEFT:
        target_row = []
        product_row = []
        quotient_row = []
        antipodal_row = []
        for right in RIGHT:
            deficit = left * right * (3 - left - right) % PRIME
            target = (1 - deficit) % PRIME
            target_row.append(target)
            product_row.append(product_counts[target])
            quotient_row.append(quotient_counts[target])
            antipodal_row.append(deficit in squares)
        targets.append(tuple(target_row))
        products.append(tuple(product_row))
        quotients.append(tuple(quotient_row))
        antipodal.append(tuple(antipodal_row))

    packet = {
        "targets": tuple(targets),
        "products": tuple(products),
        "quotients": tuple(quotients),
        "antipodal": tuple(antipodal),
    }
    assert packet["targets"] == EXPECTED_TARGETS
    assert packet["products"] == EXPECTED_PRODUCTS
    assert packet["quotients"] == EXPECTED_QUOTIENTS
    assert packet["antipodal"] == EXPECTED_ANTIPODAL
    assert all(target not in {0, 1} for row in targets for target in row)
    assert min(value for row in products for value in row) == 72
    assert min(value for row in quotients for value in row) == 79
    assert sum(value for row in antipodal for value in row) == 7
    assert PRIME < ORDER**2
    return packet


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
        "seven antipodal decorations",
        "`769<256^2`",
        "does not falsify DSP8",
        "field-size-dependent",
        "decoration-only",
    ):
        assert marker in text


def main() -> None:
    matrix_fixture()
    packet_check()
    print(
        "F3_H3_DSP8_NODAL_DECORATION_CLASS_DISCOUNT_NO_GO_PASS "
        "field=769 order=256 decorations=9 antipodal=7 min_P=72 min_R=79"
    )


if __name__ == "__main__":
    main()
