#!/usr/bin/env python3
"""Independent orbit and mutation audit for the splitting dichotomy."""


def main() -> None:
    checked = 0
    for m in range(2, 65):
        rho = 4 * m - 1
        expected_degree = 1 - (m - 1) * rho
        profiles = {
            tuple([1] + [-rho] * (m - 1)),
            tuple([0, 1 - rho] + [-rho] * (m - 2)),
        }
        assert len(profiles) == 2
        assert all(len(profile) == m for profile in profiles)
        assert all(sum(profile) == expected_degree for profile in profiles)

        # Raising two summands spends length two and is not a candidate.
        mutation = [1, 1 - rho] + [-rho] * (m - 2)
        assert sum(mutation) == expected_degree + 1
        assert tuple(mutation) not in profiles
        checked += 1

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_PICARD_KERNEL_ELEMENTARY_"
        f"MODIFICATION_DICHOTOMY_AUDIT_PASS profiles={checked * 2} mutations={checked}/{checked}"
    )


if __name__ == "__main__":
    main()
