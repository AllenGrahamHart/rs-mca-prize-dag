#!/usr/bin/env python3
"""Light exact probe for the aligned saturated (1,1,2) q-slice gate.

This is evidence, not a deletion certificate.  It reconstructs the finite
source-line candidates over one split prime-field fixture and tests the
degree-eight resultant restricted to q=P_(J_1).
"""

from collections import Counter
from itertools import combinations, combinations_with_replacement


P = 1009


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def inv(value):
    require(value % P != 0, "division by zero")
    return pow(value, P - 2, P)


def trim(poly):
    result = [value % P for value in poly]
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


def scale(poly, scalar):
    return trim([scalar * value for value in poly])


def multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = (result[i + j] + a * b) % P
    return trim(result)


def evaluate(poly, point):
    result = 0
    for value in reversed(poly):
        result = (result * point + value) % P
    return result


def divide_exact(dividend, divisor):
    work = trim(dividend)
    divisor = trim(divisor)
    require(divisor != [0], "zero divisor")
    quotient = [0] * max(1, len(work) - len(divisor) + 1)
    lead_inverse = inv(divisor[-1])
    while work != [0] and len(work) >= len(divisor):
        shift = len(work) - len(divisor)
        coefficient = work[-1] * lead_inverse % P
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            work[index + shift] = (work[index + shift] - coefficient * value) % P
        work = trim(work)
    require(work == [0], f"nonzero remainder {work}")
    return trim(quotient)


def proportional(left, right):
    left = trim(left)
    right = trim(right)
    if left == [0] or right == [0] or len(left) != len(right):
        return False
    pivot = next(index for index, value in enumerate(right) if value)
    scalar = left[pivot] * inv(right[pivot]) % P
    return all(a == scalar * b % P for a, b in zip(left, right))


