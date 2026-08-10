#!/usr/bin/env python3
"""Finite quotient-algebra core for repeated-BC cell-11 common curves."""

import itertools
import re


PRIME = 2130706433
IOTA = 16711679


def compact_polynomials(output):
    return [
        line.rstrip(",") for line in output.splitlines()[2:] if line.strip()
    ]


def parse_compact(text, variables):
    """Return monomial exponent tuples to integer coefficients."""
    terms = {}
    variable_pattern = "[" + re.escape(variables) + "]"
    tail_pattern = f"(?:{variable_pattern}\\d*)*"
    for raw in re.findall(r"[+-]?[^+-]+", text):
        match = re.fullmatch(rf"([+-]?)(\d*)({tail_pattern})", raw)
        if not match:
            raise ValueError(f"unsupported compact monomial: {raw}")
        sign, coefficient, monomial = match.groups()
        scalar = int(coefficient) if coefficient else 1
        if sign == "-":
            scalar = -scalar
        exponents = {variable: 0 for variable in variables}
        for variable, exponent in re.findall(
            rf"({variable_pattern})(\d*)", monomial
        ):
            exponents[variable] = int(exponent or 1)
        key = tuple(exponents[variable] for variable in variables)
        terms[key] = terms.get(key, 0) + scalar
    return {key: value for key, value in terms.items() if value}


def determinant_no_division(matrix):
    size = len(matrix)
    output = matrix[0][0].context.zero()
    for permutation in itertools.permutations(range(size)):
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(size) for right in range(left + 1, size)
        )
        term = matrix[0][0].context.constant(-1 if inversions % 2 else 1)
        for row, column in enumerate(permutation):
            term = term * matrix[row][column]
        output = output + term
    return output


