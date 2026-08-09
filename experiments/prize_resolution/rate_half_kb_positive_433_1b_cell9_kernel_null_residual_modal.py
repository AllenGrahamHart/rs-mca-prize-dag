#!/usr/bin/env python3
"""Test every residual target matching at the cell-9 kernel-null points."""

import hashlib
import itertools
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
REPLAY = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_endpoint_replay_result.json"
)
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_compact_kernel_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_kernel_null_residual_result.json"
)
REMOTE_REPLAY = "/root/replay.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433
IOTA = 16711679

app = modal.App("rs-mca-positive-433-1b-cell9-kernel-null-residual")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(REPLAY, REMOTE_REPLAY)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        second = values[index]
        rest = values[1:index] + values[index + 1:]
        for tail in pairings(rest):
            yield ((first, second),) + tail


MATCHINGS = tuple(pairings(range(6)))


def rank_kernel(rows):
    matrix = [[value % PRIME for value in row] for row in rows]
    pivot_columns = []
    pivot_row = 0
    for column in range(len(matrix[0])):
        pivot = next(
            (row for row in range(pivot_row, len(matrix))
             if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column], -1, PRIME)
        matrix[pivot_row] = [
            value * inverse % PRIME for value in matrix[pivot_row]
        ]
        for row in range(len(matrix)):
            if row == pivot_row:
                continue
            scale = matrix[row][column]
            if scale:
                matrix[row] = [
                    (left - scale * right) % PRIME
                    for left, right in zip(matrix[row], matrix[pivot_row])
                ]
        pivot_columns.append(column)
        pivot_row += 1
    if pivot_row != len(matrix[0]) - 1:
        raise RuntimeError(f"expected rank seven, got {pivot_row}")
    free = next(
        column for column in range(len(matrix[0]))
        if column not in pivot_columns
    )
    kernel = [0] * len(matrix[0])
    kernel[free] = 1
    for row, column in enumerate(pivot_columns):
        kernel[column] = -matrix[row][free] % PRIME
    return pivot_row, kernel


