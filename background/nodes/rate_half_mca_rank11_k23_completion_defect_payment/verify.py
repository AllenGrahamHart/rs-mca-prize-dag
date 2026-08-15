#!/usr/bin/env python3
"""Verify the exact K'=23 completion-defect payment."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "37a1bca5a03ec0b007a4ac9901e5e04ecaa40f3d4592a5ef1f080efaa6b1293b"
INTEGRAL_VERIFY = (
    ROOT
    / "background/nodes/rate_half_mca_weighted_split_pencil_integral_heavy_cap/verify.py"
)
RECORD_FLOOR = 274980728111260126
DEPTHS = {2: 7, 3: 2, 4: 1, 5: 0}
WEIGHTS = {2: 26, 3: 18, 4: 11, 5: 5}


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
    h = total // heavy_min
    cross = petal * petal // 4
    balanced = comb(total, 2) * (cross + offset * petal) // cross
    collision = comb(h, 2) * (comb(petal - 1, 2) + offset * petal)
    return clean + balanced + collision


def sparse_caps(q: int, m: int, support: int) -> tuple[int, int]:
    depth = DEPTHS[support]
    ceiling = q - depth - 1
    values = {
        b: b * comb(m - support + 1 - b, 11 - support)
        for b in range(ceiling + 1)
    }
    maximizing = max(values, key=values.get)
    deletion = comb(m, support - 1) * values[maximizing] // support
    carriers = [
        comb(q + (defect + 1) * (support - 1), support)
        * comb(m - support, 11 - support)
        for defect in range(1, depth + 1)
    ]
    return max([deletion] + carriers), maximizing


def row(kprime: int) -> dict[str, object]:
    n = 1048576 + kprime
    m = 67472 + kprime
    q = kprime - 10
    kernel = sum(
        comb(n, 10 - d) * kernel_record_cap(kprime, d) * comb(q, d + 1)
        for d in range(1, min(9, q - 1) + 1)
    )
    charts = {str(core): chart(kprime, core) for core in range(9, kprime)}
    maximizing_core = max(charts, key=charts.get)
    uniform_chart = charts[maximizing_core]
    marks = comb(n, 9) * uniform_chart
    structured = {
        str(c): comb(q + 4, c) * comb(m - c, 11 - c) for c in WEIGHTS
    }
    refined_rows = {c: sparse_caps(q, m, c) for c in WEIGHTS}
    refined = {str(c): refined_rows[c][0] for c in WEIGHTS}
    maximizers = {str(c): refined_rows[c][1] for c in WEIGHTS}
    structured_premium = sum(WEIGHTS[c] * structured[str(c)] for c in WEIGHTS)
    refined_premium = sum(WEIGHTS[c] * refined[str(c)] for c in WEIGHTS)
    premium = max(structured_premium, refined_premium)
    full_rank = (marks + RECORD_FLOOR * premium) // 45
    total = kernel + full_rank
    demand = (990810934 * RECORD_FLOOR * comb(m, 11) + 10**9 - 1) // 10**9
    coefficient = 45 * 990810934 * comb(m, 11) - 10**9 * premium
    raw = RECORD_FLOOR * coefficient - 10**9 * (45 * kernel + marks)
    return {
        "charts": charts,
        "maximizing_core": int(maximizing_core),
        "uniform_chart": uniform_chart,
        "kernel": kernel,
        "marks": marks,
        "structured": structured,
        "refined": refined,
        "maximizers": maximizers,
        "structured_premium": structured_premium,
        "premium": premium,
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
        data.get("schema") == "rate-half-mca-rank11-k23-completion-defect-payment-v1",
        "schema",
    )
    require(len(data.get("dependencies", [])) == 4, "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p.get("K_prime") == 23, "row")
    expected = row(23)
    require(p.get("core_chart_caps") == expected["charts"], "charts")
    require(p.get("maximizing_core") == expected["maximizing_core"], "max core")
    require(p.get("uniform_rank9_chart_cap") == expected["uniform_chart"], "chart")
    require(p.get("kernel_capacity") == expected["kernel"], "kernel")
    require(p.get("global_rank9_mark_capacity") == expected["marks"], "marks")
    require(p.get("structured_sparse_caps") == expected["structured"], "structured")
    require(p.get("refined_sparse_caps") == expected["refined"], "refined")
    require(p.get("completion_maximizers") == expected["maximizers"], "maximizers")
    require(p.get("structured_premium") == expected["structured_premium"], "structured premium")
    require(p.get("active_refined_premium") == expected["premium"], "premium")
    require(p.get("full_rank_capacity") == expected["full_rank"], "full rank")
    require(p.get("total_capacity") == expected["total"], "total")
    require(p.get("required_incidence") == expected["demand"], "demand")
    require(p.get("demand_capacity_gap") == expected["gap"], "gap")
    require(p.get("record_coefficient_cross") == expected["coefficient"], "coefficient")
    require(p.get("floor_record_raw_cross") == expected["raw"], "raw")
    require(expected["gap"] > 0 and expected["coefficient"] > 0 and expected["raw"] > 0, "strict")

    wall = row(24)
    declared_wall = p.get("K24_method_wall")
    require(isinstance(declared_wall, dict), "wall")
    require(declared_wall.get("uniform_rank9_chart_cap") == wall["uniform_chart"], "wall chart")
    require(declared_wall.get("active_refined_premium") == wall["premium"], "wall premium")
    require(declared_wall.get("kernel_capacity") == wall["kernel"], "wall kernel")
    require(declared_wall.get("total_capacity") == wall["total"], "wall total")
    require(declared_wall.get("required_incidence") == wall["demand"], "wall demand")
    require(declared_wall.get("capacity_excess") == -wall["gap"] > 0, "wall excess")
    require(p.get("new_closed_prefix") == [10, 23], "prefix")
    require(p.get("remaining_rank9_interval") == [24, 15528], "remaining")
    require("fails at K'=24" in str(data.get("nonclaim")), "nonclaim")
    return {"gap": int(expected["gap"]), "wall": int(-wall["gap"]), "cores": len(expected["charts"])}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item["parameters"].__setitem__("K_prime", 24),
        lambda item: item["parameters"]["core_chart_caps"].__setitem__("22", 0),
        lambda item: item["parameters"].__setitem__("maximizing_core", 21),
        lambda item: item["parameters"].__setitem__("kernel_capacity", 0),
        lambda item: item["parameters"]["refined_sparse_caps"].__setitem__("2", 0),
        lambda item: item["parameters"]["completion_maximizers"].__setitem__("3", 11),
        lambda item: item["parameters"].__setitem__("active_refined_premium", 0),
        lambda item: item["parameters"].__setitem__("demand_capacity_gap", 0),
        lambda item: item["parameters"].__setitem__("record_coefficient_cross", 0),
        lambda item: item["parameters"]["K24_method_wall"].__setitem__("capacity_excess", 0),
        lambda item: item["parameters"].__setitem__("remaining_rank9_interval", [23, 15528]),
        lambda item: item.__setitem__("nonclaim", "K'=24 closed"),
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
        "RATE_HALF_MCA_RANK11_K23_COMPLETION_DEFECT_PAYMENT_PASS "
        f"cores={result['cores']} gap={result['gap']} wall={result['wall']} "
        f"controls={controls}"
    )


if __name__ == "__main__":
    main()
