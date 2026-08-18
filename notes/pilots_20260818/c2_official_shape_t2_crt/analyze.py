#!/usr/bin/env python3
"""Fail-closed exact reconstruction for the official-shape t=2 pilot."""

from __future__ import annotations

import argparse
import copy
from decimal import Decimal, localcontext
from fractions import Fraction
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
TARGET_MODULI = {
    1152921504607075139,
    1152921504607136587,
    1152921504607459189,
    1152921504607597447,
    1152921504608457719,
    1152921504609241181,
    1152921504609333353,
    1152921504609486973,
    1152921504609978557,
    1152921504610301159,
}
CONTROL = {
    "control97": {
        "n": 32, "q": 97, "modulus": 1152921504606848701,
        "z0": 455744, "c1": 736, "z1": 44299296, "b0": 44278048,
    },
    "control5857": {
        "n": 32, "q": 5857, "modulus": 1152921504607016701,
        "z0": 1152, "c1": 256, "z1": 1829376, "b0": 787968,
    },
}
EXPECTED_COUNTS = {
    "z0": 227259606172895223931871329798529915863745504182648446230418158474213352436773778191377030361659036987692327140796443375499119317625629124310720768,
    "c1": 15075132044957192478006898191470890229562554962327895331266773111833021696,
    "z1": 1745581035014008215020703684182508283749429217626922715495841875240432760066859390287966970207903063102464764768452812247622422348576523251005605760256,
    "b0": 1745581035014008215020703684182508283749429217626922715495841875240432760066859390287966970207903063102464764768452812244988137327424369450113941136384,
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


def crt(residues: list[tuple[int, int]]) -> tuple[int, int]:
    value, product = 0, 1
    for residue, modulus in residues:
        step = (residue - value) * pow(product, -1, modulus) % modulus
        value += product * step
        product *= modulus
    return value, product


def build(payload: dict[str, object] | None = None) -> dict[str, object]:
    if payload is None:
        payload = json.loads((HERE / "results.json").read_text())
    assert payload["schema"] == "c2-official-shape-t2-crt-v1"
    assert payload["tasks_requested"] == payload["tasks_returned"] == 12
    rows = payload["results"]
    assert len(rows) == 12
    assert all(row["status"] == "PASS" for row in rows)

    for label, expected in CONTROL.items():
        row = next(row for row in rows if row["label"] == label)
        for key, value in expected.items():
            assert row[key] == value
        assert row["orbits"] > 0

    target = sorted(
        (row for row in rows if row["label"] == "target"),
        key=lambda row: row["modulus"],
    )
    assert len(target) == 10
    assert {row["modulus"] for row in target} == TARGET_MODULI
    assert all(row["n"] == 512 and row["q"] == 7681 for row in target)
    assert prime64(7681) and (7681 - 1) % 512 == 0
    assert all(row["orbits"] == 115246 for row in target)
    assert all(prime64(row["modulus"]) and (row["modulus"] - 1) % 7681 == 0
               for row in target)

    counts: dict[str, int] = {}
    for key in ("z0", "c1", "z1", "b0"):
        counts[key], crt_product = crt(
            [(row[key], row["modulus"]) for row in target[:9]]
        )
        assert crt_product.bit_length() == 541
        assert counts[key] % target[9]["modulus"] == target[9][key]
    assert counts == EXPECTED_COUNTS
    assert 0 <= counts["z0"] <= 1 << 512
    assert 0 <= counts["c1"] <= 1 << 256
    assert 0 < counts["z1"] <= 1 << 512
    assert 0 < counts["b0"] <= 1 << 512

    primitive = counts["z0"] - counts["c1"]
    assert primitive >= 0 and primitive % 512 == 0
    ratio = Fraction(primitive << 512, counts["z1"] * counts["b0"])
    fires = ratio.numerator * ratio.numerator > 1024 * ratio.denominator * ratio.denominator
    with localcontext() as context:
        context.prec = 100
        ratio_bits = (
            Decimal(ratio.numerator).ln() - Decimal(ratio.denominator).ln()
        ) / Decimal(2).ln()
    summary = {
        **counts,
        "primitive": primitive,
        "ratio_numerator": ratio.numerator,
        "ratio_denominator": ratio.denominator,
        "ratio_bits": f"{ratio_bits:.40E}",
        "sqrt_slack_bits": f"{Decimal(5) - ratio_bits:.40E}",
        "fires": fires,
        "max_seconds": max(float(row["seconds"]) for row in rows),
    }
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    payload = json.loads((HERE / "results.json").read_text())
    result = build(payload)
    if args.tamper_selftest:
        changed = copy.deepcopy(payload)
        target = next(row for row in changed["results"] if row["label"] == "target")
        target["z0"] = (target["z0"] + 1) % target["modulus"]
        caught = 0
        try:
            assert build(changed) == result
        except AssertionError:
            caught = 1
        assert caught == 1
        print("C2_OFFICIAL_SHAPE_T2_CRT_TAMPER_PASS mutations=1/1")
        return
    print(
        "C2_OFFICIAL_SHAPE_T2_CRT_PASS "
        f"fires={int(result['fires'])} ratio_bits={result['ratio_bits']} "
        f"max_seconds={result['max_seconds']:.3f}"
    )


if __name__ == "__main__":
    main()
