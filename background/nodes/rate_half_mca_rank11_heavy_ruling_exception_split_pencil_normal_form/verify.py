#!/usr/bin/env python3
"""Verify the heavy-ruling exception split-pencil normal form."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "0abba81a802b3ef46b0c7a59144f05ffa1b6c3af8b5dfd20346848fdeea00711"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def trim(poly: list[int], p: int) -> list[int]:
    out = [value % p for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(left: list[int], right: list[int], p: int) -> list[int]:
    return trim(
        [
            (left[i] if i < len(left) else 0)
            + (right[i] if i < len(right) else 0)
            for i in range(max(len(left), len(right)))
        ],
        p,
    )


def scale(poly: list[int], scalar: int, p: int) -> list[int]:
    return trim([scalar * value for value in poly], p)


def evaluate(poly: list[int], x: int, p: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % p
    return value


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-heavy-ruling-exception-split-pencil-normal-form-v1",
        "schema",
    )
    anchors = data.get("minimum_anchor_slopes")
    margin = data.get("pair_core_margin")
    emin, emax = data.get("exception_degree_minimum"), data.get("exception_degree_maximum")
    require((anchors, margin, emin, emax) == (20, 11, 1, 11), "shape")
    require(emin > 0 and emax == margin, "exception interval")
    require(data.get("minimum_split_fibers") == anchors, "split fibers")
    require(data.get("minimum_pairwise_disjoint_fibers") == anchors, "disjoint fibers")
    require(data.get("maximum_scalar_zero_anchor_slopes") == 0, "scalar zeros")
    require(data.get("pencil_gcd_degree") == 0, "pencil gcd")
    require(data.get("denominator_anchor_core_gcd_degree") == 0, "denominator separation")
    require(data.get("denominator_degree_maximum") == 67472, "denominator degree")

    toy = data.get("toy")
    require(isinstance(toy, dict), "toy")
    p, u, v = toy.get("field"), toy.get("u"), toy.get("v")
    slopes, root_sets = toy.get("slopes"), toy.get("root_sets")
    require((p, u, v) == (17, [0, 0, 1], [1]), "toy pencil")
    require(isinstance(slopes, list) and isinstance(root_sets, list), "toy fibers")
    require(len(slopes) == len(root_sets) == 3, "toy count")
    degree = toy.get("fiber_degree")
    seen: set[int] = set()
    maximum_intersection = 0
    for gamma, roots in zip(slopes, root_sets):
        fiber = add(u, scale(v, gamma, p), p)
        require(len(fiber) - 1 == degree == 2 and fiber[-1] == 1, "toy degree")
        require(isinstance(roots, list) and len(roots) == degree, "toy roots")
        require(len(set(roots)) == degree, "toy squarefree")
        require(all(evaluate(fiber, root, p) == 0 for root in roots), "toy split")
        overlap = len(seen & set(roots))
        maximum_intersection = max(maximum_intersection, overlap)
        seen.update(roots)
    require(
        maximum_intersection == toy.get("expected_pairwise_intersection") == 0,
        "toy disjointness",
    )
    require(len(seen) == 6, "toy union")
    require("no split-pencil census" in str(data.get("nonclaim")).lower(), "nonclaim")
    return {"anchors": anchors, "emax": emax, "toy_roots": len(seen)}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("minimum_anchor_slopes", 19),
        lambda item: item.__setitem__("exception_degree_minimum", 0),
        lambda item: item.__setitem__("exception_degree_maximum", 12),
        lambda item: item.__setitem__("minimum_split_fibers", 19),
        lambda item: item.__setitem__("maximum_scalar_zero_anchor_slopes", 1),
        lambda item: item.__setitem__("pencil_gcd_degree", 1),
        lambda item: item.__setitem__("denominator_anchor_core_gcd_degree", 1),
        lambda item: item["toy"].__setitem__("slopes", [16, 13, 7]),
        lambda item: item["toy"].__setitem__("root_sets", [[1, 16], [2, 15], [2, 15]]),
    )
    caught = 0
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    return caught


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    if args.tamper_selftest:
        caught = tamper_selftest(data)
        print(f"RANK11_EXCEPTION_SPLIT_PENCIL_TAMPER_PASS mutations={caught}/9")
        return
    print(
        "RANK11_EXCEPTION_SPLIT_PENCIL_PASS "
        f"anchors={result['anchors']} degree_max={result['emax']} "
        f"toy_roots={result['toy_roots']}"
    )


if __name__ == "__main__":
    main()
