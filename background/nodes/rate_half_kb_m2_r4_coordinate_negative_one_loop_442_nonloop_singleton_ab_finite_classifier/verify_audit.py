#!/usr/bin/env python3
"""Independent modular replay of the finite cells [3,6] atlas."""

import itertools


PRIME = 2130706433
IOTA = 16711679
R_ROOTS = {
    1: (382534071, PRIME-382534071),
    -1: (391001680, PRIME-391001680),
}
B_ROOTS = (1608564875, 1587494773)


def determinant(matrix):
    total = 0
    for permutation in itertools.permutations(range(4)):
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(4) for right in range(left+1, 4)
        )
        term = 1
        for row, column in enumerate(permutation):
            term = term*matrix[row][column] % PRIME
        total += (-1 if inversions % 2 else 1)*term
    return total % PRIME


def main():
    if IOTA*IOTA % PRIME != PRIME-1:
        raise RuntimeError("deployed fourth root")
    packets = set()
    for epsilon_1, epsilon_2 in itertools.product((1, -1), repeat=2):
        for r in R_ROOTS[epsilon_2]:
            for b in B_ROOTS:
                if (r*r+epsilon_2*IOTA) % PRIME != 0:
                    raise RuntimeError("r equation")
                if (2*b*b+3*b+2) % PRIME != 0:
                    raise RuntimeError("b equation")
                t_numerator = (
                    -epsilon_1*IOTA*r*r-2*r-epsilon_1*IOTA
                ) % PRIME
                t_denominator = (
                    r*r+2*epsilon_1*IOTA*r+1
                ) % PRIME
                if t_denominator == 0:
                    raise RuntimeError("t denominator")
                t = t_numerator*pow(t_denominator, -1, PRIME) % PRIME
                u_value = (r*r*t*t-3*r*r+3*t*t-1) % PRIME
                v_value = ((r*r-1)*(t*t+1)) % PRIME
                c_denominator = (b*v_value-u_value) % PRIME
                if c_denominator == 0:
                    raise RuntimeError("c denominator")
                c = (
                    b*(b*u_value-v_value)*pow(c_denominator, -1, PRIME)
                ) % PRIME

                roots = (1, t, epsilon_1*IOTA % PRIME, r,
                         epsilon_2*IOTA*r % PRIME)
                labels = tuple(root*root % PRIME for root in roots)
                products = (-(b*b) % PRIME, b, -b % PRIME, c, -c % PRIME)
                sums = (0, 1+b, 1-b, 1+c, 1-c)
                q_values = tuple(
                    root*edge_sum % PRIME
                    for root, edge_sum in zip(roots, sums)
                )
                if 0 in labels or len(set(labels)) != 5:
                    raise RuntimeError("label guard")
                if 0 in products or len(set(products)) != 5:
                    raise RuntimeError("product guard")

                rows = [
                    ((-p) % PRIME, (-p*s) % PRIME, 1, s)
                    for p, s in zip(products, labels)
                ]
                for fourth in (3, 4):
                    if determinant([rows[0], rows[1], rows[2], rows[fourth]]):
                        raise RuntimeError("product determinant")
                differences = tuple((products[0]-value) % PRIME
                                    for value in products)
                for third in (3, 4):
                    left, right = 1, 2
                    weld = (
                        q_values[left]*differences[right]*differences[third]
                        *(labels[third]-labels[right])
                        +q_values[right]*differences[left]*differences[third]
                        *(labels[left]-labels[third])
                        +q_values[third]*differences[left]*differences[right]
                        *(labels[right]-labels[left])
                    ) % PRIME
                    if weld:
                        raise RuntimeError("q weld")
                packets.add((epsilon_1, epsilon_2, r, b, t, c))
    if len(packets) != 16:
        raise RuntimeError("packet count")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_AB_FINITE_AUDIT_PASS "
        "field=2130706433 sign_rows=4 packets=16 direct_replay=1"
    )


if __name__ == "__main__":
    main()
