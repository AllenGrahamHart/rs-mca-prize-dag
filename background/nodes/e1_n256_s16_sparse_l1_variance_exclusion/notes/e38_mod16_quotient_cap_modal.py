#!/usr/bin/env python3
"""Optimize the exact mod-16 residue-capacity upper bound for E=38."""

from __future__ import annotations

import modal


app = modal.App("e1-e38-mod16-quotient-cap")
image = modal.Image.debian_slim().pip_install("ortools==9.14.6206")


@app.function(image=image, cpu=4.0, memory=1024, timeout=60)
def optimize(require_odd: bool = False) -> dict[str, object]:
    from ortools.sat.python import cp_model

    model = cp_model.CpModel()
    modulus = 16
    orbit_types = [(0, 0, 3), *[(r, modulus - r, 8) for r in range(1, 8)], (8, 8, 4)]
    ones = []
    twos = []
    for index, (_, _, capacity) in enumerate(orbit_types):
        one = model.new_int_var(0, min(6, capacity), f"one_{index}")
        two = model.new_int_var(0, min(8, capacity), f"two_{index}")
        model.add(one + two <= capacity)
        ones.append(one)
        twos.append(two)
    model.add(sum(ones) == 6)
    model.add(sum(twos) == 8)

    outer = [model.new_int_var(0, 28, f"A_{r}") for r in range(modulus)]
    inner = [model.new_int_var(0, 16, f"B_{r}") for r in range(modulus)]
    outer_terms: list[list[object]] = [[] for _ in range(modulus)]
    inner_terms: list[list[object]] = [[] for _ in range(modulus)]
    for index, (left, right, _) in enumerate(orbit_types):
        if left == right:
            outer_terms[left].append(2 * (ones[index] + twos[index]))
            inner_terms[left].append(2 * twos[index])
        else:
            for residue in (left, right):
                outer_terms[residue].append(ones[index] + twos[index])
                inner_terms[residue].append(twos[index])
    for residue in range(modulus):
        model.add(outer[residue] == sum(outer_terms[residue]))
        model.add(inner[residue] == sum(inner_terms[residue]))

    if require_odd:
        model.add(sum(outer[r] for r in range(modulus) if r % 2) >= 2)
    else:
        model.add(sum(outer[r] for r in range(modulus) if r % 4) >= 2)

    vectors = {"A": outer, "B": inner}
    totals = {"A": 28, "B": 16}
    product_cache: dict[tuple[str, str, int, int], object] = {}
    minimum_cache: dict[tuple[str, str, int, int], object] = {}

    def product_var(left_name: str, right_name: str, left_index: int, right_index: int):
        key = (left_name, right_name, left_index, right_index)
        if key not in product_cache:
            left = vectors[left_name][left_index]
            right = vectors[right_name][right_index]
            value = model.new_int_var(0, totals[left_name] * totals[right_name], "mul_" + "_".join(map(str, key)))
            model.add_multiplication_equality(value, [left, right])
            product_cache[key] = value
        return product_cache[key]

    def minimum_var(left_name: str, right_name: str, left_index: int, right_index: int):
        key = (left_name, right_name, left_index, right_index)
        if key not in minimum_cache:
            value = model.new_int_var(0, min(totals[left_name], totals[right_name]), "min_" + "_".join(map(str, key)))
            model.add_min_equality(
                value,
                [vectors[left_name][left_index], vectors[right_name][right_index]],
            )
            minimum_cache[key] = value
        return minimum_cache[key]

    def pair_bound(left_name: str, right_name: str, target_name: str, tag: str):
        contributions = []
        for target_residue in range(modulus):
            pair_terms = []
            capacity_terms = []
            for left_residue in range(modulus):
                right_residue = (-target_residue - left_residue) % modulus
                pair_terms.append(
                    product_var(left_name, right_name, left_residue, right_residue)
                )
                capacity_terms.append(
                    minimum_var(left_name, right_name, left_residue, right_residue)
                )
            pair_maximum = totals[left_name] * totals[right_name]
            pair_count = model.new_int_var(0, pair_maximum, f"pairs_{tag}_{target_residue}")
            zero_pairs = min(totals[left_name], totals[right_name]) if target_residue == 0 else 0
            model.add(pair_count == sum(pair_terms) - zero_pairs)
            capacity = model.new_int_var(0, modulus * min(totals[left_name], totals[right_name]), f"capacity_{tag}_{target_residue}")
            model.add(capacity == sum(capacity_terms))
            target_capacity = model.new_int_var(0, totals[target_name] * modulus * min(totals[left_name], totals[right_name]), f"target_capacity_{tag}_{target_residue}")
            model.add_multiplication_equality(
                target_capacity,
                [vectors[target_name][target_residue], capacity],
            )
            contribution = model.new_int_var(0, pair_maximum, f"contribution_{tag}_{target_residue}")
            model.add_min_equality(contribution, [pair_count, target_capacity])
            contributions.append(contribution)
        bound = model.new_int_var(0, totals[left_name] * totals[right_name], f"bound_{tag}")
        model.add(bound == sum(contributions))
        return bound

    bound_aaa = pair_bound("A", "A", "A", "AAA")
    bound_aab_aa = pair_bound("A", "A", "B", "AAB_AA")
    bound_aab_ab = pair_bound("A", "B", "A", "AAB_AB")
    bound_abb_ab = pair_bound("A", "B", "B", "ABB_AB")
    bound_abb_bb = pair_bound("B", "B", "A", "ABB_BB")
    bound_bbb = pair_bound("B", "B", "B", "BBB")

    cap_aab = model.new_int_var(0, 28 * 28, "cap_AAB")
    cap_abb = model.new_int_var(0, 28 * 16, "cap_ABB")
    model.add_min_equality(cap_aab, [bound_aab_aa, bound_aab_ab])
    model.add_min_equality(cap_abb, [bound_abb_ab, bound_abb_bb])
    objective = bound_aaa + 3 * cap_aab + 3 * cap_abb + bound_bbb
    model.maximize(objective)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 54.0
    solver.parameters.num_search_workers = 4
    solver.parameters.random_seed = 20260727
    status = solver.solve(model)
    result: dict[str, object] = {
        "complete": status == cp_model.OPTIMAL,
        "require_odd": require_odd,
        "status": solver.status_name(status),
        "objective": solver.objective_value,
        "best_bound": solver.best_objective_bound,
        "wall_seconds": solver.wall_time,
    }
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        result.update(
            {
                "ones": [solver.value(value) for value in ones],
                "twos": [solver.value(value) for value in twos],
                "outer": [solver.value(value) for value in outer],
                "inner": [solver.value(value) for value in inner],
                "components": [
                    solver.value(bound_aaa),
                    solver.value(cap_aab),
                    solver.value(cap_abb),
                    solver.value(bound_bbb),
                ],
            }
        )
    return result


@app.local_entrypoint()
def main(require_odd: bool = False) -> None:
    print("E1_E38_MOD16_QUOTIENT_CAP " + repr(optimize.remote(require_odd)))
