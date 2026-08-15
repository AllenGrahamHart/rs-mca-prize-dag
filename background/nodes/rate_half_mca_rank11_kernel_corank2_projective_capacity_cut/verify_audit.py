#!/usr/bin/env python3
"""Independent direct-path audit of the corank-two capacity cut."""

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


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length))


def record_cap(kprime: int, d: int, p: dict[str, object]) -> int:
    if d == 1:
        return int(p["projective_corank1_record_cap"])
    if d == 2:
        n, m = 1048578, 67474
        return n * (n - 1) * (n - 2) // (3 * (m - 1) * (m - 2))
    if d == 9:
        return int(p["rank9_record_cap"])
    rank = 10 - d
    shortened = kprime - rank
    return int(max(
        Fraction(
            falling(int(p["n_offset"]) + shortened, d + 1),
            (int(p["m_offset"]) + shortened) * rising(int(p["m_offset"]) + 1, d - 1),
        ),
        Fraction(
            falling(int(p["n_offset"]) + d, d + 1),
            rising(int(p["m_offset"]) + 1, d),
        ),
    ))


def caps(kprime: int, p: dict[str, object]) -> list[Fraction]:
    nprime = int(p["n_offset"]) + kprime
    mprime = int(p["m_offset"]) + kprime
    result = []
    for d in range(1, 10):
        extension = comb(kprime - 10, d + 1)
        ambient = Fraction(
            comb(nprime, 10 - d) * record_cap(kprime, d, p) * extension // (d + 2),
            int(p["residual_record_floor"]),
        )
        support = Fraction(comb(mprime, 10 - d) * extension // (d + 2))
        result.append(min(ambient, support))
    return result


def factor(kprime: int, step: int, source: int, p: dict[str, object]) -> Fraction:
    multiplicity = comb(9 - source + step, step)
    raising = Fraction(
        comb(source + 2, step) * comb(int(p["m_offset"]) + source, step),
        comb(kprime - source - 11 + step, step),
    )
    return Fraction(multiplicity, raising)


def direct_optimum(kprime: int, p: dict[str, object]) -> Fraction:
    cap = caps(kprime, p)
    f3 = factor(kprime, 2, 3, p)
    f4 = factor(kprime, 2, 4, p)
    f5 = factor(kprime, 3, 5, p)
    f6 = f4 * factor(kprime, 2, 6, p)
    f7 = f5 * factor(kprime, 2, 7, p)
    f8 = f6 * factor(kprime, 2, 8, p)
    f9 = f7 * factor(kprime, 2, 9, p)
    return cap[0] * (1 + f3) + cap[1] * (1 + f4 + f5 + f6 + f7 + f8 + f9)


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p, evidence = data["parameters"], data["evidence"]
    require(record_cap(377674, 2, p) == p["projective_corank2_record_cap"], "M2 reconstruction")
    rows = (
        (p["replay_minimum"], "replay_start", 1),
        (p["closed_dimension_maximum"], "endpoint", 1),
        (p["first_open_dimension"], "wall", -1),
    )
    for kprime, prefix, sign in rows:
        optimum = direct_optimum(int(kprime), p)
        require(optimum.numerator == p[f"{prefix}_optimum_numerator"], f"{prefix} numerator")
        require(optimum.denominator == p[f"{prefix}_optimum_denominator"], f"{prefix} denominator")
        demand = int(p[f"{prefix}_demand_ceiling"])
        capacity = int(p[f"{prefix}_capacity"])
        require((demand - capacity) * sign > 0, f"{prefix} sign")

    result_path = ROOT / evidence["result"]
    require(hashlib.sha256(result_path.read_bytes()).hexdigest() == evidence["result_sha256"], "result hash")
    result = json.loads(result_path.read_text())
    require(result["complete"] is True, "completion")
    require(result["checked_rows"] == p["checked_rows_including_wall"], "row count")
    cursor = int(p["replay_minimum"])
    checked = 0
    for chunk in sorted(result["chunks"], key=lambda item: item["start"]):
        require(chunk["start"] == cursor, "chunk continuity")
        require(chunk["checked"] == chunk["end"] - chunk["start"], "chunk size")
        cursor = chunk["end"]
        checked += chunk["checked"]
    require(cursor == int(p["first_open_dimension"]) + 1, "coverage end")
    require(checked == p["checked_rows_including_wall"], "coverage count")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_CORANK2_PROJECTIVE_CAPACITY_CUT_AUDIT_PASS "
        f"checked={checked} endpoints={len(rows)} chunks={len(result['chunks'])}"
    )


if __name__ == "__main__":
    main()
