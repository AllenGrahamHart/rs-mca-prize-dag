#!/usr/bin/env python3
"""Profile or eliminate final cell-14 rank-one charts after torus substitution."""

import base64
import hashlib
import json
from pathlib import Path
import time
import zlib

import modal


DIRECTORY = Path(__file__).parent
CURVE = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_curve_kernel_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_flint_profile_result.json"
REMOTE_CURVE = "/root/curve.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell14-fixed-a-rankone-flint-profile")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0", "python-flint==0.8.0")
    .add_local_file(CURVE, REMOTE_CURVE)
)


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        rest = values[1:index]+values[index+1:]
        for tail in pairings(rest):
            yield ((first, values[index]),)+tail


@app.function(image=image, cpu=1.0, memory=1024, timeout=360, max_containers=16)
def profile_case(case):
    import sympy as sp
    from flint import fmpz_mod_mpoly_ctx

    started = time.perf_counter()
    timings = {}

    def mark(name):
        timings[name] = round(time.perf_counter()-started, 3)

    epsilon_1, epsilon_2, sigma_c, sigma_o, xi_index, pairing_index, mode = case
    payload = json.loads(Path(REMOTE_CURVE).read_text())
    source = next(
        row for row in payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    )
    r, b, u, v, f = sp.symbols("r b u v f")

    def expression(summary):
        return sp.sympify(summary["expression"])

    relation = sp.Poly(expression(source["relation_rb"]), b)
    coefficient_a, coefficient_b, coefficient_c = relation.all_coeffs()
    base_field = sp.GF(PRIME).frac_field(r)
    coefficient_a = base_field.from_sympy(coefficient_a)
    coefficient_b = base_field.from_sympy(coefficient_b)
    coefficient_c = base_field.from_sympy(coefficient_c)
    base_polynomial_ring = coefficient_a.numer.ring
    quotient_u = -coefficient_b/coefficient_a
    quotient_v = -coefficient_c/coefficient_a
    inverse_guards = [coefficient_a]

    class CommonPair:
        __slots__ = ("constant", "linear")

        def __init__(self, constant=0, linear=0):
            self.constant = base_field.convert(constant)
            self.linear = base_field.convert(linear)

        @staticmethod
        def coerce(value):
            return value if isinstance(value, CommonPair) else CommonPair(value)

        def __add__(self, other):
            other = CommonPair.coerce(other)
            return CommonPair(self.constant+other.constant, self.linear+other.linear)

        __radd__ = __add__

        def __neg__(self):
            return CommonPair(-self.constant, -self.linear)

        def __sub__(self, other):
            return self+(-CommonPair.coerce(other))

        def __rsub__(self, other):
            return CommonPair.coerce(other)-self

        def __mul__(self, other):
            other = CommonPair.coerce(other)
            return CommonPair(
                self.constant*other.constant+self.linear*other.linear*quotient_v,
                self.constant*other.linear+self.linear*other.constant
                + self.linear*other.linear*quotient_u,
            )

        __rmul__ = __mul__

        def __pow__(self, exponent):
            if exponent < 0:
                return self.inverse()**(-exponent)
            result = CommonPair(1)
            base = self
            while exponent:
                if exponent & 1:
                    result = result*base
                base = base*base
                exponent //= 2
            return result

        def inverse(self):
            determinant = (
                self.constant*(self.constant+self.linear*quotient_u)
                - self.linear*self.linear*quotient_v
            )
            inverse_guards.append(determinant)
            return CommonPair(
                (self.constant+self.linear*quotient_u)/determinant,
                -self.linear/determinant,
            )

        def __truediv__(self, other):
            return self*CommonPair.coerce(other).inverse()

    common_b = CommonPair(0, 1)

    def polynomial_pair(value):
        result = CommonPair()
        for coefficient in sp.Poly(sp.expand(value), b).all_coeffs():
            result = result*common_b+CommonPair(coefficient)
        return result

    def rational_pair(summary):
        return polynomial_pair(expression(summary["numerator"])) / polynomial_pair(
            expression(summary["denominator"])
        )

    t_pair = rational_pair(source["t_map"])
    c_pair = rational_pair(source["c_map"])
    kernel = [polynomial_pair(expression(value)) for value in source["kernel"]]
    a_coefficients = kernel[:3]
    b_coefficients = kernel[3:6]
    beta_0, beta_1 = kernel[6:]

    def evaluate(coefficients, value):
        return coefficients[0]+coefficients[1]*value+coefficients[2]*value**2

    missing_label = -(t_pair*t_pair)
    a_missing = evaluate(a_coefficients, missing_label)
    b_missing = evaluate(b_coefficients, missing_label)
    missing_record = b_missing/a_missing
    if xi_index not in (0, 1, 2):
        raise ValueError("fixed-a profile requires a missing de record")
    fixed_a = (missing_record, missing_record, -missing_record)[xi_index]
    mark("common")

    target_ring = base_field.poly_ring(u, v, f)
    ring_u, ring_v, ring_f = target_ring.gens

    def target_convert(value):
        if getattr(value, "ring", None) is target_ring.ring:
            return value
        if hasattr(value, "parent") and value.parent() == base_field:
            return target_ring.ring.ground_new(value)
        return target_ring.convert(value)

    target_quotient_u = target_convert(quotient_u)
    target_quotient_v = target_convert(quotient_v)

    class TargetPair:
        __slots__ = ("constant", "linear")

        def __init__(self, constant=0, linear=0):
            self.constant = target_convert(constant)
            self.linear = target_convert(linear)

        @staticmethod
        def coerce(value):
            return value if isinstance(value, TargetPair) else TargetPair(value)

        def __add__(self, other):
            other = TargetPair.coerce(other)
            return TargetPair(self.constant+other.constant, self.linear+other.linear)

        __radd__ = __add__

        def __neg__(self):
            return TargetPair(-self.constant, -self.linear)

        def __sub__(self, other):
            return self+(-TargetPair.coerce(other))

        def __rsub__(self, other):
            return TargetPair.coerce(other)-self

        def __mul__(self, other):
            other = TargetPair.coerce(other)
            return TargetPair(
                self.constant*other.constant
                + self.linear*other.linear*target_quotient_v,
                self.constant*other.linear+self.linear*other.constant
                + self.linear*other.linear*target_quotient_u,
            )

        __rmul__ = __mul__

        def __pow__(self, exponent):
            result = TargetPair(1)
            base = self
            while exponent:
                if exponent & 1:
                    result = result*base
                base = base*base
                exponent //= 2
            return result

    def lift(value):
        return TargetPair(value.constant, value.linear)

    a_pair = lift(fixed_a)
    u_pair, v_pair, f_pair = TargetPair(ring_u), TargetPair(ring_v), TargetPair(ring_f)
    b_pair, c_target = lift(common_b), lift(c_pair)
    lifted_a = tuple(lift(value) for value in a_coefficients)
    lifted_b = tuple(lift(value) for value in b_coefficients)
    lifted_beta_0, lifted_beta_1 = lift(beta_0), lift(beta_1)
    lifted_missing_label, lifted_a_missing = lift(missing_label), lift(a_missing)
    records = (
        a_pair, a_pair, -a_pair, u_pair, sigma_o*v_pair,
        b_pair*f_pair, sigma_c*c_target*f_pair,
    )
    sum_numerators = (
        (u_pair+v_pair)**2, (u_pair+v_pair)**2, (u_pair-v_pair)**2,
        (u_pair+f_pair*f_pair)**2,
        (v_pair+sigma_o*f_pair*f_pair)**2,
        (b_pair+f_pair)**2, (c_target+sigma_c*f_pair)**2,
    )
    sum_denominators = (
        f_pair*f_pair, f_pair*f_pair, f_pair*f_pair,
        f_pair*f_pair, f_pair*f_pair, TargetPair(1), TargetPair(1),
    )

    def paired(left, right):
        p0, p1, p2 = (
            b_value-left*a_value
            for a_value, b_value in zip(lifted_a, lifted_b)
        )
        q0 = lifted_b[0]-right*lifted_a[0]
        q1 = -lifted_b[1]+right*lifted_a[1]
        q2 = lifted_b[2]-right*lifted_a[2]
        return (p2*q0-p0*q2)**2-(p2*q1-p1*q2)*(p1*q0-p0*q1)

    residual = tuple(index for index in range(7) if index != xi_index)
    matching = tuple(pairings(range(6)))[pairing_index]
    equations = [a_pair*f_pair*f_pair-u_pair*v_pair]
    equations.extend(
        paired(records[residual[left]], records[residual[right]])
        for left, right in matching
    )
    equations.append(
        sum_denominators[xi_index]
        * lifted_missing_label*(lifted_beta_0+lifted_beta_1*lifted_missing_label)**2
        - sum_numerators[xi_index]*lifted_a_missing**2
    )
    mark("ordinary_equations")

    def add_coefficient(output, key, value):
        output[key] = output.get(key, base_field.zero)+value
        if output[key] == 0:
            del output[key]

    def torus_map(equation):
        output = ({}, {})
        powers = {0: CommonPair(1)}
        for b_exponent, polynomial in enumerate(
            (equation.constant, equation.linear)
        ):
            for (u_exponent, v_exponent, f_exponent), coefficient in polynomial.terms():
                if v_exponent not in powers:
                    powers[v_exponent] = fixed_a**v_exponent
                scalar = CommonPair(coefficient)*powers[v_exponent]
                if b_exponent:
                    scalar = scalar*common_b
                key = (u_exponent-v_exponent, f_exponent+2*v_exponent)
                add_coefficient(output[0], key, scalar.constant)
                add_coefficient(output[1], key, scalar.linear)
        exponents = [key[0] for component in output for key in component]
        shift = min(exponents, default=0)
        return tuple(
            {(key[0]-shift, key[1]): value for key, value in component.items()}
            for component in output
        ), shift

    mapped = [torus_map(equation) for equation in equations]
    mark("torus_map")
    candidates = [
        (len(pair[0])+len(pair[1]), index)
        for index, (pair, _) in enumerate(mapped) if pair[1]
    ]
    if not candidates:
        raise ValueError("no b-linear cutter")
    _, cutter_index = min(candidates)

    flint_context = fmpz_mod_mpoly_ctx.get(["z", "f", "r"], PRIME)

    def flint_pair(pair):
        denominator = base_polynomial_ring.one
        for component in pair:
            for coefficient in component.values():
                denominator = denominator.lcm(coefficient.denom)

        def convert(component):
            output = {}
            for (z_exponent, f_exponent), coefficient in component.items():
                multiplier = denominator.exquo(coefficient.denom)
                numerator = coefficient.numer*multiplier
                for (r_exponent,), scalar in numerator.terms():
                    key = (z_exponent, f_exponent, r_exponent)
                    output[key] = (output.get(key, 0)+int(scalar)) % PRIME
            return flint_context.from_dict({
                key: value for key, value in output.items() if value
            })

        return convert(pair[0]), convert(pair[1]), denominator

    flint_pairs = [flint_pair(pair) for pair, _ in mapped]
    cutter_constant, cutter_linear, _ = flint_pairs[cutter_index]
    components = [
        constant*cutter_linear-linear*cutter_constant
        for index, (constant, linear, _) in enumerate(flint_pairs)
        if index != cutter_index
    ]

    curve_denominator = base_polynomial_ring.one
    for coefficient in (coefficient_a, coefficient_b, coefficient_c):
        curve_denominator = curve_denominator.lcm(coefficient.denom)

    def flint_base(value):
        multiplier = curve_denominator.exquo(value.denom)
        polynomial = value.numer*multiplier
        return flint_context.from_dict({
            (0, 0, exponent[0]): int(coefficient) % PRIME
            for exponent, coefficient in polynomial.terms()
        })

    components.append(
        flint_base(coefficient_a)*cutter_constant*cutter_constant
        - flint_base(coefficient_b)*cutter_constant*cutter_linear
        + flint_base(coefficient_c)*cutter_linear*cutter_linear
    )
    mark("flint_projection")

    def profile(value):
        if not value:
            return {"zero": True, "terms": 0, "active_variables": []}
        support = {
            (int(term[0][0]), int(term[0][1])) for term in value.terms()
        }
        minima = tuple(min(row[index] for row in support) for index in range(2))
        normalized = tuple(
            (row[0]-minima[0], row[1]-minima[1]) for row in support
        )
        maxima = tuple(max(row[index] for row in normalized) for index in range(2))
        return {
            "zero": False,
            "terms": len(support),
            "monomial_shift": list(minima),
            "degrees": list(maxima),
            "active_variables": [
                name for name, degree in zip(("z", "f"), maxima) if degree
            ],
        }

    profiles = [profile(value) for value in components]
    mark("profile")
    row = {
        "epsilon": [epsilon_1, epsilon_2],
        "sigma": [sigma_c, sigma_o],
        "xi_index": xi_index,
        "pairing_index": pairing_index,
        "mode": mode,
        "status": "COMPLETE",
        "unit": False,
        "matching": [list(value) for value in matching],
        "cutter_index": cutter_index,
        "equation_zero": [not pair[0] and not pair[1] for pair, _ in mapped],
        "equation_shifts": [int(shift) for _, shift in mapped],
        "component_profiles": profiles,
        "targetfree_components": [
            index for index, value in enumerate(profiles)
            if not value["zero"] and not value["active_variables"]
        ],
        "univariate_components": [
            index for index, value in enumerate(profiles)
            if len(value["active_variables"]) == 1
        ],
        "equation_denominator_degrees": [
            int(denominator.degree()) for _, _, denominator in flint_pairs
        ],
        "curve_denominator_degree": int(curve_denominator.degree()),
        "timings_seconds": timings,
    }
    if mode == "profile":
        return row
    if mode != "chain":
        raise ValueError("unsupported mode")

    def torus_normalize(value):
        if not value:
            return value
        terms = value.to_dict()
        minimum_z = min(exponents[0] for exponents in terms)
        minimum_f = min(exponents[1] for exponents in terms)
        return flint_context.from_dict({
            (
                exponents[0]-minimum_z,
                exponents[1]-minimum_f,
                exponents[2],
            ): int(coefficient)
            for exponents, coefficient in terms.items()
        })

    normalized_components = [torus_normalize(value) for value in components]
    univariate_indices = [
        index for index, value in enumerate(profiles)
        if len(value["active_variables"]) == 1
    ]
    mixed_indices = [
        index for index, value in enumerate(profiles)
        if set(value["active_variables"]) == {"z", "f"}
    ]
    if not univariate_indices or len(mixed_indices) < 2:
        row["status"] = "NO_CHAIN"
        return row
    univariate_index = min(
        univariate_indices,
        key=lambda index: (
            sum(profiles[index]["degrees"]), profiles[index]["terms"]
        ),
    )
    outer_variable = profiles[univariate_index]["active_variables"][0]
    inner_variable = "f" if outer_variable == "z" else "z"
    variable_index = {"z": 0, "f": 1}
    inner_candidates = []
    for left_index in range(len(mixed_indices)):
        for right_index in range(left_index+1, len(mixed_indices)):
            left = mixed_indices[left_index]
            right = mixed_indices[right_index]
            resultant = normalized_components[left].resultant(
                normalized_components[right], inner_variable
            )
            if not resultant:
                continue
            if int(resultant.degrees()[variable_index[inner_variable]]) != 0:
                raise ValueError("inner variable survived resultant")
            inner_candidates.append((
                int(resultant.total_degree()),
                len(list(resultant.terms())),
                left,
                right,
                resultant,
            ))
    if not inner_candidates:
        row["status"] = "ZERO_INNER_RESULTANTS"
        return row
    selected = None
    for candidate in sorted(inner_candidates, key=lambda value: value[:2]):
        outer = candidate[-1].resultant(
            normalized_components[univariate_index], outer_variable
        )
        if outer:
            selected = (*candidate, outer)
            break
    if selected is None:
        row["status"] = "ZERO_OUTER_RESULTANTS"
        return row
    _, _, left_index, right_index, inner, outer = selected
    degrees = [int(value) for value in outer.degrees()]
    if degrees[0] or degrees[1]:
        raise ValueError("target variable survived outer resultant")

    from flint import fmpz_mod_poly_ctx

    polynomial_context = fmpz_mod_poly_ctx(PRIME)
    coefficients = {
        exponents[2]: int(coefficient)
        for exponents, coefficient in outer.to_dict().items()
    }
    outer_polynomial = polynomial_context([
        coefficients.get(exponent, 0)
        for exponent in range(max(coefficients, default=0)+1)
    ])
    parameter = polynomial_context([0, 1])
    field_gcd = outer_polynomial.gcd(
        pow(parameter, PRIME, outer_polynomial)-parameter
    )
    _, factors = field_gcd.factor()
    roots = []
    for factor, _ in factors:
        if int(factor.degree()) != 1:
            raise ValueError("field-root gcd has a nonlinear factor")
        roots.append(
            -int(factor[0])*pow(int(factor[1]), -1, PRIME) % PRIME
        )
    roots.sort()

    def evaluate_base_polynomial(polynomial, value):
        return sum(
            int(coefficient)*pow(value, exponent[0], PRIME)
            for exponent, coefficient in polynomial.terms()
        ) % PRIME

    def evaluate_fraction(value, r_value):
        denominator = evaluate_base_polynomial(value.denom, r_value)
        if denominator == 0:
            return None
        return (
            evaluate_base_polynomial(value.numer, r_value)
            * pow(denominator, -1, PRIME)
        ) % PRIME

    def polynomial_field_roots(polynomial):
        if polynomial.is_zero():
            return None
        if int(polynomial.degree()) == 0:
            return []
        root_polynomial = polynomial.gcd(
            pow(parameter, PRIME, polynomial)-parameter
        )
        _, root_factors = root_polynomial.factor()
        values = []
        for root_factor, _ in root_factors:
            if int(root_factor.degree()) != 1:
                raise ValueError("fiber root gcd has a nonlinear factor")
            values.append(
                -int(root_factor[0])
                * pow(int(root_factor[1]), -1, PRIME)
                % PRIME
            )
        return sorted(values)

    target_index = {"z": 0, "f": 1}

    def specialize_component(
        component, free_variable, assignments, r_value
    ):
        free_index = target_index[free_variable]
        output = {}
        for exponents, coefficient in component.to_dict().items():
            scalar = int(coefficient)*pow(r_value, exponents[2], PRIME) % PRIME
            for name, index in target_index.items():
                exponent = exponents[index]
                if not exponent or index == free_index:
                    continue
                if name not in assignments:
                    raise ValueError("missing target specialization")
                scalar = scalar*pow(assignments[name], exponent, PRIME) % PRIME
            exponent = exponents[free_index]
            output[exponent] = (output.get(exponent, 0)+scalar) % PRIME
        return polynomial_context([
            output.get(exponent, 0)
            for exponent in range(max(output, default=0)+1)
        ])

    def evaluate_univariate(polynomial, value):
        return sum(
            int(polynomial[index])*pow(value, index, PRIME)
            for index in range(int(polynomial.degree())+1)
        ) % PRIME

    def curve_at_r(r_value):
        values = [
            evaluate_fraction(coefficient, r_value)
            for coefficient in (coefficient_a, coefficient_b, coefficient_c)
        ]
        return None if any(value is None for value in values) else values

    def direct_outer_fiber(r_value, outer_value):
        if outer_value == 0:
            return {
                "status": "CHECKED",
                "target_boundary": outer_variable,
                "solutions": [],
            }
        assignments = {outer_variable: outer_value}
        equation_pairs = []
        for constant, linear, _ in flint_pairs:
            constant_specialized = specialize_component(
                constant, inner_variable, assignments, r_value
            )
            linear_specialized = specialize_component(
                linear, inner_variable, assignments, r_value
            )
            if (
                not constant_specialized.is_zero()
                or not linear_specialized.is_zero()
            ):
                equation_pairs.append((constant_specialized, linear_specialized))
        curve_values = curve_at_r(r_value)
        if curve_values is None:
            return {"status": "CURVE_BOUNDARY"}
        curve_a, curve_b, curve_c = curve_values
        cuts = [
            curve_a*constant*constant
            - curve_b*constant*linear
            + curve_c*linear*linear
            for constant, linear in equation_pairs
        ]
        cuts.extend(
            left[0]*right[1]-left[1]*right[0]
            for left_index, left in enumerate(equation_pairs)
            for right in equation_pairs[left_index+1:]
        )
        cuts = [value for value in cuts if not value.is_zero()]
        if not cuts:
            return {"status": "NO_INNER_CUT"}
        common_inner = cuts[0]
        for value in cuts[1:]:
            common_inner = common_inner.gcd(value)
        inner_roots = polynomial_field_roots(common_inner)
        solutions = []
        target_boundaries = []
        for inner_value in inner_roots:
            if inner_value == 0:
                target_boundaries.append({inner_variable: 0})
                continue
            b_polynomials = [
                polynomial_context([curve_c, curve_b, curve_a])
            ]
            for constant, linear in equation_pairs:
                b_polynomials.append(polynomial_context([
                    evaluate_univariate(constant, inner_value),
                    evaluate_univariate(linear, inner_value),
                ]))
            common_b_polynomial = b_polynomials[0]
            for value in b_polynomials[1:]:
                common_b_polynomial = common_b_polynomial.gcd(value)
            b_roots = polynomial_field_roots(common_b_polynomial)
            guarded_b_roots = []
            for b_value in b_roots:
                fixed_constant = evaluate_fraction(fixed_a.constant, r_value)
                fixed_linear = evaluate_fraction(fixed_a.linear, r_value)
                if fixed_constant is None or fixed_linear is None:
                    return {"status": "FIXED_A_BOUNDARY"}
                if (fixed_constant+b_value*fixed_linear) % PRIME:
                    guarded_b_roots.append(b_value)
                else:
                    target_boundaries.append({
                        inner_variable: inner_value,
                        "b": b_value,
                        "guard": "a=0",
                    })
            if guarded_b_roots:
                solutions.append({
                    inner_variable: inner_value,
                    "b_roots": guarded_b_roots,
                })
        return {
            "status": "CHECKED",
            "inner_cut_degree": int(common_inner.degree()),
            "inner_roots": inner_roots,
            "target_boundaries": target_boundaries,
            "solutions": solutions,
        }

    r_common = CommonPair(r)
    route_pairs = {
        "r": r_common,
        "t": t_pair,
        "r2_minus_1": r_common*r_common-1,
        "r2_plus_1": r_common*r_common+1,
        "t2_minus_1": t_pair*t_pair-1,
        "t2_plus_1": t_pair*t_pair+1,
        "t2_minus_r2": t_pair*t_pair-r_common*r_common,
        "t2_plus_r2": t_pair*t_pair+r_common*r_common,
    }
    guard_values = [
        (f"inverse_{index}", guard)
        for index, guard in enumerate(inverse_guards)
    ]
    for name, pair in route_pairs.items():
        if pair.linear != base_field.zero:
            raise ValueError(f"route guard {name} depends on b")
        guard_values.append((name, pair.constant))

    root_rows = []
    unresolved_roots = []
    univariate_component = normalized_components[univariate_index]
    for r_value in roots:
        zero_guards = []
        denominator_guards = []
        for name, guard in guard_values:
            if evaluate_base_polynomial(guard.denom, r_value) == 0:
                denominator_guards.append(name)
            elif evaluate_base_polynomial(guard.numer, r_value) == 0:
                zero_guards.append(name)
        clearing_boundaries = [
            f"equation_{index}"
            for index, (_, _, denominator) in enumerate(flint_pairs)
            if evaluate_base_polynomial(denominator, r_value) == 0
        ]
        if evaluate_base_polynomial(curve_denominator, r_value) == 0:
            clearing_boundaries.append("curve")
        root_row = {
            "r": r_value,
            "zero_guards": zero_guards,
            "denominator_guards": denominator_guards,
            "clearing_boundaries": clearing_boundaries,
        }
        if zero_guards or denominator_guards:
            root_row["status"] = "GUARD_BOUNDARY"
            root_rows.append(root_row)
            continue
        if clearing_boundaries:
            root_row["status"] = "CLEARING_BOUNDARY"
            unresolved_roots.append(r_value)
            root_rows.append(root_row)
            continue
        outer_specialized = specialize_component(
            univariate_component, outer_variable, {}, r_value
        )
        outer_roots = polynomial_field_roots(outer_specialized)
        root_row["outer_source"] = "univariate_component"
        if outer_roots is None:
            outer_specialized = specialize_component(
                inner, outer_variable, {}, r_value
            )
            outer_roots = polynomial_field_roots(outer_specialized)
            root_row["outer_source"] = "inner_resultant_fallback"
        root_row["outer_roots"] = outer_roots
        if outer_roots is None:
            root_row["status"] = "UNBOUNDED_OUTER_FIBER"
            unresolved_roots.append(r_value)
            root_rows.append(root_row)
            continue
        direct_rows = [
            {
                outer_variable: outer_value,
                "direct": direct_outer_fiber(r_value, outer_value),
            }
            for outer_value in outer_roots
        ]
        root_row["direct_rows"] = direct_rows
        root_row["status"] = "CHECKED"
        if any(
            item["direct"].get("status") != "CHECKED"
            or item["direct"].get("solutions")
            for item in direct_rows
        ):
            unresolved_roots.append(r_value)
        root_rows.append(root_row)

    outer_text = outer.str()
    row.update({
        "status": "CHAIN_COMPLETE",
        "unit": not unresolved_roots,
        "case_excluded": not unresolved_roots,
        "unresolved_roots": unresolved_roots,
        "univariate_component": univariate_index,
        "mixed_components": [left_index, right_index],
        "outer_variable": outer_variable,
        "inner_variable": inner_variable,
        "inner_degrees": [int(value) for value in inner.degrees()],
        "inner_terms": len(list(inner.terms())),
        "outer_degrees": degrees,
        "outer_terms": len(list(outer.terms())),
        "field_root_gcd_degree": int(field_gcd.degree()),
        "field_roots": roots,
        "field_root_rows": root_rows,
        "outer_sha256": hashlib.sha256(outer_text.encode()).hexdigest(),
        "outer_zlib_base64": base64.b64encode(
            zlib.compress(outer_text.encode(), level=9)
        ).decode(),
    })
    mark("chain")
    row["timings_seconds"] = timings
    return row


