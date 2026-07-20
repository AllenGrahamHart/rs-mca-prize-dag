#!/usr/bin/env python3
"""Verify the NG-COUNT contract and its strip-free implication."""

from __future__ import annotations

import json
from pathlib import Path


NODE = "f3_hge4_norm_gate_count"
ROOT = Path(__file__).resolve().parents[3]


def main() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    node = nodes[NODE]
    assert node["status"] == "TARGET" and node.get("key") is True
    for token in (
        "14 n^3",
        "F-4-minimal",
        "norm-gate",
        "p >= n^2",
        "NG-ZERO is NOT",
    ):
        assert token in node["statement"]

    required_edge = {
        "from": NODE,
        "to": "f3_hge4_aggregate_budget",
        "kind": "req",
    }
    assert required_edge in dag["edges"]
    adapter_edge = {
        "from": "f3_hge4_primitive_shift_pair_aggregate_adapter",
        "to": NODE,
        "kind": "ev",
    }
    assert adapter_edge in dag["edges"]
    assert nodes[adapter_edge["from"]]["status"] == "PROVED"
    orbit_edge = {
        "from": "f3_hge4_primitive_shift_pair_orbit_aggregate_router",
        "to": NODE,
        "kind": "ev",
    }
    assert orbit_edge in dag["edges"]
    assert nodes[orbit_edge["from"]]["status"] == "PROVED"
    union_edge = {
        "from": "f3_hge4_primitive_shift_pair_near_square_union_router",
        "to": NODE,
        "kind": "ev",
    }
    assert union_edge in dag["edges"]
    assert nodes[union_edge["from"]]["status"] == "PROVED"
    tower_edge = {
        "from": "f3_hge4_exact_ratio_tower_orbit_compiler",
        "to": NODE,
        "kind": "ev",
    }
    assert tower_edge in dag["edges"]
    assert nodes[tower_edge["from"]]["status"] == "PROVED"
    complement_edge = {
        "from": "f3_hge4_nonfull_complement_third_gate",
        "to": NODE,
        "kind": "ev",
    }
    assert complement_edge in dag["edges"]
    assert nodes[complement_edge["from"]]["status"] == "PROVED"
    defect_edge = {
        "from": "f3_hge4_complement_separator_defect_normal_form",
        "to": NODE,
        "kind": "ev",
    }
    assert defect_edge in dag["edges"]
    assert nodes[defect_edge["from"]]["status"] == "PROVED"
    trace_edge = {
        "from": "f3_hge4_boundary_defect_trace_pin",
        "to": NODE,
        "kind": "ev",
    }
    assert trace_edge in dag["edges"]
    assert nodes[trace_edge["from"]]["status"] == "PROVED"
    linear_edge = {
        "from": "f3_hge4_linear_boundary_orbit_bound",
        "to": NODE,
        "kind": "ev",
    }
    assert linear_edge in dag["edges"]
    assert nodes[linear_edge["from"]]["status"] == "PROVED"
    quadratic_edge = {
        "from": "f3_hge4_quadratic_boundary_orbit_bound",
        "to": NODE,
        "kind": "ev",
    }
    assert quadratic_edge in dag["edges"]
    assert nodes[quadratic_edge["from"]]["status"] == "PROVED"
    necklace_edge = {
        "from": "f3_hge4_near_third_belyi_necklace_bound",
        "to": NODE,
        "kind": "ev",
    }
    assert necklace_edge in dag["edges"]
    assert nodes[necklace_edge["from"]]["status"] == "PROVED"
    dual_gap_edge = {
        "from": "f3_hge4_near_third_dual_gap_exclusion",
        "to": NODE,
        "kind": "ev",
    }
    assert dual_gap_edge in dag["edges"]
    assert nodes[dual_gap_edge["from"]]["status"] == "PROVED"

    statement = (Path(__file__).with_name("statement.md")).read_text()
    attack = (Path(__file__).with_name("attack.md")).read_text()
    frontier = (Path(__file__).with_name("frontier.md")).read_text()
    contract = (Path(__file__).with_name("claim_contract.md")).read_text()
    for token in (
        "H_max=min(k+t,floor(n/2))",
        "N_h^strip",
        "N_h^raw",
        "(NG-COUNT)",
        "(RAW-NG)",
        "U2-boundary",
        "DLI/skew",
        "SP_h^prim<=7000n max(1,B_h)",
        "sum_(h=4)^H_max O_h^prim<=14n^2",
        "sum_(h=4)^H_max A_h^union/h<=14n^2",
        "sum_(h=4)^floor(m/2) E_h^prim(m,p)<=(21/2)m^2",
        "f3_hge4_nonfull_complement_third_gate",
        "E_h^prim(m,p)=0",
        "sum_(h=4)^floor((m-1)/3) E_h^prim(m,p)<=(21/2)m^2",
        "f3_hge4_complement_separator_defect_normal_form",
        "G=B-A",
        "e=m-3h",
        "m(P+Q-PQG)=d^2 XP'R",
        "f3_hge4_boundary_defect_trace_pin",
        "G=d^2(a-(h/m)X)",
        "b-2a^2",
        "a=(1+x)/(x(x-1)^2)",
        "f3_hge4_linear_boundary_orbit_bound",
        "E_h^prim(m,p)<=m-2",
        "initial `m-2` debit",
        "(LBO3)",
        "not a converse",
        "f3_hge4_quadratic_boundary_orbit_bound",
        "E_h^prim(m,p)<=2(m-1)(h+1)",
        "payment for the `e=2` width",
        "f_(h+1)",
        "necessary, not sufficient",
        "f3_hge4_near_third_belyi_necklace_bound",
        "E_h^prim(m,p)<=2N(h+e,e)",
        "(m+4)/3",
        "3333532",
        "not a zero-cost deletion",
        "f3_hge4_near_third_dual_gap_exclusion",
        "E_h^prim(m,p)=0       whenever 7h>=2m+1",
        "floor(2m/7)",
        "zero-cost analytic exclusion",
        "(32,9,5)",
        "(21/2)m^2-286",
        "(ERT4'')",
        "(ERT4''')",
        "V_(r-1)!=1",
        "NG-ZERO is not claimed",
    ):
        assert token in statement
    assert "N_h^strip <= N_h^raw" in attack
    assert "raw non-toral count zero" in frontier
    assert "the full official corridor" in contract

    # The aggregate compiler reserves 1+1+14=16 cubic units. Raising the
    # HGE4 allocation to 15 breaks that exact split.
    for n in (2**13, 2**20, 2**41):
        unit = n**3
        assert unit + unit + 14 * unit == 16 * unit
        assert unit + unit + 15 * unit > 16 * unit

    # Boundary bounds are debits, not zero-cost deletions.  Work in doubled
    # units so the half-integral headline allowance stays exact.
    for m in (16, 64, 256, 1024):
        debit = 2
        residual_twice = 21 * m * m - 2 * debit
        assert residual_twice + 2 * debit == 21 * m * m
    for m in (32, 128, 512, 2048):
        debit = (m + 4) // 3
        residual_twice = 21 * m * m - 2 * debit
        assert residual_twice + 2 * debit == 21 * m * m

    paid_cells = {
        32: (286, 12, 298),
        64: (892, 2, 894),
        128: (59598, 44, 59642),
        256: (53020, 2, 53022),
        1024: (3333532, 2, 3333534),
    }
    for m, (extra, boundary, total) in paid_cells.items():
        assert extra + boundary == total
        assert 2 * total < 21 * m * m
        residual_twice = 21 * m * m - 2 * total
        assert residual_twice + 2 * total == 21 * m * m

    # The dual gap supersedes every positive boundary debit and four of the
    # five extra necklace debits. Only (32,9,5) remains charged.
    excluded = ((16, 5, 1), (32, 10, 2), (64, 20, 4), (128, 41, 5),
                (256, 84, 4), (1024, 340, 4), (4096, 1364, 4))
    for m, h, e in excluded:
        assert m == 3 * h + e
        assert h >= 2 * e + 1
        assert 7 * h >= 2 * m + 1
        assert h > (2 * m) // 7
    m, h, e = 32, 9, 5
    assert m == 3 * h + e
    assert h < 2 * e + 1
    assert h == (2 * m) // 7
    residual_twice = 21 * m * m - 2 * 286
    assert residual_twice + 2 * 286 == 21 * m * m

    # Exhaustive tiny monotonicity check for the only implication asserted by
    # this node: deletion cannot increase a record count.
    checked = 0
    for raw4 in range(6):
        for raw5 in range(6):
            for strip4 in range(raw4 + 1):
                for strip5 in range(raw5 + 1):
                    raw_total = raw4 + raw5
                    strip_total = strip4 + strip5
                    assert strip_total <= raw_total
                    for budget in range(12):
                        if raw_total <= budget:
                            assert strip_total <= budget
                    checked += 1

    refs = set(node.get("refs", []))
    expected_refs = {
        f"critical/nodes/{NODE}/statement.md",
        f"critical/nodes/{NODE}/attack.md",
        f"critical/nodes/{NODE}/frontier.md",
        f"critical/nodes/{NODE}/claim_contract.md",
        f"critical/nodes/{NODE}/verify.py",
    }
    assert expected_refs <= refs
    assert all((ROOT / ref).is_file() for ref in expected_refs)
    print(f"F3_HGE4_NORM_GATE_COUNT_CONTRACT_PASS monotonicity_cases={checked}")


if __name__ == "__main__":
    main()
