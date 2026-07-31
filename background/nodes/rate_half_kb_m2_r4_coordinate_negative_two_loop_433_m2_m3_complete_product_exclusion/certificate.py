#!/usr/bin/env python3
"""Exact low-memory certificate for the M2/M3 paired-product cells.

Universal two-variable matching resultants are evaluated in the deployed
12-dimensional base algebra instead of forming a four-variable Groebner
basis.
"""

import argparse

import sympy as sp


PRIME = 2130706433
INV4 = pow(4, -1, PRIME)
INV8 = pow(8, -1, PRIME)
MODULUS = (1, 2, 7, -4, 7, 2, 1)  # ascending P_6 coefficients
ZERO = (0,) * 6
ONE = (1, 0, 0, 0, 0, 0)


def k_const(value):
    return (value % PRIME, 0, 0, 0, 0, 0)


def k_add(left, right):
    return tuple((left[i] + right[i]) % PRIME for i in range(6))


def k_neg(value):
    return tuple((-coefficient) % PRIME for coefficient in value)


def k_scale(value, scalar):
    return tuple(coefficient * scalar % PRIME for coefficient in value)


def k_mul(left, right):
    product = [0] * 11
    for i, x_value in enumerate(left):
        for j, y_value in enumerate(right):
            product[i + j] = (product[i + j] + x_value * y_value) % PRIME
    for degree in range(10, 5, -1):
        leading = product[degree] % PRIME
        for offset, coefficient in enumerate((-1, -2, -7, 4, -7, -2)):
            product[degree - 6 + offset] = (
                product[degree - 6 + offset] + leading * coefficient
            ) % PRIME
    return tuple(value % PRIME for value in product[:6])


M_SYMBOL = sp.symbols("M")
P6_POLY = sp.Poly(
    M_SYMBOL**6 + 2*M_SYMBOL**5 + 7*M_SYMBOL**4 - 4*M_SYMBOL**3
    + 7*M_SYMBOL**2 + 2*M_SYMBOL + 1,
    M_SYMBOL,
    modulus=PRIME,
)


def expression_to_k(expression):
    polynomial = sp.Poly(expression, M_SYMBOL, modulus=PRIME)
    output = [0] * 6
    for (degree,), coefficient in polynomial.terms():
        output[degree] = int(coefficient) % PRIME
    return tuple(output)


def k_to_poly(value):
    return sp.Poly(
        sum(value[index] * M_SYMBOL**index for index in range(6)),
        M_SYMBOL,
        modulus=PRIME,
    )


def k_inverse(value):
    return expression_to_k(sp.invert(k_to_poly(value), P6_POLY).as_expr())


def k_is_unit(value):
    return sp.gcd(k_to_poly(value), P6_POLY).degree() == 0


class BaseElement:
    """u+v*b in F_p[M,b]/(P_6,4b^2+epsilon*A*b+4)."""

    __slots__ = ("u", "v", "q_coefficient")

    def __init__(self, u_value, v_value, q_coefficient):
        self.u = u_value
        self.v = v_value
        self.q_coefficient = q_coefficient  # b^2=q_coefficient*b-1

    def __add__(self, other):
        other = lift(other, self.q_coefficient)
        return BaseElement(
            k_add(self.u, other.u), k_add(self.v, other.v), self.q_coefficient
        )

    __radd__ = __add__

    def __neg__(self):
        return BaseElement(k_neg(self.u), k_neg(self.v), self.q_coefficient)

    def __sub__(self, other):
        return self + (-lift(other, self.q_coefficient))

    def __rsub__(self, other):
        return lift(other, self.q_coefficient) - self

    def __mul__(self, other):
        other = lift(other, self.q_coefficient)
        return BaseElement(
            k_add(k_mul(self.u, other.u), k_neg(k_mul(self.v, other.v))),
            k_add(
                k_add(k_mul(self.u, other.v), k_mul(self.v, other.u)),
                k_mul(self.q_coefficient, k_mul(self.v, other.v)),
            ),
            self.q_coefficient,
        )

    __rmul__ = __mul__

    def __pow__(self, exponent):
        result = lift(1, self.q_coefficient)
        factor = self
        while exponent:
            if exponent & 1:
                result = result * factor
            factor = factor * factor
            exponent //= 2
        return result

    def norm(self):
        return k_add(
            k_add(
                k_mul(self.u, self.u),
                k_mul(self.q_coefficient, k_mul(self.u, self.v)),
            ),
            k_mul(self.v, self.v),
        )

    def inverse(self):
        norm_inverse = k_inverse(self.norm())
        return BaseElement(
            k_mul(k_add(self.u, k_mul(self.q_coefficient, self.v)), norm_inverse),
            k_mul(k_neg(self.v), norm_inverse),
            self.q_coefficient,
        )

    def __truediv__(self, other):
        return self * lift(other, self.q_coefficient).inverse()

    def __rtruediv__(self, other):
        return lift(other, self.q_coefficient) * self.inverse()

    def is_unit(self):
        return k_is_unit(self.norm())

    def is_zero(self):
        return self.u == ZERO and self.v == ZERO

    def is_unit_by_matrix(self):
        basis = []
        for side in range(2):
            for degree in range(6):
                coefficient = [0] * 6
                coefficient[degree] = 1
                basis.append(BaseElement(
                    tuple(coefficient) if side == 0 else ZERO,
                    ZERO if side == 0 else tuple(coefficient),
                    self.q_coefficient,
                ))
        columns = []
        for vector in basis:
            product = self * vector
            columns.append((*product.u, *product.v))
        matrix = [[columns[column][row] % PRIME for column in range(12)]
                  for row in range(12)]
        rank = 0
        for column in range(12):
            pivot = next(
                (row for row in range(rank, 12) if matrix[row][column]), None
            )
            if pivot is None:
                continue
            matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
            inverse = pow(matrix[rank][column], -1, PRIME)
            matrix[rank] = [value * inverse % PRIME for value in matrix[rank]]
            for row in range(12):
                if row == rank or not matrix[row][column]:
                    continue
                scalar = matrix[row][column]
                matrix[row] = [
                    (matrix[row][index] - scalar * matrix[rank][index]) % PRIME
                    for index in range(12)
                ]
            rank += 1
        return rank == 12


