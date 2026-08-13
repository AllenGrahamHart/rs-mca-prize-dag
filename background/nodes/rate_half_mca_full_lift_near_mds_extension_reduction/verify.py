#!/usr/bin/env python3
"""Verify the full-lift near-MDS extension reduction controls."""

from __future__ import annotations

import copy
import hashlib
import json
from itertools import product
from math import prod
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "263f78dc4ceeb0e05e5c9a9383f98d6140376c0fb08aedaeefb6a91ca92d385e"


class Reject(ValueError):
    pass


def weight(word: tuple[int, ...]) -> int:
    return sum(value != 0 for value in word)


def add_scaled(
    left: tuple[int, ...], scale: int, right: tuple[int, ...], prime: int
) -> tuple[int, ...]:
    return tuple((a + scale * b) % prime for a, b in zip(left, right))


def rs_code(prime: int, length: int) -> list[tuple[int, ...]]:
    return [
        tuple((constant + slope * x) % prime for x in range(length))
        for constant, slope in product(range(prime), repeat=2)
    ]


def independent(left: tuple[int, ...], right: tuple[int, ...], prime: int) -> bool:
    if not any(left) or not any(right):
        return False
    return not any(
        all((right[index] - scalar * left[index]) % prime == 0
            for index in range(len(left)))
        for scalar in range(prime)
    )


def extension_weights(
    prime: int,
    code: list[tuple[int, ...]],
    direction: tuple[int, ...],
) -> tuple[int, int, int]:
    words = sorted({
        add_scaled(codeword, scalar, direction, prime)
        for codeword in code
        for scalar in range(prime)
    })
    if len(words) != prime**3:
        raise Reject("extension dimension")
    nonzero = [word for word in words if any(word)]
    first = min(map(weight, nonzero))
    second = min(
        weight(tuple(int(a != 0 or b != 0) for a, b in zip(left, right)))
        for index, left in enumerate(nonzero)
        for right in nonzero[index + 1:]
        if independent(left, right, prime)
    )
    full_support = sum(any(word[index] for word in words) for index in range(len(direction)))
    return first, second, full_support


def falling(value: int, length: int) -> int:
    return prod(value - offset for offset in range(length))


def endpoint_bound(R: int, d: int, K: int) -> int:
    numerator = falling(R + K, K + 1)
    denominator = d * prod(d + offset for offset in range(1, K + 1))
    return numerator // denominator


def required_last_factor(R: int, d: int, K: int, budget: int) -> int:
    numerator = falling(R + K, K + 1)
    base = prod(d + offset for offset in range(1, K + 1))
    low = high = 1
    while numerator // (base * high) > budget:
        high *= 2
    while low < high:
        middle = (low + high) // 2
        if numerator // (base * middle) <= budget:
            high = middle
        else:
            low = middle + 1
    return low


def validate(contract: object) -> tuple[int, int]:
    if not isinstance(contract, dict) or contract.get("schema") != (
        "rate-half-mca-full-lift-near-mds-extension-reduction-v1"
    ):
        raise Reject("schema")
    theorem = contract["theorem"]
    if theorem["dimension"] != "K+1" or theorem["first_weight"] != "d_1(W)=e":
        raise Reject("theorem")

    prime, length = 7, 6
    code = rs_code(prime, length)
    directions = {
        "delta_0": (1, 0, 0, 0, 0, 0),
        "x_squared": tuple(x * x % prime for x in range(length)),
    }
    controls = 0
    for control in contract["finite_controls"]:
        if (control["field"], control["N"], control["K"]) != (prime, length, 2):
            raise Reject("finite parameters")
        direction = directions[control["direction"]]
        distance = min(
            weight(tuple((a - b) % prime for a, b in zip(direction, word)))
            for word in code
        )
        observed = extension_weights(prime, code, direction)
        if observed != tuple(control["weights"]) or observed[0] != distance:
            raise Reject("finite weights")
        controls += 1

    expected = {
        "KoalaBear MCA": (1048576, 67472, 14, 274980728111395087,
                            1048576, 743896698428332665, 182530),
        "Mersenne-31 MCA": (1048576, 67448, 6, 16777215,
                              1048576, 219426634, 882143),
    }
    official = 0
    for row in contract["deployed"]:
        values = tuple(row[key] for key in (
            "R", "d", "K", "budget", "max_e", "mds_endpoint_bound",
            "required_last_factor",
        ))
        if values != expected.get(row["row"]):
            raise Reject("deployed row")
        if endpoint_bound(row["R"], row["d"], row["K"]) != row["mds_endpoint_bound"]:
            raise Reject("endpoint bound")
        if required_last_factor(row["R"], row["d"], row["K"], row["budget"]) != row["required_last_factor"]:
            raise Reject("required factor")
        if not row["mds_endpoint_bound"] > row["budget"]:
            raise Reject("ceiling direction")
        official += 1
    return controls, official


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    contract = json.loads(CONTRACT.read_text())
    controls, official = validate(contract)
    edits = (
        lambda value: value["finite_controls"][0]["weights"].__setitem__(1, 4),
        lambda value: value["deployed"][0].__setitem__("mds_endpoint_bound", 1),
        lambda value: value["deployed"][1].__setitem__("required_last_factor", 67448),
    )
    mutations = 0
    for edit in edits:
        changed = copy.deepcopy(contract)
        edit(changed)
        try:
            validate(changed)
        except Reject:
            mutations += 1
    if mutations != len(edits):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_FULL_LIFT_NEAR_MDS_EXTENSION_REDUCTION_PASS "
        f"controls={controls} official={official} mutations={mutations}/{len(edits)}"
    )


if __name__ == "__main__":
    main()
