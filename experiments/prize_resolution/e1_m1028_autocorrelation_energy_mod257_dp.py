#!/usr/bin/env python3
"""Exact low-energy DP for the cofactor-1028 autocorrelation congruence."""

from __future__ import annotations


MODULUS = 257
ROOT = 3
SQUARE_MASS = 18
ENERGY_CAP = 17


def main() -> None:
    assert pow(ROOT, 128, MODULUS) == MODULUS - 1
    assert pow(ROOT, 256, MODULUS) == 1

    traces = [([ENERGY_CAP + 1] * MODULUS) for _ in range(64)]
    traces[0][0] = 0
    parents: list[list[tuple[int, int] | None]] = [
        [None] * MODULUS for _ in range(64)
    ]

    for lag in range(1, 64):
        coefficient = (
            pow(ROOT, lag, MODULUS) + pow(ROOT, -lag, MODULUS)
        ) % MODULUS
        previous = traces[lag - 1]
        current = traces[lag]
        for residue, old_energy in enumerate(previous):
            if old_energy > ENERGY_CAP:
                continue
            for value in range(-4, 5):
                new_energy = old_energy + value * value
                if new_energy > ENERGY_CAP:
                    continue
                new_residue = (residue + coefficient * value) % MODULUS
                if new_energy < current[new_residue]:
                    current[new_residue] = new_energy
                    parents[lag][new_residue] = (residue, value)

    target = -SQUARE_MASS % MODULUS
    target_energy = traces[63][target]
    witness: list[tuple[int, int]] = []
    if target_energy <= ENERGY_CAP:
        residue = target
        for lag in range(63, 0, -1):
            parent = parents[lag][residue]
            assert parent is not None
            old_residue, value = parent
            if value:
                witness.append((lag, value))
            residue = old_residue
        witness.reverse()
        assert residue == 0
        assert sum(value * value for _, value in witness) == target_energy

    reachable_counts = [
        sum(energy <= cap for energy in traces[63])
        for cap in range(ENERGY_CAP + 1)
    ]
    print(
        "E1_M1028_AUTOCORRELATION_ENERGY_MOD257_DP_DONE "
        f"target={target} cap={ENERGY_CAP} "
        f"target_reachable={str(target_energy <= ENERGY_CAP).lower()} "
        f"target_energy={target_energy} "
        f"reachable_at_cap={reachable_counts[-1]}"
    )
    print(f"target_witness={witness}")
    print(f"reachable_counts={reachable_counts}")


if __name__ == "__main__":
    main()
