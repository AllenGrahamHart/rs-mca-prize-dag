#!/usr/bin/env python3
"""Checks for the selected-antipodal infinity affine compiler."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_selected_antipodal_infinity_affine_intersection_compiler"
BRANCH_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_barycentric_collision_branch_compiler"
INFINITY_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_infinity_cell_torsion_gate"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 97
ORDER = 32


def affine_values(a: int, y: int) -> tuple[int, int]:
    first = ((a + 2) * y - (a + 1)) % PRIME
    second = ((a - 1) * y + (2 - a)) % PRIME
    return first, second


def main() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    incoming = {
        edge["from"]
        for edge in dag["edges"]
        if edge["to"] == NODE_ID and edge.get("kind") == "req"
    }
    outgoing = {
        edge["to"]
        for edge in dag["edges"]
        if edge["from"] == NODE_ID and edge.get("kind") == "ev"
    }
    assert nodes[NODE_ID]["status"] == "PROVED"
    assert incoming == {BRANCH_DEP, INFINITY_DEP}
    assert CONSUMER in outgoing

    # Reorder the checked infinity quartet so the equal-weight pair is first.
    ell_1, ell_2, ell_3, ell_4 = 12, 67, 42, 28
    inverse_six = pow(6, -1, PRIME)
    d = (ell_1 - ell_2) * inverse_six % PRIME
    assert (ell_3 - ell_4) % PRIME == 2 * d % PRIME
    a = (ell_1 + ell_2 - ell_3 - ell_4) * pow(4 * d, -1, PRIME) % PRIME
    assert a * a % PRIME == -2 % PRIME

    tau = ell_4
    y = ell_3 * pow(ell_4, -1, PRIME) % PRIME
    first, second = affine_values(a, y)
    assert first == ell_1 * pow(tau, -1, PRIME) % PRIME
    assert second == ell_2 * pow(tau, -1, PRIME) % PRIME
    assert y != 1
    assert all(pow(value, ORDER, PRIME) == 1 for value in (tau, y, first, second))

    p_src = pow(ell_1 * ell_2 * ell_3 * ell_4, -1, PRIME)
    assert pow(tau, 4, PRIME) * y * first * second % PRIME == pow(p_src, -1, PRIME)
    z_inf = p_src * y * first * second % PRIME
    assert z_inf == pow(tau, -4, PRIME)
    assert pow(z_inf, ORDER // 4, PRIME) == 1
    assert pow(z_inf, ORDER // 8, PRIME) != 1

    v = (y + 1) * pow(y - 1, -1, PRIME) % PRIME
    u = (a + v) % PRIME
    assert d == tau * (y - 1) * pow(2, -1, PRIME) % PRIME
    reconstructed = [
        d * (u + a + 3) % PRIME,
        d * (u + a - 3) % PRIME,
        d * (u - a + 1) % PRIME,
        d * (u - a - 1) % PRIME,
    ]
    assert reconstructed == [ell_1, ell_2, ell_3, ell_4]

    new_a = -a % PRIME
    new_y = pow(y, -1, PRIME)
    new_tau = tau * y % PRIME
    new_first, new_second = affine_values(new_a, new_y)
    relabelled = [new_tau * new_first % PRIME, new_tau * new_second % PRIME,
                  new_tau * new_y % PRIME, new_tau]
    assert relabelled == [ell_2, ell_1, ell_4, ell_3]

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_SELECTED_ANTIPODAL_INFINITY_AFFINE_PASS "
        "normal_form=1 affine_maps=2 torsion=4 product=1 quarter_order=1 "
        "converse=1 involution=1 wiring=3"
    )


if __name__ == "__main__":
    main()
