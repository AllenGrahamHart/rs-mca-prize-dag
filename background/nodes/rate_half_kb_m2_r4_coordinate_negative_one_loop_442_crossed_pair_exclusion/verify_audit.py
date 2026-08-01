#!/usr/bin/env python3
"""Independent coefficient and symmetry audit."""

import itertools


def canonical(singleton, pairs):
    return singleton, tuple(sorted(tuple(sorted(pair)) for pair in pairs))


def main():
    # Roles L, AB+, AB-, AC+, AC-.  C-sign swap exchanges the two cells.
    first = canonical(0, ((1, 3), (2, 4)))
    second = canonical(0, ((1, 4), (2, 3)))
    swap_c = {0: 0, 1: 1, 2: 2, 3: 4, 4: 3}
    image = canonical(
        swap_c[first[0]],
        tuple((swap_c[left], swap_c[right]) for left, right in first[1]),
    )
    if image != second:
        raise RuntimeError("crossed matching symmetry")

    for prime in (13, 17, 29):
        roots = [value for value in range(prime) if value*value % prime == prime-1]
        if not roots:
            continue
        iota = roots[0]
        for b, r in itertools.product(range(1, prime), repeat=2):
            if b*b % prime == 1:
                continue
            p_value = (b*r+b-iota*r+iota) % prime
            q_value = (b*(r-1)+iota*(r+1)) % prime
            if p_value == q_value == 0:
                raise RuntimeError(f"guarded small-field survivor p={prime}")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_CROSSED_AUDIT_PASS "
        "matching_cells=2 primes=13,17,29"
    )


if __name__ == "__main__":
    main()
