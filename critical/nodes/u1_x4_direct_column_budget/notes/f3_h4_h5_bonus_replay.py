#!/usr/bin/env python3
"""Replay checks for the h=4/h=5 bonus reduction status note."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]


def load_json(path: Path):
    return json.loads(path.read_text())


def require_node_status(dag, node_id: str, status: str = "PROVED") -> None:
    by_id = {node["id"]: node for node in dag["nodes"]}
    node = by_id.get(node_id)
    if node is None:
        raise AssertionError(f"missing node {node_id}")
    if node.get("status") != status:
        raise AssertionError((node_id, node.get("status"), status))


def require_result(results, name: str):
    for row in results:
        if row.get("name") == name:
            return row
    raise AssertionError(f"missing result {name}")


def require_zero(row) -> None:
    if row.get("anchored_nontoral_trades") != 0:
        raise AssertionError(row)
    if row.get("direct_n3_exceeded"):
        raise AssertionError(row)


def require_h5_n32_certificate(rows) -> None:
    expected_primes = [
        1153,
        1217,
        1249,
        1409,
        1601,
        1697,
        1889,
        2017,
        2081,
        2113,
        2273,
        2593,
        2657,
        2689,
        2753,
        3041,
        3137,
        3169,
        3329,
        3361,
        3457,
        3617,
        4001,
        4129,
        4289,
        4481,
        4513,
        4673,
        4801,
        4993,
        5153,
        5281,
        5441,
        5569,
        5857,
        5953,
        6113,
        6337,
        6529,
        6689,
        6977,
        7297,
        7393,
        7457,
        7489,
        7649,
        7681,
        7841,
        7873,
        7937,
        8161,
        12289,
        32801,
        40961,
        61441,
        65537,
    ]
    if [row.get("p") for row in rows] != expected_primes:
        raise AssertionError(rows)
    for row in rows:
        expected = {
            "n": 32,
            "h": 5,
            "W": 32,
            "hashed": 31465,
            "probed": 169911,
            "anchored_toral_trades": 0,
            "anchored_nontoral_trades": 0,
            "partial": False,
            "complete": True,
            "direct_n3_exceeded": False,
        }
        for key, value in expected.items():
            if row.get(key) != value:
                raise AssertionError((key, row.get(key), value, row))


def require_h5_n64_certificate(rows) -> None:
    expected_primes = [
        4289,
        4481,
        4673,
        4801,
        4993,
        5441,
        5569,
        5953,
        6337,
        12289,
        40961,
        65537,
        262337,
    ]
    if [row.get("p") for row in rows] != expected_primes:
        raise AssertionError(rows)
    for row in rows:
        expected = {
            "n": 64,
            "h": 5,
            "W": 64,
            "hashed": 595665,
            "probed": 7028847,
            "anchored_toral_trades": 0,
            "anchored_nontoral_trades": 0,
            "partial": False,
            "complete": True,
            "direct_n3_exceeded": False,
        }
        for key, value in expected.items():
            if row.get(key) != value:
                raise AssertionError((key, row.get(key), value, row))


def require_h5_n96_certificate(row) -> None:
    expected = {
        "n": 96,
        "h": 5,
        "p": 9601,
        "W": 96,
        "hashed": 3183545,
        "probed": 57940519,
        "anchored_toral_trades": 0,
        "anchored_nontoral_trades": 0,
        "partial": False,
        "complete": True,
        "direct_n3_exceeded": False,
    }
    for key, value in expected.items():
        if row.get(key) != value:
            raise AssertionError((key, row.get(key), value, row))


def require_h5_n128_certificate(row, p: int = 17921) -> None:
    expected = {
        "n": 128,
        "h": 5,
        "p": p,
        "W": 128,
        "shards": 32,
        "shards_completed": 32,
        "hashed_per_shard": 10334625,
        "probed": 254231775,
        "anchored_toral_trades": 0,
        "anchored_nontoral_trades": 0,
        "partial": False,
        "complete": True,
        "direct_n3_exceeded": False,
    }
    for key, value in expected.items():
        if row.get(key) != value:
            raise AssertionError((key, row.get(key), value, row))
    rows = row.get("rows")
    if not isinstance(rows, list) or len(rows) != 32:
        raise AssertionError(row)
    if [r.get("shard") for r in rows] != list(range(32)):
        raise AssertionError(rows)
    if sum(r.get("probed", 0) for r in rows) != row["probed"]:
        raise AssertionError(row)


def require_h5_n128_extra_certificates(rows) -> None:
    expected_primes = [18049, 18433, 19073, 19457, 19841, 20353]
    if [row.get("p") for row in rows] != expected_primes:
        raise AssertionError(rows)
    for row in rows:
        require_h5_n128_certificate(row, p=row["p"])


def main() -> None:
    dag = load_json(ROOT / "dag.json")
    for node_id in (
        "h4_terminal_dichotomy",
        "x83_uniform_square_shift_obstruction_gate",
        "c1a_lowh_direct_certificates",
        "m720_h5_n32_gate_replay",
        "m720_remaining_gate_replay",
    ):
        require_node_status(dag, node_id)

    notes = ROOT / "critical/nodes/u1_x4_direct_column_budget/notes"
    a1 = load_json(notes / "f3a1_results.json")
    a2 = load_json(notes / "f3a2_results.json")

    gate = require_result(a1, "GATE_exceptional_n16_h4_p17")
    if gate.get("anchored_nontoral_trades", 0) <= 0:
        raise AssertionError(gate)

    require_zero(require_result(a1, "boundary_n32_h5_p1153_FULL"))
    for name in (
        "confine_n16_h4_p97",
        "confine_n16_h5_p97",
        "confine_n16_h4_p113",
        "confine_n16_h5_p113",
        "confine_n16_h4_p241",
        "confine_n16_h5_p241",
        "confine_n16_h4_p337",
    ):
        require_zero(require_result(a2, name))
    h5_rows = load_json(notes / "f3_h5_n32_multirow_certificate.json")
    require_h5_n32_certificate(h5_rows)
    h5_n64_rows = load_json(notes / "f3_h5_n64_multirow_certificate.json")
    require_h5_n64_certificate(h5_n64_rows)
    h5_n96_row = load_json(notes / "f3_h5_n96_boundary_certificate.json")
    require_h5_n96_certificate(h5_n96_row)
    h5_n128_row = load_json(notes / "f3_h5_n128_boundary_certificate.json")
    require_h5_n128_certificate(h5_n128_row)
    h5_n128_extra = load_json(notes / "f3_h5_n128_extra_primes_certificate.json")
    require_h5_n128_extra_certificates(h5_n128_extra)

    print("proved structural nodes: h4 dichotomy, x83 gate, c1a, m720 h5 gates")
    print("positive control n16/h4/p17:", gate["anchored_nontoral_trades"])
    print("verified q>=n^2 h4/h5 zero rows from f3a1/f3a2")
    print("h=5 n32 complete zero certificates:", len(h5_rows))
    print("h=5 n64 complete zero certificates:", len(h5_n64_rows))
    print("h=5 n96 boundary zero certificate:", h5_n96_row["p"])
    print("h=5 n128 sharded boundary zero certificate:", h5_n128_row["p"])
    print("h=5 n128 extra sharded zero certificates:", len(h5_n128_extra))
    print("H4_H5_BONUS_REDUCTION_PASS")


if __name__ == "__main__":
    main()
