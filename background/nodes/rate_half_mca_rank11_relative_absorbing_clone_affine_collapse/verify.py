#!/usr/bin/env python3
"""Verify the absorbing clone-to-affine collapse."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "345259da825c04a6634a371abf6ba4d3857c880271088824e619e83be8f8df8a"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def determinant(matrix: list[list[int]], field: int) -> int:
    require(len(matrix) == 2 and all(len(row) == 2 for row in matrix), "matrix")
    return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % field


def validate(data: object) -> int:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-relative-absorbing-clone-affine-collapse-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == ["rate_half_mca_rank11_relative_correction_tenflat_collapse"],
        "dependencies",
    )
    dimensions = data.get("dimensions")
    invariants = data.get("invariants")
    require(isinstance(dimensions, dict) and isinstance(invariants, dict), "sections")
    require(
        dimensions
        == {
            "correction_minimum": 2,
            "correction_maximum": 10,
            "slope_degree_maximum": 31,
            "received_line_degree": 1,
        },
        "dimensions",
    )
    require(
        invariants
        == {
            "R": 1048576,
            "d": 67472,
            "outside_agreement": 981104,
            "affine_owner_cap": 981105,
        },
        "invariants",
    )
    require(invariants["outside_agreement"] == invariants["R"] - invariants["d"], "outside")
    require(invariants["affine_owner_cap"] == invariants["outside_agreement"] + 1, "owner cap")
    require(
        data.get("routes") == ["AFFINE_OWNER_COMPONENT", "EVALUATION_RANK_FLAT"],
        "routes",
    )
    toy = data.get("toy")
    require(isinstance(toy, dict) and toy.get("field") == 17, "toy")
    matrix = toy.get("basis_evaluation_matrix")
    require(determinant(matrix, 17) != 0, "basis injectivity")
    high = toy.get("high_coefficient")
    solved = toy.get("solved_correction_coefficient")
    require([(a + b) % 17 for a, b in zip(high, solved)] == toy.get("sum") == [0, 0], "cancellation")
    require("remain unpaid" in str(data.get("nonclaim")), "nonclaim")
    return invariants["affine_owner_cap"]


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    cap = validate(data)
    mutations = (
        lambda item: item["dimensions"].__setitem__("received_line_degree", 2),
        lambda item: item["invariants"].__setitem__("affine_owner_cap", 981104),
        lambda item: item["routes"].append("NONLINEAR_CLONE"),
        lambda item: item["toy"].__setitem__("basis_evaluation_matrix", [[1, 1], [1, 1]]),
        lambda item: item["toy"]["solved_correction_coefficient"].__setitem__(0, 12),
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
        "RATE_HALF_MCA_RANK11_RELATIVE_ABSORBING_CLONE_AFFINE_COLLAPSE_PASS "
        f"owner_cap={cap} routes=2 controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
