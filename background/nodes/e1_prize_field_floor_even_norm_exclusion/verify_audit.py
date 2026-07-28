#!/usr/bin/env python3
"""Independent audit of the prize interval/parity argument."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_field_floor_even_norm_exclusion"
B_PRIZE = 317494674775468773183020924238786383963


def main() -> None:
    checks = 0
    lower = B_PRIZE << 128
    upper_norm = 1 << 256

    assert lower > 1 << 255
    assert upper_norm < 2 * lower
    assert upper_norm % 2 == 0
    checks += 3

    # Any divisor p>=lower has quotient at most one. Quotient one would make
    # the even norm equal to the odd prime.
    assert upper_norm // lower == 1
    assert 2 * lower > upper_norm
    checks += 2

    # Negative control: the RowC floor is too small for this argument.
    assert upper_norm >= 2 * 2**250
    checks += 1

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    assert "N=256 and S<=16" in statement
    assert "N=512 and S<=4" in statement
    assert "RowC rows retain" in statement
    checks += 3

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (NODE, "e1_low_square_mass_weighted_kernel_dictionary", "req") in edges
    assert (NODE, "e1_official_low_square_mass_pair_budget", "ev") in edges
    checks += 3

    print(
        "E1_PRIZE_FIELD_FLOOR_EVEN_NORM_EXCLUSION_AUDIT_PASS "
        f"rowc_mutation=1 checks={checks}"
    )


if __name__ == "__main__":
    main()
