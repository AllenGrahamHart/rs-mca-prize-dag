#!/usr/bin/env python3
"""Independent audit for the positive 433-1b cell-0 exclusion."""

import ast
import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
PRIME = 2130706433
IOTA = 16711679


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    scripts = (
        EXPERIMENTS / "rate_half_kb_positive_433_1b_principal_common_charts_modal.py",
        EXPERIMENTS / "rate_half_kb_positive_433_1b_cell0_principal_component_compiler_modal.py",
        EXPERIMENTS / "rate_half_kb_positive_433_1b_cell0_principal_outside_modal.py",
    )
    for script in scripts:
        ast.parse(script.read_text())
    component_result = (
        EXPERIMENTS / "rate_half_kb_positive_433_1b_cell0_principal_component_compiler_result.json"
    )
    outside = json.loads((
        EXPERIMENTS / "rate_half_kb_positive_433_1b_cell0_principal_outside_result.json"
    ).read_text())
    require(outside["source_components_sha256"] ==
            hashlib.sha256(component_result.read_bytes()).hexdigest(), "source custody")
    source = scripts[2].read_text()
    for snippet in (
        "relation_x",
        "target_values[left]**2 - target_values[right]**2",
        "list S{index}=sat(G,H{index})",
        "missing_label*b1_missing*b1_missing",
        "for pairing_index in selected_pairing_indices",
    ):
        require(snippet in source, f"outside construction {snippet}")
    inverse_two = pow(2, -1, PRIME)
    require(IOTA*IOTA % PRIME == PRIME - 1, "iota")
    for source_sign in (-1, 1):
        alpha = (1 + source_sign*IOTA)*inverse_two % PRIME
        require((2*alpha - 1 - source_sign*IOTA) % PRIME == 0, "alpha sign")
        require((-2*source_sign*IOTA*IOTA) % PRIME != 0, "split branch guard")
    keys = {
        (row["component"], row["source_sign"], tuple(row["sigma"]),
         row["xi_index"], row["pairing_index"])
        for row in outside["rows"]
    }
    require(len(keys) == 1680 and all(row["unit"] for row in outside["rows"]),
            "independent outside census")
    print("audit=ok exact_split=2 source_signs=2 outside_cases=1680")


if __name__ == "__main__":
    main()
