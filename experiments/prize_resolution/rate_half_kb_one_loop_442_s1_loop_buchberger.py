#!/usr/bin/env python3
"""Solve a forced-loop S1 cell over the quadratic common-field extension."""

import argparse
import importlib.util
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER_PATH = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_one_loop_442_s1_quotient_buchberger.py"
)
SPEC = importlib.util.spec_from_file_location("solver", SOLVER_PATH)
SOLVER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SOLVER)
BUILDER = SOLVER.BUILDER
P = SOLVER.P
Q3 = P**3

BZERO = SOLVER.ZERO
BONE = SOLVER.ONE
EZERO = (BZERO, BZERO)
EONE = (BONE, BZERO)


def eadd(left, right):
    return (SOLVER.add(left[0], right[0]), SOLVER.add(left[1], right[1]))


def eneg(value):
    return (SOLVER.neg(value[0]), SOLVER.neg(value[1]))


def emul(left, right, modulus, square):
    constant = SOLVER.add(
        SOLVER.multiply(left[0], right[0], modulus),
        SOLVER.multiply(
            SOLVER.multiply(left[1], right[1], modulus), square, modulus
        ),
    )
    linear = SOLVER.add(
        SOLVER.multiply(left[0], right[1], modulus),
        SOLVER.multiply(left[1], right[0], modulus),
    )
    return constant, linear


def einverse(value, modulus, square):
    if value == EZERO:
        raise ZeroDivisionError("zero in quadratic extension")
    denominator = SOLVER.sub(
        SOLVER.multiply(value[0], value[0], modulus),
        SOLVER.multiply(
            SOLVER.multiply(value[1], value[1], modulus), square, modulus
        ),
    )
    inverse_denominator = SOLVER.inverse(denominator, modulus)
    return (
        SOLVER.multiply(value[0], inverse_denominator, modulus),
        SOLVER.neg(SOLVER.multiply(value[1], inverse_denominator, modulus)),
    )


def epower(value, exponent, modulus, square):
    result = EONE
    base = value
    while exponent:
        if exponent & 1:
            result = emul(result, base, modulus, square)
        base = emul(base, base, modulus, square)
        exponent //= 2
    return result


def embed(value):
    return value, BZERO


def escale(scalar, value):
    return embed(SOLVER.scale(scalar, value))


def common_values(component, epsilon_1=1, epsilon_2=1):
    b, r, t, d_c, vector, polynomial, matrix = BUILDER.common_data(
        epsilon_1, epsilon_2
    )
    x = r**2
    a_poly = x**2-6*x+1
    b_poly = (x+1)**2
    c_numerator = b*(b*a_poly+b_poly)
    c_coordinates = matrix(d_c).inv_mod(P)*vector(c_numerator)
    c_value = polynomial(c_coordinates % P)
    d_m = b**3-b**2*c_value+3*b*c_value+c_value**2
    mate_numerator = -b*(b**3+3*b**2*c_value-b*c_value+c_value**2)
    mate_coordinates = matrix(d_m).inv_mod(P)*vector(mate_numerator)
    mate_value = polynomial(mate_coordinates % P)

    def project_value(expression):
        multiplication = BUILDER.SELECTOR.as_lists(matrix(expression))
        coordinates = tuple(multiplication[index][0]
                            for index in range(BUILDER.SELECTOR.SIZE))
        return SOLVER.project(
            coordinates, SOLVER.CUBICS[component], epsilon_1, epsilon_2
        )

    return project_value(c_value), project_value(mate_value)


def pclean(polynomial):
    return {powers: coefficient for powers, coefficient in polynomial.items()
            if coefficient != EZERO}


def padd(left, right):
    output = dict(left)
    for powers, coefficient in right.items():
        output[powers] = eadd(output.get(powers, EZERO), coefficient)
    return pclean(output)


def pneg(polynomial):
    return {powers: eneg(coefficient) for powers, coefficient in polynomial.items()}


