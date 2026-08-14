#!/usr/bin/env python3
"""Verify the relative correction-space incidence router."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "fdcd7e4edc3b587ca22390e620c6dc9f35af64763c520bf3cc0978819c70a43a"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def falling(value: int, length: int) -> int:
    out = 1
    for offset in range(length):
        out *= value - offset
    return out


def rising(value: int, length: int) -> int:
    out = 1
    for offset in range(length):
        out *= value + offset
    return out


def proper_cap(R: int, d: int, dimension: int, s: int) -> int:
    return 31 * (s + 1) * comb(R + dimension, s + 1) // comb(d + dimension, s + 1)


def clone_cap(n: int, R: int, d: int, a: int, s: int) -> int:
    multiplier = 31 * (R + a) // (d + a)
    return multiplier * falling(n, s) // rising(d + a, s)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-rank11-relative-correction-space-router-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == [
            "rate_half_mca_rank11_global_core_rankdrop_highcomplexity_router",
            "rate_half_mca_rank11_relative_core_interpolant_ray_payment",
        ],
        "dependencies",
    )
    row = data.get("official")
    proper = data.get("proper")
    clone = data.get("clone_tolerant")
    require(all(isinstance(x, dict) for x in (row, proper, clone)), "sections")
    require(
        tuple(row.get(key) for key in ("n", "K", "m", "R", "d", "slope_degree"))
        == (2097152, 1048576, 1116048, 1048576, 67472, 31),
        "row",
    )
    proper_entries = proper.get("caps")
    require(isinstance(proper_entries, list) and len(proper_entries) == 12, "proper entries")
    for s, entry in enumerate(proper_entries, 1):
        worst_dimension = max(10, s)
        expected = {
            "s": s,
            "worst_K": worst_dimension,
            "cap": proper_cap(row["R"], row["d"], worst_dimension, s),
        }
        require(entry == expected, f"proper {s}")
    require(proper.get("paid_through_dimension") == 11, "proper threshold")
    require(all(entry["cap"] <= row["budget"] for entry in proper_entries[:11]), "proper paid")
    require(proper_entries[11]["cap"] > row["budget"], "proper wall")

    require(clone.get("minimum_support_excess") == 1, "support excess")
    require(clone.get("M_1") == 31 * (row["R"] + 1) // (row["d"] + 1) == 481, "M1")
    clone_entries = clone.get("caps")
    require(isinstance(clone_entries, list) and len(clone_entries) == 10, "clone entries")
    for s, entry in enumerate(clone_entries, 1):
        require(
            entry == {"s": s, "cap": clone_cap(row["n"], row["R"], row["d"], 1, s)},
            f"clone {s}",
        )
    require(clone.get("paid_through_dimension") == 9, "clone threshold")
    require(all(entry["cap"] <= row["budget"] for entry in clone_entries[:9]), "clone paid")
    require(clone_entries[9]["cap"] > row["budget"], "clone wall")
    require(
        data.get("routes")
        == [
            "DIM_GE_12:correction-span-dimension-at-least-twelve",
            "RANK_FLAT:nonproper-evaluation-rank-defect",
            "CLONE_COMPONENT:nonproper-exact-polynomial-curve",
            "ABSORB_HIGH:required-for-every-survivor-of-dimension-at-most-nine",
        ],
        "routes",
    )
    require("remain unpaid" in str(data.get("nonclaim")), "nonclaim")
    return {
        "proper11": proper_entries[10]["cap"],
        "proper12": proper_entries[11]["cap"],
        "clone9": clone_entries[8]["cap"],
    }


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["proper"].__setitem__("paid_through_dimension", 12),
        lambda item: item["proper"]["caps"][10].__setitem__("worst_K", 10),
        lambda item: item["proper"]["caps"][11].__setitem__("cap", 1),
        lambda item: item["clone_tolerant"].__setitem__("M_1", 480),
        lambda item: item["clone_tolerant"]["caps"][9].__setitem__("cap", 1),
        lambda item: item["routes"].pop(),
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
        "RATE_HALF_MCA_RANK11_RELATIVE_CORRECTION_SPACE_ROUTER_PASS "
        f"proper11={result['proper11']} proper12={result['proper12']} "
        f"clone9={result['clone9']} controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
