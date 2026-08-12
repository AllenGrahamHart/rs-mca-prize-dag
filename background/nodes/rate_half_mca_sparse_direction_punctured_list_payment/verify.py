#!/usr/bin/env python3
"""Verify the sparse-direction punctured-list MCA payment."""

from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "a5eb9a794e69df94bc4aa69f040854693c0f411e09c18d2986f982aae7da57c4"
PINNED = {
    "background/nodes/upstream_gfv4_affine_span_list_compiler/statement.md": "b3be423dd1f85fff8811c98e7da41c03194b38975d89b1f860943e71334e3a31",
    "background/nodes/upstream_gfv4_affine_span_list_compiler/proof.md": "bc36d7a54e91ad5f82d14249b7e1e5c8270fc7c547ca8c37015f04997af01236",
    "background/nodes/rate_half_mca_global_core_direction_distance_router/statement.md": "0bdbd9585b37372cd9ff4ccc708d28ad1e3c2d28dc45e93f151b934e99ada8df",
    "background/nodes/rate_half_mca_global_core_direction_distance_router/proof.md": "22844c8398ab217e5bf238be97edd64c9e939d7803c4a40b0e31b95176641196",
}


class Reject(ValueError):
    pass


def bound(R: int, d: int, s: int, e: int) -> int:
    return e * (math.comb(R - e + s, s) // math.comb(d - e + s, s))


def validate(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {"schema", "sources", "theorem", "rows"}:
        raise Reject("schema")
    if contract["schema"] != "rate-half-mca-sparse-direction-punctured-list-payment-v1":
        raise Reject("version")
    if contract["sources"] != {
        "global_direction_router": "rate_half_mca_global_core_direction_distance_router",
        "ordinary_list_compiler": "upstream_gfv4_affine_span_list_compiler",
    }:
        raise Reject("sources")
    if contract["theorem"] != {
        "direction_residual": "q=r_1-b with b in C and |supp(q)|=e",
        "range": "1<=e<d",
        "punctured_row": "(N-e,s,m-e)=(R+s-e,s,d+s-e)",
        "owner_multiplicity": "at most e slopes per punctured codeword",
        "bound": "e*floor(binomial(R-e+s,s)/binomial(d-e+s,s))",
    }:
        raise Reject("theorem")
    expected = {
        "KoalaBear MCA": (1048576, 67472, 274980728111395087, 14, 5, 239567470186217925, 6, 287536780021025682, 1048571),
        "Mersenne-31 MCA": (1048576, 67448, 16777215, 6, 1, 14115447, 2, 28233244, 1048575),
    }
    checks = 0
    for row in contract["rows"]:
        values = tuple(
            row.get(key)
            for key in (
                "R", "d", "budget", "first_unpaid_s", "last_paid_e",
                "bound_last", "first_unpaid_e", "bound_first_unpaid",
                "equivalent_defect_floor",
            )
        )
        if values != expected.get(row.get("name")):
            raise Reject("row constants")
        R, d, budget, s, last, last_value, first, first_value, defect = values
        previous = -1
        observed_last = 0
        for e in range(1, d):
            value = bound(R, d, s, e)
            checks += 1
            if value < previous:
                raise Reject("monotonicity")
            previous = value
            if value <= budget:
                observed_last = e
        if observed_last != last or first != last + 1:
            raise Reject("boundary")
        if bound(R, d, s, last) != last_value or bound(R, d, s, first) != first_value:
            raise Reject("values")
        if not last_value <= budget < first_value or defect != R - last:
            raise Reject("gate")
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
    for index, key in (
        (0, "bound_last"), (0, "last_paid_e"), (1, "bound_first_unpaid"),
    ):
        changed = copy.deepcopy(contract)
        changed["rows"][index][key] += 1
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    changed = copy.deepcopy(contract)
    changed["rows"][1]["equivalent_defect_floor"] -= 1
    try:
        validate(changed)
    except Reject:
        controls.append(True)
    else:
        controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_SPARSE_DIRECTION_PUNCTURED_LIST_PAYMENT_PASS "
        f"checks={result['checks']} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
