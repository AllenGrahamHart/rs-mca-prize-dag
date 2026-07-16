#!/usr/bin/env python3
"""Size the principal-norm gcd certificate for the ell=2, weight-5 router."""

from __future__ import annotations

import itertools
import hashlib
import json
from pathlib import Path

import modal


OUTPUT = Path(__file__).with_name("dli_wcl_pair_norm_gcd_probe_result.json")
FULL_OUTPUT = Path(__file__).with_name(
    "dli_wcl_ell2_weight5_norm_gcd_certificate_result.json"
)
REPLAY_OUTPUT = Path(__file__).with_name(
    "dli_wcl_ell2_weight5_norm_gcd_replay_result.json"
)
SAMPLE_COUNTS = {256: 12, 512: 8, 1024: 4}

app = modal.App("rs-mca-dli-wcl-pair-norm-gcd-probe")
image = modal.Image.debian_slim().pip_install("python-flint")


def add(left: list[int], right: list[int]) -> list[int]:
    return [a + b for a, b in zip(left, right)]


def sub(left: list[int], right: list[int]) -> list[int]:
    return [a - b for a, b in zip(left, right)]


def scale(value: list[int], scalar: int) -> list[int]:
    return [scalar * coefficient for coefficient in value]


def mul(left: list[int], right: list[int]) -> list[int]:
    degree = len(left)
    result = [0] * degree
    left_support = [(index, value) for index, value in enumerate(left) if value]
    right_support = [(index, value) for index, value in enumerate(right) if value]
    for left_index, left_value in left_support:
        for right_index, right_value in right_support:
            exponent = left_index + right_index
            if exponent >= degree:
                result[exponent - degree] -= left_value * right_value
            else:
                result[exponent] += left_value * right_value
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
    degree = order // 2
    one = [1] + [0] * (degree - 1)
    x = monomial(order, pair[0])
    y = monomial(order, pair[1])
    u = add(x, y)
    product = mul(x, y)
    v = scale(add(one, u), -1)
    c_value = mul(u, sub(v, product))

    power = 1
    c_power = c_value
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
    representatives: list[tuple[int, int]] = []
    while unseen:
        representative = min(unseen)
        orbit = {
            tuple(
                sorted(
                    (
                        (unit * representative[0]) % order,
                        (unit * representative[1]) % order,
                    )
                )
            )
            for unit in units
        }
        unseen.difference_update(orbit)
        representatives.append(representative)
    return representatives


def evenly_spaced(values: list[tuple[int, int]], count: int) -> list[tuple[int, int]]:
    if len(values) <= count:
        return values
    positions = {
        round(index * (len(values) - 1) / (count - 1)) for index in range(count)
    }
    return [values[position] for position in sorted(positions)]


def exact_row_digest(rows: list[dict[str, object]]) -> str:
    fields = (
        "order",
        "pair",
        "status",
        "coefficient_bits",
        "first_norm_bits",
        "second_norm_bits",
        "gcd",
        "gcd_bits",
    )
    projection = [{field: row[field] for field in fields} for row in rows]
    encoded = json.dumps(projection, separators=(",", ":"), sort_keys=True).encode()
    return hashlib.sha256(encoded).hexdigest()


@app.function(image=image, cpu=1, memory=2048, timeout=300)
def select_payloads() -> dict[str, object]:
    orbit_counts: dict[str, int] = {}
    payloads: list[tuple[int, tuple[int, int]]] = []
    for order, count in SAMPLE_COUNTS.items():
        representatives = pair_orbit_representatives(order)
        orbit_counts[str(order)] = len(representatives)
        payloads.extend((order, pair) for pair in evenly_spaced(representatives, count))
    return {"orbit_counts": orbit_counts, "payloads": payloads}


@app.function(image=image, cpu=1, memory=2048, timeout=300)
def select_full_payloads() -> dict[str, object]:
    representatives = pair_orbit_representatives(1024)
    return {
        "orbit_counts": {"1024": len(representatives)},
        "payloads": [(1024, pair) for pair in representatives],
    }


@app.function(image=image, cpu=2, memory=8192, timeout=600, max_containers=128)
def norm_gcd(payload: tuple[int, tuple[int, int]]) -> dict[str, object]:
    import math
    import time

    from flint import fmpz_poly

    order, pair = payload
    started = time.monotonic()
    first, second = router_equations(order, pair)
    degree = order // 2
    cyclotomic = fmpz_poly([1] + [0] * (degree - 1) + [1])
    first_norm = abs(int(cyclotomic.resultant(fmpz_poly(first))))
    first_seconds = time.monotonic() - started
    second_norm = abs(int(cyclotomic.resultant(fmpz_poly(second))))
    second_seconds = time.monotonic() - started - first_seconds
    common = math.gcd(first_norm, second_norm)
    return {
        "order": order,
        "pair": list(pair),
        "status": "COMPLETE",
        "coefficient_bits": max(
            (abs(value).bit_length() for value in first + second), default=0
        ),
        "first_norm_bits": first_norm.bit_length(),
        "second_norm_bits": second_norm.bit_length(),
        "gcd": str(common),
        "gcd_bits": common.bit_length(),
        "first_seconds": round(first_seconds, 6),
        "second_seconds": round(second_seconds, 6),
        "seconds": round(time.monotonic() - started, 6),
    }


