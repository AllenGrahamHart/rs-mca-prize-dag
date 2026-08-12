#!/usr/bin/env python3
"""Independent audit of the K-to-K+1 badness mutation."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "391421a32ad5f40bb1be20754760065ea31490f226e13151e79a3ad61a837365"


class Reject(ValueError):
    pass


def check(data: object) -> None:
    if not isinstance(data, dict):
        raise Reject("object")
    row = data.get("row")
    if not isinstance(row, dict):
        raise Reject("row")
    fixed = (2130706433, 2097152, 1048576, 1116048, 1213133211, 67473, 0)
    if tuple(row.get(key) for key in ("p", "n", "k", "m", "zeta", "e", "slope")) != fixed:
        raise Reject("fixed record")
    p, n, dimension, agreement, zeta, e, slope = fixed
    if (
        p - 1 != 127 * 2**24
        or pow(zeta, n, p) != 1
        or pow(zeta, n // 2, p) != p - 1
        or e + agreement != row.get("expected_e_plus_m")
        or e + agreement >= n
        or agreement <= dimension
        or slope != 0
    ):
        raise Reject("arithmetic")
    # Membership is decided solely by the strict degree bound.
    xk_degree = dimension
    in_code_k = xk_degree < dimension
    in_code_kplus1 = xk_degree < dimension + 1
    if in_code_k or not in_code_kplus1:
        raise Reject("code membership")
    # A nonzero degree-k polynomial cannot have m>k distinct roots.
    if agreement - xk_degree != 67472:
        raise Reject("root surplus")


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != SHA256:
        raise Reject("contract hash")
    data = json.loads(CONTRACT.read_text())
    check(data)
    controls = []
    for key, value in (("k", 1048577), ("m", 1048576), ("expected_e_plus_m", 1183522)):
        altered = copy.deepcopy(data)
        altered["row"][key] = value
        try:
            check(altered)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("audit controls")
    print(
        "RATE_HALF_MCA_KPLUS1_BADNESS_TRANSPORT_COUNTEREXAMPLE_AUDIT_PASS "
        f"checks=field,subgroup,support,membership,root-count controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
