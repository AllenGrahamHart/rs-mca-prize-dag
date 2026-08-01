#!/usr/bin/env python3
"""Independent F_73 branch scan for cells [4,5,7,8]."""

import itertools


PRIME = 73
IOTA = 27


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
        raise RuntimeError("fourth root")
    guarded = 0
    survivors = 0
    for epsilon_1, epsilon_2 in itertools.product((1, -1), repeat=2):
        for b in range(1, PRIME):
            if b in (1, PRIME-1):
                continue
            for r in range(1, PRIME):
                candidates = [(-pow(r, -1, PRIME)) % PRIME]
                denominator = (r-epsilon_1*IOTA) % PRIME
                if denominator:
                    candidates.append(
                        (epsilon_1*IOTA*r+1)
                        *pow(denominator, -1, PRIME) % PRIME
                    )
                for t in set(candidates):
                    labels = (1, t*t % PRIME, r*r % PRIME,
                              PRIME-1, -(r*r) % PRIME)
                    if 0 in labels or len(set(labels)) != 5:
                        continue
                    a_value = (r*r*t*t-1) % PRIME
                    b_value = (r*r-t*t) % PRIME
                    c_denominator = (b*b_value+a_value) % PRIME
                    if c_denominator == 0:
                        continue
                    c = (
                        -b*(b*a_value+b_value)
                        *pow(c_denominator, -1, PRIME)
                    ) % PRIME
                    products = (-(b*b) % PRIME, b, -b % PRIME,
                                c, -c % PRIME)
                    if 0 in products or len(set(products)) != 5:
                        continue
                    guarded += 1
                    roots = (1, t, r, epsilon_1*IOTA % PRIME,
                             epsilon_2*IOTA*r % PRIME)
                    sums = (0, 1+b, 1-b, 1+c, 1-c)
                    q_values = tuple(
                        root*edge_sum % PRIME
                        for root, edge_sum in zip(roots, sums)
                    )
                    rows = [
                        ((-p) % PRIME, (-p*s) % PRIME, 1, s)
                        for p, s in zip(products, labels)
                    ]
                    equations = [
                        determinant([rows[0], rows[1], rows[2], rows[fourth]])
                        for fourth in (3, 4)
                    ]
                    differences = tuple(
                        (products[0]-value) % PRIME for value in products
                    )
                    for third in (3, 4):
                        left, right = 1, 2
                        equations.append((
                            q_values[left]*differences[right]*differences[third]
                            *(labels[third]-labels[right])
                            +q_values[right]*differences[left]*differences[third]
                            *(labels[left]-labels[third])
                            +q_values[third]*differences[left]*differences[right]
                            *(labels[right]-labels[left])
                        ) % PRIME)
                    if not any(equations):
                        survivors += 1
    if guarded == 0 or survivors != 0:
        raise RuntimeError("finite branch exclusion")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_MIXED_AUDIT_PASS "
        f"field=73 guarded_branch_rows={guarded} survivors={survivors}"
    )


if __name__ == "__main__":
    main()
