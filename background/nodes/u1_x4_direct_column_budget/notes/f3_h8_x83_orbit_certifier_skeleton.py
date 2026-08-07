#!/usr/bin/env python3
"""Shardable skeleton for the h=8 n=64 non-antipodal x83 support certifier.

This is not a full certificate run.  It supplies the mechanics a future Modal
job needs: rank-interval sharding of anchored supports, safe rotation
canonicalization, antipodal exclusion, x83 obstruction testing, and partial
progress output before the time budget expires.
"""

from __future__ import annotations

import json
from math import comb
import os
import time

from f3_h8_n64_x83_obstruction_interface import (
    forced_obstructions,
    is_antipodal_support,
    is_square_mod,
    locator_from_exponents,
    root_table,
)
from f3_h8_x83_parity_reduction import has_high_odd_locator_term


N = 64
SUPPORT_SIZE = 16
ANCHOR_TAIL = SUPPORT_SIZE - 1
ANCHOR_UNIVERSE = N - 1
TOTAL_ANCHORED = comb(ANCHOR_UNIVERSE, ANCHOR_TAIL)
ANTIPODAL_ANCHORED = comb(31, 7)
NONANTIPODAL_ANCHORED = TOTAL_ANCHORED - ANTIPODAL_ANCHORED
NONANTIPODAL_ROTATION_ORBITS = NONANTIPODAL_ANCHORED // SUPPORT_SIZE


def unrank_combination_lex(rank: int, n: int, k: int) -> tuple[int, ...]:
    """Return the rank-th k-combination of range(n) in lexicographic order."""

    if rank < 0 or rank >= comb(n, k):
        raise ValueError((rank, n, k))
    out: list[int] = []
    start = 0
    remaining_rank = rank
    for remaining in range(k, 0, -1):
        for value in range(start, n):
            count = comb(n - value - 1, remaining - 1)
            if remaining_rank < count:
                out.append(value)
                start = value + 1
                break
            remaining_rank -= count
        else:
            raise AssertionError((rank, n, k, out))
    return tuple(out)


def anchored_support_from_rank(rank: int) -> tuple[int, ...]:
    tail = unrank_combination_lex(rank, ANCHOR_UNIVERSE, ANCHOR_TAIL)
    return (0,) + tuple(x + 1 for x in tail)


def rotate_to_anchor(support: tuple[int, ...], anchor: int) -> tuple[int, ...]:
    return tuple(sorted((exponent - anchor) % N for exponent in support))


def canonical_anchored_rotation(support: tuple[int, ...]) -> tuple[int, ...]:
    return min(rotate_to_anchor(support, anchor) for anchor in support)


def is_rotation_canonical(support: tuple[int, ...]) -> bool:
    return support == canonical_anchored_rotation(support)


def shard_interval(shard_index: int, shard_count: int) -> tuple[int, int]:
    if shard_count <= 0 or not (0 <= shard_index < shard_count):
        raise ValueError((shard_index, shard_count))
    start = TOTAL_ANCHORED * shard_index // shard_count
    stop = TOTAL_ANCHORED * (shard_index + 1) // shard_count
    return start, stop


def x83_full_zero(support: tuple[int, ...], vals: list[int], p: int) -> bool:
    locator = locator_from_exponents(support, vals, p)
    _, obstructions, lam = forced_obstructions(locator, p, 8)
    return all(v == 0 for v in obstructions) and lam != 0 and is_square_mod(lam, p)


def self_check() -> None:
    if NONANTIPODAL_ANCHORED % SUPPORT_SIZE != 0:
        raise AssertionError("non-antipodal anchored supports should split into 16 anchors")
    if NONANTIPODAL_ROTATION_ORBITS != 7_633_233_227_520:
        raise AssertionError(NONANTIPODAL_ROTATION_ORBITS)

    support = (0, 1, 3, 6, 8, 11, 14, 17, 20, 23, 27, 31, 36, 42, 49, 57)
    if is_antipodal_support(support, N):
        raise AssertionError(support)
    canonical = canonical_anchored_rotation(support)
    for anchor in support:
        rotated = rotate_to_anchor(support, anchor)
        if canonical_anchored_rotation(rotated) != canonical:
            raise AssertionError((support, anchor, rotated, canonical))


