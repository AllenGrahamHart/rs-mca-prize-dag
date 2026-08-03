#!/usr/bin/env python3
"""Test source-only endpoint compatibility for cell-3 xi5 and xi6."""

import hashlib
import json
from pathlib import Path
import time

import modal


DIRECTORY = Path(__file__).parent
QUOTIENT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_birational_profile_result.json"
KERNEL = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_compact_kernel_result.json"
PRODUCT = DIRECTORY / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_xi5_xi6_endpoint_compatibility_pilot_result.json"
CENSUS_RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_xi5_xi6_endpoint_compatibility_census_result.json"
REMOTE_QUOTIENT = "/root/quotient.json"
REMOTE_KERNEL = "/root/kernel.json"
REMOTE_PRODUCT = "/root/product.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell3-xi5-xi6-endpoint-compatibility")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0", "python-flint==0.8.0")
    .add_local_file(QUOTIENT, REMOTE_QUOTIENT)
    .add_local_file(KERNEL, REMOTE_KERNEL)
    .add_local_file(PRODUCT, REMOTE_PRODUCT)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=600, max_containers=16)
def profile_case(case):
    import sympy as sp
    from flint import fmpz_mod_poly_ctx

    started = time.perf_counter()
    epsilon_1, epsilon_2, sigma_c, sigma_o, xi_index, pairing_index = case
    if (xi_index not in (5, 6) or pairing_index != 0 or
            sigma_c != 0 or sigma_o != 0):
        raise ValueError(
            "the pilot is scoped to source-only xi5/xi6 compatibility"
        )
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

    source_sum_record = (
        missing_label*(beta_0+beta_1*missing_label)**2/a_missing**2
    )
    endpoint_record = common_b if xi_index == 5 else c_pair
    endpoint_square = endpoint_record**2
    endpoint_compatibility = (
        (endpoint_square+missing_record)**2
        - source_sum_record*endpoint_square
    )
    if endpoint_compatibility == Pair():
        raise ValueError("endpoint compatibility vanishes identically")
    print(json.dumps({
        "phase": "endpoint_compatibility",
        "xi_index": xi_index,
        "seconds": time.perf_counter()-started,
    }), flush=True)
    cut_seconds = time.perf_counter()-started
    endpoint_compatibility_pair_norm = (
        endpoint_compatibility.constant
        * (
            endpoint_compatibility.constant
            + endpoint_compatibility.linear*quotient_u
        )
        - endpoint_compatibility.linear*endpoint_compatibility.linear*quotient_v
    )
    endpoint_compatibility_norm = endpoint_compatibility_pair_norm.norm()
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

    numerator = endpoint_compatibility_norm.numer
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
    guard_values.append((
        "endpoint_compatibility_norm", endpoint_compatibility_norm
    ))
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
                    name != "endpoint_compatibility_norm"
                    for name in zero_numerators
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

    lift_rows = []
    source_points = []
    compatible_source_points = []
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
                source_sum_value = (
                    missing_label_value
                    * pow(
                        (beta_0_value+beta_1_value*missing_label_value) % PRIME,
                        2, PRIME,
                    )
                    * pow(a_missing_value, -2, PRIME)
                ) % PRIME
                b_row.update({
                    "source_missing": source_missing,
                    "source_sum": source_sum_value,
                })
                point = [r_value, t_value, b_value, c_value]
                source_points.append(point)
                if source_missing == 0:
                    b_row["status"] = "MISSING_PRODUCT_BOUNDARY"
                    t_row["b_rows"].append(b_row)
                    continue
                endpoint_value = b_value if xi_index == 5 else c_value
                signed_other = (
                    source_missing*pow(endpoint_value, -1, PRIME)
                ) % PRIME
                endpoint_square_value = endpoint_value*endpoint_value % PRIME
                cleared_compatibility = (
                    pow(endpoint_square_value+source_missing, 2, PRIME)
                    - source_sum_value*endpoint_square_value
                ) % PRIME
                direct_compatibility = (
                    pow(endpoint_value+signed_other, 2, PRIME)
                    - source_sum_value
                ) % PRIME
                if cleared_compatibility != (
                    endpoint_square_value*direct_compatibility % PRIME
                ):
                    raise ValueError("cleared endpoint compatibility replay failed")
                b_row.update({
                    "endpoint": endpoint_value,
                    "endpoint_kind": "b" if xi_index == 5 else "c",
                    "signed_other": signed_other,
                    "cleared_compatibility": cleared_compatibility,
                    "direct_compatibility": direct_compatibility,
                })
                if cleared_compatibility == 0:
                    compatible = {
                        "point": point,
                        "endpoint": endpoint_value,
                        "endpoint_kind": "b" if xi_index == 5 else "c",
                        "source_missing": source_missing,
                        "source_sum": source_sum_value,
                        "signed_other": signed_other,
                    }
                    compatible_source_points.append(compatible)
                    b_row["status"] = "COMPATIBLE_SOURCE"
                else:
                    b_row["status"] = "COMPATIBILITY_NONZERO"
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
        "compatible_source_point_count": len(compatible_source_points),
        "compatible_source_points": compatible_source_points,
        "unresolved_count": len(unresolved),
        "unresolved": unresolved,
        "case_excluded": not compatible_source_points and not unresolved,
        "rows": lift_rows,
    }
    print(json.dumps({
        "phase": "direct_lift",
        "live_norm_roots": len(live_r_values),
        "exceptional_roots": len(exceptional_r_values),
        "candidate_r_values": len(candidate_r_values),
        "source_points": len(source_points),
        "compatible_source_points": len(compatible_source_points),
        "unresolved": len(unresolved),
        "case_excluded": direct_lift["case_excluded"],
        "seconds": time.perf_counter()-started,
    }), flush=True)

    return {
        "epsilon": [epsilon_1, epsilon_2],
        "sigma_c_anchor": sigma_c,
        "sigma_o_anchor": sigma_o,
        "xi_index": xi_index,
        "pairing_index": pairing_index,
        "status": "COMPLETE",
        "target_lanes_covered": [
            [-1, -1], [-1, 1], [1, -1], [1, 1]
        ],
        "endpoint_kind": "b" if xi_index == 5 else "c",
        "basis": ["1", "t", "t^2", "b", "b*t", "b*t^2"],
        "base_degree": 3,
        "b_degree": 2,
        "algebra_dimension": 6,
        "timings_seconds": {
            "algebra": algebra_seconds,
            "kernel": kernel_seconds-algebra_seconds,
            "endpoint_compatibility_cut": cut_seconds-kernel_seconds,
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
        "source_sum_profiles": [
            fraction_profile(value) for value in source_sum_record.vector()
        ],
        "endpoint_record_profiles": [
            fraction_profile(value) for value in endpoint_record.vector()
        ],
        "endpoint_compatibility_profiles": [
            fraction_profile(value)
            for value in endpoint_compatibility.vector()
        ],
        "endpoint_compatibility_norm": fraction_profile(
            endpoint_compatibility_norm
        ),
        "tower_norm_used": True,
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
    xi_index: int = 5,
    all_signs: bool = False,
    source_census: bool = False,
):
    sign_pairs = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    if source_census:
        cases = tuple(
            (*epsilon, 0, 0, selected_xi, 0)
            for epsilon in sign_pairs
            for selected_xi in (5, 6)
        )
    else:
        selected_signs = (
            sign_pairs if all_signs
            else (tuple(int(value) for value in signs.split(":")),)
        )
        cases = tuple(
            (*epsilon, 0, 0, xi_index, 0)
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
                "sigma_c_anchor": case[2],
                "sigma_o_anchor": case[3],
                "xi_index": case[4],
                "pairing_index": case[5],
                "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-cell3-xi5-xi6-endpoint-compatibility-source-census-v1"
            if source_census else
            "rate-half-kb-positive-433-1b-cell3-xi5-xi6-endpoint-compatibility-pilot-v1"
        ),
        "scope": (
            "Exact source-only endpoint compatibility and exceptional-root census "
            "at xi=5 and xi=6. A source exclusion applies to every pairing and "
            "every target sign lane for the printed source signs; compatible "
            "sources are not asserted to be target witnesses."
        ),
        "source_quotient_sha256": hashlib.sha256(QUOTIENT.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "source_product_sha256": hashlib.sha256(PRODUCT.read_bytes()).hexdigest(),
        "rows": rows,
    }
    output_path = CENSUS_RESULT if source_census else RESULT
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(output_path),
        "rows": [
            {
                "epsilon": row.get("epsilon"),
                "pairing_index": row.get("pairing_index"),
                "sigma_c_anchor": row.get("sigma_c_anchor"),
                "sigma_o_anchor": row.get("sigma_o_anchor"),
                "status": row.get("status"),
                "error": row.get("error"),
                "seconds": (row.get("timings_seconds") or {}).get("total"),
                "norm": row.get("endpoint_compatibility_norm"),
                "tower_norm_used": row.get("tower_norm_used"),
                "field_root_count": (
                    None if row.get("field_roots") is None
                    else len(row.get("field_roots", []))
                ),
                "direct_lift": {
                    key: (row.get("direct_lift") or {}).get(key)
                    for key in (
                        "live_norm_root_count", "exceptional_root_count",
                        "candidate_r_count", "source_point_count",
                        "compatible_source_point_count",
                        "unresolved_count", "case_excluded",
                    )
                },
            }
            for row in rows
        ],
    }, sort_keys=True))
