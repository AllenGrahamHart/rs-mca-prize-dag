#!/usr/bin/env python3
"""Check the cell-5 certificate-denominator pole census."""

import argparse
import ast
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


HERE = Path(__file__).parent
BASE_RESULT = HERE / "rate_half_kb_positive_433_1a_cell5_specialization_poles_result.json"
OPERATOR_RESULT = HERE / (
    "rate_half_kb_positive_433_1a_cell5_specialization_operator_poles_result.json"
)
EXPECTED_BASE_SHA256 = (
    "dc93d2b41a26ed5717c366c799f341cad67cdf5aef8fbec32602252af2c5ea23"
)
EXPECTED_OPERATOR_SHA256 = (
    "0927bb86e6d87f4a2120c75d88f5e64c6740fb54988615d893eacb075edab92a"
)
PRIME = 2130706433
INPUTS = {
    "basis": HERE
    / "rate_half_kb_positive_433_1a_cell5_pair_function_field_julia_basis_result.json",
    "primitive_factor": HERE
    / "rate_half_kb_positive_433_1a_cell5_pair_primitive_polynomial_result.json",
    "factorization": HERE
    / "rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization_result.json",
    "maps": HERE
    / "rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map_result.json",
    "colored": HERE
    / "rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd_result.json",
    "guard_norms": HERE
    / "rate_half_kb_positive_433_1a_cell5_pair_guard_norms_result.json",
    "operator": HERE
    / "rate_half_kb_positive_433_1a_cell5_pair_localized_operator_merged_result.json",
}
CATEGORY_SOURCES = {
    "basis": ("basis",),
    "primitive_factor": ("primitive_factor", "factorization"),
    "maps": ("maps",),
    "colored": ("colored",),
    "guard_norms": ("guard_norms",),
    "operator": ("operator",),
}
EXPECTED_LEDGER = {
    "basis": (907, 362, 13, 87, "41664967d5bff24c0f9f6e97daef84221fe60b8874f7edf483e928b4d903157f"),
    "primitive_factor": (54, 18, 3, 48, "f377ac3d6638e704ae6e2803672ea78077b6e3b15498ca289e89722b5d5398ec"),
    "maps": (72, 26, 43, 1046, "28f9efe2c8e396ce70abbb23f4016ab2650e0a85fe390b4bb26043fe8ac67f95"),
    "colored": (354, 111, 20, 335, "58400e8f23095494db7f1309f1fd470cab9adbc362274d9a5381e56cad69bb54"),
    "guard_norms": (160, 14, 3, 16, "142946f9adda80f54aea1d82adf47b9a2529c9a34ba688cf88960ab1eef061f4"),
    "operator": (2112, 612, 13, 185, "5e38203d37ce23a6bb47b61ec357f54f0ecb43c8177ad016b367afcd5c2c59b7"),
}
EXPECTED_ROOTS = {
    0, 1, 16711679, 16711680, 16903576, 59577338, 60142635, 100334506,
    259897937, 263415810, 282428254, 314606277, 350200897, 399214728,
    429335281, 457960787, 534616264, 658388861, 719443868, 790247430,
    825068466, 898552563, 967866903, 994619988, 1108567599, 1112415117,
    1156161765, 1157872027, 1179254816, 1182328414, 1207246658,
    1234520829, 1248074151, 1310630326, 1328213402, 1332924776,
    1373882361, 1379619328, 1410757125, 1474082935, 1502791638,
    1548270121, 1552698975, 1593520725, 1594419216, 1618157807,
    1618717679, 1660665744, 1665662739, 1729517783, 1777239993,
    1783507114, 1806635209, 1910266670, 1969598264, 2026412590,
    2029231698, 2042457704, 2086242076, 2113994754, 2130706432,
}


