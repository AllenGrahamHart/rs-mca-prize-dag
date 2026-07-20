#!/usr/bin/env python3
"""Exact replay of the RF3-double-prime KoalaBear safe-row corollary."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
NODE_ID = "paving_rf3_double_prime_koalabear_safe_rows"

BRIDGE_HASH = "284b4cb81f308499eb91d5d2470c71c097d2fd36e4bbfebfe2d6432b683e5092"
AUDIT_HASH = "fb2400cd2ed67178cc5ef0d58d7565236f33af9ffadbeeed0b4ea4abd7cdcf75"

ROWS = (
    {
        "rate": "1/2",
        "K": 1_048_576,
        "r": 611_982,
        "A": 1_485_170,
        "m": 119,
        "U": 176_735_230,
        "V": 169,
        "W": 27_525,
        "upper": 274_589_064_742_753_629,
        "margin": 391_663_368_641_458,
    },
    {
        "rate": "1/4",
        "K": 524_288,
        "r": 1_045_433,
        "A": 1_051_719,
        "m": 104,
        "U": 109_378_776,
        "V": 209,
        "W": 29_028,
        "upper": 274_721_012_201_293_956,
        "margin": 259_715_910_101_131,
    },
    {
        "rate": "1/8",
        "K": 262_144,
        "r": 1_352_390,
        "A": 744_762,
        "m": 90,
        "U": 67_028_580,
        "V": 256,
        "W": 31_500,
        "upper": 274_578_888_391_562_205,
        "margin": 401_839_719_832_882,
    },
    {
        "rate": "1/16",
        "K": 131_072,
        "r": 1_569_744,
        "A": 527_408,
        "m": 78,
        "U": 41_137_824,
        "V": 314,
        "W": 34_101,
        "upper": 274_861_787_390_263_486,
        "margin": 118_940_721_131_601,
    },
)


def ceil_fraction(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_sources() -> None:
    bridge = HERE / "upstream_bridge.md"
    audit = HERE / "upstream_ordinary_audit.md"
    assert digest(bridge) == BRIDGE_HASH
    assert digest(audit) == AUDIT_HASH
    assert "Status: PROVED" in bridge.read_text()
    assert "Status: AUDIT PASS (mathematics)" in audit.read_text()


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE_ID]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (NODE_ID, "mca_safe", "ev") in edges
    assert (NODE_ID, "compiler", "ev") in edges


def check_rows(rows: tuple[dict[str, int | str], ...] = ROWS) -> None:
    p = 2**31 - 2**24 + 1
    q = p**6
    n = 2**21
    eps = Fraction(1, 2**64)
    budget = q // 2**128

    assert p - 1 == 127 * 2**24
    assert 127 < 2**24
    assert pow(3, (p - 1) // 2, p) == p - 1
    assert (p - 1) % n == 0
    assert budget == 274_980_728_111_395_087

    for row in rows:
        K = int(row["K"])
        r = int(row["r"])
        A = int(row["A"])
        m = int(row["m"])
        U = int(row["U"])
        V = int(row["V"])
        W = int(row["W"])

        dx = Fraction(U - 1) + eps
        dy = Fraction(V - 1) + eps
        dz = Fraction(W - 1) + eps

        assert A == n - r
        assert K * int(row["rate"].split("/")[1]) == n
        assert ceil_fraction(dx) == U
        assert ceil_fraction(dy) == V
        assert ceil_fraction(dz) == W
        assert V >= m and W >= V
        assert U > K * (V - 1)
        assert dx < m * A
        assert p > V - 1
        assert (A - K - 1) * (2 * U - 1) > (n - K - 1) * (2 * K + 1)
        assert q > 2 * U * dy

        interpolation = sum((U - K * j) * (W - j) for j in range(V))
        conditions = n * sum((W - s) * (m - s) for s in range(m))
        assert interpolation > conditions

        threshold = (1 + 2 * U * dy * dy) * dz + (r + 1) * dy
        upper = ceil_fraction(threshold)
        assert upper == int(row["upper"])
        assert budget - upper == int(row["margin"])
        assert upper <= budget


def main() -> None:
    check_sources()
    check_dag()
    check_rows()
    print("PAVING_RF3_DOUBLE_PRIME_KOALABEAR_SAFE_ROWS_PASS rows=4")


if __name__ == "__main__":
    main()
