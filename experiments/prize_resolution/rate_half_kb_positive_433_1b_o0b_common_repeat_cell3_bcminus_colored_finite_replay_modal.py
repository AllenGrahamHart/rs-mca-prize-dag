#!/usr/bin/env python3
"""Replay every exceptional fiber of the cell-3 BC- colored cut norms."""

from collections import Counter, defaultdict
import hashlib
import itertools
import json
from pathlib import Path
import time

import modal


DIRECTORY = Path(__file__).parent
NORMS = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcminus_colored_norm_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcminus_colored_finite_replay_result.json"
)
REMOTE_NORMS = "/root/norms.json"
PRIME = 2130706433
IOTA = 16711679

app = modal.App("rs-mca-positive-433-1b-o0b-cell3-bcminus-colored-replay")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
    .add_local_file(NORMS, REMOTE_NORMS)
)


def determinant(matrix):
    """Division-free determinant; all matrices here are five by five."""
    output = 0
    for permutation in itertools.permutations(range(len(matrix))):
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(len(matrix))
            for right in range(left + 1, len(matrix))
        )
        term = PRIME - 1 if inversions % 2 else 1
        for row, column in enumerate(permutation):
            term = term * matrix[row][column] % PRIME
        output = (output + term) % PRIME
    return output


def colored_cuts(b_value, c_value, r_value, epsilon_1, epsilon_2):
    r2 = r_value * r_value % PRIME
    r4 = r2 * r2 % PRIME
    labels = (1, r4, PRIME - 1, r2, -r2 % PRIME)
    products = (PRIME - 1, b_value, c_value,
                b_value * c_value % PRIME, b_value * c_value % PRIME)
    matrix = [
        [
            -product % PRIME,
            -product * label % PRIME,
            -product * label * label % PRIME,
            1,
            label,
            label * label % PRIME,
        ]
        for product, label in zip(products, labels)
    ]
    cofactors = []
    for column in range(6):
        minor = [row[:column] + row[column + 1:] for row in matrix]
        value = determinant(minor)
        cofactors.append(-value % PRIME if column % 2 else value)

    scale = r4 * (1 - r4) % PRIME
    kernel = [scale * value % PRIME for value in cofactors]
    a_values, b_values = kernel[:3], kernel[3:]
    a_pivot = sum(
        value * pow(r4, index, PRIME)
        for index, value in enumerate(cofactors[:3])
    ) % PRIME
    beta_0 = -epsilon_1 * epsilon_2 * r2 * (1 + b_value) * a_pivot % PRIME
    beta_1 = -beta_0 % PRIME
    missing_label = -r4 % PRIME

    def evaluate(coefficients):
        return sum(
            coefficient * pow(missing_label, index, PRIME)
            for index, coefficient in enumerate(coefficients)
        ) % PRIME

    a_missing = evaluate(a_values)
    b_missing = evaluate(b_values)
    beta_missing = (beta_0 + beta_1 * missing_label) % PRIME
    cuts = {}
    for missing_record, known in (("BE", b_value), ("CF", c_value)):
        known_squared = known * known % PRIME
        cuts[missing_record] = (
            r4 * known_squared * beta_missing * beta_missing
            + pow((known_squared * a_missing + b_missing) % PRIME, 2, PRIME)
        ) % PRIME
    return {
        "cofactors": cofactors,
        "a_missing": a_missing,
        "b_missing": b_missing,
        "beta_missing": beta_missing,
        "cuts": cuts,
    }


