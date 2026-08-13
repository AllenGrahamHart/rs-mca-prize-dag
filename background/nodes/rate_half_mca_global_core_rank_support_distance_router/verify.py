#!/usr/bin/env python3
"""Verify the rank/support router regression and surviving gates."""

import copy
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "c22d48362899884588530448b4b7d518e8b30b46b40ae0a12ded9a72a0cd8cf9"


class Reject(ValueError):
    pass


def validate(contract: object) -> int:
    if not isinstance(contract, dict) or contract.get("schema") != "rate-half-mca-global-core-rank-support-replacement-target-v5":
        raise Reject("schema")
    if contract.get("status") != "TARGET" or contract.get("refuter") != "rate_half_mca_affine_span_incidence_counterexample":
        raise Reject("status")
    if contract.get("retracted") != ["affine-rank gate", "direction-support affine-basis gate", "common-zero gate"]:
        raise Reject("retracted")
    if contract["surviving_sources"].get("near_mds") != (
        "rate_half_mca_full_lift_near_mds_extension_reduction"
    ):
        raise Reject("near-MDS supplier")
    expected = {
        "KoalaBear MCA": (14, 1048576, 5, 4337, 1044239),
        "Mersenne-31 MCA": (6, 1048576, 1, 4334, 1044242),
    }
    checks = 0
    for row in contract["first_gates"]:
        values = tuple(row[key] for key in ("s", "R", "low_e", "frontier_j", "high_e"))
        if values != expected.get(row["row"]):
            raise Reject("row")
        if row["high_e"] != row["R"] - row["frontier_j"]:
            raise Reject("conversion")
        checks += 1
    replacement = {
        "KoalaBear MCA": (14, 5, 9, [[10,981108],[11,981153],[12,981861],[13,992852]], 14, 1044239),
        "Mersenne-31 MCA": (6, 1, 1, [[2,981144],[3,981363],[4,984779],[5,1037876]], 6, 1044242),
    }
    for row in contract["replacement_walls"]:
        values = tuple(row[key] for key in (
            "s", "low_e", "unconditional_through_q", "conditional", "top_q", "top_high_e"
        ))
        if values != replacement.get(row["row"]):
            raise Reject("replacement wall")
        if any(not row["low_e"] + 1 < threshold < row["top_high_e"]
               for _, threshold in row["conditional"]):
            raise Reject("residual interval")
        checks += 1
    split = {
        "KoalaBear MCA": (14, 5, 14, 992852, 15, 1044239),
        "Mersenne-31 MCA": (6, 1, 6, 1037876, 7, 1044242),
    }
    for row in contract["top_rank_split"]:
        values = tuple(row[key] for key in (
            "q", "low_e", "drop_lifted_rank", "drop_high_e",
            "full_lifted_rank", "full_high_e"
        ))
        if values != split.get(row["row"]):
            raise Reject("top-rank split")
        if not row["low_e"] < row["drop_high_e"] < row["full_high_e"]:
            raise Reject("top-rank wall order")
        checks += 1
    ceilings = {
        "KoalaBear MCA": (15, "e", "N-K+j-1", 743896698428332665,
                            274980728111395087),
        "Mersenne-31 MCA": (7, "e", "N-K+j-1", 219426634, 16777215),
    }
    for row in contract["full_lift_ceiling"]:
        values = tuple(row[key] for key in (
            "extension_dimension", "first_weight", "higher_weights",
            "mds_endpoint_bound", "budget",
        ))
        if values != ceilings.get(row["row"]):
            raise Reject("full-lift ceiling")
        if not row["mds_endpoint_bound"] > row["budget"]:
            raise Reject("ceiling direction")
        checks += 1
    return checks


if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
    raise Reject("contract hash")
contract = json.loads(CONTRACT.read_text())
checks = validate(contract)
changed = copy.deepcopy(contract)
changed["top_rank_split"][0]["drop_lifted_rank"] += 1
try:
    validate(changed)
except Reject:
    mutation = 1
else:
    raise AssertionError("mutation")
print(f"RATE_HALF_MCA_GLOBAL_CORE_RANK_SUPPORT_REPLACEMENT_TARGET_PASS gates={checks} mutations={mutation}/1")
