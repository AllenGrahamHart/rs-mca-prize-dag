#!/usr/bin/env python3
"""Verify the two elementary-modification splitting profiles."""


def sections(degrees: list[int]) -> int:
    return sum(max(degree + 1, 0) for degree in degrees)


def main() -> None:
    scales = (2, 3, 4, 8, 64, 2**37)
    for m in scales:
        rho = 4 * m - 1
        base_degree = -(m - 1) * rho
        first_degree = 1 - (m - 1) * rho
        second_degree = (1 - rho) - (m - 2) * rho

        assert first_degree == base_degree + 1
        assert second_degree == base_degree + 1
        assert first_degree == second_degree == m * (5 - 4 * m)
        assert rho >= 7

        if m <= 64:
            base = [0] + [-rho] * (m - 1)
            first = [1] + [-rho] * (m - 1)
            second = [0, 1 - rho] + [-rho] * (m - 2)
            assert len(base) == len(first) == len(second) == m
            assert sections(base) == 1
            assert sections(first) == 2
            assert sections(second) == 1

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_PICARD_KERNEL_ELEMENTARY_"
        f"MODIFICATION_DICHOTOMY_PASS scales={len(scales)} official_m={2**37}"
    )


if __name__ == "__main__":
    main()
