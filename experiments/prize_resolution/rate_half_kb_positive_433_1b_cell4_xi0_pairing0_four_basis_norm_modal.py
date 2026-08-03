#!/usr/bin/env python3
"""Evaluate cell-4 xi0/pairing0 in the exact four-basis common algebra."""

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
    "rate_half_kb_positive_433_1b_cell4_xi0_pairing0_four_basis_norm_result.json"
)
REMOTE_STRUCTURE = "/root/structure.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell4-xi0-pairing0-four-basis")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0", "python-flint==0.8.0")
    .add_local_file(STRUCTURE, REMOTE_STRUCTURE)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=300, max_containers=4)
def evaluate_case(signs):
    import re

    from flint import fmpz_mod_poly_ctx
    import sympy as sp

    started = time.perf_counter()
    epsilon_1, epsilon_2 = signs
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

    base_field = sp.GF(PRIME).frac_field(r)
    zero = base_field.zero
    one = base_field.one
    inverse_guards = []

    def field_value(expression):
        polynomial = sp.Poly(expression, r, modulus=PRIME)
        return base_field.from_sympy(polynomial.as_expr())

    def field_equal(left, right):
        left = base_field.convert(left)
        right = base_field.convert(right)
        return left.numer * right.denom == right.numer * left.denom

    def field_is_zero(value):
        return base_field.convert(value).numer == zero.numer

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

    def paired(left, right):
        p0, p1, p2 = (
            b_value - left * a_value
            for a_value, b_value in zip(a_coefficients, b_coefficients)
        )
        q0 = b_coefficients[0] - right * a_coefficients[0]
        q1 = -b_coefficients[1] + right * a_coefficients[1]
        q2 = b_coefficients[2] - right * a_coefficients[2]
        return (p2 * q0 - p0 * q2)**2 - (
            p2 * q1 - p1 * q2
        ) * (p1 * q0 - p0 * q1)

    target_free = paired(missing_record, -missing_record)
    cut_seconds = time.perf_counter() - started
    target_norm = target_free.norm()
    norm_seconds = time.perf_counter() - started

    polynomial_context = fmpz_mod_poly_ctx(PRIME)

    def flint_polynomial(polynomial):
        coefficients = {
            exponents[0]: int(coefficient) % PRIME
            for exponents, coefficient in polynomial.terms()
        }
        maximum = max(coefficients, default=0)
        return polynomial_context([
            coefficients.get(exponent, 0) for exponent in range(maximum + 1)
        ])

    def field_roots(polynomial):
        value = flint_polynomial(polynomial)
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

    def polynomial_profile(polynomial):
        terms = polynomial.terms()
        degree = max((exponents[0] for exponents, _ in terms), default=-1)
        text = str(polynomial.as_expr())
        return {
            "degree": degree,
            "terms": len(terms),
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
            "expression": text,
        }

    def fraction_profile(value):
        return {
            "numerator": polynomial_profile(value.numer),
            "denominator": polynomial_profile(value.denom),
        }

    guard_values = []
    seen_guards = set()
    for name, guard in inverse_guards:
        key = (str(guard.numer.as_expr()), str(guard.denom.as_expr()))
        if key in seen_guards:
            continue
        seen_guards.add(key)
        guard_values.append((f"{name}_{len(guard_values)}", guard))

    target_roots = field_roots(target_norm.numer)
    candidate_roots = set(target_roots or [])
    all_field_roots = False
    for _, guard in [*guard_values, ("target_norm", target_norm)]:
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
    witnesses = []
    unresolved = []
    boundary_rows = []
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

                def paired_scalar(left, right):
                    p0, p1, p2 = (
                        (b_value - left * a_value) % PRIME
                        for a_value, b_value in zip(a_values, b_values)
                    )
                    q0 = (b_values[0] - right * a_values[0]) % PRIME
                    q1 = (-b_values[1] + right * a_values[1]) % PRIME
                    q2 = (b_values[2] - right * a_values[2]) % PRIME
                    return (
                        pow((p2*q0 - p0*q2) % PRIME, 2, PRIME)
                        - ((p2*q1 - p1*q2) % PRIME)
                        * ((p1*q0 - p0*q1) % PRIME)
                    ) % PRIME

                cut_value = paired_scalar(missing, -missing % PRIME)
                status = "TARGET_FREE_ZERO" if cut_value == 0 else "NONZERO"
                row = {**point, "missing": missing, "cut": cut_value,
                       "status": status}
                finite_rows.append(row)
                if cut_value == 0:
                    witnesses.append(row)

    if all_field_roots:
        unresolved.append({"reason": "IDENTICALLY_ZERO_ROOT_POLYNOMIAL"})
    replay_seconds = time.perf_counter() - started
    return {
        "epsilon": [epsilon_1, epsilon_2],
        "status": "COMPLETE",
        "timings": {
            "algebra": algebra_seconds,
            "kernel": kernel_seconds - algebra_seconds,
            "target_free": cut_seconds - kernel_seconds,
            "norm": norm_seconds - cut_seconds,
            "replay": replay_seconds - norm_seconds,
            "total": replay_seconds,
        },
        "base_relation": str(base_expression),
        "b_relation": str(b_expression),
        "c_relation": str(c_expression),
        "target_free_profiles": [
            fraction_profile(value) for value in target_free.vector()
        ],
        "target_norm": fraction_profile(target_norm),
        "target_root_count": None if target_roots is None else len(target_roots),
        "target_roots": target_roots,
        "candidate_root_count": len(candidate_roots),
        "candidate_roots": sorted(candidate_roots),
        "source_point_count": source_point_count,
        "route_point_count": route_point_count,
        "boundary_rows": boundary_rows,
        "finite_rows": finite_rows,
        "witnesses": witnesses,
        "unresolved": unresolved,
        "excluded": not witnesses and not unresolved,
        "inverse_guards": [
            {"name": name, **fraction_profile(value)}
            for name, value in guard_values
        ],
    }


@app.local_entrypoint()
def main(signs: str = "-1:-1,-1:1,1:-1,1:1"):
    cases = tuple(
        tuple(int(value) for value in pair.split(":"))
        for pair in signs.split(",") if pair
    )
    raw = list(evaluate_case.map(
        cases, order_outputs=True, return_exceptions=True
    ))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case),
                "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell4-xi0-pairing0-four-basis-v1",
        "field": PRIME,
        "scope": (
            "Exact four-basis norm and direct finite replay for cell 4, "
            "xi0, pairing0; no other pairing or full-cell claim."
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
                    "epsilon", "status", "timings", "target_norm",
                    "target_root_count", "candidate_root_count", "candidate_roots",
                    "source_point_count", "route_point_count",
                    "boundary_rows", "witnesses", "unresolved", "excluded",
                )
            }
            for row in rows
        ],
    }, sort_keys=True))