class FunctionFieldContext:
    """A=F_p(x)[r,y]/(plane(y), quadratic(r,y))."""

    def __init__(self, tower_row):
        from flint import fmpz_mod_poly_ctx

        self.row = tower_row
        self.polynomial_context = fmpz_mod_poly_ctx(PRIME)
        self.x_polynomial = self.polynomial_context([0, 1])
        self.guards = []
        tower = compact_polynomials(tower_row["tower_output"])
        lift = compact_polynomials(tower_row["ordered_lift_output"])
        if len(tower) != 4 or len(lift) != 5:
            raise ValueError("tower/lift basis census")
        self.tower_polynomials = tower
        self.lift_polynomial = lift[-1]
        self.y_degree = 3 if tower_row["bc_sign"] == -1 else 2
        self.dimension = 2 * self.y_degree

        plane = parse_compact(tower[0], "ryx")
        if any(key[0] for key in plane):
            raise ValueError("plane depends on r")
        plane_by_y = {}
        for (_, y_degree, x_degree), coefficient in plane.items():
            plane_by_y[y_degree] = plane_by_y.get(
                y_degree, self._rf_zero()
            ) + self.rf_monomial(coefficient, x_degree)
        lead = plane_by_y[self.y_degree]
        self.y_relation = [
            -plane_by_y.get(index, self._rf_zero()) / lead
            for index in range(self.y_degree)
        ]

        quadratic = parse_compact(tower[1], "ryx")
        r2_coefficients = {}
        for (r_degree, y_degree, x_degree), coefficient in quadratic.items():
            if r_degree != 2:
                continue
            r2_coefficients[y_degree] = r2_coefficients.get(
                y_degree, self._rf_zero()
            ) + self.rf_monomial(coefficient, x_degree)
        if set(r2_coefficients) != {0}:
            raise ValueError("quadratic leading coefficient is not in F_p(x)")
        lead = r2_coefficients[0]
        linear = [self._rf_zero() for _ in range(self.y_degree)]
        constant = [self._rf_zero() for _ in range(self.y_degree)]
        for (r_degree, y_degree, x_degree), coefficient in quadratic.items():
            if r_degree == 2:
                continue
            target = linear if r_degree == 1 else constant
            target[y_degree] = target[y_degree] + self.rf_monomial(
                coefficient, x_degree
            )
        self.r_linear = [-value / lead for value in linear]
        self.r_constant = [-value / lead for value in constant]

        self._zero = AlgebraElement(self, [self._rf_zero()] * self.dimension)
        values = [self._rf_zero()] * self.dimension
        values[0] = self._rf_one()
        self._one = AlgebraElement(self, values)
        values = [self._rf_zero()] * self.dimension
        values[self.y_degree] = self._rf_one()
        self.r = AlgebraElement(self, values)
        values = [self._rf_zero()] * self.dimension
        values[1] = self._rf_one()
        self.y = AlgebraElement(self, values)
        self.x = self.constant(RationalFunction(self, self.x_polynomial))
        self.b = self._recover_b()
        self.c = self.y - self.b

    def _rf_zero(self):
        return RationalFunction(self, 0)

    def _rf_one(self):
        return RationalFunction(self, 1)

    def rf_monomial(self, coefficient, degree):
        values = [0] * (degree + 1)
        values[degree] = coefficient
        return RationalFunction(self, self.polynomial_context(values))

    def register_guard(self, polynomial):
        if polynomial.is_zero():
            raise ZeroDivisionError("zero function-field guard")
        leading = int(polynomial[polynomial.degree()]) % PRIME
        normalized = polynomial * pow(leading, -1, PRIME)
        self.guards.append(normalized)

    def zero(self):
        return self._zero

    def one(self):
        return self._one

    def constant(self, value):
        value = RationalFunction.coerce(self, value)
        values = [self._rf_zero()] * self.dimension
        values[0] = value
        return AlgebraElement(self, values)

    def basis(self):
        output = []
        for index in range(self.dimension):
            values = [self._rf_zero()] * self.dimension
            values[index] = self._rf_one()
            output.append(AlgebraElement(self, values))
        return tuple(output)

    def reduce_y(self, terms):
        terms = dict(terms)
        maximum = max((degree for _, degree in terms), default=-1)
        for y_degree in range(maximum, self.y_degree - 1, -1):
            for r_degree in (0, 1):
                coefficient = terms.pop((r_degree, y_degree), self._rf_zero())
                if coefficient.is_zero():
                    continue
                shift = y_degree - self.y_degree
                for relation_degree, relation_value in enumerate(self.y_relation):
                    key = (r_degree, shift + relation_degree)
                    terms[key] = terms.get(key, self._rf_zero()) + coefficient * relation_value
        values = [self._rf_zero()] * self.dimension
        for (r_degree, y_degree), coefficient in terms.items():
            if not coefficient.is_zero():
                values[r_degree * self.y_degree + y_degree] = coefficient
        return AlgebraElement(self, values)

    def multiply(self, left, right):
        terms = {}
        for left_index, left_value in enumerate(left.values):
            if left_value.is_zero():
                continue
            left_r, left_y = divmod(left_index, self.y_degree)
            for right_index, right_value in enumerate(right.values):
                if right_value.is_zero():
                    continue
                right_r, right_y = divmod(right_index, self.y_degree)
                coefficient = left_value * right_value
                r_degree, y_degree = left_r + right_r, left_y + right_y
                if r_degree < 2:
                    key = (r_degree, y_degree)
                    terms[key] = terms.get(key, self._rf_zero()) + coefficient
                    continue
                for degree, relation_value in enumerate(self.r_linear):
                    key = (1, y_degree + degree)
                    terms[key] = terms.get(key, self._rf_zero()) + coefficient * relation_value
                for degree, relation_value in enumerate(self.r_constant):
                    key = (0, y_degree + degree)
                    terms[key] = terms.get(key, self._rf_zero()) + coefficient * relation_value
        return self.reduce_y(terms)

    def evaluate_compact(self, text, variables="ryx", substitutions=None):
        substitutions = substitutions or {}
        parsed = parse_compact(text, variables)
        output = self.zero()
        defaults = {"r": self.r, "y": self.y, "x": self.x}
        defaults.update(substitutions)
        for exponents, coefficient in parsed.items():
            term = self.constant(coefficient)
            for variable, exponent in zip(variables, exponents):
                term = term * defaults[variable] ** exponent
            output = output + term
        return output

    def _recover_b(self):
        parsed = parse_compact(self.lift_polynomial, "bryx")
        b_coefficient = parsed.pop((1, 0, 0, 0), None)
        if b_coefficient != 1 or any(key[0] for key in parsed):
            raise ValueError("ordered lift is not monic linear in b")
        output = self.zero()
        for (_, r_degree, y_degree, x_degree), coefficient in parsed.items():
            output = output + self.constant(coefficient) * self.r**r_degree * self.y**y_degree * self.x**x_degree
        return -output

    def validate_tower(self):
        checks = [self.evaluate_compact(value) for value in self.tower_polynomials]
        checks.append(self.evaluate_compact(
            self.lift_polynomial, "bryx", {"b": self.b}
        ))
        checks.extend((self.b + self.c - self.y, self.b * self.c - self.x))
        return tuple(value.is_zero() for value in checks)


