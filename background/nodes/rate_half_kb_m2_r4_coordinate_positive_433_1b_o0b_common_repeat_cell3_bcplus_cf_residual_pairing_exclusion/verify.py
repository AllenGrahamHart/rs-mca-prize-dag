#!/usr/bin/env python3
"""Verify the repeated-BC BC+ missing-CF residual exclusion."""

from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
LAUNCHER = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcplus_cf_residual_pairing_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcplus_cf_residual_pairing_result.json"
)
SOURCE = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcplus_colored_missing_roots_result.json"
)
LAUNCHER_SHA256 = "3328932c8eb69dae3ee7a37e3e25d0c53b4dd330176a7b182358bfec3419e099"
RESULT_SHA256 = "ed89203804b4e2e1b714f364fc61de60cbbbaa967539e51585aadf7ef237c0ee"
SOURCE_SHA256 = "88a0856e6d0dc7ef649095306d0758b18a3b84304dd8e6db4f80aac34d2f6c36"
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcplus_colored_missing_atlas"
TRANSPORT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cells3_6_full_system_transport"
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


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
    return trim([-item % PRIME for item in value])


def subtract(left, right):
    return add(left, negate(right))


def scale(value, scalar):
    return trim([scalar*item % PRIME for item in value])


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
        output = multiply(output, [-root % PRIME, 1])
    return monic(output)


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


def resultant(left, right, left_degree, right_degree):
    left = left+[0]*(left_degree+1-len(left))
    right = right+[0]*(right_degree+1-len(right))
    left_descending = list(reversed(left[:left_degree+1]))
    right_descending = list(reversed(right[:right_degree+1]))
    size = left_degree+right_degree
    matrix = []
    for shift in range(right_degree):
        matrix.append([0]*shift+left_descending
                      +[0]*(right_degree-1-shift))
    for shift in range(left_degree):
        matrix.append([0]*shift+right_descending
                      +[0]*(left_degree-1-shift))
    require(len(matrix) == size and all(len(row) == size for row in matrix),
            "Sylvester shape")
    return determinant(matrix)


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


def common_kernel(point):
    b_value, c_value, r_value = point["b"], point["u"], point["r"]
    r2 = r_value*r_value % PRIME
    r4 = r2*r2 % PRIME
    labels = (1, r4, PRIME-1, r2, -r2 % PRIME)
    products = (PRIME-1, b_value, c_value,
                b_value*c_value % PRIME, b_value*c_value % PRIME)
    matrix = [
        [-product % PRIME, -product*label % PRIME,
         -product*label*label % PRIME, 1, label, label*label % PRIME]
        for product, label in zip(products, labels)
    ]
    cofactors = []
    for column in range(6):
        minor = [row[:column]+row[column+1:] for row in matrix]
        cofactors.append(((-1)**column*determinant(minor)) % PRIME)
    scale_value = r4*(1-r4) % PRIME
    return [scale_value*value % PRIME for value in cofactors]


def polynomial_at(coefficients, value):
    return sum(coefficient*pow(value, index, PRIME)
               for index, coefficient in enumerate(coefficients)) % PRIME


def paired(a_values, b_values, left, right):
    p_values = [subtract([b_value], scale(left, a_value))
                for a_value, b_value in zip(a_values, b_values)]
    q_values = [
        subtract([b_values[0]], scale(right, a_values[0])),
        add([-b_values[1] % PRIME], scale(right, a_values[1])),
        subtract([b_values[2]], scale(right, a_values[2])),
    ]
    first = subtract(multiply(p_values[2], q_values[0]),
                     multiply(p_values[0], q_values[2]))
    second = subtract(multiply(p_values[2], q_values[1]),
                      multiply(p_values[1], q_values[2]))
    third = subtract(multiply(p_values[1], q_values[0]),
                     multiply(p_values[0], q_values[1]))
    return subtract(multiply(first, first), multiply(second, third))


def equations_at_d(kernel, point, sigma_o, matching, d_value):
    b_value = point["b"]
    f_value = point["missing_target_coordinate"]
    records = (
        [0, b_value],
        [0, d_value],
        [0, -d_value % PRIME],
        [d_value*f_value % PRIME],
        [-d_value*f_value % PRIME],
        [0, sigma_o*f_value % PRIME],
    )
    return [paired(kernel[:3], kernel[3:], records[left], records[right])
            for left, right in matching]


