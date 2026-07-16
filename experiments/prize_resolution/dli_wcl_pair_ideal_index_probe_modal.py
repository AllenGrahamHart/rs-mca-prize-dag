#!/usr/bin/env python3
"""Size an exact ideal-index route for the ell-two weight-five router.

This is a route-selection probe.  For fixed normalized roots x and y in
mu_M, it clears the two equations asserting that the router's final
quadratic has both roots in mu_M.  The resulting elements generate an ideal
in Z[zeta_M].  Any characteristic supporting the fixed pair divides the
finite index of that ideal.
"""

from __future__ import annotations

import itertools
import json
import math
import time
from pathlib import Path

import modal


OUTPUT = Path(__file__).with_name("dli_wcl_pair_ideal_index_probe_result.json")
ORDERS = (16, 32, 64, 128)
EXACT_ORDERS = (16, 32, 64, 128)
MAX_REPS_PER_ORDER = 24

app = modal.App("rs-mca-dli-wcl-pair-ideal-index-probe")
image = modal.Image.debian_slim().apt_install("pari-gp").pip_install("python-flint")


def add(left: list[int], right: list[int]) -> list[int]:
    return [a + b for a, b in zip(left, right)]


def sub(left: list[int], right: list[int]) -> list[int]:
    return [a - b for a, b in zip(left, right)]


def scale(value: list[int], scalar: int) -> list[int]:
    return [scalar * coefficient for coefficient in value]


def mul(left: list[int], right: list[int]) -> list[int]:
    """Multiply modulo X^d+1, where d is the common list length."""
    degree = len(left)
    result = [0] * degree
    left_support = [(i, value) for i, value in enumerate(left) if value]
    right_support = [(i, value) for i, value in enumerate(right) if value]
    for i, a in left_support:
        for j, b in right_support:
            exponent = i + j
            if exponent >= degree:
                result[exponent - degree] -= a * b
            else:
                result[exponent] += a * b
    return result


def monomial(order: int, exponent: int) -> list[int]:
    degree = order // 2
    exponent %= order
    result = [0] * degree
    if exponent >= degree:
        result[exponent - degree] = -1
    else:
        result[exponent] = 1
    return result


def router_equations(order: int, pair: tuple[int, int]) -> tuple[list[int], list[int]]:
    """Return cleared B^M=1 and D_M=2 equations in Z[zeta_M]."""
    degree = order // 2
    one = [1] + [0] * (degree - 1)
    x = monomial(order, pair[0])
    y = monomial(order, pair[1])
    u = add(x, y)
    product = mul(x, y)
    v = scale(add(one, u), -1)
    c = mul(u, sub(v, product))

    # E_m = v^m D_m(v,c/v).  The Dickson doubling identity gives
    # E_(2m) = E_m^2 - 2 c^m v^m without introducing denominators.
    power = 1
    c_power = c
    v_power = v
    dickson_cleared = mul(v, v)
    while power < order:
        dickson_cleared = sub(
            mul(dickson_cleared, dickson_cleared),
            scale(mul(c_power, v_power), 2),
        )
        c_power = mul(c_power, c_power)
        v_power = mul(v_power, v_power)
        power *= 2
    return sub(c_power, v_power), sub(dickson_cleared, scale(v_power, 2))


def legal_pairs(order: int) -> list[tuple[int, int]]:
    half = order // 2
    available = [exponent for exponent in range(1, order) if exponent != half]
    return [
        pair
        for pair in itertools.combinations(available, 2)
        if (pair[1] - pair[0]) % order != half
    ]


def pair_orbit_representatives(order: int) -> list[tuple[int, int]]:
    units = range(1, order, 2)
    unseen = set(legal_pairs(order))
    representatives = []
    while unseen:
        representative = min(unseen)
        orbit = {
            tuple(sorted(((unit * representative[0]) % order,
                          (unit * representative[1]) % order)))
            for unit in units
        }
        unseen.difference_update(orbit)
        representatives.append(representative)
    return representatives


def multiplication_matrix(value: list[int]) -> list[list[int]]:
    degree = len(value)
    rows = [[0] * degree for _ in range(degree)]
    for column in range(degree):
        for exponent, coefficient in enumerate(value):
            target = exponent + column
            if target >= degree:
                rows[target - degree][column] -= coefficient
            else:
                rows[target][column] += coefficient
    return rows


