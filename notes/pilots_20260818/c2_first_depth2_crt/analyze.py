#!/usr/bin/env python3
"""Exact CRT reconstruction for the first depth-two C2 row."""

from __future__ import annotations

import argparse
import copy
from decimal import Decimal, localcontext
from fractions import Fraction
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
TARGET_MODULI = {
    1152921504606850301,
    1152921504606873847,
    1152921504606875777,
}
CONTROL = {
    "z0": 455744,
    "c1": 736,
    "z1": 44299296,
    "b0": 44278048,
}
EXPECTED_COUNTS = {
    "z0": 13295206688,
    "c1": 116512,
    "z1": 495229865162016,
    "z2": 95579012297974912,
    "b0": 495228544669824,
    "b1": 95578985107762144,
}


def prime64(value: int) -> bool:
    if value < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value % p == 0:
            return value == p
    d, s = value - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if base % value == 0:
            continue
        x = pow(base, d, value)
        if x in (1, value - 1):
            continue
        for _ in range(s - 1):
            x = x * x % value
            if x == value - 1:
                break
        else:
            return False
    return True


def crt(rows: list[tuple[int, int]]) -> tuple[int, int]:
    value, product = 0, 1
    for residue, modulus in rows:
        step = (residue - value) * pow(product, -1, modulus) % modulus
        value += product * step
        product *= modulus
    return value, product


def build(payload: dict[str, object] | None = None) -> dict[str, object]:
    if payload is None:
        payload = json.loads((HERE / "results.json").read_text())
    assert payload["schema"] == "c2-first-depth2-crt-v1"
    assert payload["tasks_requested"] == payload["tasks_returned"] == 4
    rows = payload["results"]
    assert len(rows) == 4 and all(row["status"] == "PASS" for row in rows)

    control = next(row for row in rows if row["label"] == "control")
    assert (control["n"], control["t"], control["q"], control["modulus"]) == (
        32, 2, 97, 1152921504606848701
    )
    assert all(control[key] == value for key, value in CONTROL.items())

    target = sorted(
        (row for row in rows if row["label"] == "target"),
        key=lambda row: row["modulus"],
    )
    assert len(target) == 3
    assert {row["modulus"] for row in target} == TARGET_MODULI
    assert all((row["n"], row["t"], row["q"]) == (64, 4, 193) for row in target)
    assert prime64(193) and (193 - 1) % 64 == 0
    assert all(prime64(row["modulus"]) and (row["modulus"] - 1) % 193 == 0
               for row in target)

    counts: dict[str, int] = {}
    for key in ("z0", "c1", "z1", "z2", "b0", "b1"):
        counts[key], product = crt([(row[key], row["modulus"]) for row in target[:2]])
        assert product.bit_length() == 121
        assert 0 <= counts[key] <= 1 << 64
        assert counts[key] % target[2]["modulus"] == target[2][key]
    assert counts == EXPECTED_COUNTS

    primitive = counts["z0"] - counts["c1"]
    assert primitive >= 0 and primitive % 64 == 0
    first = Fraction(primitive << 64, counts["z1"] * counts["b0"])
    tail = Fraction(counts["z1"] << 64, counts["z2"] * counts["b1"])
    ratio = Fraction(primitive << 128, counts["z2"] * counts["b0"] * counts["b1"])
    assert ratio == first * tail
    fires = ratio.numerator * ratio.numerator > 128 * ratio.denominator * ratio.denominator
    with localcontext() as context:
        context.prec = 80
        def ratio_bits(value: Fraction) -> Decimal:
            if value.numerator == 0:
                return Decimal("-Infinity")
            return (
                Decimal(value.numerator).ln() - Decimal(value.denominator).ln()
            ) / Decimal(2).ln()

        bits = ratio_bits(ratio)
        first_bits = ratio_bits(first)
        tail_bits = ratio_bits(tail)
    return {
        **counts,
        "primitive": primitive,
        "ratio_numerator": ratio.numerator,
        "ratio_denominator": ratio.denominator,
        "ratio_bits": f"{bits:.40E}",
        "first_ratio_bits": f"{first_bits:.40E}",
        "tail_ratio_bits": f"{tail_bits:.40E}",
        "sqrt_slack_bits": f"{Decimal(3.5) - bits:.40E}",
        "fires": fires,
        "max_seconds": max(float(row["seconds"]) for row in rows),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    payload = json.loads((HERE / "results.json").read_text())
    result = build(payload)
    if args.tamper_selftest:
        changed = copy.deepcopy(payload)
        row = next(row for row in changed["results"] if row["label"] == "target")
        row["z0"] = (row["z0"] + 1) % row["modulus"]
        caught = 0
        try:
            assert build(changed) == result
        except AssertionError:
            caught = 1
        assert caught == 1
        print("C2_FIRST_DEPTH2_CRT_TAMPER_PASS mutations=1/1")
        return
    print(
        "C2_FIRST_DEPTH2_CRT_PASS "
        f"fires={int(result['fires'])} ratio_bits={result['ratio_bits']} "
        f"max_seconds={result['max_seconds']:.3f}"
    )


if __name__ == "__main__":
    main()
