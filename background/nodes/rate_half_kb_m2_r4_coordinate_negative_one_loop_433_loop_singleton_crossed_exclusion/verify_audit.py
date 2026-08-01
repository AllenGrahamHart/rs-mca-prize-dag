#!/usr/bin/env python3
"""Independent F_73 q scan for crossed one-loop 433 cells."""

import itertools


P = 73
IOTA = 27


def weld(labels, products, q_values, third):
    left, right = 1, 2
    dl = (products[0]-products[left]) % P
    dr = (products[0]-products[right]) % P
    dk = (products[0]-products[third]) % P
    return (
        q_values[left]*dr*dk*(labels[third]-labels[right])
        +q_values[right]*dl*dk*(labels[left]-labels[third])
        +q_values[third]*dl*dr*(labels[right]-labels[left])
    ) % P


def main():
    if IOTA*IOTA % P != P-1:
        raise RuntimeError("fourth root")
    survivors = 0
    tested = 0
    matchings = (((1, 3), (2, 4)), ((1, 4), (2, 3)))
    for matching, epsilon_1, epsilon_2 in itertools.product(
        matchings, (1, -1), (1, -1)
    ):
        for b in range(1, P):
            for c in range(1, P):
                products = (-1 % P, b, c, b*c % P, -b*c % P)
                if len(set(products)) != 5:
                    continue
                sums = (0, 1+b, 1+c, b+c, b-c)
                for r in range(1, P):
                    roots = [0]*5
                    roots[matching[0][0]] = 1
                    roots[matching[0][1]] = epsilon_1*IOTA % P
                    roots[matching[1][0]] = r
                    roots[matching[1][1]] = epsilon_2*IOTA*r % P
                    roots[0] = 1
                    labels = tuple(root*root % P for root in roots)
                    if len(set(labels[1:])) != 4:
                        continue
                    q_values = tuple(
                        root*edge_sum % P
                        for root, edge_sum in zip(roots, sums)
                    )
                    tested += 1
                    if weld(labels, products, q_values, 3) == 0 and weld(
                        labels, products, q_values, 4
                    ) == 0:
                        survivors += 1
    if tested == 0 or survivors:
        raise RuntimeError("finite crossed q scan")
    print(
        "RATE_HALF_KB_ONE_LOOP_433_CROSSED_AUDIT_PASS "
        f"field={P} tested={tested} survivors={survivors}"
    )


if __name__ == "__main__":
    main()
