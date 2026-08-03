#!/usr/bin/env python3
"""Independent audit of the cell-3 quadratic quotient packet."""

import ast
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_birational_profile_modal.py"
RESULT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_birational_profile_result.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "base_rows = [*product_rows, sum_rows[1]]",
        "for index in (2, 3, 4)",
        "quotient_saturation_stages",
        "ring L={PRIME},(c,b,t,r),lp;",
        "ideal Q=K[1],K[3],K[7]; Q=std(Q);",
        "list QSC=sat(Q,LDC)",
        "list QSB=sat(Q,LDB)",
        "b_leading_expected = r*r*(t + epsilon_2*IOTA*r)",
        "c_denominator = t - epsilon_1 * epsilon_2 * r * r",
    ):
        require(snippet in source, f"source construction {snippet}")

    payload = json.loads(RESULT.read_text())
    rows = payload["rows"]
    keys = {(*row["epsilon"], row["chart"]) for row in rows}
    require(keys == set(itertools.product((-1, 1), (-1, 1), range(6))),
            "Cartesian cover")
    require(len(rows) == 24 and all(
        row["status"] == "COMPLETE" and
        row["dimension"] == row["quotient_dimension"] == 1 and
        row["basis_size"] == row["quotient_basis_size"] == 10 and
        row["c_boundary_unit"] and row["b_boundary_unit"] and
        row["quotient_remainders"] == ["0"] * 10
        for row in rows
    ), "exact quotient transcript")
    for row in rows:
        interface = row["quotient_interface"]
        require(interface["b_leading"] == interface["b_constant"],
                "palindromic coefficient summaries")
        require(interface["base_relation"] == row["basis"][0] and
                interface["b_relation"] == row["basis"][2] and
                interface["c_relation"] == row["basis"][6],
                "three selected generators")

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    require("does not assert birationality" in statement and
            "outside signed-edge exclusion" in statement and
            "saturation cannot move" in proof and
            "Do not return" in frontier,
            "nonclaim and containment audit")
    print("audit=ok charts=24 generators=3 reductions=240 outside=open")


if __name__ == "__main__":
    main()
