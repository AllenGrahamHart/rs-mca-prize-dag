#!/usr/bin/env python3
"""Test source-only endpoint compatibility for cell-4 xi5 and xi6."""

import hashlib
import json
from pathlib import Path
import time

import modal


DIRECTORY = Path(__file__).parent
STRUCTURE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_remaining_compact_pivot_scout_result.json"
)
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell4_compact_kernel_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell4_xi5_xi6_endpoint_compatibility_result.json"
)
REMOTE_STRUCTURE = "/root/structure.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell4-xi5-xi6-endpoint-compatibility")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0", "python-flint==0.8.0")
    .add_local_file(STRUCTURE, REMOTE_STRUCTURE)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=300, max_containers=16)
def evaluate_case(case):
    import re

    from flint import fmpz_mod_poly_ctx
    import sympy as sp

    started = time.perf_counter()
    epsilon_1, epsilon_2, xi_index = case
    if xi_index not in (5, 6):
        raise ValueError("scope is source-only xi in {5,6}")
    t, r, c, b = sp.symbols("t r c b")
    variables = (t, r, c, b)
    symbols = {"t": t, "r": r, "c": c, "b": b}

    def parse_singular(text, ordered_variables):
        expression = 0
        for term in re.findall(r"[+-]?[^+-]+", text):
            sign = -1 if term.startswith("-") else 1
            unsigned = term.lstrip("+-")
            digits = re.match(r"\d*", unsigned).group()
            monomial = sp.Integer(sign * int(digits or "1"))
            for variable, exponent in re.findall(
                r"([trcb])(\d*)", unsigned[len(digits):]
            ):
                monomial *= symbols[variable] ** int(exponent or "1")
            expression += monomial
        return sp.Poly(
            expression, *ordered_variables, modulus=PRIME
        ).as_expr()

    structure = json.loads(Path(REMOTE_STRUCTURE).read_text())
    structure_row = next(
        row for row in structure["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2] and row["chart"] == 0
    )
    base_expression = parse_singular(
        structure_row["lex_basis"][0]["expression"], (t, r)
    )
    b_expression = parse_singular(
        structure_row["lex_basis"][1]["expression"], (b, t, r)
    )
    c_expression = parse_singular(
        structure_row["lex_basis"][5]["expression"], (c, b, t, r)
    )
    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    kernel_row = next(
        row for row in kernel_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    )
    kernel_expressions = tuple(
        sp.sympify(value["expression"]) for value in kernel_row["kernel"]
    )

    polynomial_context = fmpz_mod_poly_ctx(PRIME)
    polynomial_type = type(polynomial_context.zero())

    def flint_polynomial(polynomial):
        coefficients = {
            exponents[0]: int(coefficient) % PRIME
            for exponents, coefficient in polynomial.terms()
        }
        maximum = max(coefficients, default=0)
        return polynomial_context([
            coefficients.get(exponent, 0) for exponent in range(maximum + 1)
        ])

    class RationalFunction:
        __slots__ = ("numer", "denom")

        def __init__(self, numer=0, denom=1):
            if isinstance(numer, RationalFunction):
                if denom != 1:
                    raise TypeError("cannot supply a second denominator")
                self.numer, self.denom = numer.numer, numer.denom
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
            numer //= common
            denom //= common
            scale = pow(int(denom[denom.degree()]), -1, PRIME)
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
                self.numer*right_denominator + other.numer*left_denominator,
                left_denominator*other.denom,
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
                (self.numer // left_common)*(other.numer // right_common),
                (self.denom // right_common)*(other.denom // left_common),
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
            return self*other.inverse()

        def __rtruediv__(self, other):
            other = RationalFunction.coerce(other)
            if other is NotImplemented:
                return NotImplemented
            return other/self

        def __pow__(self, exponent):
            if exponent < 0:
                return self.inverse()**(-exponent)
            return RationalFunction(self.numer**exponent, self.denom**exponent)

        def __eq__(self, other):
            other = RationalFunction.coerce(other)
            return (other is not NotImplemented and self.numer == other.numer
                    and self.denom == other.denom)

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

    def field_value(expression):
        return RationalFunction(flint_polynomial(
            sp.Poly(expression, r, modulus=PRIME)
        ))

    def field_equal(left, right):
        return base_field.convert(left) == base_field.convert(right)

    def field_is_zero(value):
        return base_field.convert(value).numer.is_zero()

    base_polynomial = sp.Poly(base_expression, t)
    base_coefficients = [
        field_value(value) for value in base_polynomial.all_coeffs()
    ]
    if len(base_coefficients) != 3:
        raise ValueError("base relation is not quadratic in t")
    base_leading, base_linear, base_constant = base_coefficients
    t_u = -base_linear / base_leading
    t_v = -base_constant / base_leading
    inverse_guards.append(("base_leading", base_leading))

    class Quad:
        __slots__ = ("constant", "linear")

        def __init__(self, constant=0, linear=0):
            self.constant = base_field.convert(constant)
            self.linear = base_field.convert(linear)

        @staticmethod
        def coerce(value):
            return value if isinstance(value, Quad) else Quad(value)

        def __add__(self, other):
            other = Quad.coerce(other)
            return Quad(
                self.constant + other.constant,
                self.linear + other.linear,
            )

        __radd__ = __add__

        def __neg__(self):
            return Quad(-self.constant, -self.linear)

        def __sub__(self, other):
            return self + (-Quad.coerce(other))

        def __rsub__(self, other):
            return Quad.coerce(other) - self

        def __mul__(self, other):
            other = Quad.coerce(other)
            return Quad(
                self.constant * other.constant
                + self.linear * other.linear * t_v,
                self.constant * other.linear
                + self.linear * other.constant
                + self.linear * other.linear * t_u,
            )

        __rmul__ = __mul__

        def __pow__(self, exponent):
            if exponent < 0:
                return self.inverse() ** (-exponent)
            output = Quad(1)
            base = self
            power = exponent
            while power:
                if power & 1:
                    output = output * base
                base = base * base
                power //= 2
            return output

        def norm(self):
            return (
                self.constant * (self.constant + self.linear * t_u)
                - self.linear * self.linear * t_v
            )

        def inverse(self):
            determinant = self.norm()
            inverse_guards.append(("quad_inverse", determinant))
            return Quad(
                (self.constant + self.linear * t_u) / determinant,
                -self.linear / determinant,
            )

        def __truediv__(self, other):
            return self * Quad.coerce(other).inverse()

        def __eq__(self, other):
            other = Quad.coerce(other)
            return field_equal(self.constant, other.constant) and field_equal(
                self.linear, other.linear
            )

        def vector(self):
            return (self.constant, self.linear)

    common_t = Quad(0, 1)
    if common_t * common_t != Quad(t_v, t_u):
        raise ValueError("quadratic t relation self-check failed")

    def quad_expression(expression):
        output = Quad()
        for (t_degree, r_degree), coefficient in sp.Poly(
            expression, t, r, modulus=PRIME
        ).terms():
            output += field_value(int(coefficient) * r**r_degree) * (
                common_t**t_degree
            )
        return output

    b_polynomial = sp.Poly(b_expression, b)
    b_leading_expression, b_linear_expression, b_constant_expression = (
        b_polynomial.all_coeffs()
    )
    b_leading = quad_expression(b_leading_expression)
    b_linear = quad_expression(b_linear_expression)
    b_constant = quad_expression(b_constant_expression)
    if b_leading != b_constant:
        raise ValueError("b relation is not palindromic")
    b_u = -b_linear / b_leading
    b_v = -b_constant / b_leading

    class Pair:
        __slots__ = ("constant", "linear")

        def __init__(self, constant=0, linear=0):
            self.constant = Quad.coerce(constant)
            self.linear = Quad.coerce(linear)

        @staticmethod
        def coerce(value):
            return value if isinstance(value, Pair) else Pair(value)

        def __add__(self, other):
            other = Pair.coerce(other)
            return Pair(
                self.constant + other.constant,
                self.linear + other.linear,
            )

        __radd__ = __add__

        def __neg__(self):
            return Pair(-self.constant, -self.linear)

        def __sub__(self, other):
            return self + (-Pair.coerce(other))

        def __rsub__(self, other):
            return Pair.coerce(other) - self

        def __mul__(self, other):
            other = Pair.coerce(other)
            return Pair(
                self.constant * other.constant
                + self.linear * other.linear * b_v,
                self.constant * other.linear
                + self.linear * other.constant
                + self.linear * other.linear * b_u,
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
                    output = output * base
                base = base * base
                power //= 2
            return output

        def pair_norm(self):
            return (
                self.constant * (self.constant + self.linear * b_u)
                - self.linear * self.linear * b_v
            )

        def norm(self):
            return self.pair_norm().norm()

        def inverse(self):
            determinant = self.pair_norm()
            determinant_inverse = determinant.inverse()
            return Pair(
                (self.constant + self.linear * b_u) * determinant_inverse,
                -self.linear * determinant_inverse,
            )

        def __truediv__(self, other):
            return self * Pair.coerce(other).inverse()

        def __eq__(self, other):
            other = Pair.coerce(other)
            return self.constant == other.constant and self.linear == other.linear

        def vector(self):
            return (*self.constant.vector(), *self.linear.vector())

    common_b = Pair(0, 1)
    if common_b * common_b != Pair(b_v, b_u):
        raise ValueError("quadratic b relation self-check failed")

    def pair_expression(expression):
        output = Pair()
        for (b_degree, t_degree, r_degree), coefficient in sp.Poly(
            expression, b, t, r, modulus=PRIME
        ).terms():
            scalar = field_value(int(coefficient) * r**r_degree)
            output += Pair(scalar * common_t**t_degree) * common_b**b_degree
        return output

    c_polynomial = sp.Poly(c_expression, c)
    c_leading_expression, c_constant_expression = c_polynomial.all_coeffs()
    c_leading = pair_expression(c_leading_expression)
    c_constant = pair_expression(c_constant_expression)
    c_pair = -c_constant / c_leading

    def tower_expression(expression):
        output = Pair()
        for exponents, coefficient in sp.Poly(
            expression, c, b, t, r, modulus=PRIME
        ).terms():
            c_degree, b_degree, t_degree, r_degree = exponents
            scalar = field_value(int(coefficient) * r**r_degree)
            output += (
                Pair(scalar * common_t**t_degree)
                * common_b**b_degree * c_pair**c_degree
            )
        return output

    algebra_seconds = time.perf_counter() - started
    kernel = tuple(tower_expression(value) for value in kernel_expressions)
    kernel_seconds = time.perf_counter() - started
    print(json.dumps({"phase": "kernel", "seconds": kernel_seconds}),
          flush=True)
    a_coefficients = kernel[:3]
    b_coefficients = kernel[3:6]

    def evaluate(coefficients, value):
        return sum(
            coefficient * value**index
            for index, coefficient in enumerate(coefficients)
        )

    missing_label = -Pair(common_t * common_t)
    a_missing = evaluate(a_coefficients, missing_label)
    b_missing = evaluate(b_coefficients, missing_label)
    missing_record = b_missing / a_missing

    beta_0, beta_1 = kernel[6:]
    source_sum_record = (
        missing_label * (beta_0 + beta_1 * missing_label) ** 2
        / a_missing**2
    )
    endpoint_record = common_b if xi_index == 5 else c_pair
    endpoint_square = endpoint_record**2
    endpoint_compatibility = (
        (endpoint_square + missing_record) ** 2
        - source_sum_record * endpoint_square
    )
    if endpoint_compatibility == Pair():
        raise ValueError("endpoint compatibility vanishes identically")
    print(json.dumps({
        "phase": "endpoint_compatibility",
        "seconds": time.perf_counter() - started,
    }), flush=True)
    cut_seconds = time.perf_counter() - started
    compatibility_norm = endpoint_compatibility.norm()
    print(json.dumps({
        "phase": "norm",
        "seconds": time.perf_counter() - started,
    }), flush=True)
    norm_seconds = time.perf_counter() - started

    def field_roots(polynomial):
        value = polynomial
        if value.is_zero():
            return None
        if int(value.degree()) == 0:
            return []
        variable = polynomial_context([0, 1])
        root_part = value.gcd(pow(variable, PRIME, value) - variable)
        _, factors = root_part.factor()
        roots = []
        for factor, multiplicity in factors:
            if int(factor.degree()) != 1:
                raise ValueError("field-root gcd has nonlinear factor")
            root = -int(factor[0]) * pow(int(factor[1]), -1, PRIME) % PRIME
            roots.extend([root] * int(multiplicity))
        return sorted(set(roots))

    def polynomial_profile(polynomial, include_expression=True):
        coefficients = polynomial.coeffs()
        terms = sum(int(value) != 0 for value in coefficients)
        degree = int(polynomial.degree())
        text = str(polynomial)
        profile = {
            "degree": degree,
            "terms": terms,
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
        }
        if include_expression:
            profile["expression"] = text
        return profile

    def fraction_profile(value, include_expression=True):
        return {
            "numerator": polynomial_profile(
                value.numer, include_expression=include_expression
            ),
            "denominator": polynomial_profile(
                value.denom, include_expression=include_expression
            ),
        }

    guard_values = []
    seen_guards = set()
    for name, guard in inverse_guards:
        key = (str(guard.numer), str(guard.denom))
        if key in seen_guards:
            continue
        seen_guards.add(key)
        guard_values.append((f"{name}_{len(guard_values)}", guard))

    compatibility_roots = field_roots(compatibility_norm.numer)
    candidate_roots = set(compatibility_roots or [])
    all_field_roots = False
    for _, guard in [
        *guard_values,
        ("endpoint_compatibility_norm", compatibility_norm),
    ]:
        for polynomial in (guard.numer, guard.denom):
            roots = field_roots(polynomial)
            if roots is None:
                all_field_roots = True
            else:
                candidate_roots.update(roots)

    def mod_value(expression, point):
        values = {r: point["r"], t: point.get("t", 0),
                  b: point.get("b", 0), c: point.get("c", 0)}
        output = 0
        for exponents, coefficient in sp.Poly(
            expression, *variables, modulus=PRIME
        ).terms():
            term = int(coefficient) % PRIME
            for variable, exponent in zip(variables, exponents):
                term = term * pow(values[variable], exponent, PRIME) % PRIME
            output = (output + term) % PRIME
        return output

    def univariate_roots(coefficients):
        while coefficients and coefficients[-1] % PRIME == 0:
            coefficients.pop()
        if not coefficients:
            return None
        polynomial = polynomial_context([value % PRIME for value in coefficients])
        _, factors = polynomial.factor()
        roots = []
        for factor, multiplicity in factors:
            if int(factor.degree()) == 1:
                root = -int(factor[0]) * pow(int(factor[1]), -1, PRIME) % PRIME
                roots.extend([root] * int(multiplicity))
        return sorted(set(roots))

    def coefficients_at(expression, variable, point):
        polynomial = sp.Poly(expression, variable)
        return [
            mod_value(polynomial.coeff_monomial(variable**degree), point)
            for degree in range(polynomial.degree() + 1)
        ]

    route_guards = (
        b, c, r, t, b - 1, b + 1, c - 1, c + 1, b - c, b + c,
        r*r - 1, r*r + 1, t*t - 1, t*t + 1,
        t*t - r*r, t*t + r*r,
    )

    finite_rows = []
    unresolved = []
    boundary_rows = []
    target_boundary_rows = []
    no_lift_rows = []
    compatible_source_points = []
    source_point_count = 0
    route_point_count = 0
    for r_value in sorted(candidate_roots):
        base_point = {"r": r_value}
        if any(mod_value(guard, base_point) == 0 for guard in (
            r, r*r - 1, r*r + 1,
        )):
            boundary_rows.append({**base_point, "stage": "R_GUARD"})
            continue
        t_roots = univariate_roots(
            coefficients_at(base_expression, t, base_point)
        )
        if t_roots is None:
            unresolved.append({"r": r_value, "reason": "FREE_T"})
            continue
        if not t_roots:
            no_lift_rows.append({**base_point, "stage": "NO_T_ROOT"})
            continue
        for t_value in t_roots:
            bt_point = {"r": r_value, "t": t_value}
            if any(mod_value(guard, bt_point) == 0 for guard in (
                t, t*t - 1, t*t + 1,
                t*t - r*r, t*t + r*r,
            )):
                boundary_rows.append({**bt_point, "stage": "T_GUARD"})
                continue
            b_roots = univariate_roots(
                coefficients_at(b_expression, b, bt_point)
            )
            if b_roots is None:
                unresolved.append({**bt_point, "reason": "FREE_B"})
                continue
            if not b_roots:
                no_lift_rows.append({**bt_point, "stage": "NO_B_ROOT"})
                continue
            for b_value in b_roots:
                c_point = {**bt_point, "b": b_value}
                if any(mod_value(guard, c_point) == 0 for guard in (
                    b, b - 1, b + 1,
                )):
                    boundary_rows.append({**c_point, "stage": "B_GUARD"})
                    continue
                c_coefficients = coefficients_at(c_expression, c, c_point)
                if len(c_coefficients) < 2 or c_coefficients[1] == 0:
                    if c_coefficients and c_coefficients[0] != 0:
                        no_lift_rows.append({**c_point, "stage": "NO_C_ROOT"})
                        continue
                    unresolved.append({**c_point, "reason": "FREE_C"})
                    continue
                c_value = -c_coefficients[0] * pow(
                    c_coefficients[1], -1, PRIME
                ) % PRIME
                point = {**c_point, "c": c_value}
                source_point_count += 1
                if any(mod_value(guard, point) == 0 for guard in route_guards):
                    boundary_rows.append({**point, "stage": "FULL_GUARD"})
                    continue
                route_point_count += 1
                values = [mod_value(value, point) for value in kernel_expressions]
                a_values = values[:3]
                b_values = values[3:6]
                beta_0_value, beta_1_value = values[6:]
                label = -t_value * t_value % PRIME
                a_value = sum(
                    value * pow(label, index, PRIME)
                    for index, value in enumerate(a_values)
                ) % PRIME
                b_value_at_label = sum(
                    value * pow(label, index, PRIME)
                    for index, value in enumerate(b_values)
                ) % PRIME
                if a_value == 0:
                    status = "MISSING_IMPOSSIBLE" if b_value_at_label else "MISSING_FREE"
                    if status == "MISSING_FREE":
                        unresolved.append({**point, "reason": status})
                    finite_rows.append({**point, "status": status})
                    continue
                missing = b_value_at_label * pow(a_value, -1, PRIME) % PRIME
                source_sum = (
                    label
                    * pow((beta_0_value + beta_1_value*label) % PRIME,
                          2, PRIME)
                    * pow(a_value, -2, PRIME)
                ) % PRIME
                endpoint_value = b_value if xi_index == 5 else c_value
                endpoint_row = {
                    **point,
                    "missing": missing,
                    "source_sum": source_sum,
                    "endpoint_kind": "b" if xi_index == 5 else "c",
                    "endpoint": endpoint_value,
                }
                if missing == 0:
                    endpoint_row["status"] = "TARGET_PRODUCT_BOUNDARY"
                    target_boundary_rows.append(endpoint_row)
                    finite_rows.append(endpoint_row)
                    continue
                if endpoint_value == 0:
                    endpoint_row["status"] = "TARGET_ENDPOINT_BOUNDARY"
                    target_boundary_rows.append(endpoint_row)
                    finite_rows.append(endpoint_row)
                    continue
                endpoint_square_value = endpoint_value * endpoint_value % PRIME
                other_endpoint = (
                    missing * pow(endpoint_value, -1, PRIME) % PRIME
                )
                cleared_compatibility = (
                    pow((endpoint_square_value + missing) % PRIME, 2, PRIME)
                    - source_sum * endpoint_square_value
                ) % PRIME
                direct_compatibility = (
                    pow((endpoint_value + other_endpoint) % PRIME, 2, PRIME)
                    - source_sum
                ) % PRIME
                if cleared_compatibility != (
                    endpoint_square_value * direct_compatibility % PRIME
                ):
                    raise ValueError("cleared endpoint compatibility replay failed")
                endpoint_row.update({
                    "other_endpoint": other_endpoint,
                    "cleared_compatibility": cleared_compatibility,
                    "direct_compatibility": direct_compatibility,
                    "status": (
                        "COMPATIBLE_SOURCE"
                        if cleared_compatibility == 0
                        else "INCOMPATIBLE_SOURCE"
                    ),
                })
                if cleared_compatibility == 0:
                    compatible_source_points.append(endpoint_row)
                finite_rows.append(endpoint_row)

    if all_field_roots:
        unresolved.append({"reason": "IDENTICALLY_ZERO_ROOT_POLYNOMIAL"})
    replay_seconds = time.perf_counter() - started
    return {
        "epsilon": [epsilon_1, epsilon_2],
        "xi_index": xi_index,
        "status": "COMPLETE" if not unresolved else "INCOMPLETE",
        "timings": {
            "algebra": algebra_seconds,
            "kernel": kernel_seconds - algebra_seconds,
            "endpoint_compatibility": cut_seconds - kernel_seconds,
            "norm": norm_seconds - cut_seconds,
            "replay": replay_seconds - norm_seconds,
            "total": replay_seconds,
        },
        "base_relation": str(base_expression),
        "b_relation": str(b_expression),
        "c_relation": str(c_expression),
        "endpoint_kind": "b" if xi_index == 5 else "c",
        "endpoint_compatibility_profiles": [
            fraction_profile(value, include_expression=False)
            for value in endpoint_compatibility.vector()
        ],
        "endpoint_compatibility_norm": fraction_profile(compatibility_norm),
        "compatibility_root_count": (
            None if compatibility_roots is None else len(compatibility_roots)
        ),
        "compatibility_roots": compatibility_roots,
        "candidate_root_count": len(candidate_roots),
        "candidate_roots": sorted(candidate_roots),
        "source_point_count": source_point_count,
        "route_point_count": route_point_count,
        "boundary_rows": boundary_rows,
        "target_boundary_rows": target_boundary_rows,
        "no_lift_rows": no_lift_rows,
        "finite_rows": finite_rows,
        "compatible_source_point_count": len(compatible_source_points),
        "compatible_source_points": compatible_source_points,
        "unresolved": unresolved,
        "source_excluded": not compatible_source_points and not unresolved,
        "inverse_guards": [
            {"name": name, **fraction_profile(value)}
            for name, value in guard_values
        ],
    }


@app.local_entrypoint()
def main(cases: str = "-1:-1:6", all_cases: bool = False):
    if all_cases:
        selected = tuple(
            (epsilon_1, epsilon_2, xi_index)
            for epsilon_1 in (-1, 1)
            for epsilon_2 in (-1, 1)
            for xi_index in (5, 6)
        )
    else:
        selected = tuple(
            tuple(int(value) for value in item.split(":"))
            for item in cases.split(",") if item
        )
    raw = list(evaluate_case.map(
        selected, order_outputs=True, return_exceptions=True
    ))
    rows = []
    for case, row in zip(selected, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]),
                "xi_index": case[2],
                "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-cell4-xi5-xi6-"
            "endpoint-compatibility-v1"
        ),
        "field": PRIME,
        "scope": (
            "Exact source-only endpoint compatibility norm and exceptional-root "
            "replay for cell 4 at xi in {5,6}. A source exclusion applies to "
            "every pairing and target-sign lane; compatible sources are not "
            "asserted to be target witnesses."
        ),
        "source_structure_sha256": hashlib.sha256(STRUCTURE.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {
                key: row.get(key) for key in (
                    "epsilon", "xi_index", "endpoint_kind", "status", "timings",
                    "compatibility_root_count", "candidate_root_count",
                    "source_point_count", "route_point_count",
                    "compatible_source_point_count", "boundary_rows",
                    "target_boundary_rows", "no_lift_rows", "unresolved",
                    "source_excluded",
                )
            }
            for row in rows
        ],
    }, sort_keys=True))
