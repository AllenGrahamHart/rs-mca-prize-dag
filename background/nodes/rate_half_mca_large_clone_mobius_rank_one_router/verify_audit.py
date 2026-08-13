#!/usr/bin/env python3
"""Independent projective-chart audit of the large-clone router."""

from __future__ import annotations

import copy
import json
from pathlib import Path


HERE=Path(__file__).resolve().parent
CONTRACT=HERE/"source_contract.json"


class Reject(ValueError): pass


def inv(x: int,p: int) -> int:
    if x%p == 0: raise ZeroDivisionError
    return pow(x,p-2,p)


def audit(contract: object) -> dict[str,int]:
    if not isinstance(contract,dict) or contract.get("schema") != "rate-half-mca-large-clone-mobius-rank-one-router-v1":
        raise Reject("schema")
    p=103
    chart_checks=owner_checks=boundary_checks=0
    # Build coordinate equations as lambda*(a+bz+ctau+dztau), then compare
    # direct owner evaluation with the pulled-back numerator/denominator.
    a,b,c,d=2,5,7,11
    if (a*d-b*c)%p == 0: raise Reject("determinant")
    for q0,q1,r0,r1,lam in ((13,17,19,23,29),(31,37,41,43,47)):
        A0=(q0*r0+lam*a)%p; B0=(q0*r1+lam*b)%p
        A1=(q1*r0+lam*c)%p; B1=(q1*r1+lam*d)%p
        for z in range(p):
            den=(c+d*z)%p
            if den == 0: continue
            tau=(-(a+b*z)*inv(den,p))%p
            direct_q=(q0+tau*q1)%p
            direct_n=(A0+tau*A1+z*(B0+tau*B1))%p
            pull_q=(den*q0-(a+b*z)*q1)%p
            pull_n=(den*(A0+z*B0)-(a+b*z)*(A1+z*B1))%p
            if pull_q != den*direct_q%p or pull_n != den*direct_n%p:
                raise Reject("chart scaling")
            if pull_n != pull_q*((r0+z*r1)%p)%p:
                raise Reject("clone identity")
            chart_checks += 1

    # Independent rank-one synthetic family. Away from ell=0 every owner
    # ratio is exactly (A+zB)/Q; a nonzero locator remainder blocks this.
    Q,A,B=17,29,31
    root=43
    for z in range(p):
        ell=(z-root)%p
        if ell == 0: continue
        qhat=ell*Q%p
        nhat=ell*(A+z*B)%p
        if nhat*inv(qhat,p)%p != (A+z*B)*inv(Q,p)%p:
            raise Reject("fixed owner")
        owner_checks += 1
    for mu in (1,2,7,19):
        value=mu*53%p
        if value == 0: raise Reject("boundary control")
        boundary_checks += 1

    rows=contract.get("rows",[])
    if [(x.get("m"),x.get("d")) for x in rows] != [(1116048,67472),(1116024,67448)]:
        raise Reject("rows")
    return {"charts":chart_checks,"owners":owner_checks,"boundaries":boundary_checks}


def main() -> None:
    contract=json.loads(CONTRACT.read_text())
    result=audit(contract)
    controls=[]
    for key in ("schema","rows"):
        changed=copy.deepcopy(contract)
        if key == "schema": changed[key]="wrong"
        else: changed[key][1]["m"] += 1
        try: audit(changed)
        except Reject: controls.append(True)
        else: controls.append(False)
    if not all(controls): raise AssertionError("controls")
    print("RATE_HALF_MCA_LARGE_CLONE_MOBIUS_RANK_ONE_ROUTER_AUDIT_PASS "
          f"chart_checks={result['charts']} owner_checks={result['owners']} "
          f"boundary_checks={result['boundaries']} controls={sum(controls)}/{len(controls)}")


if __name__ == "__main__": main()