def verify_resultant(certificate, kernel, point, sigma_o, matching):
    selected = certificate["selected_equations"]
    require(len(selected) == 2 and len(set(selected)) == 2
            and all(index in range(3) for index in selected),
            "selected equations")
    stored = trim(certificate["selected_resultant_coefficients"])
    require(len(stored)-1 == certificate["selected_resultant_degree"]
            and len(stored) <= 17, "selected resultant degree")

    probes = [equations_at_d(kernel, point, sigma_o, matching, value)
              for value in range(33)]
    degrees = []
    for equation_index in selected:
        degree = max(len(probe[equation_index])-1 for probe in probes[:5])
        require(degree <= 4, "paired equation degree")
        degrees.append(degree)
    comparisons = []
    for value, equations in enumerate(probes):
        direct = resultant(
            equations[selected[0]], equations[selected[1]],
            degrees[0], degrees[1],
        )
        comparisons.append((evaluate(stored, value), direct))
    anchor = next(((left, right) for left, right in comparisons if left), None)
    require(anchor is not None and anchor[1], "resultant comparison anchor")
    scalar = anchor[1]*pow(anchor[0], -1, PRIME) % PRIME
    require(scalar and all(right == scalar*left % PRIME
                           for left, right in comparisons),
            "resultant interpolation")

    roots = certificate["selected_roots"]
    require(roots == sorted(set(roots)), "projected root normalization")
    field_part = gcd(stored, subtract(powmod([0, 1], PRIME, stored), [0, 1]))
    require(field_part == root_polynomial(roots), "projected root completeness")
    fibers = certificate["fiber_certificates"]
    require([fiber["free_value"] for fiber in fibers] == roots,
            "fiber indexing")
    for root, fiber in zip(roots, fibers):
        equations = equations_at_d(kernel, point, sigma_o, matching, root)
        common = equations[0]
        for equation in equations[1:]:
            common = gcd(common, equation)
        require(common == [1] and fiber["gcd_coefficients"] == [1]
                and fiber["other_roots"] == [], "unit residual fiber")
    return len(roots)


def cases(rows):
    return {(tuple(row["epsilon"]), row["point_index"], row["sigma_o"]): row
            for row in rows}


def validate(source, payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-cell3-bcplus-cf-pairing-v1",
            "schema")
    require(payload["source_sha256"] == SOURCE_SHA256, "source custody")
    require(payload["case_count"] == 32 and payload["formal_system_count"] == 480,
            "global census")
    require(payload["status_counts"] == {"COMPLETE": 32}
            and payload["pairing_status_counts"] == {"EMPTY": 480}
            and payload["guarded_survivor_count"] == payload["unresolved_count"] == 0,
            "global status")
    expected = set(itertools.product(
        itertools.product((-1, 1), repeat=2), range(4), (-1, 1)
    ))
    rows = cases(payload["rows"])
    require(set(rows) == expected and len(payload["rows"]) == 32, "case cover")
    source_rows = {
        tuple(row["epsilon"]): row for row in source["rows"]
        if row["missing_record"] == "CF"
    }
    require(set(source_rows) == set(itertools.product((-1, 1), repeat=2)),
            "source rows")

    degree_histogram = Counter()
    root_histogram = Counter()
    total_roots = 0
    for key in sorted(rows):
        epsilon, point_index, sigma_o = key
        row = rows[key]
        point = source_rows[epsilon]["points"][point_index]
        require(row["status"] == "COMPLETE"
                and row["common_point"] == {
                    "b": point["b"], "c": point["u"], "r": point["r"],
                    "f": point["missing_target_coordinate"],
                }, "common-point custody")
        kernel = common_kernel(point)
        require(row["kernel"] == kernel, "common kernel")
        r4 = pow(point["r"], 4, PRIME)
        missing = -r4 % PRIME
        source_product = (
            polynomial_at(kernel[3:], missing)
            * pow(polynomial_at(kernel[:3], missing), -1, PRIME)
        ) % PRIME
        require(source_product == point["source_product"]
                == point["u"]*point["missing_target_coordinate"] % PRIME,
                "CF reconstruction")
        pairing_rows = {item["pairing_index"]: item
                        for item in row["pairing_rows"]}
        require(set(pairing_rows) == set(range(15))
                and len(row["pairing_rows"]) == 15, "matching cover")
        for pairing_index, matching in enumerate(MATCHINGS):
            certificate = pairing_rows[pairing_index]
            require(certificate["status"] == "EMPTY"
                    and certificate["selected_free"] == "d"
                    and certificate["solution_count"] == 0
                    and certificate["guarded_count"] == 0,
                    "pairing status")
            roots = verify_resultant(
                certificate, kernel, point, sigma_o, matching
            )
            degree_histogram[certificate["selected_resultant_degree"]] += 1
            root_histogram[roots] += 1
            total_roots += roots
    require(degree_histogram == {8: 64, 12: 384, 16: 32}, "degree histogram")
    require(root_histogram == {0: 160, 1: 208, 2: 112}
            and total_roots == 432, "root histogram")


def main():
    require(hashlib.sha256(LAUNCHER.read_bytes()).hexdigest() == LAUNCHER_SHA256,
            "launcher hash")
    require(hashlib.sha256(RESULT.read_bytes()).hexdigest() == RESULT_SHA256,
            "result hash")
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256,
            "source hash")
    source = json.loads(SOURCE.read_text())
    payload = json.loads(RESULT.read_text())
    validate(source, payload)
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG status")
    for parent in (PARENT, TRANSPORT):
        require(nodes[parent]["status"] == "PROVED"
                and (parent, NODE.name, "req") in edges, f"parent {parent}")
    require((NODE.name, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_BCPLUS_CF_RESIDUAL_VERIFY_PASS systems=480 roots=432 unit_fibers=432 cell3_CF=120 cell6_BE=120")


if __name__ == "__main__":
    main()
