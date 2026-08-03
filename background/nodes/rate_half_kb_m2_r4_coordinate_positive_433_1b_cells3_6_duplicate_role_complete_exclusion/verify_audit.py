#!/usr/bin/env python3
"""Independent arithmetic and scope audit for the cell-3/cell-6 transport."""

import ast
import itertools
from pathlib import Path


NODE = Path(__file__).resolve().parent
VALUES = (-2, -1, 1, 2)
PERMUTATION = (0, 1, 2, 3, 4, 6, 5)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def common3(b, c, r, t, iota, e1, e2):
    return {
        "LA": (-1, 0, 1),
        "AB": (b, t*(1+b), t*t),
        "AC": (c, e1*iota*(1+c), -1),
        "BC+": (b*c, r*(b+c), r*r),
        "BC-": (-b*c, e2*iota*r*(b-c), -r*r),
    }


def common6(b, c, r, t, iota, e1, e2):
    return {
        "LA": (-1, 0, 1),
        "AB": (b, e1*iota*(1+b), -1),
        "AC": (c, t*(1+c), t*t),
        "BC+": (b*c, r*(b+c), r*r),
        "BC-": (-b*c, e2*iota*r*(b-c), -r*r),
    }


def outside(b, c, d, e, f, sigma_c, sigma_o):
    products = (d*e,d*e,-d*e,d*f,sigma_o*e*f,b*f,sigma_c*c*f)
    sums = ((d+e)**2,(d+e)**2,(d-e)**2,(d+f)**2,
            (e+sigma_o*f)**2,(b+f)**2,(c+sigma_c*f)**2)
    return products, sums


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        second = values[index]
        rest = values[1:index] + values[index+1:]
        for tail in pairings(rest):
            yield ((first, second),) + tail


def canonical(matching):
    return tuple(sorted(tuple(sorted(pair)) for pair in matching))


def main():
    ast.parse((NODE / "verify.py").read_text())
    common_rows = 0
    for b,c,r,t,iota in itertools.product(VALUES, repeat=5):
        for e1,e2 in itertools.product((-1,1), repeat=2):
            left = common3(b,c,r,t,iota,e1,e2)
            right = common6(c,b,r,t,iota,e1,-e2)
            role_map = {"LA":"LA","AB":"AC","AC":"AB",
                        "BC+":"BC+","BC-":"BC-"}
            require(all(right[new] == left[old]
                        for new,old in role_map.items()), "common identity")
            common_rows += 1

    outside_rows = 0
    for b,c,d,e,f in itertools.product(VALUES, repeat=5):
        for sigma_c,sigma_o in itertools.product((-1,1), repeat=2):
            left_products,left_sums = outside(b,c,d,e,f,sigma_c,sigma_o)
            right_products,right_sums = outside(
                c,b,sigma_c*d,sigma_c*e,sigma_c*f,sigma_c,sigma_o
            )
            require(all(right_products[PERMUTATION[i]] == left_products[i]
                        for i in range(7)), "outside product identity")
            require(all(right_sums[PERMUTATION[i]] == left_sums[i]
                        for i in range(7)), "outside sum identity")
            outside_rows += 1

    matching_rows = tuple(pairings(range(6)))
    lookup = {canonical(row): index for index,row in enumerate(matching_rows)}
    images = set()
    for xi in range(7):
        old_residual = tuple(i for i in range(7) if i != xi)
        new_xi = PERMUTATION[xi]
        new_residual = tuple(i for i in range(7) if i != new_xi)
        compact = {value:index for index,value in enumerate(new_residual)}
        for matching in matching_rows:
            mapped = canonical(tuple(
                (compact[PERMUTATION[old_residual[l]]],
                 compact[PERMUTATION[old_residual[r]]])
                for l,r in matching
            ))
            images.add((new_xi,lookup[mapped]))
    require(images == set(itertools.product(range(7),range(15))),
            "105-case bijection")
    proof = (NODE / "proof.md").read_text()
    statement = (NODE / "statement.md").read_text()
    require("all 1,680" in proof and "individual" in statement
            and "within-cell matching" in statement,
            "symmetry scope")
    print(f"audit=ok common_rows={common_rows} outside_rows={outside_rows} cases=105")


if __name__ == "__main__":
    main()
