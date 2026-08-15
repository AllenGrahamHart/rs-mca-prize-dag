#!/usr/bin/env python3
"""Exact parallel replay of the corank-three projective-basis frontier."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
RESULT = HERE / "rate_half_mca_rank11_kernel_corank3_projective_exact_result.json"

app = modal.App("rate-half-mca-rank11-kernel-corank3-projective-exact")
image = modal.Image.debian_slim()

K_MIN = 568339
K_CLOSED = 796598
K_WALL = 796599
N_OFFSET = 1048576
M_OFFSET = 67472
RESIDUAL = 274980728111260126
M1_PROJECTIVE = 8147918
M2_PROJECTIVE = 84416263
M3_PROJECTIVE = 983902549
TREE = [(2, 4), (2, 5), (3, 6), (4, 7), (5, 8), (6, 9)]


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length))


def ceil_fraction(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def record_cap(kprime: int, d: int) -> int:
    if d == 1:
        return M1_PROJECTIVE
    if d == 2:
        return M2_PROJECTIVE
    if d == 3:
        return M3_PROJECTIVE
    if d == 9:
        return 61871313426630599
    rank = 10 - d
    shortened = kprime - rank
    return int(max(
        Fraction(
            falling(N_OFFSET + shortened, d + 1),
            (M_OFFSET + shortened) * rising(M_OFFSET + 1, d - 1),
        ),
        Fraction(
            falling(N_OFFSET + d, d + 1),
            rising(M_OFFSET + 1, d),
        ),
    ))


def cap_data(kprime: int) -> tuple[list[Fraction], list[str]]:
    nprime, mprime = N_OFFSET + kprime, M_OFFSET + kprime
    caps, branches = [], []
    for d in range(1, 10):
        extension = comb(kprime - 10, d + 1)
        ambient = Fraction(
            comb(nprime, 10 - d) * record_cap(kprime, d) * extension // (d + 2),
            RESIDUAL,
        )
        support = Fraction(comb(mprime, 10 - d) * extension // (d + 2))
        caps.append(min(ambient, support))
        branches.append("ambient" if ambient <= support else "record")
    return caps, branches


def raising(kprime: int, step: int, source: int) -> Fraction:
    return Fraction(
        comb(source + 2, step) * comb(M_OFFSET + source, step),
        comb(kprime - source - 11 + step, step),
    )


def multiplicity(step: int, source: int) -> int:
    return comb(9 - source + step, step)


def primary_certificate(kprime: int):
    caps, branches = cap_data(kprime)
    parent = {source: (step, source) for step, source in TREE}
    children: dict[int, list[tuple[int, int]]] = {d: [] for d in range(1, 10)}
    for step, source in TREE:
        children[source - step].append((step, source))

    factors = [Fraction(0) for _ in range(9)]
    roots = [0 for _ in range(9)]
    for root in (1, 2, 3):
        factors[root - 1] = Fraction(1)
        roots[root - 1] = root
    for source in range(4, 10):
        step, _ = parent[source]
        target = source - step
        factors[source - 1] = (
            multiplicity(step, source)
            * factors[target - 1]
            / raising(kprime, step, source)
        )
        roots[source - 1] = roots[target - 1]
    allocation = [factors[index] * caps[roots[index] - 1] for index in range(9)]

    hierarchy_dual: dict[tuple[int, int], Fraction] = {}
    for source in range(9, 3, -1):
        edge = parent[source]
        child_charge = sum(
            multiplicity(*child) * hierarchy_dual[child]
            for child in children[source]
        )
        hierarchy_dual[edge] = (1 + child_charge) / raising(kprime, *edge)
    cap_dual = {
        root: 1 + sum(
            multiplicity(*child) * hierarchy_dual[child]
            for child in children[root]
        )
        for root in (1, 2, 3)
    }
    optimum = sum(allocation, Fraction(0))
    dual_optimum = sum(cap_dual[root] * caps[root - 1] for root in (1, 2, 3))
    assert optimum == dual_optimum
    return caps, branches, allocation, hierarchy_dual, cap_dual, optimum


def audit_optimum(kprime: int, caps: list[Fraction]) -> Fraction:
    factors = {1: Fraction(1), 2: Fraction(1), 3: Fraction(1)}
    for step, source in TREE:
        factors[source] = Fraction(multiplicity(step, source), raising(kprime, step, source))
    return (
        caps[0]
        + caps[1] * (factors[2] + factors[4])
        + caps[2] * sum(factors[d] for d in (3, 5, 6, 7, 8, 9))
    )


def check_row(kprime: int) -> dict[str, object]:
    caps, branches, allocation, hierarchy_dual, cap_dual, optimum = primary_certificate(kprime)
    assert optimum == audit_optimum(kprime, caps)
    assert branches[:3] == ["ambient", "ambient", "ambient"]
    assert all(0 < value <= cap for value, cap in zip(allocation, caps))
    assert allocation[:3] == caps[:3]
    assert all(allocation[index] < caps[index] for index in range(3, 9))

    mprime = M_OFFSET + kprime
    shadow = [
        Fraction(comb(d + 2, 2), comb(kprime - d - 9, 2))
        for d in range(1, 10)
    ]
    assert sum(shadow[i] * allocation[i] for i in range(9)) < comb(mprime, 9)
    e0 = comb(mprime - 9, 2)
    containment = [
        52 + Fraction(3 * e0, comb(kprime - 10, 2)),
        55 + Fraction(6 * comb(67474, 2), comb(kprime - 11, 2)),
        *[Fraction(55) for _ in range(7)],
    ]
    assert sum(containment[i] * allocation[i] for i in range(9)) < e0 * comb(mprime, 9)

    tight = []
    for step in range(2, 9):
        for source in range(step + 1, 10):
            left = raising(kprime, step, source) * allocation[source - 1]
            right = multiplicity(step, source) * allocation[source - step - 1]
            assert left <= right
            if left == right:
                tight.append([step, source])
    assert len(tight) == 12
    assert all(value > 0 for value in hierarchy_dual.values())
    assert all(value > 0 for value in cap_dual.values())

    demand = Fraction(495405467 * comb(mprime, 11), 10**9)
    assert (demand > optimum) == (kprime <= K_CLOSED)
    integer_demand = ceil_fraction(RESIDUAL * demand)
    scaled_capacity = RESIDUAL * optimum
    integer_capacity = scaled_capacity.numerator // scaled_capacity.denominator
    return {
        "kprime": kprime,
        "optimum_numerator": optimum.numerator,
        "optimum_denominator": optimum.denominator,
        "integer_demand": integer_demand,
        "integer_capacity": integer_capacity,
        "signed_gap": integer_demand - integer_capacity,
        "tight": tight,
    }


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=64)
def check_chunk(bounds: tuple[int, int]) -> dict[str, object]:
    import resource
    import time

    started = time.monotonic()
    start, end = bounds
    endpoint_rows = []
    for kprime in range(start, end):
        row = check_row(kprime)
        if kprime in (K_MIN, K_CLOSED, K_WALL):
            endpoint_rows.append(row)
    return {
        "start": start,
        "end": end,
        "checked": end - start,
        "endpoint_rows": endpoint_rows,
        "seconds": time.monotonic() - started,
        "peak_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024,
    }


def chunks(count: int = 64) -> list[tuple[int, int]]:
    total = K_WALL - K_MIN + 1
    width = (total + count - 1) // count
    return [
        (start, min(K_WALL + 1, start + width))
        for start in range(K_MIN, K_WALL + 1, width)
    ]


@app.local_entrypoint()
def main() -> None:
    bounds = chunks()
    rows = []

    def write(complete: bool, error: str | None = None) -> None:
        endpoints = sorted(
            [endpoint for row in rows for endpoint in row["endpoint_rows"]],
            key=lambda row: row["kprime"],
        )
        payload = {
            "schema": "rate-half-mca-rank11-kernel-corank3-projective-exact-v1",
            "complete": complete,
            "error": error,
            "expected_chunks": len(bounds),
            "completed_chunks": len(rows),
            "checked_rows": sum(row["checked"] for row in rows),
            "interval": [K_MIN, K_CLOSED, K_WALL],
            "record_cap_M1": M1_PROJECTIVE,
            "record_cap_M2": M2_PROJECTIVE,
            "record_cap_M3": M3_PROJECTIVE,
            "tree": [list(edge) for edge in TREE],
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "endpoint_rows": endpoints,
            "worker_seconds": sum(float(row["seconds"]) for row in rows),
            "peak_mb": max([int(row["peak_mb"]) for row in rows], default=0),
            "chunks": sorted(rows, key=lambda row: row["start"]),
        }
        RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

    write(False)
    try:
        for row in check_chunk.map(bounds, return_exceptions=True):
            if isinstance(row, BaseException):
                raise row
            rows.append(row)
            write(False)
    except BaseException as error:
        write(False, f"{type(error).__name__}: {error}")
        raise
    expected = K_WALL - K_MIN + 1
    write(len(rows) == len(bounds) and sum(row["checked"] for row in rows) == expected)
    payload = json.loads(RESULT.read_text())
    print(json.dumps({
        "complete": payload["complete"],
        "checked_rows": payload["checked_rows"],
        "record_cap_M1": payload["record_cap_M1"],
        "record_cap_M2": payload["record_cap_M2"],
        "record_cap_M3": payload["record_cap_M3"],
        "worker_seconds": payload["worker_seconds"],
        "peak_mb": payload["peak_mb"],
        "endpoint_rows": payload["endpoint_rows"],
    }, indent=2, sort_keys=True))
    print(f"RESULT {RESULT}")


if __name__ == "__main__":
    main()
