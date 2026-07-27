#!/usr/bin/env python3
"""Bound the E=38 weighted Schur-triple problem with CP-SAT on Modal."""

from __future__ import annotations

from collections import Counter

import modal


app = modal.App("e1-e38-weighted-schur-cpsat")
image = modal.Image.debian_slim().pip_install("ortools==9.14.6206")


def representative(residue: int) -> int:
    residue %= 128
    return min(residue, 128 - residue)


@app.function(image=image, cpu=4.0, memory=2048, timeout=60)
def optimize() -> dict[str, object]:
    from ortools.sat.python import cp_model

    model = cp_model.CpModel()
    weights = {
        index: model.new_int_var(0, 2, f"w_{index}") for index in range(1, 64)
    }
    is_one = {
        index: model.new_bool_var(f"one_{index}") for index in range(1, 64)
    }
    is_two = {
        index: model.new_bool_var(f"two_{index}") for index in range(1, 64)
    }
    for index in range(1, 64):
        model.add(weights[index] == is_one[index] + 2 * is_two[index])
        model.add(is_one[index] + is_two[index] <= 1)
    model.add(sum(is_one.values()) == 6)
    model.add(sum(is_two.values()) == 8)

    monomial_counts: Counter[tuple[int, int, int]] = Counter()
    for first in range(128):
        for second in range(128):
            third = (-first - second) % 128
            triple = tuple(
                sorted(
                    (
                        representative(first),
                        representative(second),
                        representative(third),
                    )
                )
            )
            if triple[0] == 0 or 64 in triple:
                continue
            monomial_counts[triple] += 1

    objective_terms = []
    products = []
    for triple, multiplicity in sorted(monomial_counts.items()):
        product = model.new_int_var(0, 8, "p_" + "_".join(map(str, triple)))
        model.add_multiplication_equality(
            product, [weights[index] for index in triple]
        )
        products.append(product)
        objective_terms.append(multiplicity * product)
    objective = sum(objective_terms)
    model.maximize(objective)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 54.0
    solver.parameters.num_search_workers = 4
    solver.parameters.log_search_progress = True
    status = solver.solve(model)
    status_name = solver.status_name(status)
    result: dict[str, object] = {
        "complete": status in (cp_model.OPTIMAL, cp_model.INFEASIBLE),
        "status": status_name,
        "objective": solver.objective_value,
        "best_bound": solver.best_objective_bound,
        "wall_seconds": solver.wall_time,
        "monomials": len(monomial_counts),
    }
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        result["layer_one"] = [
            index for index in range(1, 64) if solver.value(weights[index]) >= 1
        ]
        result["layer_two"] = [
            index for index in range(1, 64) if solver.value(weights[index]) == 2
        ]
    return result


@app.local_entrypoint()
def main() -> None:
    print("E1_E38_WEIGHTED_SCHUR_CPSAT " + repr(optimize.remote()))
