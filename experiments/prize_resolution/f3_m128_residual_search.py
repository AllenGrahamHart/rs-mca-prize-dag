#!/usr/bin/env python3
"""Low-memory adversarial search for the m=128 HGE4 Haar residual."""

import argparse
from dataclasses import dataclass
from math import comb, log2
from random import Random


M = 128
AMBIENT_EXPONENT = 13
TAYLOR_CAP = 8


@dataclass
class Record:
    gap: float
    mask: int
    nu: int
    energies: tuple[int, ...]
    support: tuple[int, ...]


def taylor_multiplicity_mod_two(occupied):
    for degree in range(1, TAYLOR_CAP):
        if sum(comb(exponent, degree) for exponent in occupied) & 1:
            return degree
    return TAYLOR_CAP


def evaluate(plus, minus, h):
    values = [0] * M
    for exponent in plus:
        values[exponent] = 1
    for exponent in minus:
        values[exponent] = -1

    half = M // 2
    q_values = [values[index] + values[index + half] for index in range(half)]
    odd_energy = sum(
        (values[index] - values[index + half]) ** 2 for index in range(half)
    )

    haar = []
    folded = q_values
    levels = ((h - 1) // 2).bit_length()
    for _ in range(levels):
        midpoint = len(folded) // 2
        haar.append(
            sum(
                (folded[index] - folded[index + midpoint]) ** 2
                for index in range(midpoint)
            )
        )
        folded = [
            folded[index] + folded[index + midpoint]
            for index in range(midpoint)
        ]

    positive = [index for index, energy in enumerate(haar) if energy]
    mask = sum(1 << index for index in positive)
    zero = [index for index, energy in enumerate(haar) if not energy]
    orders = [M // (1 << (index + 1)) for index in range(levels)]
    norm_orders = [M] + [orders[index] for index in positive]

    H = (h - 1) // 2
    r_values = [((H // (1 << index)) + 1) // 2 for index in range(levels)]
    row_exponent = h // 2 + sum(r_values[index] for index in positive)
    structural_two = sum(
        min(order, orders[index]) // 2
        for order in norm_orders
        for index in zero
    )

    occupied = tuple(sorted(plus + minus))
    nu = taylor_multiplicity_mod_two(occupied)
    taylor_two = sum(min(nu, order // 2) for order in norm_orders)

    if odd_energy == 0 or any(haar[index] == 0 for index in positive):
        upper_log = float("-inf")
    else:
        upper_log = (M // 4) * log2(odd_energy)
        for index in positive:
            upper_log += (orders[index] // 4) * log2(haar[index])

    # Structural cyclotomic factors and Taylor multiplicity both measure the
    # unique 2-adic prime.  They are alternative lower bounds, not additive.
    balanced_structural_two = structural_two + len(norm_orders)
    lower_log = max(balanced_structural_two, taylor_two) + (
        2 * AMBIENT_EXPONENT * row_exponent
    )
    return Record(
        gap=upper_log - lower_log,
        mask=mask,
        nu=nu,
        energies=(odd_energy, *haar),
        support=occupied,
    )


def search(h, trials, seed):
    rng = Random(seed + h)
    best = None
    best_by_mask = {}
    for _ in range(trials):
        occupied = rng.sample(range(M), 2 * h)
        rng.shuffle(occupied)
        record = evaluate(occupied[:h], occupied[h:], h)
        if best is None or record.gap > best.gap:
            best = record
        old = best_by_mask.get(record.mask)
        if old is None or record.gap > old.gap:
            best_by_mask[record.mask] = record
    return best, best_by_mask


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=20_000)
    parser.add_argument("--seed", type=int, default=20260727)
    args = parser.parse_args()

    for h in range(4, 12):
        best, by_mask = search(h, args.trials, args.seed)
        masks = ",".join(
            f"{mask:0{((h - 1) // 2).bit_length()}b}:{record.gap:.3f}"
            for mask, record in sorted(by_mask.items())
        )
        print(
            f"h={h} best_gap={best.gap:.6f} mask={best.mask:b} "
            f"nu={best.nu} energies={best.energies} masks=[{masks}]"
        )


if __name__ == "__main__":
    main()