@app.function(image=image, cpu=1.0, memory=2048, timeout=300, max_containers=32)
def decide(case):
    import sympy as sp

    epsilon_1, epsilon_2, point_index, sigma_c, sigma_o = case
    replay = json.loads(Path(REMOTE_REPLAY).read_text())
    endpoint_rows = [
        row for row in replay["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    ]
    if {row["endpoint"] for row in endpoint_rows} != {"b", "c"}:
        raise RuntimeError("missing endpoint replay row")
    point_lists = [row["kernel_null_points"] for row in endpoint_rows]
    if point_lists[0] != point_lists[1] or len(point_lists[0]) != 2:
        raise RuntimeError("endpoint null schemes do not coincide")
    point = point_lists[0][point_index]
    if not point["guard_nonzero"]:
        raise RuntimeError("unguarded kernel-null source point")

    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    kernel_row = next(
        row for row in kernel_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    )
    t, r, c, b = sp.symbols("t r c b")
    substitutions = {
        t: point["t"], r: point["r"], c: point["c"], b: point["b"]
    }
    section = [
        int(sp.sympify(item["expression"]).subs(substitutions)) % PRIME
        for item in kernel_row["kernel"]
    ]

    roots = (
        1,
        epsilon_1 * IOTA % PRIME,
        point["r"],
        point["t"],
        epsilon_2 * IOTA * point["r"] % PRIME,
    )
    labels = tuple(root * root % PRIME for root in roots)
    products = (
        -1,
        point["b"],
        point["c"],
        point["b"] * point["c"],
        -point["b"] * point["c"],
    )
    sums = (0, 1 + point["b"], 1 + point["c"],
            point["b"] + point["c"], point["b"] - point["c"])
    q_values = tuple(root * edge_sum % PRIME
                     for root, edge_sum in zip(roots, sums))
    common_rows = [
        [
            -product,
            -product * label,
            -product * label * label,
            1,
            label,
            label * label,
            0,
            0,
        ]
        for product, label in zip(products, labels)
    ]
    common_rows.extend(
        [
            q_value,
            q_value * label,
            q_value * label * label,
            0,
            0,
            0,
            label,
            label * label,
        ]
        for q_value, label in zip(q_values, labels)
    )
    rank, kernel = rank_kernel(common_rows)
    kernel_dots = [
        sum(left * right for left, right in zip(row, kernel)) % PRIME
        for row in common_rows
    ]
    section_dots = [
        sum(left * right for left, right in zip(row, section)) % PRIME
        for row in common_rows
    ]
    if any(kernel_dots) or any(section_dots):
        raise RuntimeError(f"bad common kernel: rank={rank}, dots={kernel_dots}")
    if any(section):
        scale_index = next(index for index, value in enumerate(section) if value)
        scale = kernel[scale_index] * pow(section[scale_index], -1, PRIME) % PRIME
        if [scale * value % PRIME for value in section] != kernel:
            raise RuntimeError("stored section does not span the pointwise kernel")

    a_coefficients = kernel[:3]
    b_coefficients = kernel[3:6]
    missing_label = -point["t"] * point["t"] % PRIME

    def evaluate(coefficients, value):
        return sum(coefficient * pow(value, index, PRIME)
                   for index, coefficient in enumerate(coefficients)) % PRIME

    missing_values = (
        evaluate(a_coefficients, missing_label),
        evaluate(b_coefficients, missing_label),
        (kernel[6] + kernel[7] * missing_label) % PRIME,
    )
    if missing_values[0]:
        missing_mode = "REGULARIZED_CONSTRAINED"
        missing_product = (
            missing_values[1] * pow(missing_values[0], -1, PRIME) % PRIME
        )
    elif missing_values[1] or missing_values[2]:
        return {
            "epsilon": [epsilon_1, epsilon_2],
            "point_index": point_index,
            "point": point,
            "sigma": [sigma_c, sigma_o],
            "status": "SOURCE_EMPTY",
            "common_rank": rank,
            "section_values": section,
            "section_is_zero": not any(section),
            "kernel_dots": kernel_dots,
            "missing_values": list(missing_values),
            "missing_mode": "REGULARIZED_INCONSISTENT",
            "systems": 0,
            "completed_systems": 0,
            "unit_systems": 0,
            "nonunit_systems": [],
            "rows": [],
        }
    else:
        missing_mode = "REGULARIZED_UNCONSTRAINED"
        missing_product = None

    d, e, f = sp.symbols("d e f")

    def paired(left, right):
        p0, p1, p2 = (
            b_value - left * a_value
            for a_value, b_value in zip(a_coefficients, b_coefficients)
        )
        q0 = b_coefficients[0] - right * a_coefficients[0]
        q1 = -b_coefficients[1] + right * a_coefficients[1]
        q2 = b_coefficients[2] - right * a_coefficients[2]
        return sp.expand(
            (p2 * q0 - p0 * q2) ** 2
            - (p2 * q1 - p1 * q2) * (p1 * q0 - p0 * q1)
        )

    records = (
        d * e,
        d * e,
        -d * e,
        d * f,
        sigma_o * e * f,
        point["b"] * f,
        sigma_c * point["c"] * f,
    )
    squared_sums = (
        d * d + e * e + 2 * d * e,
        d * d + e * e + 2 * d * e,
        d * d + e * e - 2 * d * e,
        d * d + f * f + 2 * d * f,
        e * e + f * f + 2 * sigma_o * e * f,
        point["b"] ** 2 + f * f + 2 * point["b"] * f,
        point["c"] ** 2 + f * f + 2 * sigma_c * point["c"] * f,
    )
    representatives = (1, point["b"], point["c"], d, e, f)
    guard = sp.prod(representatives)
    for left, right in itertools.combinations(representatives, 2):
        guard *= (left - right) * (left + right)

    def singular(expression):
        return str(
            sp.Poly(expression, d, e, f, modulus=PRIME).as_expr()
        ).replace("**", "^")

    systems = []
    for xi_index in range(7):
        residual = tuple(records[index] for index in range(7)
                         if index != xi_index)
        for pairing_index, matching in enumerate(MATCHINGS):
            equations = [
                paired(residual[left], residual[right])
                for left, right in matching
            ]
            if missing_mode == "REGULARIZED_CONSTRAINED":
                equations.insert(0, records[xi_index] - missing_product)
                equations.append(
                    missing_label * missing_values[2] * missing_values[2]
                    - squared_sums[xi_index]
                    * missing_values[0] * missing_values[0]
                )
            systems.append({
                "xi_index": xi_index,
                "pairing_index": pairing_index,
                "equations": tuple(equations),
            })

    blocks = [f"poly h={singular(sp.expand(guard))};"]
    for index, system in enumerate(systems):
        definitions = "\n".join(
            f"poly p{equation_index}={singular(equation)};"
            for equation_index, equation in enumerate(system["equations"])
        )
        generators = ",".join(
            f"p{index}" for index in range(len(system["equations"]))
        )
        kills = " ".join(
            f"kill p{index};" for index in range(len(system["equations"]))
        )
        blocks.append(f"""
{definitions}
ideal G={generators},z*h-1; G=slimgb(G);
print("SYS={index},BEGIN");
print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); print("BASIS_BEGIN"); G; print("BASIS_END"); }}
print("SYS={index},END");
kill G; {kills}
""")
    program = f"""
ring R={PRIME},(z,d,e,f),(dp(1),dp(3));
option(redSB);
print("BEGIN");
{chr(10).join(blocks)}
print("END"); quit;
"""

    def parse(stdout):
        rows = []
        for index, system in enumerate(systems):
            match = re.search(
                rf"SYS={index},BEGIN\nDIM=(-?\d+)\nSIZE=(\d+)\nUNIT=(\d)\n"
                rf"(?:(?:BASIS_BEGIN\n(.*?)\nBASIS_END\n))?"
                rf"SYS={index},END",
                stdout,
                re.DOTALL,
            )
            if not match:
                continue
            rows.append({
                "xi_index": system["xi_index"],
                "pairing_index": system["pairing_index"],
                "dimension": int(match.group(1)),
                "basis_size": int(match.group(2)),
                "unit": match.group(3) == "1",
                "nonunit_basis": match.group(4),
            })
        return rows

    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=270,
        )
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        rows = parse(stdout)
        return {
            "epsilon": [epsilon_1, epsilon_2],
            "point_index": point_index,
            "point": point,
            "sigma": [sigma_c, sigma_o],
            "status": "TIMEOUT",
            "common_rank": rank,
            "section_values": section,
            "section_is_zero": not any(section),
            "kernel_dots": kernel_dots,
            "missing_values": list(missing_values),
            "missing_mode": missing_mode,
            "systems": len(systems),
            "completed_systems": len(rows),
            "unit_systems": sum(row["unit"] for row in rows),
            "nonunit_systems": [row for row in rows if not row["unit"]],
            "rows": rows,
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
            "partial_stdout": stdout[-4000:],
        }

    rows = parse(process.stdout)
    valid = (
        process.returncode == 0
        and "END" in process.stdout
        and "?" not in process.stdout
        and len(rows) == len(systems)
    )
    return {
        "epsilon": [epsilon_1, epsilon_2],
        "point_index": point_index,
        "point": point,
        "sigma": [sigma_c, sigma_o],
        "status": "COMPLETE" if valid else "ERROR",
        "common_rank": rank,
        "section_values": section,
        "section_is_zero": not any(section),
        "kernel_dots": kernel_dots,
        "missing_values": list(missing_values),
        "missing_mode": missing_mode,
        "systems": len(systems),
        "completed_systems": len(rows),
        "unit_systems": sum(row["unit"] for row in rows),
        "nonunit_systems": [row for row in rows if not row["unit"]],
        "rows": rows,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stderr": process.stderr[-1000:],
    }


@app.local_entrypoint()
def main(limit: int = 0):
    cases = tuple(
        (epsilon_1, epsilon_2, point_index, sigma_c, sigma_o)
        for epsilon_1 in (-1, 1) for epsilon_2 in (-1, 1)
        for point_index in range(2)
        for sigma_c in (-1, 1) for sigma_o in (-1, 1)
    )
    if limit:
        cases = cases[:limit]
    rows = list(decide.map(cases, order_outputs=True))
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell9-kernel-null-residual-v1",
        "field": PRIME,
        "scope": (
            "Exact all-role, all-matching target census at every deployed "
            "cell-9 source point where A(-t^2)=B(-t^2)=beta(-t^2)=0."
        ),
        "source_replay_sha256": hashlib.sha256(REPLAY.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "cases": len(rows),
        "complete": sum(row.get("status") == "COMPLETE" for row in rows),
        "systems": sum(row.get("systems", 0) for row in rows),
        "completed_systems": sum(
            row.get("completed_systems", 0) for row in rows
        ),
        "unit_systems": sum(row.get("unit_systems", 0) for row in rows),
        "nonunit_systems": sum(
            len(row.get("nonunit_systems", [])) for row in rows
        ),
    }, sort_keys=True))
