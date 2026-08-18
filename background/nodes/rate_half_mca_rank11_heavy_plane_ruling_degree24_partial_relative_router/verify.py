#!/usr/bin/env python3
"""Verify the heavy-ruling degree-24 partial-relative router."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "aebdf3c851ac2dbdfe437b569beaeb37a5374abbd7eb658e2ee305bcc6cb4547"


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


def multiply(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return trim(out, p)


def locator(roots: list[int], p: int) -> list[int]:
    out = [1]
    for root in roots:
        out = multiply(out, [(-root) % p, 1], p)
    return out


def validate_toy(toy: object) -> int:
    require(isinstance(toy, dict), "toy")
    p, dimension, agreement = (toy.get(k) for k in ("field", "K", "m"))
    require((p, dimension, agreement) == (17, 6, 8), "toy row")
    LC = toy.get("common_locator")
    AC, BC = toy.get("common_A"), toy.get("common_B")
    u, v = toy.get("residual_u"), toy.get("residual_v")
    Q = toy.get("denominator_Q")
    c0, c1 = toy.get("scalar_c0"), toy.get("scalar_c1")
    require(
        (LC, AC, BC, u, v, Q, c0, c1)
        == (
            [0, 16, 1],
            [4, 1],
            [6, 2],
            [1, 2, 0, 1],
            [3, 0, 4],
            [2, 1, 1],
            5,
            2,
        ),
        "toy pins",
    )
    c = len(LC) - 1
    residual_dimension = dimension - c
    residual_agreement = agreement - c
    require(residual_dimension >= 3, "toy residual dimension")
    require(len(trim(u, p)) - 1 < residual_dimension, "toy u degree")
    require(len(trim(v, p)) - 1 < residual_dimension, "toy v degree")
    require(len(trim(Q, p)) - 1 <= agreement - dimension, "toy denominator")
    LR = locator(toy.get("residual_locator_roots"), p)
    require(len(LR) - 1 == residual_agreement, "toy residual locator")
    A1 = add(multiply(Q, u, p), scale(LR, c0, p), p)
    B1 = add(multiply(Q, v, p), scale(LR, c1, p), p)
    require(max(len(A1), len(B1)) - 1 <= residual_agreement, "toy residual profile")
    A = add(multiply(Q, AC, p), multiply(LC, A1, p), p)
    B = add(multiply(Q, BC, p), multiply(LC, B1, p), p)
    L = multiply(LC, LR, p)
    maximum_degree = 0
    for gamma in toy.get("slopes"):
        h1 = add(u, scale(v, gamma, p), p)
        h = add(add(AC, scale(BC, gamma, p), p), multiply(LC, h1, p), p)
        scalar = (c0 + c1 * gamma) % p
        require(
            add(multiply(Q, h1, p), scale(LR, scalar, p), p)
            == add(A1, scale(B1, gamma, p), p),
            "toy residual identity",
        )
        require(
            add(multiply(Q, h, p), scale(L, scalar, p), p)
            == add(A, scale(B, gamma, p), p),
            "toy lifted identity",
        )
        require(len(h) - 1 < dimension, "toy explanation degree")
        maximum_degree = max(maximum_degree, len(h) - 1)
    require(len(L) - 1 == agreement and L[-1] == 1, "toy monic lift")
    require(max(len(A), len(B)) - 1 <= agreement, "toy lifted degree")
    return maximum_degree


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-heavy-ruling-degree24-partial-relative-router-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == ["rate_half_mca_rank11_heavy_plane_ruling_degree24_order32_seed"],
        "dependency",
    )
    row = data.get("official")
    require(isinstance(row, dict), "official")
    n, dimension, agreement = (row.get(k) for k in ("n", "K", "m"))
    require((n, dimension, agreement) == (2097152, 1048576, 1116048), "row")
    excess = agreement - dimension
    threshold = 3 * agreement - dimension + 3
    require(excess == row.get("agreement_excess") == 67472, "excess")
    require(row.get("denominator_degree_maximum") == excess, "denominator")
    require(row.get("original_complexity_threshold") == threshold == 2299571, "threshold")
    require(
        (
            row.get("seed_size"),
            row.get("anchor_records_minimum"),
            row.get("slope_degree_minimum"),
            row.get("slope_degree_maximum"),
        )
        == (32, 24, 24, 31),
        "degree interface",
    )
    require(row.get("common_support_maximum") == dimension - 3, "core endpoint")
    require(row.get("residual_dimension_minimum") == 3, "residual endpoint")
    samples = data.get("staircase_samples")
    require(isinstance(samples, list) and len(samples) == 4, "samples")
    for sample in samples:
        require(isinstance(sample, dict), "sample")
        c = sample.get("c")
        require(isinstance(c, int) and 0 <= c <= dimension - 3, "sample core")
        kp, mp = dimension - c, agreement - c
        unknowns = (excess + 1) + 2 * (mp + 1)
        require(
            sample
            == {"c": c, "K_residual": kp, "m_residual": mp, "unknowns": unknowns},
            "sample row",
        )
        require(unknowns == 3 * mp - kp + 3, "unknown identity")
        require(unknowns + 2 * c == threshold, "complexity lift")
    toy_degree = validate_toy(data.get("toy"))
    require("pays none" in str(data.get("nonclaim")), "nonclaim")
    return {
        "threshold": threshold,
        "samples": len(samples),
        "toy_explanation_degree": toy_degree,
    }


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item["official"].__setitem__("slope_degree_minimum", 23),
        lambda item: item["official"].__setitem__("anchor_records_minimum", 23),
        lambda item: item["official"].__setitem__("common_support_maximum", 1048574),
        lambda item: item["official"].__setitem__("residual_dimension_minimum", 2),
        lambda item: item["official"].__setitem__("denominator_degree_maximum", 67471),
        lambda item: item["official"].__setitem__("original_complexity_threshold", 2299570),
        lambda item: item["staircase_samples"][3].__setitem__("unknowns", 202424),
        lambda item: item["toy"].__setitem__("scalar_c1", 3),
        lambda item: item["toy"].__setitem__("common_locator", [0, 1, 1]),
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
        print(f"RANK11_RULING_DEG24_PARTIAL_TAMPER_PASS mutations={caught}/9")
        return
    print(
        "RANK11_RULING_DEG24_PARTIAL_PASS "
        f"chi={result['threshold']} stairs={result['samples']} "
        f"toy_explanation_degree={result['toy_explanation_degree']}"
    )


if __name__ == "__main__":
    main()
