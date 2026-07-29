#!/usr/bin/env python3
"""Validate a remote h=7 low-degree aggregate norm certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
LAUNCHER = HERE / "l1_m8_h7_low_degree_norm_endpoints_modal.py"
EXPECTED_LAUNCHER_SHA256 = "502c0922832a5aba3e4700d89369f901a8292d72eeb43d1bf2a23258c1ead8b3"
APP_NAME = "l1-m8-h7-low-degree-norm-endpoints"
PRIMES = (8191, 131071, 524287, 2147483647)
EXPECTED_DEGREES = {
    "q2_pair_degree8": 8,
    "q2_all_degree14": 14,
    "c222_x0_p5": 5,
    "c222_q6x2_r12": 12,
}


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[int], right: list[int], factor: int = 1) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += factor * value
    return trim(out)


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def scale(poly: list[int], value: int) -> list[int]:
    return trim([value * coefficient for coefficient in poly])


def endpoint_polynomials() -> dict[str, list[int]]:
    q2_pair = [4860, -44172, 8199, -15516, 2862, 672, -180, 10, 5]
    a0 = [720, 0, 0, 15]
    b0 = [-2160, 0, 760, 550, 130]
    c0 = [2160, 2556, 2844, 1956, 744, 120]
    a1 = [0, 0, 35]
    b1 = [0, 378, 378, 154]
    c1 = [360, 720, 840, 480, 120]
    ac = add(multiply(a0, c1), multiply(c0, a1), factor=-1)
    ab = add(multiply(a0, b1), multiply(b0, a1), factor=-1)
    bc = add(multiply(b0, c1), multiply(c0, b1), factor=-1)
    q2_all = add(multiply(ac, ac), multiply(ab, bc), factor=-1)

    p5 = [360, 1218, 1659, 1147, 407, 60]
    a = [27, 27, 11]
    b = [3, 6, 7, 4, 1]
    s = [9, 9, 2]
    u = [2, 2, 1]
    t = [63, 63, 19]
    d_plus_2_squared = [4, 4, 1]
    e = add(scale(multiply(s, s), 14), scale(b, 75), factor=-1)
    f = add(
        scale(multiply(b, t), 5),
        scale(multiply(d_plus_2_squared, multiply(u, u)), 126),
        factor=-1,
    )
    r12 = add(
        add(scale(multiply(f, f), 105), scale(multiply(multiply(a, f), e), 7)),
        scale(multiply(b, multiply(e, e)), 10),
    )
    return {
        "q2_pair_degree8": q2_pair,
        "q2_all_degree14": q2_all,
        "c222_x0_p5": p5,
        "c222_q6x2_r12": r12,
    }


def input_digest() -> str:
    payload = {
        "primes": PRIMES,
        "polynomials": endpoint_polynomials(),
        "exponent": "8*(p+1)",
    }
    encoded = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode()
    return hashlib.sha256(encoded).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()

    launcher_hash = hashlib.sha256(LAUNCHER.read_bytes()).hexdigest()
    assert launcher_hash == EXPECTED_LAUNCHER_SHA256
    result = json.loads(args.certificate.read_text())
    assert result["app"] == APP_NAME
    assert result["launcher_sha256"] == EXPECTED_LAUNCHER_SHA256
    assert result["digest"] == input_digest()
    assert result["status"] == "COMPLETE"

    rows = result["rows"]
    assert len(rows) == 16
    expected = {(endpoint, prime) for endpoint in EXPECTED_DEGREES for prime in PRIMES}
    actual = {(row["endpoint"], row["p"]) for row in rows}
    assert actual == expected and len(actual) == len(rows)
    for row in rows:
        assert row["exponent"] == 8 * (row["p"] + 1)
        assert row["gcd_degree"] == 0
        assert row["gcd_coefficients_low_to_high"] == [1]
        assert row["status"] == "UNIT"
        assert row["seconds"] >= 0
    assert result["all_unit"] is True
    print(
        "L1_M8_H7_LOW_DEGREE_NORM_CERTIFICATE_PASS "
        f"rows={len(rows)} digest={result['digest']}"
    )


if __name__ == "__main__":
    main()