class RationalFunction:
    __slots__ = ("context", "numer", "denom")

    def __init__(self, context, numer=0, denom=1):
        self.context = context
        polynomial_context = context.polynomial_context
        if isinstance(numer, RationalFunction):
            if denom != 1 or numer.context is not context:
                raise TypeError("incompatible rational function")
            self.numer, self.denom = numer.numer, numer.denom
            return
        numer = numer if hasattr(numer, "degree") else polynomial_context([numer])
        denom = denom if hasattr(denom, "degree") else polynomial_context([denom])
        if denom.is_zero():
            raise ZeroDivisionError("zero rational denominator")
        if numer.is_zero():
            self.numer, self.denom = polynomial_context.zero(), polynomial_context.one()
            return
        common = numer.gcd(denom)
        numer, denom = numer // common, denom // common
        scale = pow(int(denom[denom.degree()]), -1, PRIME)
        self.numer, self.denom = numer * scale, denom * scale

    @staticmethod
    def coerce(context, value):
        if isinstance(value, RationalFunction):
            if value.context is not context:
                raise TypeError("context mismatch")
            return value
        return RationalFunction(context, value)

    def __add__(self, other):
        other = self.coerce(self.context, other)
        common = self.denom.gcd(other.denom)
        left, right = self.denom // common, other.denom // common
        return RationalFunction(
            self.context, self.numer * right + other.numer * left,
            left * other.denom,
        )

    __radd__ = __add__

    def __neg__(self):
        return RationalFunction(self.context, -self.numer, self.denom)

    def __sub__(self, other):
        return self + (-self.coerce(self.context, other))

    def __rsub__(self, other):
        return self.coerce(self.context, other) - self

    def __mul__(self, other):
        other = self.coerce(self.context, other)
        left_common = self.numer.gcd(other.denom)
        right_common = other.numer.gcd(self.denom)
        return RationalFunction(
            self.context,
            (self.numer // left_common) * (other.numer // right_common),
            (self.denom // right_common) * (other.denom // left_common),
        )

    __rmul__ = __mul__

    def inverse(self):
        self.context.register_guard(self.numer)
        return RationalFunction(self.context, self.denom, self.numer)

    def __truediv__(self, other):
        return self * self.coerce(self.context, other).inverse()

    def __rtruediv__(self, other):
        return self.coerce(self.context, other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        output, base = RationalFunction(self.context, 1), self
        while exponent:
            if exponent & 1:
                output = output * base
            base = base * base
            exponent //= 2
        return output

    def is_zero(self):
        return self.numer.is_zero()

    def __eq__(self, other):
        other = self.coerce(self.context, other)
        return self.numer == other.numer and self.denom == other.denom


class AlgebraElement:
    __slots__ = ("context", "values")

    def __init__(self, context, values):
        self.context = context
        self.values = tuple(values)

    @staticmethod
    def coerce(context, value):
        if isinstance(value, AlgebraElement):
            if value.context is not context:
                raise TypeError("context mismatch")
            return value
        return context.constant(value)

    def __add__(self, other):
        other = self.coerce(self.context, other)
        return AlgebraElement(self.context, [
            left + right for left, right in zip(self.values, other.values)
        ])

    __radd__ = __add__

    def __neg__(self):
        return AlgebraElement(self.context, [-value for value in self.values])

    def __sub__(self, other):
        return self + (-self.coerce(self.context, other))

    def __rsub__(self, other):
        return self.coerce(self.context, other) - self

    def __mul__(self, other):
        return self.context.multiply(self, self.coerce(self.context, other))

    __rmul__ = __mul__

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        output, base = self.context.one(), self
        while exponent:
            if exponent & 1:
                output = output * base
            base = base * base
            exponent //= 2
        return output

    def multiplication_matrix(self):
        columns = [(self * basis).values for basis in self.context.basis()]
        return [
            [columns[column][row] for column in range(self.context.dimension)]
            for row in range(self.context.dimension)
        ]

    def inverse(self):
        matrix = self.multiplication_matrix()
        size = self.context.dimension
        work = [
            row[:] + [self.context._rf_one() if index == 0 else self.context._rf_zero()]
            for index, row in enumerate(matrix)
        ]
        for column in range(size):
            pivot = next((row for row in range(column, size)
                          if not work[row][column].is_zero()), None)
            if pivot is None:
                raise ZeroDivisionError("nonunit algebra element")
            work[column], work[pivot] = work[pivot], work[column]
            inverse = work[column][column].inverse()
            work[column] = [value * inverse for value in work[column]]
            for row in range(size):
                if row == column:
                    continue
                scalar = work[row][column]
                if scalar.is_zero():
                    continue
                work[row] = [
                    left - scalar * right
                    for left, right in zip(work[row], work[column])
                ]
        return AlgebraElement(self.context, [row[-1] for row in work])

    def __truediv__(self, other):
        return self * self.coerce(self.context, other).inverse()

    def __rtruediv__(self, other):
        return self.coerce(self.context, other) / self

    def is_zero(self):
        return all(value.is_zero() for value in self.values)

    def __eq__(self, other):
        other = self.coerce(self.context, other)
        return self.values == other.values


def cell11_common_data(context, epsilon_1, epsilon_2, bc_sign):
    r = context.r
    t = epsilon_1 * epsilon_2 * r**2
    b, c = context.b, context.c
    roots = (
        context.one(), r, epsilon_2 * IOTA * r, t,
        context.constant(epsilon_1 * IOTA),
    )
    labels = tuple(root**2 for root in roots)
    products = (-context.one(), b, c, bc_sign * context.x, bc_sign * context.x)
    sums = (context.zero(), 1 + b, 1 + c,
            b + bc_sign * c, b + bc_sign * c)
    matrix = [
        [-product, -product * label, -product * label**2,
         context.one(), label, label**2]
        for product, label in zip(products, labels)
    ]
    cofactors = []
    for column in range(6):
        minor = [row[:column] + row[column + 1:] for row in matrix]
        cofactors.append(((-1) ** column) * determinant_no_division(minor))
    a_values, b_values = tuple(cofactors[:3]), tuple(cofactors[3:])

    def evaluate(coefficients, value):
        return sum(
            (coefficient * value**index for index, coefficient in enumerate(coefficients)),
            context.zero(),
        )

    pivot_label = labels[1]
    pivot_q = roots[1] * sums[1]
    beta_0 = -pivot_q * evaluate(a_values, pivot_label) / (
        pivot_label * (1 - pivot_label)
    )
    beta_1 = -beta_0
    q_values = tuple(root * edge_sum for root, edge_sum in zip(roots, sums))
    product_checks = tuple(
        sum((coefficient * value for coefficient, value in zip(row, cofactors)), context.zero())
        for row in matrix
    )
    sum_checks = tuple(
        q_value * evaluate(a_values, label)
        + label * (beta_0 + beta_1 * label)
        for q_value, label in zip(q_values, labels)
    )
    missing_label = -t**2
    a_missing = evaluate(a_values, missing_label)
    b_missing = evaluate(b_values, missing_label)
    beta_missing = beta_0 + beta_1 * missing_label
    missing_product = b_missing / a_missing
    missing_sum_squared = (
        missing_label * beta_missing**2 / a_missing**2
    )
    return {
        "roots": roots, "labels": labels, "products": products,
        "sums": sums, "a_values": a_values, "b_values": b_values,
        "beta": (beta_0, beta_1), "product_checks": product_checks,
        "sum_checks": sum_checks, "missing_label": missing_label,
        "missing_product": missing_product,
        "missing_sum_squared": missing_sum_squared,
    }
