#!/usr/bin/env python3
"""Independent degree replay of the three canonical skeletons."""


def main():
    skeletons = (
        ((0, 1, 1), (0, 0, 0), (2, 2, 1)),
        ((0, 1, 1), (1, 0, 0), (1, 1, 2)),
        ((2, 0, 0), (0, 1, 0), (0, 2, 2)),
    )
    for colored, loops, internal in skeletons:
        m_de, m_df, m_ef = internal
        degrees = (
            2*loops[0]+m_de+m_df+colored[0],
            2*loops[1]+m_de+m_ef+colored[1],
            2*loops[2]+m_df+m_ef+colored[2],
        )
        if degrees != (4, 4, 4):
            raise RuntimeError("outside degree replay")
        if sum(colored) != 2 or sum(loops)+sum(internal) != 5:
            raise RuntimeError("outside record census")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_SKELETON_AUDIT_PASS "
        "skeletons=3 degrees=4,4,4"
    )


if __name__ == "__main__":
    main()
