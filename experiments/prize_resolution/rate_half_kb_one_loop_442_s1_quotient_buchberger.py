#!/usr/bin/env python3
"""Run a sparse forced-record pass in each cubic common component."""

import argparse
import functools
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BUILDER_PATH = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_one_loop_442_s1_deployed_cell.py"
)
SPEC = importlib.util.spec_from_file_location("builder", BUILDER_PATH)
BUILDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILDER)
P = BUILDER.P
IOTA = BUILDER.IOTA

CUBICS = (
    (1057281976, -1005684111, 674394299),
    (414697007, 424510262, -674394301),
)


def add(left, right):
    return tuple((left[index]+right[index]) % P for index in range(3))


def neg(value):
    return tuple(-entry % P for entry in value)


def sub(left, right):
    return add(left, neg(right))


def scale(scalar, value):
    return tuple(scalar*entry % P for entry in value)


def multiply(left, right, modulus):
    work = [0]*5
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            work[i+j] = (work[i+j]+first*second) % P
    a0, a1, a2 = (entry % P for entry in modulus)
    for degree in (4, 3):
        coefficient = work[degree] % P
        work[degree] = 0
        shift = degree-3
        work[shift] = (work[shift]-coefficient*a0) % P
        work[shift+1] = (work[shift+1]-coefficient*a1) % P
        work[shift+2] = (work[shift+2]-coefficient*a2) % P
    return tuple(work[:3])


ONE = (1, 0, 0)
ZERO = (0, 0, 0)
B_ELEMENT = (0, 1, 0)


def power(value, exponent, modulus):
    result = ONE
    base = value
    while exponent:
        if exponent & 1:
            result = multiply(result, base, modulus)
        base = multiply(base, base, modulus)
        exponent //= 2
    return result


def inverse(value, modulus):
    if value == ZERO:
        raise ZeroDivisionError("zero in cubic field")
    return power(value, P**3-2, modulus)


@functools.lru_cache(maxsize=None)
def projected_basis(modulus, epsilon_1=1, epsilon_2=1):
    if (epsilon_1, epsilon_2) != (1, 1):
        b, c, r, t = BUILDER.sp.symbols("b c r t")
        cubic, product, weld, _ = BUILDER.MATE.PARENT.common_generators(
            epsilon_1, epsilon_2, b, c, r, t
        )
        factor = b**3+modulus[2]*b**2+modulus[1]*b+modulus[0]
        basis = BUILDER.sp.groebner(
            (cubic, factor, product, weld), t, r, b,
            order="lex", method="f5b", modulus=P,
        )

        def project_expression(expression):
            remainder = BUILDER.sp.Poly(
                basis.reduce(expression)[1], t, r, b, modulus=P
            )
            coordinates = [0, 0, 0]
            for powers, coefficient in remainder.terms():
                if powers[0] or powers[1] or powers[2] > 2:
                    raise RuntimeError(
                        f"non-cubic projection {epsilon_1},{epsilon_2}: "
                        f"{remainder.as_expr()}"
                    )
                coordinates[powers[2]] = int(coefficient) % P
            return tuple(coordinates)

        values = tuple(project_expression(expression) for expression in (
            BUILDER.sp.Integer(1), b, b**2, r, b*r, t
        ))
        if values[:3] != (ONE, B_ELEMENT,
                          multiply(B_ELEMENT, B_ELEMENT, modulus)):
            raise RuntimeError("common quotient cubic basis")
        return values

    r_numerator = (-1 % P, (IOTA+1) % P, -1 % P)
    r_denominator = (1, (IOTA-1) % P, 1)
    r_value = multiply(r_numerator, inverse(r_denominator, modulus), modulus)
    t_value = scale(-IOTA, inverse(r_value, modulus))
    br_value = multiply(B_ELEMENT, r_value, modulus)
    b_squared = multiply(B_ELEMENT, B_ELEMENT, modulus)
    b_cubed = multiply(b_squared, B_ELEMENT, modulus)

    def total(*values):
        result = ZERO
        for value in values:
            result = add(result, value)
        return result

    inverse_2 = pow(2, -1, P)
    relations = (
        total(multiply(b_squared, r_value, modulus), b_squared,
              scale(IOTA-1, br_value), scale(-(IOTA+1), B_ELEMENT),
              r_value, ONE),
        total(b_cubed, scale(-(IOTA+1), b_squared),
              scale(IOTA-1, br_value), scale(IOTA+2, B_ELEMENT),
              scale((IOTA+1)*inverse_2, add(r_value, t_value)),
              scale(-IOTA, ONE)),
        total(multiply(t_value, t_value, modulus), scale(-IOTA, r_value),
              scale(-(2*IOTA+1), t_value), scale(-(2*IOTA-1), ONE)),
        total(multiply(r_value, t_value, modulus), scale(IOTA, ONE)),
        total(multiply(r_value, r_value, modulus), scale(IOTA+2, r_value),
              t_value, scale(-(2*IOTA+1), ONE)),
        total(scale(IOTA-1, b_squared),
              multiply(B_ELEMENT, add(r_value, t_value), modulus),
              scale(-(IOTA-1), B_ELEMENT), scale(IOTA-1, ONE)),
    )
    if any(relation != ZERO for relation in relations):
        raise RuntimeError(f"common quotient projection: {relations}")
    return (ONE, B_ELEMENT, b_squared, r_value, br_value, t_value)


