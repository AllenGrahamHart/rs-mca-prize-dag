#!/usr/bin/env python3
"""Pure record router for O0b split cell-0 outside ideals."""


# Variables are indexed as (b,c,d,e,f); sign 0 denotes the outside EF sign.
EDGE_SPECS = {
    "S0": (
        (0, 3, 1), (1, 4, 1),
        (2, 3, 1), (2, 3, -1),
        (2, 4, 1), (2, 4, -1),
        (3, 4, 0),
    ),
    "SDE": (
        (0, 3, 1), (1, 4, 1),
        (2, 3, 1), (2, 3, 1),
        (2, 4, 1), (2, 4, -1),
        (3, 4, 0),
    ),
    "SDF": (
        (0, 3, 1), (1, 4, 1),
        (2, 3, 1), (2, 3, -1),
        (2, 4, 1), (2, 4, 1),
        (3, 4, 0),
    ),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def edge_specs(lane, sigma_o):
    require(lane in EDGE_SPECS and sigma_o in (-1, 1), "lane/sign domain")
    return tuple((left, right, sigma_o if sign == 0 else sign)
                 for left, right, sign in EDGE_SPECS[lane])


def verify(edge_table=EDGE_SPECS):
    require(set(edge_table) == {"S0", "SDE", "SDF"}, "lane cover")
    expected = {
        "S0": ((0, 3, 1), (1, 4, 1), (2, 3, 1), (2, 3, -1),
               (2, 4, 1), (2, 4, -1), (3, 4, 0)),
        "SDE": ((0, 3, 1), (1, 4, 1), (2, 3, 1), (2, 3, 1),
                (2, 4, 1), (2, 4, -1), (3, 4, 0)),
        "SDF": ((0, 3, 1), (1, 4, 1), (2, 3, 1), (2, 3, -1),
                (2, 4, 1), (2, 4, 1), (3, 4, 0)),
    }
    require(edge_table == expected, "signed-edge table")
    for lane in expected:
        for sigma_o in (-1, 1):
            rows = edge_specs(lane, sigma_o)
            require(len(rows) == 7 and rows[-1] == (3, 4, sigma_o),
                    "outside EF sign")
    return 6, 42


def main():
    lanes, rows = verify()
    print(f"RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELL0_OUTSIDE_CORE_PASS "
          f"lanes={lanes} signed_records={rows}")


if __name__ == "__main__":
    main()
