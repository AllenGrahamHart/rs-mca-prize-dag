#!/usr/bin/env python3
"""Verify the HGE4 swap norm and Haar-band exclusion packet."""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_swap_norm_haar_band_exclusion"
DEPENDENCIES = {
    "f3_hge4_primitive_swap_odd_moment_router",
    "f3_hge4_cyclotomic_haar_near_quarter_swap_router",
}
CONSUMER = "f3_hge4_norm_gate_count"


def primitive_root(prime: int) -> int:
    factors: set[int] = set()
    value = prime - 1
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.add(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.add(value)
    for candidate in range(2, prime):
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors):
            return candidate
    raise AssertionError("primitive root not found")


def first_swap_control() -> int:
    prime, order, width = 257, 16, 3
    generator = pow(primitive_root(prime), (prime - 1) // order, prime)
    roots = [pow(generator, exponent, prime) for exponent in range(order)]
    survivors = 0
    # Choose one representative from each antipodal pair, then choose signs.
    for pair_indices in combinations(range(order // 2), width):
        for signs in range(1 << width):
            support = [
                roots[index + (order // 2 if signs >> offset & 1 else 0)]
                for offset, index in enumerate(pair_indices)
            ]
            if sum(support) % prime == 0:
                survivors += 1
    assert survivors == 0
    return survivors


def band_check() -> tuple[int, int]:
    total = 0
    top = 0
    for exponent in range(4, 42):
        order = 1 << exponent
        cap = order // (2 * exponent) - 1
        assert exponent * (cap + 1) <= order // 2
        assert exponent * (cap + 2) > order // 2
        if cap >= 1:
            total += cap
        if exponent == 41:
            top = cap
    assert top == 26_817_356_774
    return total, top


def exact_norm_criterion_check() -> int:
    checked = 0
    for exponent in range(4, 14):
        order = 1 << exponent
        quarter = order // 4
        cap = min(quarter - 4, order // (2 * exponent) - 1)
        for defect in range(1, max(0, cap) + 1):
            width = quarter - defect
            assert order ** (width - 1) >= width ** quarter
            checked += 1
    return checked


def haar_inclusion_check() -> int:
    checked = 0
    for exponent in range(4, 42):
        order = 1 << exponent
        logarithm = math.log(order)
        search_cap = max(0, math.ceil(math.sqrt(order) / (4 * logarithm)) - 1)
        haar_cap = 0
        for defect in range(1, search_cap + 2):
            width = order // 4 - defect
            x_value = 4 * (defect + 1) * logarithm
            block_count = 1 << math.ceil(math.log2(x_value))
            exponent_floor = 1 - (4 * defect + 8 * block_count) / order
            if (
                block_count < width
                and math.log(block_count * x_value) < exponent_floor * logarithm
            ):
                haar_cap = defect
        swap_cap = order // (2 * exponent) - 1
        assert haar_cap <= swap_cap
        checked += haar_cap
    assert checked == 39_487
    assert haar_cap == 9223
    return checked


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md", "dependency_subdag.md",
        "audit.md", "result.md", "verify.py", "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join((base / name).read_text() for name in required if name.endswith(".md"))
    for marker in (
        "m^(h-1)<h^(m/4)",
        "s(d+1)<=m/2",
        "26,817,356,774",
        "BX<m^(1-(4d+8B)/m)",
        "full Haar band",
        "E_h^prim(m,p)=0",
        "free pairs",
        "remain possible",
    ):
        assert marker in text


def main() -> None:
    control = first_swap_control()
    band_cells, top = band_check()
    exact_checks = exact_norm_criterion_check()
    haar_cells = haar_inclusion_check()
    packet_check()
    print(
        "F3_HGE4_SWAP_NORM_HAAR_BAND_EXCLUSION_PASS "
        f"control_survivors={control} band_cells={band_cells} "
        f"top_defect={top} exact_checks={exact_checks} haar_cells={haar_cells}"
    )


if __name__ == "__main__":
    main()
