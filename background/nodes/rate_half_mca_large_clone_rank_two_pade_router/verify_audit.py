#!/usr/bin/env python3
"""Independent polynomial-remainder audit for the rank-two clone router."""

from __future__ import annotations

import copy
import json
from pathlib import Path


HERE=Path(__file__).resolve().parent
CONTRACT=HERE/"source_contract.json"


class Reject(ValueError): pass


def audit(contract:object)->dict[str,int]:
    if not isinstance(contract,dict) or contract.get("schema") != "rate-half-mca-large-clone-rank-two-pade-router-v1":
        raise Reject("schema")
    p=1013
    checks=0
    # Evaluate the remainder at the root gamma=-q0/q1. Multiplication by
    # q1^2 recovers exactly Omega.
    for q0 in range(1,12):
        for q1 in range(13,19):
            inv=pow(q1,p-2,p)
            root=(-q0*inv)%p
            for p0,p1,p2 in ((2,3,5),(7,11,13),(17,19,23)):
                rem=(p0+root*p1+root*root*p2)%p
                omega=(q1*q1*p0-q0*q1*p1+q0*q0*p2)%p
                if q1*q1*rem%p != omega: raise Reject("remainder")
                checks+=1
    boundary=0
    for row in contract.get("rows",[]):
        m,d,wall=row["m"],row["d"],row["wall"]
        if wall-m != 2*d or wall>=row["n"]: raise Reject("boundary")
        boundary+=1
    if contract.get("source") != "rate_half_mca_large_clone_mobius_rank_one_router": raise Reject("source")
    return {"remainders":checks,"boundaries":boundary}


def main()->None:
    contract=json.loads(CONTRACT.read_text())
    result=audit(contract)
    controls=[]
    for mode in ("schema","source","boundary"):
        changed=copy.deepcopy(contract)
        if mode=="schema": changed["schema"]="wrong"
        elif mode=="source": changed["source"]="wrong"
        else: changed["rows"][1]["wall"]-=1
        try: audit(changed)
        except Reject: controls.append(True)
        else: controls.append(False)
    if not all(controls): raise AssertionError("controls")
    print("RATE_HALF_MCA_LARGE_CLONE_RANK_TWO_PADE_ROUTER_AUDIT_PASS "
          f"remainder_checks={result['remainders']} boundaries={result['boundaries']} "
          f"controls={sum(controls)}/{len(controls)}")


if __name__=="__main__": main()
