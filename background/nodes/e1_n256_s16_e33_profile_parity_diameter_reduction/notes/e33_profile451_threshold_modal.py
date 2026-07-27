#!/usr/bin/env python3
"""Threshold-test the symmetric E33 profile-(4,5,1) weighted Schur problem."""

from __future__ import annotations

from collections import Counter
from itertools import product

import modal


app = modal.App("e1-n256-e33-profile451-threshold")
image = modal.Image.debian_slim().pip_install("ortools==9.14.6206")
THRESHOLD = 1733


def representative(residue: int) -> int:
    residue %= 128
    return min(residue, 128 - residue)


def valuation_two(value: int) -> int:
    return (value & -value).bit_length() - 1


def monomial_counter() -> Counter[tuple[int, int, int]]:
    counts: Counter[tuple[int, int, int]] = Counter()
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
            counts[triple] += 1
    return counts


def evaluate(labels: dict[int, int]) -> int:
    return sum(
        multiplicity * labels[first] * labels[second] * labels[third]
        for (first, second, third), multiplicity in monomial_counter().items()
    )


@app.function(image=image, cpu=2.0, memory=1024, timeout=60)
def solve_shard(minimum_support_valuation: int) -> dict[str, object]:
    from ortools.sat.python import cp_model

    model = cp_model.CpModel()
    categories = {
        weight: {
            index: model.new_bool_var(f"w{weight}_{index}")
            for index in range(1, 64)
        }
        for weight in (1, 2, 3)
    }
    for index in range(1, 64):
        model.add(sum(categories[weight][index] for weight in (1,2,3)) <= 1)
        if valuation_two(index) < minimum_support_valuation:
            for weight in (1,2,3):
                model.add(categories[weight][index] == 0)
    model.add(
        sum(categories[weight][1 << minimum_support_valuation] for weight in (1,2,3))
        == 1
    )
    model.add(sum(categories[1].values()) == 4)
    model.add(sum(categories[2].values()) == 5)
    model.add(sum(categories[3].values()) == 1)

    terms = []
    coefficients = []
    product_count = 0
    for triple, multiplicity in sorted(monomial_counter().items()):
        occurrences = Counter(triple)
        indices = sorted(occurrences)
        for assigned_weights in product((1,2,3), repeat=len(indices)):
            factors = [
                categories[weight][index]
                for index, weight in zip(indices, assigned_weights)
            ]
            coefficient = multiplicity
            for index, weight in zip(indices, assigned_weights):
                coefficient *= weight ** occurrences[index]
            if len(factors) == 1:
                term = factors[0]
            else:
                term = model.new_bool_var(f"and_{product_count}")
                product_count += 1
                for factor in factors:
                    model.add(term <= factor)
                model.add(term >= sum(factors) - (len(factors) - 1))
            terms.append(term)
            coefficients.append(coefficient)

    objective = sum(
        coefficient * term for coefficient, term in zip(coefficients, terms)
    )
    model.add(objective >= THRESHOLD)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 54.0
    solver.parameters.num_search_workers = 2
    solver.parameters.random_seed = 330451 + minimum_support_valuation
    status = solver.solve(model)
    result: dict[str, object] = {
        "complete": status in (cp_model.OPTIMAL, cp_model.INFEASIBLE),
        "status": solver.status_name(status),
        "minimum_support_valuation": minimum_support_valuation,
        "wall_seconds": solver.wall_time,
        "monomials": len(monomial_counter()),
        "boolean_products": product_count,
    }
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        labels = {
            index: next(
                (
                    weight
                    for weight in (1,2,3)
                    if solver.value(categories[weight][index])
                ),
                0,
            )
            for index in range(1,64)
        }
        result["objective"] = evaluate(labels)
        result["labels"] = {
            index: weight for index, weight in labels.items() if weight
        }
    return result


@app.local_entrypoint()
def main() -> None:
    print(
        "E33_PROFILE451_THRESHOLD "
        + repr(list(solve_shard.map(range(6))))
    )
