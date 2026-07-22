#!/usr/bin/env python3
"""Bounded CP-SAT falsifier for the (p,n,m,h)=(31,128,4,3) analogue.

The exact colored-code equivalence gives 128 variables in
{0,1,omega,omega^2}, with 31 occurrences of each nonzero color and 35 zeros.
Both the word and its coefficientwise square must have Fourier zeros through
frequency 30 over GF(31^4). The model expands every field equation into four
linear congruences modulo 31.

FEASIBLE emits a replayed three-fiber witness. INFEASIBLE is finite analogue
evidence only. UNKNOWN changes nothing. Resources: two CPUs, 2 GiB, one
container, 60 seconds; the solver itself is capped at 45 seconds.
"""

from __future__ import annotations

import modal


app = modal.App("l1-m4-h3-two-schur-cpsat")
image = modal.Image.debian_slim(python_version="3.12").pip_install(
    "galois==0.4.7", "ortools==9.14.6206"
)


@app.function(image=image, cpu=2.0, memory=2048, timeout=60)
def solve() -> dict[str, object]:
    import galois
    from ortools.sat.python import cp_model

    p, n = 31, 128
    values = (0, 1, 5, 25)
    squares = tuple(value * value % p for value in values)
    field = galois.GF(p**4)
    zeta = field.primitive_element ** ((field.order - 1) // n)
    assert zeta.multiplicative_order() == n

    coefficients: list[list[tuple[int, ...]]] = []
    for exponent in range(1, p):
        row = []
        for index in range(n):
            vector = tuple(int(item) for item in (zeta ** (exponent * index)).vector())
            assert len(vector) == 4
            row.append(vector)
        coefficients.append(row)

    model = cp_model.CpModel()
    choice = [[model.NewBoolVar(f"x_{index}_{color}") for color in range(4)]
              for index in range(n)]
    for row in choice:
        model.AddExactlyOne(row)
    model.Add(sum(choice[index][0] for index in range(n)) == p + 4)
    for color in range(1, 4):
        model.Add(sum(choice[index][color] for index in range(n)) == p)

    # Rotation and cube-root scaling put one color-1 point at exponent zero.
    model.Add(choice[0][1] == 1)

    for exponent_row in coefficients:
        for coordinate in range(4):
            linear_terms = [
                (exponent_row[index][coordinate] * values[color]) % p
                * choice[index][color]
                for index in range(n) for color in range(1, 4)
            ]
            square_terms = [
                (exponent_row[index][coordinate] * squares[color]) % p
                * choice[index][color]
                for index in range(n) for color in range(1, 4)
            ]
            total = model.NewIntVar(0, n * (p - 1), "moment_sum")
            square_total = model.NewIntVar(0, n * (p - 1), "square_moment_sum")
            model.Add(total == sum(linear_terms))
            model.Add(square_total == sum(square_terms))
            model.AddModuloEquality(0, total, p)
            model.AddModuloEquality(0, square_total, p)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 45.0
    solver.parameters.num_search_workers = 2
    solver.parameters.random_seed = 1
    validation = model.Validate()
    if validation:
        return {"status": "MODEL_INVALID", "validation": validation}
    status = solver.Solve(model)
    status_name = solver.StatusName(status)
    output: dict[str, object] = {
        "status": status_name,
        "wall_seconds": solver.WallTime(),
        "branches": solver.NumBranches(),
        "conflicts": solver.NumConflicts(),
    }

    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        colors = [next(color for color in range(4)
                       if solver.Value(choice[index][color]))
                  for index in range(n)]
        classes = [[index for index, color in enumerate(colors) if color == wanted]
                   for wanted in range(4)]
        for exponent in range(p):
            first = field(0)
            second = field(0)
            for index, color in enumerate(colors):
                first += field(values[color]) * zeta ** (exponent * index)
                second += field(squares[color]) * zeta ** (exponent * index)
            assert first == 0 and second == 0
        assert [len(group) for group in classes] == [35, 31, 31, 31]
        output["classes"] = classes
        output["zeta"] = int(zeta)
        output["replay"] = "PASS"
    return output


@app.local_entrypoint()
def main() -> None:
    import json

    result = solve.remote()
    print(json.dumps(result, sort_keys=True))
