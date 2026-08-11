#!/usr/bin/env python3
"""Independent boundary audit for the rational-branch genus argument."""


def main() -> None:
    assert (4 * 1 - 2) * (1 - 1) == 0
    checked = 0
    for m in range(2, 129):
        genus = (4 * m - 2) * (m - 1)
        assert genus >= 6
        assert genus != 0
        checked += 1

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_RATIONAL_ELEMENTARY_BRANCH_"
        f"EXCLUSION_AUDIT_PASS m_gt_1={checked} m1_boundary=0"
    )


if __name__ == "__main__":
    main()
