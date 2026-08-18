#!/usr/bin/env python3
"""Verify the complete xi2/pairing0 chart and transport composition."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
QUOTIENT = EXP / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_quotient.py"
PARENTS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_matching_resultant_projective_charts",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_xi2_pairing0_all_infinity_chart_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_xi2_pairing0_one_finite_chart_exclusions",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_xi2_pairing0_ffi_fif_collapsed_common_exclusions",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_xi2_pairing0_iff_rational_branch_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_xi2_pairing0_fff_chart_complete_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_split_cells3_6_v4_quotient",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_split_cells3_6_basis_case0_orbit_exclusion",
}
TARGET = (3, "S0", -1, -1, -1, 2, 0)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def validate(statuses):
    require(statuses == {identifier: "PROVED" for identifier in PARENTS},
            "proved chart and transport parents")


def main():
    statuses = {
        identifier: json.loads(
            (ROOT / "background/nodes" / identifier / "node.json").read_text()
        )["node"]["status"] for identifier in PARENTS
    }
    validate(statuses)
    own = json.loads((NODE / "node.json").read_text())
    require({row["from"] for row in own["requires"]} == PARENTS,
            "exact parent set")
    spec = importlib.util.spec_from_file_location("cells36_quotient", QUOTIENT)
    quotient = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(quotient)
    manifest = quotient.representative_manifest()
    require(manifest["representative_count"] == 1416 and
            TARGET in manifest["representatives"], "representative ledger")
    matchings = tuple(quotient.BC.pairings(range(6)))
    first = lambda row: quotient.bc_action(row, matchings)
    second = quotient.secondary_action
    orbit = {TARGET, first(TARGET), second(TARGET), first(second(TARGET))}
    require(len(orbit) == 4, "four-case orbit")
    require(own["node"]["status"] == "PROVED" and
            "1,414 remain" in own["node"]["statement"], "residual scope")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_XI2_PAIRING0_"
          "COMPLETE_VERIFY_PASS charts=8 orbit=4 residual=1414")


if __name__ == "__main__":
    main()
