#!/usr/bin/env python3
"""Map the relaxed-slack plus layered-cubic route below E=41."""

from __future__ import annotations

import modal


app = modal.App("e1-n256-low-energy-layer-route")
image = modal.Image.debian_slim().pip_install("sympy")


@app.function(image=image, cpu=1.0, memory=512, timeout=60)
def derive() -> dict[str, object]:
    import itertools

    import sympy as sp

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

    def relaxed_minimum_energies(maximum_slack: int) -> list[int | None]:
        class_types = set()
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
                        if 0 < slack <= maximum_slack:
                            class_types.add((slack, count_2, count_1, class_sum))

        answers = []
        for target_slack in range(maximum_slack + 1):
            best = None
            for diameter_2 in range(4):
                for diameter_1 in range(3):
                    if diameter_2 + 2 * diameter_1 > 4:
                        continue
                    if diameter_1 + diameter_2 > 3:
                        continue
                    diameter_slack = 4 * diameter_2 + 3 * diameter_1
                    if diameter_slack > target_slack:
                        continue
                    target = target_slack - diameter_slack
                    states = {(0, 0, 0): 0}
                    for used_slack in range(target + 1):
                        current = [
                            item for item in states.items() if item[0][0] == used_slack
                        ]
                        for (state_slack, used_2, used_1), state_energy in current:
                            for slack, count_2, count_1, class_sum in class_types:
                                new_state = (
                                    state_slack + slack,
                                    used_2 + count_2,
                                    used_1 + count_1,
                                )
                                if new_state[0] > target:
                                    continue
                                if new_state[1] > 12 - diameter_2:
                                    continue
                                if new_state[2] > 6 - diameter_1:
                                    continue
                                new_energy = state_energy + class_sum * class_sum
                                states[new_state] = min(
                                    states.get(new_state, new_energy), new_energy
                                )
                    for (state_slack, used_2, used_1), state_energy in states.items():
                        if state_slack != target:
                            continue
                        total_energy = (
                            state_energy
                            + 4 * (12 - diameter_2 - used_2)
                            + (6 - diameter_1 - used_1)
                        )
                        best = total_energy if best is None else min(best, total_energy)
            answers.append(best)
        return answers

    def layer_cap(counts: tuple[int, ...]) -> int:
        sizes = [
            2 * sum(counts[level:])
            for level in range(len(counts))
            if sum(counts[level:])
        ]
        return sum(
            min(
                first * second - min(first, second),
                first * third - min(first, third),
                second * third - min(second, third),
            )
            for first, second, third in itertools.product(sizes, repeat=3)
        )

    relaxed = relaxed_minimum_energies(64)

    y = sp.symbols("y")
    log_a, log_b = sp.symbols("log_a log_b")
    coefficient_symbols = sp.symbols("c0:4")
    polynomial = sum(
        coefficient_symbols[index] * y**index for index in range(4)
    )
    hermite_candidates = []
    for left in range(10, 17):
        for right in range(40, 65):
            solution = sp.solve(
                (
                    sp.Eq(polynomial.subs(y, left), log_a),
                    sp.Eq(
                        sp.diff(polynomial, y).subs(y, left),
                        sp.Rational(1, left),
                    ),
                    sp.Eq(polynomial.subs(y, right), log_b),
                    sp.Eq(
                        sp.diff(polynomial, y).subs(y, right),
                        sp.Rational(1, right),
                    ),
                ),
                coefficient_symbols,
                rational=True,
            )
            exact_leading = solution[coefficient_symbols[3]].subs(
                {log_a: sp.log(left), log_b: sp.log(right)}
            )
            if exact_leading <= 0:
                continue
            hermite_candidates.append((left, right, solution))

    target = sp.Rational(125, 32) * sp.log(2)
    rows = []
    for energy in range(40, 19, -1):
        base_l1 = (energy + 66) // 4
        l1_ceiling = None
        l1_trace = []
        for l1_norm in range(base_l1, -1, -1):
            slack = energy + 66 - 4 * l1_norm
            minimum_energy = relaxed[slack]
            l1_trace.append((l1_norm, slack, minimum_energy))
            if minimum_energy is not None and minimum_energy <= energy:
                l1_ceiling = l1_norm
                break
        if l1_ceiling is None:
            raise AssertionError(f"no relaxed support at energy {energy}")

        profiles = []
        for counts in itertools.product(
            range(43), range(11), range(5), range(3), range(2), range(2)
        ):
            profile_l1 = sum(
                (index + 1) * count for index, count in enumerate(counts)
            )
            profile_energy = sum(
                (index + 1) ** 2 * count for index, count in enumerate(counts)
            )
            if (
                profile_energy == energy
                and profile_l1 <= l1_ceiling
                and sum(counts) <= 21
            ):
                profiles.append((layer_cap(counts), counts, profile_l1))
        third_moment_cap, worst_profile, worst_l1 = max(profiles)
        variance = 2 * energy
        raw_second = 16**2 + variance
        raw_third = 16**3 + 3 * 16 * variance + third_moment_cap

        best = None
        for left, right, solution in hermite_candidates:
            expected = sp.expand(
                solution[coefficient_symbols[0]]
                + 16 * solution[coefficient_symbols[1]]
                + raw_second * solution[coefficient_symbols[2]]
                + raw_third * solution[coefficient_symbols[3]]
            )
            exact_expected = expected.subs(
                {log_a: sp.log(left), log_b: sp.log(right)}
            )
            margin = target - exact_expected
            candidate = {
                "left": left,
                "right": right,
                "margin": str(sp.N(margin, 50)),
                "numeric_margin": float(margin),
                "expected_expression": str(expected),
                "leading_expression": str(solution[coefficient_symbols[3]]),
                "coefficients": [
                    str(solution[symbol]) for symbol in coefficient_symbols
                ],
            }
            if best is None or candidate["numeric_margin"] > best["numeric_margin"]:
                best = candidate
        rows.append(
            {
                "energy": energy,
                "variance": variance,
                "base_l1": base_l1,
                "l1_ceiling": l1_ceiling,
                "l1_trace": l1_trace,
                "profile_count": len(profiles),
                "third_moment_cap": third_moment_cap,
                "worst_profile": worst_profile,
                "worst_profile_l1": worst_l1,
                "best_hermite": best,
                "route_closes": bool(best and best["numeric_margin"] > 0),
            }
        )

    return {
        "complete": True,
        "relaxed_table_0_through_32": relaxed[:33],
        "hermite_candidate_count": len(hermite_candidates),
        "rows": rows,
    }


@app.local_entrypoint()
def main() -> None:
    print("E1_N256_LOW_ENERGY_LAYER_ROUTE " + repr(derive.remote()))
