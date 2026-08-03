#!/usr/bin/env python3
"""Compute the cell-3 xi2/pairing0 target-free cut in the six-basis algebra."""

import hashlib
import json
from pathlib import Path
import time

import modal


DIRECTORY = Path(__file__).parent
QUOTIENT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_birational_profile_result.json"
KERNEL = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_compact_kernel_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_xi2_pairing0_six_basis_cut_result.json"
CENSUS_RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_xi2_pairing0_six_basis_cut_census_result.json"
REMOTE_QUOTIENT = "/root/quotient.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell3-xi2-pairing0-six-basis-cut")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0", "python-flint==0.8.0")
    .add_local_file(QUOTIENT, REMOTE_QUOTIENT)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=300, max_containers=4)
def profile_case(case):
    import sympy as sp
    from flint import fmpz_mod_poly_ctx

    started = time.perf_counter()
    epsilon_1, epsilon_2, sigma_c, sigma_o, xi_index, pairing_index = case
    if xi_index != 2 or pairing_index != 0:
        raise ValueError("the pilot is scoped exactly to xi=2, pairing=0")
    quotient_payload = json.loads(Path(REMOTE_QUOTIENT).read_text())
    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    source = next(
        row for row in quotient_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2] and row["chart"] == 0
    )
    kernel_row = next(
        row for row in kernel_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    )
    interface = source["quotient_interface"]
    r, t, b, c = sp.symbols("r t b c")
    base_field = sp.GF(PRIME).frac_field(r)
    zero = base_field.zero
    one = base_field.one
    inverse_guards = []

    def field_equal(left, right):
        left = base_field.convert(left)
        right = base_field.convert(right)
        return left.numer*right.denom == right.numer*left.denom

    def field_is_zero(value):
        return value.numer == value.numer.ring.zero

    def field_value(expression):
        polynomial = sp.Poly(expression, r, modulus=PRIME)
        return base_field.from_sympy(polynomial.as_expr())

    base_expression = sp.sympify(interface["base_relation"]["expression"])
    base_in_t = sp.Poly(base_expression, t)
    base_modulus = sp.Poly(base_expression, t, domain=base_field).monic()
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
            polynomial = sp.Poly(
                list(reversed(self.values)), t, domain=base_field
            )
            inverse, _, gcd = sp.gcdex(polynomial, base_modulus)
            if gcd.degree() != 0:
                raise ZeroDivisionError("nonunit in cubic function field")
            inverse = inverse.mul_ground(one/gcd.nth(0)).rem(base_modulus)
            return Cubic(*(inverse.nth(index) for index in range(3)))

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
            return Pair(
                (self.constant+self.linear*quotient_u)/determinant_value,
                -self.linear/determinant_value,
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
    a_coefficients = tuple(kernel[:3])
    b_coefficients = tuple(kernel[3:6])

    def evaluate(coefficients, value):
        return coefficients[0]+coefficients[1]*value+coefficients[2]*value**2

    missing_label = -Pair(cubic_t*cubic_t)
    a_missing = evaluate(a_coefficients, missing_label)
    b_missing = evaluate(b_coefficients, missing_label)
    missing_record = b_missing/a_missing

    def paired(left, right):
        p0, p1, p2 = (
            b_value-left*a_value
            for a_value, b_value in zip(a_coefficients, b_coefficients)
        )
        q0 = b_coefficients[0]-right*a_coefficients[0]
        q1 = -b_coefficients[1]+right*a_coefficients[1]
        q2 = b_coefficients[2]-right*a_coefficients[2]
        return (p2*q0-p0*q2)**2-(p2*q1-p1*q2)*(p1*q0-p0*q1)

    # At xi=2 the missing record is -de, so de=-missing_record and the
    # first residual pair under canonical matching zero is (de,de).
    de_record = -missing_record
    target_free = paired(de_record, de_record)
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
        terms = polynomial.terms()
        degree = max((exponents[0] for exponents, _ in terms), default=-1)
        expression = str(polynomial.as_expr())
        return {
            "degree": degree,
            "terms": len(terms),
            "sha256": hashlib.sha256(expression.encode()).hexdigest(),
            "expression": (
                expression if include_expression or len(terms) <= 80 else None
            ),
        }

    def fraction_profile(value):
        return {
            "numerator": polynomial_profile(value.numer),
            "denominator": polynomial_profile(value.denom),
        }

    polynomial_context = fmpz_mod_poly_ctx(PRIME)

    def flint_polynomial(polynomial):
        coefficients = {
            exponents[0]: int(coefficient)
            for exponents, coefficient in polynomial.terms()
        }
        maximum = max(coefficients, default=0)
        return polynomial_context([
            coefficients.get(exponent, 0) for exponent in range(maximum+1)
        ])

    numerator = flint_polynomial(target_free_norm.numer)
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
        return sum(
            int(coefficient)*pow(point, exponents[0], PRIME)
            for exponents, coefficient in polynomial.terms()
        ) % PRIME

    guard_values = []
    seen_guards = set()
    for index, guard in enumerate(inverse_guards):
        key = (str(guard.numer.as_expr()), str(guard.denom.as_expr()))
        if key in seen_guards:
            continue
        seen_guards.add(key)
        guard_values.append((f"inverse_{index}", guard))
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
                "DENOMINATOR_BOUNDARY" if
                zero_denominators or any(
                    name != "target_free_norm" for name in zero_numerators
                ) else "LIVE_NORM_ROOT"
            ),
        })

    return {
        "epsilon": [epsilon_1, epsilon_2],
        "sigma": [sigma_c, sigma_o],
        "xi_index": xi_index,
        "pairing_index": pairing_index,
        "status": "COMPLETE",
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
        "target_free_norm": fraction_profile(target_free_norm),
        "tower_norm_match": True,
        "field_root_gcd_degree": (
            None if roots is None else int(field_gcd.degree())
        ),
        "field_root_factor_degrees": factor_degrees,
        "field_roots": roots,
        "field_root_rows": root_rows,
    }


@app.local_entrypoint()
def main(
    signs: str = "-1:-1",
    lane: str = "-1:-1",
    xi_index: int = 2,
    pairing_index: int = 0,
    all_signs: bool = False,
):
    sigma = tuple(int(value) for value in lane.split(":"))
    selected_signs = (
        ((-1, -1), (-1, 1), (1, -1), (1, 1))
        if all_signs else (tuple(int(value) for value in signs.split(":")),)
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
                "xi_index": xi_index,
                "pairing_index": pairing_index,
                "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-cell3-xi2-pairing0-six-basis-cut-census-v1"
            if all_signs else
            "rate-half-kb-positive-433-1b-cell3-xi2-pairing0-six-basis-cut-v1"
        ),
        "scope": (
            "Exact target-free outside cuts in the six-dimensional common "
            "function field at xi2/pairing0; no wider outside or cell claim."
        ),
        "source_quotient_sha256": hashlib.sha256(QUOTIENT.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "rows": rows,
    }
    output_path = CENSUS_RESULT if all_signs else RESULT
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
            }
            for row in rows
        ],
    }, sort_keys=True))
