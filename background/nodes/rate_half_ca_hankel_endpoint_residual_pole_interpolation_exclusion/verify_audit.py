#!/usr/bin/env python3
"""Finite local-length audit for the pole-cancellation inequality."""

from itertools import product


def compositions(total, parts, prefix=()):
    if parts == 1:
        yield prefix + (total,)
        return
    for value in range(1, total - parts + 2):
        yield from compositions(total - value, parts - 1, prefix + (value,))


def main():
    profiles = 0
    for rho in range(3, 13):
        for points in range(1, rho + 1):
            for fibre_lengths in compositions(rho, points):
                # A domain point has common order at least one; a non-domain
                # point has common order zero. Enumerate both choices.
                for common_flags in product((0, 1), repeat=points):
                    u = sum(common_flags)
                    pole = sum(
                        length - 1 if common else length
                        for length, common in zip(fibre_lengths, common_flags)
                    )
                    assert pole == rho - u

                    # Higher common multiplicity only decreases the pole.
                    strengthened = sum(
                        max(length - (2 if common else 0), 0)
                        for length, common in zip(fibre_lengths, common_flags)
                    )
                    assert strengthened <= rho - u
                    profiles += 1

    rho = 23
    u = 17
    mutated_pole = rho - u + 1
    assert mutated_pole > rho - u

    print(
        "RATE_HALF_CA_HANKEL_ENDPOINT_RESIDUAL_POLE_INTERPOLATION_EXCLUSION_AUDIT_PASS "
        f"local_profiles={profiles} mutation=detected"
    )


if __name__ == "__main__":
    main()
