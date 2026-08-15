#!/usr/bin/env python3
"""Verify the integral heavy-owner split-pencil cap."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "e701eafd9f64560bbbe67023ff62009028e8ae11e0426f8becb88976cb26878f"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def exact_clean_cap(petal_mass: int, total: int, offset: int) -> dict[str, int]:
    a = petal_mass // 2 + 1
    b = petal_mass - 1
    width = b - a
    c0 = comb(petal_mass, 2) + offset * petal_mass

    def phi(weight: int) -> Fraction:
        return Fraction(c0, petal_mass - weight) - weight

    def value(light: int, count: int, full: int) -> Fraction:
        if full == count:
            return light * count * phi(b)
        minimum = count - full - 1
        residual = total - light - full * b - minimum * a
        require(a <= residual <= b, "residual weight")
        return light * (full * phi(b) + minimum * phi(a) + phi(residual))

    def derivative(light: int, count: int, full: int) -> Fraction:
        minimum = count - full - 1
        delta = petal_mass - total + full * b + minimum * a
        constant = full * phi(b) + minimum * phi(a)
        linear = constant + delta - petal_mass
        denominator = light + delta
        return 2 * light + linear + Fraction(c0 * delta, denominator * denominator)

    candidates: list[tuple[Fraction, int, int, int]] = []
    segment_count = 0
    for count in range(1, total // a + 1):
        if total - count * b >= 0:
            high = total - count * b
            candidates.append((value(0, count, count), 0, count, count))
            candidates.append((value(high, count, count), high, count, count))
            segment_count += 1

        for full in range(count):
            low = max(0, total - count * a - (full + 1) * width + 1)
            high = min(total - count * a, total - count * a - full * width)
            if low > high:
                continue
            segment_count += 1
            points = {low, high}
            minimum = count - full - 1
            delta = petal_mass - total + full * b + minimum * a

            if delta > 0:
                if (low + delta) ** 3 >= c0 * delta:
                    split = low
                elif (high + delta) ** 3 < c0 * delta:
                    split = high + 1
                else:
                    left, right = low, high
                    while left < right:
                        middle = (left + right) // 2
                        if (middle + delta) ** 3 >= c0 * delta:
                            right = middle
                        else:
                            left = middle + 1
                    split = left

                concave_high = min(high, split - 1)
                if low <= concave_high:
                    d_low = derivative(low, count, full)
                    d_high = derivative(concave_high, count, full)
                    if d_low > 0 and d_high < 0:
                        left, right = low, concave_high
                        while left < right:
                            middle = (left + right) // 2
                            if derivative(middle, count, full) <= 0:
                                right = middle
                            else:
                                left = middle + 1
                        points.update(
                            range(max(low, left - 2), min(high, left + 2) + 1)
                        )
                points.update(
                    range(max(low, split - 2), min(high, split + 2) + 1)
                )

            for light in points:
                candidates.append((value(light, count, full), light, count, full))

    best, light, count, full = max(candidates)
    return {
        "cap": best.numerator // best.denominator,
        "light": light,
        "count": count,
        "full": full,
        "segments": segment_count,
        "candidates": len(candidates),
    }


def chart(core: int) -> dict[str, int]:
    petal_mass = 67494 - core
    total = 1048598 - core
    offset = core - 9
    clean = exact_clean_cap(petal_mass, total, offset)
    heavy_min = petal_mass // 2 + 1
    heavy_count = total // heavy_min
    cross_floor = petal_mass * petal_mass // 4
    balanced = (
        comb(total, 2) * (cross_floor + offset * petal_mass) // cross_floor
    )
    collision = comb(heavy_count, 2) * (
        comb(petal_mass - 1, 2) + offset * petal_mass
    )
    return {
        **clean,
        "chart": clean["cap"] + balanced + collision,
        "balanced": balanced,
        "collision": collision,
    }


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-weighted-split-pencil-integral-heavy-cap-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == ["rate_half_mca_weighted_split_pencil_core_offset_cap"],
        "dependencies",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p.get("K_prime") == 22, "row")
    require(p.get("core_interval") == [9, 21], "core interval")

    rows = {str(core): chart(core) for core in range(9, 22)}
    require(
        p.get("clean_caps") == {key: value["cap"] for key, value in rows.items()},
        "clean caps",
    )
    require(
        p.get("chart_caps") == {key: value["chart"] for key, value in rows.items()},
        "chart caps",
    )
    require(
        p.get("light_mass_maximizers")
        == {key: value["light"] for key, value in rows.items()},
        "light maximizers",
    )
    require(all(value["count"] == value["full"] == 8 for value in rows.values()), "owners")
    require(all(value["segments"] == 271 for value in rows.values()), "segments")
    uniform = max(value["chart"] for value in rows.values())
    maximum_core = max(rows, key=lambda key: rows[key]["chart"])
    require(p.get("uniform_chart_cap") == uniform, "uniform cap")
    require(p.get("maximizing_core") == int(maximum_core), "max core")
    require(p.get("chart_saving") == p.get("old_uniform_chart_cap") - uniform, "saving")
    require("does not pay K'=22" in str(data.get("nonclaim")), "nonclaim")
    return {
        "cores": len(rows),
        "segments": sum(value["segments"] for value in rows.values()),
        "candidates": sum(value["candidates"] for value in rows.values()),
        "uniform": uniform,
    }


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item["parameters"].__setitem__("core_interval", [9, 20]),
        lambda item: item["parameters"]["clean_caps"].__setitem__("21", 0),
        lambda item: item["parameters"]["chart_caps"].__setitem__("9", 0),
        lambda item: item["parameters"]["light_mass_maximizers"].__setitem__("15", 0),
        lambda item: item["parameters"].__setitem__("uniform_chart_cap", 0),
        lambda item: item["parameters"].__setitem__("maximizing_core", 9),
        lambda item: item["parameters"].__setitem__("chart_saving", 0),
        lambda item: item.__setitem__("nonclaim", "K'=22 is paid"),
    )
    rejected = 0
    for mutation in mutations:
        hostile = copy.deepcopy(data)
        mutation(hostile)
        try:
            validate(hostile)
        except (Reject, KeyError, TypeError):
            rejected += 1
    require(rejected == len(mutations), "tamper controls")
    return rejected


def main() -> None:
    raw = CONTRACT.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(raw)
    result = validate(data)
    controls = tamper_selftest(data)
    print(
        "RATE_HALF_MCA_WEIGHTED_SPLIT_PENCIL_INTEGRAL_HEAVY_CAP_PASS "
        f"cores={result['cores']} segments={result['segments']} "
        f"candidates={result['candidates']} uniform={result['uniform']} "
        f"controls={controls}"
    )


if __name__ == "__main__":
    main()
