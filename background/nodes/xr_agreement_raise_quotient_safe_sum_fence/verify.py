#!/usr/bin/env python3
"""Verify the XR agreement-raise quotient safe-sum fence."""

from __future__ import annotations

from math import comb
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_agreement_raise_quotient_safe_sum_fence"
DEPENDENCIES = {
    "census_bounded_scales",
    "xr_target_budget_audit",
    "xr_mismatch_terminal_tangent_agreement_raise",
}
CONSUMER = "xr_tangent_support_mismatch_bridge"
PRIZE_BSTAR = 317494674775468773183020924238786383963


ROWS = (
    ("RowC-1/4", 1 << 10, 1 << 8, 261, 1 << 3, 261, 1 << 122),
    ("RowC-1/8", 1 << 10, 1 << 7, 133, 1 << 3, 135, 1 << 122),
    ("RowC-1/16", 1 << 10, 1 << 6, 67, 1 << 4, 79, 1 << 122),
    (
        "prize-1/4",
        1 << 41,
        1 << 39,
        558345748481,
        1 << 34,
        558345748481,
        PRIZE_BSTAR,
    ),
    (
        "prize-1/8",
        1 << 41,
        1 << 38,
        283467841537,
        1 << 34,
        283467841537,
        PRIZE_BSTAR,
    ),
    (
        "prize-1/16",
        1 << 41,
        1 << 37,
        141733920769,
        1 << 33,
        141733920769,
        PRIZE_BSTAR,
    ),
)


def quotient_envelope(n: int, k: int, agreement: int) -> int:
    reserve = agreement - k
    total = 0
    quotient_length = 2
    while quotient_length <= n and quotient_length * reserve <= n:
        selected = (n - agreement) * quotient_length // n
        if 1 <= selected < quotient_length:
            total += comb(quotient_length, selected)
        quotient_length *= 2
    return total


def arithmetic_check() -> tuple[int, int]:
    assert PRIZE_BSTAR**10 <= 1 << 1279 < (PRIZE_BSTAR + 1) ** 10
    comparisons = 0
    fixed_ledgers = 0
    for name, n, k, agreement, fiber, support_size, threshold in ROWS:
        quotient_length = n // fiber
        assert quotient_length in (64, 128, 256)
        assert agreement <= support_size <= n
        assert support_size - k < fiber
        profile, remainder = divmod(support_size, fiber)
        residual_ambient = n - fiber * profile

        if name.startswith("RowC"):
            summand = comb(quotient_length, profile) * comb(
                residual_ambient, remainder
            )
            assert summand > threshold
        else:
            assert support_size == agreement
            assert profile == k // fiber
            assert residual_ambient == n - k
            assert remainder == agreement - k
            assert 4 <= remainder <= residual_ambient // 2
            assert comb(residual_ambient, 4) > threshold
        comparisons += 1

        fixed = quotient_envelope(n, k, agreement)
        assert fixed + (n - agreement + 1) + 16 * n**3 <= threshold
        fixed_ledgers += 1
    return comparisons, fixed_ledgers


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "activeonlywhen`c>B-k`",
        "`(c,B)=(8,261),(8,135),(16,79)`",
        "sharperdistinct-slopeimage/coalescingtheorem",
        "doesnotassertthattheactualquotientslopeunion",
    ):
        assert marker in statement


def main() -> None:
    comparisons, fixed_ledgers = arithmetic_check()
    packet_check()
    print(
        "XR_AGREEMENT_RAISE_QUOTIENT_SAFE_SUM_FENCE_PASS "
        f"oversized_terms={comparisons} fixed_ledgers={fixed_ledgers}"
    )


if __name__ == "__main__":
    main()