def scan() -> dict[str, int | tuple[int, ...] | None]:
    p = int(os.environ.get("F3_H8_ORBIT_P", "4289"))
    shard_count = int(os.environ.get("F3_H8_ORBIT_SHARDS", "1"))
    shard_index = int(os.environ.get("F3_H8_ORBIT_SHARD", "0"))
    max_supports = int(os.environ.get("F3_H8_ORBIT_MAX_SUPPORTS", "2048"))
    seconds = float(os.environ.get("F3_H8_ORBIT_SECONDS", "0"))

    shard_start, shard_stop = shard_interval(shard_index, shard_count)
    start = int(os.environ.get("F3_H8_ORBIT_START_RANK", str(shard_start)))
    stop = int(os.environ.get("F3_H8_ORBIT_STOP_RANK", str(shard_stop)))
    if not (shard_start <= start <= stop <= shard_stop):
        raise ValueError((shard_start, start, stop, shard_stop))
    if max_supports > 0:
        stop = min(stop, start + max_supports)

    vals = root_table(p, N)
    deadline = time.monotonic() + seconds if seconds > 0 else None
    processed = 0
    nonantipodal = 0
    canonical = 0
    high_odd_zero_skipped = 0
    first_obstruction_zero = 0
    full_zero = 0
    first_full_zero: tuple[int, ...] | None = None

    rank = start
    while rank < stop:
        if deadline is not None and processed and processed % 64 == 0:
            if time.monotonic() >= deadline:
                break
        support = anchored_support_from_rank(rank)
        processed += 1
        if not is_antipodal_support(support, N):
            nonantipodal += 1
            if is_rotation_canonical(support):
                canonical += 1
                locator = locator_from_exponents(support, vals, p)
                if not has_high_odd_locator_term(locator):
                    high_odd_zero_skipped += 1
                    rank += 1
                    continue
                _, obstructions, lam = forced_obstructions(locator, p, 8)
                first_obstruction_zero += int(obstructions[-1] == 0)
                if all(v == 0 for v in obstructions) and lam != 0 and is_square_mod(lam, p):
                    full_zero += 1
                    if first_full_zero is None:
                        first_full_zero = support
        rank += 1

    return {
        "p": p,
        "shard": shard_index,
        "shards": shard_count,
        "shard_start": shard_start,
        "shard_stop": shard_stop,
        "start_rank": start,
        "next_rank": rank,
        "stop_rank": stop,
        "processed": processed,
        "nonantipodal": nonantipodal,
        "canonical": canonical,
        "high_odd_zero_skipped": high_odd_zero_skipped,
        "first_obstruction_zero": first_obstruction_zero,
        "full_zero": full_zero,
        "first_full_zero": first_full_zero,
    }


def main() -> None:
    self_check()
    row = scan()
    print("h=8 x83 orbit-certifier skeleton")
    print(f"total_anchored={TOTAL_ANCHORED}")
    print(f"nonantipodal_anchored={NONANTIPODAL_ANCHORED}")
    print(f"nonantipodal_rotation_orbits={NONANTIPODAL_ROTATION_ORBITS}")
    for key, value in row.items():
        print(f"{key}={value}")
    print("CERT_RECORD " + json.dumps(row, sort_keys=True))
    if row["full_zero"] != 0:
        raise AssertionError(("non-antipodal x83 full-zero candidate", row["first_full_zero"]))
    print("H8_X83_ORBIT_CERTIFIER_SKELETON_PASS")


if __name__ == "__main__":
    main()
