#!/usr/bin/env python3
"""Pure-Python verifier core for the uncolored repeated-BC certificates."""

import ast
from collections import Counter
from functools import lru_cache
import hashlib
import itertools
import json


PRIME = 2130706433
IOTA = 16711679
GLOBAL_RECORDS = ("BE", "CF", "DE+", "DE-", "DF+", "DF-", "EF")
MISSING_RECORDS = ("DE+", "DF+", "EF")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest_values(values):
    return hashlib.sha256(json.dumps(
        values, separators=(",", ":")
    ).encode()).hexdigest()


def trim(value):
    value = [item % PRIME for item in value]
    while len(value) > 1 and value[-1] == 0:
        value.pop()
    return value or [0]


def add(left, right):
    size = max(len(left), len(right))
    return trim([
        ((left[index] if index < len(left) else 0)
         + (right[index] if index < len(right) else 0)) % PRIME
        for index in range(size)
    ])


def negate(value):
    return trim([-item for item in value])


def subtract(left, right):
    return add(left, negate(right))


def scale(value, scalar):
    return trim([scalar*item for item in value])


def multiply(left, right):
    output = [0]*(len(left)+len(right)-1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            output[left_index+right_index] = (
                output[left_index+right_index]+left_value*right_value
            ) % PRIME
    return trim(output)


def divide(dividend, divisor):
    dividend, divisor = trim(dividend), trim(divisor)
    require(divisor != [0], "zero polynomial divisor")
    quotient = [0]*max(1, len(dividend)-len(divisor)+1)
    work = dividend[:]
    inverse = pow(divisor[-1], -1, PRIME)
    while work != [0] and len(work) >= len(divisor):
        shift = len(work)-len(divisor)
        coefficient = work[-1]*inverse % PRIME
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            work[shift+index] = (
                work[shift+index]-coefficient*value
            ) % PRIME
        work = trim(work)
    return trim(quotient), work


def monic(value):
    value = trim(value)
    if value == [0]:
        return value
    return scale(value, pow(value[-1], -1, PRIME))


def gcd(left, right):
    left, right = trim(left), trim(right)
    while right != [0]:
        _, remainder = divide(left, right)
        left, right = right, remainder
    return monic(left)


def powmod(base, exponent, modulus):
    modulus = trim(modulus)
    require(modulus not in ([0], [1]), "nonconstant modulus required")
    output = [1]
    _, base = divide(base, modulus)
    while exponent:
        if exponent & 1:
            _, output = divide(multiply(output, base), modulus)
        _, base = divide(multiply(base, base), modulus)
        exponent //= 2
    return trim(output)


def evaluate(polynomial, value):
    output = 0
    for coefficient in reversed(polynomial):
        output = (output*value+coefficient) % PRIME
    return output


def root_polynomial(roots):
    output = [1]
    for root in roots:
        output = multiply(output, [-root, 1])
    return monic(output)


def certify_roots(polynomial, roots, label):
    polynomial = trim(polynomial)
    roots = list(roots)
    require(roots == sorted(set(roots)), f"{label}: root normalization")
    if len(polynomial) == 1:
        require(polynomial != [0] and not roots, f"{label}: constant roots")
        return
    field_part = gcd(
        polynomial,
        subtract(powmod([0, 1], PRIME, polynomial), [0, 1]),
    )
    require(field_part == root_polynomial(roots),
            f"{label}: deployed-field root completeness")


def determinant(matrix):
    matrix = [[value % PRIME for value in row] for row in matrix]
    output = 1
    for column in range(len(matrix)):
        pivot = next((
            row for row in range(column, len(matrix))
            if matrix[row][column]
        ), None)
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


def pairings(values):
    values = tuple(values)
    if not values:
        return ((),)
    output = []
    for index in range(1, len(values)):
        for tail in pairings(values[1:index]+values[index+1:]):
            output.append(((values[0], values[index]),)+tail)
    return tuple(output)


MATCHINGS = pairings(range(6))


def polynomial_value(coefficients, value):
    return sum(coefficient*pow(value, index, PRIME)
               for index, coefficient in enumerate(coefficients)) % PRIME


def paired(a_values, b_values, left, right):
    p_values = [subtract([b_value], scale(left, a_value))
                for a_value, b_value in zip(a_values, b_values)]
    q_values = [
        subtract([b_values[0]], scale(right, a_values[0])),
        add([-b_values[1]], scale(right, a_values[1])),
        subtract([b_values[2]], scale(right, a_values[2])),
    ]
    first = subtract(multiply(p_values[2], q_values[0]),
                     multiply(p_values[0], q_values[2]))
    second = subtract(multiply(p_values[2], q_values[1]),
                      multiply(p_values[1], q_values[2]))
    third = subtract(multiply(p_values[1], q_values[0]),
                     multiply(p_values[0], q_values[1]))
    return subtract(multiply(first, first), multiply(second, third))


@lru_cache(maxsize=8)
def guard_tree(expression):
    return ast.parse(expression, mode="eval")


def evaluate_guard(expression, r_value, u_value):
    def visit(node):
        if isinstance(node, ast.Expression):
            return visit(node.body)
        if isinstance(node, ast.Constant):
            return int(node.value) % PRIME
        if isinstance(node, ast.Name):
            require(node.id in ("r", "u"), "guard variable")
            return {"r": r_value, "u": u_value}[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -visit(node.operand) % PRIME
        if isinstance(node, ast.BinOp):
            left, right = visit(node.left), visit(node.right)
            if isinstance(node.op, ast.Add):
                return (left+right) % PRIME
            if isinstance(node.op, ast.Sub):
                return (left-right) % PRIME
            if isinstance(node.op, ast.Mult):
                return left*right % PRIME
            if isinstance(node.op, ast.Pow):
                return pow(left, right, PRIME)
        raise RuntimeError(f"unsupported guard AST: {ast.dump(node)}")

    return visit(guard_tree(expression))


def common_data(epsilon, u_value, r_value):
    epsilon_1, epsilon_2 = epsilon
    require(u_value != 0, "unguarded u=0")
    b_value = -pow(u_value, -3, PRIME) % PRIME
    c_value = u_value
    r2, r4 = r_value*r_value % PRIME, pow(r_value, 4, PRIME)
    labels = (1, r4, PRIME-1, r2, -r2 % PRIME)
    products = (PRIME-1, b_value, c_value,
                b_value*c_value % PRIME, b_value*c_value % PRIME)
    matrix = [
        [-product, -product*label, -product*label*label,
         1, label, label*label]
        for product, label in zip(products, labels)
    ]
    cofactors = []
    for column in range(6):
        minor = [row[:column]+row[column+1:] for row in matrix]
        cofactors.append(((-1)**column*determinant(minor)) % PRIME)
    kernel = [r4*(1-r4)*value % PRIME for value in cofactors]
    a_values, b_values = kernel[:3], kernel[3:]
    a_pivot = sum(cofactors[index]*pow(r4, index, PRIME)
                  for index in range(3)) % PRIME
    beta_0 = -epsilon_1*epsilon_2*r2*(1+b_value)*a_pivot % PRIME
    beta_1 = -beta_0 % PRIME
    missing_label = -r4 % PRIME
    a_missing = polynomial_value(a_values, missing_label)
    b_missing = polynomial_value(b_values, missing_label)
    beta_missing = (beta_0+beta_1*missing_label) % PRIME
    return {
        "b": b_value,
        "c": c_value,
        "a": a_values,
        "beta": b_values,
        "missing_label": missing_label,
        "a_missing": a_missing,
        "b_missing": b_missing,
        "beta_missing": beta_missing,
    }


def residual_records(missing_record, data, sigma_o, endpoint, other, q_value):
    b_value, c_value = data["b"], data["c"]
    if missing_record == "DE+":
        return {
            "BE": [b_value*other],
            "CF": [0, c_value],
            "DE-": [-q_value],
            "DF+": [0, endpoint],
            "DF-": [0, -endpoint],
            "EF": [0, sigma_o*other],
        }
    if missing_record == "DF+":
        return {
            "BE": [0, b_value],
            "CF": [c_value*other],
            "DE+": [0, endpoint],
            "DE-": [0, -endpoint],
            "DF-": [-q_value],
            "EF": [0, sigma_o*other],
        }
    require(missing_record == "EF", "missing record")
    f_value = sigma_o*other % PRIME
    return {
        "BE": [b_value*endpoint],
        "CF": [c_value*f_value],
        "DE+": [0, endpoint],
        "DE-": [0, -endpoint],
        "DF+": [0, f_value],
        "DF-": [0, -f_value],
    }


def case_key(row):
    return (tuple(row["epsilon"]), row["missing_record"],
            row["sigma_o"], row["pairing_index"])


def validate_exceptional(missing_record, payload, generic, roots, torus):
    require(missing_record in MISSING_RECORDS, "record scope")
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-cell3-bcplus-uncolored-exceptional-shard-v1",
            "shard schema")
    require(payload["missing_record"] == missing_record, "shard record")
    require(payload["case_count"] == 120
            and payload["status_counts"] == {"COMPLETE": 120}
            and payload["survivor_count"] == 0
            and payload["unresolved_count"] == 0, "shard summary")

    expected = set(itertools.product(
        itertools.product((-1, 1), repeat=2),
        (missing_record,), (-1, 1), range(15),
    ))
    rows = {case_key(row): row for row in payload["rows"]}
    require(len(rows) == len(payload["rows"]) == 120
            and set(rows) == expected, "shard case cover")
    generic_rows = {case_key(row): row for row in generic["rows"]}
    roots_by_hash = {row["sha256"]: row["roots"] for row in roots["rows"]}
    torus_rows = {tuple(row["epsilon"]): row for row in torus["rows"]}

    total_fibers = 0
    total_endpoint_rows = 0
    all_statuses = Counter()
    for key in sorted(rows):
        epsilon, _, sigma_o, pairing_index = key
        row = rows[key]
        generic_row = generic_rows[key]
        require(row["status"] == "COMPLETE"
                and row["survivor_count"] == 0
                and row["survivors"] == []
                and row["unresolved"] == [], "case status")
        require(generic_row["status"] == "GENERIC_UNIT", "generic status")
        expected_u = sorted({
            value for digest in generic_row["guard_hashes"]
            for value in roots_by_hash[digest]
        })
        require(row["u_values"] == expected_u, "exceptional u cover")

        fibers = {(fiber["u"], fiber["r"]): fiber
                  for fiber in row["fibers"]}
        require(len(fibers) == len(row["fibers"]) == row["fiber_count"],
                "fiber uniqueness")
        fibers_by_u = {}
        for (u_value, r_value), fiber in fibers.items():
            fibers_by_u.setdefault(u_value, []).append(r_value)
        require(set(fibers_by_u) <= set(expected_u), "u lift support")
        for u_value in expected_u:
            h_polynomial = [
                epsilon[1]*IOTA*u_value,
                -epsilon[0]*(IOTA+epsilon[1])*(u_value*u_value+1),
                u_value,
            ]
            certify_roots(
                h_polynomial, sorted(fibers_by_u.get(u_value, [])),
                f"torus {epsilon}/{u_value}",
            )

        status_counts = Counter()
        expression = torus_rows[epsilon]["transformed_guard"]["expression"]
        residual_names = tuple(
            name for name in GLOBAL_RECORDS if name != missing_record
        )
        matching = MATCHINGS[pairing_index]
        for (u_value, r_value), fiber in sorted(fibers.items()):
            guard_zero = evaluate_guard(expression, r_value, u_value) == 0
            if guard_zero:
                require(fiber["status"] == "COMMON_GUARD_BOUNDARY",
                        "common boundary status")
                status_counts[fiber["status"]] += 1
                continue

            data = common_data(epsilon, u_value, r_value)
            a_missing, b_missing = data["a_missing"], data["b_missing"]
            if a_missing == 0:
                require(b_missing != 0
                        and fiber["status"] == "MISSING_PRODUCT_INCONSISTENT",
                        "missing-product inconsistency")
                status_counts[fiber["status"]] += 1
                continue

            q_value = b_missing*pow(a_missing, -1, PRIME) % PRIME
            sum_squared = (
                data["missing_label"]*data["beta_missing"]**2
                * pow(a_missing, -2, PRIME)
            ) % PRIME
            require(fiber["q"] == q_value
                    and fiber["sum_squared"] == sum_squared,
                    "missing-edge reconstruction")
            if q_value == 0:
                require(fiber["status"] == "ZERO_MISSING_PRODUCT_BOUNDARY",
                        "zero missing product")
                status_counts[fiber["status"]] += 1
                continue

            endpoint_polynomial = [
                q_value*q_value, 0, 2*q_value-sum_squared, 0, 1,
            ]
            endpoint_roots = fiber["endpoint_roots"]
            certify_roots(endpoint_polynomial, endpoint_roots,
                          "missing endpoint quartic")
            endpoint_rows = {item["endpoint"]: item
                             for item in fiber["endpoint_rows"]}
            require(len(endpoint_rows) == len(fiber["endpoint_rows"])
                    and set(endpoint_rows) == set(endpoint_roots),
                    "endpoint cover")
            for endpoint in endpoint_roots:
                endpoint_row = endpoint_rows[endpoint]
                other = q_value*pow(endpoint, -1, PRIME) % PRIME
                require(endpoint_row["other"] == other
                        and endpoint*other % PRIME == q_value
                        and pow(endpoint+other, 2, PRIME) == sum_squared,
                        "endpoint reconstruction")
                records = residual_records(
                    missing_record, data, sigma_o, endpoint, other, q_value
                )
                residual = tuple(records[name] for name in residual_names)
                equations = [
                    paired(data["a"], data["beta"],
                           residual[left], residual[right])
                    for left, right in matching
                ]
                common = equations[0]
                for equation in equations[1:]:
                    common = gcd(common, equation)
                require(common == [1]
                        and endpoint_row["gcd_degree"] == 0
                        and endpoint_row["y_roots"] == []
                        and endpoint_row["status"] == "EMPTY_RESIDUAL_GCD",
                        "unit residual gcd")
                total_endpoint_rows += 1
            require(fiber["status"] == "EMPTY_ENDPOINT_FIBERS",
                    "empty endpoint status")
            status_counts[fiber["status"]] += 1

        require(dict(sorted(status_counts.items())) == row["status_counts"],
                "case status census")
        total_fibers += len(fibers)
        all_statuses.update(status_counts)

    require(total_fibers == payload["fiber_count"], "shard fiber census")
    expected_profiles = {
        "DE+": (2488, 1792, {
            "COMMON_GUARD_BOUNDARY": 1560,
            "EMPTY_ENDPOINT_FIBERS": 448,
            "MISSING_PRODUCT_INCONSISTENT": 240,
            "ZERO_MISSING_PRODUCT_BOUNDARY": 240,
        }),
        "DF+": (2248, 832, {
            "COMMON_GUARD_BOUNDARY": 1560,
            "EMPTY_ENDPOINT_FIBERS": 208,
            "MISSING_PRODUCT_INCONSISTENT": 240,
            "ZERO_MISSING_PRODUCT_BOUNDARY": 240,
        }),
        "EF": (2264, 896, {
            "COMMON_GUARD_BOUNDARY": 1560,
            "EMPTY_ENDPOINT_FIBERS": 224,
            "MISSING_PRODUCT_INCONSISTENT": 240,
            "ZERO_MISSING_PRODUCT_BOUNDARY": 240,
        }),
    }
    expected_fibers, expected_endpoints, expected_statuses = (
        expected_profiles[missing_record]
    )
    require(total_fibers == expected_fibers
            and total_endpoint_rows == expected_endpoints
            and dict(sorted(all_statuses.items())) == expected_statuses,
            "record census")
    return {
        "cases": 120,
        "fibers": total_fibers,
        "endpoint_rows": total_endpoint_rows,
    }
