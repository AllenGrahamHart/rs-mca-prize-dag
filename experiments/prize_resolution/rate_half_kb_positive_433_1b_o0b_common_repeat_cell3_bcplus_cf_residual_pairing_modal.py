#!/usr/bin/env python3
"""Replay residual paired-product systems at the finite cell-3 CF cuts."""

from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import time

import modal


DIRECTORY = Path(__file__).parent
SOURCE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcplus_colored_missing_roots_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcplus_cf_residual_pairing_result.json"
)
REMOTE_SOURCE = "/root/colored_roots.json"
PRIME = 2130706433
RECORDS = ("BE", "DE+", "DE-", "DF+", "DF-", "EF")

app = modal.App("rs-mca-positive-433-1b-o0b-cell3-bcplus-cf-pairing")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
    .add_local_file(SOURCE, REMOTE_SOURCE)
)


def canonical_matchings(items):
    if not items:
        return ((),)
    output = []
    for index in range(1, len(items)):
        for tail in canonical_matchings(items[1:index]+items[index+1:]):
            output.append(((items[0], items[index]),)+tail)
    return tuple(output)


MATCHINGS = canonical_matchings(tuple(range(6)))


@app.function(image=image, cpu=1.0, memory=1536, timeout=240, max_containers=32)
def replay(case):
    from flint import fmpz_mod_mpoly_ctx, fmpz_mod_poly_ctx

    started = time.perf_counter()
    epsilon_1, epsilon_2, point_index, sigma_o = case
    payload = json.loads(Path(REMOTE_SOURCE).read_text())
    source_row = next(
        row for row in payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
        and row["missing_record"] == "CF"
    )
    point = source_row["points"][point_index]
    b_value, r_value, c_value = point["b"], point["r"], point["u"]
    f_value = point["missing_target_coordinate"]

    def determinant(matrix):
        matrix = [[value % PRIME for value in row] for row in matrix]
        output = 1
        for column in range(len(matrix)):
            pivot = next(
                (row for row in range(column, len(matrix))
                 if matrix[row][column]),
                None,
            )
            if pivot is None:
                return 0
            if pivot != column:
                matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
                output = -output
            pivot_value = matrix[column][column]
            output = output*pivot_value % PRIME
            inverse = pow(pivot_value, -1, PRIME)
            for row in range(column+1, len(matrix)):
                factor = matrix[row][column]*inverse % PRIME
                for index in range(column, len(matrix)):
                    matrix[row][index] = (
                        matrix[row][index]-factor*matrix[column][index]
                    ) % PRIME
        return output % PRIME

    r2 = r_value*r_value % PRIME
    r4 = r2*r2 % PRIME
    labels = (1, r4, PRIME-1, r2, -r2 % PRIME)
    products = (PRIME-1, b_value, c_value,
                b_value*c_value % PRIME, b_value*c_value % PRIME)
    matrix = [
        [
            -product % PRIME,
            -product*label % PRIME,
            -product*label*label % PRIME,
            1,
            label,
            label*label % PRIME,
        ]
        for product, label in zip(products, labels)
    ]
    cofactors = []
    for column in range(6):
        minor = [row[:column]+row[column+1:] for row in matrix]
        cofactors.append(((-1)**column*determinant(minor)) % PRIME)
    scale = r4*(1-r4) % PRIME
    kernel = [scale*value % PRIME for value in cofactors]
    a_values, b_values = kernel[:3], kernel[3:]

    def evaluate(coefficients, value):
        return sum(
            coefficient*pow(value, index, PRIME)
            for index, coefficient in enumerate(coefficients)
        ) % PRIME

    missing_label = -r4 % PRIME
    a_missing = evaluate(a_values, missing_label)
    b_missing = evaluate(b_values, missing_label)
    if not a_missing:
        raise ValueError("missing-product ratio boundary")
    source_product = b_missing*pow(a_missing, -1, PRIME) % PRIME
    if source_product != point["source_product"]:
        raise ValueError("missing-product reconstruction")
    if c_value*f_value % PRIME != source_product:
        raise ValueError("CF target reconstruction")

    context = fmpz_mod_mpoly_ctx.get(["d", "e"], PRIME)
    d_variable = context.from_dict({(1, 0): 1})
    e_variable = context.from_dict({(0, 1): 1})

    def constant(value):
        return context.from_dict({(0, 0): value % PRIME})

    def paired(left, right):
        p0, p1, p2 = (
            constant(b_coefficient)-left*a_coefficient
            for a_coefficient, b_coefficient in zip(a_values, b_values)
        )
        q0 = constant(b_values[0])-right*a_values[0]
        q1 = constant(-b_values[1])+right*a_values[1]
        q2 = constant(b_values[2])-right*a_values[2]
        return (p2*q0-p0*q2)**2-(p2*q1-p1*q2)*(p1*q0-p0*q1)

    polynomial_context = fmpz_mod_poly_ctx(PRIME)
    variable = polynomial_context([0, 1])

    def specialize(polynomial, free_index, assignments=None):
        assignments = assignments or {}
        coefficients = {}
        for exponents, coefficient in polynomial.to_dict().items():
            scalar = int(coefficient) % PRIME
            for index, value in assignments.items():
                scalar = scalar*pow(value, exponents[index], PRIME) % PRIME
            if any(
                exponent and index != free_index and index not in assignments
                for index, exponent in enumerate(exponents)
            ):
                raise ValueError("incomplete specialization")
            degree = exponents[free_index]
            coefficients[degree] = (
                coefficients.get(degree, 0)+scalar
            ) % PRIME
        return polynomial_context([
            coefficients.get(degree, 0)
            for degree in range(max(coefficients, default=0)+1)
        ])

    def field_roots(polynomial):
        if polynomial.is_zero():
            return None
        if polynomial.degree() == 0:
            return []
        field_part = polynomial.gcd(pow(variable, PRIME, polynomial)-variable)
        _, factors = field_part.factor()
        roots = []
        for factor, _ in factors:
            if factor.degree() != 1:
                raise ValueError("field-root gcd contains nonlinear factor")
            roots.append(
                -int(factor[0])*pow(int(factor[1]), -1, PRIME) % PRIME
            )
        return sorted(set(roots))

    def coefficients(polynomial):
        return [
            int(polynomial[index]) % PRIME
            for index in range(int(polynomial.degree())+1)
        ]

    def evaluate_pair(polynomial, d_value, e_value):
        return sum(
            int(coefficient)
            * pow(d_value, exponents[0], PRIME)
            * pow(e_value, exponents[1], PRIME)
            for exponents, coefficient in polynomial.to_dict().items()
        ) % PRIME

    def guarded(d_value, e_value):
        values = (1, b_value, c_value, d_value, e_value, f_value)
        return (
            all(value for value in values)
            and all((values[left]-values[right]) % PRIME
                    and (values[left]+values[right]) % PRIME
                    for left, right in itertools.combinations(range(6), 2))
        )

    records = (
        b_value*e_variable,
        d_variable*e_variable,
        -d_variable*e_variable,
        f_value*d_variable,
        -f_value*d_variable,
        sigma_o*f_value*e_variable,
    )
    pairing_rows = []
    for pairing_index, matching in enumerate(MATCHINGS):
        equations = [
            paired(records[left], records[right])
            for left, right in matching
        ]
        candidates = []
        resultant_profiles = []
        for free_index, eliminated in ((1, "d"), (0, "e")):
            for left, right in itertools.combinations(range(3), 2):
                resultant = equations[left].resultant(equations[right], eliminated)
                profile = {
                    "free_index": free_index,
                    "equations": [left, right],
                    "zero": not bool(resultant),
                }
                if resultant:
                    degrees = tuple(int(value) for value in resultant.degrees())
                    profile.update({
                        "degrees": list(degrees),
                        "terms": len(resultant.to_dict()),
                    })
                    eliminated_index = 1-free_index
                    if degrees[eliminated_index] != 0:
                        raise ValueError("eliminated variable survived resultant")
                    univariate = specialize(resultant, free_index)
                    candidates.append((
                        int(univariate.degree()), len(resultant.to_dict()),
                        free_index, left, right, univariate,
                    ))
                resultant_profiles.append(profile)
        row = {
            "pairing_index": pairing_index,
            "resultant_profiles": resultant_profiles,
            "unresolved": [],
        }
        if not candidates:
            row["status"] = "ZERO_PAIRWISE_RESULTANTS"
            row["unresolved"].append(row["status"])
            pairing_rows.append(row)
            continue
        _, _, free_index, left, right, selected = min(candidates)
        roots = field_roots(selected)
        if roots is None:
            raise ValueError("selected resultant became zero")
        row.update({
            "selected_free": "d" if free_index == 0 else "e",
            "selected_equations": [left, right],
            "selected_resultant_degree": int(selected.degree()),
            "selected_resultant_coefficients": coefficients(selected),
            "selected_roots": roots,
            "fiber_certificates": [],
        })
        other_index = 1-free_index
        solutions = []
        for free_value in roots:
            specialized = [
                specialize(value, other_index, {free_index: free_value})
                for value in equations
            ]
            nonzero = [value for value in specialized if not value.is_zero()]
            if not nonzero:
                row["unresolved"].append({
                    "free_value": free_value, "reason": "FREE_OTHER",
                })
                continue
            common = nonzero[0]
            for value in nonzero[1:]:
                common = common.gcd(value)
            other_roots = field_roots(common)
            if other_roots is None:
                raise ValueError("fiber gcd became zero")
            row["fiber_certificates"].append({
                "free_value": free_value,
                "gcd_coefficients": coefficients(common),
                "other_roots": other_roots,
            })
            for other_value in other_roots:
                coordinates = [None, None]
                coordinates[free_index] = free_value
                coordinates[other_index] = other_value
                d_value, e_value = coordinates
                equation_values = [
                    evaluate_pair(value, d_value, e_value)
                    for value in equations
                ]
                if any(equation_values):
                    raise ValueError("fiber solution replay")
                solutions.append((d_value, e_value, guarded(d_value, e_value)))
        guarded_solutions = [value for value in solutions if value[2]]
        row.update({
            "solution_count": len(solutions),
            "solutions_sha256": hashlib.sha256(
                json.dumps(solutions, separators=(",", ":")).encode()
            ).hexdigest(),
            "guarded_count": len(guarded_solutions),
        })
        if guarded_solutions:
            row["guarded_witnesses"] = guarded_solutions[:8]
        if row["unresolved"]:
            row["status"] = "UNRESOLVED"
        elif guarded_solutions:
            row["status"] = "GUARDED_SURVIVOR"
        elif solutions:
            row["status"] = "GUARD_BOUNDARY_ONLY"
        else:
            row["status"] = "EMPTY"
        row["resultant_profile_sha256"] = hashlib.sha256(
            json.dumps(
                resultant_profiles, sort_keys=True, separators=(",", ":")
            ).encode()
        ).hexdigest()
        del row["resultant_profiles"]
        if not row["unresolved"]:
            del row["unresolved"]
        pairing_rows.append(row)

    status_counts = dict(sorted(Counter(
        row["status"] for row in pairing_rows
    ).items()))
    return {
        "epsilon": [epsilon_1, epsilon_2],
        "point_index": point_index,
        "sigma_o": sigma_o,
        "common_point": {
            "b": b_value, "c": c_value, "r": r_value, "f": f_value,
        },
        "kernel": kernel,
        "status_counts": status_counts,
        "guarded_survivors": sum(
            row.get("guarded_count", 0) for row in pairing_rows
        ),
        "unresolved_count": sum(bool(row.get("unresolved"))
                                for row in pairing_rows),
        "pairing_rows": pairing_rows,
        "seconds": time.perf_counter()-started,
    }


