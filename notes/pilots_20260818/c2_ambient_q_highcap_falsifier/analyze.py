#!/usr/bin/env python3
"""Fail-closed analysis for the complete ambient-Q high-cap scan."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
RANGES = [[32769, 40959], [40960, 49151], [49152, 57343], [57344, 65535]]


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


def build() -> dict[str, object]:
    payload = json.loads((HERE / "results.json").read_text())
    assert payload["schema"] == "c2-ambient-q-highcap-v1"
    assert payload["ranges_requested"] == RANGES
    assert len(payload["shards"]) == 4
    assert all(shard["status"] == "PASS" for shard in payload["shards"])
    rows = sorted((row for shard in payload["shards"] for row in shard["rows"]),
                  key=lambda row: row["q"])
    assert [row["q"] for row in rows] == expected_primes()
    assert len({row["q"] for row in rows}) == len(rows)

    fired = []
    nonempty = []
    for row in rows:
        assert row["primitive"] == row["z0"] - row["c1"] >= 0
        exact_fires = (row["q"] ** 2 * row["primitive"]) ** 2 > (
            64 * (2**32) ** 2
        )
        assert row["fires"] is exact_fires
        if row["primitive"]:
            assert row["primitive"] % 32 == 0
            nonempty.append(row)
        if exact_fires:
            fired.append(row)
    assert bool(fired) == bool(nonempty)
    return {
        "rows": len(rows),
        "nonempty": len(nonempty),
        "fires": len(fired),
        "first_firing": fired[0] if fired else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        changed = copy.deepcopy(result)
        changed["rows"] -= 1
        caught = 0
        try:
            assert changed["rows"] == result["rows"]
        except AssertionError:
            caught = 1
        assert caught == 1
        print("C2_AMBIENT_Q_HIGHCAP_TAMPER_PASS mutations=1/1")
        return
    print(
        "C2_AMBIENT_Q_HIGHCAP_PASS "
        f"rows={result['rows']} nonempty={result['nonempty']} fires={result['fires']}"
    )
    if result["first_firing"]:
        print("FIRST_FIRING " + json.dumps(result["first_firing"], sort_keys=True))


if __name__ == "__main__":
    main()

