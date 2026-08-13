#!/usr/bin/env python3
"""Verify the imported deployed pole-line typed witness certificate."""

from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "9423f8ab7c0444205ba7eb9a78fdf16a818d58d1dc0e17c6a81c74a78eb2edc4"


class Reject(ValueError):
    pass


def integer(value: object) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise Reject("integer field")
    return value


def trim(poly: list[int], p: int) -> list[int]:
    out = [value % p for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def subtract(left: list[int], right: list[int], p: int) -> list[int]:
    size = max(len(left), len(right))
    return trim(
        [
            (left[i] if i < len(left) else 0)
            - (right[i] if i < len(right) else 0)
            for i in range(size)
        ],
        p,
    )


def multiply(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return trim(out, p)


def divide(left: list[int], right: list[int], p: int) -> tuple[list[int], list[int]]:
    dividend = trim(left[:], p)
    divisor = trim(right[:], p)
    if divisor == [0]:
        raise Reject("polynomial division by zero")
    if len(dividend) < len(divisor):
        return [0], dividend
    quotient = [0] * (len(dividend) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, p)
    while dividend != [0] and len(dividend) >= len(divisor):
        shift = len(dividend) - len(divisor)
        coefficient = dividend[-1] * inverse % p
        quotient[shift] = coefficient
        for i, value in enumerate(divisor):
            dividend[i + shift] = (dividend[i + shift] - coefficient * value) % p
        dividend = trim(dividend, p)
    return trim(quotient, p), dividend


def gcd(left: list[int], right: list[int], p: int) -> list[int]:
    a, b = trim(left, p), trim(right, p)
    while b != [0]:
        _, remainder = divide(a, b, p)
        a, b = b, remainder
    inverse = pow(a[-1], -1, p)
    return trim([inverse * value for value in a], p)


def pow_x(exponent: int, modulus: list[int], p: int) -> list[int]:
    result = [1]
    base = [0, 1]
    while exponent:
        if exponent & 1:
            result = divide(multiply(result, base, p), modulus, p)[1]
        base = divide(multiply(base, base, p), modulus, p)[1]
        exponent >>= 1
    return trim(result, p)


def validate(data: object) -> dict[str, int]:
    if not isinstance(data, dict) or set(data) != {
        "schema",
        "canonical_dossier_commit",
        "upstream",
        "field",
        "row",
        "record",
    }:
        raise Reject("top-level schema")
    if data["schema"] != "rate-half-mca-pole-line-typed-witness-certificate-v1":
        raise Reject("schema")
    if data["canonical_dossier_commit"] != "c8d48cd4b94fb256ad9fedfc1d53b4b14c77bfad":
        raise Reject("canonical pin")
    if data["upstream"] != {
        "pr1159_head": "e603e0cedc5220ec2f29bd53836e732e3ec14934",
        "manifest_blob": "ad2adb39a3f20dc6453c0ed3f509db353751ad68",
        "schema_blob": "6789b48476e3f16557ef6be59d086c6dd6c77008",
        "python_verifier_blob": "57bfec727a3bf032236c7c0d3f5852c55fd526d9",
        "sage_verifier_blob": "dbfabead1542e2297f3c8ea4e0ac58b503ecf8eb",
        "flint_verifier_blob": "3f8b6b57cab4e2ff598556c94f42784001fe56f4",
        "wolfram_verifier_blob": "59a755387b7add10ce273a13422eeb373abc9513",
        "semantic_mutations_rejected": 62,
        "parser_mutations_rejected": 3,
    }:
        raise Reject("upstream pins")

    field = data["field"]
    row = data["row"]
    record = data["record"]
    if not isinstance(field, dict) or set(field) != {
        "p",
        "p_minus_1_two_exponent",
        "p_minus_1_odd_prime",
        "pocklington_witness_for_2",
        "pocklington_witness_for_127",
        "extension_modulus_low_to_high",
    }:
        raise Reject("field schema")
    if not isinstance(row, dict) or set(row) != {
        "n",
        "k",
        "effective_k",
        "m",
        "omega",
        "zeta",
    }:
        raise Reject("row schema")
    if not isinstance(record, dict) or set(record) != {
        "id",
        "error_prefix_size",
        "support_start",
        "support_end_exclusive",
        "slope",
        "r0",
        "r1",
        "slope_word",
        "explanation",
        "guarded_quotient_degree",
        "d1_code_shift",
        "d1_effective_shift",
        "frozen_owner",
    }:
        raise Reject("record schema")

    p = integer(field["p"])
    two_exponent = integer(field["p_minus_1_two_exponent"])
    odd_prime = integer(field["p_minus_1_odd_prime"])
    witnesses = {
        2: integer(field["pocklington_witness_for_2"]),
        odd_prime: integer(field["pocklington_witness_for_127"]),
    }
    modulus = field["extension_modulus_low_to_high"]
    if p != 2130706433 or two_exponent != 24 or odd_prime != 127:
        raise Reject("base modulus")
    if p - 1 != odd_prime * 2**two_exponent or odd_prime != 127:
        raise Reject("factorization")
    for prime, witness in witnesses.items():
        if (
            pow(witness, p - 1, p) != 1
            or math.gcd(pow(witness, (p - 1) // prime, p) - 1, p) != 1
        ):
            raise Reject("Pocklington witness")
    if modulus != [6, 1, 0, 0, 0, 0, 1]:
        raise Reject("extension modulus")
    x = [0, 1]
    if pow_x(p**6, modulus, p) != x:
        raise Reject("extension closure")
    for exponent in (p**2, p**3):
        if gcd(modulus, subtract(pow_x(exponent, modulus, p), x, p), p) != [1]:
            raise Reject("extension reducible")

    n = integer(row["n"])
    k = integer(row["k"])
    effective_k = integer(row["effective_k"])
    m = integer(row["m"])
    omega = integer(row["omega"])
    zeta = integer(row["zeta"])
    if (
        n != 1 << 21
        or k != 1 << 20
        or effective_k != k + 1
        or m != 1116048
        or omega != n - m
        or zeta != pow(3, (p - 1) // n, p)
        or pow(zeta, n, p) != 1
        or pow(zeta, n // 2, p) != p - 1
    ):
        raise Reject("deployed row")

    e = integer(record["error_prefix_size"])
    start = integer(record["support_start"])
    end = integer(record["support_end_exclusive"])
    if (
        record["id"] != "KB_SPARSE_BOUNDARY_ACTUAL_RECORD_V1"
        or e != 67473
        or start != e
        or end != e + m
        or end >= n
        or record["slope"] != "alpha"
        or record["r0"] != "indicator_E + alpha/(x-alpha)"
        or record["r1"] != "-1/(x-alpha)"
        or record["slope_word"] != "indicator_E"
        or record["explanation"] != "0"
        or record["guarded_quotient_degree"] != -1
        or record["frozen_owner"] != "UNASSIGNED"
    ):
        raise Reject("typed record")

    # Exact support witness, guarded adapter, and pole noncontainment margins.
    if (
        end - start != m
        or omega != n - m
        or not -1 < k
        or not m > k + 1
        or m - k != 67472
        or m - effective_k != 67471
    ):
        raise Reject("witness guard")

    # Exact lattice minimum under both shifts.
    off_error = n - e
    actual_n_degree = k + e - 2
    effective_n_degree = k + e - 1
    if (
        off_error != 2029679
        or not off_error > effective_n_degree > actual_n_degree
        or record["d1_code_shift"] != e
        or record["d1_effective_shift"] != e
        or e != (m - k) + 1
        or e != (m - effective_k) + 2
    ):
        raise Reject("minimum/profile ledger")

    return {
        "d1": e,
        "support": m,
        "actual_root_margin": m - k,
        "effective_root_margin": m - (k + 1),
    }


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != SHA256:
        raise Reject("contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["field"].__setitem__("p", item["field"]["p"] + 2),
        lambda item: item["field"]["extension_modulus_low_to_high"].__setitem__(0, 0),
        lambda item: item["row"].__setitem__("zeta", 1),
        lambda item: item["row"].__setitem__("effective_k", item["row"]["k"]),
        lambda item: item["record"].__setitem__("support_end_exclusive", 1183522),
        lambda item: item["record"].__setitem__("guarded_quotient_degree", 1048576),
        lambda item: item["record"].__setitem__("d1_effective_shift", 67472),
        lambda item: item["record"].__setitem__("frozen_owner", "BC"),
        lambda item: item["upstream"].__setitem__("manifest_blob", "0" * 40),
    )
    controls = []
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError(f"negative controls caught {sum(controls)}/{len(controls)}")
    print(
        "RATE_HALF_MCA_POLE_LINE_TYPED_WITNESS_CERTIFICATE_PASS "
        f"d1={result['d1']} support={result['support']} "
        f"root_margins={result['actual_root_margin']},{result['effective_root_margin']} "
        f"owner=UNASSIGNED controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
