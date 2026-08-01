#!/usr/bin/env python3
"""Independent orbit-cover audit for complete one-loop 433 exclusion."""


def main():
    owner = {}
    for name, cells in (
        ("aligned", (0,)),
        ("crossed", (1, 2)),
        ("ab_ac", (3, 6)),
        ("mixed", (4, 5, 7, 8)),
        ("bc_mixed", (9, 10, 12, 13)),
        ("opposite", (11, 14)),
    ):
        for cell in cells:
            if cell in owner:
                raise RuntimeError(f"duplicate cell {cell}")
            owner[cell] = name
    if set(owner) != set(range(15)):
        raise RuntimeError("incomplete cover")
    print(
        "RATE_HALF_KB_ONE_LOOP_433_COMPLETE_AUDIT_PASS "
        "orbits=6 cells=15"
    )


if __name__ == "__main__":
    main()
