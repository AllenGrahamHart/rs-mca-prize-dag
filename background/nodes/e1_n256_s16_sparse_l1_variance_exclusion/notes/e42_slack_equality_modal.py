#!/usr/bin/env python3
"""Enumerate equality signatures in the relaxed E=42, L=24 slack ledger."""

from __future__ import annotations

import modal


app = modal.App("e1-n256-e42-slack-equality")
image = modal.Image.debian_slim()


@app.function(image=image, cpu=1.0, memory=256, timeout=60)
def enumerate_equalities() -> dict[str, object]:
    from functools import lru_cache

    def attainable_sums(count_4: int, count_2: int, count_1: int) -> set[int]:
        sums = {0}
        for value, count in ((4, count_4), (2, count_2), (1, count_1)):
            for _ in range(count):
                sums = {
                    current + sign * value
                    for current in sums
                    for sign in (-1, 1)
                }
        return {abs(value) for value in sums}

    b_options: dict[tuple[int, int, int, int], list[int]] = {}
    for count_4 in range(4):
        for count_2 in range(13):
            for count_1 in range(7):
                if count_4 + count_2 + count_1 == 0:
                    continue
                for class_sum in attainable_sums(count_4, count_2, count_1):
                    slack = (
                        (class_sum - 2) ** 2
                        + 4 * count_2
                        + 3 * count_1
                        - 4
                    )
                    if 0 < slack <= 12:
                        key = (slack, count_2, count_1, class_sum)
                        b_options.setdefault(key, []).append(count_4)

    class_types = sorted(b_options)
    solutions: list[dict[str, object]] = []

    for diameter_2 in range(4):
        for diameter_1 in range(3):
            if diameter_2 + 2 * diameter_1 > 4:
                continue
            if diameter_1 + diameter_2 > 3:
                continue
            class_slack = 12 - 4 * diameter_2 - 3 * diameter_1
            if class_slack < 0:
                continue

            @lru_cache(maxsize=None)
            def search(
                start: int,
                remaining_slack: int,
                remaining_2: int,
                remaining_1: int,
                remaining_energy: int,
            ) -> tuple[tuple[int, ...], ...]:
                if remaining_slack == 0:
                    return ((),) if remaining_energy == 0 else ()
                found: list[tuple[int, ...]] = []
                for index in range(start, len(class_types)):
                    slack, count_2, count_1, class_sum = class_types[index]
                    energy = class_sum * class_sum - 4 * count_2 - count_1
                    if slack > remaining_slack:
                        break
                    if count_2 > remaining_2 or count_1 > remaining_1:
                        continue
                    for suffix in search(
                        index,
                        remaining_slack - slack,
                        remaining_2 - count_2,
                        remaining_1 - count_1,
                        remaining_energy - energy,
                    ):
                        found.append((index,) + suffix)
                return tuple(found)

            baseline = 4 * (12 - diameter_2) + (6 - diameter_1)
            for indices in search(
                0,
                class_slack,
                12 - diameter_2,
                6 - diameter_1,
                42 - baseline,
            ):
                pattern = [class_types[index] for index in indices]
                solutions.append(
                    {
                        "diameter_2": diameter_2,
                        "diameter_1": diameter_1,
                        "classes": pattern,
                        "magnitude_4_options": [
                            sorted(set(b_options[class_type]))
                            for class_type in pattern
                        ],
                    }
                )

    return {
        "complete": True,
        "target": {"energy": 42, "l1_norm": 24, "slack": 12},
        "class_type_count": len(class_types),
        "solution_count": len(solutions),
        "solutions": solutions,
    }


@app.local_entrypoint()
def main() -> None:
    print("E1_N256_E42_SLACK_EQUALITY " + repr(enumerate_equalities.remote()))
