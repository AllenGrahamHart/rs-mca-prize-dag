#!/usr/bin/env python3
"""Independent representative check for the one-loop 433 skeletons."""


REPRESENTATIVES = (
    ((0, 1, 1), (0, 0, 0), (2, 2, 1)),
    ((0, 1, 1), (1, 0, 0), (1, 1, 2)),
    ((2, 0, 0), (0, 1, 0), (0, 2, 2)),
)


def main():
    for colored, loops, multiplicities in REPRESENTATIVES:
        de, df, ef = multiplicities
        degrees = (
            2*loops[0]+de+df,
            2*loops[1]+de+ef,
            2*loops[2]+df+ef,
        )
        if sum(colored) != 2 or sum(loops) > 1:
            raise RuntimeError("budget")
        if any(degree != 4-colored[index]
               for index, degree in enumerate(degrees)):
            raise RuntimeError("degree")
        if sum(loops)+sum(multiplicities) != 5:
            raise RuntimeError("edge count")
    print(
        "RATE_HALF_KB_ONE_LOOP_433_OUTSIDE_SKELETON_AUDIT_PASS "
        "representatives=3"
    )


if __name__ == "__main__":
    main()
