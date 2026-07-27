#!/usr/bin/env python3
"""Test the exact weighted-Schur threshold in six 2-adic CP-SAT shards."""

from __future__ import annotations

from collections import Counter
from itertools import product

import modal


app = modal.App("e1-e38-weighted-schur-threshold")
image = modal.Image.debian_slim().pip_install("ortools==9.14.6206")
THRESHOLD = 2804


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


def evaluate(layer_one: list[int], layer_two: list[int]) -> int:
    weights = {
        index: 2 if index in layer_two else 1 if index in layer_one else 0
        for index in range(1, 64)
    }
    return sum(
        multiplicity * weights[first] * weights[second] * weights[third]
        for (first, second, third), multiplicity in monomial_counter().items()
    )


@app.function(image=image, cpu=2.0, memory=1024, timeout=60)
def solve_shard(minimum_two_valuation: int) -> dict[str, object]:
    from ortools.sat.python import cp_model

    model = cp_model.CpModel()
    is_one = {
        index: model.new_bool_var(f"one_{index}") for index in range(1, 64)
    }
    is_two = {
        index: model.new_bool_var(f"two_{index}") for index in range(1, 64)
    }
    for index in range(1, 64):
        model.add(is_one[index] + is_two[index] <= 1)
        if valuation_two(index) < minimum_two_valuation:
            model.add(is_two[index] == 0)
    model.add(is_two[1 << minimum_two_valuation] == 1)
    model.add(sum(is_one.values()) == 6)
    model.add(sum(is_two.values()) == 8)

    terms = []
    coefficients = []
    product_count = 0
    for triple, multiplicity in sorted(monomial_counter().items()):
        occurrences = Counter(triple)
        indices = sorted(occurrences)
        for categories in product((1, 2), repeat=len(indices)):
            factors = [
                is_one[index] if category == 1 else is_two[index]
                for index, category in zip(indices, categories)
            ]
            coefficient = multiplicity
            for index, category in zip(indices, categories):
                coefficient *= category ** occurrences[index]
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
    solver.parameters.random_seed = 20260727 + minimum_two_valuation
    status = solver.solve(model)
    status_name = solver.status_name(status)
    result: dict[str, object] = {
        "complete": status in (cp_model.OPTIMAL, cp_model.INFEASIBLE),
        "status": status_name,
        "minimum_two_valuation": minimum_two_valuation,
        "wall_seconds": solver.wall_time,
        "monomials": len(monomial_counter()),
        "boolean_products": product_count,
    }
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        layer_one = [
            index
            for index in range(1, 64)
            if solver.value(is_one[index]) or solver.value(is_two[index])
        ]
        layer_two = [
            index for index in range(1, 64) if solver.value(is_two[index])
        ]
        result["layer_one"] = layer_one
        result["layer_two"] = layer_two
        result["objective"] = evaluate(layer_one, layer_two)
    return result


@app.local_entrypoint()
def main() -> None:
    known_one = [8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60]
    known_two = [8, 16, 24, 32, 36, 44, 52, 60]
    assert evaluate(known_one, known_two) == 2718
    print(
        "E1_E38_WEIGHTED_SCHUR_THRESHOLD "
        + repr(list(solve_shard.map(range(6))))
    )
