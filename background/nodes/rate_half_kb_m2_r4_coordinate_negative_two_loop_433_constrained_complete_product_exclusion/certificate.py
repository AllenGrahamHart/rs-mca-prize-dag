#!/usr/bin/env python3
"""Exact quotient-algebra certificate for the X2/N1/L1 product cells."""

import argparse
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
M23_NODE = ROOT / "background/nodes/rate_half_kb_m2_r4_coordinate_negative_two_loop_433_m2_m3_complete_product_exclusion"
sys.path.insert(0, str(M23_NODE))
import certificate as universal  # noqa: E402


PRIME = 2130706433


class ResidueField:
    def __init__(self, modulus):
        leading_inverse = pow(modulus[-1] % PRIME, -1, PRIME)
        self.modulus = tuple(value * leading_inverse % PRIME for value in modulus)
        self.degree = len(modulus) - 1
        self.zero = (0,) * self.degree
        self.one = (1,) + (0,) * (self.degree - 1)
        self.symbol = sp.symbols("T")
        self.poly = sp.Poly(
            sum(self.modulus[index] * self.symbol**index
                for index in range(self.degree + 1)),
            self.symbol,
            modulus=PRIME,
        )

    def const(self, value):
        return (value % PRIME,) + (0,) * (self.degree - 1)

    def generator(self):
        return (0, 1) + (0,) * (self.degree - 2)

    def add(self, left, right):
        return tuple((left[i] + right[i]) % PRIME for i in range(self.degree))

    def neg(self, value):
        return tuple(-coefficient % PRIME for coefficient in value)

    def scale(self, value, scalar):
        return tuple(coefficient * scalar % PRIME for coefficient in value)

    def mul(self, left, right):
        product = [0] * (2*self.degree - 1)
        for i, x_value in enumerate(left):
            for j, y_value in enumerate(right):
                product[i + j] = (product[i + j] + x_value*y_value) % PRIME
        for degree in range(2*self.degree - 2, self.degree - 1, -1):
            leading = product[degree] % PRIME
            for offset, coefficient in enumerate(self.modulus[:-1]):
                product[degree - self.degree + offset] = (
                    product[degree - self.degree + offset] - leading*coefficient
                ) % PRIME
        return tuple(value % PRIME for value in product[:self.degree])

    def pow(self, value, exponent):
        output = self.one
        factor = value
        while exponent:
            if exponent & 1:
                output = self.mul(output, factor)
            factor = self.mul(factor, factor)
            exponent //= 2
        return output

    def to_poly(self, value):
        return sp.Poly(
            sum(value[index]*self.symbol**index for index in range(self.degree)),
            self.symbol,
            modulus=PRIME,
        )

    def from_poly(self, polynomial):
        output = [0] * self.degree
        for (degree,), coefficient in sp.Poly(
            polynomial, self.symbol, modulus=PRIME
        ).terms():
            output[degree] = int(coefficient) % PRIME
        return tuple(output)

    def inverse(self, value):
        return self.from_poly(sp.invert(self.to_poly(value), self.poly).as_expr())

    def is_unit(self, value):
        return sp.gcd(self.to_poly(value), self.poly).degree() == 0


