#!/usr/bin/env python3
"""Independent audit for positive 433-1b cells 1 and 2."""

import ast
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    script = EXPERIMENTS / "rate_half_kb_positive_433_1b_principal_common_charts_modal.py"
    result = EXPERIMENTS / "rate_half_kb_positive_433_1b_cells1_2_principal_common_charts_result.json"
    ast.parse(script.read_text())
    source = script.read_text()
    for snippet in ("for value in charts.split", "itertools.product", "z*({guard})*h-1"):
        require(snippet in source, f"chart construction {snippet}")
    payload = json.loads(result.read_text())
    keys = {(row["cell"], tuple(row["epsilon"]), row["chart"])
            for row in payload["rows"]}
    require(len(keys) == 48 and {key[0] for key in keys} == {1, 2}, "row census")
    require(all(row["unit"] and row["dimension"] == -1 and
                row["basis_size"] == 1 for row in payload["rows"]), "unit audit")
    print("audit=ok cells=2 signs=4 charts=6 unit=48")


if __name__ == "__main__":
    main()