def solve_unique(matrix, target):
    rows = [[value % P for value in row] + [rhs % P]
            for row, rhs in zip(matrix, target)]
    columns = len(matrix[0])
    pivot_columns = []
    pivot_row = 0
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, len(rows))
                      if rows[row][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        factor = inv(rows[pivot_row][column])
        rows[pivot_row] = [factor * value % P for value in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row or not rows[row][column]:
                continue
            factor = rows[row][column]
            rows[row] = [
                (left - factor * right) % P
                for left, right in zip(rows[row], rows[pivot_row])
            ]
        pivot_columns.append(column)
        pivot_row += 1
    if any(all(value == 0 for value in row[:columns]) and row[-1]
           for row in rows):
        return None
    if len(pivot_columns) != columns:
        return None
    solution = [0] * columns
    for row, column in enumerate(pivot_columns):
        solution[column] = rows[row][-1]
    return solution


def u_evaluation(epsilon, point):
    point2 = point * point % P
    if epsilon == 1:
        return [
            [1, point, point2, 0, 0],
            [0, 0, 0, 1 + point2, point],
            [point2, point, 1, 0, 0],
        ]
    return [
        [1, point, point2, 0],
        [0, 0, 0, 1 - point2],
        [-point2, -point, -1, 0],
    ]


def u_polynomials(epsilon, coefficients):
    if epsilon == 1:
        a, b, c, d, e = coefficients
        return ([a, b, c], [d, e, d], [c, b, a])
    a, b, c, d = coefficients
    return ([a, b, c], [d, 0, -d], [-c, -b, -a])


def v_polynomials(epsilon, w, q):
    q0, q1, q2 = q
    f = (q0 - epsilon * w * q2) % P
    g = (epsilon * q2 - w * q0) % P
    m = q1 * (1 - epsilon * w) % P
    return ([f, g], [m, epsilon * m], [epsilon * g, epsilon * f])


def t_evaluate(coefficient_polys, point):
    result = [0]
    power = 1
    for poly in coefficient_polys:
        result = add(result, scale(poly, power))
        power = power * point % P
    return result


def edge_poly(edge, labels):
    left, right = (labels[index] for index in edge)
    return [left * right % P, -(left + right) % P, 1]


def reconstruct(epsilon, w, z, q, first, second, labels):
    v = v_polynomials(epsilon, w, q)
    vz = [evaluate(poly, z) for poly in v]
    common = set(first) & set(second)
    require(len(common) == 1, "internal edges are not adjacent")
    common_index = next(iter(common))
    other_first = next(index for index in first if index != common_index)
    other_second = next(index for index in second if index != common_index)
    a = labels[common_index]
    b = labels[other_first]
    c = labels[other_second]
    l1 = vz[2]
    l0 = (vz[1] + a * l1) % P
    require(vz[0] == -a * l0 % P, "incidence division")
    first_scale = (l0 + c * l1) % P
    second_scale = (l0 + b * l1) % P
    denominator = inv(c - b)
    target = scale(
        add(scale(edge_poly(first, labels), first_scale),
            scale(edge_poly(second, labels), second_scale)),
        denominator,
    )
    target += [0] * (3 - len(target))

    at_w = u_evaluation(epsilon, w)
    at_z = u_evaluation(epsilon, z)
    q0, q1, _ = q
    matrix = [
        [(at_w[0][j] - q0 * at_w[2][j]) % P for j in range(len(at_w[0]))],
        [(at_w[1][j] - q1 * at_w[2][j]) % P for j in range(len(at_w[0]))],
        *at_z,
    ]
    coefficients = solve_unique(matrix, [0, 0, *target])
    if coefficients is None:
        return None
    ubar = u_polynomials(epsilon, coefficients)
    require([evaluate(poly, z) for poly in ubar] == target,
            "reconstruction target")
    return ubar, v


def qslice_passes(ubar, v, z, w, q_roots):
    values = []
    for root in q_roots:
        u_at_root = t_evaluate(ubar, root)
        v_at_root = t_evaluate(v, root)
        norm = add(scale(multiply(u_at_root, u_at_root), z),
                   scale([0] + multiply(v_at_root, v_at_root), -1))
        values.append(norm)
    resultant = multiply(values[0], values[1])
    forced = [(-w) % P, 1]
    residual = divide_exact(resultant, multiply(multiply(forced, forced),
                                                multiply(forced, forced)))
    crossing = multiply([(-inv(q_roots[0])) % P, 1],
                        [(-inv(q_roots[1])) % P, 1])
    return proportional(residual, multiply(crossing, crossing))


def collision(packet):
    return sum(weight * (weight - 1) // 2 for weight in packet.values())


def main():
    labels = [2, inv(2), 3, inv(3)]
    q_roots = (5, 7)
    q = [q_roots[0] * q_roots[1] % P,
         -(q_roots[0] + q_roots[1]) % P, 1]
    w = 11
    tau = {0: 1, 1: 0, 2: 3, 3: 2}
    edges = list(combinations(range(4), 2))
    edge_index = {edge: index for index, edge in enumerate(edges)}
    tau_edge = {
        index: edge_index[tuple(sorted((tau[left], tau[right])))]
        for index, (left, right) in enumerate(edges)
    }

    tested = reconstructed = survivors = 0
    invalid_label_fixtures = 0
    for first_index, second_index in combinations_with_replacement(range(6), 2):
        packet = Counter((first_index, second_index,
                          tau_edge[first_index], tau_edge[second_index]))
        if collision(packet) > 1:
            continue
        first, second = edges[first_index], edges[second_index]
        common = next(iter(set(first) & set(second)))
        a = labels[common]
        for epsilon in (1, -1):
            tested += 1
            q0, q1, q2 = q
            f = (q0 - epsilon * w * q2) % P
            g = (epsilon * q2 - w * q0) % P
            m = q1 * (1 - epsilon * w) % P
            numerator = (f + m * a + epsilon * g * a * a) % P
            denominator = (g + epsilon * m * a
                           + epsilon * f * a * a) % P
            require(denominator, "incidence denominator")
            z = -numerator * inv(denominator) % P
            endpoint_labels = set(labels + [*q_roots, inv(q_roots[0]),
                                             inv(q_roots[1]), w, inv(w),
                                             z, inv(z)])
            if len(endpoint_labels) != 12 or z in (1, P - 1):
                invalid_label_fixtures += 1
                continue
            candidate = reconstruct(epsilon, w, z, q, first, second, labels)
            if candidate is None:
                continue
            reconstructed += 1
            if qslice_passes(*candidate, z, w, q_roots):
                survivors += 1

    require(tested == 24, "admissible internal pair/sign count")
    print(
        "KB_C2_112_QSLICE_PROBE_PASS "
        f"prime={P} tested={tested} reconstructed={reconstructed} "
        f"invalid_label_fixtures={invalid_label_fixtures} survivors={survivors}"
    )


if __name__ == "__main__":
    main()
