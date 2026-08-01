#!/usr/bin/env python3
"""One-cell aligned outside-product ideals for positive 433-1a/O0b.

This is a bounded route pilot, not a fanout driver.  Even its default
reduced-resultant case exhausted the 180-second Modal cap.
"""

import hashlib
import itertools
import json
from pathlib import Path
import subprocess

import modal


APP_NAME = "rs-mca-positive-433-1a-outside-product-singular"
COMPILER = Path(__file__).with_name(
    "rate_half_kb_positive_433_1a_product_base_rank_compiler.py"
)
REMOTE_COMPILER = "/root/rate_half_kb_positive_433_1a_product_base_rank_compiler.py"
PRIME = 2130706433
IOTA = 16711679

app = modal.App(APP_NAME)
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMPILER, REMOTE_COMPILER)
)


def pairings(values):
    values = tuple(values)
    first = values[0]
    for index in range(1, len(values)):
        second = values[index]
        rest = values[1:index] + values[index + 1:]
        yield ((first, second), (rest[0], rest[1]))


def cells():
    output = []
    for singleton in range(5):
        rest = tuple(index for index in range(5) if index != singleton)
        for matching in pairings(rest):
            output.append((singleton, matching))
    return tuple(output)


def perfect_matchings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        second = values[index]
        rest = values[1:index] + values[index + 1:]
        for tail in perfect_matchings(rest):
            yield ((first, second), *tail)


def singular_expression(expression, variables):
    import sympy as sp

    polynomial = sp.Poly(sp.expand(expression), *variables, modulus=PRIME)
    return str(polynomial.as_expr()).replace("**", "^")


@app.function(image=image, cpu=1.0, memory=1024, timeout=180, max_containers=4)
def test_case(case):
    import sympy as sp

    cell, epsilon_1, epsilon_2, cycle_sign, eta_index, matching_index = case
    compiler = subprocess.run(
        ["python3", REMOTE_COMPILER, "--cell", str(cell), "--dump"],
        capture_output=True,
        text=True,
        timeout=40,
    )
    if compiler.returncode:
        return {"case": case, "status": "COMPILER_ERROR", "stderr": compiler.stderr}
    payload = json.loads(compiler.stdout)

    b, c, r, t, d, e, f = sp.symbols("b c r t d e f")
    beta0, beta1, z = sp.symbols("beta0 beta1 z")
    variables = (d, e, f, beta0, beta1, r, t, c, b, z)
    cofactors = [sp.sympify(value) for value in payload["kernel_cofactor_expressions"]]

    singleton, matching = cells()[cell]
    roots = [None] * 5
    roots[matching[0][0]] = sp.Integer(1)
    roots[matching[0][1]] = epsilon_1 * IOTA
    roots[matching[1][0]] = r
    roots[matching[1][1]] = epsilon_2 * IOTA * r
    roots[singleton] = t
    labels = [sp.expand(root**2) for root in roots]
    sums = (0, 1 + b, 1 + b, 1 - b, 1 + c)

    def a2(point):
        return cofactors[0] + cofactors[1] * point + cofactors[2] * point**2

    def a0(point):
        return cofactors[3] + cofactors[4] * point + cofactors[5] * point**2

    def pair_resultant(left, right):
        p0, p1, p2 = [cofactors[3 + index] - left * cofactors[index]
                      for index in range(3)]
        q0 = cofactors[3] - right * cofactors[0]
        q1 = -cofactors[4] + right * cofactors[1]
        q2 = cofactors[5] - right * cofactors[2]
        return ((p2 * q0 - p0 * q2) ** 2
                - (p2 * q1 - p1 * q2) * (p1 * q0 - p0 * q1))

    equations = [
        label * (beta0 + beta1 * label) + root * edge_sum * a2(label)
        for root, label, edge_sum in zip(roots, labels, sums)
    ]
    internal = (d * e, -d * e, d * f, -d * f, cycle_sign * e * f)
    records = [value for index, value in enumerate(internal) if index != eta_index]
    records.extend((b * e, c * f))
    matching_rows = tuple(perfect_matchings(range(6)))
    selected_matching = matching_rows[matching_index]
    equations.append(a0(-t**2) - internal[eta_index] * a2(-t**2))
    for left, right in selected_matching:
        equations.append(pair_resultant(records[left], records[right]))

    guard_factors = [
        r, t, b, c, b**2 - 1, c**2 - 1, b**2 - c**2,
        r**4 - 1, t**4 - 1, t**4 - r**4, d, e, f,
    ]
    target_representatives = (sp.Integer(1), b, c, d, e, f)
    for left, right in itertools.combinations(target_representatives, 2):
        guard_factors.append(left**2 - right**2)
    guard_factors.extend(a2(label) for label in labels)
    guard_factors.append(a2(-t**2))

    singular_equations = [singular_expression(value, variables) for value in equations]
    singular_guard = "*".join(
        f"({singular_expression(value, variables)})" for value in guard_factors
    )
    program = [
        f"ring q={PRIME},(d,e,f,beta0,beta1,r,t,c,b,z),dp;",
        "option(redSB);",
    ]
    program.extend(f"poly f{index}={value};"
                   for index, value in enumerate(singular_equations))
    program.extend([
        f"ideal I={','.join(f'f{index}' for index in range(len(equations)))},z*({singular_guard})-1;",
        "ideal G=std(I);",
        'if (reduce(1,G)==0) { print("UNIT"); } else { print("NONUNIT"); }',
        "print(size(G));",
        "G[1];",
        "quit;",
    ])
    try:
        process = subprocess.run(
            ["Singular", "-q"],
            input="\n".join(program),
            capture_output=True,
            text=True,
            timeout=130,
        )
    except subprocess.TimeoutExpired as error:
        return {"case": case, "status": "TIMEOUT",
                "stdout": error.stdout or "", "stderr": error.stderr or ""}
    return {
        "case": case,
        "status": "COMPLETE" if process.returncode == 0 else "SINGULAR_ERROR",
        "equation_count": len(equations),
        "matching": selected_matching,
        "program_sha256": hashlib.sha256("\n".join(program).encode()).hexdigest(),
        "stdout": process.stdout[-2000:],
        "stderr": process.stderr[-2000:],
    }


@app.local_entrypoint()
def main(
    cell: int = 3,
    epsilon_1: int = -1,
    epsilon_2: int = -1,
    cycle_sign: int = -1,
    eta_index: int = 0,
    matching_index: int = 0,
):
    case = (cell, epsilon_1, epsilon_2, cycle_sign, eta_index, matching_index)
    print(json.dumps(test_case.remote(case), sort_keys=True))
