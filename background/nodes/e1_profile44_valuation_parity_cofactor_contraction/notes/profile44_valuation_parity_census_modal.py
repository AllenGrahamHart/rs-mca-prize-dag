#!/usr/bin/env python3
"""Complete normalized singleton valuation/parity census for profile (4,4)."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
import json


def hasse_order(support: tuple[int, ...]) -> int:
    residues = Counter(position % 32 for position in support)
    odd_residues = tuple(residue for residue, count in residues.items() if count & 1)
    if not odd_residues:
        return 32
    for derivative in range(32):
        if sum((derivative & ~residue) == 0 for residue in odd_residues) & 1:
            return derivative
    raise AssertionError("nonzero residue polynomial vanished")


def parity_weight(support: tuple[int, ...]) -> int:
    mask = 0
    for left, right in combinations(support, 2):
        delta = (right - left) % 128
        if delta != 64:
            mask ^= 1 << min(delta, 128 - delta)
    return mask.bit_count()


def main() -> None:
    joint: Counter[tuple[int, int]] = Counter()
    examples: dict[tuple[int, int], list[tuple[int, ...]]] = defaultdict(list)
    for tail in combinations(range(1, 128), 3):
        support = (0,) + tail
        key = (hasse_order(support), parity_weight(support))
        joint[key] += 1
        if len(examples[key]) < 3:
            examples[key].append(support)
    print(
        json.dumps(
            {
                "normalized_supports": sum(joint.values()),
                "joint_counts": {
                    f"{valuation},{weight}": count
                    for (valuation, weight), count in sorted(joint.items())
                },
                "weights_by_valuation": {
                    str(valuation): sorted(
                        weight for mu, weight in joint if mu == valuation
                    )
                    for valuation in sorted({mu for mu, _ in joint})
                },
                "examples": {
                    f"{valuation},{weight}": rows
                    for (valuation, weight), rows in sorted(examples.items())
                },
            },
            separators=(",", ":"),
        )
    )


if __name__ == "__main__":
    main()
