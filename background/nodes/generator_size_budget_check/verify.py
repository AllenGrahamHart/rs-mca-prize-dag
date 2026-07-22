#!/usr/bin/env python3
"""Exact count and toy padding audit for the signed-8-core route."""

from __future__ import annotations

from itertools import combinations
from math import comb


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def reduced_sum(exponents: set[int], order: int) -> tuple[int, ...]:
    half = order // 2
    out = [0] * half
    for exponent in exponents:
        if exponent < half:
            out[exponent] += 1
        else:
            out[exponent - half] -= 1
    return tuple(out)


def check_toy_padding_collision() -> None:
    order = 32
    pair_count = order // 2
    core_pairs = tuple(range(8))
    core = {index for index in core_pairs}
    remaining = tuple(range(8, pair_count))
    values = set()
    subsets = set()
    for padding in combinations(remaining, 4):
        subset = set(core)
        for index in padding:
            subset.update((index, index + pair_count))
        require(len(subset) == order // 2, "toy subset has wrong size")
        subsets.add(tuple(sorted(subset)))
        values.add(reduced_sum(subset, order))
    require(len(subsets) == comb(8, 4), "toy padding count failed")
    require(len(values) == 1, "antipodal paddings changed the core sum")


def main() -> None:
    target = 1 << 89
    supports = comb(64, 8)
    paddings = comb(56, 28)
    raw_count = 19 * supports * paddings
    named_center_bound = 19 * supports
    all_sign_center_bound = (1 << 8) * supports

    require(raw_count > target, "raw proposal does not cross its printed target")
    require(named_center_bound < target, "named signed cores unexpectedly meet target")
    require(all_sign_center_bound < target, "all signed cores unexpectedly meet target")
    require(raw_count == named_center_bound * paddings, "raw factorization failed")
    require(paddings > 1, "padding does not create duplicate subsets")
    check_toy_padding_collision()

    print(
        "GENERATOR_SIZE_BUDGET_CHECK_REFUTED "
        f"raw={raw_count} named_centers<={named_center_bound} "
        f"all_sign_centers<={all_sign_center_bound} padding_multiplicity={paddings}"
    )


if __name__ == "__main__":
    main()


def _status_pin() -> None:
    # M8 guard (wave-20 audit): the refutation is a dag-level fact; a silent
    # REFUTED -> PROVED resurrection must trip this verifier.
    import json
    from pathlib import Path
    root = Path(__file__).resolve().parents[3]
    dag = json.loads((root / "dag.json").read_text())
    status = next(n["status"] for n in dag["nodes"]
                  if n["id"] == "generator_size_budget_check")
    assert status == "REFUTED", f"status pin: expected REFUTED, found {status}"


_status_pin()
