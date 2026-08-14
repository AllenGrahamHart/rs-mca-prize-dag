#!/usr/bin/env python3
"""Verify the shortened partial-relative router and exact lift."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "a0f9798b18dec6bcfa3b1d3bab305255dfafd049ceb4e129b261f42a74d18d07"


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
            (left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0)
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
    u, v, Q = toy.get("residual_u"), toy.get("residual_v"), toy.get("denominator_Q")
    c0, c1 = toy.get("scalar_c0"), toy.get("scalar_c1")
    require(LC == [0, 16, 1], "common locator")
    require(
        (AC, BC, u, v, Q, c0, c1)
        == ([4, 1], [6, 2], [1, 2, 0, 1], [3, 0, 4], [2, 1, 1], 5, 2),
        "toy certificate pins",
    )
    c = len(LC) - 1
    residual_dimension = dimension - c
    residual_agreement = agreement - c
    require(len(trim(u, p)) - 1 < residual_dimension and len(trim(v, p)) - 1 < residual_dimension, "residual codewords")
    require(len(trim(Q, p)) - 1 <= agreement - dimension, "denominator degree")
    LR = locator(toy.get("residual_locator_roots"), p)
    require(len(LR) - 1 == residual_agreement, "residual locator")
    A1 = add(multiply(Q, u, p), scale(LR, c0, p), p)
    B1 = add(multiply(Q, v, p), scale(LR, c1, p), p)
    require(max(len(A1), len(B1)) - 1 <= residual_agreement, "residual certificate degree")
    A = add(multiply(Q, AC, p), multiply(LC, A1, p), p)
    B = add(multiply(Q, BC, p), multiply(LC, B1, p), p)
    L = multiply(LC, LR, p)
    max_degree = 0
    for gamma in toy.get("slopes"):
        h1 = add(u, scale(v, gamma, p), p)
        h = add(add(AC, scale(BC, gamma, p), p), multiply(LC, h1, p), p)
        scalar = (c0 + c1 * gamma) % p
        residual_left = add(multiply(Q, h1, p), scale(LR, scalar, p), p)
        residual_right = add(A1, scale(B1, gamma, p), p)
        require(residual_left == residual_right, "residual identity")
        lifted_left = add(multiply(Q, h, p), scale(L, scalar, p), p)
        lifted_right = add(A, scale(B, gamma, p), p)
        require(lifted_left == lifted_right, "lifted identity")
        require(len(h) - 1 < dimension, "lifted explanation degree")
        max_degree = max(max_degree, len(lifted_left) - 1)
    require(max_degree <= agreement and len(L) - 1 == agreement and L[-1] == 1, "lifted profile")
    return max_degree


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-shortened-partial-relative-router-v1", "schema")
    row = data.get("official")
    require(isinstance(row, dict), "official")
    n, dimension, agreement = (row.get(k) for k in ("n", "K", "m"))
    require((n, dimension, agreement) == (2097152, 1048576, 1116048), "row")
    excess = agreement - dimension
    threshold = 3 * agreement - dimension + 3
    require(excess == row.get("agreement_excess") == row.get("denominator_degree_maximum") == 67472, "excess")
    require(threshold == row.get("original_complexity_threshold") == 2299571, "threshold")
    require(
        (row.get("seed_size"), row.get("slope_degree_minimum"), row.get("slope_degree_maximum"))
        == (32, 18, 31),
        "degree interface",
    )
    require(row.get("maximal_common_support_maximum") == dimension - 1, "maximal core")
    require(row.get("residual_dimension_minimum") == 1, "residual minimum")
    samples = data.get("staircase_samples")
    require(isinstance(samples, list) and len(samples) == 4, "samples")
    for sample in samples:
        require(isinstance(sample, dict), "sample")
        c = sample.get("c")
        kp, mp = dimension - c, agreement - c
        unknowns = (excess + 1) + 2 * (mp + 1)
        require(sample == {"c": c, "K_residual": kp, "m_residual": mp, "unknowns": unknowns}, "sample row")
        require(unknowns == 3 * mp - kp + 3, "unknown identity")
        require(unknowns + 2 * c == threshold, "complexity lift")
    toy_degree = validate_toy(data.get("toy"))
    require("no residual branch payment" in str(data.get("nonclaim")), "nonclaim")
    return {"threshold": threshold, "toy_degree": toy_degree, "samples": len(samples)}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["official"].__setitem__("original_complexity_threshold", 2299570),
        lambda item: item["official"].__setitem__("maximal_common_support_maximum", 1048576),
        lambda item: item["official"].__setitem__("denominator_degree_maximum", 67471),
        lambda item: item["staircase_samples"][2].__setitem__("unknowns", 207620),
        lambda item: item["toy"].__setitem__("scalar_c1", 3),
        lambda item: item["toy"].__setitem__("common_locator", [0, 1, 1]),
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
    require(all(controls), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_SHORTENED_PARTIAL_RELATIVE_ROUTER_PASS "
        f"chi={result['threshold']} toy_degree={result['toy_degree']} "
        f"stairs={result['samples']} controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