class Element:
    __slots__ = ("field", "u", "v", "q_coefficient")

    def __init__(self, field, u_value, v_value, q_coefficient):
        self.field = field
        self.u = u_value
        self.v = v_value
        self.q_coefficient = q_coefficient

    def lift(self, value):
        if isinstance(value, Element):
            return value
        if isinstance(value, tuple):
            return Element(self.field, value, self.field.zero, self.q_coefficient)
        return Element(
            self.field, self.field.const(int(value)), self.field.zero,
            self.q_coefficient,
        )

    def __add__(self, other):
        other = self.lift(other)
        return Element(
            self.field, self.field.add(self.u, other.u),
            self.field.add(self.v, other.v), self.q_coefficient,
        )

    __radd__ = __add__

    def __neg__(self):
        return Element(
            self.field, self.field.neg(self.u), self.field.neg(self.v),
            self.q_coefficient,
        )

    def __sub__(self, other):
        return self + (-self.lift(other))

    def __rsub__(self, other):
        return self.lift(other) - self

    def __mul__(self, other):
        other = self.lift(other)
        field = self.field
        return Element(
            field,
            field.add(field.mul(self.u, other.u), field.neg(field.mul(self.v, other.v))),
            field.add(
                field.add(field.mul(self.u, other.v), field.mul(self.v, other.u)),
                field.mul(self.q_coefficient, field.mul(self.v, other.v)),
            ),
            self.q_coefficient,
        )

    __rmul__ = __mul__

    def __pow__(self, exponent):
        output = self.lift(1)
        factor = self
        while exponent:
            if exponent & 1:
                output = output * factor
            factor = factor * factor
            exponent //= 2
        return output

    def norm(self):
        field = self.field
        return field.add(
            field.add(
                field.mul(self.u, self.u),
                field.mul(self.q_coefficient, field.mul(self.u, self.v)),
            ),
            field.mul(self.v, self.v),
        )

    def inverse(self):
        field = self.field
        norm_inverse = field.inverse(self.norm())
        return Element(
            field,
            field.mul(
                field.add(self.u, field.mul(self.q_coefficient, self.v)),
                norm_inverse,
            ),
            field.mul(field.neg(self.v), norm_inverse),
            self.q_coefficient,
        )

    def __truediv__(self, other):
        return self * self.lift(other).inverse()

    def __rtruediv__(self, other):
        return self.lift(other) * self.inverse()

    def is_unit(self):
        return self.field.is_unit(self.norm())

    def is_zero(self):
        return self.u == self.field.zero and self.v == self.field.zero

    def is_unit_by_matrix(self):
        basis = []
        for side in range(2):
            for degree in range(self.field.degree):
                coefficient = [0] * self.field.degree
                coefficient[degree] = 1
                basis.append(Element(
                    self.field,
                    tuple(coefficient) if side == 0 else self.field.zero,
                    self.field.zero if side == 0 else tuple(coefficient),
                    self.q_coefficient,
                ))
        dimension = 2*self.field.degree
        columns = []
        for vector in basis:
            product = self * vector
            columns.append((*product.u, *product.v))
        matrix = [[columns[column][row] % PRIME for column in range(dimension)]
                  for row in range(dimension)]
        rank = 0
        for column in range(dimension):
            pivot = next(
                (row for row in range(rank, dimension) if matrix[row][column]), None
            )
            if pivot is None:
                continue
            matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
            inverse = pow(matrix[rank][column], -1, PRIME)
            matrix[rank] = [value*inverse % PRIME for value in matrix[rank]]
            for row in range(dimension):
                if row == rank or not matrix[row][column]:
                    continue
                scalar = matrix[row][column]
                matrix[row] = [
                    (matrix[row][index] - scalar*matrix[rank][index]) % PRIME
                    for index in range(dimension)
                ]
            rank += 1
        return rank == dimension


def p8_base(name):
    field = ResidueField((1, 8, -2, 8, 1))
    m_value = field.generator()
    one = field.one
    m_plus = field.add(m_value, one)
    m_minus = field.add(m_value, field.neg(one))
    sign = -1 if name == "X2" else 1
    ratio = field.mul(
        field.pow(m_minus, 2), field.inverse(field.pow(m_plus, 2))
    )
    q_coefficient = field.scale(ratio, -sign)
    c_value = Element(field, field.zero, field.one, q_coefficient)
    m_element = Element(field, m_value, field.zero, q_coefficient)
    b_value = -(c_value**3)
    if name == "X2":
        p_value = (
            -2*m_element**3*c_value + 3*m_element**3
            - 16*m_element**2*c_value + 24*m_element**2
            + 6*m_element*c_value - 9*m_element - 36*c_value + 32
        ) / 22
        gamma = c_value**3 + c_value - 1
        alpha = -c_value**3*(c_value**2 - c_value + 1)
        beta = c_value**5*(c_value**3 - c_value**2 - 1)
    else:
        p_value = (
            2*m_element**3*c_value + 3*m_element**3
            + 16*m_element**2*c_value + 24*m_element**2
            - 6*m_element*c_value - 9*m_element + 36*c_value + 32
        ) / 22
        gamma = c_value**3 + c_value + 1
        alpha = -c_value**3*(c_value**2 + c_value + 1)
        beta = -c_value**5*(c_value**3 + c_value**2 + 1)
    return b_value, c_value, p_value, gamma, alpha, beta


