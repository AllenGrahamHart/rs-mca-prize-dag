#!/usr/bin/env python3
"""Direct finite-field replay on every guarded cell-11 guard boundary."""

from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import time

import modal


DIRECTORY = Path(__file__).parent
BOUNDARY = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_guard_boundary_classifier_result.json"
)
OUTPUT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_guard_boundary_direct_replay_result.json"
)
EXPECTED_BOUNDARY_SHA256 = (
    "e01e1a6ceaf55f530c0bd62549c9d64b18e5eeacc5a95be24c543c18f6fbcac5"
)
PRIME = 2130706433
IOTA = 16711679
GLOBAL_RECORDS = ("BE", "CF", "DE+", "DE-", "DF+", "DF-", "EF")
MISSING_RECORDS = ("DE+", "DF+", "EF")


def canonical_matchings(items):
    if not items:
        return ((),)
    output = []
    for index in range(1, len(items)):
        rest = items[1:index] + items[index + 1:]
        for tail in canonical_matchings(rest):
            output.append(((items[0], items[index]),) + tail)
    return tuple(output)


MATCHINGS = canonical_matchings(tuple(range(6)))

app = modal.App("rs-mca-positive-433-1b-o0b-cell11-guard-direct-replay")
image = modal.Image.debian_slim(python_version="3.12").pip_install(
    "python-flint==0.8.0"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def point_digest(point):
    payload = {
        key: point[key]
        for key in ("b", "c", "r", "t", "x", "y")
    }
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


@app.function(image=image, cpu=1.0, memory=1024, timeout=120, max_containers=8)
def replay(row):
    from flint import fmpz_mod_poly_ctx

    started = time.perf_counter()
    epsilon_1, epsilon_2 = row["epsilon"]
    bc_sign = row["bc_sign"]
    polynomial_context = fmpz_mod_poly_ctx(PRIME)
    variable = polynomial_context([0, 1])

    def scalar(value):
        return value % PRIME

    def inverse(value):
        value %= PRIME
        if not value:
            raise ZeroDivisionError("zero finite-field denominator")
        return pow(value, -1, PRIME)

    def determinant(matrix):
        size = len(matrix)
        total = 0
        for permutation in itertools.permutations(range(size)):
            inversions = sum(
                permutation[left] > permutation[right]
                for left in range(size)
                for right in range(left + 1, size)
            )
            term = -1 if inversions % 2 else 1
            for matrix_row, column in enumerate(permutation):
                term = term * matrix[matrix_row][column] % PRIME
            total = (total + term) % PRIME
        return total

    def evaluate(coefficients, value):
        output = 0
        for coefficient in reversed(coefficients):
            output = (output * value + coefficient) % PRIME
        return output

    def common_data(point):
        b, c, r, t, x = (
            point[key] % PRIME for key in ("b", "c", "r", "t", "x")
        )
        require(x == b * c % PRIME, "point product")
        require(point["y"] % PRIME == (b + c) % PRIME, "point sum")
        require(
            t == epsilon_1 * epsilon_2 * r * r % PRIME,
            "source-sign relation",
        )
        roots = (
            1,
            r,
            epsilon_2 * IOTA * r % PRIME,
            t,
            epsilon_1 * IOTA % PRIME,
        )
        labels = tuple(root * root % PRIME for root in roots)
        products = (
            PRIME - 1,
            b,
            c,
            bc_sign * x % PRIME,
            bc_sign * x % PRIME,
        )
        sums = (
            0,
            (1 + b) % PRIME,
            (1 + c) % PRIME,
            (b + bc_sign * c) % PRIME,
            (b + bc_sign * c) % PRIME,
        )
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
            minor = [
                matrix_row[:column] + matrix_row[column + 1:]
                for matrix_row in matrix
            ]
            cofactor = determinant(minor)
            cofactors.append((-cofactor if column % 2 else cofactor) % PRIME)
        a_values, b_values = tuple(cofactors[:3]), tuple(cofactors[3:])
        pivot_label = labels[1]
        pivot_denominator = pivot_label * (1 - pivot_label) % PRIME
        if not pivot_denominator:
            raise ZeroDivisionError("pivot beta denominator")
        pivot_q = roots[1] * sums[1] % PRIME
        beta_0 = (
            -pivot_q * evaluate(a_values, pivot_label)
            * inverse(pivot_denominator)
        ) % PRIME
        beta_1 = -beta_0 % PRIME
        q_values = tuple(
            root * edge_sum % PRIME for root, edge_sum in zip(roots, sums)
        )
        product_checks = tuple(
            sum(value * cofactor for value, cofactor in zip(matrix_row, cofactors))
            % PRIME
            for matrix_row in matrix
        )
        sum_checks = tuple(
            (
                q_value * evaluate(a_values, label)
                + label * (beta_0 + beta_1 * label)
            ) % PRIME
            for q_value, label in zip(q_values, labels)
        )
        require(not any(product_checks), "product interpolation checks")
        require(not any(sum_checks), "sum interpolation checks")
        missing_label = -t * t % PRIME
        a_missing = evaluate(a_values, missing_label)
        if not a_missing:
            raise ZeroDivisionError("missing-label reconstruction denominator")
        b_missing = evaluate(b_values, missing_label)
        beta_missing = (beta_0 + beta_1 * missing_label) % PRIME
        missing_product = b_missing * inverse(a_missing) % PRIME
        missing_sum_squared = (
            missing_label * beta_missing * beta_missing
            * inverse(a_missing) * inverse(a_missing)
        ) % PRIME
        return {
            "a_values": a_values,
            "b_values": b_values,
            "missing_product": missing_product,
            "missing_sum_squared": missing_sum_squared,
        }

    def polynomial(value):
        if hasattr(value, "degree"):
            return value
        return polynomial_context([value % PRIME])

    def paired(left, right, a_values, b_values):
        p_values = [
            polynomial(b_coefficient) - left * a_coefficient
            for a_coefficient, b_coefficient in zip(a_values, b_values)
        ]
        q_values = (
            polynomial(b_values[0]) - right * a_values[0],
            polynomial(-b_values[1]) + right * a_values[1],
            polynomial(b_values[2]) - right * a_values[2],
        )
        return (
            (p_values[2] * q_values[0] - p_values[0] * q_values[2]) ** 2
            - (p_values[2] * q_values[1] - p_values[1] * q_values[2])
            * (p_values[1] * q_values[0] - p_values[0] * q_values[1])
        )

    denominator_failures = []
    colored_candidates = []
    uncolored_candidates = []
    point_rows = []
    uncolored_formal_case_count = 0
    for point in row["source_points"]:
        digest = point_digest(point)
        try:
            common = common_data(point)
        except ZeroDivisionError as error:
            denominator_failures.append({
                "point_sha256": digest,
                "error": str(error),
            })
            continue
        b, c = point["b"] % PRIME, point["c"] % PRIME
        q_value = common["missing_product"]
        sum_squared = common["missing_sum_squared"]
        for missing_record, base in (("BE", b), ("CF", c)):
            if not base:
                denominator_failures.append({
                    "point_sha256": digest,
                    "error": f"zero colored base {missing_record}",
                })
                continue
            endpoint = q_value * inverse(base) % PRIME
            consistency = ((base + endpoint) ** 2 - sum_squared) % PRIME
            if not consistency:
                colored_candidates.append({
                    "point_sha256": digest,
                    "missing_record": missing_record,
                    "endpoint": endpoint,
                })
        quartic = polynomial_context([
            q_value * q_value % PRIME,
            0,
            (2 * q_value - sum_squared) % PRIME,
            0,
            1,
        ])
        endpoint_roots = sorted(
            (int(root) % PRIME, int(multiplicity))
            for root, multiplicity in quartic.roots()
        )
        point_rows.append({
            "point_sha256": digest,
            "missing_product": q_value,
            "missing_sum_squared": sum_squared,
            "endpoint_roots": [
                {"value": value, "multiplicity": multiplicity}
                for value, multiplicity in endpoint_roots
            ],
        })
        if not q_value:
            denominator_failures.append({
                "point_sha256": digest,
                "error": "zero missing product",
            })
            continue
        for endpoint, _ in endpoint_roots:
            if not endpoint:
                denominator_failures.append({
                    "point_sha256": digest,
                    "error": "zero endpoint with nonzero product",
                })
                continue
            partner = q_value * inverse(endpoint) % PRIME
            for missing_record, sigma_o, pairing_index in itertools.product(
                MISSING_RECORDS, (-1, 1), range(15)
            ):
                uncolored_formal_case_count += 1
                if missing_record == "DE+":
                    records = {
                        "BE": polynomial(b * partner),
                        "CF": variable * c,
                        "DE-": polynomial(-q_value),
                        "DF+": variable * endpoint,
                        "DF-": -(variable * endpoint),
                        "EF": variable * (sigma_o * partner),
                    }
                elif missing_record == "DF+":
                    records = {
                        "BE": variable * b,
                        "CF": polynomial(c * partner),
                        "DE+": variable * endpoint,
                        "DE-": -(variable * endpoint),
                        "DF-": polynomial(-q_value),
                        "EF": variable * (sigma_o * partner),
                    }
                else:
                    f_value = sigma_o * partner % PRIME
                    records = {
                        "BE": polynomial(b * endpoint),
                        "CF": polynomial(c * f_value),
                        "DE+": variable * endpoint,
                        "DE-": -(variable * endpoint),
                        "DF+": variable * f_value,
                        "DF-": -(variable * f_value),
                    }
                residual_names = tuple(
                    name for name in GLOBAL_RECORDS if name != missing_record
                )
                residual = tuple(records[name] for name in residual_names)
                matching = MATCHINGS[pairing_index]
                equations = [
                    paired(
                        residual[left], residual[right],
                        common["a_values"], common["b_values"],
                    )
                    for left, right in matching
                ]
                nonzero = [equation for equation in equations if not equation.is_zero()]
                if not nonzero:
                    candidate_roots = [(0, 1)]
                    common_polynomial_degree = -1
                else:
                    common_polynomial = nonzero[0]
                    for equation in nonzero[1:]:
                        common_polynomial = common_polynomial.gcd(equation)
                    common_polynomial_degree = int(common_polynomial.degree())
                    candidate_roots = sorted(
                        (int(root) % PRIME, int(multiplicity))
                        for root, multiplicity in common_polynomial.roots()
                    )
                for free_endpoint, multiplicity in candidate_roots:
                    if any(
                        int(equation(free_endpoint)) % PRIME
                        for equation in equations
                    ):
                        raise RuntimeError("reported free endpoint is not common")
                    uncolored_candidates.append({
                        "point_sha256": digest,
                        "missing_record": missing_record,
                        "sigma_o": sigma_o,
                        "pairing_index": pairing_index,
                        "endpoint": endpoint,
                        "partner": partner,
                        "free_endpoint": free_endpoint,
                        "root_multiplicity": multiplicity,
                        "common_polynomial_degree": common_polynomial_degree,
                    })
    status = (
        "DIRECT_BOUNDARY_CANDIDATE_PRESENT"
        if denominator_failures or colored_candidates or uncolored_candidates
        else "DIRECT_BOUNDARY_EXCLUDED"
    )
    return {
        "epsilon": row["epsilon"],
        "bc_sign": bc_sign,
        "source_point_count": len(row["source_points"]),
        "point_rows": point_rows,
        "colored_case_count": 2 * len(row["source_points"]),
        "uncolored_formal_case_count": uncolored_formal_case_count,
        "denominator_failures": denominator_failures,
        "colored_candidates": colored_candidates,
        "uncolored_candidates": uncolored_candidates,
        "status": status,
        "seconds": time.perf_counter() - started,
    }


@app.local_entrypoint()
def main():
    require(
        hashlib.sha256(BOUNDARY.read_bytes()).hexdigest()
        == EXPECTED_BOUNDARY_SHA256,
        "boundary classifier SHA-256",
    )
    boundary = json.loads(BOUNDARY.read_text())
    require(
        boundary["schema"]
        == "kb-positive-433-1b-o0b-cell11-guard-boundary-classifier-v1",
        "boundary schema",
    )
    require(boundary["case_count"] == len(boundary["rows"]) == 8, "row census")
    worker_rows = []
    all_point_keys = []
    for row in boundary["rows"]:
        source_points = []
        for root_row in row["root_rows"]:
            for point in root_row["source_points"]:
                if not point.get("guarded"):
                    continue
                require(point["bc_matches_x"], "classifier point product")
                require(point["common_equations_zero"], "classifier equations")
                require(point["common_guard_nonzero"], "classifier source guard")
                source_points.append(point)
                all_point_keys.append((
                    row["bc_sign"], tuple(row["epsilon"]), point_digest(point)
                ))
        worker_rows.append({
            "epsilon": row["epsilon"],
            "bc_sign": row["bc_sign"],
            "source_points": source_points,
        })
    require(len(all_point_keys) == len(set(all_point_keys)) == 160, "point census")
    raw = list(replay.map(worker_rows, order_outputs=True, return_exceptions=True))
    rows = []
    for worker_row, result in zip(worker_rows, raw):
        if isinstance(result, BaseException):
            rows.append({
                "epsilon": worker_row["epsilon"],
                "bc_sign": worker_row["bc_sign"],
                "source_point_count": len(worker_row["source_points"]),
                "status": "REMOTE_ERROR",
                "error": repr(result),
            })
        else:
            rows.append(result)
    output = {
        "schema": "kb-positive-433-1b-o0b-cell11-guard-direct-replay-v1",
        "statement": (
            "Direct finite-field reconstruction and colored/uncolored paired-"
            "product replay on every guarded source point lying on a registered "
            "cell-11 construction guard."
        ),
        "boundary_classifier_sha256": EXPECTED_BOUNDARY_SHA256,
        "source_tower_count": len(rows),
        "source_point_count": sum(row["source_point_count"] for row in rows),
        "colored_case_count": sum(row.get("colored_case_count", 0) for row in rows),
        "uncolored_formal_case_count": sum(
            row.get("uncolored_formal_case_count", 0) for row in rows
        ),
        "denominator_failure_count": sum(
            len(row.get("denominator_failures", ())) for row in rows
        ),
        "colored_candidate_count": sum(
            len(row.get("colored_candidates", ())) for row in rows
        ),
        "uncolored_candidate_count": sum(
            len(row.get("uncolored_candidates", ())) for row in rows
        ),
        "status_counts": dict(sorted(Counter(row["status"] for row in rows).items())),
        "rows": rows,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        key: output[key]
        for key in (
            "source_tower_count", "source_point_count", "colored_case_count",
            "uncolored_formal_case_count", "denominator_failure_count",
            "colored_candidate_count", "uncolored_candidate_count", "status_counts",
        )
    }, sort_keys=True))
