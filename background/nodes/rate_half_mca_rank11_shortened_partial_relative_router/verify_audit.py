#!/usr/bin/env python3
"""Independent audit of shortened extraction and certificate lifting."""

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


def convolution(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for total in range(len(out)):
        out[total] = sum(
            left[i] * right[total - i]
            for i in range(len(left))
            if 0 <= total - i < len(right)
        ) % p
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def value(poly: list[int], x: int, p: int) -> int:
    return sum(coefficient * pow(x, degree, p) for degree, coefficient in enumerate(poly)) % p


def audit(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    row = data.get("official")
    toy = data.get("toy")
    require(isinstance(row, dict) and isinstance(toy, dict), "records")
    dimension, agreement = row.get("K"), row.get("m")
    excess = agreement - dimension
    threshold = 3 * agreement - dimension + 3
    require((excess, threshold) == (67472, 2299571), "official arithmetic")
    for c in (0, 1, 4130, 1045975, dimension - 1):
        kp, mp = dimension - c, agreement - c
        unknowns = excess + 1 + 2 * (mp + 1)
        require(unknowns == 3 * mp - kp + 3, "unknown count")
        require(unknowns + 2 * c == threshold, "threshold lift")

    p = toy.get("field")
    LC = toy.get("common_locator")
    Q = toy.get("denominator_Q")
    AC, BC = toy.get("common_A"), toy.get("common_B")
    u, v = toy.get("residual_u"), toy.get("residual_v")
    require(
        (LC, Q, AC, BC, u, v, toy.get("scalar_c0"), toy.get("scalar_c1"))
        == (
            [0, 16, 1],
            [2, 1, 1],
            [4, 1],
            [6, 2],
            [1, 2, 0, 1],
            [3, 0, 4],
            5,
            2,
        ),
        "toy certificate pins",
    )
    LR = [1]
    for root in toy.get("residual_locator_roots"):
        LR = convolution(LR, [(-root) % p, 1], p)
    c0, c1 = toy.get("scalar_c0"), toy.get("scalar_c1")
    Qu, Qv = convolution(Q, u, p), convolution(Q, v, p)
    size = max(len(Qu), len(LR))
    A1 = [((Qu[i] if i < len(Qu) else 0) + c0 * (LR[i] if i < len(LR) else 0)) % p for i in range(size)]
    size = max(len(Qv), len(LR))
    B1 = [((Qv[i] if i < len(Qv) else 0) + c1 * (LR[i] if i < len(LR) else 0)) % p for i in range(size)]
    QA, QB = convolution(Q, AC, p), convolution(Q, BC, p)
    LCA, LCB = convolution(LC, A1, p), convolution(LC, B1, p)
    size = max(len(QA), len(LCA))
    A = [((QA[i] if i < len(QA) else 0) + (LCA[i] if i < len(LCA) else 0)) % p for i in range(size)]
    size = max(len(QB), len(LCB))
    B = [((QB[i] if i < len(QB) else 0) + (LCB[i] if i < len(LCB) else 0)) % p for i in range(size)]
    L = convolution(LC, LR, p)
    for gamma in toy.get("slopes"):
        scalar = (c0 + c1 * gamma) % p
        for x in range(p):
            h1 = (value(u, x, p) + gamma * value(v, x, p)) % p
            h = (value(AC, x, p) + gamma * value(BC, x, p) + value(LC, x, p) * h1) % p
            left = (value(Q, x, p) * h + scalar * value(L, x, p)) % p
            right = (value(A, x, p) + gamma * value(B, x, p)) % p
            require(left == right, "pointwise lifted identity")
    require(len(L) - 1 == toy.get("m") == 8 and L[-1] == 1, "monic lift")
    require(max(len(A), len(B)) - 1 <= toy.get("m"), "lifted degree")
    require(row.get("slope_degree_minimum") == 18 and row.get("slope_degree_maximum") == 31, "degree pin")
    return {"threshold": threshold, "toy_degree": max(len(A), len(B)) - 1}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = audit(data)
    controls = []
    for section, key, value in (
        ("official", "m", 1116047),
        ("official", "slope_degree_minimum", 17),
        ("toy", "common_B", [6, 3]),
        ("toy", "scalar_c0", 6),
        ("toy", "m", 7),
    ):
        altered = copy.deepcopy(data)
        altered[section][key] = value
        try:
            audit(altered)
        except (Reject, TypeError):
            controls.append(True)
        else:
            controls.append(False)
    require(all(controls), "audit controls")
    print(
        "RATE_HALF_MCA_RANK11_SHORTENED_PARTIAL_RELATIVE_ROUTER_AUDIT_PASS "
        f"chi={result['threshold']} toy_degree={result['toy_degree']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