class CertificateError(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise CertificateError(message)


def trim(value):
    value = [item % PRIME for item in value]
    while len(value) > 1 and value[-1] == 0:
        value.pop()
    return value


def add(left, right):
    return trim([
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(max(len(left), len(right)))
    ])


def negate(value):
    return trim([-item for item in value])


def multiply(left, right):
    output = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            output[left_index + right_index] = (
                output[left_index + right_index] + left_value * right_value
            ) % PRIME
    return trim(output)


def power(value, exponent):
    output = [1]
    while exponent:
        if exponent & 1:
            output = multiply(output, value)
        exponent >>= 1
        if exponent:
            value = multiply(value, value)
    return output


def parse_polynomial(text):
    def visit(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, int):
            return [node.value]
        if isinstance(node, ast.Name) and node.id == "t":
            return [0, 1]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return negate(visit(node.operand))
        if isinstance(node, ast.BinOp):
            if isinstance(node.op, ast.Add):
                return add(visit(node.left), visit(node.right))
            if isinstance(node.op, ast.Sub):
                return add(visit(node.left), negate(visit(node.right)))
            if isinstance(node.op, ast.Mult):
                return multiply(visit(node.left), visit(node.right))
            if isinstance(node.op, ast.Pow):
                require(
                    isinstance(node.right, ast.Constant)
                    and isinstance(node.right.value, int),
                    "nonintegral denominator exponent",
                )
                return power(visit(node.left), node.right.value)
        raise CertificateError(f"unsupported denominator syntax {type(node).__name__}")

    return trim(visit(ast.parse(text.replace("^", "**"), mode="eval").body))


def collect_structured(value, output):
    if isinstance(value, dict):
        for key, child in value.items():
            if (
                key == "denominator"
                and isinstance(child, list)
                and child
                and all(isinstance(item, int) for item in child)
            ):
                output.append(tuple(trim(child)))
            collect_structured(child, output)
    elif isinstance(value, list):
        for child in value:
            collect_structured(child, output)


def source_denominators(category):
    output = []
    if category == "basis":
        payload = json.loads(INPUTS["basis"].read_text())
        require(isinstance(payload, list) and len(payload) == 1, "basis packet shape mismatch")
        for line in payload[0]["basis_lines"]:
            texts = re.findall(r"//\(([^()]*)\)", line)
            require(len(texts) == line.count("//"), "unparsed basis denominator")
            output.extend(tuple(parse_polynomial(text)) for text in texts)
    else:
        for name in CATEGORY_SOURCES[category]:
            collect_structured(json.loads(INPUTS[name].read_text()), output)
    require(output and all(value != (0,) for value in output), "bad source denominator")
    return Counter(output)


def evaluate(polynomial, point):
    output = 0
    for coefficient in reversed(polynomial):
        output = (output * point + coefficient) % PRIME
    return output


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-result", type=Path, default=BASE_RESULT)
    parser.add_argument("--operator-result", type=Path, default=OPERATOR_RESULT)
    return parser.parse_args()


def verify(base_path=BASE_RESULT, operator_path=OPERATOR_RESULT):
    base_raw = base_path.read_bytes()
    operator_raw = operator_path.read_bytes()
    if base_path == BASE_RESULT:
        require(hashlib.sha256(base_raw).hexdigest() == EXPECTED_BASE_SHA256, "base result hash mismatch")
    if operator_path == OPERATOR_RESULT:
        require(hashlib.sha256(operator_raw).hexdigest() == EXPECTED_OPERATOR_SHA256, "operator result hash mismatch")
    payload = json.loads(base_raw) + json.loads(operator_raw)
    require([item["category"] for item in payload] == list(EXPECTED_LEDGER), "category order mismatch")
    root_union = set()
    for shard in payload:
        category = shard["category"]
        occurrences, unique_count, root_count, maximum_degree, program_hash = EXPECTED_LEDGER[category]
        require(shard["status"] == "COMPLETE" and shard["returncode"] == 0, "incomplete shard")
        require(shard["occurrences"] == occurrences, "occurrence count mismatch")
        require(shard["unique_denominators"] == unique_count, "unique count mismatch")
        require(shard["program_sha256"] == program_hash, "program hash mismatch")
        expected_sources = {
            name: hashlib.sha256(INPUTS[name].read_bytes()).hexdigest()
            for name in CATEGORY_SOURCES[category]
        }
        require(shard["source_sha256"] == expected_sources, "source hash mismatch")
        records = shard.get("records")
        require(isinstance(records, list) and len(records) == unique_count, "record coverage mismatch")
        source = source_denominators(category)
        returned = Counter()
        category_roots = set()
        for record in records:
            denominator = tuple(trim(record["denominator"]))
            require(denominator == tuple(record["denominator"]), "noncanonical denominator")
            require(record["degree"] == len(denominator) - 1, "degree mismatch")
            require(record["occurrences"] > 0, "bad occurrence multiplicity")
            returned[denominator] += record["occurrences"]
            roots = record["roots"]
            require(
                isinstance(roots, list)
                and roots == sorted(set(roots))
                and all(isinstance(root, int) and 0 <= root < PRIME for root in roots),
                "bad root list",
            )
            require(all(evaluate(denominator, root) == 0 for root in roots), "listed nonroot")
            category_roots.update(roots)
        require(returned == source, "source-denominator multiset mismatch")
        require(len(category_roots) == root_count, "category root-union count mismatch")
        require(max(record["degree"] for record in records) == maximum_degree, "maximum degree mismatch")
        root_union.update(category_roots)
    require(root_union == EXPECTED_ROOTS, "global root union mismatch")
    return root_union


def main():
    args = parse_args()
    roots = verify(args.base_result, args.operator_result)
    forbidden = {0, 1, PRIME - 1, 16711679, PRIME - 16711679}
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_SPECIALIZATION_POLES_PASS "
        "categories=6 denominator_occurrences=3659 unique_category_denominators=1143 "
        f"root_union={len(roots)} admissible_looking={len(roots - forbidden)}"
    )


if __name__ == "__main__":
    try:
        main()
    except (CertificateError, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"RATE_HALF_KB_POSITIVE_433_1A_CELL5_SPECIALIZATION_POLES_FAIL {error}")
        raise SystemExit(1)
