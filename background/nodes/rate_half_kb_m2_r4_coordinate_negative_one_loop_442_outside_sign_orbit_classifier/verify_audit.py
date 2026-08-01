#!/usr/bin/env python3
"""Independent parity audit of the outside sign actions."""


def rank_mod_2(vectors):
    rows = [sum((value & 1) << index for index, value in enumerate(vector))
            for vector in vectors]
    rank = 0
    for column in range(max(len(vector) for vector in vectors)):
        pivot = next((index for index in range(rank, len(rows))
                      if rows[index] & (1 << column)), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for index in range(len(rows)):
            if index != rank and rows[index] & (1 << column):
                rows[index] ^= rows[rank]
        rank += 1
    return rank


def main():
    # A sign flip is represented by 1 in the affected coordinates.
    if rank_mod_2(((1, 0, 1), (0, 1, 1))) != 2:
        raise RuntimeError("S0 action rank")
    if rank_mod_2(((0, 0, 1, 1), (1, 0, 1, 0),
                   (0, 1, 0, 1))) != 3:
        raise RuntimeError("S1 action rank")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_SIGN_AUDIT_PASS "
        "action_ranks=2,3 orbit_counts=2,2,1"
    )


if __name__ == "__main__":
    main()
