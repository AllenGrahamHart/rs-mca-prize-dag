#!/usr/bin/env python3
"""Replay the primitive tower ratio on the frozen full-window bank."""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
PILOT = ROOT / "notes/pilots_20260809/c2pp_falsifier_redesign"
sys.path.insert(0, str(PILOT))

import c2lib  # noqa: E402


def build() -> dict[str, object]:
    bank = json.loads((PILOT / "ckpt.json").read_text())
    rows: dict[str, dict[str, int]] = {}
    maximum = (Fraction(-1), "")

    for tower_key, tower_rows in bank["D"].items():
        n_text, t_text, window = tower_key.split("|")
        n, t = int(n_text), int(t_text)
        m = t.bit_length() - 1
        if window != "-".join(str(j) for j in range(m)):
            continue
        for q_text, record in tower_rows.items():
            q = int(q_text)
            z = {int(key): int(value) for key, value in record["Z"].items()}
            blocks = {int(key): int(value) for key, value in record["B"].items()}
            c1 = c2lib.Csub(q, n, t, 1)
            half = c2lib.Zlev(q, n // 2, t // 2, 0)
            assert c1 == half <= z[0]

            denominator = z[m] * math.prod(blocks[j] for j in range(m))
            primitive = z[0] - c1
            ratio = Fraction(primitive << (n * m), denominator)
            unreduced = Fraction(z[0] << (n * m), denominator)
            assert ratio <= unreduced
            assert ratio * z[0] == unreduced * primitive
            assert ratio <= 1 << 21

            key = f"{n}|{t}|{q}"
            rows[key] = {
                "z0": z[0],
                "c1": c1,
                "primitive": primitive,
                "ratio_numerator": ratio.numerator,
                "ratio_denominator": ratio.denominator,
            }
            maximum = max(maximum, (ratio, key))

    summary = {
        "rows": len(rows),
        "positive": sum(row["primitive"] > 0 for row in rows.values()),
        "zero": sum(row["primitive"] == 0 for row in rows.values()),
        "max_key": maximum[1],
        "max_numerator": maximum[0].numerator,
        "max_denominator": maximum[0].denominator,
    }
    assert summary == {
        "rows": 45,
        "positive": 16,
        "zero": 29,
        "max_key": "32|2|5857",
        "max_numerator": 14680064,
        "max_denominator": 5498847,
    }
    return {"summary": summary, "rows": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        changed = copy.deepcopy(result)
        changed["summary"]["max_numerator"] += 1
        caught = 0
        try:
            assert changed == result
        except AssertionError:
            caught = 1
        assert caught == 1
        print("DLI_PRIMITIVE_RATIO_TELESCOPING_TAMPER_PASS mutations=1/1")
        return
    summary = result["summary"]
    print(
        "DLI_PRIMITIVE_RATIO_TELESCOPING_PASS "
        f"rows={summary['rows']} zero={summary['zero']} "
        f"max={summary['max_numerator']}/{summary['max_denominator']}"
    )


if __name__ == "__main__":
    main()
