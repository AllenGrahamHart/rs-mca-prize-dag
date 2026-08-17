#!/usr/bin/env python3
"""Verify the repeated-BC cell-11 registered-guard boundary exclusion."""

from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell11_symmetric_function_field_tower",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell11_common_kernel_reconstruction",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell11_uncolored_generic_rank_atlas",
)
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
PRIME = 2130706433
IOTA = 16711679
GLOBAL_RECORDS = ("BE", "CF", "DE+", "DE-", "DF+", "DF-", "EF")
MISSING_RECORDS = ("DE+", "DF+", "EF")
FILES = {
    "classifier_launcher": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_guard_boundary_classifier_modal.py",
        "028de7a757f27fa5179c9b79d0c41d194093b008e482f84493884cd98146f105",
    ),
    "classifier_result": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_guard_boundary_classifier_result.json",
        "e01e1a6ceaf55f530c0bd62549c9d64b18e5eeacc5a95be24c543c18f6fbcac5",
    ),
    "replay_launcher": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_guard_boundary_direct_replay_modal.py",
        "40639f55d76c628b28982d52bd1cb7751f33fceb5de035d98a7649ba89681617",
    ),
    "replay_result": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_guard_boundary_direct_replay_result.json",
        "9b7f9907253e05c2d197b1e126962d3a8c9bc563be0e315353b368d47bd9efb0",
    ),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def trim(value):
    value = [item % PRIME for item in value]
    while len(value) > 1 and value[-1] == 0:
        value.pop()
    return tuple(value or (0,))


def add(left, right):
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    ])


def neg(value):
    return trim([-item for item in value])


def sub(left, right):
    return add(left, neg(right))


def mul(left, right):
    output = [0] * (len(left) + len(right) - 1)
    for left_degree, left_value in enumerate(left):
        for right_degree, right_value in enumerate(right):
            output[left_degree + right_degree] += left_value * right_value
    return trim(output)


def scale(value, scalar):
    return trim([scalar * item for item in value])


def power(value, exponent):
    output, base = (1,), value
    while exponent:
        if exponent & 1:
            output = mul(output, base)
        base = mul(base, base)
        exponent //= 2
    return output


def divmod_poly(dividend, divisor):
    dividend, divisor = list(trim(dividend)), trim(divisor)
    require(divisor != (0,), "zero polynomial divisor")
    if len(dividend) < len(divisor):
        return (0,), trim(dividend)
    quotient = [0] * (len(dividend) - len(divisor) + 1)
    inverse_lead = pow(divisor[-1], -1, PRIME)
    while len(dividend) >= len(divisor) and any(dividend):
        degree = len(dividend) - len(divisor)
        coefficient = dividend[-1] * inverse_lead % PRIME
        quotient[degree] = coefficient
        for index, value in enumerate(divisor):
            dividend[degree + index] = (
                dividend[degree + index] - coefficient * value
            ) % PRIME
        while len(dividend) > 1 and dividend[-1] == 0:
            dividend.pop()
    return trim(quotient), trim(dividend)


def monic(value):
    value = trim(value)
    if value == (0,):
        return value
    return scale(value, pow(value[-1], -1, PRIME))


def gcd(left, right):
    left, right = trim(left), trim(right)
    while right != (0,):
        _, remainder = divmod_poly(left, right)
        left, right = right, remainder
    return monic(left)


def mod_poly(value, modulus):
    return divmod_poly(value, modulus)[1]


def powmod_poly(value, exponent, modulus):
    output, base = (1,), mod_poly(value, modulus)
    while exponent:
        if exponent & 1:
            output = mod_poly(mul(output, base), modulus)
        base = mod_poly(mul(base, base), modulus)
        exponent //= 2
    return output


def evaluate(value, point):
    output = 0
    for coefficient in reversed(value):
        output = (output * point + coefficient) % PRIME
    return output


def field_root_polynomial(value):
    value = monic(value)
    if len(value) <= 1:
        return (1,)
    variable = (0, 1)
    return gcd(value, sub(powmod_poly(variable, PRIME, value), variable))


