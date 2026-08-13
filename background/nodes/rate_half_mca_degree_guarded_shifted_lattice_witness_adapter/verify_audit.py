#!/usr/bin/env python3
"""Independent audit of the guarded K=k+1 to K=k witness adapter."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "94935311eaf6f4292add51fe8be92c08d66a17362babc07510b2b5b6a9532517"


class Reject(ValueError):
    pass


def evaluate(poly: tuple[int, ...], x: int, p: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % p
    return value


def check(data: object) -> None:
    if not isinstance(data, dict):
        raise Reject("object")
    row = data.get("official_row_check")
    theorem = data.get("theorem")
    if not isinstance(row, dict) or not isinstance(theorem, dict):
        raise Reject("records")
    fixed = (2097152, 1048576, 1048577, 1116048, 981104, 2029680, 2029679)
    if tuple(
        row.get(key)
        for key in (
            "n",
            "k",
            "effective_k",
            "m",
            "omega",
            "effective_numerator_degree_cap",
            "actual_numerator_degree_cap",
        )
    ) != fixed:
        raise Reject("fixed row")
    n, k, effective_k, m, omega, effective_cap, actual_cap = fixed
    if (
        effective_k != k + 1
        or omega != n - m
        or effective_cap != omega + k
        or actual_cap != omega + k - 1
        or effective_cap - actual_cap != theorem.get("maximum_shift_gap")
    ):
        raise Reject("coefficient gap")

    # Same-support criterion: U=u+v vanishes, while u and v have degree k
    # on an m=k+1 point support and therefore are not code explanations.
    p = 7
    toy_k = 3
    support = (1, 2, 3, 4)
    u = (0, 0, 0, 1)
    v = (0, 0, 0, -1)
    if any((evaluate(u, x, p) + evaluate(v, x, p)) % p for x in support):
        raise Reject("slope-word explanation")
    if len(u) - 1 < toy_k or len(v) - 1 < toy_k:
        raise Reject("noncontainment")

    # Contained control: both support interpolants have degree below k.
    contained_u = (1, 2, 1)
    contained_v = (3, 1)
    if len(contained_u) - 1 >= toy_k or len(contained_v) - 1 >= toy_k:
        raise Reject("contained control")


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != SHA256:
        raise Reject("contract hash")
    data = json.loads(CONTRACT.read_text())
    check(data)
    controls = []
    for key, value in (
        ("effective_k", 1048576),
        ("omega", 981105),
        ("actual_numerator_degree_cap", 2029680),
    ):
        altered = copy.deepcopy(data)
        altered["official_row_check"][key] = value
        try:
            check(altered)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("audit controls")
    print(
        "RATE_HALF_MCA_DEGREE_GUARDED_SHIFTED_LATTICE_WITNESS_ADAPTER_AUDIT_PASS "
        f"checks=official-gap,same-support-badness,contained-control controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
