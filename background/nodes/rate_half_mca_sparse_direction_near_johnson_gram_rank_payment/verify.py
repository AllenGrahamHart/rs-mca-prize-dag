#!/usr/bin/env python3
"""Verify the sparse-direction near-Johnson Gram-rank payment."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "52a8d0de1e089db1db91035f45b3affdd97039ce849f7340eb68f493ccda27a1"
PINNED = {
    "background/nodes/rate_half_mca_sparse_direction_heavy_fiber_profile/statement.md": "b953ec015b2f4180e1086de29983cbd2d4aff2c3e67066493edc368af07891be",
    "background/nodes/rate_half_mca_sparse_direction_heavy_fiber_profile/proof.md": "28978c430f5d8159948a864e0e2c4a5ab3c12bfb7a5e727c5e73073c020a5465",
    "background/nodes/rate_half_mca_sparse_direction_punctured_johnson_profile/statement.md": "3cf121f53d306a72c6e624da54d7488a8036272e9013f54eceb87617923a2fdb",
    "background/nodes/rate_half_mca_sparse_direction_punctured_johnson_profile/proof.md": "109d04f93c9d4f0d506a5d5826f7a37241be174b96f8cb751dd3ca73e958092b",
}


class Reject(ValueError):
    pass


def values(R: int, d: int, K: int, e: int) -> dict[str, int | None]:
    N = R + K
    m = d + K
    c = K - 1
    n = N - e
    A = m - e
    johnson_den = A * A - n * c
    g = -johnson_den
    gram_den = (A - c) ** 2 - c * g
    ordinary = None if gram_den <= 0 else n * A * (A - c) // gram_den
    u = e // 2
    Au = m - u
    half_den = Au * Au - n * c
    if half_den <= 0:
        raise Reject("half Johnson denominator")
    half_cap = n * (Au - c) // half_den
    bound = None if ordinary is None else (e - 1) * half_cap + ordinary
    return {
        "punctured_length": n,
        "agreement": A,
        "johnson_denominator": johnson_den,
        "johnson_defect": g,
        "gram_denominator": gram_den,
        "ordinary_cap": ordinary,
        "half_index": u,
        "johnson_cap_at_half": half_cap,
        "bound": bound,
    }


def validate(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {"schema", "sources", "theorem", "rows"}:
        raise Reject("schema")
    if contract["schema"] != "rate-half-mca-sparse-direction-near-johnson-gram-rank-v1":
        raise Reject("version")
    if contract["sources"] != {
        "heavy_fiber_profile": "rate_half_mca_sparse_direction_heavy_fiber_profile",
        "punctured_johnson_profile": "rate_half_mca_sparse_direction_punctured_johnson_profile",
    }:
        raise Reject("sources")
    if contract["theorem"] != {
        "post_johnson_defect": "g=nc-A^2>=0",
        "gram_denominator": "G=(A-c)^2-cg>0",
        "ordinary_list_cap": "floor(n*A*(A-c)/G)",
        "mca_bound": "(e-1)J_floor(e/2)+Q_e",
    }:
        raise Reject("theorem")

    expected = {
        "KoalaBear MCA": (
            1048576, 67472, 14, 274980728111395087, 63909, 64037, 984539,
            984553, 3449, 903588, 59452, 196254209, 32018, 28, 198047217,
            64038, -36911, None,
        ),
        "Mersenne-31 MCA": (
            1048576, 67448, 6, 16777215, 65237, 65418, 983158,
            983164, 2036, 770524, 272341, 14927965, 32709, 28, 16759641,
            65419, 247950, 18212004,
        ),
    }
    keys = (
        "R", "d", "K", "budget", "first_new_e", "last_paid_e",
        "equivalent_defect_floor", "punctured_length_at_last",
        "agreement_at_last", "johnson_defect_at_last",
        "gram_denominator_at_last", "ordinary_cap_at_last",
        "half_index_at_last", "johnson_cap_at_half", "bound_at_last",
        "adjacent_e", "adjacent_gram_denominator", "adjacent_bound",
    )
    if len(contract["rows"]) != 2:
        raise Reject("row count")
    checks = 0
    for row in contract["rows"]:
        record = tuple(row.get(key) for key in keys)
        if record != expected.get(row.get("name")):
            raise Reject("row constants")
        R, d, K, budget, first, last, defect, nlast, Alast, glast, Glast, Qlast, ulast, Jlast, Blast, adjacent, Gnext, Bnext = record
        if defect != R - last or adjacent != last + 1:
            raise Reject("boundary coordinates")

        endpoint = values(R, d, K, last)
        if endpoint != {
            "punctured_length": nlast,
            "agreement": Alast,
            "johnson_denominator": -glast,
            "johnson_defect": glast,
            "gram_denominator": Glast,
            "ordinary_cap": Qlast,
            "half_index": ulast,
            "johnson_cap_at_half": Jlast,
            "bound": Blast,
        }:
            raise Reject("endpoint")
        if Blast > budget:
            raise Reject("endpoint budget")
        next_record = values(R, d, K, adjacent)
        if next_record["gram_denominator"] != Gnext or next_record["bound"] != Bnext:
            raise Reject("adjacent")
        if row["name"] == "KoalaBear MCA":
            if Gnext >= 0 or Bnext is not None:
                raise Reject("KoalaBear stop")
        elif Gnext <= 0 or Bnext is None or Bnext <= budget:
            raise Reject("Mersenne stop")

        for e in range(first, last + 1):
            item = values(R, d, K, e)
            if item["johnson_defect"] < 0 or item["gram_denominator"] <= 0:
                raise Reject("strip hypotheses")
            if item["bound"] is None or item["bound"] > budget:
                raise Reject("strip budget")
            checks += 1
    return {"checks": checks}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for relative, digest in PINNED.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            raise Reject(f"source pin: {relative}")
    contract = json.loads(CONTRACT.read_text())
    result = validate(contract)

    controls = []
    for row_index, key, delta in (
        (0, "gram_denominator_at_last", 1),
        (0, "adjacent_gram_denominator", 1),
        (1, "bound_at_last", 1),
        (1, "adjacent_bound", -1),
    ):
        changed = copy.deepcopy(contract)
        changed["rows"][row_index][key] += delta
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_SPARSE_DIRECTION_NEAR_JOHNSON_GRAM_RANK_PASS "
        f"checks={result['checks']} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
