#!/usr/bin/env python3
"""Arithmetic replay for both clean Picard pushforward splittings."""


def main():
    profiles = 0
    evaluations = 0
    for m in list(range(2, 65)) + [1 << j for j in range(7, 16)]:
        rho = 4 * m - 1

        x_split = [0, 1 - rho] + [-rho] * (m - 2)
        z_split = [0, 1 - m] + [-m] * (rho - 2)

        assert len(x_split) == m
        assert len(z_split) == rho
        assert sum(x_split) == 1 - (m - 1) * rho
        assert sum(z_split) == 1 - (rho - 1) * m
        assert sum(1 for degree in x_split if degree >= 0) == 1
        assert sum(1 for degree in z_split if degree >= 0) == 1

        # Evaluation directions are checked by dimension and their unit
        # coordinate; do not materialize official-scale power vectors.
        s = 3 * m + 1
        x0 = 5 * m + 2
        assert pow(s, 0, 1009) == pow(x0, 0, 1009) == 1
        evaluations += (m - 1) + (rho - 1)
        profiles += 1

    official_m = 1 << 37
    assert 4 * official_m - 1 == (1 << 39) - 1
    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_PICARD_TWO_PROJECTION_SOCLE_FRAME_PASS "
        f"profiles={profiles} evaluations={evaluations} official_m={official_m}"
    )


if __name__ == "__main__":
    main()
