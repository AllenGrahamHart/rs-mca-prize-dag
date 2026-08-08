#!/usr/bin/env python3
"""Census residual targets for the surviving cell-12 positive-DE points."""

import hashlib
import itertools
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
REPLAY = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_parallel_de_four_basis_replay_result.json"
)
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_compact_kernel_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_parallel_de_first_pair_residual_result.json"
)
REMOTE_REPLAY = "/root/replay.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433
MATCHINGS = (
    ((0, 1), (2, 3), (4, 5)),
    ((0, 1), (2, 4), (3, 5)),
    ((0, 1), (2, 5), (3, 4)),
)

app = modal.App("rs-mca-positive-433-1b-cell12-parallel-de-residual")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(REPLAY, REMOTE_REPLAY)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=240, max_containers=16)
def decide(case):
    import sympy as sp

    epsilon_1, epsilon_2, sigma_c, sigma_o = case
    d, e, f = sp.symbols("d e f")
    variables = (d, e, f)
    replay = json.loads(Path(REMOTE_REPLAY).read_text())
    source_row = next(
        row for row in replay["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
        and row["cut_kind"] == "opposite"
    )
    points = source_row["witnesses"]
    if len(points) != 2:
        raise RuntimeError("unexpected source-point count")
    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    kernel_expressions = [
        sp.sympify(item["expression"])
        for item in kernel_payload["rows"][0]["kernel"]
    ]
    t, r, c, b = sp.symbols("t r c b")

    def singular(expression):
        return str(sp.Poly(expression, *variables, modulus=PRIME).as_expr()).replace(
            "**", "^"
        )

    systems = []
    for point_index, point in enumerate(points):
        substitutions = {t: point["t"], r: point["r"],
                         b: point["b"], c: point["c"]}
        kernel = [int(value.subs(substitutions)) % PRIME
                  for value in kernel_expressions]
        a_coefficients, b_coefficients = kernel[:3], kernel[3:6]
        beta_0, beta_1 = kernel[6:]
        missing = point["missing"]
        label = -point["t"]*point["t"] % PRIME
        a_missing = sum(value*pow(label, index, PRIME)
                        for index, value in enumerate(a_coefficients)) % PRIME
        source_sum = (label*pow((beta_0+beta_1*label) % PRIME, 2, PRIME)
                      * pow(a_missing, -2, PRIME)) % PRIME

        def paired(left, right):
            p0, p1, p2 = (
                b_value-left*a_value
                for a_value, b_value in zip(a_coefficients, b_coefficients)
            )
            q0 = b_coefficients[0]-right*a_coefficients[0]
            q1 = -b_coefficients[1]+right*a_coefficients[1]
            q2 = b_coefficients[2]-right*a_coefficients[2]
            return sp.expand(
                (p2*q0-p0*q2)**2-(p2*q1-p1*q2)*(p1*q0-p0*q1)
            )

        records = (
            d*e, -d*e, d*f, sigma_o*e*f,
            point["b"]*f, sigma_c*point["c"]*f,
        )
        representatives = (1, point["b"], point["c"], d, e, f)
        guard = sp.Integer(1)
        for value in representatives:
            guard *= value
        for left, right in itertools.combinations(representatives, 2):
            guard *= (left-right)*(left+right)
        for pairing_index, matching in enumerate(MATCHINGS):
            equations = [d*e-missing, (d+e)**2-source_sum]
            equations.extend(
                paired(records[left], records[right])
                for left, right in matching
            )
            systems.append({
                "point_index": point_index,
                "pairing_index": pairing_index,
                "equations": equations,
                "guard": sp.expand(guard),
            })

    definitions = []
    commands = []
    for index, system in enumerate(systems):
        for equation_index, equation in enumerate(system["equations"]):
            definitions.append(f"poly p{index}_{equation_index}={singular(equation)};")
        definitions.append(f"poly h{index}={singular(system['guard'])};")
        commands.append(
            f"ideal G{index}=p{index}_0,p{index}_1,p{index}_2,p{index}_3,"
            f"p{index}_4,"
            f"z*h{index}-1; G{index}=slimgb(G{index}); "
            f'print("SYS={index},BEGIN"); '
            f'print("DIM="+string(dim(G{index}))); '
            f'print("SIZE="+string(size(G{index}))); '
            f"if ((size(G{index})==1) && (G{index}[1]==1)) "
            f'{{ print("UNIT=1"); }} else {{ print("UNIT=0"); }} '
            f'print("SYS={index},END");'
        )
    program = f"""
ring R={PRIME},(z,d,e,f),dp;
option(redSB);
{chr(10).join(definitions)}
print("BEGIN");
{chr(10).join(commands)}
print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=210,
        )
    except subprocess.TimeoutExpired as error:
        return {
            "epsilon": [epsilon_1, epsilon_2], "sigma": [sigma_c, sigma_o],
            "status": "TIMEOUT", "partial_stdout": (error.stdout or "")[-3000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }
    stdout = process.stdout
    rows = []
    for index, system in enumerate(systems):
        match = re.search(
            rf"SYS={index},BEGIN\nDIM=(-?\d+)\nSIZE=(\d+)\nUNIT=(\d)\n"
            rf"SYS={index},END", stdout,
        )
        rows.append({
            "point_index": system["point_index"],
            "pairing_index": system["pairing_index"],
            "dimension": int(match.group(1)) if match else None,
            "basis_size": int(match.group(2)) if match else None,
            "unit": match.group(3) == "1" if match else None,
        })
    valid = (process.returncode == 0 and "END" in stdout and "?" not in stdout
             and all(row["unit"] is not None for row in rows))
    return {
        "epsilon": [epsilon_1, epsilon_2], "sigma": [sigma_c, sigma_o],
        "status": "COMPLETE" if valid else "ERROR",
        "source_points": len(points), "systems": len(systems),
        "unit_systems": sum(row["unit"] is True for row in rows),
        "nonunit_systems": [row for row in rows if row["unit"] is False],
        "rows": rows,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stdout_tail": stdout[-2000:], "stderr_tail": process.stderr[-1000:],
    }


@app.local_entrypoint()
def main(limit: int = 0):
    cases = tuple(
        (epsilon_1, epsilon_2, sigma_c, sigma_o)
        for epsilon_1 in (-1, 1) for epsilon_2 in (-1, 1)
        for sigma_c in (-1, 1) for sigma_o in (-1, 1)
    )
    if limit:
        cases = cases[:limit]
    raw = list(decide.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]), "sigma": list(case[2:]),
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell12-parallel-de-residual-v1",
        "field": PRIME,
        "scope": (
            "Exact guarded residual census for xi=0 and first-pair matchings "
            "0,1,2 at every surviving P(m,-m) source point."
        ),
        "source_replay_sha256": hashlib.sha256(REPLAY.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT), "cases": len(rows),
        "complete": sum(row.get("status") == "COMPLETE" for row in rows),
        "systems": sum(row.get("systems", 0) for row in rows),
        "unit_systems": sum(row.get("unit_systems", 0) for row in rows),
        "nonunit_systems": sum(len(row.get("nonunit_systems", []))
                               for row in rows),
    }, sort_keys=True))
