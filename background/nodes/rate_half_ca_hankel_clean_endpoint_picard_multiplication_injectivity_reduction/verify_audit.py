#!/usr/bin/env python3
"""Audit the bundle splitting fence independently."""


def main() -> None:
    checked = 0
    for m in range(2, 65):
        degree = m * (5 - 4 * m)
        rank = m

        # A negative total degree can still carry a global section.
        splitting = [0] + [-1] * (rank - 2)
        splitting.append(degree - sum(splitting))
        assert len(splitting) == rank
        assert sum(splitting) == degree
        assert max(splitting) == 0
        assert sum(max(value + 1, 0) for value in splitting) >= 1

        # The balanced negative profile has no section, showing the exact
        # extra statement still required.
        quotient, remainder = divmod(-degree, rank)
        balanced = [-quotient - (1 if index < remainder else 0) for index in range(rank)]
        assert sum(balanced) == degree
        assert all(value < 0 for value in balanced)
        assert sum(max(value + 1, 0) for value in balanced) == 0
        checked += 1

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_PICARD_MULTIPLICATION_"
        f"INJECTIVITY_REDUCTION_AUDIT_PASS splittings={checked}"
    )


if __name__ == "__main__":
    main()
