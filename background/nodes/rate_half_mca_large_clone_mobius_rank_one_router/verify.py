#!/usr/bin/env python3
"""Verify the large-clone Mobius formulas and exact boundary split."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
PINNED = {
    "background/nodes/rate_half_mca_coordinate_clone_subcritical_payment/statement.md":
        "cbeb3646f76418e08a10dae63405dad8b9b3d086db2de379e2bff6f9ca47308d",
    "background/nodes/rate_half_mca_coordinate_clone_subcritical_payment/proof.md":
        "4140a0689a49351b3fe8d651dbf47109c6f90295e74f37da6f4acbe2de433ab0",
}


class Reject(ValueError):
    pass


def coeffs(a: int, b: int, c: int, d: int, q0: int, q1: int,
           a0: int, a1: int, b0: int, b1: int, p: int) -> tuple[list[int], list[int]]:
    qhat = [(c*q0-a*q1) % p, (d*q0-b*q1) % p]
    nhat = [
        (c*a0-a*a1) % p,
        (d*a0+c*b0-b*a1-a*b1) % p,
        (d*b0-b*b1) % p,
    ]
    return qhat, nhat


def eval_poly(values: list[int], z: int, p: int) -> int:
    out = 0
    for value in reversed(values):
        out = (out*z+value) % p
    return out


def validate(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or contract.get("schema") != "rate-half-mca-large-clone-mobius-rank-one-router-v1":
        raise Reject("schema")
    if contract.get("residuals") != ["MOVING_DENOMINATOR_RANK_TWO", "EXACT_M_CLONE_LOCATOR_REMAINDER"]:
        raise Reject("residuals")
    if contract.get("degree_profile") != {
        "denominator": "m-k", "numerator": "m",
        "pulled_denominator_slope_degree": 1,
        "pulled_numerator_slope_degree": 2,
    }:
        raise Reject("degrees")
    row_checks = 0
    for row in contract.get("rows", []):
        if row["d"] != row["m"]-row["k"] or not (row["k"] < row["m"] < row["n"] < 2*row["m"]):
            raise Reject("row")
        row_checks += 1

    p = 101
    identity_checks = 0
    for a,b,c,d in ((2,3,5,7), (1,4,6,9), (3,8,2,11)):
        if (a*d-b*c) % p == 0:
            raise Reject("control determinant")
        for q0,q1,r0,r1,lam in ((7,13,17,19,23), (29,31,37,41,43)):
            a0=(q0*r0+lam*a)%p; b0=(q0*r1+lam*b)%p
            a1=(q1*r0+lam*c)%p; b1=(q1*r1+lam*d)%p
            qhat,nhat=coeffs(a,b,c,d,q0,q1,a0,a1,b0,b1,p)
            for z in range(p):
                if eval_poly(nhat,z,p) != eval_poly(qhat,z,p)*((r0+z*r1)%p)%p:
                    raise Reject("Mobius identity")
                identity_checks += 1

    # Rank-one factor and boundary remainder in F_p[gamma].
    factor_checks = 0
    for root in (2,17,53):
        # ell=gamma-root; N=ell(A+B gamma)+mu L.
        A,B,L = 11,19,31
        for mu in (0,1,7):
            n = [(-root*A+mu*L)%p, (A-root*B)%p, B%p]
            if eval_poly(n,root,p) != mu*L%p:
                raise Reject("boundary remainder")
            if (mu == 0) != (eval_poly(n,root,p) == 0):
                raise Reject("factor dichotomy")
            factor_checks += 1
    return {"rows": row_checks, "identities": identity_checks, "factors": factor_checks}


def main() -> None:
    for relative,digest in PINNED.items():
        if hashlib.sha256((ROOT/relative).read_bytes()).hexdigest() != digest:
            raise Reject(f"source pin: {relative}")
    contract=json.loads(CONTRACT.read_text())
    result=validate(contract)
    controls=[]
    for mutate in ("degree", "row", "residual"):
        changed=copy.deepcopy(contract)
        if mutate == "degree": changed["degree_profile"]["pulled_numerator_slope_degree"] = 3
        elif mutate == "row": changed["rows"][0]["d"] += 1
        else: changed["residuals"][0] = "UNNAMED"
        try: validate(changed)
        except Reject: controls.append(True)
        else: controls.append(False)
    if not all(controls): raise AssertionError("mutation controls")
    print("RATE_HALF_MCA_LARGE_CLONE_MOBIUS_RANK_ONE_ROUTER_PASS "
          f"rows={result['rows']} identities={result['identities']} "
          f"factor_checks={result['factors']} mutations={sum(controls)}/{len(controls)}")


if __name__ == "__main__":
    main()