@app.local_entrypoint()
def main(
    signs: str = "-1:-1",
    lanes: str = "-1:-1",
    xi_indices: str = "0",
    pairing_indices: str = "3",
    mode: str = "profile",
):
    if mode not in ("profile", "chain"):
        raise ValueError("unsupported mode")
    selected_xi = tuple(int(value) for value in xi_indices.split(","))
    selected_pairings = tuple(int(value) for value in pairing_indices.split(","))
    selected_signs = tuple(
        tuple(int(item) for item in value.split(":"))
        for value in signs.split(",") if value
    )
    selected_lanes = tuple(
        tuple(int(item) for item in value.split(":"))
        for value in lanes.split(",") if value
    )
    cases = [
        (*source_signs, *target_signs, xi_index, pairing_index, mode)
        for source_signs in selected_signs
        for target_signs in selected_lanes
        for xi_index in selected_xi
        for pairing_index in selected_pairings
    ]
    rows = list(profile_case.map(cases, order_outputs=False))
    rows.sort(key=lambda row: (
        row["epsilon"], row["sigma"], row["xi_index"], row["pairing_index"]
    ))
    payload = {
        "schema": "rate-half-kb-positive-433-1b-cell14-fixed-a-rankone-flint-v1",
        "scope": "One source-sign/target-lane exact termwise-torus profile or chain.",
        "mode": mode,
        "field": PRIME,
        "source_curve_sha256": hashlib.sha256(CURVE.read_bytes()).hexdigest(),
        "source_script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "case_count": len(rows),
        "unit_count": sum(bool(row["unit"]) for row in rows),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT),
        "case_count": len(rows),
        "targetfree_case_count": sum(bool(row["targetfree_components"]) for row in rows),
        "univariate_case_count": sum(bool(row["univariate_components"]) for row in rows),
        "unit_count": sum(bool(row["unit"]) for row in rows),
    }, sort_keys=True))
