#!/usr/bin/env python3
"""Sparse outside-product solver for the finite one-loop 442 cells [3,6]."""

import argparse
import math


P = 2130706433
ROWS = (
    (1608564875, 181785890, 893470876),
    (1587494773, 449324246, 1479361290),
)
LOOP_ROOTS = (101399882, 592085280)


def clean(polynomial):
    return {power: coefficient % P for power, coefficient in polynomial.items()
            if coefficient % P}


def poly_add(left, right):
    output = dict(left)
    for powers, coefficient in right.items():
        output[powers] = (output.get(powers, 0)+coefficient) % P
    return clean(output)


def poly_neg(polynomial):
    return {powers: -coefficient % P
            for powers, coefficient in polynomial.items()}


def poly_mul(left, right):
    output = {}
    for (d_left, s_left), first in left.items():
        for (d_right, s_right), second in right.items():
            powers = (d_left+d_right, s_left+s_right)
            output[powers] = (
                output.get(powers, 0)+first*second
            ) % P
    return clean(output)


def poly_scale(scalar, polynomial):
    return clean({powers: scalar*coefficient
                  for powers, coefficient in polynomial.items()})


def binary_mul(left, right):
    output = [{} for _ in range(len(left)+len(right)-1)]
    for left_index, first in enumerate(left):
        for right_index, second in enumerate(right):
            output[left_index+right_index] = poly_add(
                output[left_index+right_index], poly_mul(first, second)
            )
    return output


def constant(value):
    return {(0, 0): value % P}


def monomial(d_power, s_power, value=1):
    return {(d_power, s_power): value % P}


def action_matrix(alpha, beta, gamma):
    delta = (alpha*alpha+beta*gamma) % P
    action = [[0 for _ in range(7)] for _ in range(3)]
    for ell in range(3):
        for j in range(7):
            value = 0
            for q_value in range(max(0, ell-(6-j)), min(ell, j)+1):
                p_value = ell-q_value
                scalar = math.comb(6-j, p_value)*math.comb(j, q_value)
                if q_value % 2:
                    scalar = -scalar
                term = (
                    pow(alpha, 6-j-p_value, P)*pow(beta, p_value, P)
                    *pow(gamma, j-q_value, P)*pow(alpha, q_value, P)
                )
                value = (value+scalar*term) % P
            if ell == j:
                value = (value-pow(delta, 3, P)) % P
            action[ell][j] = value
    return action


