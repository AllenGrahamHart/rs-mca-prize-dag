#!/usr/bin/env python3
"""Count realized energy-five parity masks and odd-unit lag orbits."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
import json


UNITS = tuple(range(1, 128, 2))


def folded_lag(left: int, right: int) -> int | None:
    delta = (right - left) % 128
    if delta == 64:
        return None
    return min(delta, 128 - delta)


def parity_mask(support: tuple[int, ...]) -> tuple[int, ...]:
    mask = set()
    for left, right in combinations(support, 2):
        lag = folded_lag(left, right)
        if lag is not None:
            if lag in mask:
                mask.remove(lag)
            else:
                mask.add(lag)
    return tuple(sorted(mask))


def hasse_order(support: tuple[int, ...]) -> int:
    residues = Counter(position % 32 for position in support)
    live = tuple(residue for residue, count in residues.items() if count & 1)
    if not live:
        return 32
    for derivative in range(32):
        if sum((derivative & ~residue) == 0 for residue in live) & 1:
            return derivative
    raise AssertionError


def transport(mask: tuple[int, ...], unit: int) -> tuple[int, ...]:
    return tuple(sorted(min((unit * lag) % 128, 128 - (unit * lag) % 128) for lag in mask))


def canonical(mask: tuple[int, ...]) -> tuple[int, ...]:
    return min(transport(mask, unit) for unit in UNITS)


def main() -> None:
    masks_by_weight: dict[int, set[tuple[int, ...]]] = defaultdict(set)
    valuations_by_mask: dict[tuple[int, ...], set[int]] = defaultdict(set)
    support_counts = Counter()
    for tail in combinations(range(1, 128), 3):
        support = (0,) + tail
        mask = parity_mask(support)
        if len(mask) not in (1, 5):
            continue
        valuation = hasse_order(support)
        masks_by_weight[len(mask)].add(mask)
        valuations_by_mask[mask].add(valuation)
        support_counts[(len(mask), valuation)] += 1

    packet = {
        "unique_masks": {str(weight): len(masks) for weight, masks in sorted(masks_by_weight.items())},
        "unit_orbits": {
            str(weight): len({canonical(mask) for mask in masks})
            for weight, masks in sorted(masks_by_weight.items())
        },
        "orbit_sizes": {
            str(weight): dict(
                sorted(
                    Counter(
                        sum(transport(mask, unit) == mask for unit in UNITS)
                        for mask in {canonical(row) for row in masks}
                    ).items()
                )
            )
            for weight, masks in sorted(masks_by_weight.items())
        },
        "valuation_sets": {
            str(weight): sorted(
                {valuation for mask in masks for valuation in valuations_by_mask[mask]}
            )
            for weight, masks in sorted(masks_by_weight.items())
        },
        "support_counts": {
            f"{weight},{valuation}": count
            for (weight, valuation), count in sorted(support_counts.items())
        },
        "canonical_masks": {
            str(weight): sorted([list(mask) for mask in {canonical(row) for row in masks}])
            for weight, masks in sorted(masks_by_weight.items())
        },
    }
    print(json.dumps(packet, separators=(",", ":")))


if __name__ == "__main__":
    main()
