#!/usr/bin/env python3
"""Exact outside paired-product ideals at the 433-1b rank-drop common points."""

import hashlib
import itertools
import json
from pathlib import Path
import subprocess

import modal


DIRECTORY = Path(__file__).parent
POINTS = DIRECTORY / "rate_half_kb_positive_433_1b_rankdrop_fglm_profile_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_rankdrop_outside_product_result.json"
REMOTE_POINTS = "/root/points.json"
PRIME = 2130706433
IOTA = 16711679

app = modal.App("rs-mca-positive-433-1b-rankdrop-outside-product")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(POINTS, REMOTE_POINTS)
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


def matching_cells():
    output = []
    for singleton in range(5):
        rest = tuple(index for index in range(5) if index != singleton)
        output.extend((singleton, matching) for matching in pairings(rest))
    return tuple(output)


def rank_kernel(rows):
    matrix = [[value % PRIME for value in row] for row in rows]
    pivot_columns = []
    pivot_row = 0
    for column in range(len(matrix[0])):
        pivot = next((row for row in range(pivot_row, len(matrix))
                      if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column], -1, PRIME)
        matrix[pivot_row] = [value * inverse % PRIME
                             for value in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row:
                continue
            scale = matrix[row][column]
            if scale:
                matrix[row] = [(left - scale * right) % PRIME
                               for left, right in zip(matrix[row], matrix[pivot_row])]
        pivot_columns.append(column)
        pivot_row += 1
    if pivot_row != len(matrix[0]) - 1:
        raise RuntimeError(f"expected rank seven, got {pivot_row}")
    free = next(column for column in range(len(matrix[0]))
                if column not in pivot_columns)
    kernel = [0] * len(matrix[0])
    kernel[free] = 1
    for row, column in enumerate(pivot_columns):
        kernel[column] = -matrix[row][free] % PRIME
    return kernel


def common_kernel(record):
    cell = record["cell"]
    epsilon = record["epsilon"]
    point = record["point"]
    singleton, matching = matching_cells()[cell]
    roots = [None] * 5
    roots[matching[0][0]] = 1
    roots[matching[0][1]] = epsilon[0] * IOTA
    roots[matching[1][0]] = point["r"]
    roots[matching[1][1]] = epsilon[1] * IOTA * point["r"]
    roots[singleton] = point["t"]
    labels = [root * root % PRIME for root in roots]
    b, c = point["b"], point["c"]
    products = (-1, b, c, b*c, -b*c)
    sums = (0, 1+b, 1+c, b+c, b-c)
    rows = [
        [-product, -product*label, -product*label*label,
         1, label, label*label, 0, 0]
        for product, label in zip(products, labels)
    ]
    rows.extend(
        [q, q*label, q*label*label, 0, 0, 0, label, label*label]
        for root, label, edge_sum in zip(roots, labels, sums)
        for q in [root * edge_sum]
    )
    return rank_kernel(rows)


def flattened_points():
    payload = json.loads(Path(REMOTE_POINTS).read_text())
    return tuple(
        {
            "cell": row["cell"],
            "epsilon": row["epsilon"],
            "point_index": point_index,
            "point": point,
        }
        for row in payload["rows"]
        for point_index, point in enumerate(row["rational_points"])
    )


@app.function(image=image, cpu=1.0, memory=1024, timeout=210, max_containers=16)
def decide_lane(case):
    import sympy as sp

    point_id, sigma_c, sigma_o = case
    record = flattened_points()[point_id]
    point = record["point"]
    kernel = common_kernel(record)
    d0, d1, d2, e0, e1, e2, beta0, beta1 = kernel
    missing_label = -point["t"] * point["t"] % PRIME

    def evaluate(coefficients, value):
        return (coefficients[0] + coefficients[1]*value
                + coefficients[2]*value*value) % PRIME

    denominator = evaluate((d0, d1, d2), missing_label)
    if not denominator:
        raise RuntimeError("missing-mate leading support failure")
    missing_product = (
        evaluate((e0, e1, e2), missing_label)
        * pow(denominator, -1, PRIME) % PRIME
    )

    d, e, f, y, z = sp.symbols("d e f y z")
    p0, p1, p2 = e0-y*d0, e1-y*d1, e2-y*d2
    q0, q1, q2 = e0-z*d0, -e1+z*d1, e2-z*d2
    paired = sp.expand(
        (p2*q0-p0*q2)**2 - (p2*q1-p1*q2)*(p1*q0-p0*q1)
    )
    records = (
        d*e, d*e, -d*e, d*f, sigma_o*e*f,
        point["b"]*f, sigma_c*point["c"]*f,
    )
    squared_sums = (
        d*d + e*e + 2*d*e,
        d*d + e*e + 2*d*e,
        d*d + e*e - 2*d*e,
        d*d + f*f + 2*d*f,
        e*e + f*f + 2*sigma_o*e*f,
        point["b"]**2 + f*f + 2*point["b"]*f,
        point["c"]**2 + f*f + 2*sigma_c*point["c"]*f,
    )
    a2_missing = evaluate((d0, d1, d2), missing_label)
    b1_missing = (beta0 + beta1*missing_label) % PRIME
    target_values = (1, point["b"], point["c"], d, e, f)
    guard = sp.prod(
        [d, e, f]
        + [target_values[left] - target_values[right]
           for left in range(6) for right in range(left + 1, 6)]
        + [target_values[left] + target_values[right]
           for left in range(6) for right in range(left + 1, 6)]
    )

    def singular(expression):
        return str(sp.Poly(expression, d, e, f, modulus=PRIME).as_expr()).replace(
            "**", "^"
        )

    pairing_list = tuple(pairings(tuple(range(6))))
    rows = []
    started_cases = 0
    for xi_index in range(7):
        residual = tuple(index for index in range(7) if index != xi_index)
        for pairing_index, matching in enumerate(pairing_list):
            started_cases += 1
            equations = [records[xi_index] - missing_product]
            for left, right in matching:
                equations.append(paired.subs({
                    y: records[residual[left]],
                    z: records[residual[right]],
                }))
            equations.append(
                missing_label*b1_missing*b1_missing
                - squared_sums[xi_index]*a2_missing*a2_missing
            )
            definitions = "\n".join(
                f"poly q{index}={singular(value)};"
                for index, value in enumerate(equations)
            )
            program = f"""
ring R={PRIME},(u,d,e,f),(dp(1),dp(3));
option(redSB);
{definitions}
poly guard={singular(guard)};
ideal I=q0,q1,q2,q3,q4,u*guard-1;
ideal G=std(I);
print("BEGIN"); print(dim(G)); print(size(G));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); }}
print("END");
quit;
"""
            try:
                process = subprocess.run(
                    ["Singular", "--quiet"], input=program,
                    capture_output=True, text=True, timeout=3,
                )
            except subprocess.TimeoutExpired:
                rows.append({
                    "xi_index": xi_index,
                    "pairing_index": pairing_index,
                    "status": "TIMEOUT",
                    "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
                })
                continue
            stdout = process.stdout
            valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
            row = {
                "xi_index": xi_index,
                "pairing_index": pairing_index,
                "status": "COMPLETE" if valid else "ERROR",
                "unit": "UNIT=1" in stdout,
                "stdout": stdout[-500:],
                "stderr": process.stderr[-500:],
                "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
            }
            if valid and not row["unit"]:
                lex_program = f"""
ring R={PRIME},(u,d,e,f),(dp(1),dp(3));
option(redSB);
{definitions}
poly guard={singular(guard)};
ideal I=q0,q1,q2,q3,q4,u*guard-1;
ideal G=std(I);
ring L={PRIME},(u,d,e,f),lp;
option(redSB);
ideal H=fglm(R,G);
print("LEX_BEGIN"); print("LEX_SIZE="+string(size(H))); H;
print("LEX_END");
quit;
"""
                try:
                    lex_process = subprocess.run(
                        ["Singular", "--quiet"], input=lex_program,
                        capture_output=True, text=True, timeout=5,
                    )
                except subprocess.TimeoutExpired:
                    row["lex_status"] = "TIMEOUT"
                else:
                    lex_stdout = lex_process.stdout
                    lex_valid = (lex_process.returncode == 0 and
                                 "LEX_END" in lex_stdout and "?" not in lex_stdout)
                    row["lex_status"] = "COMPLETE" if lex_valid else "ERROR"
                    row["lex_stdout"] = lex_stdout[-10000:]
                    row["lex_stderr"] = lex_process.stderr[-500:]
                    row["lex_program_sha256"] = hashlib.sha256(
                        lex_program.encode()
                    ).hexdigest()
                    eliminant_match = __import__("re").search(
                        r"H\[1\]=(.*)", lex_stdout
                    )
                    if lex_valid and eliminant_match:
                        expression = eliminant_match.group(1).strip()
                        converted = __import__("re").sub(
                            r"([a-zA-Z])(\d+)", r"\1**\2", expression
                        )
                        converted = __import__("re").sub(
                            r"(?<=\d)(?=[a-zA-Z])", "*", converted
                        )
                        factor_variable = sp.symbols("f")
                        _, factor_rows = sp.factor_list(
                            sp.sympify(converted), factor_variable, modulus=PRIME
                        )
                        row["eliminant"] = expression
                        row["factor_degrees"] = [
                            sp.Poly(value, factor_variable, modulus=PRIME).degree()
                            for value, multiplicity in factor_rows
                            for _ in range(multiplicity)
                        ]
                        row["linear_factor_count"] = sum(
                            multiplicity
                            for value, multiplicity in factor_rows
                            if sp.Poly(value, factor_variable,
                                       modulus=PRIME).degree() == 1
                        )
            rows.append(row)
    return {
        "point_id": point_id,
        "cell": record["cell"],
        "epsilon": record["epsilon"],
        "point_index": record["point_index"],
        "sigma_c": sigma_c,
        "sigma_o": sigma_o,
        "missing_product": missing_product,
        "case_count": started_cases,
        "rows": rows,
    }


@app.local_entrypoint()
def main(points: str = "0"):
    selected = tuple(int(value) for value in points.split(",") if value)
    cases = tuple(itertools.product(selected, (-1, 1), (-1, 1)))
    raw = list(decide_lane.map(cases, order_outputs=True, return_exceptions=True))
    lanes = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            lanes.append({
                "point_id": case[0], "sigma_c": case[1], "sigma_o": case[2],
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            row["status"] = "COMPLETE" if all(
                item["status"] == "COMPLETE" for item in row["rows"]
            ) else "PARTIAL"
            row["unit_count"] = sum(item.get("unit", False) for item in row["rows"])
            row["survivor_count"] = sum(
                item["status"] == "COMPLETE" and not item.get("unit", False)
                for item in row["rows"]
            )
            row["rational_candidate_cases"] = sum(
                item.get("linear_factor_count", 0) > 0 for item in row["rows"]
            )
            lanes.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-rankdrop-outside-product-v2",
        "app": "rs-mca-positive-433-1b-rankdrop-outside-product",
        "scope": (
            "Exact target-guarded missing-product, three paired-product, and "
            "missing-mate squared-sum ideals. Residual source-pair lifts and "
            "the other six sum rows are not needed by a unit certificate."
        ),
        "source_points_sha256": hashlib.sha256(POINTS.read_bytes()).hexdigest(),
        "point_count": len(selected),
        "lane_count": len(lanes),
        "case_count": sum(len(row.get("rows", [])) for row in lanes),
        "status_counts": {
            status: sum(
                item["status"] == status
                for row in lanes for item in row.get("rows", [])
            )
            for status in sorted({
                item["status"] for row in lanes for item in row.get("rows", [])
            })
        },
        "lanes": lanes,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "lanes": [
            {"point_id": row["point_id"], "sigma": [row["sigma_c"], row["sigma_o"]],
             "status": row["status"], "unit": row.get("unit_count"),
             "survivors": row.get("survivor_count"),
             "rational_candidates": row.get("rational_candidate_cases")}
            for row in lanes
        ],
    }, sort_keys=True))