def factors_for(cell, c_value, mate, theta, alpha_sign, delta_sign, ef_sign):
    c_inverse = pow(c_value, -1, P)
    mate_over_c = mate*c_inverse % P
    if cell == "forced-de":
        return (
            (monomial(1, 0), constant(alpha_sign*c_value*mate)),
            (constant(1), monomial(1, 1, c_value)),
            (constant(1), monomial(2, 0)),
            (constant(1), monomial(2, 1, -1)),
            (constant(1), {}, monomial(0, 2, -(mate*mate))),
        )
    if cell == "forced-ce":
        return (
            (constant(1), monomial(0, 1, c_value)),
            (constant(1), monomial(2, 0)),
            (constant(1), monomial(1, 0, -mate_over_c)),
            (constant(1), monomial(1, 1, -delta_sign)),
            (constant(1), {}, monomial(0, 2, -(mate_over_c**2))),
        )
    if cell == "forced-ef":
        return (
            (monomial(0, 1), constant(ef_sign*c_value*mate)),
            (monomial(0, 1), monomial(
                1, 0, -delta_sign*ef_sign*mate
            )),
            (constant(1), monomial(0, 1, c_value)),
            (constant(1), monomial(2, 0)),
            (constant(1), monomial(1, 1)),
            (constant(1), constant(mate)),
        )
    if cell == "s1-forced-loop":
        return (
            (constant(1), monomial(1, 0, c_value)),
            (constant(1), monomial(0, 1, c_value)),
            (constant(1), monomial(1, 0, theta)),
            (constant(1), monomial(0, 1, -delta_sign*theta)),
            (constant(1), {}, monomial(2, 2, -1)),
        )
    if cell == "s2-forced-colored":
        return (
            (constant(1), constant(mate)),
            (constant(1), monomial(2, 0)),
            (constant(1), {}, monomial(0, 2, -(mate_over_c**2))),
            (constant(1), {}, monomial(2, 2, -1)),
        )
    if cell == "s2-forced-df":
        return (
            (constant(1), {}, monomial(2, 0, -(c_value**2))),
            (constant(1), monomial(0, 2)),
            (constant(1), constant(mate)),
            (monomial(2, 0), {}, monomial(0, 2, -(mate**2))),
        )
    if cell == "s2-forced-ef":
        return (
            (constant(1), {}, monomial(2, 0, -(c_value**2))),
            (constant(1), monomial(0, 2)),
            (monomial(0, 2), {}, monomial(2, 0, -(mate**2))),
            (constant(1), constant(mate)),
        )
    if cell == "s2-forced-loop":
        return (
            (constant(1), {}, monomial(2, 0, -(c_value**2))),
            (constant(1), {}, monomial(2, 2, -1)),
            (constant(1), {}, monomial(0, 2, mate)),
        )
    if cell == "s0-forced-colored":
        return (
            (constant(1), monomial(0, 1, -c_value)),
            (constant(1), {}, monomial(2, 0, -(mate_over_c**2))),
            (constant(1), {}, monomial(2, 2, -1)),
            (constant(1), monomial(0, 1, -alpha_sign*mate_over_c)),
        )
    if cell == "s0-forced-ef":
        return (
            (constant(1), monomial(0, 1, -c_value)),
            (monomial(0, 1), constant(-alpha_sign*c_value*mate)),
            (constant(1), {}, monomial(2, 2, -1)),
            (monomial(0, 2), {}, monomial(2, 0, -(mate**2))),
        )
    if cell == "s0-forced-internal":
        return (
            (monomial(1, 0), constant(-c_value*mate)),
            (constant(1), monomial(0, 1, -c_value)),
            (constant(1), constant(mate)),
            (constant(1), {}, monomial(2, 2, -1)),
            (monomial(1, 0), monomial(0, 1, -alpha_sign*mate)),
        )
    raise ValueError(f"unsupported cell {cell}")


def equations(row, cell, alpha_sign=1, delta_sign=-1, ef_sign=1):
    b_value, c_value, mate = ROWS[row]
    gamma = b_value*(b_value+1) % P
    alpha = -(b_value**3+c_value**2) % P
    beta = -b_value*(b_value+1)*c_value**2 % P
    action = action_matrix(alpha, beta, gamma)
    coefficients = [constant(1)]
    for factor in factors_for(
        cell, c_value, mate, LOOP_ROOTS[row],
        alpha_sign, delta_sign, ef_sign
    ):
        coefficients = binary_mul(coefficients, factor)
    if len(coefficients) != 7:
        raise RuntimeError("residual form is not sextic")
    output = []
    for ell in range(3):
        equation = {}
        for j in range(7):
            equation = poly_add(
                equation, poly_scale(action[ell][j], coefficients[j])
            )
        output.append(equation)
    return output


def order_key(powers):
    return (sum(powers), -powers[1])


def leading(polynomial):
    powers = max(polynomial, key=order_key)
    return powers, polynomial[powers]


def shifted(polynomial, monomial_value, coefficient):
    return {
        (powers[0]+monomial_value[0], powers[1]+monomial_value[1]):
        coefficient*value % P
        for powers, value in polynomial.items()
    }


def monic(polynomial):
    polynomial = clean(polynomial)
    if not polynomial:
        return {}
    _, coefficient = leading(polynomial)
    return shifted(polynomial, (0, 0), pow(coefficient, -1, P))


def divides(left, right):
    return left[0] <= right[0] and left[1] <= right[1]