@app.function(
    image=modal.Image.debian_slim().apt_install("pari-gp"),
    cpu=2,
    memory=4096,
    timeout=600,
    max_containers=128,
)
def factor_gcd(value_text: str) -> dict[str, object]:
    import subprocess
    import time

    started = time.monotonic()
    program = (
        f"n={value_text};f=factor(n);"
        'for(i=1,matsize(f)[1],print(f[i,1]," : ",f[i,2]));quit()\n'
    )
    try:
        completed = subprocess.run(
            ["gp", "-q", "-s", "1073741824"],
            input=program,
            text=True,
            capture_output=True,
            timeout=580,
            check=True,
        )
    except subprocess.TimeoutExpired as exc:
        return {
            "gcd": value_text,
            "status": "TIMEOUT",
            "seconds": round(time.monotonic() - started, 6),
            "stdout": exc.stdout or "",
            "stderr": exc.stderr or "",
        }
    factors: list[dict[str, object]] = []
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
        factors.append(
            {
                "prime": prime_text,
                "prime_bits": prime.bit_length(),
                "exponent": exponent,
                "v2_prime_minus_1": valuation,
            }
        )
        product *= prime**exponent
    if product != int(value_text):
        raise AssertionError((value_text, product, completed.stdout))
    return {
        "gcd": value_text,
        "status": "COMPLETE",
        "factors": factors,
        "seconds": round(time.monotonic() - started, 6),
    }


@app.local_entrypoint()
def main(
    factor_only: bool = False,
    full: bool = False,
    verify_only: bool = False,
) -> None:
    output = FULL_OUTPUT if full else OUTPUT
    if verify_only and not full:
        raise ValueError("--verify-only requires --full")
    if factor_only:
        result = json.loads(output.read_text())
        distinct = sorted(
            {str(row["gcd"]) for row in result["rows"] if int(row["gcd"]) > 1},
            key=int,
        )
        remote_factors = list(factor_gcd.map(distinct, return_exceptions=True))
        factor_rows: list[dict[str, object]] = []
        for value_text, row in zip(distinct, remote_factors):
            if isinstance(row, BaseException):
                factor_rows.append(
                    {"gcd": value_text, "status": "REMOTE_ERROR", "error": repr(row)}
                )
            else:
                factor_rows.append(row)
        result["factor_rows"] = factor_rows
        result["factor_status"] = (
            "COMPLETE"
            if all(row["status"] == "COMPLETE" for row in factor_rows)
            else "PARTIAL"
        )
        complete = [row for row in factor_rows if row["status"] == "COMPLETE"]
        result["eligible_factors"] = [
            factor
            for row in complete
            for factor in row["factors"]
            if int(factor["prime_bits"]) < 257
            and int(factor["v2_prime_minus_1"]) >= 41
        ]
        output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        print(
            "DLI_WCL_PAIR_NORM_GCD_FACTOR "
            + json.dumps(
                {
                    "status": result["factor_status"],
                    "complete": len(complete),
                    "rows": len(factor_rows),
                    "max_seconds": max(
                        (float(row["seconds"]) for row in complete), default=0
                    ),
                    "eligible_factors": len(result["eligible_factors"]),
                },
                sort_keys=True,
            )
        )
        return

    selection = select_full_payloads.remote() if full else select_payloads.remote()
    orbit_counts = selection["orbit_counts"]
    payloads = selection["payloads"]

    remote_rows = list(norm_gcd.map(payloads, return_exceptions=True))
    rows: list[dict[str, object]] = []
    for payload, row in zip(payloads, remote_rows):
        if isinstance(row, BaseException):
            rows.append(
                {
                    "order": payload[0],
                    "pair": list(payload[1]),
                    "status": "REMOTE_ERROR",
                    "error": repr(row),
                }
            )
        else:
            rows.append(row)

    if verify_only:
        expected = json.loads(FULL_OUTPUT.read_text())
        complete = all(row["status"] == "COMPLETE" for row in rows)
        expected_digest = exact_row_digest(expected["rows"])
        actual_digest = exact_row_digest(rows) if complete else ""
        replay = {
            "schema": "dli-wcl-ell2-weight5-norm-gcd-replay-v1",
            "status": (
                "COMPLETE"
                if complete and actual_digest == expected_digest
                else "MISMATCH"
            ),
            "orbit_counts": orbit_counts,
            "rows": len(rows),
            "expected_digest": expected_digest,
            "actual_digest": actual_digest,
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        }
        REPLAY_OUTPUT.write_text(json.dumps(replay, indent=2, sort_keys=True) + "\n")
        print("DLI_WCL_PAIR_NORM_GCD_REPLAY " + json.dumps(replay, sort_keys=True))
        return

    result = {
        "schema": "dli-wcl-pair-norm-gcd-probe-v1",
        "scope": (
            "complete M=1024 odd-dilation orbit certificate"
            if full
            else "route sizing only; deterministic orbit samples"
        ),
        "orbit_counts": orbit_counts,
        "rows": rows,
        "status": "COMPLETE"
        if all(row["status"] == "COMPLETE" for row in rows)
        else "PARTIAL",
    }
    if not full:
        result["sample_counts"] = SAMPLE_COUNTS
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    complete = [row for row in rows if row["status"] == "COMPLETE"]
    print(
        "DLI_WCL_PAIR_NORM_GCD_PROBE "
        + json.dumps(
            {
                "status": result["status"],
                "orbit_counts": orbit_counts,
                "complete": len(complete),
                "rows": len(rows),
                "max_seconds": max(
                    (float(row["seconds"]) for row in complete), default=0
                ),
                "max_gcd_bits": max(
                    (int(row["gcd_bits"]) for row in complete), default=0
                ),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
