#!/usr/bin/env python3
"""Verify the rank-two clone Pade obstruction and exact row walls."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
CONTRACT=HERE/"source_contract.json"
PIN="background/nodes/rate_half_mca_large_clone_mobius_rank_one_router/statement.md"
PIN_SHA256="77bd0aebfb835948005af0442aaee0cc8f5236cde63d9f11be44c8f3f74922be"


class Reject(ValueError): pass


def obstruction(q0:int,q1:int,p0:int,p1:int,p2:int,p:int)->int:
    return (q1*q1*p0-q0*q1*p1+q0*q0*p2)%p


def validate(contract:object)->dict[str,int]:
    if not isinstance(contract,dict) or contract.get("schema") != "rate-half-mca-large-clone-rank-two-pade-router-v1":
        raise Reject("schema")
    if contract.get("obstruction") != [1,-1,1] or contract.get("fixed_owner_denominator_degree_multiplier") != 2:
        raise Reject("formula")
    rows=0
    for row in contract.get("rows",[]):
        if row["d"] != row["m"]-row["k"] or row["wall"] != row["m"]+2*row["d"]:
            raise Reject("wall")
        rows+=1
    p=1009
    zeros=division=0
    for q0,q1,r0,r1 in ((2,3,5,7),(11,13,17,19),(23,29,31,37)):
        p0=q0*r0%p
        p1=(q0*r1+q1*r0)%p
        p2=q1*r1%p
        if obstruction(q0,q1,p0,p1,p2,p): raise Reject("clone zero")
        zeros+=1
        # Scalar specialization of the fraction-field division identity.
        L=1
        A=p0*pow(q0,p-2,p)%p; B=p2*pow(q1,p-2,p)%p
        for z in range(17):
            left=L*(p0+z*p1+z*z*p2)%p
            right=(q0+z*q1)*(A+z*B)%p
            if left != right: raise Reject("division")
            division+=1
    expected=["MOVING_CLONE_BAND_M_TO_M_PLUS_2D","M_PLUS_2D_LOCATOR_REMAINDER","FIXED_DOUBLE_DENOMINATOR_OWNER"]
    if contract.get("residuals") != expected: raise Reject("residuals")
    return {"rows":rows,"zeros":zeros,"division":division}


def main()->None:
    if hashlib.sha256((ROOT/PIN).read_bytes()).hexdigest()!=PIN_SHA256:
        raise Reject("source pin")
    contract=json.loads(CONTRACT.read_text())
    result=validate(contract)
    controls=[]
    for mode in ("wall","formula","residual"):
        changed=copy.deepcopy(contract)
        if mode=="wall": changed["rows"][0]["wall"]+=1
        elif mode=="formula": changed["obstruction"][1]=1
        else: changed["residuals"].pop()
        try: validate(changed)
        except Reject: controls.append(True)
        else: controls.append(False)
    if not all(controls): raise AssertionError("controls")
    print("RATE_HALF_MCA_LARGE_CLONE_RANK_TWO_PADE_ROUTER_PASS "
          f"rows={result['rows']} zero_checks={result['zeros']} "
          f"division_checks={result['division']} mutations={sum(controls)}/{len(controls)}")


if __name__=="__main__": main()
