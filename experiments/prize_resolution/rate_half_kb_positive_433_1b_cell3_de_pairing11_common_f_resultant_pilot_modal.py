#!/usr/bin/env python3
"""Pilot the cell-3 DE-missing pairing-11 common-f resultant cut."""

import hashlib
import json
from pathlib import Path
import time

import modal


DIRECTORY = Path(__file__).parent
QUOTIENT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_birational_profile_result.json"
KERNEL = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_compact_kernel_result.json"
PRODUCT = DIRECTORY / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_de_pairing11_common_f_resultant_pilot_result.json"
CENSUS_RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_de_pairing11_common_f_resultant_census_result.json"
REMOTE_QUOTIENT = "/root/quotient.json"
REMOTE_KERNEL = "/root/kernel.json"
REMOTE_PRODUCT = "/root/product.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell3-de-pairing11-common-f-resultant-pilot")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0", "python-flint==0.8.0")
    .add_local_file(QUOTIENT, REMOTE_QUOTIENT)
    .add_local_file(KERNEL, REMOTE_KERNEL)
    .add_local_file(PRODUCT, REMOTE_PRODUCT)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=300, max_containers=16)
def profile_case(case):
    import sympy as sp
    from flint import fmpz_mod_poly_ctx

    started = time.perf_counter()
    epsilon_1, epsilon_2, sigma_c, sigma_o, xi_index, pairing_index = case
    if xi_index not in (0, 2) or pairing_index != 11:
        raise ValueError("the pilot is scoped to xi in {0,2}, pairing=11")
    quotient_payload = json.loads(Path(REMOTE_QUOTIENT).read_text())
    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    product_payload = json.loads(Path(REMOTE_PRODUCT).read_text())
    source = next(
        row for row in quotient_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2] and row["chart"] == 0
    )
    kernel_row = next(
        row for row in kernel_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    )
    product_row = next(
        row for row in product_payload["rows"] if row["cell"] == 3
    )
    interface = source["quotient_interface"]
    r, t, b, c = sp.symbols("r t b c")
    polynomial_context = fmpz_mod_poly_ctx(PRIME)
    polynomial_type = type(polynomial_context.zero())

    class RationalFunction:
        """Reduced fractions in F_p(r), backed entirely by FLINT."""

        __slots__ = ("numer", "denom")

        def __init__(self, numer=0, denom=1):
            if isinstance(numer, RationalFunction):
                if denom != 1:
                    raise TypeError("cannot supply a second denominator")
                self.numer = numer.numer
                self.denom = numer.denom
                return
            numer = (
                numer if isinstance(numer, polynomial_type)
                else polynomial_context([int(numer) % PRIME])
            )
            denom = (
                denom if isinstance(denom, polynomial_type)
                else polynomial_context([int(denom) % PRIME])
            )
            if denom.is_zero():
                raise ZeroDivisionError("zero rational-function denominator")
            if numer.is_zero():
                self.numer = polynomial_context.zero()
                self.denom = polynomial_context.one()
                return
            common = numer.gcd(denom)
            if common.degree() >= 0:
                numer = numer // common
                denom = denom // common
            leading = int(denom[denom.degree()])
            scale = pow(leading, -1, PRIME)
            self.numer = numer * scale
            self.denom = denom * scale

        @staticmethod
        def coerce(value):
            if isinstance(value, RationalFunction):
                return value
            if isinstance(value, (int, polynomial_type)):
                return RationalFunction(value)
            return NotImplemented

        def __add__(self, other):
            other = RationalFunction.coerce(other)
            if other is NotImplemented:
                return NotImplemented
            common = self.denom.gcd(other.denom)
            left_denominator = self.denom // common
            right_denominator = other.denom // common
            return RationalFunction(
                self.numer * right_denominator
                + other.numer * left_denominator,
                left_denominator * other.denom,
            )

        __radd__ = __add__

        def __neg__(self):
            return RationalFunction(-self.numer, self.denom)

        def __sub__(self, other):
            other = RationalFunction.coerce(other)
            if other is NotImplemented:
                return NotImplemented
            return self + (-other)

        def __rsub__(self, other):
            other = RationalFunction.coerce(other)
            if other is NotImplemented:
                return NotImplemented
            return other - self

        def __mul__(self, other):
            other = RationalFunction.coerce(other)
            if other is NotImplemented:
                return NotImplemented
            left_common = self.numer.gcd(other.denom)
            right_common = other.numer.gcd(self.denom)
            return RationalFunction(
                (self.numer // left_common) * (other.numer // right_common),
                (self.denom // right_common) * (other.denom // left_common),
            )

        __rmul__ = __mul__

        def inverse(self):
            if self.numer.is_zero():
                raise ZeroDivisionError("inverse of zero rational function")
            return RationalFunction(self.denom, self.numer)

        def __truediv__(self, other):
            other = RationalFunction.coerce(other)
            if other is NotImplemented:
                return NotImplemented
            return self * other.inverse()

        def __rtruediv__(self, other):
            other = RationalFunction.coerce(other)
            if other is NotImplemented:
                return NotImplemented
            return other / self

        def __pow__(self, exponent):
            if exponent < 0:
                return self.inverse() ** (-exponent)
            return RationalFunction(
                self.numer ** exponent, self.denom ** exponent
            )

        def __eq__(self, other):
            other = RationalFunction.coerce(other)
            if other is NotImplemented:
                return False
            return self.numer == other.numer and self.denom == other.denom

        def __repr__(self):
            return f"({self.numer})/({self.denom})"

    class RationalFunctionField:
        zero = RationalFunction(0)
        one = RationalFunction(1)

        @staticmethod
        def convert(value):
            converted = RationalFunction.coerce(value)
            if converted is NotImplemented:
                raise TypeError(f"cannot coerce {type(value).__name__}")
            return converted

    base_field = RationalFunctionField()
    zero = base_field.zero
    one = base_field.one
    inverse_guards = []

    def field_equal(left, right):
        return base_field.convert(left) == base_field.convert(right)

    def field_is_zero(value):
        return base_field.convert(value).numer.is_zero()

    def flint_polynomial(polynomial):
        coefficients = {
            exponents[0]: int(coefficient) % PRIME
            for exponents, coefficient in polynomial.terms()
        }
        maximum = max(coefficients, default=0)
        return polynomial_context([
            coefficients.get(exponent, 0) for exponent in range(maximum+1)
        ])

    def field_value(expression):
        polynomial = sp.Poly(expression, r, modulus=PRIME)
        return RationalFunction(flint_polynomial(polynomial))

    base_expression = sp.sympify(interface["base_relation"]["expression"])
    base_in_t = sp.Poly(base_expression, t)
    base_coefficients = [field_value(value) for value in base_in_t.all_coeffs()]
    if len(base_coefficients) != 4:
        raise ValueError("base relation is not cubic in t")
    base_leading, base_t2, base_t1, base_t0 = base_coefficients
    cubic_relation = (
        -base_t0/base_leading,
        -base_t1/base_leading,
        -base_t2/base_leading,
    )

    def determinant(matrix):
        size = len(matrix)
        work = [list(row) for row in matrix]
        output = one
        for column in range(size):
            pivot = next(
                (row for row in range(column, size)
                 if not field_is_zero(work[row][column])),
                None,
            )
            if pivot is None:
                return zero
            if pivot != column:
                work[column], work[pivot] = work[pivot], work[column]
                output = -output
            pivot_value = work[column][column]
            output = output*pivot_value
            inverse = one/pivot_value
            for index in range(column, size):
                work[column][index] = work[column][index]*inverse
            for row in range(column+1, size):
                scale = work[row][column]
                if field_is_zero(scale):
                    continue
                for index in range(column, size):
                    work[row][index] = (
                        work[row][index]-scale*work[column][index]
                    )
        return output

    def solve(matrix, right):
        size = len(matrix)
        work = [list(matrix[row])+[right[row]] for row in range(size)]
        for column in range(size):
            pivot = next(
                (row for row in range(column, size)
                 if not field_is_zero(work[row][column])),
                None,
            )
            if pivot is None:
                raise ZeroDivisionError("singular cubic multiplication matrix")
            work[column], work[pivot] = work[pivot], work[column]
            inverse = one/work[column][column]
            for index in range(column, size+1):
                work[column][index] = work[column][index]*inverse
            for row in range(size):
                if row == column:
                    continue
                scale = work[row][column]
                if field_is_zero(scale):
                    continue
                for index in range(column, size+1):
                    work[row][index] = (
                        work[row][index]-scale*work[column][index]
                    )
        return [work[index][-1] for index in range(size)]

    class Cubic:
        __slots__ = ("values",)

        def __init__(self, constant=0, linear=0, quadratic=0):
            self.values = tuple(
                base_field.convert(value)
                for value in (constant, linear, quadratic)
            )

        @staticmethod
        def coerce(value):
            return value if isinstance(value, Cubic) else Cubic(value)

        def __add__(self, other):
            other = Cubic.coerce(other)
            return Cubic(*(left+right for left, right in zip(
                self.values, other.values
            )))

        __radd__ = __add__

        def __neg__(self):
            return Cubic(*(-value for value in self.values))

        def __sub__(self, other):
            return self + (-Cubic.coerce(other))

        def __rsub__(self, other):
            return Cubic.coerce(other) - self

        def __mul__(self, other):
            other = Cubic.coerce(other)
            coefficients = [base_field.zero for _ in range(5)]
            for left_degree, left in enumerate(self.values):
                for right_degree, right in enumerate(other.values):
                    degree = left_degree+right_degree
                    coefficients[degree] = coefficients[degree]+left*right
            for degree in (4, 3):
                value = coefficients[degree]
                if field_is_zero(value):
                    continue
                shift = degree-3
                coefficients[degree] = zero
                for relation_degree, relation_value in enumerate(cubic_relation):
                    target_degree = shift+relation_degree
                    coefficients[target_degree] = (
                        coefficients[target_degree]+value*relation_value
                    )
            return Cubic(*coefficients[:3])

        __rmul__ = __mul__

        def __pow__(self, exponent):
            if exponent < 0:
                return self.inverse() ** (-exponent)
            output = Cubic(1)
            base = self
            power = exponent
            while power:
                if power & 1:
                    output = output*base
                base = base*base
                power //= 2
            return output

        def vector(self):
            return self.values

        def multiplication_matrix(self):
            basis = (Cubic(1), Cubic(0, 1), Cubic(0, 0, 1))
            columns = [(self*value).vector() for value in basis]
            return [[columns[column][row] for column in range(3)]
                    for row in range(3)]

        def norm(self):
            return determinant(self.multiplication_matrix())

        def inverse(self):
            guard = self.norm()
            inverse_guards.append(guard)
            return Cubic(*solve(
                self.multiplication_matrix(), [one, zero, zero]
            ))

        def __truediv__(self, other):
            return self*Cubic.coerce(other).inverse()

        def __eq__(self, other):
            return all(
                field_equal(left, right)
                for left, right in zip(
                    self.values, Cubic.coerce(other).values
                )
            )

    cubic_t = Cubic(0, 1)
    if cubic_t**3 != Cubic(*cubic_relation):
        raise ValueError("cubic multiplication does not satisfy base relation")

    def cubic_expression(expression):
        output = Cubic()
        for (t_degree, r_degree), coefficient in sp.Poly(
            expression, t, r, modulus=PRIME
        ).terms():
            scalar = field_value(int(coefficient)*r**r_degree)
            output += scalar*cubic_t**t_degree
        return output

    b_expression = sp.sympify(interface["b_relation"]["expression"])
    b_in_b = sp.Poly(b_expression, b)
    b_leading, b_linear, b_constant = (
        cubic_expression(value) for value in b_in_b.all_coeffs()
    )
    if b_leading != b_constant:
        raise ValueError("b relation is not palindromic in the cubic algebra")
    b_leading_inverse = b_leading.inverse()
    inverse_check = b_leading*b_leading_inverse
    if inverse_check != Cubic(1):
        raise ValueError(
            "cubic inverse self-check failed: "
            + repr([str(value) for value in inverse_check.values])
        )
    quotient_u = -b_linear*b_leading_inverse
    quotient_v = Cubic(-1)
    print(json.dumps({
        "phase": "quotient_algebra",
        "seconds": time.perf_counter()-started,
    }), flush=True)

    class Pair:
        __slots__ = ("constant", "linear")

        def __init__(self, constant=0, linear=0):
            self.constant = Cubic.coerce(constant)
            self.linear = Cubic.coerce(linear)

        @staticmethod
        def coerce(value):
            return value if isinstance(value, Pair) else Pair(value)

        def __add__(self, other):
            other = Pair.coerce(other)
            return Pair(
                self.constant+other.constant, self.linear+other.linear
            )

        __radd__ = __add__

        def __neg__(self):
            return Pair(-self.constant, -self.linear)

        def __sub__(self, other):
            return self + (-Pair.coerce(other))

        def __rsub__(self, other):
            return Pair.coerce(other)-self

        def __mul__(self, other):
            other = Pair.coerce(other)
            return Pair(
                self.constant*other.constant
                + self.linear*other.linear*quotient_v,
                self.constant*other.linear
                + self.linear*other.constant
                + self.linear*other.linear*quotient_u,
            )

        __rmul__ = __mul__

        def __pow__(self, exponent):
            if exponent < 0:
                return self.inverse() ** (-exponent)
            output = Pair(1)
            base = self
            power = exponent
            while power:
                if power & 1:
                    output = output*base
                base = base*base
                power //= 2
            return output

        def vector(self):
            return (*self.constant.vector(), *self.linear.vector())

        def multiplication_matrix(self):
            cubic_basis = (Cubic(1), Cubic(0, 1), Cubic(0, 0, 1))
            basis = tuple(Pair(value) for value in cubic_basis) + tuple(
                Pair(0, value) for value in cubic_basis
            )
            columns = [(self*value).vector() for value in basis]
            return [[columns[column][row] for column in range(6)]
                    for row in range(6)]

        def norm(self):
            return determinant(self.multiplication_matrix())

        def inverse(self):
            determinant_value = (
                self.constant*(self.constant+self.linear*quotient_u)
                - self.linear*self.linear*quotient_v
            )
            determinant_inverse = determinant_value.inverse()
            return Pair(
                (self.constant+self.linear*quotient_u)*determinant_inverse,
                -self.linear*determinant_inverse,
            )

        def __truediv__(self, other):
            return self*Pair.coerce(other).inverse()

        def __eq__(self, other):
            other = Pair.coerce(other)
            return self.constant == other.constant and self.linear == other.linear

    common_b = Pair(0, 1)

    def pair_expression(expression):
        output = Pair()
        for exponents, coefficient in sp.Poly(
            expression, c, b, t, r, modulus=PRIME
        ).terms():
            c_degree, b_degree, t_degree, r_degree = exponents
            if c_degree:
                raise ValueError("c must be substituted before pair reduction")
            scalar = field_value(int(coefficient)*r**r_degree)
            output += scalar*Pair(cubic_t**t_degree)*common_b**b_degree
        return output

    c_constant_expression = sp.sympify(interface["c_constant"]["expression"])
    c_denominator_expression = sp.sympify(
        interface["c_denominator"]["expression"]
    )
    c_pair = -pair_expression(c_constant_expression)/Pair(
        cubic_expression(c_denominator_expression)
    )

    def kernel_expression(expression):
        output = Pair()
        for exponents, coefficient in sp.Poly(
            expression, c, b, t, r, modulus=PRIME
        ).terms():
            c_degree, b_degree, t_degree, r_degree = exponents
            scalar = field_value(int(coefficient)*r**r_degree)
            output += (
                scalar*Pair(cubic_t**t_degree)
                * c_pair**c_degree * common_b**b_degree
            )
        return output

    algebra_seconds = time.perf_counter()-started
    kernel = [
        kernel_expression(sp.sympify(value["expression"]))
        for value in kernel_row["kernel"]
    ]
    kernel_seconds = time.perf_counter()-started
    print(json.dumps({
        "phase": "kernel_reduction",
        "seconds": kernel_seconds,
    }), flush=True)
    a_coefficients = tuple(kernel[:3])
    b_coefficients = tuple(kernel[3:6])

    def evaluate(coefficients, value):
        return coefficients[0]+coefficients[1]*value+coefficients[2]*value**2

    missing_label = -Pair(cubic_t*cubic_t)
    a_missing = evaluate(a_coefficients, missing_label)
    b_missing = evaluate(b_coefficients, missing_label)
    missing_record = b_missing/a_missing
    beta_0, beta_1 = kernel[6:]

    def paired(left, right):
        p0, p1, p2 = (
            b_value-left*a_value
            for a_value, b_value in zip(a_coefficients, b_coefficients)
        )
        q0 = b_coefficients[0]-right*a_coefficients[0]
        q1 = -b_coefficients[1]+right*a_coefficients[1]
        q2 = b_coefficients[2]-right*a_coefficients[2]
        return (p2*q0-p0*q2)**2-(p2*q1-p1*q2)*(p1*q0-p0*q1)

    class PairPolynomial:
        def __init__(self, *coefficients):
            self.coefficients = tuple(Pair.coerce(value) for value in coefficients)

        @staticmethod
        def coerce(value):
            return value if isinstance(value, PairPolynomial) else PairPolynomial(value)

        def __add__(self, other):
            other = PairPolynomial.coerce(other)
            size = max(len(self.coefficients), len(other.coefficients))
            return PairPolynomial(*(
                (self.coefficients[index]
                 if index < len(self.coefficients) else Pair())
                + (other.coefficients[index]
                   if index < len(other.coefficients) else Pair())
                for index in range(size)
            ))

        __radd__ = __add__

        def __neg__(self):
            return PairPolynomial(*(-value for value in self.coefficients))

        def __sub__(self, other):
            other = PairPolynomial.coerce(other)
            size = max(len(self.coefficients), len(other.coefficients))
            return PairPolynomial(*(
                (self.coefficients[index] if index < len(self.coefficients) else Pair())
                - (other.coefficients[index] if index < len(other.coefficients) else Pair())
                for index in range(size)
            ))

        def __rsub__(self, other):
            return PairPolynomial.coerce(other)-self

        def __mul__(self, other):
            other = PairPolynomial.coerce(other)
            output = [Pair()] * (len(self.coefficients)+len(other.coefficients)-1)
            for left_degree, left in enumerate(self.coefficients):
                for right_degree, right in enumerate(other.coefficients):
                    degree = left_degree+right_degree
                    output[degree] = output[degree]+left*right
            return PairPolynomial(*output)

        __rmul__ = __mul__

        def __pow__(self, exponent):
            output = PairPolynomial(1)
            base = self
            while exponent:
                if exponent & 1:
                    output = output*base
                base = base*base
                exponent //= 2
            return output

        def degree(self):
            for index in range(len(self.coefficients)-1, -1, -1):
                if self.coefficients[index] != Pair():
                    return index
            return -1

        def descending(self):
            degree = self.degree()
            return list(reversed(self.coefficients[:degree+1]))

    def polynomial_remainder(dividend, divisor):
        divisor_degree = divisor.degree()
        if divisor_degree < 0:
            raise ZeroDivisionError("zero polynomial divisor")
        work = list(dividend.coefficients)
        divisor_leading = divisor.coefficients[divisor_degree]
        while True:
            degree = next((index for index in range(len(work)-1, -1, -1)
                           if work[index] != Pair()), -1)
            if degree < divisor_degree:
                return PairPolynomial(*work[:degree+1])
            shift = degree-divisor_degree
            factor = work[degree]/divisor_leading
            for index in range(divisor_degree+1):
                work[shift+index] = (
                    work[shift+index]
                    - factor*divisor.coefficients[index]
                )

    def euclidean_resultant(left, right):
        left_degree = left.degree()
        right_degree = right.degree()
        if left_degree < 0 or right_degree < 0:
            return Pair()
        if right_degree == 0:
            return right.coefficients[0]**left_degree
        if left_degree < right_degree:
            sign = -1 if (left_degree*right_degree) % 2 else 1
            return sign*euclidean_resultant(right, left)
        remainder = polynomial_remainder(left, right)
        remainder_degree = remainder.degree()
        if remainder_degree < 0:
            return Pair()
        sign = -1 if (left_degree*right_degree) % 2 else 1
        return (
            sign
            * right.coefficients[right_degree]**(left_degree-remainder_degree)
            * euclidean_resultant(right, remainder)
        )

    def paired_polynomial(left, right):
        p0, p1, p2 = (
            PairPolynomial(b_value)-left*a_value
            for a_value, b_value in zip(a_coefficients, b_coefficients)
        )
        q0 = PairPolynomial(b_coefficients[0])-right*a_coefficients[0]
        q1 = PairPolynomial(-b_coefficients[1])+right*a_coefficients[1]
        q2 = PairPolynomial(b_coefficients[2])-right*a_coefficients[2]
        return (p2*q0-p0*q2)**2-(p2*q1-p1*q2)*(p1*q0-p0*q1)

    variable_polynomial = PairPolynomial(0, 1)
    de_record = missing_record if xi_index == 0 else -missing_record
    second_de = -de_record if xi_index == 0 else de_record
    p_b = paired_polynomial(
        PairPolynomial(de_record),
        variable_polynomial*common_b,
    )
    p_c = paired_polynomial(
        PairPolynomial(second_de),
        variable_polynomial*sigma_c*c_pair,
    )
    if p_b.degree() != 2 or p_c.degree() != 2:
        raise ValueError("common-f paired cuts are not quadratic")

    eta = 1 if xi_index == 0 else -1
    p_b_c, p_b_b, p_b_a = p_b.coefficients[:3]
    p_c_c, p_c_b, p_c_a = p_c.coefficients[:3]
    target_free = (
        (p_b_a*p_c_c-p_b_c*p_c_a)**2
        - (p_b_a*p_c_b-p_b_b*p_c_a)
        * (p_b_b*p_c_c-p_b_c*p_c_b)
    )
    print(json.dumps({
        "phase": "common_f_resultant_cut",
        "p_b_degree": p_b.degree(),
        "p_c_degree": p_c.degree(),
        "seconds": time.perf_counter()-started,
    }), flush=True)
    cut_seconds = time.perf_counter()-started
    target_free_norm = target_free.norm()
    target_free_pair_determinant = (
        target_free.constant
        * (target_free.constant+target_free.linear*quotient_u)
        - target_free.linear*target_free.linear*quotient_v
    )
    target_free_tower_norm = target_free_pair_determinant.norm()
    if not field_equal(target_free_norm, target_free_tower_norm):
        raise ValueError("six-by-six norm disagrees with the 2-by-3 tower norm")
    norm_seconds = time.perf_counter()-started

    def polynomial_profile(polynomial, include_expression=False):
        coefficients = polynomial.coeffs()
        terms = sum(int(value) != 0 for value in coefficients)
        degree = int(polynomial.degree())
        expression = str(polynomial)
        return {
            "degree": degree,
            "terms": terms,
            "sha256": hashlib.sha256(expression.encode()).hexdigest(),
            "expression": (
                expression if include_expression or terms <= 80 else None
            ),
        }

    def fraction_profile(value):
        return {
            "numerator": polynomial_profile(value.numer),
            "denominator": polynomial_profile(value.denom),
        }

    numerator = target_free_norm.numer
    variable = polynomial_context([0, 1])
    if numerator.is_zero():
        field_gcd = numerator
        roots = None
        factor_degrees = None
    elif int(numerator.degree()) == 0:
        field_gcd = numerator
        roots = []
        factor_degrees = []
    else:
        field_gcd = numerator.gcd(pow(variable, PRIME, numerator)-variable)
        _, factors = field_gcd.factor()
        roots = []
        factor_degrees = []
        for factor, multiplicity in factors:
            factor_degrees.extend([int(factor.degree())]*int(multiplicity))
            if int(factor.degree()) != 1:
                raise ValueError("field-root gcd contains a nonlinear factor")
            roots.append(
                -int(factor[0])*pow(int(factor[1]), -1, PRIME) % PRIME
            )
        roots.sort()

    def evaluate_polynomial(polynomial, point):
        output = 0
        for coefficient in reversed(polynomial.coeffs()):
            output = (output*point+int(coefficient)) % PRIME
        return output

    guard_values = []
    seen_guards = set()
    for index, guard in enumerate(inverse_guards):
        key = (str(guard.numer), str(guard.denom))
        if key in seen_guards:
            continue
        seen_guards.add(key)
        guard_values.append((f"inverse_{index}", guard))
    guard_values.append(("base_cubic_leading", base_leading))
    guard_values.append(("target_free_norm", target_free_norm))
    root_rows = []
    for root in roots or []:
        zero_numerators = []
        zero_denominators = []
        for name, guard in guard_values:
            if evaluate_polynomial(guard.denom, root) == 0:
                zero_denominators.append(name)
            elif evaluate_polynomial(guard.numer, root) == 0:
                zero_numerators.append(name)
        root_rows.append({
            "r": root,
            "zero_guard_numerators": zero_numerators,
            "zero_guard_denominators": zero_denominators,
            "status": (
                "ALGEBRA_EXCEPTIONAL_ROOT" if
                zero_denominators or any(
                    name != "target_free_norm" for name in zero_numerators
                ) else "LIVE_NORM_ROOT"
            ),
        })

    def compile_terms(expression, variables):
        return [
            (exponents, int(coefficient) % PRIME)
            for exponents, coefficient in sp.Poly(
                sp.sympify(expression), *variables, modulus=PRIME
            ).terms()
        ]

    def evaluate_terms(compiled, values):
        output = 0
        for exponents, coefficient in compiled:
            term = coefficient
            for value, exponent in zip(values, exponents):
                term = term*pow(value, exponent, PRIME) % PRIME
            output = (output+term) % PRIME
        return output

    def specialized_coefficients(compiled, variable_position, values):
        maximum = max(
            (exponents[variable_position] for exponents, _ in compiled),
            default=0,
        )
        coefficients = [0]*(maximum+1)
        for exponents, coefficient in compiled:
            value = coefficient
            for position, point in enumerate(values):
                if position != variable_position:
                    value = value*pow(point, exponents[position], PRIME) % PRIME
            degree = exponents[variable_position]
            coefficients[degree] = (coefficients[degree]+value) % PRIME
        return coefficients

    def field_roots(polynomial):
        if polynomial.is_zero():
            return None
        if polynomial.degree() == 0:
            return []
        root_polynomial = polynomial.gcd(
            pow(variable, PRIME, polynomial)-variable
        )
        _, factors = root_polynomial.factor()
        output = []
        for factor, _ in factors:
            if factor.degree() != 1:
                raise ValueError("field-root gcd contains a nonlinear factor")
            output.append(
                -int(factor[0])*pow(int(factor[1]), -1, PRIME) % PRIME
            )
        return sorted(output)

    exceptional_root_rows = []
    exceptional_r_values = set()
    for name, guard in guard_values:
        for part_name, polynomial in (
            ("numerator", guard.numer), ("denominator", guard.denom)
        ):
            part_roots = field_roots(polynomial)
            exceptional_root_rows.append({
                "guard": name,
                "part": part_name,
                "degree": polynomial.degree(),
                "roots": part_roots,
            })
            if part_roots is None:
                raise ValueError(f"identically zero guard {name}/{part_name}")
            exceptional_r_values.update(part_roots)

    base_terms = compile_terms(
        interface["base_relation"]["expression"], (t, r)
    )
    b_terms = compile_terms(
        interface["b_relation"]["expression"], (b, t, r)
    )
    c_constant_terms = compile_terms(
        interface["c_constant"]["expression"], (b, t, r)
    )
    c_denominator_terms = compile_terms(
        interface["c_denominator"]["expression"], (t, r)
    )
    kernel_terms = [
        compile_terms(value["expression"], (c, b, t, r))
        for value in kernel_row["kernel"]
    ]
    cofactor_terms = [
        compile_terms(value, (t, r, c, b))
        for value in product_row["stripped_expressions"]
    ]

    def route_guards(r_value, t_value=None, b_value=None, c_value=None):
        values = {"r": r_value, "r2_minus_1": r_value*r_value-1,
                  "r2_plus_1": r_value*r_value+1}
        if t_value is not None:
            values.update({
                "t": t_value,
                "t2_minus_1": t_value*t_value-1,
                "t2_plus_1": t_value*t_value+1,
                "t2_minus_r2": t_value*t_value-r_value*r_value,
                "t2_plus_r2": t_value*t_value+r_value*r_value,
            })
        if b_value is not None and c_value is not None:
            values.update({
                "b": b_value, "c": c_value,
                "b_minus_1": b_value-1, "b_plus_1": b_value+1,
                "c_minus_1": c_value-1, "c_plus_1": c_value+1,
                "b_minus_c": b_value-c_value,
                "b_plus_c": b_value+c_value,
            })
        return [name for name, value in values.items() if value % PRIME == 0]

    def target_guards(representatives):
        failures = []
        for index, value in enumerate(representatives):
            if value % PRIME == 0:
                failures.append(f"nonzero_{index}")
        for left in range(6):
            for right in range(left+1, 6):
                if (representatives[left]-representatives[right]) % PRIME == 0:
                    failures.append(f"difference_{left}_{right}")
                if (representatives[left]+representatives[right]) % PRIME == 0:
                    failures.append(f"sum_{left}_{right}")
        return failures

    def paired_polynomial_at(left, right_scale=1):
        p0, p1, p2 = (
            (b_value-left*a_value) % PRIME
            for a_value, b_value in zip(a_values, b_values)
        )
        q0 = polynomial_context([
            b_values[0], -right_scale*a_values[0]
        ])
        q1 = polynomial_context([
            -b_values[1], right_scale*a_values[1]
        ])
        q2 = polynomial_context([
            b_values[2], -right_scale*a_values[2]
        ])
        return (p2*q0-p0*q2)**2-(p2*q1-p1*q2)*(p1*q0-p0*q1)

    def paired_value_at(left, right):
        p0, p1, p2 = (
            (b_value-left*a_value) % PRIME
            for a_value, b_value in zip(a_values, b_values)
        )
        q0 = (b_values[0]-right*a_values[0]) % PRIME
        q1 = (-b_values[1]+right*a_values[1]) % PRIME
        q2 = (b_values[2]-right*a_values[2]) % PRIME
        return (
            (p2*q0-p0*q2)**2-(p2*q1-p1*q2)*(p1*q0-p0*q1)
        ) % PRIME

    lift_rows = []
    source_points = []
    uf_candidates = []
    third_pair_solutions = []
    boundary_solutions = []
    witnesses = []
    unresolved = []
    live_r_values = {
        row["r"] for row in root_rows if row["status"] == "LIVE_NORM_ROOT"
    }
    candidate_r_values = set(roots or []) | exceptional_r_values
    for r_value in sorted(candidate_r_values):
        r_row = {
            "r": r_value,
            "route_guards": route_guards(r_value),
            "t_rows": [],
        }
        if r_row["route_guards"]:
            r_row["status"] = "ROUTE_BOUNDARY"
            lift_rows.append(r_row)
            continue
        t_roots = field_roots(polynomial_context(specialized_coefficients(
            base_terms, 0, (0, r_value)
        )))
        r_row["t_roots"] = t_roots
        if t_roots is None:
            r_row["status"] = "ZERO_BASE_POLYNOMIAL"
            unresolved.append([r_value, "ZERO_BASE_POLYNOMIAL"])
            lift_rows.append(r_row)
            continue
        for t_value in t_roots:
            t_row = {
                "t": t_value,
                "route_guards": route_guards(r_value, t_value),
                "b_rows": [],
            }
            if t_row["route_guards"]:
                t_row["status"] = "ROUTE_BOUNDARY"
                r_row["t_rows"].append(t_row)
                continue
            b_roots = field_roots(polynomial_context(specialized_coefficients(
                b_terms, 0, (0, t_value, r_value)
            )))
            t_row["b_roots"] = b_roots
            if b_roots is None:
                t_row["status"] = "ZERO_B_POLYNOMIAL"
                unresolved.append([r_value, t_value, "ZERO_B_POLYNOMIAL"])
                r_row["t_rows"].append(t_row)
                continue
            for b_value in b_roots:
                c_denominator = evaluate_terms(
                    c_denominator_terms, (t_value, r_value)
                )
                b_row = {"b": b_value, "c_denominator": c_denominator}
                if c_denominator == 0:
                    b_row["status"] = "C_DENOMINATOR_BOUNDARY"
                    t_row["b_rows"].append(b_row)
                    continue
                c_value = (
                    -evaluate_terms(
                        c_constant_terms, (b_value, t_value, r_value)
                    )*pow(c_denominator, -1, PRIME)
                ) % PRIME
                b_row["c"] = c_value
                b_row["route_guards"] = route_guards(
                    r_value, t_value, b_value, c_value
                )
                if b_row["route_guards"]:
                    b_row["status"] = "ROUTE_BOUNDARY"
                    t_row["b_rows"].append(b_row)
                    continue
                cofactors = [
                    evaluate_terms(value, (t_value, r_value, c_value, b_value))
                    for value in cofactor_terms
                ]
                b_row["nonzero_cofactor_indices"] = [
                    index for index, value in enumerate(cofactors) if value
                ]
                if not b_row["nonzero_cofactor_indices"]:
                    b_row["status"] = "PRODUCT_RANK_DROP"
                    t_row["b_rows"].append(b_row)
                    continue
                kernel_values = [
                    evaluate_terms(value, (c_value, b_value, t_value, r_value))
                    for value in kernel_terms
                ]
                a_values = kernel_values[:3]
                b_values = kernel_values[3:6]
                beta_0_value, beta_1_value = kernel_values[6:]
                missing_label_value = -t_value*t_value % PRIME
                a_missing_value = (
                    a_values[0]+a_values[1]*missing_label_value
                    + a_values[2]*missing_label_value*missing_label_value
                ) % PRIME
                b_missing_value = (
                    b_values[0]+b_values[1]*missing_label_value
                    + b_values[2]*missing_label_value*missing_label_value
                ) % PRIME
                b_row["a_missing"] = a_missing_value
                b_row["b_missing"] = b_missing_value
                if a_missing_value == 0:
                    b_row["status"] = (
                        "MISSING_RATIO_FREE" if b_missing_value == 0
                        else "MISSING_RATIO_INCONSISTENT"
                    )
                    if b_missing_value == 0:
                        unresolved.append([
                            r_value, t_value, b_value, c_value,
                            "MISSING_RATIO_FREE",
                        ])
                    t_row["b_rows"].append(b_row)
                    continue
                source_missing = (
                    b_missing_value*pow(a_missing_value, -1, PRIME)
                ) % PRIME
                de_value = source_missing if xi_index == 0 else -source_missing % PRIME
                source_sum = (
                    missing_label_value
                    * pow(
                        (beta_0_value+beta_1_value*missing_label_value) % PRIME,
                        2, PRIME,
                    )
                    * pow(a_missing_value, -2, PRIME)
                ) % PRIME
                second_de_value = (
                    -de_value % PRIME if xi_index == 0 else de_value
                )
                b_row.update({
                    "source_missing": source_missing,
                    "de": de_value,
                    "source_sum": source_sum,
                })
                point = [r_value, t_value, b_value, c_value]
                source_points.append(point)
                if de_value == 0:
                    b_row["status"] = "TARGET_PRODUCT_BOUNDARY"
                    t_row["b_rows"].append(b_row)
                    continue
                p_b_field = paired_polynomial_at(de_value, b_value)
                p_c_field = paired_polynomial_at(
                    second_de_value, sigma_c*c_value % PRIME
                )
                b_roots_f = field_roots(p_b_field)
                c_roots_f = field_roots(p_c_field)
                b_row["b_pair_f_roots"] = b_roots_f
                b_row["c_pair_f_roots"] = c_roots_f
                if b_roots_f is None or c_roots_f is None:
                    b_row["status"] = "ZERO_PAIR_CUT"
                    unresolved.append([point, "ZERO_PAIR_CUT"])
                    t_row["b_rows"].append(b_row)
                    continue
                f_roots = sorted(set(b_roots_f) & set(c_roots_f))
                b_row["common_f_roots"] = f_roots
                b_row["uf_rows"] = []
                for f_value in f_roots:
                    if f_value == 0:
                        candidate = {"point": point, "u": None, "f": f_value}
                        uf_row = {
                            "u": None,
                            "f": f_value,
                            "status": "TARGET_BOUNDARY",
                            "failed_guards": ["nonzero_5"],
                            "target_lanes_covered": [
                                [sigma_c, lane_o] for lane_o in (-1, 1)
                            ],
                        }
                        boundary_solutions.append({**candidate, **uf_row})
                        b_row["uf_rows"].append(uf_row)
                        continue
                    f_squared = f_value*f_value % PRIME
                    relation_polynomial = polynomial_context([
                        de_value*de_value*f_squared*f_squared % PRIME,
                        0,
                        f_squared*(2*eta*de_value-source_sum) % PRIME,
                        0,
                        1,
                    ])
                    u_roots = field_roots(relation_polynomial)
                    if u_roots is None:
                        b_row["status"] = "ZERO_MISSING_RELATION"
                        unresolved.append([point, f_value,
                                           "ZERO_MISSING_RELATION"])
                        continue
                    for u_value in u_roots:
                        relation_value = (
                            pow(
                                u_value*u_value
                                + eta*de_value*f_value*f_value,
                                2, PRIME,
                            )
                            - source_sum*f_value*f_value*u_value*u_value
                        ) % PRIME
                        uf_row = {
                            "u": u_value,
                            "f": f_value,
                            "relation": relation_value,
                        }
                        if relation_value:
                            raise ValueError("field root violates source relation")
                        candidate = {
                            "point": point, "u": u_value, "f": f_value,
                        }
                        uf_candidates.append(candidate)
                        e_value = u_value*pow(f_value, -1, PRIME) % PRIME
                        if e_value == 0:
                            uf_row.update({
                                "e": e_value,
                                "status": "TARGET_BOUNDARY",
                                "failed_guards": ["nonzero_4"],
                                "target_lanes_covered": [
                                    [sigma_c, lane_o]
                                    for lane_o in (-1, 1)
                                ],
                            })
                            boundary_solutions.append({**candidate, **uf_row})
                            b_row["uf_rows"].append(uf_row)
                            continue
                        d_value = de_value*pow(e_value, -1, PRIME) % PRIME
                        v_value = d_value*f_value % PRIME
                        uf_row.update({
                            "d": d_value, "e": e_value, "v": v_value,
                            "lanes": [],
                        })
                        for lane_c in (sigma_c,):
                            for lane_o in (-1, 1):
                                third_pair_cut = paired_value_at(
                                    v_value,
                                    lane_o*u_value % PRIME,
                                )
                                lane_row = {
                                    "sigma": [lane_c, lane_o],
                                    "third_pair_cut": third_pair_cut,
                                }
                                if third_pair_cut:
                                    lane_row["status"] = "THIRD_PAIR_NONZERO"
                                    uf_row["lanes"].append(lane_row)
                                    continue
                                representatives = (
                                    1, b_value, c_value,
                                    d_value, e_value, f_value,
                                )
                                failed_guards = target_guards(representatives)
                                equation_values = [
                                    (d_value*e_value-de_value) % PRIME,
                                    (
                                        pow(d_value+eta*e_value, 2, PRIME)
                                        - source_sum
                                    ) % PRIME,
                                    paired_value_at(
                                        de_value,
                                        b_value*f_value % PRIME,
                                    ),
                                    paired_value_at(
                                        second_de_value,
                                        lane_c*c_value*f_value % PRIME,
                                    ),
                                    third_pair_cut,
                                ]
                                if any(equation_values):
                                    raise ValueError("direct lift replay failed")
                                lane_row.update({
                                    "target_representatives": list(
                                        representatives
                                    ),
                                    "failed_guards": failed_guards,
                                    "equation_values": equation_values,
                                    "status": (
                                        "TARGET_BOUNDARY" if failed_guards
                                        else "WITNESS"
                                    ),
                                })
                                record = {
                                    **candidate,
                                    "d": d_value,
                                    "e": e_value,
                                    "v": v_value,
                                    **lane_row,
                                }
                                third_pair_solutions.append(record)
                                (
                                    boundary_solutions
                                    if failed_guards else witnesses
                                ).append(record)
                                uf_row["lanes"].append(lane_row)
                        uf_row["status"] = "CHECKED"
                        b_row["uf_rows"].append(uf_row)
                b_row["status"] = "CHECKED"
                t_row["b_rows"].append(b_row)
            t_row["status"] = "CHECKED"
            r_row["t_rows"].append(t_row)
        r_row["status"] = "CHECKED"
        lift_rows.append(r_row)

    direct_lift = {
        "live_norm_root_count": len(live_r_values),
        "exceptional_root_count": len(exceptional_r_values),
        "candidate_r_count": len(candidate_r_values),
        "source_point_count": len(source_points),
        "source_points": source_points,
        "uf_candidate_count": len(uf_candidates),
        "uf_candidates": uf_candidates,
        "third_pair_solution_count": len(third_pair_solutions),
        "third_pair_solutions": third_pair_solutions,
        "boundary_solution_count": len(boundary_solutions),
        "boundary_solutions": boundary_solutions,
        "witness_count": len(witnesses),
        "witnesses": witnesses,
        "unresolved_count": len(unresolved),
        "unresolved": unresolved,
        "case_excluded": not witnesses and not unresolved,
        "rows": lift_rows,
    }
    print(json.dumps({
        "phase": "direct_lift",
        "live_norm_roots": len(live_r_values),
        "exceptional_roots": len(exceptional_r_values),
        "candidate_r_values": len(candidate_r_values),
        "source_points": len(source_points),
        "uf_candidates": len(uf_candidates),
        "third_pair_solutions": len(third_pair_solutions),
        "boundary_solutions": len(boundary_solutions),
        "witnesses": len(witnesses),
        "unresolved": len(unresolved),
        "case_excluded": direct_lift["case_excluded"],
        "seconds": time.perf_counter()-started,
    }), flush=True)

    return {
        "epsilon": [epsilon_1, epsilon_2],
        "sigma": [sigma_c, sigma_o],
        "xi_index": xi_index,
        "pairing_index": pairing_index,
        "status": "COMPLETE",
        "target_lanes_covered": [
            [sigma_c, lane_o]
            for lane_o in (-1, 1)
        ],
        "basis": ["1", "t", "t^2", "b", "b*t", "b*t^2"],
        "base_degree": 3,
        "b_degree": 2,
        "algebra_dimension": 6,
        "timings_seconds": {
            "algebra": algebra_seconds,
            "kernel": kernel_seconds-algebra_seconds,
            "target_free_cut": cut_seconds-kernel_seconds,
            "norm": norm_seconds-cut_seconds,
            "total": time.perf_counter()-started,
        },
        "inverse_guard_count": len(inverse_guards),
        "distinct_inverse_guard_count": len(seen_guards),
        "kernel_profiles": [
            [fraction_profile(value) for value in item.vector()]
            for item in kernel
        ],
        "missing_record_profiles": [
            fraction_profile(value) for value in missing_record.vector()
        ],
        "target_free_profiles": [
            fraction_profile(value) for value in target_free.vector()
        ],
        "p_b_degree": p_b.degree(),
        "p_c_degree": p_c.degree(),
        "target_free_norm": fraction_profile(target_free_norm),
        "tower_norm_match": True,
        "field_root_gcd_degree": (
            None if roots is None else int(field_gcd.degree())
        ),
        "field_root_factor_degrees": factor_degrees,
        "field_roots": roots,
        "field_root_rows": root_rows,
        "exceptional_root_rows": exceptional_root_rows,
        "direct_lift": direct_lift,
    }


@app.local_entrypoint()
def main(
    signs: str = "-1:-1",
    lane: str = "-1:-1",
    xi_index: int = 0,
    pairing_index: int = 11,
    all_signs: bool = False,
    source_census: bool = False,
    full_census: bool = False,
):
    sigma = tuple(int(value) for value in lane.split(":"))
    sign_pairs = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    if full_census:
        cases = tuple(
            (*epsilon, sigma_c, sigma_o, selected_xi, 11)
            for epsilon in sign_pairs
            for sigma_c in (-1, 1)
            for sigma_o in (-1, 1)
            for selected_xi in (0, 2)
        )
    elif source_census:
        cases = tuple(
            (*epsilon, sigma_c, -1, selected_xi, 11)
            for epsilon in sign_pairs
            for sigma_c in (-1, 1)
            for selected_xi in (0, 2)
        )
    else:
        selected_signs = (
            sign_pairs if all_signs
            else (tuple(int(value) for value in signs.split(":")),)
        )
        cases = tuple(
            (*epsilon, *sigma, xi_index, pairing_index)
            for epsilon in selected_signs
        )
    raw = list(profile_case.map(
        cases, order_outputs=True, return_exceptions=True
    ))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]),
                "sigma": list(case[2:4]),
                "xi_index": case[4],
                "pairing_index": case[5],
                "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-cell3-de-pairing11-common-f-resultant-source-census-v1"
            if source_census else
            "rate-half-kb-positive-433-1b-cell3-de-pairing11-common-f-resultant-census-v1"
            if all_signs or full_census else
            "rate-half-kb-positive-433-1b-cell3-de-pairing11-common-f-resultant-pilot-v1"
        ),
        "scope": (
            "Exact common-f resultant and exceptional-root census at "
            "DE-missing pairing 11; no claim beyond the printed cases."
        ),
        "source_quotient_sha256": hashlib.sha256(QUOTIENT.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "source_product_sha256": hashlib.sha256(PRODUCT.read_bytes()).hexdigest(),
        "rows": rows,
    }
    output_path = (
        CENSUS_RESULT if all_signs or source_census or full_census else RESULT
    )
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(output_path),
        "rows": [
            {
                "epsilon": row.get("epsilon"),
                "status": row.get("status"),
                "error": row.get("error"),
                "seconds": (row.get("timings_seconds") or {}).get("total"),
                "norm": row.get("target_free_norm"),
                "tower_norm_match": row.get("tower_norm_match"),
                "field_root_count": (
                    None if row.get("field_roots") is None
                    else len(row.get("field_roots", []))
                ),
                "direct_lift": {
                    key: (row.get("direct_lift") or {}).get(key)
                    for key in (
                        "live_norm_root_count", "exceptional_root_count",
                        "candidate_r_count", "source_point_count",
                        "uf_candidate_count", "third_pair_solution_count",
                        "boundary_solution_count", "witness_count",
                        "unresolved_count", "case_excluded",
                    )
                },
            }
            for row in rows
        ],
    }, sort_keys=True))
