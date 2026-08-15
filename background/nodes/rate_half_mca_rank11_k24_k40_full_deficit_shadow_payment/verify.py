#!/usr/bin/env python3
"""Verify the exact K'=24..40 full-deficit shadow payment."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from fractions import Fraction
from functools import cache
from math import comb, prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "29303e23b2286b8c6dbd5d496d5ec9dc779f929bf880d20c5c1eb86268e9782a"
INTEGRAL_VERIFY = (
    ROOT
    / "background/nodes/rate_half_mca_weighted_split_pencil_integral_heavy_cap/verify.py"
)
RECORD_FLOOR = 274980728111260126
DEFECT_DEPTHS = {2: 7, 3: 2, 4: 1, 5: 0}
DEFICITS = {c: comb(11 - c, 2) for c in range(2, 10)}


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def load_integral_module():
    spec = importlib.util.spec_from_file_location("integral_heavy_verify", INTEGRAL_VERIFY)
    require(spec is not None and spec.loader is not None, "integral module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


INTEGRAL = load_integral_module()


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length))


def kernel_record_cap(kprime: int, corank: int) -> int:
    if corank == 1:
        return 8147918
    if corank == 9:
        return 61871313426630599
    rank = 10 - corank
    shortened = kprime - rank
    zero = Fraction(
        falling(1048576 + shortened, corank + 1),
        (67472 + shortened) * rising(67473, corank - 1),
    )
    endpoint = Fraction(
        falling(1048576 + corank, corank + 1), rising(67473, corank)
    )
    return int(max(zero, endpoint))


def chart(kprime: int, core: int) -> int:
    n = 1048576 + kprime
    m = 67472 + kprime
    petal = m - core
    total = n - core
    offset = core - 9
    clean = INTEGRAL.exact_clean_cap(petal, total, offset)["cap"]
    heavy_min = petal // 2 + 1
    heavy_count = total // heavy_min
    cross = petal * petal // 4
    balanced = comb(total, 2) * (cross + offset * petal) // cross
    collision = comb(heavy_count, 2) * (
        comb(petal - 1, 2) + offset * petal
    )
    return clean + balanced + collision


def completion_value(m: int, support: int, completions: int) -> int:
    return completions * comb(m - support + 1 - completions, 11 - support)


def defect_cap(q: int, m: int, support: int) -> tuple[int, int]:
    depth = DEFECT_DEPTHS[support]
    ceiling = q - depth - 1
    values = {b: completion_value(m, support, b) for b in range(ceiling + 1)}
    maximizing = max(values, key=values.get)
    deletion = comb(m, support - 1) * values[maximizing] // support
    carriers = [
        comb(q + (defect + 1) * (support - 1), support)
        * comb(m - support, 11 - support)
        for defect in range(1, depth + 1)
    ]
    return max([deletion] + carriers), maximizing


def universal_cap(q: int, m: int, support: int) -> tuple[int, int]:
    values = {b: completion_value(m, support, b) for b in range(q + 1)}
    maximizing = max(values, key=values.get)
    return comb(m, support - 1) * values[maximizing] // support, maximizing


@cache
def row(kprime: int) -> dict[str, object]:
    n = 1048576 + kprime
    m = 67472 + kprime
    q = kprime - 10
    kernel = sum(
        comb(n, 10 - corank)
        * kernel_record_cap(kprime, corank)
        * comb(q, corank + 1)
        for corank in range(1, min(9, q - 1) + 1)
    )
    charts = {str(core): chart(kprime, core) for core in range(9, kprime)}
    max_core = max(charts, key=charts.get)
    uniform_chart = charts[max_core]
    marks = comb(n, 9) * uniform_chart

    structured = {
        c: comb(q + 4, c) * comb(m - c, 11 - c) for c in range(2, 6)
    }
    refined = {c: defect_cap(q, m, c) for c in range(2, 6)}
    universal = {c: universal_cap(q, m, c) for c in range(6, 10)}
    common = sum(DEFICITS[c] * universal[c][0] for c in range(6, 10))
    structured_premium = common + sum(
        DEFICITS[c] * structured[c] for c in range(2, 6)
    )
    refined_premium = common + sum(
        DEFICITS[c] * refined[c][0] for c in range(2, 6)
    )
    premium = max(structured_premium, refined_premium)
    full_rank = (marks + RECORD_FLOOR * premium) // 55
    total = kernel + full_rank
    demand = (990810934 * RECORD_FLOOR * comb(m, 11) + 10**9 - 1) // 10**9
    coefficient = 55 * 990810934 * comb(m, 11) - 10**9 * premium
    raw = RECORD_FLOOR * coefficient - 10**9 * (55 * kernel + marks)
    return {
        "charts": charts,
        "max_core": int(max_core),
        "chart": uniform_chart,
        "kernel": kernel,
        "structured_premium": structured_premium,
        "refined_premium": refined_premium,
        "premium": premium,
        "completion_maximizers": {
            **{str(c): refined[c][1] for c in range(2, 6)},
            **{str(c): universal[c][1] for c in range(6, 10)},
        },
        "marks": marks,
        "full_rank": full_rank,
        "total": total,
        "demand": demand,
        "gap": demand - total,
        "coefficient": coefficient,
        "raw": raw,
    }


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-k24-k40-full-deficit-shadow-payment-v1",
        "schema",
    )
    require(len(data.get("dependencies", [])) == 5, "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p.get("closed_interval") == [24, 40], "interval")
    require(p.get("new_closed_prefix") == [10, 40], "prefix")
    require(p.get("first_method_wall") == 41, "wall row")
    require(p.get("shadow_baseline") == 55, "baseline")
    require(
        p.get("deficit_weights") == {str(c): DEFICITS[c] for c in range(2, 10)},
        "deficits",
    )

    declared_rows = p.get("rows")
    require(isinstance(declared_rows, dict), "rows")
    expected_rows = {k: row(k) for k in range(24, 42)}
    require(set(declared_rows) == {str(k) for k in expected_rows}, "row keys")
    for kprime, expected in expected_rows.items():
        declared = declared_rows[str(kprime)]
        require(declared.get("max_core") == expected["max_core"], f"max core {kprime}")
        require(declared.get("chart") == expected["chart"], f"chart {kprime}")
        require(declared.get("premium") == expected["premium"], f"premium {kprime}")
        require(declared.get("gap") == expected["gap"], f"gap {kprime}")
        require(expected["premium"] == expected["refined_premium"], f"active branch {kprime}")
        require(expected["max_core"] == kprime - 1, f"last core {kprime}")
        if kprime <= 40:
            require(
                expected["gap"] > 0
                and expected["coefficient"] > 0
                and expected["raw"] > 0,
                f"strict row {kprime}",
            )
        else:
            require(expected["gap"] < 0 and expected["raw"] < 0, "wall signs")

    first = expected_rows[24]
    last = expected_rows[40]
    wall = expected_rows[41]
    require(
        p.get("K24_endpoint")
        == {
            "kernel_capacity": first["kernel"],
            "full_rank_capacity": first["full_rank"],
            "total_capacity": first["total"],
            "required_incidence": first["demand"],
        },
        "K24 endpoint",
    )
    require(
        p.get("K40_endpoint")
        == {
            "kernel_capacity": last["kernel"],
            "full_rank_capacity": last["full_rank"],
            "total_capacity": last["total"],
            "required_incidence": last["demand"],
            "record_coefficient_cross": last["coefficient"],
            "floor_record_raw_cross": last["raw"],
        },
        "K40 endpoint",
    )
    require(
        p.get("K41_method_wall")
        == {
            "kernel_capacity": wall["kernel"],
            "full_rank_capacity": wall["full_rank"],
            "total_capacity": wall["total"],
            "required_incidence": wall["demand"],
            "capacity_excess": -wall["gap"],
            "floor_record_raw_cross": wall["raw"],
        },
        "K41 wall",
    )
    require(p.get("remaining_rank9_interval") == [41, 15528], "remaining")
    require("fails at K'=41" in str(data.get("nonclaim")), "nonclaim")
    return {
        "rows": len(expected_rows) - 1,
        "charts": sum(len(expected_rows[k]["charts"]) for k in expected_rows),
        "minimum_gap": min(expected_rows[k]["gap"] for k in range(24, 41)),
        "wall": -wall["gap"],
    }


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item["parameters"].__setitem__("closed_interval", [24, 39]),
        lambda item: item["parameters"].__setitem__("shadow_baseline", 45),
        lambda item: item["parameters"]["deficit_weights"].__setitem__("6", 9),
        lambda item: item["parameters"]["rows"]["24"].__setitem__("max_core", 22),
        lambda item: item["parameters"]["rows"]["30"].__setitem__("chart", 0),
        lambda item: item["parameters"]["rows"]["35"].__setitem__("premium", 0),
        lambda item: item["parameters"]["rows"]["40"].__setitem__("gap", 0),
        lambda item: item["parameters"]["K24_endpoint"].__setitem__("kernel_capacity", 0),
        lambda item: item["parameters"]["K40_endpoint"].__setitem__("floor_record_raw_cross", 0),
        lambda item: item["parameters"]["K41_method_wall"].__setitem__("capacity_excess", 0),
        lambda item: item["parameters"].__setitem__("remaining_rank9_interval", [42, 15528]),
        lambda item: item.__setitem__("nonclaim", "K'=41 closed"),
    )
    rejected = 0
    for mutation in mutations:
        hostile = copy.deepcopy(data)
        mutation(hostile)
        try:
            validate(hostile)
        except (Reject, KeyError, TypeError, ValueError):
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
        "RATE_HALF_MCA_RANK11_K24_K40_FULL_DEFICIT_SHADOW_PAYMENT_PASS "
        f"rows={result['rows']} charts={result['charts']} "
        f"minimum_gap={result['minimum_gap']} wall={result['wall']} "
        f"controls={controls}"
    )


if __name__ == "__main__":
    main()
