#!/usr/bin/env python3
"""Verify the nine complete-chart projective-paving record caps."""

from __future__ import annotations

import copy
import hashlib
import json
from math import prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "2aa863ef930e21cd06b8268dbe12a64571ffbf4ecca42888e77453a9b70d23ea"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def validate(data: object) -> list[int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-kernel-projective-paving-record-caps-v2",
        "schema",
    )
    require(data.get("dependencies") == [
        "matroid_paving_basis_floor",
        "rate_half_mca_rank11_kernel_canonical_basis_globalizer",
        "rate_half_mca_support_local_transversality_compiler",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    n0, m0 = p["n_offset"], p["m_offset"]
    require((n0, m0) == (1048576, 67472), "offsets")
    require(
        p["chart"] == "(n,K,m,s)=(1048576+d,d,67472+d,d)",
        "chart",
    )
    require(
        p["basis_floor_formula"] == "(d+1)*(m-1)_fall_d",
        "basis formula",
    )
    records = p.get("records")
    require(isinstance(records, list) and len(records) == 9, "record table")
    caps = []
    for dimension, row in enumerate(records, 1):
        n, m = n0 + dimension, m0 + dimension
        require(
            (row["dimension"], row["domain_size"], row["support_size"])
            == (dimension, n, m),
            "complete row",
        )
        bases = (dimension + 1) * falling(m - 1, dimension)
        resource = falling(n, dimension + 1)
        cap, remainder = divmod(resource, bases)
        require(row["minimum_ordered_bases"] == bases, "basis floor")
        require(row["ordered_coordinate_resource"] == resource, "resource")
        require(
            (row["record_cap"], row["division_remainder"])
            == (cap, remainder),
            "division",
        )
        caps.append(cap)
    require("not uniform" in str(data.get("nonclaim")), "scope fence")
    return caps


def main() -> None:
    require(
        hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256,
        "contract hash",
    )
    data = json.loads(CONTRACT.read_text())
    caps = validate(data)
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item["parameters"].__setitem__("n_offset", 1048575),
        lambda item: item["parameters"]["records"][3].__setitem__("dimension", 5),
        lambda item: item["parameters"]["records"][4].__setitem__("minimum_ordered_bases", 1),
        lambda item: item["parameters"]["records"][5].__setitem__("ordered_coordinate_resource", 1),
        lambda item: item["parameters"]["records"][6].__setitem__("record_cap", 1),
        lambda item: item["parameters"]["records"][7].__setitem__("division_remainder", 0),
        lambda item: item.__setitem__("nonclaim", "uniform"),
    )
    caught = 0
    for mutation in mutations:
        altered = copy.deepcopy(data)
        mutation(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_PROJECTIVE_PAVING_RECORD_CAPS_PASS "
        f"complete_caps={','.join(map(str, caps))} controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
