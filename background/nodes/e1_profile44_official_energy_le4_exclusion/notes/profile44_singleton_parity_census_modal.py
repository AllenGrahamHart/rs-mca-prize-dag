#!/usr/bin/env python3
"""Complete normalized parity census for the four singleton positions."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
import json


def lag(left: int, right: int) -> int | None:
    delta = (right - left) % 128
    if delta == 64:
        return None
    return min(delta, 128 - delta)


def main() -> None:
    counts: Counter[int] = Counter()
    examples: dict[int, list[tuple[int, int, int, int]]] = {}
    total = 0
    for tail in combinations(range(1, 128), 3):
        support = (0,) + tail
        mask = 0
        for left, right in combinations(support, 2):
            distance = lag(left, right)
            if distance is not None:
                mask ^= 1 << distance
        weight = mask.bit_count()
        counts[weight] += 1
        total += 1
        if len(examples.setdefault(weight, [])) < 16:
            examples[weight].append(support)
    print(
        json.dumps(
            {
                "normalized_supports": total,
                "parity_weight_counts": dict(sorted(counts.items())),
                "examples": examples,
            },
            separators=(",", ":"),
        )
    )


if __name__ == "__main__":
    main()