def project(coordinates, modulus, epsilon_1=1, epsilon_2=1):
    value = ZERO
    for scalar, element in zip(
        coordinates, projected_basis(modulus, epsilon_1, epsilon_2)
    ):
        value = add(value, scale(scalar, element))
    return value


def clean(polynomial):
    return {powers: coefficient for powers, coefficient in polynomial.items()
            if coefficient != ZERO}


def poly_add(left, right):
    output = dict(left)
    for powers, coefficient in right.items():
        output[powers] = add(output.get(powers, ZERO), coefficient)
    return clean(output)


def poly_neg(polynomial):
    return {powers: neg(coefficient) for powers, coefficient in polynomial.items()}


def order_key(powers):
    return (sum(powers), -powers[1])


def leading(polynomial):
    powers = max(polynomial, key=order_key)
    return powers, polynomial[powers]


def shifted(polynomial, monomial, coefficient, modulus):
    return {
        (powers[0]+monomial[0], powers[1]+monomial[1]):
        multiply(coefficient, value, modulus)
        for powers, value in polynomial.items()
    }


def monic(polynomial, modulus):
    polynomial = clean(polynomial)
    if not polynomial:
        return {}
    _, coefficient = leading(polynomial)
    return shifted(polynomial, (0, 0), inverse(coefficient, modulus), modulus)


def divides(left, right):
    return left[0] <= right[0] and left[1] <= right[1]


def reduce_polynomial(polynomial, basis, modulus, step_cap=200000):
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
                divisor = (candidate, candidate_powers, candidate_coefficient)
                break
        if divisor is None:
            remainder[powers] = coefficient
            del work[powers]
            continue
        candidate, candidate_powers, candidate_coefficient = divisor
        monomial = (powers[0]-candidate_powers[0],
                    powers[1]-candidate_powers[1])
        scalar = multiply(coefficient, inverse(candidate_coefficient, modulus),
                          modulus)
        work = poly_add(work, poly_neg(shifted(
            candidate, monomial, scalar, modulus
        )))
    return clean(remainder)


def s_polynomial(left, right, modulus):
    left_powers, left_coefficient = leading(left)
    right_powers, right_coefficient = leading(right)
    lcm = (max(left_powers[0], right_powers[0]),
           max(left_powers[1], right_powers[1]))
    left_shift = (lcm[0]-left_powers[0], lcm[1]-left_powers[1])
    right_shift = (lcm[0]-right_powers[0], lcm[1]-right_powers[1])
    first = shifted(left, left_shift, inverse(left_coefficient, modulus), modulus)
    second = shifted(right, right_shift, inverse(right_coefficient, modulus),
                     modulus)
    return poly_add(first, poly_neg(second))