def pmul(left, right, modulus, square):
    output = {}
    for (e_left, f_left), first in left.items():
        for (e_right, f_right), second in right.items():
            powers = (e_left+e_right, f_left+f_right)
            term = emul(first, second, modulus, square)
            output[powers] = eadd(output.get(powers, EZERO), term)
    return pclean(output)


def pleft(value, polynomial, modulus, square):
    return {powers: emul(value, coefficient, modulus, square)
            for powers, coefficient in polynomial.items()}


def binary_mul(left, right, modulus, square):
    output = [{} for _ in range(len(left)+len(right)-1)]
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            output[i+j] = padd(output[i+j], pmul(first, second, modulus, square))
    return output


def order_key(powers):
    return (sum(powers), -powers[1])


def leading(polynomial):
    powers = max(polynomial, key=order_key)
    return powers, polynomial[powers]


def shifted(polynomial, monomial, coefficient, modulus, square):
    return {
        (powers[0]+monomial[0], powers[1]+monomial[1]):
        emul(coefficient, value, modulus, square)
        for powers, value in polynomial.items()
    }


def monic(polynomial, modulus, square):
    polynomial = pclean(polynomial)
    if not polynomial:
        return {}
    _, coefficient = leading(polynomial)
    return shifted(polynomial, (0, 0),
                   einverse(coefficient, modulus, square), modulus, square)


def divides(left, right):
    return left[0] <= right[0] and left[1] <= right[1]


def reduce_polynomial(polynomial, basis, modulus, square, step_cap=200000):
    work = pclean(polynomial)
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
        monomial = (powers[0]-candidate_powers[0],
                    powers[1]-candidate_powers[1])
        scalar = emul(coefficient,
                      einverse(candidate_coefficient, modulus, square),
                      modulus, square)
        work = padd(work, pneg(shifted(
            candidate, monomial, scalar, modulus, square
        )))
    return pclean(remainder)


def s_polynomial(left, right, modulus, square):
    left_powers, left_coefficient = leading(left)
    right_powers, right_coefficient = leading(right)
    lcm = (max(left_powers[0], right_powers[0]),
           max(left_powers[1], right_powers[1]))
    first = shifted(
        left, (lcm[0]-left_powers[0], lcm[1]-left_powers[1]),
        einverse(left_coefficient, modulus, square), modulus, square,
    )
    second = shifted(
        right, (lcm[0]-right_powers[0], lcm[1]-right_powers[1]),
        einverse(right_coefficient, modulus, square), modulus, square,
    )
    return padd(first, pneg(second))


def buchberger(equations, modulus, square):
    basis = []
    for equation in equations:
        remainder = (reduce_polynomial(equation, basis, modulus, square)
                     if basis else equation)
        if remainder:
            basis.append(monic(remainder, modulus, square))
    pairs = [(left, right) for left in range(len(basis))
             for right in range(left)]
    processed = 0
    while pairs:
        left, right = pairs.pop(0)
        processed += 1
        remainder = reduce_polynomial(
            s_polynomial(basis[left], basis[right], modulus, square),
            basis, modulus, square,
        )
        if not remainder:
            continue
        remainder = monic(remainder, modulus, square)
        if set(remainder) == {(0, 0)}:
            print(f"LOOP_BUCHBERGER_UNIT pairs={processed}", flush=True)
            return [remainder]
        index = len(basis)
        basis.append(remainder)
        pairs.extend((index, old) for old in range(index))
        print(
            f"LOOP_BUCHBERGER_PROGRESS basis={len(basis)} pairs={processed} "
            f"terms={len(remainder)} lm={leading(remainder)[0]}", flush=True,
        )
        if len(basis) > 80:
            raise RuntimeError("basis-length cap")
    print(f"LOOP_BUCHBERGER_DONE basis={len(basis)} pairs={processed}", flush=True)
    return basis


