#!/usr/bin/env python3
"""Independent direct-path audit of the projective-pair capacity cut."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
ROOT = Path(__file__).resolve().parents[3]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def fall(value: int, length: int) -> int:
    return prod(value - offset for offset in range(length))


def rise(value: int, length: int) -> int:
    return prod(value + offset for offset in range(length))


def local_record_cap(p: dict[str, int], kprime: int, d: int) -> int:
    if d == 1:
        return p["projective_corank1_record_cap"]
    if d == 9:
        return p["rank9_record_cap"]
    rank = 10 - d
    shortened = kprime - rank
    return int(max(
        Fraction(fall(p["n_offset"] + shortened, d + 1), (p["m_offset"] + shortened) * rise(p["m_offset"] + 1, d - 1)),
        Fraction(fall(p["n_offset"] + d, d + 1), rise(p["m_offset"] + 1, d)),
    ))


def caps(p: dict[str, int], kprime: int) -> list[Fraction]:
    values = []
    for d in range(1, 10):
        extension = comb(kprime - 10, d + 1)
        ambient = Fraction(
            comb(p["n_offset"] + kprime, 10 - d) * local_record_cap(p, kprime, d) * extension // (d + 2),
            p["residual_record_floor"],
        )
        support = Fraction(comb(p["m_offset"] + kprime, 10 - d) * extension // (d + 2))
        values.append(min(ambient, support))
    return values


def edge_ratio(p: dict[str, int], kprime: int, step: int, source: int) -> Fraction:
    raising = Fraction(
        comb(source + 2, step) * comb(p["m_offset"] + source, step),
        comb(kprime - source - 11 + step, step),
    )
    return Fraction(comb(9 - source + step, step), 1) / raising


def direct_optimum(p: dict[str, int], kprime: int) -> Fraction:
    cap = caps(p, kprime)
    factor = {1: Fraction(1), 2: Fraction(1)}
    factor[3] = edge_ratio(p, kprime, 2, 3)
    factor[4] = edge_ratio(p, kprime, 3, 4)
    factor[5] = factor[3] * edge_ratio(p, kprime, 2, 5)
    factor[6] = factor[4] * edge_ratio(p, kprime, 2, 6)
    factor[7] = factor[5] * edge_ratio(p, kprime, 2, 7)
    factor[8] = factor[6] * edge_ratio(p, kprime, 2, 8)
    factor[9] = factor[7] * edge_ratio(p, kprime, 2, 9)
    return cap[1] + cap[0] * sum(factor[d] for d in (1, 3, 4, 5, 6, 7, 8, 9))


def demand(p: dict[str, int], kprime: int) -> Fraction:
    return Fraction(
        p["lane_density_numerator"] * comb(p["m_offset"] + kprime, 11),
        p["lane_density_denominator"],
    )


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p, evidence = data["parameters"], data["evidence"]
    row_specs = (
        ("replay_start", p["replay_minimum"], True),
        ("endpoint", p["closed_dimension_maximum"], True),
        ("wall", p["first_open_dimension"], False),
    )
    for prefix, kprime, closed in row_specs:
        optimum = direct_optimum(p, kprime)
        require(optimum == Fraction(p[f"{prefix}_optimum_numerator"], p[f"{prefix}_optimum_denominator"]), f"{prefix} optimum")
        require((demand(p, kprime) > optimum) is closed, f"{prefix} sign")
        scaled = p["residual_record_floor"] * optimum
        require(scaled.numerator // scaled.denominator == p[f"{prefix}_capacity"], f"{prefix} capacity")

    script = ROOT / evidence["script"]
    result_path = ROOT / evidence["result"]
    require(hashlib.sha256(script.read_bytes()).hexdigest() == evidence["script_sha256"], "script custody")
    require(hashlib.sha256(result_path.read_bytes()).hexdigest() == evidence["result_sha256"], "result custody")
    result = json.loads(result_path.read_text())
    require(result["complete"] and result["completed_chunks"] == result["expected_chunks"] == evidence["expected_chunks"], "complete chunks")
    require(result["checked_rows"] == p["checked_rows_including_wall"], "checked rows")
    require(sum(chunk["checked"] for chunk in result["chunks"]) == p["checked_rows_including_wall"], "ledger total")
    require(max(chunk["seconds"] for chunk in result["chunks"]) < evidence["worker_timeout_seconds"], "worker timeout")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_PROJECTIVE_PAIR_CAPACITY_CUT_AUDIT_PASS "
        f"checked={result['checked_rows']} endpoints={len(row_specs)} chunks={result['completed_chunks']}"
    )


if __name__ == "__main__":
    main()
