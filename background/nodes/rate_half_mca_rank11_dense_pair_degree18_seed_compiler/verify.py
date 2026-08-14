#!/usr/bin/env python3
"""Verify the dense-pair degree-18 seed compiler."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "48c77d234369c35e783a1ad98afe915caef50c071ddd263a2912034bc2de7906"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def multiply(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return out


def evaluate(poly: list[int], x: int, p: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % p
    return value


def validate_toy(toy: object) -> int:
    require(isinstance(toy, dict), "toy")
    p = toy.get("field")
    slopes = toy.get("slopes")
    dense = toy.get("dense_slopes")
    a = toy.get("line_constant")
    b = toy.get("line_direction")
    q = toy.get("degree18_coefficient")
    require((p, slopes, dense, a, b, q) == (257, list(range(32)), 18, 7, 11, 3), "toy constants")
    roots = [1]
    for slope in slopes[:dense]:
        roots = multiply(roots, [(-slope) % p, 1], p)
    require(len(roots) - 1 == dense and roots[-1] == 1, "root polynomial")
    poly = [(q * value) % p for value in roots]
    poly[0] = (poly[0] + a) % p
    poly[1] = (poly[1] + b) % p
    values = [evaluate(poly, slope, p) for slope in slopes]
    require(all(values[z] == (a + b * z) % p for z in slopes[:dense]), "dense line")
    require(values[dense] != (a + b * dense) % p, "off-line record")
    require(len(poly) - 1 == toy.get("expected_degree") == 18, "degree")
    return len(poly) - 1


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-dense-pair-degree18-seed-v1", "schema")
    require(
        data.get("dependencies")
        == [
            "rate_half_mca_rank11_heavy_pair_order32_seed_compiler",
            "rate_half_mca_rank11_order32_common_support_cancellation",
        ],
        "dependencies",
    )
    row = data.get("official")
    require(isinstance(row, dict), "official")
    require(tuple(row.get(k) for k in ("n", "K", "m")) == (2097152, 1048576, 1116048), "row")
    low = row.get("low_record_minimum")
    pairs = row.get("pair_type_maximum")
    owner = (low + pairs - 1) // pairs
    require(owner == row.get("dense_pair_owner_minimum") == 220, "dense owner")
    require(row.get("theta_maximum") == 387, "theta")
    require(row.get("dense_records_selected") == 18, "dense selection")
    require(row.get("seed_size") == 32 and row.get("other_slot_budget") == 14, "seed slots")
    require(
        pairs + row.get("fixed_pair_record_maximum") < low
        and row.get("fixed_pair_record_maximum") == row.get("n") - row.get("m") + 1,
        "distinct heavy basis",
    )

    schedule = data.get("selection_schedule")
    require(isinstance(schedule, list) and len(schedule) == 10, "schedule")
    max_singles = 0
    for t, entry in enumerate(schedule, 1):
        require(isinstance(entry, dict), "schedule entry")
        doubled = min(t, 14 - t)
        singles = t - doubled
        used = 18 + t + doubled
        require(
            entry
            == {
                "basis_pairs": t,
                "doubled_pairs": doubled,
                "single_pairs": singles,
                "used": used,
            },
            f"schedule {t}",
        )
        require(used <= 32, f"slot overflow {t}")
        max_singles = max(max_singles, singles)
    require(max_singles == row.get("singly_represented_pair_maximum") == 6, "single maximum")
    require(row.get("other_basis_pair_maximum") == 10, "basis dimension")

    core = row.get("heavy_core_intersection_maximum")
    selected_core = core + max_singles * row.get("theta_maximum")
    residual = row.get("K") - selected_core
    require(
        (core, selected_core, residual)
        == (
            row.get("K") - 4923,
            row.get("selected_common_support_maximum"),
            row.get("residual_dimension_minimum"),
        )
        == (1043653, 1045975, 2601),
        "core ledger",
    )
    require(
        (row.get("slope_degree_minimum"), row.get("slope_degree_maximum"), row.get("critical_order"))
        == (18, 31, 32),
        "degree interface",
    )
    degree = validate_toy(data.get("toy"))
    require("does not pay" in str(data.get("nonclaim")), "nonclaim")
    return {"owner": owner, "residual": residual, "degree": degree, "singles": max_singles}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["official"].__setitem__("dense_pair_owner_minimum", 219),
        lambda item: item["official"].__setitem__("other_slot_budget", 13),
        lambda item: item["official"].__setitem__("singly_represented_pair_maximum", 5),
        lambda item: item["official"].__setitem__("selected_common_support_maximum", 1045976),
        lambda item: item["official"].__setitem__("slope_degree_minimum", 17),
        lambda item: item["selection_schedule"][9].__setitem__("doubled_pairs", 5),
        lambda item: item["toy"].__setitem__("dense_slopes", 17),
    )
    controls = []
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError, ZeroDivisionError):
            controls.append(True)
        else:
            controls.append(False)
    require(all(controls), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_DENSE_PAIR_DEGREE18_SEED_PASS "
        f"owner={result['owner']} Kmin={result['residual']} "
        f"degree={result['degree']} singles={result['singles']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
