#!/usr/bin/env python3
"""Independent exhaustive audit of the local-core route cut."""

from __future__ import annotations

import copy
import hashlib
import itertools
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "7a27aef1521b42bc9704c97345be34263e8b22980b5e7fd65f84560b92ff6c94"


class Reject(ValueError):
    pass


def evaluate(poly: tuple[int, ...], x: int, p: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % p
    return value


def solve_interpolant(
    points: tuple[int, ...], values: tuple[int, ...], p: int
) -> tuple[int, ...]:
    size = len(points)
    matrix = [
        [pow(x, j, p) for j in range(size)] + [value % p]
        for x, value in zip(points, values)
    ]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if matrix[row][column] % p), None
        )
        if pivot is None:
            raise Reject("singular interpolation")
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        inverse = pow(matrix[column][column], -1, p)
        matrix[column] = [(inverse * value) % p for value in matrix[column]]
        for row in range(size):
            if row == column:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                (left - factor * right) % p
                for left, right in zip(matrix[row], matrix[column])
            ]
    coefficients = [matrix[row][-1] for row in range(size)]
    while coefficients and coefficients[-1] == 0:
        coefficients.pop()
    return tuple(coefficients)


def audit(data: object) -> dict[str, int]:
    if not isinstance(data, dict):
        raise Reject("object")
    p = data.get("field")
    domain = tuple(data.get("domain", ()))
    k = data.get("k")
    m = data.get("m")
    line = data.get("received_line")
    explanations = data.get("explanations")
    records = data.get("records")
    if (p, domain, k, m) != (11, tuple(range(1, 11)), 5, 7):
        raise Reject("row")
    if not isinstance(line, dict) or not isinstance(explanations, list):
        raise Reject("payload")
    u = tuple(line.get("u", ()))
    v = tuple(line.get("v", ()))
    if len(u) != 10 or len(v) != 10:
        raise Reject("line")

    supports: dict[int, set[int]] = {}
    enumerated = 0
    for item in explanations:
        slope = item.get("slope")
        expected = tuple(item.get("coefficients", ()))
        word = tuple((a + slope * b) % p for a, b in zip(u, v))
        found: list[tuple[int, ...]] = []
        for coefficients in itertools.product(range(p), repeat=k):
            agreements = sum(
                evaluate(coefficients, x, p) == value
                for x, value in zip(domain, word)
            )
            enumerated += 1
            if agreements >= m:
                found.append(coefficients)
        if found != [expected]:
            raise Reject("exhaustive unique explanation")
        support = {
            x
            for x, value in zip(domain, word)
            if evaluate(expected, x, p) == value
        }
        if support != set(item.get("maximal_support", ())):
            raise Reject("support")
        witness = tuple(item.get("witness_support", ()))
        indices = tuple(domain.index(x) for x in witness)
        u_poly = solve_interpolant(witness, tuple(u[i] for i in indices), p)
        v_poly = solve_interpolant(witness, tuple(v[i] for i in indices), p)
        if (len(u_poly) - 1, len(v_poly) - 1) != (
            item.get("u_interpolant_degree"),
            item.get("v_interpolant_degree"),
        ) or (len(u_poly) <= k and len(v_poly) <= k):
            raise Reject("pair containment")
        supports[slope] = support

    if not isinstance(records, list) or len(records) != 2:
        raise Reject("records")
    cores = []
    for record in records:
        slopes = tuple(record.get("slopes", ()))
        core = set(domain)
        for slope in slopes:
            if slope not in supports:
                raise Reject("unknown slope")
            core &= supports[slope]
        if core != set(record.get("common_core", ())):
            raise Reject("core")
        cores.append(core)
    if data.get("shared_slope") not in set(records[0]["slopes"]) & set(records[1]["slopes"]):
        raise Reject("shared slope")
    if cores[0] == cores[1]:
        raise Reject("distinct cores")
    return {"codewords": enumerated, "slopes": len(supports)}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != SHA256:
        raise Reject("contract hash")
    data = json.loads(CONTRACT.read_text())
    result = audit(data)
    controls = []
    for path, value in (
        (("shared_slope",), 10),
        (("records", 1, "common_core"), [8, 10]),
        (("explanations", 6, "coefficients"), [4, 8, 0, 10, 7]),
    ):
        changed = copy.deepcopy(data)
        target = changed
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        try:
            audit(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("audit controls")
    print(
        "RATE_HALF_MCA_RECORD_LOCAL_CORE_OWNER_NONINVARIANCE_AUDIT_PASS "
        f"slopes={result['slopes']} codewords={result['codewords']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
