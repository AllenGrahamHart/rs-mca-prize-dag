#!/usr/bin/env python3
"""Mutation audit for axis order, ranks, and degree sums."""


def valid(m, rho, x_split, z_split):
    return (
        rho == 4 * m - 1
        and len(x_split) == m
        and len(z_split) == rho
        and sum(x_split) == 1 - (m - 1) * rho
        and sum(z_split) == 1 - (rho - 1) * m
        and sum(degree >= 0 for degree in x_split) == 1
        and sum(degree >= 0 for degree in z_split) == 1
    )


def main():
    mutations = 0
    rejected = 0
    for m in range(2, 33):
        rho = 4 * m - 1
        x_split = [0, 1 - rho] + [-rho] * (m - 2)
        z_split = [0, 1 - m] + [-m] * (rho - 2)
        assert valid(m, rho, x_split, z_split)

        candidates = [
            (rho + 1, x_split, z_split),
            (rho, x_split + [-rho], z_split),
            (rho, x_split, z_split[:-1]),
            (rho, [1] + x_split[1:], z_split),
            (rho, x_split, [1] + z_split[1:]),
            (rho, [0, -rho] + x_split[2:], z_split),
            (rho, x_split, [0, -m] + z_split[2:]),
        ]
        for bad_rho, bad_x, bad_z in candidates:
            mutations += 1
            if not valid(m, bad_rho, bad_x, bad_z):
                rejected += 1

    assert rejected == mutations
    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_PICARD_TWO_PROJECTION_SOCLE_FRAME_AUDIT_PASS "
        f"mutations={rejected}/{mutations}"
    )


if __name__ == "__main__":
    main()
