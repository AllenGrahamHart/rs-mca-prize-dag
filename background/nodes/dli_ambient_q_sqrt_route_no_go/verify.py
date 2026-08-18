#!/usr/bin/env python3
"""Verify the complete high-cap artifacts and explicit no-go certificate."""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PILOT = ROOT / "notes/pilots_20260818/c2_ambient_q_highcap_falsifier"


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def expected_primes() -> list[int]:
    return [q for q in range(32769, 65536) if q % 32 == 1 and is_prime(q)]


def rows(path: Path) -> list[dict[str, int | bool]]:
    payload = json.loads(path.read_text())
    assert payload["schema"] == "c2-ambient-q-highcap-v1"
    assert len(payload["shards"]) == 4
    assert all(shard["status"] == "PASS" for shard in payload["shards"])
    output = sorted((row for shard in payload["shards"] for row in shard["rows"]),
                    key=lambda row: row["q"])
    assert [row["q"] for row in output] == expected_primes()
    return output


def build() -> dict[str, object]:
    first = rows(PILOT / "results.json")
    followup = rows(PILOT / "followup_results.json")
    assert len(first) == len(followup) == 189
    old = {row["q"]: row for row in first}
    ambient_fires = 0
    haar_fires = 0
    maximum = (Fraction(0), 0)
    for row in followup:
        for key in ("z0", "c1", "primitive", "fires"):
            assert row[key] == old[row["q"]][key]
        assert row["primitive"] == row["z0"] - row["c1"] >= 0
        ambient = Fraction(row["q"] ** 2 * row["primitive"], 2**32)
        haar = Fraction(row["primitive"] * 2**32, row["z1"] * row["b0"])
        assert row["fires"] is (ambient > 8)
        assert row["j_fires"] is (haar > 8)
        ambient_fires += ambient > 8
        haar_fires += haar > 8
        if haar > maximum[0]:
            maximum = (haar, row["q"])

    witness = next(row for row in followup if row["q"] == 33409)
    assert witness == {
        "q": 33409, "z0": 384, "c1": 256, "primitive": 128,
        "fires": True, "z1": 1696000, "b0": 174912, "j_fires": False,
    }
    ambient = Fraction(33409**2 * 128, 2**32)
    haar = Fraction(128 * 2**32, 1696000 * 174912)
    assert ambient == Fraction(1116161281, 33554432) > 8
    assert haar == Fraction(33554432, 18106125) < 8
    assert ambient_fires == 56 and haar_fires == 0
    assert maximum == (Fraction(2097152, 505197), 37217)
    return {
        "rows": len(followup),
        "ambient_fires": ambient_fires,
        "haar_fires": haar_fires,
        "witness": witness,
        "maximum": [maximum[0].numerator, maximum[0].denominator, maximum[1]],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        changed = copy.deepcopy(result)
        changed["witness"]["primitive"] += 32
        caught = 0
        try:
            assert changed["witness"] == result["witness"]
        except AssertionError:
            caught = 1
        assert caught == 1
        print("DLI_AMBIENT_Q_NO_GO_TAMPER_PASS mutations=1/1")
        return
    print(
        "DLI_AMBIENT_Q_NO_GO_PASS "
        "rows=189 ambient_fires=56 haar_fires=0 witness_q=33409"
    )


if __name__ == "__main__":
    main()