@app.local_entrypoint()
def main():
    cases = tuple(
        (epsilon_1, epsilon_2, point_index, sigma_o)
        for epsilon_1, epsilon_2 in itertools.product((-1, 1), repeat=2)
        for point_index in range(4)
        for sigma_o in (-1, 1)
    )
    raw = list(replay.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]), "point_index": case[2],
                "sigma_o": case[3], "error": repr(row),
                "status": "REMOTE_ERROR",
            })
        else:
            rows.append({"status": "COMPLETE", **row})
    pairing_statuses = Counter(
        pairing["status"]
        for row in rows if row["status"] == "COMPLETE"
        for pairing in row["pairing_rows"]
    )
    output = {
        "schema": "rate-half-kb-positive-433-1b-o0b-cell3-bcplus-cf-pairing-v1",
        "scope": (
            "Exact deployed-field residual paired-product replay at all live "
            "CF necessary points; no squared-sum, source-label, or route claim."
        ),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "case_count": len(rows),
        "formal_system_count": len(rows)*len(MATCHINGS),
        "status_counts": dict(sorted(Counter(row["status"] for row in rows).items())),
        "pairing_status_counts": dict(sorted(pairing_statuses.items())),
        "guarded_survivor_count": sum(
            row.get("guarded_survivors", 0) for row in rows
        ),
        "unresolved_count": sum(row.get("unresolved_count", 0) for row in rows),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT),
        "status_counts": output["status_counts"],
        "pairing_status_counts": output["pairing_status_counts"],
        "guarded_survivor_count": output["guarded_survivor_count"],
        "unresolved_count": output["unresolved_count"],
        "maximum_seconds": max(
            (row.get("seconds", 0) for row in rows), default=0
        ),
    }, sort_keys=True))
