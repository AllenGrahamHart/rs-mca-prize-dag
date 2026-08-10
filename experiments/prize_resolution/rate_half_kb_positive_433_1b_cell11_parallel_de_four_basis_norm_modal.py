#!/usr/bin/env python3
"""Compute four-basis norms for the two cell-11 parallel-DE source cuts."""

import hashlib
import json
from pathlib import Path
import time

import modal


DIRECTORY = Path(__file__).parent
TOWER = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_four_basis_tower_result.json"
)
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_parallel_de_four_basis_norm_result.json"
)
REMOTE_TOWER = "/root/tower.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell11-parallel-de-four-basis")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0", "python-flint==0.8.0")
    .add_local_file(TOWER, REMOTE_TOWER)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=300, max_containers=8)
def evaluate(case):
    from flint import fmpz_mod_poly_ctx
    import sympy as sp

    started = time.perf_counter()
    epsilon_1, epsilon_2, cut_kind = case
    t, r, c, b = sp.symbols("t r c b")
    tower = json.loads(Path(REMOTE_TOWER).read_text())
    row = next(
        item for item in tower["rows"]
        if item["epsilon"] == [epsilon_1, epsilon_2]
        and item["c_row_index"] == 5
    )
    base_expression = sp.sympify(row["base"]["expression"])
    b_expression = sp.sympify(row["b_relation"]["expression"])
    c_expression = sp.sympify(row["c_relation"]["expression"])
    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    kernel_row = next(
        item for item in kernel_payload["rows"]
        if item["epsilon"] == [epsilon_1, epsilon_2]
    )
    kernel_expressions = tuple(
        sp.sympify(item["expression"]) for item in kernel_row["kernel"]
    )

    field = sp.GF(PRIME).frac_field(r)
    inverse_guards = []

    def field_value(expression):
        polynomial = sp.Poly(expression, r, modulus=PRIME)
        return field.from_sympy(polynomial.as_expr())

    def field_equal(left, right):
        left, right = field.convert(left), field.convert(right)
        return left.numer*right.denom == right.numer*left.denom

    base_coefficients = [
        field_value(value) for value in sp.Poly(base_expression, t).all_coeffs()
    ]
    if len(base_coefficients) != 3:
        raise RuntimeError("nonquadratic t relation")
    base_leading, base_linear, base_constant = base_coefficients
    t_u, t_v = -base_linear/base_leading, -base_constant/base_leading
    inverse_guards.append(("base_leading", base_leading))

    class Quad:
        __slots__ = ("constant", "linear")

        def __init__(self, constant=0, linear=0):
            self.constant = field.convert(constant)
            self.linear = field.convert(linear)

        @staticmethod
        def coerce(value):
            return value if isinstance(value, Quad) else Quad(value)

        def __add__(self, other):
            other = Quad.coerce(other)
            return Quad(self.constant+other.constant, self.linear+other.linear)

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
                self.constant*other.constant+self.linear*other.linear*t_v,
                self.constant*other.linear+self.linear*other.constant
                + self.linear*other.linear*t_u,
            )

        __rmul__ = __mul__

        def __pow__(self, exponent):
            output, base, power = Quad(1), self, exponent
            if power < 0:
                return self.inverse() ** (-power)
            while power:
                if power & 1:
                    output = output*base
                base, power = base*base, power//2
            return output

        def norm(self):
            return (self.constant*(self.constant+self.linear*t_u)
                    - self.linear*self.linear*t_v)

        def inverse(self):
            determinant = self.norm()
            inverse_guards.append(("quad_inverse", determinant))
            return Quad((self.constant+self.linear*t_u)/determinant,
                        -self.linear/determinant)

        def __truediv__(self, other):
            return self*Quad.coerce(other).inverse()

        def __eq__(self, other):
            other = Quad.coerce(other)
            return field_equal(self.constant, other.constant) and field_equal(
                self.linear, other.linear
            )

        def vector(self):
            return self.constant, self.linear

    common_t = Quad(0, 1)
    if common_t*common_t != Quad(t_v, t_u):
        raise RuntimeError("t relation self-check")

    def quad_expression(expression):
        output = Quad()
        for (t_degree, r_degree), coefficient in sp.Poly(
            expression, t, r, modulus=PRIME
        ).terms():
            output += field_value(int(coefficient)*r**r_degree)*common_t**t_degree
        return output

    b_coefficients = sp.Poly(b_expression, b).all_coeffs()
    if len(b_coefficients) != 3:
        raise RuntimeError("nonquadratic b relation")
    b_leading, b_linear, b_constant = map(quad_expression, b_coefficients)
    b_u, b_v = -b_linear/b_leading, -b_constant/b_leading

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
            return Pair(self.constant+other.constant, self.linear+other.linear)

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
                self.constant*other.constant+self.linear*other.linear*b_v,
                self.constant*other.linear+self.linear*other.constant
                + self.linear*other.linear*b_u,
            )

        __rmul__ = __mul__

        def __pow__(self, exponent):
            output, base, power = Pair(1), self, exponent
            if power < 0:
                return self.inverse() ** (-power)
            while power:
                if power & 1:
                    output = output*base
                base, power = base*base, power//2
            return output

        def pair_norm(self):
            return (self.constant*(self.constant+self.linear*b_u)
                    - self.linear*self.linear*b_v)

        def norm(self):
            return self.pair_norm().norm()

        def inverse(self):
            determinant = self.pair_norm()
            determinant_inverse = determinant.inverse()
            return Pair((self.constant+self.linear*b_u)*determinant_inverse,
                        -self.linear*determinant_inverse)

        def __truediv__(self, other):
            return self*Pair.coerce(other).inverse()

        def vector(self):
            return (*self.constant.vector(), *self.linear.vector())

        def __eq__(self, other):
            other = Pair.coerce(other)
            return (self.constant == other.constant
                    and self.linear == other.linear)

    common_b = Pair(0, 1)
    if common_b*common_b != Pair(b_v, b_u):
        raise RuntimeError("b relation self-check")

    def pair_expression(expression):
        output = Pair()
        for (b_degree, t_degree, r_degree), coefficient in sp.Poly(
            expression, b, t, r, modulus=PRIME
        ).terms():
            output += Pair(field_value(int(coefficient)*r**r_degree)
                           * common_t**t_degree)*common_b**b_degree
        return output

    c_coefficients = sp.Poly(c_expression, c).all_coeffs()
    if len(c_coefficients) != 2:
        raise RuntimeError("nonlinear c relation")
    c_leading, c_constant = map(pair_expression, c_coefficients)
    common_c = -c_constant/c_leading
    if c_leading*common_c+c_constant != Pair():
        raise RuntimeError("c relation self-check")

    def tower_expression(expression):
        output = Pair()
        for exponents, coefficient in sp.Poly(
            expression, c, b, t, r, modulus=PRIME
        ).terms():
            c_degree, b_degree, t_degree, r_degree = exponents
            output += (Pair(field_value(int(coefficient)*r**r_degree)
                            * common_t**t_degree)
                       * common_b**b_degree * common_c**c_degree)
        return output

    algebra_seconds = time.perf_counter()-started
    kernel = tuple(tower_expression(value) for value in kernel_expressions)
    kernel_seconds = time.perf_counter()-started
    a_coefficients, b_coefficients = kernel[:3], kernel[3:6]

    def polynomial_value(coefficients, value):
        return sum(coefficient*value**index
                   for index, coefficient in enumerate(coefficients))

    missing_label = -Pair(common_t*common_t)
    missing = (polynomial_value(b_coefficients, missing_label)
               / polynomial_value(a_coefficients, missing_label))

    def paired(left, right):
        p0, p1, p2 = (
            b_value-left*a_value
            for a_value, b_value in zip(a_coefficients, b_coefficients)
        )
        q0 = b_coefficients[0]-right*a_coefficients[0]
        q1 = -b_coefficients[1]+right*a_coefficients[1]
        q2 = b_coefficients[2]-right*a_coefficients[2]
        return ((p2*q0-p0*q2)**2
                - (p2*q1-p1*q2)*(p1*q0-p0*q1))

    target_free = (
        paired(missing, -missing)
        if cut_kind == "opposite" else paired(-missing, -missing)
    )
    cut_seconds = time.perf_counter()-started
    target_norm = target_free.norm()
    norm_seconds = time.perf_counter()-started

    context = fmpz_mod_poly_ctx(PRIME)

    def flint_polynomial(polynomial):
        coefficients = {
            exponents[0]: int(coefficient) % PRIME
            for exponents, coefficient in polynomial.terms()
        }
        return context([coefficients.get(index, 0)
                        for index in range(max(coefficients, default=0)+1)])

    def field_roots(polynomial):
        value = flint_polynomial(polynomial)
        if value.is_zero():
            return None
        if int(value.degree()) == 0:
            return []
        variable = context([0, 1])
        root_part = value.gcd(pow(variable, PRIME, value)-variable)
        _, factors = root_part.factor()
        roots = []
        for factor, _ in factors:
            if int(factor.degree()) != 1:
                raise RuntimeError("nonlinear factor in field-root part")
            roots.append(-int(factor[0])*pow(int(factor[1]), -1, PRIME) % PRIME)
        return sorted(set(roots))

    def polynomial_profile(polynomial):
        terms = polynomial.terms()
        text = str(polynomial.as_expr())
        return {
            "degree": max((item[0][0] for item in terms), default=-1),
            "terms": len(terms),
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
            "expression": text,
        }

    def fraction_profile(value):
        return {"numerator": polynomial_profile(value.numer),
                "denominator": polynomial_profile(value.denom)}

    roots = field_roots(target_norm.numer)
    guard_roots = set()
    guard_profiles = []
    seen = set()
    for name, guard in inverse_guards:
        key = (str(guard.numer.as_expr()), str(guard.denom.as_expr()))
        if key in seen:
            continue
        seen.add(key)
        guard_profiles.append({"name": name, **fraction_profile(guard)})
        for polynomial in (guard.numer, guard.denom):
            values = field_roots(polynomial)
            if values is not None:
                guard_roots.update(values)
    finished = time.perf_counter()
    return {
        "epsilon": [epsilon_1, epsilon_2], "cut_kind": cut_kind,
        "status": "COMPLETE",
        "timings": {
            "algebra": algebra_seconds,
            "kernel": kernel_seconds-algebra_seconds,
            "cut": cut_seconds-kernel_seconds,
            "norm": norm_seconds-cut_seconds,
            "roots": finished-norm_seconds-started,
            "total": finished-started,
        },
        "target_free_profiles": [fraction_profile(value)
                                 for value in target_free.vector()],
        "target_norm": fraction_profile(target_norm),
        "t_reduction": {
            "constant": fraction_profile(t_v),
            "linear": fraction_profile(t_u),
        },
        "b_reduction": {
            "constant": [fraction_profile(value) for value in b_v.vector()],
            "linear": [fraction_profile(value) for value in b_u.vector()],
        },
        "target_roots": roots,
        "target_root_count": None if roots is None else len(roots),
        "guard_root_count": len(guard_roots),
        "candidate_roots": sorted(set(roots or []) | guard_roots),
        "inverse_guards": guard_profiles,
    }