def l1_base():
    field = ResidueField((2, 0, 3, 0, 2))
    c_generator = field.generator()
    q_coefficient = field.zero
    m_value = Element(field, field.zero, field.one, q_coefficient)
    c_value = Element(field, c_generator, field.zero, q_coefficient)
    b_value = -(c_value**3)
    p_value = (3*c_value**2 + 10) / 8
    gamma = -c_value**2*(c_value**2 + 1)
    alpha = 2*c_value**6
    beta = c_value**8*(c_value**2 + 1)
    return b_value, c_value, p_value, gamma, alpha, beta


def parameter_values(kind, tau, data):
    b_value, c_value, forced, gamma, alpha, beta = data
    if kind == "bD":
        return (tau*forced/(b_value*c_value), b_value/(c_value*forced),
                gamma, alpha, beta)
    if kind == "cE":
        return (tau*forced/(b_value*c_value), b_value*forced/c_value,
                gamma, alpha, beta)
    if kind == "DE":
        return (tau*forced*b_value*c_value, tau*forced*b_value**2,
                gamma, alpha, beta)
    if kind == "DF":
        return (tau/(b_value*c_value), b_value*forced/c_value, forced,
                gamma, alpha, beta)
    if kind == "EF":
        return (tau/(b_value*c_value), c_value*forced/b_value, forced,
                gamma, alpha, beta)
    raise RuntimeError(kind)


def evaluate(polynomial, values):
    terms = polynomial.terms()
    powers = []
    for position, value in enumerate(values):
        maximum = max(monomial[position] for monomial, _ in terms)
        powers.append([value**exponent for exponent in range(maximum + 1)])
    output = values[0].lift(0)
    for monomial, coefficient in terms:
        term = values[0].lift(int(coefficient))
        for position, exponent in enumerate(monomial):
            term = term * powers[position][exponent]
        output = output + term
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--preferred-chain", type=int, choices=(0, 1), default=0)
    parser.add_argument("--kind", choices=tuple(universal.TYPE_DATA))
    parser.add_argument("--cell", choices=("X2", "N1", "L1"))
    parser.add_argument("--matching", type=int, choices=tuple(range(15)))
    parser.add_argument("--unit-check", choices=("norm", "matrix"), default="norm")
    arguments = parser.parse_args()
    kinds = (arguments.kind,) if arguments.kind else tuple(universal.TYPE_DATA)
    cells = (arguments.cell,) if arguments.cell else ("X2", "N1", "L1")
    matchings = ((arguments.matching,) if arguments.matching is not None
                 else tuple(range(15)))

    compiled = {}
    chain_counts = {0: 0, 1: 0, 2: 0}
    for kind in kinds:
        for index in matchings:
            order = (arguments.preferred_chain, 1 - arguments.preferred_chain, 2)
            polynomial = None
            for shared_index in order:
                polynomial = universal.obstruction_polynomial(kind, index, shared_index)
                if polynomial is not None:
                    chain_counts[shared_index] += 1
                    break
            compiled[(kind, index)] = polynomial

    base = {"X2": p8_base("X2"), "N1": p8_base("N1"), "L1": l1_base()}
    units = 0
    failures = []
    for cell in cells:
        data = base[cell]
        for name, value in zip(("b", "c", "p", "Gamma", "Alpha", "Beta"), data):
            is_unit = (value.is_unit() if arguments.unit_check == "norm"
                       else value.is_unit_by_matrix())
            if not is_unit:
                raise RuntimeError(f"nonunit base value {cell}/{name}")
        for tau in (-1, 1):
            for kind in kinds:
                values = parameter_values(kind, tau, data)
                for index in matchings:
                    result = evaluate(compiled[(kind, index)], values)
                    is_unit = (result.is_unit() if arguments.unit_check == "norm"
                               else result.is_unit_by_matrix())
                    if is_unit:
                        units += 1
                    else:
                        failures.append((cell, tau, kind, index,
                                         "ZERO" if result.is_zero() else "ZERO_DIVISOR"))
    if failures:
        raise RuntimeError(f"nonunit constrained obstructions: {failures}")
    print(
        "KB_433_CONSTRAINED_PAIRING_PASS "
        f"preferred_chain={arguments.preferred_chain} cells={','.join(cells)} "
        f"kinds={','.join(kinds)} matchings={','.join(map(str, matchings))} "
        f"units={units} unit_check={arguments.unit_check} "
        f"chain0={chain_counts[0]} chain1={chain_counts[1]} "
        f"chain2={chain_counts[2]}"
    )


if __name__ == "__main__":
    main()
