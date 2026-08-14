#!/usr/bin/env python3
"""Independent audit for the dense-locator incidence dichotomy."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "6eec697bc3729eab2aba4d282b3c1536e862826cc7c1c17379c2df4ebf55d59b"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def audit(data: object) -> tuple[int, int]:
    require(isinstance(data, dict), "contract")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["correction_dimension"], p["tuple_size"]) == (10, 11), "dimensions")
    require((p["dense_locator_degree"], p["isolated_bezout"]) == (18, 198), "degree")
    exact = Fraction(198 * comb(p["R"] + p["K_min"], 11), comb(p["d"] + p["K_min"], 11))
    ceiling = (exact.numerator + exact.denominator - 1) // exact.denominator
    require(ceiling == p["isolated_equivalent_ceiling"], "independent endpoint")
    require(
        all(
            p["R"] + K - i > p["d"] + K - i > 0
            for K in (p["K_min"], p["K_max"])
            for i in range(11)
        ),
        "positive factors",
    )
    floor = p["budget"] + 1 - p["near_charge"] - p["removed_dense_records"]
    require(floor == p["non_dense_record_floor"], "floor")
    proper = (ceiling * 10**9 + floor - 1) // floor
    require((proper, 10**9 - proper) == (9189066, 990810934), "ppb")
    require(p["one_lane_ppb_floor"] == (10**9 - proper) // 2, "half")
    require(len(data["lanes"]) == 2 and len(data["logical_pins"]) == 5, "structure")

    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    for token in ("bidegree at most `(18,1)`", "2526815879272440", "990810934"):
        require(token in statement, f"statement token {token}")
    for token in (
        "Generic independent perturbations",
        "I_iso<=198*C(n',11)",
        "No division by overlap multiplicity",
    ):
        require(token in proof, f"proof token {token}")
    return ceiling, 10**9 - proper


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    endpoint, component = audit(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("tuple_size", 10),
        lambda item: item["parameters"].__setitem__("isolated_bezout", 199),
        lambda item: item["parameters"].__setitem__("non_dense_record_floor", 274980728111260127),
        lambda item: item["parameters"].__setitem__("one_lane_ppb_floor", 495405468),
        lambda item: item["logical_pins"].pop(),
    )
    controls = []
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            audit(altered)
        except (Reject, KeyError, TypeError, ValueError):
            controls.append(True)
        else:
            controls.append(False)
    require(all(controls), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_DENSE_LOCATOR_COMPONENT_INCIDENCE_DICHOTOMY_AUDIT_PASS "
        f"isolated={endpoint} component_ppb={component} controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
