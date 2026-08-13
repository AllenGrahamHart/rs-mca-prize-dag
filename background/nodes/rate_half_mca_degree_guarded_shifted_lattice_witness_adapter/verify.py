#!/usr/bin/env python3
"""Verify the degree-guarded cross-shift lattice adapter."""

from __future__ import annotations

import copy
import hashlib
import itertools
import json
import math
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "94935311eaf6f4292add51fe8be92c08d66a17362babc07510b2b5b6a9532517"


class Reject(ValueError):
    pass


def trim(poly: list[int], p: int) -> list[int]:
    out = [value % p for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def degree(poly: list[int], p: int) -> int:
    value = trim(poly, p)
    return -1 if value == [0] else len(value) - 1


def add(left: list[int], right: list[int], p: int) -> list[int]:
    size = max(len(left), len(right))
    out = [0] * size
    for index in range(size):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % p
    return trim(out, p)


def scale(poly: list[int], scalar: int, p: int) -> list[int]:
    return trim([(scalar * value) % p for value in poly], p)


def multiply(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return trim(out, p)


def locator(points: tuple[int, ...], p: int) -> list[int]:
    out = [1]
    for point in points:
        out = multiply(out, [(-point) % p, 1], p)
    return out


def interpolate(points: tuple[int, ...], values: tuple[int, ...], p: int) -> list[int]:
    out = [0]
    for i, (x_i, y_i) in enumerate(zip(points, values)):
        basis = [1]
        denominator = 1
        for j, x_j in enumerate(points):
            if i == j:
                continue
            basis = multiply(basis, [(-x_j) % p, 1], p)
            denominator = denominator * (x_i - x_j) % p
        out = add(out, scale(basis, y_i * pow(denominator, -1, p), p), p)
    return trim(out, p)


def integer(value: object) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise Reject("integer field")
    return value


def validate(data: object) -> dict[str, int]:
    if not isinstance(data, dict) or set(data) != {
        "schema",
        "canonical_dossier_commit",
        "upstream",
        "theorem",
        "official_row_check",
        "toy_exhaustion",
    }:
        raise Reject("top-level schema")
    if data["schema"] != "rate-half-mca-degree-guarded-shifted-lattice-witness-adapter-v1":
        raise Reject("schema")
    if data["canonical_dossier_commit"] != "c8d48cd4b94fb256ad9fedfc1d53b4b14c77bfad":
        raise Reject("canonical pin")
    if data["upstream"] != {
        "pr1160_head": "c5f4ea7a0c78828c901ae5f3428894a8b2e2806b",
        "lattice_source_blob": "001c3898b6317911e487ee0199adcce701aaae57",
        "pr1163_head": "e26c15b2d2c2f98ae12dda17b97c40981f76e1ff",
        "dimension_audit_blob": "9a3ea00b216ff16c32cfab0b2b7f8a179cb16ee7",
    }:
        raise Reject("upstream pins")
    if data["theorem"] != {
        "code_shift": "max(deg W, deg N-(k-1))",
        "effective_shift": "max(deg W, deg N-k)",
        "maximum_shift_gap": 1,
        "effective_quotient_degree_cap": "deg(N/W)<=k",
        "actual_quotient_degree_guard": "deg(N/W)<k",
        "same_support_pair_test": "at least one degree-below-m support interpolant has degree at least k",
    }:
        raise Reject("theorem contract")

    official = data["official_row_check"]
    toy = data["toy_exhaustion"]
    if not isinstance(official, dict) or set(official) != {
        "n",
        "k",
        "effective_k",
        "m",
        "omega",
        "effective_numerator_degree_cap",
        "actual_numerator_degree_cap",
    }:
        raise Reject("official schema")
    if not isinstance(toy, dict) or set(toy) != {
        "field",
        "domain_size",
        "k",
        "effective_k",
        "m",
        "supports",
        "assignments_per_support",
        "total_records",
        "expected_actual_records_per_support",
    }:
        raise Reject("toy schema")

    n = integer(official["n"])
    k = integer(official["k"])
    effective_k = integer(official["effective_k"])
    m = integer(official["m"])
    omega = integer(official["omega"])
    effective_cap = integer(official["effective_numerator_degree_cap"])
    actual_cap = integer(official["actual_numerator_degree_cap"])
    if (
        n != 1 << 21
        or k != 1 << 20
        or effective_k != k + 1
        or m != 1116048
        or omega != n - m
        or effective_cap != omega + k
        or actual_cap != omega + k - 1
        or effective_cap != actual_cap + 1
    ):
        raise Reject("official arithmetic")

    p = integer(toy["field"])
    toy_n = integer(toy["domain_size"])
    toy_k = integer(toy["k"])
    toy_effective_k = integer(toy["effective_k"])
    toy_m = integer(toy["m"])
    if (
        p != 7
        or toy_n != 6
        or toy_k != 3
        or toy_effective_k != toy_k + 1
        or toy_m != 4
        or toy["supports"] != math.comb(toy_n, toy_m)
        or toy["assignments_per_support"] != p**toy_m
        or toy["total_records"] != math.comb(toy_n, toy_m) * p**toy_m
        or toy["expected_actual_records_per_support"] != p**toy_k
    ):
        raise Reject("toy arithmetic")

    # Exhaust every exact-support effective-envelope record on the toy row.
    domain = tuple(range(1, toy_n + 1))
    records = 0
    for support in itertools.combinations(domain, toy_m):
        complement = tuple(x for x in domain if x not in support)
        W = locator(complement, p)
        if degree(W, p) != toy_n - toy_m or W[-1] != 1:
            raise Reject("locator")
        actual_count = 0
        for values in itertools.product(range(p), repeat=toy_m):
            h = interpolate(support, values, p)
            N = multiply(W, h, p)
            deg_h = degree(h, p)
            deg_n = degree(N, p)
            effective_envelope = deg_n <= (toy_n - toy_m) + toy_k
            actual_explanation = deg_h < toy_k
            degree_guard = deg_n <= (toy_n - toy_m) + toy_k - 1
            code_shift_cap = max(degree(W, p), deg_n - (toy_k - 1)) <= toy_n - toy_m
            if not effective_envelope:
                raise Reject("effective envelope coverage")
            if actual_explanation != degree_guard or degree_guard != code_shift_cap:
                raise Reject("guard equivalence")
            actual_count += int(actual_explanation)
            records += 1
        if actual_count != p**toy_k:
            raise Reject("support dimension")
    if records != toy["total_records"]:
        raise Reject("record total")

    # Exhaust the abstract degree comparison in a bounded box, including N=0.
    shift_checks = 0
    for deg_w in range(9):
        for deg_n in range(-1, 11):
            s_effective = max(deg_w, deg_n - toy_k)
            s_code = max(deg_w, deg_n - (toy_k - 1))
            if not s_effective <= s_code <= s_effective + 1:
                raise Reject("shift gap")
            shift_checks += 1

    return {"records": records, "shift_checks": shift_checks, "official_gap": 1}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != SHA256:
        raise Reject("contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["theorem"].__setitem__("maximum_shift_gap", 0),
        lambda item: item["official_row_check"].__setitem__("effective_k", 1048576),
        lambda item: item["official_row_check"].__setitem__("omega", 981105),
        lambda item: item["official_row_check"].__setitem__("actual_numerator_degree_cap", 2029680),
        lambda item: item["toy_exhaustion"].__setitem__("field", 6),
        lambda item: item["toy_exhaustion"].__setitem__("total_records", 36014),
        lambda item: item["toy_exhaustion"].__setitem__("expected_actual_records_per_support", 344),
        lambda item: item["upstream"].__setitem__("lattice_source_blob", "0" * 40),
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
        "RATE_HALF_MCA_DEGREE_GUARDED_SHIFTED_LATTICE_WITNESS_ADAPTER_PASS "
        f"toy_records={result['records']} shift_checks={result['shift_checks']} "
        f"official_coefficient_gap={result['official_gap']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