def buchberger(equations, modulus):
    basis = []
    for equation in equations:
        remainder = reduce_polynomial(equation, basis, modulus) if basis else equation
        if remainder:
            basis.append(monic(remainder, modulus))
    pairs = [(left, right) for left in range(len(basis))
             for right in range(left)]
    processed = 0
    while pairs:
        left, right = pairs.pop(0)
        processed += 1
        remainder = reduce_polynomial(
            s_polynomial(basis[left], basis[right], modulus), basis, modulus
        )
        if not remainder:
            continue
        remainder = monic(remainder, modulus)
        if set(remainder) == {(0, 0)}:
            print(f"BUCHBERGER_UNIT pairs={processed}", flush=True)
            return [remainder]
        index = len(basis)
        basis.append(remainder)
        pairs.extend((index, old) for old in range(index))
        print(
            f"BUCHBERGER_PROGRESS basis={len(basis)} pairs={processed} "
            f"new_terms={len(remainder)} lm={leading(remainder)[0]}",
            flush=True,
        )
        if len(basis) > 80:
            raise RuntimeError("basis-length cap")
    print(f"BUCHBERGER_DONE basis={len(basis)} pairs={processed}", flush=True)
    return basis


def component_equations(matrix_equations, modulus, epsilon_1=1, epsilon_2=1):
    equations = []
    for equation in matrix_equations:
        projected = {}
        for powers, matrix in equation.items():
            coordinates = tuple(matrix[index][0]
                                for index in range(BUILDER.SELECTOR.SIZE))
            projected[powers] = project(
                coordinates, modulus, epsilon_1, epsilon_2
            )
        equations.append(clean(projected))
    return equations


def solve_component(component, alpha_sign=1, cell="forced-de", delta_sign=-1,
                    ef_sign=1, epsilon_1=1, epsilon_2=1):
    _, _, _, matrix_equations = BUILDER.build(
        alpha_sign, cell, delta_sign, ef_sign, epsilon_1, epsilon_2
    )
    modulus = CUBICS[component]
    equations = component_equations(
        matrix_equations, modulus, epsilon_1, epsilon_2
    )
    print(
        "S1_QUOTIENT_COMPONENT_BUILT "
        f"component={component} cell={cell} alpha_sign={alpha_sign} "
        f"delta_sign={delta_sign} ef_sign={ef_sign} "
        f"common_signs={epsilon_1},{epsilon_2} "
        f"terms={tuple(len(equation) for equation in equations)} "
        f"leaders={tuple(leading(equation)[0] for equation in equations)}",
        flush=True,
    )
    return equations, buchberger(equations, modulus)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("component", type=int, choices=(0, 1))
    parser.add_argument("--alpha-sign", type=int, choices=(-1, 1), default=1)
    parser.add_argument("--cell", choices=("forced-de", "forced-ce", "forced-ef",
                                            "s2-forced-colored"),
                        default="forced-de")
    parser.add_argument("--delta-sign", type=int, choices=(-1, 1), default=-1)
    parser.add_argument("--ef-sign", type=int, choices=(-1, 1), default=1)
    parser.add_argument("--epsilon-1", type=int, choices=(-1, 1), default=1)
    parser.add_argument("--epsilon-2", type=int, choices=(-1, 1), default=1)
    arguments = parser.parse_args()
    _, basis = solve_component(
        arguments.component, arguments.alpha_sign,
        arguments.cell, arguments.delta_sign, arguments.ef_sign,
        arguments.epsilon_1, arguments.epsilon_2,
    )
    print(
        "S1_QUOTIENT_COMPONENT_RESULT "
        f"component={arguments.component} cell={arguments.cell} "
        f"alpha_sign={arguments.alpha_sign} delta_sign={arguments.delta_sign} "
        f"ef_sign={arguments.ef_sign} "
        f"common_signs={arguments.epsilon_1},{arguments.epsilon_2} "
        f"unit={basis == [{(0, 0): ONE}]} "
        f"basis={len(basis)}",
        flush=True,
    )


if __name__ == "__main__":
    main()
