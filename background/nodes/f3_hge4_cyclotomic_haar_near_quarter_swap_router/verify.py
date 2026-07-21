#!/usr/bin/env python3
"""Verify the HGE4 cyclotomic-Haar near-quarter swap router."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_cyclotomic_haar_near_quarter_swap_router"
DEPENDENCIES = {
    "f3_hge4_exact_ratio_tower_orbit_compiler",
    "f3_hge4_primitive_swap_odd_moment_router",
}
CONSUMER = "f3_hge4_norm_gate_count"


def collapse(values: list[int]) -> list[int]:
    half = len(values) // 2
    return [values[index] + values[index + half] for index in range(half)]


def difference_energy(values: list[int]) -> int:
    half = len(values) // 2
    return sum(
        (values[index] - values[index + half]) ** 2 for index in range(half)
    )


def haar_identity_check() -> int:
    fixtures = [
        [1, 0, -1, 0, -1, 0, 1, 0],
        [1, -1, 0, 0, 0, 0, -1, 1],
        [1, 0, 0, -1, 1, 0, 0, -1],
    ]
    checked = 0
    for values in fixtures:
        current = values
        while len(current) >= 2:
            following = collapse(current)
            assert difference_energy(current) + sum(x * x for x in following) == 2 * sum(
                x * x for x in current
            )
            current = following
            checked += 1
    return checked


def admitted_band_check() -> tuple[int, int, dict[int, int], dict[int, int]]:
    exact_total = 0
    clean_total = 0
    exact_maxima: dict[int, int] = {}
    clean_maxima: dict[int, int] = {}
    for exponent in range(4, 42):
        order = 1 << exponent
        logarithm = math.log(order)
        search_cap = max(0, math.ceil(math.sqrt(order) / (4 * logarithm)) - 1)
        exact_admitted: list[int] = []
        clean_admitted: list[int] = []
        for defect in range(1, search_cap + 2):
            width = order // 4 - defect
            if width < 4:
                continue
            x_value = 4 * (defect + 1) * logarithm
            tower_depth = math.ceil(math.log2(x_value))
            block_count = 1 << tower_depth
            assert x_value <= block_count < 2 * x_value
            exponent_floor = 1 - (4 * defect + 8 * block_count) / order
            exact = (
                block_count < width
                and math.log(block_count * x_value) < exponent_floor * logarithm
            )
            clean = 64 * (defect + 1) ** 2 * logarithm**2 < order
            if clean:
                assert exact
                clean_admitted.append(defect)
                clean_total += 1
            if not exact:
                continue
            for level in range(1, tower_depth + 1):
                scale = 1 << level
                cutoff = (width - 1) // scale
                prime_count = (cutoff + 1) // 2
                assert prime_count >= 1
                exact_norm_log_floor = (
                    8 * scale * prime_count * logarithm / order
                )
                assert exact_norm_log_floor > math.log(scale * x_value)
            exact_admitted.append(defect)
            exact_total += 1
        if exact_admitted:
            assert exact_admitted == list(range(1, exact_admitted[-1] + 1))
            exact_maxima[exponent] = exact_admitted[-1]
        if clean_admitted:
            assert clean_admitted == list(range(1, clean_admitted[-1] + 1))
            clean_maxima[exponent] = clean_admitted[-1]
    assert exact_total == 39_487
    assert min(exact_maxima) == 15 and exact_maxima[15] == 2
    assert exact_maxima[41] == 9223
    assert clean_total == 23_777
    assert min(clean_maxima) == 15 and clean_maxima[15] == 1
    assert clean_maxima[41] == 6521
    return exact_total, clean_total, exact_maxima, clean_maxima


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
        "B<h,       BX<m^(1-(4d+8B)/m)",
        "64(d+1)^2(log m)^2<m",
        "0<=L<4(d+1)log m",
        "z_1=z_2=...=z_T=0",
        "L=0",
        "antipodal-swap",
        "does not bound the odd swap count",
    ):
        assert marker in text


def main() -> None:
    haar_checks = haar_identity_check()
    exact_cells, clean_cells, exact_maxima, clean_maxima = admitted_band_check()
    packet_check()
    print(
        "F3_HGE4_CYCLOTOMIC_HAAR_NEAR_QUARTER_SWAP_ROUTER_PASS "
        f"haar_checks={haar_checks} exact_cells={exact_cells} "
        f"clean_cells={clean_cells} first_level={min(exact_maxima)} "
        f"top_defect={exact_maxima[41]} clean_top={clean_maxima[41]}"
    )


if __name__ == "__main__":
    main()
