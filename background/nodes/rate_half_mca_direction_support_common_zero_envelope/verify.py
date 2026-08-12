#!/usr/bin/env python3
"""Verify the exact common-zero direction-support envelope."""

from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "2c0e5a87b672f095c87423f88f0914a9c8b72654369d996329d5f7f06aab0328"
PINNED = {
    "background/nodes/rate_half_mca_direction_support_affine_basis_payment/statement.md": "4dd5c56a4fc636a6f0460f9be7ad468ddf767851090b9e7dcbfcddae048d687e",
    "background/nodes/rate_half_mca_direction_support_affine_basis_payment/proof.md": "9c5d4599da0fcf754e5b7965efcf22be59ab47266278ab1310267d9eb368b02c",
    "background/nodes/rate_half_mca_supportwise_affine_span_compiler/statement.md": "08bd599c71cf40b4ee53a7eb7483f0b16f99f77616234ceb737ce08301922190",
    "background/nodes/rate_half_mca_supportwise_affine_span_compiler/proof.md": "97915ef59268ab5c1eb64e31b6947c6380ce2ee9cebbd95b61f66153d18e9ae3",
}


class Reject(ValueError):
    pass


def falling(x: int, length: int) -> int:
    return math.prod(range(x - length + 1, x + 1))


def rising(x: int, length: int) -> int:
    return math.prod(range(x, x + length))


def direct_maximum(R: int, d: int, rank: int, e: int) -> tuple[int, int, int]:
    denominator_tail = rising(d, rank)
    best_numerator = -1
    best_denominator = 1
    best_x = -1
    checks = 0
    for x in range(R + rank, 2 * R + 1):
        numerator = falling(x, rank + 1) - falling(x - e, rank + 1)
        denominator = (x - R + d) * denominator_tail
        checks += 1
        if best_x < 0 or numerator * best_denominator > best_numerator * denominator:
            best_numerator, best_denominator, best_x = numerator, denominator, x
    return best_numerator // best_denominator, best_x, checks


def expected_rows() -> dict[str, tuple[object, ...]]:
    return {
        "KoalaBear MCA": (
            1048576, 67472, 274980728111395087,
            [(12, 31806, 274974775880138282, 2097152, 31807, 274982650871609405, 2097152),
             (13, 870, 274698567974075567, 2097152, 871, 275013461593529982, 2097152),
             (14, 26, 274047980317063719, 2097152, 27, 284587337354865036, 2097152),
             (15, 0, 0, None, 1, 349406786895662257, 2097152)],
        ),
        "Mersenne-31 MCA": (
            1048576, 67448, 16777215,
            [(5, 124471, 16777173, 2097152, 124472, 16777288, 2097152),
             (6, 2973, 16774034, 2097152, 2974, 16779652, 2097152),
             (7, 83, 16707825, 2097152, 84, 16909096, 2097152),
             (8, 2, 14083061, 2097152, 3, 21124551, 2097152),
             (9, 0, 0, None, 1, 243238797, 2097152)],
        ),
    }


def validate_shape(contract: object) -> None:
    if not isinstance(contract, dict) or set(contract) != {"schema", "sources", "theorem", "rows"}:
        raise Reject("schema")
    if contract["schema"] != "rate-half-mca-direction-support-common-zero-envelope-v1":
        raise Reject("version")
    if contract["sources"] != {
        "support_basis_payment": "rate_half_mca_direction_support_affine_basis_payment",
        "supportwise_incidence": "rate_half_mca_supportwise_affine_span_compiler",
    }:
        raise Reject("sources")
    if contract["theorem"] != {
        "zero_normal_split": "z=g+c with 0<=z<=K-r",
        "fixed_z_maximizer": "c=0,g=z",
        "x_change": "x=R+K-z in [R+r,R+K]",
        "bound": "floor(max_(x=R+r..R+K) ((x)_fall_(r+1)-(x-e)_fall_(r+1))/((x-R+d)d_rise_r))",
        "uniform_range": "replace R+K by 2R for every r<=K<=R",
    }:
        raise Reject("theorem")
    expected = expected_rows()
    if len(contract["rows"]) != len(expected):
        raise Reject("row count")
    for row in contract["rows"]:
        walls = [
            (item.get("rank"), item.get("last_paid_e"), item.get("bound_last"),
             item.get("argmax_last_x"), item.get("first_unpaid_e"),
             item.get("bound_first_unpaid"), item.get("argmax_first_x"))
            for item in row.get("rank_support_walls", ())
        ]
        values = (row.get("R"), row.get("d"), row.get("budget"), walls)
        if values != expected.get(row.get("name")):
            raise Reject("row constants")


def validate(contract: object) -> dict[str, int]:
    validate_shape(contract)
    scans = 0
    walls_checked = 0
    for row in contract["rows"]:
        R, d, budget = row["R"], row["d"], row["budget"]
        for wall in row["rank_support_walls"]:
            rank, last = wall["rank"], wall["last_paid_e"]
            if last:
                value, argmax, checks = direct_maximum(R, d, rank, last)
                scans += checks
                if value != wall["bound_last"] or argmax != wall["argmax_last_x"]:
                    raise Reject("last maximum")
                if value > budget:
                    raise Reject("last budget")
            elif wall["bound_last"] != 0 or wall["argmax_last_x"] is not None:
                raise Reject("empty last")
            first = wall["first_unpaid_e"]
            if first != last + 1:
                raise Reject("adjacency")
            value, argmax, checks = direct_maximum(R, d, rank, first)
            scans += checks
            if value != wall["bound_first_unpaid"] or argmax != wall["argmax_first_x"]:
                raise Reject("first maximum")
            if value <= budget:
                raise Reject("first budget")
            walls_checked += 1
    return {"scans": scans, "walls": walls_checked}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for relative, digest in PINNED.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            raise Reject(f"source pin: {relative}")
    contract = json.loads(CONTRACT.read_text())
    result = validate(contract)
    controls = []
    for row_index, wall_index, key in (
        (0, 0, "last_paid_e"),
        (0, 2, "argmax_first_x"),
        (1, 0, "bound_last"),
        (1, 3, "bound_first_unpaid"),
    ):
        changed = copy.deepcopy(contract)
        changed["rows"][row_index]["rank_support_walls"][wall_index][key] += 1
        try:
            validate_shape(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_DIRECTION_SUPPORT_COMMON_ZERO_ENVELOPE_PASS "
        f"scan_cells={result['scans']} walls={result['walls']} "
        f"mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
