#!/usr/bin/env python3
"""Certify generic guard units in every signed-pair residue field."""

import argparse
import ast
import hashlib
import json
import sys
from pathlib import Path


HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import check_rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map as map_checker
import check_rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization as factor_checker


PRIME = 2130706433
FIBER = 2
IOTA = 16711679
ATLAS = HERE / "rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json"
EXPECTED_ATLAS_SHA256 = (
    "a7610836af981845fca5bf13db61f15beb6df5da08f22338846142495825e548"
)
EXPECTED_LEDGER_SHA256 = (
    "a48d3a028d422b19edda8d6ecac1f663bf2710fbc491a492b660b6b6e264bcb6"
)


class CertificateError(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise CertificateError(message)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--coordinate-map", type=Path, default=map_checker.COORDINATE_MAP)
    parser.add_argument("--factorization", type=Path, default=factor_checker.FACTORIZATION)
    parser.add_argument("--atlas", type=Path, default=ATLAS)
    return parser.parse_args()


def trim(polynomial):
    result = [value % PRIME for value in polynomial]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def add(left, right):
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    ])


def negate(polynomial):
    return trim([-value for value in polynomial])


def subtract(left, right):
    return add(left, negate(right))


def multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] = (
                result[left_index + right_index] + left_value * right_value
            ) % PRIME
    return trim(result)


def divmod_poly(dividend, divisor):
    dividend = trim(dividend)
    divisor = trim(divisor)
    require(divisor != [0], "zero polynomial divisor")
    quotient = [0] * max(1, len(dividend) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, PRIME)
    while dividend != [0] and len(dividend) >= len(divisor):
        shift = len(dividend) - len(divisor)
        scale = dividend[-1] * inverse % PRIME
        quotient[shift] = scale
        for index, value in enumerate(divisor):
            dividend[index + shift] = (
                dividend[index + shift] - scale * value
            ) % PRIME
        dividend = trim(dividend)
    return trim(quotient), dividend


def reduce_mod(polynomial, modulus):
    return divmod_poly(polynomial, modulus)[1]


def multiply_mod(left, right, modulus):
    return reduce_mod(multiply(left, right), modulus)


def power_mod(base, exponent, modulus):
    result = [1]
    base = reduce_mod(base, modulus)
    while exponent:
        if exponent & 1:
            result = multiply_mod(result, base, modulus)
        base = multiply_mod(base, base, modulus)
        exponent >>= 1
    return result


def inverse_mod(value, modulus):
    old_remainder, remainder = trim(modulus), trim(value)
    old_coefficient, coefficient = [0], [1]
    while remainder != [0]:
        quotient, new_remainder = divmod_poly(old_remainder, remainder)
        old_remainder, remainder = remainder, new_remainder
        old_coefficient, coefficient = (
            coefficient,
            subtract(old_coefficient, multiply(quotient, coefficient)),
        )
    require(len(old_remainder) == 1 and old_remainder[0] != 0, "guard chart denominator is not invertible")
    scale = pow(old_remainder[0], -1, PRIME)
    return reduce_mod([scale * item for item in old_coefficient], modulus)


def expression_mod(text, environment, modulus):
    def visit(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, int):
            return [node.value]
        if isinstance(node, ast.Name) and node.id in environment:
            return environment[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return negate(visit(node.operand))
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            return add(visit(node.left), visit(node.right))
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Sub):
            return subtract(visit(node.left), visit(node.right))
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
            return multiply_mod(visit(node.left), visit(node.right), modulus)
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Pow):
            require(isinstance(node.right, ast.Constant) and isinstance(node.right.value, int), "nonintegral atlas exponent")
            return power_mod(visit(node.left), node.right.value, modulus)
        raise CertificateError(f"unsupported atlas expression node {type(node).__name__}")

    return reduce_mod(visit(ast.parse(text, mode="eval").body), modulus)


def specialize_map(records):
    return [
        map_checker.evaluate_fraction(record, FIBER)
        for record in records
    ]


def scalar(value):
    return [value % PRIME]


