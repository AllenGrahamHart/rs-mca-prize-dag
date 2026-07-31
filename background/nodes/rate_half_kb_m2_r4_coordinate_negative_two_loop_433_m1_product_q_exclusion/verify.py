#!/usr/bin/env python3
"""Verify the 433 M1 product-q exclusion."""

import itertools
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_m1_product_q_exclusion"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("M1 is empty" in statement and "b^2(b+1)^2" in statement, "claim")
    require("five `4 x 4`" in proof and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_product_q_weld",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_product_minor_cell_cut",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    m, r, b, c, x = sp.symbols("m r b c x")
    labels = (r,m,1,-1,-r)
    products = (-1,-c**2,b,-b,b*c)
    rows = [[-p,-p*k,1,k] for k,p in zip(labels,products)]
    minors = [sp.rem(sp.expand(sp.det(sp.Matrix([rows[i] for i in indices]))),m**2+1,m)
              for indices in itertools.combinations(range(5),4)]

    # The raw chart boundary forces M=r^3 and c=M r^2 under label guards.
    boundary = sp.groebner((m**2+1,b+r,*minors),c,b,r,m,order="lex")
    require(boundary.domain == sp.ZZ, "boundary integral domain")
    boundary_guard = r*(r-1)*(r+1)
    require(boundary.reduce(sp.expand(boundary_guard*(r**3-m)))[1] == 0,
            "boundary M relation")
    require(boundary.reduce(sp.expand(boundary_guard*(c-m*r**2)))[1] == 0,
            "boundary c relation")

    q = (1-r)**2*(c**2+b)**2+4*c**2*r*(1+b)**2
    boundary_q = sp.rem(sp.expand(q.subs({b:-r,c:r**5})),r**6+1,r)
    require(sp.expand(boundary_q+2*(r**5-r+2)) == 0, "boundary q reduction")
    require(sp.resultant(r**6+1,r**5-r+2,r) == 4, "boundary resultant")

    # On b+r != 0, reconstruct the normalized Mobius map and its two
    # remaining product equations by cross multiplication.
    numerator = b*(b+r)*x+b*(-b*r-1)
    denominator = (-b*r-1)*x+(b+r)
    require(sp.expand(numerator.subs(x,1)-b*denominator.subs(x,1)) == 0,
            "chart F(1)")
    require(sp.expand(numerator.subs(x,-1)+b*denominator.subs(x,-1)) == 0,
            "chart F(-1)")
    require(sp.expand(numerator.subs(x,r)+denominator.subs(x,r)) == 0,
            "chart F(r)")

    e1 = b*c*r**2+b*c+2*b*r+2*c*r+r**2+1
    e2 = (-b**2*m+b**2*r+b*c**2*m*r-b*c**2-b*m*r+b
          +c**2*m-c**2*r)
    cross_bc = sp.rem(sp.expand(numerator.subs(x,-r)-b*c*denominator.subs(x,-r)),m**2+1,m)
    cross_c2 = sp.rem(sp.expand(numerator.subs(x,m)+c**2*denominator.subs(x,m)),m**2+1,m)
    require(sp.expand(cross_bc+b*e1) == 0, "chart E1")
    require(sp.expand(cross_c2+e2) == 0, "chart E2")

    generators = (m**2+1,e1,e2,q)
    t_poly = m*r+3*m+5*r**2+3*r+4

    first = sp.groebner(generators,c,b,r,m,order="lex")
    require(first.domain == sp.ZZ, "first integral domain")
    guard = (b+1)*(r-1)**3*(r+1)**3*(r**2+1)**2
    target = sp.expand(guard*t_poly)
    require(first.reduce(target)[1] == 0, "first membership")

    second = sp.groebner((*generators,t_poly),c,b,r,m,order="lex")
    require(second.domain == sp.ZZ, "second integral domain")
    require(second.reduce(b**2*(b+1)**2)[1] == 0, "second membership")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_433_M1_PASS "
        "boundary=resultant_4 interior_stage1=T "
        "interior_stage2=b^2(b+1)^2 cell=deleted"
    )


if __name__ == "__main__":
    main()