@app.local_entrypoint()
def main(limit: int = 0):
    cases = tuple(
        (epsilon_1, epsilon_2, cut_kind)
        for epsilon_1 in (-1, 1) for epsilon_2 in (-1, 1)
        for cut_kind in ("opposite", "equal_negative")
    )
    if limit:
        cases = cases[:limit]
    raw = list(evaluate.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]), "cut_kind": case[2],
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            rows.append(row)
    certificate_rows = []
    for row in rows:
        certificate = dict(row)
        certificate.pop("timings", None)
        certificate_rows.append(certificate)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell11-parallel-de-four-basis-v1",
        "field": PRIME,
        "scope": (
            "Exact four-basis norms for the cell-11 first-pair parallel-DE "
            "source cuts; candidate routing only until direct tower replay."
        ),
        "source_tower_sha256": hashlib.sha256(TOWER.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "rows": certificate_rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [{key: row.get(key) for key in (
            "epsilon", "cut_kind", "status", "timings",
            "target_root_count", "guard_root_count", "candidate_roots",
        )} | {
            "target_norm": {
                side: {key: row.get("target_norm", {}).get(side, {}).get(key)
                       for key in ("degree", "terms", "sha256")}
                for side in ("numerator", "denominator")
            }
        } for row in rows],
    }, sort_keys=True))