def reduce_polynomial(polynomial, basis, step_cap=200000):
    work = clean(polynomial)
    remainder = {}
    steps = 0
    while work:
        steps += 1
        if steps > step_cap:
            raise RuntimeError("reduction step cap")
        powers, coefficient = leading(work)
        divisor = None
        for candidate in basis:
            candidate_powers, candidate_coefficient = leading(candidate)
            if divides(candidate_powers, powers):
                divisor = candidate, candidate_powers, candidate_coefficient
                break
        if divisor is None:
            remainder[powers] = coefficient
            del work[powers]
            continue
        candidate, candidate_powers, candidate_coefficient = divisor
        shift = (powers[0]-candidate_powers[0],
                 powers[1]-candidate_powers[1])
        scalar = coefficient*pow(candidate_coefficient, -1, P) % P
        work = poly_add(work, poly_neg(shifted(candidate, shift, scalar)))
    return clean(remainder)


def s_polynomial(left, right):
    left_powers, left_coefficient = leading(left)
    right_powers, right_coefficient = leading(right)
    lcm = (max(left_powers[0], right_powers[0]),
           max(left_powers[1], right_powers[1]))
    first = shifted(
        left, (lcm[0]-left_powers[0], lcm[1]-left_powers[1]),
        pow(left_coefficient, -1, P),
    )
    second = shifted(
        right, (lcm[0]-right_powers[0], lcm[1]-right_powers[1]),
        pow(right_coefficient, -1, P),
    )
    return poly_add(first, poly_neg(second))


def buchberger(polynomials):
    basis = []
    for polynomial in polynomials:
        remainder = reduce_polynomial(polynomial, basis) if basis else polynomial
        if remainder:
            basis.append(monic(remainder))
    pairs = [(left, right) for left in range(len(basis))
             for right in range(left)]
    processed = 0
    while pairs:
        left, right = pairs.pop(0)
        processed += 1
        remainder = reduce_polynomial(s_polynomial(basis[left], basis[right]),
                                      basis)
        if not remainder:
            continue
        remainder = monic(remainder)
        if set(remainder) == {(0, 0)}:
            print(f"BUCHBERGER_UNIT pairs={processed}", flush=True)
            return [remainder], processed
        index = len(basis)
        basis.append(remainder)
        pairs.extend((index, old) for old in range(index))
        print(
            f"BUCHBERGER_PROGRESS basis={len(basis)} pairs={processed} "
            f"terms={len(remainder)} lm={leading(remainder)[0]}",
            flush=True,
        )
        if len(basis) > 80:
            raise RuntimeError("basis-length cap")
    print(f"BUCHBERGER_DONE basis={len(basis)} pairs={processed}", flush=True)
    return basis, processed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--row", type=int, choices=(0, 1), required=True)
    parser.add_argument("--cell", choices=(
        "forced-de", "forced-ce", "forced-ef",
        "s1-forced-loop",
        "s2-forced-colored", "s2-forced-df", "s2-forced-ef",
        "s2-forced-loop", "s0-forced-colored", "s0-forced-ef",
        "s0-forced-internal",
    ), required=True)
    parser.add_argument("--alpha-sign", type=int, choices=(-1, 1), default=1)
    parser.add_argument("--delta-sign", type=int, choices=(-1, 1), default=-1)
    parser.add_argument("--ef-sign", type=int, choices=(-1, 1), default=1)
    parser.add_argument("--dump", action="store_true")
    arguments = parser.parse_args()
    values = equations(
        arguments.row, arguments.cell, arguments.alpha_sign,
        arguments.delta_sign, arguments.ef_sign,
    )
    print(
        f"CELL36_OUTSIDE_BUILT row={arguments.row} cell={arguments.cell} "
        f"alpha={arguments.alpha_sign} delta={arguments.delta_sign} "
        f"ef={arguments.ef_sign} terms={tuple(map(len, values))} "
        f"leaders={tuple(leading(value)[0] for value in values)}",
        flush=True,
    )
    basis, pairs = buchberger(values)
    print(
        f"CELL36_OUTSIDE_RESULT unit={int(basis == [constant(1)])} "
        f"basis={len(basis)} pairs={pairs}",
        flush=True,
    )
    if arguments.dump:
        for index, polynomial in enumerate(basis):
            print(f"basis[{index}]={polynomial}", flush=True)


if __name__ == "__main__":
    main()