def build_equations(component, delta_sign, epsilon_1=1, epsilon_2=1):
    modulus = SOLVER.CUBICS[component]
    c_base, mate_base = common_values(component, epsilon_1, epsilon_2)
    square = SOLVER.neg(mate_base)
    legendre = SOLVER.power(square, (Q3-1)//2, modulus)
    if legendre != SOLVER.neg(BONE):
        raise RuntimeError(f"loop quadratic is not irreducible: {legendre}")

    b = embed(SOLVER.B_ELEMENT)
    c = embed(c_base)
    mate = embed(mate_base)
    theta = (BZERO, BONE)
    alpha = eneg(emul(b, eadd(c, emul(b, b, modulus, square)), modulus, square))
    beta = emul(
        emul(b, b, modulus, square),
        eadd(eadd(c, eneg(emul(b, b, modulus, square))),
             eneg(emul(escale(2, BONE), emul(b, c, modulus, square),
                       modulus, square))),
        modulus, square,
    )
    gamma = eadd(eadd(c, emul(escale(2, BONE), b, modulus, square)),
                 eneg(emul(b, b, modulus, square)))
    determinant = eadd(emul(alpha, alpha, modulus, square),
                       emul(beta, gamma, modulus, square))

    action = [[EZERO for _ in range(7)] for _ in range(3)]
    for ell in range(3):
        for j in range(7):
            value = EZERO
            for q in range(max(0, ell-(6-j)), min(ell, j)+1):
                p = ell-q
                term = emul(
                    emul(epower(alpha, 6-j-p, modulus, square),
                         epower(beta, p, modulus, square), modulus, square),
                    emul(epower(gamma, j-q, modulus, square),
                         epower(alpha, q, modulus, square), modulus, square),
                    modulus, square,
                )
                scalar = math.comb(6-j, p)*math.comb(j, q)
                if q % 2:
                    scalar = -scalar
                value = eadd(value, emul(escale(scalar, BONE), term,
                                         modulus, square))
            if ell == j:
                value = eadd(value, eneg(epower(determinant, 3,
                                                modulus, square)))
            action[ell][j] = value

    constant = lambda value: {(0, 0): value}
    monomial = lambda e_power, f_power, value=EONE: {
        (e_power, f_power): value
    }
    factors = (
        (constant(EONE), monomial(1, 0, c)),
        (constant(EONE), monomial(0, 1, c)),
        (constant(EONE), monomial(1, 0, theta)),
        (constant(EONE), monomial(0, 1,
                                  eneg(emul(escale(delta_sign, BONE), theta,
                                            modulus, square)))),
        (constant(EONE), {}, monomial(2, 2, eneg(EONE))),
    )
    coefficients = [constant(EONE)]
    for factor in factors:
        coefficients = binary_mul(coefficients, factor, modulus, square)

    equations = []
    for ell in range(3):
        equation = {}
        for j in range(7):
            equation = padd(
                equation, pleft(action[ell][j], coefficients[j], modulus, square)
            )
        equations.append(equation)
    return modulus, square, equations


def solve(component, delta_sign, epsilon_1=1, epsilon_2=1):
    modulus, square, equations = build_equations(
        component, delta_sign, epsilon_1, epsilon_2
    )
    print(
        "S1_LOOP_COMPONENT_BUILT "
        f"component={component} delta_sign={delta_sign} "
        f"common_signs={epsilon_1},{epsilon_2} "
        f"terms={tuple(len(equation) for equation in equations)} "
        f"leaders={tuple(leading(equation)[0] for equation in equations)}",
        flush=True,
    )
    return equations, buchberger(equations, modulus, square)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("component", type=int, choices=(0, 1))
    parser.add_argument("--delta-sign", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--epsilon-1", type=int, choices=(-1, 1), default=1)
    parser.add_argument("--epsilon-2", type=int, choices=(-1, 1), default=1)
    arguments = parser.parse_args()
    _, basis = solve(
        arguments.component, arguments.delta_sign,
        arguments.epsilon_1, arguments.epsilon_2,
    )
    print(
        "S1_LOOP_COMPONENT_RESULT "
        f"component={arguments.component} delta_sign={arguments.delta_sign} "
        f"common_signs={arguments.epsilon_1},{arguments.epsilon_2} "
        f"unit={basis == [{(0, 0): EONE}]} basis={len(basis)}",
        flush=True,
    )


if __name__ == "__main__":
    main()