@app.function(image=image, cpu=1, memory=8192, timeout=600, max_containers=128)
def ideal_index(payload: tuple[int, tuple[int, int]]) -> dict[str, object]:
    from flint import fmpz_mat

    order, pair = payload
    started = time.monotonic()
    first, second = router_equations(order, pair)
    first_matrix = multiplication_matrix(first)
    second_matrix = multiplication_matrix(second)
    presentation = fmpz_mat([
        left + right for left, right in zip(first_matrix, second_matrix)
    ])
    coefficient_bits = max(
        (abs(value).bit_length() for value in first + second), default=0
    )
    try:
        smith = presentation.snf()
        diagonal = [abs(int(smith[i, i])) for i in range(order // 2)]
        index = math.prod(diagonal)
        status = "COMPLETE" if index else "POSITIVE_RANK"
        error = ""
    except Exception as exc:  # pragma: no cover - route probe diagnostics
        diagonal = []
        index = 0
        status = "ERROR"
        error = repr(exc)
    return {
        "order": order,
        "pair": list(pair),
        "status": status,
        "coefficient_bits": coefficient_bits,
        "index": str(index),
        "index_bits": index.bit_length(),
        "nonunit_invariants": [str(value) for value in diagonal if value > 1],
        "error": error,
        "seconds": round(time.monotonic() - started, 6),
    }


@app.function(image=image, cpu=1, memory=1024, timeout=180, max_containers=48)
def factor_index(index_text: str) -> dict[str, object]:
    import subprocess

    started = time.monotonic()
    program = (
        f"n={index_text};f=factor(n);"
        'for(i=1,matsize(f)[1],print(f[i,1]," : ",f[i,2]));quit()\n'
    )
    completed = subprocess.run(
        ["gp", "-q", "-s", "268435456"],
        input=program,
        text=True,
        capture_output=True,
        timeout=170,
        check=True,
    )
    factors = []
    product = 1
    for line in completed.stdout.splitlines():
        if ":" not in line:
            continue
        prime_text, exponent_text = (part.strip() for part in line.split(":", 1))
        prime = int(prime_text)
        exponent = int(exponent_text)
        quotient = prime - 1
        valuation = 0
        while quotient and quotient % 2 == 0:
            quotient //= 2
            valuation += 1
        factors.append({
            "prime": prime_text,
            "exponent": exponent,
            "v2_prime_minus_1": valuation,
        })
        product *= prime**exponent
    if product != int(index_text):
        raise AssertionError((index_text, product, completed.stdout))
    return {
        "index": index_text,
        "factors": factors,
        "seconds": round(time.monotonic() - started, 6),
    }


@app.local_entrypoint()
def main(factor_only: bool = False) -> None:
    if factor_only:
        result = json.loads(OUTPUT.read_text())
        rows = result["rows"]
        orbit_counts = result["orbit_counts"]
    else:
        orbit_counts = {}
        payloads = []
        for order in ORDERS:
            representatives = pair_orbit_representatives(order)
            orbit_counts[str(order)] = len(representatives)
            if order in EXACT_ORDERS or len(representatives) <= MAX_REPS_PER_ORDER:
                selected = representatives
            else:
                positions = {
                    round(index * (len(representatives) - 1) / (MAX_REPS_PER_ORDER - 1))
                    for index in range(MAX_REPS_PER_ORDER)
                }
                selected = [representatives[index] for index in sorted(positions)]
            payloads.extend((order, pair) for pair in selected)

        remote_rows = list(ideal_index.map(payloads, return_exceptions=True))
        rows = []
        for payload, row in zip(payloads, remote_rows):
            if isinstance(row, BaseException):
                rows.append({
                    "order": payload[0],
                    "pair": list(payload[1]),
                    "status": "REMOTE_ERROR",
                    "error": repr(row),
                })
            else:
                rows.append(row)
        result = {
            "schema": "dli-wcl-pair-ideal-index-probe-v2",
            "scope": "route selection only; sampled pair orbits above the exact small ladder",
            "orders": list(ORDERS),
            "orbit_counts": orbit_counts,
            "rows": rows,
            "status": "COMPLETE"
            if all(row["status"] == "COMPLETE" for row in rows)
            else "PARTIAL",
        }

    distinct_indices = sorted({row["index"] for row in rows if int(row["index"]) > 1})
    remote_factors = list(factor_index.map(distinct_indices, return_exceptions=True))
    factor_rows = []
    for index_text, row in zip(distinct_indices, remote_factors):
        if isinstance(row, BaseException):
            factor_rows.append({"index": index_text, "error": repr(row)})
        else:
            factor_rows.append(row)
    result["factor_rows"] = factor_rows
    result["max_v2_prime_minus_1"] = max(
        (
            factor["v2_prime_minus_1"]
            for row in factor_rows
            for factor in row.get("factors", [])
        ),
        default=0,
    )
    if any("error" in row for row in factor_rows):
        result["status"] = "PARTIAL"
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "DLI_WCL_PAIR_IDEAL_INDEX_PROBE "
        + json.dumps({
            "status": result["status"],
            "orbit_counts": orbit_counts,
            "rows": len(rows),
            "max_seconds": max((row.get("seconds", 0) for row in rows), default=0),
            "max_coefficient_bits": max(
                (row.get("coefficient_bits", 0) for row in rows), default=0
            ),
            "max_index_bits": max((row.get("index_bits", 0) for row in rows), default=0),
            "max_v2_prime_minus_1": result["max_v2_prime_minus_1"],
        }, sort_keys=True)
    )


if __name__ == "__main__":
    main()