def lift(value, q_coefficient):
    if isinstance(value, BaseElement):
        return value
    if isinstance(value, tuple):
        return BaseElement(value, ZERO, q_coefficient)
    return BaseElement(k_const(int(value)), ZERO, q_coefficient)


def base_data(epsilon, unit_check="norm"):
    locator_a = expression_to_k(
        2*M_SYMBOL**5 + 3*M_SYMBOL**4 + 12*M_SYMBOL**3
        - 14*M_SYMBOL**2 + 18*M_SYMBOL + 3
    )
    locator_d = expression_to_k(
        2*M_SYMBOL**5 + 5*M_SYMBOL**4 + 16*M_SYMBOL**3
        - 2*M_SYMBOL**2 + 6*M_SYMBOL + 5
    )
    locator_e = k_add(locator_a, k_const(-8))
    q_coefficient = k_scale(locator_a, -epsilon * INV4 % PRIME)
    b_value = BaseElement(ZERO, ONE, q_coefficient)
    m_value = BaseElement((0, 1, 0, 0, 0, 0), ZERO, q_coefficient)
    c_value = -(
        b_value * BaseElement(locator_d, ZERO, q_coefficient)
        + epsilon * BaseElement(locator_e, ZERO, q_coefficient)
    ) * INV8
    numerator = epsilon * b_value * (
        b_value * (m_value - 1)**2 - epsilon * (m_value + 1)**2
    )
    denominator = b_value * (m_value + 1)**2 - epsilon * (m_value - 1)**2
    forced = numerator / denominator
    gamma = 2*b_value + epsilon*(b_value*c_value + 1)
    alpha = b_value*(b_value*c_value - 1)
    beta = epsilon*b_value**2*(b_value*c_value + 2*epsilon*c_value + 1)
    for name, value in (
        ("b", b_value), ("c", c_value), ("p", forced),
        ("Gamma", gamma), ("Alpha", alpha), ("Beta", beta),
    ):
        is_unit = (
            value.is_unit() if unit_check == "norm" else value.is_unit_by_matrix()
        )
        if not is_unit:
            raise RuntimeError(f"nonunit protected base value {epsilon}/{name}")
    return b_value, c_value, forced, gamma, alpha, beta


def matchings(items):
    if not items:
        yield ()
        return
    first = items[0]
    for index in range(1, len(items)):
        for tail in matchings(items[1:index] + items[index + 1:]):
            yield ((first, items[index]),) + tail


MATCHINGS = tuple(matchings(tuple(range(6))))
A_VAR, X_VAR, Q_VAR = sp.symbols("a x q")
K_VAR, H_VAR, P_VAR = sp.symbols("k h p")
G_VAR, ALPHA_VAR, BETA_VAR = sp.symbols("Gamma Alpha Beta")