@app.function(image=image, cpu=1.0, memory=2048, timeout=180)
def replay():
    from flint import fmpz_mod_poly_ctx

    started = time.perf_counter()
    norms = json.loads(Path(REMOTE_NORMS).read_text())
    context = fmpz_mod_poly_ctx(PRIME)
    variable = context([0, 1])

    def field_roots(coefficients):
        polynomial = context([value % PRIME for value in coefficients])
        if polynomial.is_zero():
            raise ValueError("zero exceptional polynomial")
        field_part = polynomial.gcd(pow(variable, PRIME, polynomial) - variable)
        _, factors = field_part.factor()
        values = []
        for factor, _ in factors:
            if int(factor.degree()) != 1:
                raise ValueError("field part has nonlinear factor")
            values.append(
                -int(factor[0]) * pow(int(factor[1]), -1, PRIME) % PRIME
            )
        return sorted(set(values))

    root_ledger = []
    incidence = defaultdict(list)
    for norm_row in norms["rows"]:
        case = {
            "epsilon": norm_row["epsilon"],
            "missing_record": norm_row["missing_record"],
        }
        polynomials = [
            ("CUT_NORM_NUMERATOR", "numerator", norm_row["cut_norm_numerator"]),
            ("CUT_NORM_DENOMINATOR", "denominator", norm_row["cut_norm_denominator"]),
        ]
        polynomials.extend(
            ("CONSTRUCTION_GUARD", digest, coefficients)
            for digest, coefficients in sorted(
                norm_row["construction_guards"].items()
            )
        )
        for kind, identity, coefficients in polynomials:
            roots = field_roots(coefficients)
            ledger_row = {
                **case,
                "kind": kind,
                "identity": identity,
                "degree": len(coefficients) - 1,
                "roots": roots,
            }
            root_ledger.append(ledger_row)
            for q_value in roots:
                incidence[q_value].append({
                    **case, "kind": kind, "identity": identity,
                })

    rows = []
    cut_zero_points = []
    for q_value in sorted(incidence):
        q2 = q_value * q_value % PRIME
        q3 = q2 * q_value % PRIME
        numerator = (q3 + 2 * q2 + q_value + 4) % PRIME
        denominator = (q3 + 6 * q2 + q_value) % PRIME
        row = {
            "q": q_value,
            "incidence": incidence[q_value],
            "numerator": numerator,
            "denominator": denominator,
            "y_rows": [],
        }
        if denominator == 0:
            row["status"] = "PROJECTION_DENOMINATOR_BOUNDARY"
            rows.append(row)
            continue
        y_square = numerator * pow(denominator, -1, PRIME) % PRIME
        y_values = field_roots([-y_square, 0, 1])
        row["y_square"] = y_square
        row["y_values"] = y_values
        if not y_values:
            row["status"] = "NO_BASE_FIELD_Y"
            rows.append(row)
            continue

        guarded_point_count = 0
        for y_value in y_values:
            y_row = {"y": y_value, "sign_rows": []}
            if (y_value - 1) % PRIME == 0 or (q_value * y_value - 1) % PRIME == 0:
                y_row["status"] = "MOBIUS_DENOMINATOR_BOUNDARY"
                row["y_rows"].append(y_row)
                continue
            b_value = (
                (q_value * y_value + 1)
                * pow(q_value * y_value - 1, -1, PRIME)
            ) % PRIME
            c_value = (y_value + 1) * pow(y_value - 1, -1, PRIME) % PRIME
            y_row.update({"b": b_value, "c": c_value})
            target_guard = (
                b_value * c_value * (b_value - 1) * (b_value + 1)
                * (c_value - 1) * (c_value + 1)
                * (b_value - c_value) * (b_value + c_value)
            ) % PRIME
            if target_guard == 0 or (b_value * c_value - 1) % PRIME == 0:
                y_row["status"] = "TARGET_GUARD_BOUNDARY"
                row["y_rows"].append(y_row)
                continue
            projection = (
                b_value**3 * c_value**3 + b_value**2 * c_value**4
                + 3 * b_value**2 * c_value**3
                - 2 * b_value**2 * c_value**2 - 2 * b_value**2 * c_value
                - b_value**2 - b_value * c_value**4
                - 2 * b_value * c_value**3 - 2 * b_value * c_value**2
                + 3 * b_value * c_value + b_value + c_value
            ) % PRIME
            if projection:
                raise ValueError("projection replay")

            for epsilon_1, epsilon_2 in itertools.product((-1, 1), repeat=2):
                ratio = (
                    (c_value - b_value)
                    * pow(b_value * c_value - 1, -1, PRIME)
                ) % PRIME
                alpha = epsilon_1 * (IOTA + epsilon_2) * ratio % PRIME
                beta = -epsilon_2 * IOTA % PRIME
                r_values = field_roots([-beta, -alpha, 1])
                sign_row = {
                    "epsilon": [epsilon_1, epsilon_2],
                    "r_values": r_values,
                    "points": [],
                }
                for r_value in r_values:
                    r2 = r_value * r_value % PRIME
                    r4 = r2 * r2 % PRIME
                    t_value = epsilon_1 * epsilon_2 * r2 % PRIME
                    labels = (1, r4, PRIME - 1, r2, -r2 % PRIME)
                    common_guard = bool(r_value * t_value % PRIME) and all(
                        (labels[left] - labels[right]) % PRIME
                        for left in range(5)
                        for right in range(left + 1, 5)
                    )
                    relation = (
                        (b_value * c_value - 1)
                        * (epsilon_1 * epsilon_2 * r2 + epsilon_1 * IOTA)
                        - (epsilon_2 * IOTA + 1)
                        * r_value * (c_value - b_value)
                    ) % PRIME
                    if relation:
                        raise ValueError("r relation replay")
                    point = {
                        "r": r_value,
                        "t": t_value,
                        "status": (
                            "GUARDED" if common_guard else "COMMON_GUARD_BOUNDARY"
                        ),
                    }
                    if common_guard:
                        guarded_point_count += 1
                        evaluation = colored_cuts(
                            b_value, c_value, r_value, epsilon_1, epsilon_2
                        )
                        point.update(evaluation)
                        for missing_record, cut_value in evaluation["cuts"].items():
                            if cut_value == 0:
                                cut_zero_points.append({
                                    "q": q_value,
                                    "y": y_value,
                                    "b": b_value,
                                    "c": c_value,
                                    "r": r_value,
                                    "t": t_value,
                                    "epsilon": [epsilon_1, epsilon_2],
                                    "missing_record": missing_record,
                                })
                    sign_row["points"].append(point)
                y_row["sign_rows"].append(sign_row)
            y_row["status"] = "LIFTED"
            row["y_rows"].append(y_row)
        row["guarded_point_count"] = guarded_point_count
        row["status"] = (
            "LIFTED" if guarded_point_count else "NO_GUARDED_COMMON_POINT"
        )
        rows.append(row)

    return {
        "root_ledger": root_ledger,
        "q_count": len(rows),
        "status_counts": dict(sorted(Counter(row["status"] for row in rows).items())),
        "guarded_point_count": sum(row.get("guarded_point_count", 0) for row in rows),
        "cut_zero_points": cut_zero_points,
        "rows": rows,
        "seconds": time.perf_counter() - started,
    }


@app.local_entrypoint()
def main():
    payload = replay.remote()
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-o0b-cell3-bcminus-"
            "colored-finite-replay-v1"
        ),
        "scope": (
            "Exact deployed-field replay of every colored-cut norm zero, "
            "norm pole, and registered tower-construction boundary."
        ),
        "source_norms_sha256": hashlib.sha256(NORMS.read_bytes()).hexdigest(),
        **payload,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "q_count": output["q_count"],
        "status_counts": output["status_counts"],
        "guarded_point_count": output["guarded_point_count"],
        "cut_zero_point_count": len(output["cut_zero_points"]),
        "root_counts": dict(sorted(Counter(
            f'{row["kind"]}:{len(row["roots"])}'
            for row in output["root_ledger"]
        ).items())),
        "seconds": output["seconds"],
    }, sort_keys=True))
