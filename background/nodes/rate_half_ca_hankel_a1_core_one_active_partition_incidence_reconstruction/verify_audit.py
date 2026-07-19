#!/usr/bin/env python3
"""Bounded audit for the incidence potential and density interfaces."""

from verify import propagate


def main():
    p = 1009
    cases = 0
    mutations = 0
    for size in range(4, 48):
        rows = list(range(size))
        cols = list(range(size))
        row_scale = {x: (7 * x + 3) % p or 1 for x in rows}
        col_scale = {g: (11 * g + 5) % p or 1 for g in cols}
        theta = {
            (x, g): row_scale[x] * pow(col_scale[g], -1, p) % p
            for x in rows
            for g in cols
            if x != g
        }
        assert propagate(rows, cols, theta, p) is not None
        cases += len(theta)

        edge = next(iter(theta))
        broken = dict(theta)
        broken[edge] = 2 * broken[edge] % p
        assert propagate(rows, cols, broken, p) is None
        mutations += 1

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_ACTIVE_PARTITION_"
        f"INCIDENCE_RECONSTRUCTION_AUDIT_PASS edges={cases} mutations={mutations}"
    )


if __name__ == "__main__":
    main()