def root_product(roots):
    output = (1,)
    for root in sorted(set(roots)):
        output = mul(output, (-root % PRIME, 1))
    return monic(output)


def root_multiplicity(value, root):
    divisor = (-root % PRIME, 1)
    multiplicity = 0
    while True:
        quotient, remainder = divmod_poly(value, divisor)
        if remainder != (0,):
            return multiplicity
        multiplicity += 1
        value = quotient


def determinant(matrix):
    work = [[value % PRIME for value in row] for row in matrix]
    output = 1
    for column in range(len(work)):
        pivot = next(
            (row for row in range(column, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            output = -output % PRIME
        pivot_value = work[column][column]
        output = output * pivot_value % PRIME
        inverse = pow(pivot_value, -1, PRIME)
        for row in range(column + 1, len(work)):
            scalar = work[row][column] * inverse % PRIME
            for target in range(column, len(work)):
                work[row][target] = (
                    work[row][target] - scalar * work[column][target]
                ) % PRIME
    return output


def point_digest(point):
    payload = {key: point[key] for key in ("b", "c", "r", "t", "x", "y")}
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


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


def common_data(point, epsilon, bc_sign):
    epsilon_1, epsilon_2 = epsilon
    b, c, r, t, x = (point[key] % PRIME for key in ("b", "c", "r", "t", "x"))
    require(x == b * c % PRIME and point["y"] % PRIME == (b + c) % PRIME,
            "source symmetric coordinates")
    require(t == epsilon_1 * epsilon_2 * r * r % PRIME, "source sign")
    roots = (1, r, epsilon_2 * IOTA * r % PRIME, t, epsilon_1 * IOTA % PRIME)
    labels = tuple(root * root % PRIME for root in roots)
    products = (PRIME - 1, b, c, bc_sign * x % PRIME, bc_sign * x % PRIME)
    sums = (0, (1 + b) % PRIME, (1 + c) % PRIME,
            (b + bc_sign * c) % PRIME, (b + bc_sign * c) % PRIME)
    matrix = [[-product % PRIME, -product * label % PRIME,
               -product * label * label % PRIME, 1, label,
               label * label % PRIME]
              for product, label in zip(products, labels)]
    cofactors = []
    for column in range(6):
        minor = [row[:column] + row[column + 1:] for row in matrix]
        value = determinant(minor)
        cofactors.append((-value if column % 2 else value) % PRIME)
    a_values, b_values = tuple(cofactors[:3]), tuple(cofactors[3:])
    poly_at = lambda coefficients, value: sum(
        coefficient * pow(value, index, PRIME)
        for index, coefficient in enumerate(coefficients)
    ) % PRIME
    require(all(sum(value * cofactor for value, cofactor in zip(row, cofactors))
                % PRIME == 0 for row in matrix), "product interpolation")
    pivot_label = labels[1]
    pivot_denominator = pivot_label * (1 - pivot_label) % PRIME
    require(pivot_denominator != 0, "pivot denominator")
    pivot_q = roots[1] * sums[1] % PRIME
    beta_0 = (-pivot_q * poly_at(a_values, pivot_label)
              * pow(pivot_denominator, -1, PRIME)) % PRIME
    beta_1 = -beta_0 % PRIME
    q_values = tuple(root * edge_sum % PRIME for root, edge_sum in zip(roots, sums))
    require(all((q_value * poly_at(a_values, label)
                 + label * (beta_0 + beta_1 * label)) % PRIME == 0
                for q_value, label in zip(q_values, labels)), "sum interpolation")
    missing_label = -t * t % PRIME
    a_missing = poly_at(a_values, missing_label)
    require(a_missing != 0, "missing-label denominator")
    inverse_a = pow(a_missing, -1, PRIME)
    beta_missing = (beta_0 + beta_1 * missing_label) % PRIME
    return {
        "a_values": a_values,
        "b_values": b_values,
        "missing_product": poly_at(b_values, missing_label) * inverse_a % PRIME,
        "missing_sum_squared": (
            missing_label * beta_missing * beta_missing * inverse_a * inverse_a
        ) % PRIME,
    }


def paired(left, right, a_values, b_values):
    p_values = [sub((coefficient,), scale(left, a_value))
                for a_value, coefficient in zip(a_values, b_values)]
    q_values = (
        sub((b_values[0],), scale(right, a_values[0])),
        add((-b_values[1] % PRIME,), scale(right, a_values[1])),
        sub((b_values[2],), scale(right, a_values[2])),
    )
    return sub(
        power(sub(mul(p_values[2], q_values[0]), mul(p_values[0], q_values[2])), 2),
        mul(sub(mul(p_values[2], q_values[1]), mul(p_values[1], q_values[2])),
            sub(mul(p_values[1], q_values[0]), mul(p_values[0], q_values[1]))),
    )


def load_payloads():
    return (
        json.loads((EXPERIMENTS / FILES["classifier_result"][0]).read_text()),
        json.loads((EXPERIMENTS / FILES["replay_result"][0]).read_text()),
    )


def validate(boundary, replay, check_dag=True):
    require(boundary["schema"].endswith("cell11-guard-boundary-classifier-v1"),
            "classifier schema")
    require(boundary["case_count"] == len(boundary["rows"]) == 8, "classifier rows")
    require(boundary["guarded_source_point_count"] == 160, "classifier point count")
    require(boundary["status_counts"] == {"GUARDED_GUARD_BOUNDARY_PRESENT": 8},
            "classifier statuses")
    require(replay["schema"].endswith("cell11-guard-direct-replay-v1"), "replay schema")
    require(replay["boundary_classifier_sha256"] == FILES["classifier_result"][1],
            "replay source")
    require(replay["source_tower_count"] == len(replay["rows"]) == 8, "replay rows")
    require(replay["source_point_count"] == 160, "replay points")
    require(replay["colored_case_count"] == 320, "colored census")
    require(replay["uncolored_formal_case_count"] == 34560, "uncolored census")
    require(replay["denominator_failure_count"] == 0, "denominator failures")
    require(replay["colored_candidate_count"] == 0, "colored candidates")
    require(replay["uncolored_candidate_count"] == 0, "uncolored candidates")
    require(replay["status_counts"] == {"DIRECT_BOUNDARY_EXCLUDED": 8},
            "replay statuses")

    replay_by_key = {(row["bc_sign"], tuple(row["epsilon"])): row
                     for row in replay["rows"]}
    require(len(replay_by_key) == 8, "replay sign coverage")
    point_count = colored_count = uncolored_count = nonconstant_gcds = 0
    sign_points = Counter()
    for boundary_row in boundary["rows"]:
        key = (boundary_row["bc_sign"], tuple(boundary_row["epsilon"]))
        require(key in replay_by_key, "classifier/replay row join")
        replay_row = replay_by_key[key]
        require(replay_row["status"] == "DIRECT_BOUNDARY_EXCLUDED", "row status")
        require(not replay_row["denominator_failures"], "row denominator failures")
        require(not replay_row["colored_candidates"], "row colored candidates")
        require(not replay_row["uncolored_candidates"], "row uncolored candidates")
        guarded_points = [point for root_row in boundary_row["root_rows"]
                          for point in root_row["source_points"] if point.get("guarded")]
        require(len(guarded_points) == boundary_row["guarded_source_point_count"],
                "guarded point row census")
        printed_points = {row["point_sha256"]: row for row in replay_row["point_rows"]}
        require(len(printed_points) == len(guarded_points), "point replay coverage")
        row_uncolored = 0
        for point in guarded_points:
            require(point["bc_matches_x"] and point["common_equations_zero"]
                    and point["common_guard_nonzero"], "source point guards")
            digest = point_digest(point)
            require(digest in printed_points, "point digest coverage")
            common = common_data(point, key[1], key[0])
            printed = printed_points[digest]
            require(printed["missing_product"] == common["missing_product"], "q replay")
            require(printed["missing_sum_squared"] == common["missing_sum_squared"],
                    "squared-sum replay")
            q_value, sum_squared = common["missing_product"], common["missing_sum_squared"]
            b, c = point["b"] % PRIME, point["c"] % PRIME
            require(b and c, "colored base denominator")
            for base in (b, c):
                endpoint = q_value * pow(base, -1, PRIME) % PRIME
                require(((base + endpoint) ** 2 - sum_squared) % PRIME != 0,
                        "colored boundary candidate")
                colored_count += 1
            quartic = (q_value * q_value % PRIME, 0,
                       (2 * q_value - sum_squared) % PRIME, 0, 1)
            roots = [row["value"] for row in printed["endpoint_roots"]]
            require(len(roots) == len(set(roots)), "duplicate endpoint roots")
            require(field_root_polynomial(quartic) == root_product(roots),
                    "endpoint root completeness")
            for root_row in printed["endpoint_roots"]:
                root = root_row["value"]
                require(evaluate(quartic, root) == 0, "endpoint root")
                require(root_row["multiplicity"] == root_multiplicity(quartic, root),
                        "endpoint multiplicity")
            require(q_value != 0 and all(roots), "endpoint denominator")
            for endpoint in roots:
                partner = q_value * pow(endpoint, -1, PRIME) % PRIME
                for missing_record, sigma_o, matching in itertools.product(
                    MISSING_RECORDS, (-1, 1), MATCHINGS
                ):
                    variable = (0, 1)
                    if missing_record == "DE+":
                        records = {"BE": (b * partner % PRIME,), "CF": scale(variable, c),
                                   "DE-": (-q_value % PRIME,),
                                   "DF+": scale(variable, endpoint),
                                   "DF-": scale(variable, -endpoint),
                                   "EF": scale(variable, sigma_o * partner)}
                    elif missing_record == "DF+":
                        records = {"BE": scale(variable, b), "CF": (c * partner % PRIME,),
                                   "DE+": scale(variable, endpoint),
                                   "DE-": scale(variable, -endpoint),
                                   "DF-": (-q_value % PRIME,),
                                   "EF": scale(variable, sigma_o * partner)}
                    else:
                        f_value = sigma_o * partner % PRIME
                        records = {"BE": (b * endpoint % PRIME,), "CF": (c * f_value % PRIME,),
                                   "DE+": scale(variable, endpoint),
                                   "DE-": scale(variable, -endpoint),
                                   "DF+": scale(variable, f_value),
                                   "DF-": scale(variable, -f_value)}
                    names = tuple(name for name in GLOBAL_RECORDS if name != missing_record)
                    residual = tuple(records[name] for name in names)
                    equations = [paired(residual[left], residual[right],
                                        common["a_values"], common["b_values"])
                                 for left, right in matching]
                    common_divisor = (0,)
                    for equation in equations:
                        common_divisor = gcd(common_divisor, equation)
                    require(common_divisor != (0,), "identically zero paired system")
                    if len(common_divisor) > 1:
                        nonconstant_gcds += 1
                    require(field_root_polynomial(common_divisor) == (1,),
                            "uncolored boundary candidate")
                    row_uncolored += 1
                    uncolored_count += 1
            point_count += 1
            sign_points[key[0]] += 1
        require(row_uncolored == replay_row["uncolored_formal_case_count"],
                "row uncolored census")
        require(2 * len(guarded_points) == replay_row["colored_case_count"],
                "row colored census")
    require(point_count == 160 and sign_points == Counter({-1: 128, 1: 32}),
            "global point census")
    require(colored_count == 320 and uncolored_count == 34560, "global replay census")
    if check_dag:
        dag = json.loads((ROOT / "dag.json").read_text())
        nodes = {row["id"]: row for row in dag["nodes"]}
        edges = {(row["from"], row["to"], row.get("kind", "req"))
                 for row in dag["edges"]}
        require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
        for parent in PARENTS:
            require(nodes[parent]["status"] == "PROVED"
                    and (parent, NODE_ID, "req") in edges, "DAG parent")
        require((NODE_ID, CONSUMER, "ev") in edges, "DAG consumer")
    return nonconstant_gcds


def main():
    for filename, expected in FILES.values():
        require(hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
                == expected, f"file custody {filename}")
    nonconstant = validate(*load_payloads())
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELL11_GUARD_BOUNDARY_VERIFY_PASS "
          f"points=160 colored=320 uncolored=34560 nonconstant_gcds={nonconstant}")


if __name__ == "__main__":
    main()
