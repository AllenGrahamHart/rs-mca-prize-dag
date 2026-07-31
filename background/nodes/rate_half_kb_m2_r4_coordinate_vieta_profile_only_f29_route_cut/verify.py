#!/usr/bin/env python3
"""Reconstruct the exact F_29 coordinate Vieta route-cut witness."""

from __future__ import annotations

from collections import Counter
import json
from itertools import combinations
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_vieta_profile_only_f29_route_cut"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def trim(poly: list[int], p: int) -> list[int]:
    result = [value % p for value in poly]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def add(left: list[int], right: list[int], p: int) -> list[int]:
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    ], p)


def scale(poly: list[int], scalar: int, p: int) -> list[int]:
    return trim([scalar * value for value in poly], p)


def multiply(left: list[int], right: list[int], p: int) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = (result[i + j] + a * b) % p
    return trim(result, p)


def product(polynomials: list[list[int]], p: int) -> list[int]:
    result = [1]
    for poly in polynomials:
        result = multiply(result, poly, p)
    return result


def evaluate(poly: list[int], value: int, p: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = (result * value + coefficient) % p
    return result


def derivative(poly: list[int], p: int) -> list[int]:
    return trim([degree * poly[degree] for degree in range(1, len(poly))], p)


def divide(dividend: list[int], divisor: list[int], p: int) -> tuple[list[int], list[int]]:
    remainder = trim(dividend, p)
    divisor = trim(divisor, p)
    require(divisor != [0], "zero divisor")
    if len(remainder) < len(divisor):
        return [0], remainder
    quotient = [0] * (len(remainder) - len(divisor) + 1)
    inverse_lead = pow(divisor[-1], p - 2, p)
    while remainder != [0] and len(remainder) >= len(divisor):
        degree = len(remainder) - len(divisor)
        coefficient = remainder[-1] * inverse_lead % p
        quotient[degree] = coefficient
        for index, value in enumerate(divisor):
            remainder[index + degree] = (
                remainder[index + degree] - coefficient * value
            ) % p
        remainder = trim(remainder, p)
    return trim(quotient, p), remainder


def monic(poly: list[int], p: int) -> list[int]:
    poly = trim(poly, p)
    require(poly != [0], "zero polynomial")
    return scale(poly, pow(poly[-1], p - 2, p), p)


def gcd(left: list[int], right: list[int], p: int) -> list[int]:
    left, right = trim(left, p), trim(right, p)
    while right != [0]:
        _, remainder = divide(left, right, p)
        left, right = right, remainder
    return monic(left, p)


def root_poly(roots: list[int], p: int) -> list[int]:
    return product([[-root % p, 1] for root in roots], p)


def matrix_rank(matrix: list[list[int]], p: int) -> int:
    work = [[value % p for value in row] for row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][column], p - 2, p)
        work[pivot_row] = [value * inverse % p for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or not work[row][column]:
                continue
            multiple = work[row][column]
            work[row] = [
                (left - multiple * right) % p
                for left, right in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
    return pivot_row


def main() -> None:
    data = json.loads((NODE / "certificate.json").read_text())
    p = data["field"]
    require(p == 29, "field")
    i_pairs = [tuple(pair) for pair in data["I_pairs"]]
    j_pairs = [tuple(pair) for pair in data["J_pairs"]]
    i_set = {value for pair in i_pairs for value in pair}
    j_set = {value for pair in j_pairs for value in pair}
    require(len(i_set) == len(j_set) == 6 and not i_set & j_set, "label partition")
    require(all((-left) % p == right for left, right in [*i_pairs, *j_pairs]), "deck pairs")
    k_points = data["K"]
    xi = data["xi"]
    require(set(k_points) == i_set - {xi} and xi == 20, "common five-set")

    def edge(values: list[int]) -> frozenset[int]:
        result = frozenset(value % p for value in values)
        require(len(result) == 2, "simple star")
        return result

    def bar_edge(value: frozenset[int]) -> frozenset[int]:
        return frozenset((-endpoint) % p for endpoint in value)

    k_orbits = [(edge(pair[0]), edge(pair[1])) for pair in data["k_orbits"]]
    eta_orbit = tuple(edge(value) for value in data["eta_orbit"])
    right_records = data["right_records"]
    right_orbits = [tuple(edge(value) for value in record["stars"])
                    for record in right_records]
    all_orbits = [*k_orbits, eta_orbit, *right_orbits]
    require(all(bar_edge(first) == second for first, second in all_orbits), "deck transport")

    stars = [value for orbit in all_orbits for value in orbit]
    require(len(stars) == 24, "24 star slots")
    multiplicities = Counter(stars)
    defect = sum(count * (count - 1) // 2 for count in multiplicities.values())
    require(defect == 2, "defect two")

    categories = Counter()
    for value in stars:
        if value <= i_set:
            categories["II"] += 1
        elif value <= j_set:
            categories["JJ"] += 1
        else:
            categories["IJ"] += 1
    require(categories == Counter({"II": 10, "JJ": 10, "IJ": 4}), "category census")
    degrees = Counter(vertex for value in stars for vertex in value)
    require(all(degrees[label] == 4 for label in i_set | j_set), "source degrees")
    k_degrees = Counter(vertex for orbit in k_orbits for value in orbit for vertex in value)
    require(sorted(k_degrees[label] for label in j_set) == [2, 2, 4, 4, 4, 4], "K profile")

    left_degrees = Counter()
    pole_edges: set[tuple[int, int]] = set()
    colored = 0
    colored_rights = []
    for record, (first, second) in zip(right_records, right_orbits):
        right = record["right"]
        neighbors = tuple(record["neighbors"])
        require(right in j_set and len(set(neighbors)) == 2, "right record")
        require(right not in neighbors and set(neighbors) <= j_set, "diagonal-free graph")
        for neighbor in neighbors:
            require((neighbor, right) not in pole_edges, "simple pole edge")
            pole_edges.add((neighbor, right))
            left_degrees[neighbor] += 1
        common = i_set - {record["x"]}
        if first <= i_set:
            require(first <= common and second <= common, "common-I facet")
        else:
            require(len(first & j_set) == len(second & j_set) == 1, "one exchange")
            require(next(iter(first & j_set)) == neighbors[0], "first colored edge")
            require(next(iter(second & j_set)) == neighbors[1], "second colored edge")
            require((first & i_set) <= common and (second & i_set) <= common, "mixed facet")
            colored += 2
            colored_rights.append(right)
    require(len(pole_edges) == 12, "pole edge count")
    require(all(left_degrees[label] == 2 for label in j_set), "left pole degrees")
    require({record["x"] for record in right_records} == i_set, "facet matching")
    require(colored == 4, "colored edges")
    require(sorted(colored_rights) == sorted(data["colored_rights"]) == [3, 26],
            "colored right vertices")

    coefficients = data["positive_coefficients"]
    a2 = coefficients["A2"]
    a0 = coefficients["A0"]
    b1 = coefficients["B1"]
    require(len(a2) == len(a0) == 3 and len(b1) == 2 and b1 != [0, 0],
            "exact positive coefficient space")
    vector = [*a2, *a0, *b1]
    matrix: list[list[int]] = []
    for kappa, square_root, (first, _) in zip(
        k_points, data["k_square_roots"], k_orbits
    ):
        require(square_root * square_root % p == kappa, "square-root lift")
        endpoints = tuple(first)
        edge_product = endpoints[0] * endpoints[1] % p
        edge_sum = sum(endpoints) % p
        weighted_sum = square_root * edge_sum % p
        basis2 = [1, kappa, kappa * kappa % p]
        matrix.extend((
            [(-edge_product * value) % p for value in basis2]
            + basis2 + [0, 0],
            [(weighted_sum * value) % p for value in basis2]
            + [0, 0, 0, kappa, kappa * kappa % p],
        ))
        lead = evaluate(a2, kappa, p)
        require(lead != 0, "leading support")
        require(evaluate(a0, kappa, p) == edge_product * lead % p, "product Vieta")
        require(
            kappa * evaluate(b1, kappa, p) % p == -weighted_sum * lead % p,
            "sum Vieta",
        )
        row_poly = [
            evaluate(a0, kappa, p),
            square_root * evaluate(b1, kappa, p) % p,
            lead,
        ]
        expected = scale([edge_product, -edge_sum, 1], lead, p)
        require(row_poly == expected, "actual edge roots")
    require(all(sum(left * right for left, right in zip(row, vector)) % p == 0
                for row in matrix), "matrix kernel")
    require(matrix_rank(matrix, p) == 7, "rank seven")

    a2_x = [a2[0], 0, a2[1], 0, a2[2]]
    a0_x = [a0[0], 0, a0[1], 0, a0[2]]
    xb1_x = [0, b1[0], 0, b1[1]]
    require(gcd(gcd(a2_x, a0_x, p), xb1_x, p) == [1], "primitive coefficients")
    discriminant = add(
        [0, *multiply(b1, b1, p)],
        scale(multiply(a2, a0, p), -4, p),
        p,
    )
    require(discriminant == [10, 6, 8, 19, 16], "discriminant")
    require(discriminant[0] != 0 and gcd(discriminant, derivative(discriminant, p), p) == [1],
            "nonsquare discriminant")

    def phi(y_value: int) -> list[int]:
        base = add(scale(a2, y_value, p), a0, p)
        return add(
            multiply(base, base, p),
            scale([0, *multiply(b1, b1, p)], -y_value, p),
            p,
        )

    r_j = product([phi(base * base % p) for base, _ in j_pairs], p)
    r_i = product([phi(base * base % p) for base, _ in i_pairs], p)
    k5 = root_poly(k_points, p)
    forced_c, remainder = divide(r_j, multiply(k5, k5, p), p)
    require(remainder == [0] and monic(forced_c, p) == data["forced_c"], "forced quotient")
    require(all(evaluate(forced_c, root, p) == 0 for root in data["forced_c_roots"]),
            "forced roots")
    require(not set(data["forced_c_roots"]) & j_set, "forbidden colored support")
    colored_c = monic(root_poly(data["colored_rights"], p), p)
    require(colored_c == [20, 0, 1] and colored_c != monic(forced_c, p),
            "packet-colored quadratic mismatch")
    supported = [monic(root_poly(list(roots), p), p) for roots in combinations(sorted(j_set), 2)]
    require(monic(forced_c, p) not in supported, "all supported quadratics rejected")

    r7 = root_poly([xi, *sorted(j_set)], p)
    left_at_xi = evaluate(multiply(forced_c, r_i, p), xi, p)
    right_at_xi = evaluate(multiply(r7, r7, p), xi, p)
    require((left_at_xi, right_at_xi) == (8, 0), "companion identity failure")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(item["from"], item["to"], item.get("kind", "req")) for item in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
        "rate_half_kb_m2_r4_coordinate_k_fiber_vieta_rank_compiler",
        "rate_half_kb_m2_r4_coordinate_colored_quotient_resultant_compiler",
    ):
        require((parent, NODE_ID, "req") in edges, f"missing parent {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer edge")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_VIETA_PROFILE_ONLY_F29_ROUTE_CUT_PASS "
        f"defect={defect} rank=7 forced_c={forced_c} companion={left_at_xi}/{right_at_xi}"
    )


if __name__ == "__main__":
    main()