def verify(map_path=map_checker.COORDINATE_MAP, factor_path=factor_checker.FACTORIZATION, atlas_path=ATLAS):
    maps, _, _, _ = map_checker.verify(map_path)
    generic_factors, _ = factor_checker.verify(factor_path)
    atlas_raw = atlas_path.read_bytes()
    require(hashlib.sha256(atlas_raw).hexdigest() == EXPECTED_ATLAS_SHA256, "lift-atlas hash mismatch")
    atlas = json.loads(atlas_raw)
    require(atlas["characteristic"] == PRIME and atlas["iota"] == IOTA, "lift-atlas field mismatch")
    require(IOTA * IOTA % PRIME == PRIME - 1, "invalid deployed iota")
    charts = {item["basis_index"]: item for item in atlas["c_charts"]}
    require(2 in charts, "chart-2 lift formula missing")

    specialized_factors = [
        trim([factor_checker.evaluate_rational(value, FIBER) for value in factor])
        for factor in generic_factors
    ]
    specialized_maps = {
        name: specialize_map(records)
        for name, records in maps.items()
    }
    ledger = []
    for factor_index, modulus in enumerate(specialized_factors, start=1):
        require(modulus[-1] == 1, "specialized factor is not monic")
        b = reduce_mod(specialized_maps["b"], modulus)
        x0 = reduce_mod(specialized_maps["x0"], modulus)
        x1 = reduce_mod(specialized_maps["x1"], modulus)
        environment = {"b": b, "t": scalar(FIBER)}

        r_leading = expression_mod(atlas["r_chart"]["leading"], environment, modulus)
        r_constant = expression_mod(atlas["r_chart"]["constant"], environment, modulus)
        r = negate(multiply_mod(r_constant, inverse_mod(r_leading, modulus), modulus))
        c_leading = expression_mod(charts[2]["leading"], environment, modulus)
        c_constant = expression_mod(charts[2]["constant"], environment, modulus)
        c = negate(multiply_mod(c_constant, inverse_mod(c_leading, modulus), modulus))

        one = [1]
        t_value = scalar(FIBER)
        iota = scalar(IOTA)
        common_guards = {
            "t-1": subtract(t_value, one),
            "t+1": add(t_value, one),
            "r-1": subtract(r, one),
            "r+1": add(r, one),
            "r-iota": subtract(r, iota),
            "r+iota": add(r, iota),
            "t-r": subtract(t_value, r),
            "t+r": add(t_value, r),
            "t-iota*r": subtract(t_value, multiply_mod(iota, r, modulus)),
            "t+iota*r": add(t_value, multiply_mod(iota, r, modulus)),
            "t-iota": subtract(t_value, iota),
            "t+iota": add(t_value, iota),
            "r": r,
            "t": t_value,
            "b": b,
            "c": c,
            "b-1": subtract(b, one),
            "b+1": add(b, one),
            "c-1": subtract(c, one),
            "c+1": add(c, one),
            "c-b": subtract(c, b),
            "b+c": add(b, c),
        }
        r_fourth = power_mod(r, 4, modulus)
        outside_guards = {}
        for name, value in (("x0", x0), ("x1", x1)):
            outside_guards[name] = value
            outside_guards[f"{name}-1"] = subtract(value, one)
            outside_guards[f"{name}-t^4"] = subtract(
                value, scalar(pow(FIBER, 4, PRIME))
            )
            outside_guards[f"{name}-r^4"] = subtract(value, r_fourth)
        require(len(common_guards) == 22 and len(outside_guards) == 8, "guard ledger size mismatch")
        for family, guards in (("common", common_guards), ("outside_squared", outside_guards)):
            for name, remainder in sorted(guards.items()):
                remainder = reduce_mod(remainder, modulus)
                require(remainder != [0], f"{family} guard {name} vanishes on factor {factor_index}")
                ledger.append({
                    "factor": factor_index,
                    "factor_degree": len(modulus) - 1,
                    "family": family,
                    "guard": name,
                    "remainder": remainder,
                })
    require(len(ledger) == 5 * 30, "guard coverage mismatch")
    canonical = "\n".join(
        f"{item['factor']}:{item['factor_degree']}:{item['family']}:{item['guard']}:"
        + ",".join(map(str, item["remainder"]))
        for item in ledger
    )
    digest = hashlib.sha256(canonical.encode()).hexdigest()
    require(digest == EXPECTED_LEDGER_SHA256, "guard ledger digest mismatch")
    return ledger, digest


def main():
    args = parse_args()
    ledger, digest = verify(args.coordinate_map, args.factorization, args.atlas)
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_GENERIC_GUARD_UNITS_PASS "
        "factors=5 common_guards=22 outside_squared_guards=8 checks=150 "
        f"fiber={FIBER} ledger_sha256={digest}"
    )


if __name__ == "__main__":
    try:
        main()
    except (CertificateError, KeyError, ValueError, SyntaxError) as error:
        print(f"RATE_HALF_KB_POSITIVE_433_1A_CELL5_GENERIC_GUARD_UNITS_FAIL {error}")
        raise SystemExit(1)