TYPE_DATA = {
    "bD": (
        (A_VAR, K_VAR*A_VAR, X_VAR, -X_VAR,
         H_VAR*A_VAR*X_VAR, -H_VAR*A_VAR*X_VAR),
        X_VAR,
        (K_VAR, H_VAR, G_VAR, ALPHA_VAR, BETA_VAR),
    ),
    "cE": (
        (A_VAR, K_VAR*A_VAR, X_VAR, -X_VAR,
         H_VAR*X_VAR/A_VAR, -H_VAR*X_VAR/A_VAR),
        X_VAR,
        (K_VAR, H_VAR, G_VAR, ALPHA_VAR, BETA_VAR),
    ),
    "DE": (
        (A_VAR, K_VAR/A_VAR, X_VAR, -X_VAR,
         H_VAR*X_VAR/A_VAR**2, -H_VAR*X_VAR/A_VAR**2),
        X_VAR,
        (K_VAR, H_VAR, G_VAR, ALPHA_VAR, BETA_VAR),
    ),
    "DF": (
        (A_VAR, Q_VAR, K_VAR*A_VAR*Q_VAR, -P_VAR,
         H_VAR*Q_VAR/A_VAR, -H_VAR*Q_VAR/A_VAR),
        Q_VAR,
        (K_VAR, H_VAR, P_VAR, G_VAR, ALPHA_VAR, BETA_VAR),
    ),
    "EF": (
        (A_VAR, Q_VAR, K_VAR*A_VAR*Q_VAR,
         H_VAR*A_VAR/Q_VAR, -H_VAR*A_VAR/Q_VAR, -P_VAR),
        Q_VAR,
        (K_VAR, H_VAR, P_VAR, G_VAR, ALPHA_VAR, BETA_VAR),
    ),
}


def obstruction_polynomial(kind, matching_index, shared_index):
    values, first_variable, parameters = TYPE_DATA[kind]
    equations = []
    for left, right in MATCHINGS[matching_index]:
        y_value, z_value = values[left], values[right]
        equation = (
            G_VAR*y_value*z_value
            - ALPHA_VAR*(y_value + z_value)
            - BETA_VAR
        )
        equations.append(sp.together(equation).as_numer_denom()[0])
    other = [index for index in range(3) if index != shared_index]
    first = sp.resultant(
        equations[shared_index], equations[other[0]], first_variable
    )
    second = sp.resultant(
        equations[shared_index], equations[other[1]], first_variable
    )
    obstruction = sp.resultant(first, second, A_VAR)
    if obstruction == 0:
        return None
    return sp.Poly(obstruction, *parameters)


def evaluate(polynomial, values):
    terms = polynomial.terms()
    powers = []
    for position, value in enumerate(values):
        maximum = max(monomial[position] for monomial, _ in terms)
        powers.append([value**exponent for exponent in range(maximum + 1)])
    output = lift(0, values[0].q_coefficient)
    for monomial, coefficient in terms:
        term = lift(int(coefficient), values[0].q_coefficient)
        for position, exponent in enumerate(monomial):
            term = term * powers[position][exponent]
        output = output + term
    return output


def parameter_values(kind, tau, b_value, c_value, forced, gamma, alpha, beta):
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--preferred-chain", type=int, choices=(0, 1), default=0)
    parser.add_argument("--kind", choices=tuple(TYPE_DATA))
    parser.add_argument("--matching", type=int, choices=tuple(range(15)))
    parser.add_argument("--unit-check", choices=("norm", "matrix"), default="norm")
    arguments = parser.parse_args()
    selected_kinds = (arguments.kind,) if arguments.kind else tuple(TYPE_DATA)
    selected_matchings = (
        (arguments.matching,) if arguments.matching is not None else tuple(range(15))
    )
    compiled = {}
    chain_counts = {0: 0, 1: 0, 2: 0}
    for kind in selected_kinds:
        for index in selected_matchings:
            order = (arguments.preferred_chain, 1 - arguments.preferred_chain, 2)
            polynomial = None
            for shared_index in order:
                polynomial = obstruction_polynomial(kind, index, shared_index)
                if polynomial is not None:
                    chain_counts[shared_index] += 1
                    break
            compiled[(kind, index)] = polynomial

    unit_count = 0
    failures = []
    for epsilon in (-1, 1):
        data = base_data(epsilon, arguments.unit_check)
        for tau in (-1, 1):
            for kind in selected_kinds:
                values = parameter_values(kind, tau, *data)
                for index in selected_matchings:
                    polynomial = compiled[(kind, index)]
                    if polynomial is None:
                        status = "NO_PROJECTION"
                    else:
                        result = evaluate(polynomial, values)
                        is_unit = (
                            result.is_unit() if arguments.unit_check == "norm"
                            else result.is_unit_by_matrix()
                        )
                        status = "UNIT" if is_unit else (
                            "ZERO" if result.is_zero() else "ZERO_DIVISOR"
                        )
                    if status == "UNIT":
                        unit_count += 1
                    else:
                        failures.append((epsilon, tau, kind, index, status))
                        print(
                            f"FAIL epsilon={epsilon} tau={tau} kind={kind} "
                            f"matching={index} status={status}",
                            flush=True,
                        )
    if failures:
        raise RuntimeError(f"nonunit matching obstructions: {failures}")
    print(
        "KB_433_PAIRING_QUOTIENT_PASS "
        f"preferred_chain={arguments.preferred_chain} kinds={','.join(selected_kinds)} "
        f"matchings={','.join(map(str, selected_matchings))} units={unit_count} "
        f"unit_check={arguments.unit_check} "
        f"chain0={chain_counts[0]} chain1={chain_counts[1]} "
        f"chain2={chain_counts[2]}"
    )


if __name__ == "__main__":
    main()
