#!/usr/bin/env python3
"""Target-dependent b-projection probe for positive 433-1b cell 14.

This is a discovery-only prototype for the retained outside cases.  It works
over F_p(r), chooses one equation C+bL, eliminates b from every other
equation and from the quadratic common curve, and asks for the resulting
three-target generic Groebner basis.
"""

import base64
import hashlib
import itertools
import json
from pathlib import Path
import re
import subprocess
import time
import zlib

import modal


DIRECTORY = Path(__file__).parent
CURVE = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_curve_kernel_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_target_projection_result.json"
REMOTE_CURVE = "/root/curve.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell14-target-projection")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
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
        rest = values[1:index] + values[index + 1:]
        for tail in pairings(rest):
            yield ((first, values[index]),) + tail


@app.function(image=image, cpu=1.0, memory=2048, timeout=360, max_containers=32)
def decide_case(case):
    import sympy as sp

    started = time.perf_counter()
    epsilon_1, epsilon_2, sigma_c, sigma_o, xi_index, pairing_index = case[:6]
    branch = case[6] if len(case) > 6 else "open"
    factor_index = case[7] if len(case) > 7 else -1
    payload = json.loads(Path(REMOTE_CURVE).read_text())
    source = next(
        row for row in payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    )
    r, b, a, u, v, f = sp.symbols("r b a u v f")

    def expression(summary):
        return sp.sympify(summary["expression"])

    relation = expression(source["relation_rb"])
    relation_in_b = sp.Poly(relation, b)
    coefficient_a, coefficient_b, coefficient_c = relation_in_b.all_coeffs()
    base_field = sp.GF(PRIME).frac_field(r)
    coefficient_a = base_field.from_sympy(coefficient_a)
    coefficient_b = base_field.from_sympy(coefficient_b)
    coefficient_c = base_field.from_sympy(coefficient_c)
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
            return value if isinstance(value, CommonPair) else CommonPair(value, 0)

        def __add__(self, other):
            other = CommonPair.coerce(other)
            return CommonPair(self.constant+other.constant, self.linear+other.linear)

        __radd__ = __add__

        def __neg__(self):
            return CommonPair(-self.constant, -self.linear)

        def __sub__(self, other):
            return self + (-CommonPair.coerce(other))

        def __rsub__(self, other):
            return CommonPair.coerce(other) - self

        def __mul__(self, other):
            other = CommonPair.coerce(other)
            return CommonPair(
                self.constant*other.constant
                + self.linear*other.linear*quotient_v,
                self.constant*other.linear + self.linear*other.constant
                + self.linear*other.linear*quotient_u,
            )

        __rmul__ = __mul__

        def __pow__(self, exponent):
            if exponent < 0:
                return self.inverse() ** (-exponent)
            result = CommonPair(1, 0)
            base = self
            power = exponent
            while power:
                if power & 1:
                    result = result*base
                base = base*base
                power //= 2
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
        polynomial = sp.Poly(sp.expand(value), b)
        result = CommonPair(0, 0)
        for coefficient in polynomial.all_coeffs():
            result = result*common_b + CommonPair(coefficient, 0)
        return result

    def rational_pair(summary):
        return (
            polynomial_pair(expression(summary["numerator"]))
            / polynomial_pair(expression(summary["denominator"]))
        )

    t_pair = rational_pair(source["t_map"])
    c_pair = rational_pair(source["c_map"])
    kernel = [polynomial_pair(expression(value)) for value in source["kernel"]]
    a_coefficients = kernel[:3]
    b_coefficients = kernel[3:6]
    beta_0, beta_1 = kernel[6:]

    def evaluate(coefficients, value):
        return coefficients[0] + coefficients[1]*value + coefficients[2]*value**2

    missing_label = -(t_pair*t_pair)
    a_missing = evaluate(a_coefficients, missing_label)
    b_missing = evaluate(b_coefficients, missing_label)
    missing_record = b_missing/a_missing
    print(json.dumps({"phase": "common", "seconds": round(time.perf_counter()-started, 3)}), flush=True)

    target_ring = base_field.poly_ring(a, u, v, f)
    ring_a, ring_u, ring_v, ring_f = target_ring.gens

    def target_convert(value):
        if getattr(value, "ring", None) is target_ring.ring:
            return value
        if hasattr(value, "parent") and value.parent() == base_field:
            return target_ring.ring.ground_new(value)
        if hasattr(value, "as_expr"):
            return target_ring.from_sympy(value.as_expr())
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
            return value if isinstance(value, TargetPair) else TargetPair(value, 0)

        def __add__(self, other):
            other = TargetPair.coerce(other)
            return TargetPair(self.constant+other.constant, self.linear+other.linear)

        __radd__ = __add__

        def __neg__(self):
            return TargetPair(-self.constant, -self.linear)

        def __sub__(self, other):
            return self + (-TargetPair.coerce(other))

        def __rsub__(self, other):
            return TargetPair.coerce(other) - self

        def __mul__(self, other):
            other = TargetPair.coerce(other)
            return TargetPair(
                self.constant*other.constant
                + self.linear*other.linear*target_quotient_v,
                self.constant*other.linear + self.linear*other.constant
                + self.linear*other.linear*target_quotient_u,
            )

        __rmul__ = __mul__

        def __pow__(self, exponent):
            if exponent < 0:
                raise ValueError("target-polynomial quotient does not invert")
            result = TargetPair(1, 0)
            base = self
            power = exponent
            while power:
                if power & 1:
                    result = result*base
                base = base*base
                power //= 2
            return result

    def lift(value):
        return TargetPair(value.constant, value.linear)

    target = {
        a: TargetPair(ring_a),
        u: TargetPair(ring_u),
        v: TargetPair(ring_v),
        f: TargetPair(ring_f),
    }
    primary = (a, a, a, u, v, f, f)[xi_index]
    common_replacement = (
        missing_record,
        missing_record,
        -missing_record,
        missing_record,
        sigma_o*missing_record,
        missing_record/common_b,
        sigma_c*missing_record/c_pair,
    )[xi_index]
    target[primary] = lift(common_replacement)
    eliminated_target = None
    if branch in (
        "rankone_singular", "rankone_profile", "rankone_resultant",
        "rankone_chain", "rankone_targetfree"
    ):
        if xi_index == 3:
            eliminated_target = v
            target[v] = (
                target[a]*target[f]**2*lift(common_replacement.inverse())
            )
        elif xi_index == 4:
            eliminated_target = u
            target[u] = (
                target[a]*target[f]**2*lift(common_replacement.inverse())
            )
        elif xi_index in (5, 6):
            eliminated_target = a
            target[a] = (
                target[u]*target[v]
                * lift((common_replacement**2).inverse())
            )
        else:
            raise ValueError(
                "rank-one target chart requires xi_index in 3,4,5,6"
            )
    a_pair, u_pair, v_pair, f_pair = (
        target[a], target[u], target[v], target[f]
    )
    remaining = tuple(
        value for value in (a, u, v, f)
        if value not in (primary, eliminated_target)
    )
    b_pair = lift(common_b)
    c_target = lift(c_pair)
    a_coefficients = tuple(lift(value) for value in a_coefficients)
    b_coefficients = tuple(lift(value) for value in b_coefficients)
    beta_0, beta_1 = lift(beta_0), lift(beta_1)
    missing_label = lift(missing_label)
    a_missing = lift(a_missing)
    records = (
        a_pair, a_pair, -a_pair, u_pair, sigma_o*v_pair,
        b_pair*f_pair, sigma_c*c_target*f_pair,
    )
    sum_numerators = (
        (u_pair+v_pair)**2,
        (u_pair+v_pair)**2,
        (u_pair-v_pair)**2,
        (u_pair+f_pair*f_pair)**2,
        (v_pair+sigma_o*f_pair*f_pair)**2,
        (b_pair+f_pair)**2,
        (c_target+sigma_c*f_pair)**2,
    )
    sum_denominators = (
        f_pair*f_pair, f_pair*f_pair, f_pair*f_pair,
        f_pair*f_pair, f_pair*f_pair, TargetPair(1), TargetPair(1),
    )

    def paired(left, right):
        p0, p1, p2 = (
            b_value-left*a_value
            for a_value, b_value in zip(a_coefficients, b_coefficients)
        )
        q0 = b_coefficients[0]-right*a_coefficients[0]
        q1 = -b_coefficients[1]+right*a_coefficients[1]
        q2 = b_coefficients[2]-right*a_coefficients[2]
        return (p2*q0-p0*q2)**2 - (p2*q1-p1*q2)*(p1*q0-p0*q1)

    residual = tuple(index for index in range(7) if index != xi_index)
    matching = tuple(pairings(range(6)))[pairing_index]
    equations = [a_pair*f_pair*f_pair-u_pair*v_pair]
    equations.extend(
        paired(records[residual[left]], records[residual[right]])
        for left, right in matching
    )
    equations.append(
        sum_denominators[xi_index]
        * missing_label*(beta_0+beta_1*missing_label)**2
        - sum_numerators[xi_index]*a_missing**2
    )
    def monomial_support(value):
        support = []
        for b_exponent, component in ((0, value.constant), (1, value.linear)):
            for exponents, _ in component.terms():
                support.append([b_exponent, *exponents])
        return sorted(support)

    equation_supports = [monomial_support(equation) for equation in equations]
    print(json.dumps({"phase": "outside", "seconds": round(time.perf_counter()-started, 3)}), flush=True)

    target_singular_components = None
    target_singular_cutter_index = None
    if branch in (
        "target_singular", "rankone_singular", "rankone_profile",
        "rankone_resultant", "rankone_chain", "rankone_targetfree"
    ):
        candidates = [
            (
                len(cutter.constant.terms()) + len(cutter.linear.terms()),
                cutter_index,
                cutter,
            )
            for cutter_index, cutter in enumerate(equations)
            if cutter.linear
        ]
        if not candidates:
            return {
                "epsilon": [epsilon_1, epsilon_2],
                "sigma": [sigma_c, sigma_o],
                "xi_index": xi_index,
                "pairing_index": pairing_index,
                "branch": branch,
                "status": "NO_CUTTER",
            }
        _, target_singular_cutter_index, cutter = min(candidates)
        target_singular_components = [
            equation.constant*cutter.linear
            - equation.linear*cutter.constant
            for index, equation in enumerate(equations)
            if index != target_singular_cutter_index
        ]
        target_singular_components.append(
            target_convert(coefficient_a)*cutter.constant*cutter.constant
            - target_convert(coefficient_b)*cutter.constant*cutter.linear
            + target_convert(coefficient_c)*cutter.linear*cutter.linear
        )
        print(json.dumps({
            "phase": "projected",
            "case": list(case),
            "seconds": round(time.perf_counter()-started, 3),
            "cutter_index": target_singular_cutter_index,
            "score": sum(
                len(value.terms()) for value in target_singular_components
            ),
            "variables": [str(value) for value in remaining],
        }, sort_keys=True), flush=True)
        if branch == "rankone_profile":
            component_profiles = []
            all_targets = (a, u, v, f)
            for component in target_singular_components:
                terms = component.terms()
                used = [
                    str(target_variable)
                    for index, target_variable in enumerate(all_targets)
                    if any(exponents[index] for exponents, _ in terms)
                ]
                component_profiles.append({
                    "degree": max(
                        (sum(exponents) for exponents, _ in terms),
                        default=-1,
                    ),
                    "terms": len(terms),
                    "variables": used,
                })
            return {
                "epsilon": [epsilon_1, epsilon_2],
                "sigma": [sigma_c, sigma_o],
                "xi_index": xi_index,
                "pairing_index": pairing_index,
                "branch": branch,
                "status": "COMPLETE",
                "unit": False,
                "cutter_index": target_singular_cutter_index,
                "remaining": [str(value) for value in remaining],
                "component_profiles": component_profiles,
                "seconds": time.perf_counter()-started,
            }

    if branch == "target":
        from sympy.polys.groebnertools import groebner as ring_groebner

        candidates = [
            (
                len(cutter.constant.terms()) + len(cutter.linear.terms()),
                cutter_index,
                cutter,
            )
            for cutter_index, cutter in enumerate(equations)
            if cutter.linear
        ]
        if not candidates:
            return {
                "epsilon": [epsilon_1, epsilon_2],
                "sigma": [sigma_c, sigma_o],
                "xi_index": xi_index,
                "pairing_index": pairing_index,
                "branch": branch,
                "status": "NO_CUTTER",
            }
        _, cutter_index, cutter = min(candidates)
        components = [
            equation.constant*cutter.linear
            - equation.linear*cutter.constant
            for index, equation in enumerate(equations)
            if index != cutter_index
        ]
        components.append(
            target_convert(coefficient_a)*cutter.constant*cutter.constant
            - target_convert(coefficient_b)*cutter.constant*cutter.linear
            + target_convert(coefficient_c)*cutter.linear*cutter.linear
        )
        score = sum(len(value.terms()) for value in components)
        all_targets = (a, u, v, f)
        primary_index = all_targets.index(primary)
        remaining_indices = tuple(
            all_targets.index(value) for value in remaining
        )
        remaining_ring = base_field.poly_ring(*remaining, order="grevlex")

        def target_polynomial(value):
            terms = {}
            for exponents, coefficient in value.terms():
                if exponents[primary_index]:
                    raise ValueError("eliminated target remains in projection")
                remaining_exponents = tuple(
                    exponents[index] for index in remaining_indices
                )
                terms[remaining_exponents] = coefficient
            return remaining_ring.ring.from_dict(terms)

        def polynomial_profile(polynomial):
            terms = polynomial.terms()
            return {
                "degree": max(
                    (sum(exponents) for exponents, _ in terms),
                    default=-1,
                ),
                "terms": len(terms),
            }

        projected_polynomials = [
            target_polynomial(value)
            for value in components
            if value
        ]
        profiles = [polynomial_profile(value) for value in projected_polynomials]
        print(json.dumps({
            "phase": "projected",
            "case": list(case),
            "seconds": round(time.perf_counter()-started, 3),
            "cutter_index": cutter_index,
            "score": score,
            "variables": [str(value) for value in remaining],
            "profiles": profiles,
        }, sort_keys=True), flush=True)
        basis_polynomials = ring_groebner(
            projected_polynomials,
            remaining_ring.ring,
            method="f5b",
        )
        unit = len(basis_polynomials) == 1 and basis_polynomials[0].is_one
        return {
            "epsilon": [epsilon_1, epsilon_2],
            "sigma": [sigma_c, sigma_o],
            "xi_index": xi_index,
            "pairing_index": pairing_index,
            "branch": branch,
            "status": "COMPLETE",
            "unit": unit,
            "cutter_index": cutter_index,
            "cutter_support": monomial_support(cutter),
            "cutter_constant_terms": len(cutter.constant.terms()),
            "cutter_linear_terms": len(cutter.linear.terms()),
            "variables": [str(value) for value in remaining],
            "projected_profiles": profiles,
            "basis_profiles": [
                polynomial_profile(value) for value in basis_polynomials
            ],
            "seconds": time.perf_counter()-started,
        }

    variables = (b, *remaining)
    all_targets = (a, u, v, f)
    remaining_indices = tuple(all_targets.index(value) for value in remaining)

    def base_polynomial(value):
        terms = []
        for (exponent,), coefficient in value.terms():
            scalar = int(coefficient)
            monomial = "" if exponent == 0 else (
                "r" if exponent == 1 else f"r^{exponent}"
            )
            if monomial:
                terms.append(f"{scalar}*{monomial}")
            else:
                terms.append(str(scalar))
        return "+".join(terms) if terms else "0"

    def component_rows(component, b_exponent):
        rows = []
        for exponents, coefficient in component.terms():
            for index, target_variable in enumerate(all_targets):
                if target_variable not in remaining and exponents[index] != 0:
                    raise ValueError(
                        "eliminated target variable survived substitution"
                    )
            factors = []
            if b_exponent:
                factors.append("b")
            for target_index in remaining_indices:
                exponent = exponents[target_index]
                if exponent == 1:
                    factors.append(str(all_targets[target_index]))
                elif exponent > 1:
                    factors.append(f"{all_targets[target_index]}^{exponent}")
            rows.append((coefficient, factors))
        return rows

    def serialize_rows(rows):
        common_denominator = rows[0][0].denom.ring.one
        for coefficient, _ in rows:
            common_denominator = common_denominator.lcm(coefficient.denom)
        serialized = []
        for coefficient, factors in rows:
            multiplier = common_denominator.exquo(coefficient.denom)
            coefficient_text = base_polynomial(coefficient.numer*multiplier)
            serialized.append("*".join((f"({coefficient_text})", *factors)))
        return "+".join(serialized), common_denominator.degree()

    def materialize(value):
        rows = [
            *component_rows(value.constant, 0),
            *component_rows(value.linear, 1),
        ]
        degree = max(
            (
                b_exponent + sum(exponents[index] for index in remaining_indices)
                for b_exponent, component in ((0, value.constant), (1, value.linear))
                for exponents, _ in component.terms()
            ),
            default=0,
        )
        if not rows:
            return "0", [degree, 0], 0
        text, denominator_degree = serialize_rows(rows)
        return text, [degree, len(rows)], denominator_degree

    def materialize_component(component):
        rows = component_rows(component, 0)
        degree = max(
            (
                sum(exponents[index] for index in remaining_indices)
                for exponents, _ in component.terms()
            ),
            default=0,
        )
        if not rows:
            return "0", [degree, 0], 0
        text, denominator_degree = serialize_rows(rows)
        return text, [degree, len(rows)], denominator_degree

    if branch == "rankone_targetfree":
        from flint import fmpz_mod_mpoly_ctx, fmpz_mod_poly_ctx

        all_targets = (a, u, v, f)
        targetfree_rows = []
        for component_index, component in enumerate(
            target_singular_components
        ):
            if not component:
                continue
            terms = component.terms()
            if all(not any(exponents) for exponents, _ in terms):
                targetfree_rows.append((component_index, component))
        if not targetfree_rows:
            return {
                "epsilon": [epsilon_1, epsilon_2],
                "sigma": [sigma_c, sigma_o],
                "xi_index": xi_index,
                "pairing_index": pairing_index,
                "branch": branch,
                "status": "NO_TARGETFREE_COMPONENT",
            }
        component_index, component = targetfree_rows[0]
        component_terms = component.terms()
        if len(component_terms) != 1:
            raise ValueError("target-free component has multiple target terms")
        coefficient = component_terms[0][1]
        numerator = coefficient.numer
        univariate_context = fmpz_mod_poly_ctx(PRIME)
        coefficients = {
            exponent: int(value)
            for (exponent,), value in numerator.terms()
        }
        maximum = max(coefficients, default=0)
        polynomial = univariate_context([
            coefficients.get(exponent, 0)
            for exponent in range(maximum+1)
        ])
        variable_univariate = univariate_context([0, 1])
        field_gcd = polynomial.gcd(
            pow(variable_univariate, PRIME, polynomial)
            - variable_univariate
        )
        _, factors = field_gcd.factor()
        roots = []
        for factor, _ in factors:
            if int(factor.degree()) != 1:
                raise ValueError("field-root gcd has nonlinear factor")
            roots.append(
                -int(factor[0])*pow(int(factor[1]), -1, PRIME) % PRIME
            )
        inner_variable, outer_variable = remaining

        def evaluate_base_polynomial(value, point):
            return sum(
                int(source)*pow(point, exponent, PRIME)
                for (exponent,), source in value.terms()
            ) % PRIME

        def polynomial_field_roots(value):
            if value.is_zero():
                return None
            if int(value.degree()) == 0:
                return []
            root_polynomial = value.gcd(
                pow(variable_univariate, PRIME, value)-variable_univariate
            )
            _, root_factors = root_polynomial.factor()
            output = []
            for root_factor, _ in root_factors:
                if int(root_factor.degree()) != 1:
                    raise ValueError("field-root gcd has nonlinear factor")
                output.append(
                    -int(root_factor[0])
                    * pow(int(root_factor[1]), -1, PRIME)
                    % PRIME
                )
            return sorted(output)

        def specialize_component(
            source, free_variable, assignments, r_value
        ):
            free_index = all_targets.index(free_variable)
            output = {}
            for exponents, source_coefficient in source.terms():
                denominator = evaluate_base_polynomial(
                    source_coefficient.denom, r_value
                )
                if denominator == 0:
                    return None
                scalar = (
                    evaluate_base_polynomial(
                        source_coefficient.numer, r_value
                    ) * pow(denominator, -1, PRIME)
                ) % PRIME
                for target_index, target_variable in enumerate(all_targets):
                    exponent = exponents[target_index]
                    if not exponent or target_index == free_index:
                        continue
                    scalar = (
                        scalar
                        * pow(assignments[target_variable], exponent, PRIME)
                    ) % PRIME
                exponent = exponents[free_index]
                output[exponent] = (output.get(exponent, 0)+scalar) % PRIME
            maximum = max(output, default=0)
            return univariate_context([
                output.get(exponent, 0) for exponent in range(maximum+1)
            ])

        def evaluate_univariate(value, point):
            return sum(
                int(value[index])*pow(point, index, PRIME)
                for index in range(int(value.degree())+1)
            ) % PRIME

        def curve_at_r(r_value):
            output = []
            for curve_coefficient in (
                coefficient_a, coefficient_b, coefficient_c
            ):
                denominator = evaluate_base_polynomial(
                    curve_coefficient.denom, r_value
                )
                if denominator == 0:
                    return None
                output.append(
                    evaluate_base_polynomial(
                        curve_coefficient.numer, r_value
                    ) * pow(denominator, -1, PRIME) % PRIME
                )
            return output

        def direct_outer_fiber(r_value, outer_value):
            assignments = {outer_variable: outer_value}
            equation_pairs = []
            for equation in equations:
                constant = specialize_component(
                    equation.constant, inner_variable, assignments, r_value
                )
                linear = specialize_component(
                    equation.linear, inner_variable, assignments, r_value
                )
                if constant is None or linear is None:
                    return {"status": "COEFFICIENT_BOUNDARY"}
                if not constant.is_zero() or not linear.is_zero():
                    equation_pairs.append((constant, linear))
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
                for left, right in itertools.combinations(equation_pairs, 2)
            )
            cuts = [value for value in cuts if not value.is_zero()]
            if not cuts:
                return {"status": "NO_INNER_CUT"}
            common_inner = cuts[0]
            for value in cuts[1:]:
                common_inner = common_inner.gcd(value)
            inner_roots = polynomial_field_roots(common_inner)
            solutions = []
            for inner_value in inner_roots:
                b_polynomials = [
                    univariate_context([curve_c, curve_b, curve_a])
                ]
                for constant, linear in equation_pairs:
                    b_polynomials.append(univariate_context([
                        evaluate_univariate(constant, inner_value),
                        evaluate_univariate(linear, inner_value),
                    ]))
                common_b = b_polynomials[0]
                for value in b_polynomials[1:]:
                    common_b = common_b.gcd(value)
                b_roots = polynomial_field_roots(common_b)
                if b_roots:
                    solutions.append({
                        str(inner_variable): inner_value,
                        "b_roots": b_roots,
                    })
            return {
                "status": "CHECKED",
                "inner_cut_degree": int(common_inner.degree()),
                "inner_roots": inner_roots,
                "solutions": solutions,
            }

        def direct_unbounded_fiber(r_value):
            target_context = fmpz_mod_mpoly_ctx.get(
                [str(value) for value in remaining], PRIME
            )

            def target_at_r(source):
                output = {}
                for exponents, source_coefficient in source.terms():
                    denominator = evaluate_base_polynomial(
                        source_coefficient.denom, r_value
                    )
                    if denominator == 0:
                        return None
                    scalar = (
                        evaluate_base_polynomial(
                            source_coefficient.numer, r_value
                        ) * pow(denominator, -1, PRIME)
                    ) % PRIME
                    key = tuple(
                        exponents[all_targets.index(value)]
                        for value in remaining
                    )
                    output[key] = (output.get(key, 0)+scalar) % PRIME
                return target_context.from_dict({
                    key: source_coefficient
                    for key, source_coefficient in output.items()
                    if source_coefficient
                })

            equation_pairs = []
            for equation in equations:
                constant = target_at_r(equation.constant)
                linear = target_at_r(equation.linear)
                if constant is None or linear is None:
                    return {"status": "COEFFICIENT_BOUNDARY"}
                if constant or linear:
                    equation_pairs.append((constant, linear))
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
                for left, right in itertools.combinations(equation_pairs, 2)
            )
            cuts = sorted(
                (value for value in cuts if value),
                key=lambda value: (
                    int(value.total_degree()), len(list(value.terms()))
                ),
            )
            inner_index = remaining.index(inner_variable)
            outer_index = remaining.index(outer_variable)
            outer_cut = next((
                value for value in cuts
                if int(value.degrees()[inner_index]) == 0
            ), None)
            source = "univariate_cut"
            if outer_cut is None:
                source = "pair_resultant"
                for left, right in itertools.combinations(cuts, 2):
                    candidate = left.resultant(
                        right, str(inner_variable)
                    )
                    if candidate:
                        outer_cut = candidate
                        break
            if outer_cut is None:
                return {"status": "NO_OUTER_CUT"}
            output = {}
            for monomial, source_coefficient in outer_cut.to_dict().items():
                if monomial[inner_index] != 0:
                    raise ValueError("direct cut retained inner target")
                exponent = monomial[outer_index]
                output[exponent] = (
                    output.get(exponent, 0)+int(source_coefficient)
                ) % PRIME
            maximum = max(output, default=0)
            outer_polynomial = univariate_context([
                output.get(exponent, 0) for exponent in range(maximum+1)
            ])
            outer_roots = polynomial_field_roots(outer_polynomial)
            if outer_roots is None:
                return {"status": "ZERO_OUTER_CUT"}
            direct_rows = [
                {
                    str(outer_variable): outer_value,
                    "direct": direct_outer_fiber(r_value, outer_value),
                }
                for outer_value in outer_roots
            ]
            failures = [
                row for row in direct_rows
                if row["direct"].get("status") != "CHECKED"
                or row["direct"].get("solutions")
            ]
            return {
                "status": "CHECKED",
                "source": source,
                "outer_cut_degree": int(outer_polynomial.degree()),
                "outer_roots": outer_roots,
                "direct_rows": direct_rows,
                "solutions": failures,
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
        guard_values.extend(
            (name, pair.constant) for name, pair in route_pairs.items()
        )
        root_rows = []
        unresolved_roots = []
        for r_value in sorted(roots):
            zero_guards = []
            denominator_guards = []
            for name, guard in guard_values:
                if evaluate_base_polynomial(guard.denom, r_value) == 0:
                    denominator_guards.append(name)
                elif evaluate_base_polynomial(guard.numer, r_value) == 0:
                    zero_guards.append(name)
            row = {
                "r": r_value,
                "zero_guards": zero_guards,
                "denominator_guards": denominator_guards,
            }
            if zero_guards or denominator_guards:
                row["status"] = "GUARD_BOUNDARY"
            else:
                direct = direct_unbounded_fiber(r_value)
                row["status"] = "CHECKED"
                row["direct"] = direct
                if (
                    direct.get("status") != "CHECKED"
                    or direct.get("solutions")
                ):
                    unresolved_roots.append(r_value)
            root_rows.append(row)
        case_excluded = not unresolved_roots
        polynomial_text = polynomial.str()
        return {
            "epsilon": [epsilon_1, epsilon_2],
            "sigma": [sigma_c, sigma_o],
            "xi_index": xi_index,
            "pairing_index": pairing_index,
            "branch": branch,
            "status": "COMPLETE",
            "unit": case_excluded,
            "case_excluded": case_excluded,
            "unresolved_roots": unresolved_roots,
            "targetfree_component": component_index,
            "polynomial_degree": int(polynomial.degree()),
            "polynomial_terms": sum(
                bool(polynomial[index])
                for index in range(int(polynomial.degree())+1)
            ),
            "field_root_gcd_degree": int(field_gcd.degree()),
            "field_roots": sorted(roots),
            "field_root_rows": root_rows,
            "total_seconds": time.perf_counter()-started,
            "polynomial_sha256": hashlib.sha256(
                polynomial_text.encode()
            ).hexdigest(),
            "polynomial_zlib_base64": base64.b64encode(
                zlib.compress(polynomial_text.encode(), level=9)
            ).decode(),
        }

    if branch == "rankone_chain":
        from flint import fmpz_mod_mpoly_ctx, fmpz_mod_poly_ctx

        all_targets = (a, u, v, f)
        component_rows_with_index = []
        for component_index, component in enumerate(
            target_singular_components
        ):
            if not component:
                continue
            terms = component.terms()
            used = tuple(
                target_variable
                for index, target_variable in enumerate(all_targets)
                if any(exponents[index] for exponents, _ in terms)
            )
            component_rows_with_index.append((
                component_index, component, used,
                materialize_component(component),
            ))
        univariate_rows = [
            row for row in component_rows_with_index if len(row[2]) == 1
        ]
        mixed_rows = [
            row for row in component_rows_with_index
            if set(row[2]) == set(remaining)
        ]
        if not univariate_rows or len(mixed_rows) < 2:
            return {
                "epsilon": [epsilon_1, epsilon_2],
                "sigma": [sigma_c, sigma_o],
                "xi_index": xi_index,
                "pairing_index": pairing_index,
                "branch": branch,
                "status": "NO_CHAIN",
            }
        univariate_row = min(
            univariate_rows, key=lambda row: row[3][1][1]
        )
        outer_variable = univariate_row[2][0]
        inner_variable = next(
            value for value in remaining if value != outer_variable
        )
        flint_variables = (*remaining, r)
        flint_context = fmpz_mod_mpoly_ctx.get(
            [str(value) for value in flint_variables], PRIME
        )

        def flint_target_component(component):
            component_terms = component.terms()
            common_denominator = component_terms[0][1].denom.ring.one
            for _, coefficient in component_terms:
                common_denominator = common_denominator.lcm(
                    coefficient.denom
                )
            output = {}
            for exponents, coefficient in component_terms:
                multiplier = common_denominator.exquo(coefficient.denom)
                numerator = coefficient.numer*multiplier
                target_exponents = tuple(
                    exponents[all_targets.index(value)]
                    for value in remaining
                )
                for (r_exponent,), scalar in numerator.terms():
                    key = (*target_exponents, r_exponent)
                    output[key] = (
                        output.get(key, 0) + int(scalar)
                    ) % PRIME
            return flint_context.from_dict({
                key: coefficient
                for key, coefficient in output.items()
                if coefficient
            })

        univariate_polynomial = flint_target_component(univariate_row[1])
        chain_candidates = []
        for left, right in itertools.combinations(mixed_rows, 2):
            inner = flint_target_component(left[1]).resultant(
                flint_target_component(right[1]), str(inner_variable)
            )
            if inner:
                chain_candidates.append((
                    int(inner.total_degree()),
                    len(list(inner.terms())),
                    left,
                    right,
                    inner,
                ))
        if not chain_candidates:
            return {
                "epsilon": [epsilon_1, epsilon_2],
                "sigma": [sigma_c, sigma_o],
                "xi_index": xi_index,
                "pairing_index": pairing_index,
                "branch": branch,
                "status": "ZERO_INNER_RESULTANTS",
            }
        _, _, left, right, inner = min(
            chain_candidates, key=lambda row: row[:2]
        )
        outer = inner.resultant(
            univariate_polynomial, str(outer_variable)
        )
        if not outer:
            return {
                "epsilon": [epsilon_1, epsilon_2],
                "sigma": [sigma_c, sigma_o],
                "xi_index": xi_index,
                "pairing_index": pairing_index,
                "branch": branch,
                "status": "ZERO_OUTER_RESULTANT",
            }
        outer_text = outer.str()
        degrees = [int(value) for value in outer.degrees()]
        if any(degrees[index] for index in range(len(remaining))):
            raise ValueError("target variable survived chained resultant")
        univariate_context = fmpz_mod_poly_ctx(PRIME)
        coefficients = {
            monomial[-1]: int(coefficient)
            for monomial, coefficient in outer.to_dict().items()
        }
        maximum = max(coefficients, default=0)
        outer_univariate = univariate_context([
            coefficients.get(exponent, 0)
            for exponent in range(maximum+1)
        ])
        variable_univariate = univariate_context([0, 1])
        field_gcd = outer_univariate.gcd(
            pow(variable_univariate, PRIME, outer_univariate)
            - variable_univariate
        )
        _, factors = field_gcd.factor()
        roots = []
        for factor, _ in factors:
            if int(factor.degree()) != 1:
                raise ValueError("field-root gcd has nonlinear factor")
            roots.append(
                -int(factor[0])*pow(int(factor[1]), -1, PRIME) % PRIME
            )

        def evaluate_base_polynomial(polynomial, value):
            return sum(
                int(coefficient)*pow(value, exponent, PRIME)
                for (exponent,), coefficient in polynomial.terms()
            ) % PRIME

        def specialize_component(
            component, free_variable, assignments, r_value
        ):
            free_index = all_targets.index(free_variable)
            output = {}
            for exponents, coefficient in component.terms():
                denominator = evaluate_base_polynomial(
                    coefficient.denom, r_value
                )
                if denominator == 0:
                    return None
                scalar = (
                    evaluate_base_polynomial(coefficient.numer, r_value)
                    * pow(denominator, -1, PRIME)
                ) % PRIME
                for target_index, target_variable in enumerate(all_targets):
                    exponent = exponents[target_index]
                    if not exponent or target_index == free_index:
                        continue
                    if target_variable not in assignments:
                        raise ValueError("missing target specialization")
                    scalar = (
                        scalar
                        * pow(assignments[target_variable], exponent, PRIME)
                    ) % PRIME
                exponent = exponents[free_index]
                output[exponent] = (output.get(exponent, 0)+scalar) % PRIME
            maximum = max(output, default=0)
            return univariate_context([
                output.get(exponent, 0) for exponent in range(maximum+1)
            ])

        def polynomial_field_roots(polynomial):
            if polynomial.is_zero():
                return None
            if int(polynomial.degree()) == 0:
                return []
            root_polynomial = polynomial.gcd(
                pow(variable_univariate, PRIME, polynomial)
                - variable_univariate
            )
            _, root_factors = root_polynomial.factor()
            values = []
            for factor, _ in root_factors:
                if int(factor.degree()) != 1:
                    raise ValueError("field-root gcd has nonlinear factor")
                values.append(
                    -int(factor[0])*pow(int(factor[1]), -1, PRIME)
                    % PRIME
                )
            return sorted(values)

        def evaluate_univariate(polynomial, value):
            return sum(
                int(polynomial[index])*pow(value, index, PRIME)
                for index in range(int(polynomial.degree())+1)
            ) % PRIME

        def direct_outer_fiber(r_value, outer_value):
            assignments = {outer_variable: outer_value}
            equation_pairs = []
            for equation in equations:
                constant = specialize_component(
                    equation.constant, inner_variable, assignments, r_value
                )
                linear = specialize_component(
                    equation.linear, inner_variable, assignments, r_value
                )
                if constant is None or linear is None:
                    return {"status": "COEFFICIENT_BOUNDARY"}
                if not constant.is_zero() or not linear.is_zero():
                    equation_pairs.append((constant, linear))
            curve_values = []
            for coefficient in (
                coefficient_a, coefficient_b, coefficient_c
            ):
                denominator = evaluate_base_polynomial(
                    coefficient.denom, r_value
                )
                if denominator == 0:
                    return {"status": "CURVE_BOUNDARY"}
                curve_values.append(
                    evaluate_base_polynomial(coefficient.numer, r_value)
                    * pow(denominator, -1, PRIME)
                    % PRIME
                )
            curve_a, curve_b, curve_c = curve_values
            cuts = [
                curve_a*constant*constant
                - curve_b*constant*linear
                + curve_c*linear*linear
                for constant, linear in equation_pairs
            ]
            cuts.extend(
                left_pair[0]*right_pair[1]
                - left_pair[1]*right_pair[0]
                for left_pair, right_pair in itertools.combinations(
                    equation_pairs, 2
                )
            )
            nonzero_cuts = [cut for cut in cuts if not cut.is_zero()]
            if not nonzero_cuts:
                return {"status": "NO_INNER_CUT"}
            common_inner = nonzero_cuts[0]
            for cut in nonzero_cuts[1:]:
                common_inner = common_inner.gcd(cut)
            inner_roots = polynomial_field_roots(common_inner)
            solutions = []
            for inner_value in inner_roots:
                b_polynomials = [
                    univariate_context([curve_c, curve_b, curve_a])
                ]
                for constant, linear in equation_pairs:
                    b_polynomials.append(univariate_context([
                        evaluate_univariate(constant, inner_value),
                        evaluate_univariate(linear, inner_value),
                    ]))
                common_b = b_polynomials[0]
                for polynomial in b_polynomials[1:]:
                    common_b = common_b.gcd(polynomial)
                b_roots = polynomial_field_roots(common_b)
                if b_roots:
                    solutions.append({
                        str(inner_variable): inner_value,
                        "b_roots": b_roots,
                    })
            return {
                "status": "CHECKED",
                "inner_cut_degree": int(common_inner.degree()),
                "inner_roots": inner_roots,
                "solutions": solutions,
            }

        def direct_unbounded_fiber(r_value):
            target_context = fmpz_mod_mpoly_ctx.get(
                [str(value) for value in remaining], PRIME
            )

            def target_at_r(component):
                output = {}
                for exponents, coefficient in component.terms():
                    denominator = evaluate_base_polynomial(
                        coefficient.denom, r_value
                    )
                    if denominator == 0:
                        return None
                    scalar = (
                        evaluate_base_polynomial(coefficient.numer, r_value)
                        * pow(denominator, -1, PRIME)
                    ) % PRIME
                    key = tuple(
                        exponents[all_targets.index(value)]
                        for value in remaining
                    )
                    output[key] = (output.get(key, 0)+scalar) % PRIME
                return target_context.from_dict({
                    key: coefficient
                    for key, coefficient in output.items()
                    if coefficient
                })

            equation_pairs = []
            for equation in equations:
                constant = target_at_r(equation.constant)
                linear = target_at_r(equation.linear)
                if constant is None or linear is None:
                    return {"status": "COEFFICIENT_BOUNDARY"}
                if constant or linear:
                    equation_pairs.append((constant, linear))
            curve_values = []
            for coefficient in (
                coefficient_a, coefficient_b, coefficient_c
            ):
                denominator = evaluate_base_polynomial(
                    coefficient.denom, r_value
                )
                if denominator == 0:
                    return {"status": "CURVE_BOUNDARY"}
                curve_values.append(
                    evaluate_base_polynomial(coefficient.numer, r_value)
                    * pow(denominator, -1, PRIME)
                    % PRIME
                )
            curve_a, curve_b, curve_c = curve_values
            cuts = [
                curve_a*constant*constant
                - curve_b*constant*linear
                + curve_c*linear*linear
                for constant, linear in equation_pairs
            ]
            cuts.extend(
                left_pair[0]*right_pair[1]
                - left_pair[1]*right_pair[0]
                for left_pair, right_pair in itertools.combinations(
                    equation_pairs, 2
                )
            )
            cuts = sorted(
                (cut for cut in cuts if cut),
                key=lambda cut: (
                    int(cut.total_degree()), len(list(cut.terms()))
                ),
            )
            inner_index = remaining.index(inner_variable)
            outer_index = remaining.index(outer_variable)
            outer_cut = next(
                (
                    cut for cut in cuts
                    if int(cut.degrees()[inner_index]) == 0
                ),
                None,
            )
            source = "univariate_cut"
            if outer_cut is None:
                source = "pair_resultant"
                for first, second in itertools.combinations(cuts, 2):
                    candidate = first.resultant(
                        second, str(inner_variable)
                    )
                    if candidate:
                        outer_cut = candidate
                        break
            if outer_cut is None:
                return {"status": "NO_OUTER_CUT"}
            if int(outer_cut.degrees()[inner_index]) != 0:
                raise ValueError("direct resultant retained inner target")
            output = {}
            for monomial, coefficient in outer_cut.to_dict().items():
                exponent = monomial[outer_index]
                output[exponent] = (
                    output.get(exponent, 0)+int(coefficient)
                ) % PRIME
            maximum = max(output, default=0)
            outer_polynomial = univariate_context([
                output.get(exponent, 0)
                for exponent in range(maximum+1)
            ])
            outer_roots = polynomial_field_roots(outer_polynomial)
            if outer_roots is None:
                return {"status": "ZERO_OUTER_CUT"}
            direct_rows = [
                {
                    str(outer_variable): outer_value,
                    "direct": direct_outer_fiber(r_value, outer_value),
                }
                for outer_value in outer_roots
            ]
            return {
                "status": "CHECKED",
                "source": source,
                "outer_cut_degree": int(outer_polynomial.degree()),
                "outer_roots": outer_roots,
                "direct_rows": direct_rows,
                "solutions": [
                    item for item in direct_rows
                    if item["direct"].get("solutions")
                    or item["direct"].get("status") != "CHECKED"
                ],
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
        guard_values.extend(
            (name, pair.constant) for name, pair in route_pairs.items()
        )

        def specialize_inner_resultant(r_value):
            outer_index = remaining.index(outer_variable)
            output = {}
            for monomial, coefficient in inner.to_dict().items():
                for index in range(len(remaining)):
                    if index != outer_index and monomial[index] != 0:
                        raise ValueError(
                            "inner resultant retained eliminated target"
                        )
                exponent = monomial[outer_index]
                scalar = (
                    int(coefficient)*pow(r_value, monomial[-1], PRIME)
                ) % PRIME
                output[exponent] = (output.get(exponent, 0)+scalar) % PRIME
            maximum = max(output, default=0)
            return univariate_context([
                output.get(exponent, 0)
                for exponent in range(maximum+1)
            ])

        root_rows = []
        unresolved_roots = []
        for r_value in sorted(roots):
            zero_guards = []
            denominator_guards = []
            for name, guard in guard_values:
                if evaluate_base_polynomial(guard.denom, r_value) == 0:
                    denominator_guards.append(name)
                elif evaluate_base_polynomial(guard.numer, r_value) == 0:
                    zero_guards.append(name)
            row = {
                "r": r_value,
                "zero_guards": zero_guards,
                "denominator_guards": denominator_guards,
            }
            if zero_guards or denominator_guards:
                row["status"] = "GUARD_BOUNDARY"
                root_rows.append(row)
                continue
            outer_specialized = specialize_component(
                univariate_row[1], outer_variable, {}, r_value
            )
            if outer_specialized is None:
                row["status"] = "COEFFICIENT_BOUNDARY"
                unresolved_roots.append(r_value)
                root_rows.append(row)
                continue
            outer_roots = polynomial_field_roots(outer_specialized)
            if outer_roots is None:
                row["outer_source"] = "inner_resultant_fallback"
                outer_roots = polynomial_field_roots(
                    specialize_inner_resultant(r_value)
                )
            else:
                row["outer_source"] = "univariate_component"
            row["outer_roots"] = outer_roots
            if outer_roots is None:
                direct_unbounded = direct_unbounded_fiber(r_value)
                row["direct_unbounded"] = direct_unbounded
                row["status"] = "CHECKED"
                if (
                    direct_unbounded.get("status") != "CHECKED"
                    or direct_unbounded.get("solutions")
                ):
                    unresolved_roots.append(r_value)
                root_rows.append(row)
                continue
            direct_rows = [
                {
                    str(outer_variable): outer_value,
                    "direct": direct_outer_fiber(r_value, outer_value),
                }
                for outer_value in outer_roots
            ]
            row["direct_rows"] = direct_rows
            row["status"] = "CHECKED"
            if any(
                item["direct"].get("status") != "CHECKED"
                or item["direct"].get("solutions")
                for item in direct_rows
            ):
                unresolved_roots.append(r_value)
            root_rows.append(row)
        case_excluded = not unresolved_roots
        return {
            "epsilon": [epsilon_1, epsilon_2],
            "sigma": [sigma_c, sigma_o],
            "xi_index": xi_index,
            "pairing_index": pairing_index,
            "branch": branch,
            "status": "COMPLETE",
            "unit": case_excluded,
            "case_excluded": case_excluded,
            "unresolved_roots": sorted(set(unresolved_roots)),
            "outer_variable": str(outer_variable),
            "inner_variable": str(inner_variable),
            "univariate_component": univariate_row[0],
            "mixed_components": [left[0], right[0]],
            "inner_degrees": [int(value) for value in inner.degrees()],
            "inner_terms": len(list(inner.terms())),
            "outer_degrees": degrees,
            "outer_terms": len(list(outer.terms())),
            "field_root_gcd_degree": int(field_gcd.degree()),
            "field_roots": sorted(roots),
            "field_root_rows": root_rows,
            "total_seconds": time.perf_counter()-started,
            "outer_sha256": hashlib.sha256(outer_text.encode()).hexdigest(),
            "outer_zlib_base64": base64.b64encode(
                zlib.compress(outer_text.encode(), level=9)
            ).decode(),
        }

    if branch == "rankone_resultant":
        all_targets = (a, u, v, f)
        component_rows_with_index = []
        for component_index, component in enumerate(
            target_singular_components
        ):
            if not component:
                continue
            terms = component.terms()
            used = tuple(
                target_variable
                for index, target_variable in enumerate(all_targets)
                if any(exponents[index] for exponents, _ in terms)
            )
            component_rows_with_index.append((
                component_index,
                component,
                used,
                materialize_component(component),
            ))
        resultant_candidates = []
        for left, right in itertools.combinations(
            component_rows_with_index, 2
        ):
            if len(left[2]) == 1 and left[2] == right[2]:
                score = left[3][1][1] + right[3][1][1]
                resultant_candidates.append((score, left, right))
        if not resultant_candidates:
            return {
                "epsilon": [epsilon_1, epsilon_2],
                "sigma": [sigma_c, sigma_o],
                "xi_index": xi_index,
                "pairing_index": pairing_index,
                "branch": branch,
                "status": "NO_RESULTANT_PAIR",
            }
        _, left, right = min(resultant_candidates)
        elimination_variable = left[2][0]
        from flint import fmpz_mod_mpoly_ctx, fmpz_mod_poly_ctx

        flint_context = fmpz_mod_mpoly_ctx.get(
            [str(elimination_variable), "r"], PRIME
        )
        elimination_index = all_targets.index(elimination_variable)

        def flint_component(component):
            component_terms = component.terms()
            common_denominator = component_terms[0][1].denom.ring.one
            for _, coefficient in component_terms:
                common_denominator = common_denominator.lcm(
                    coefficient.denom
                )
            output = {}
            for exponents, coefficient in component_terms:
                for index, exponent in enumerate(exponents):
                    if index != elimination_index and exponent:
                        raise ValueError(
                            "non-resultant target survived projection"
                        )
                multiplier = common_denominator.exquo(coefficient.denom)
                numerator = coefficient.numer*multiplier
                for (r_exponent,), scalar in numerator.terms():
                    key = (exponents[elimination_index], r_exponent)
                    output[key] = (
                        output.get(key, 0) + int(scalar)
                    ) % PRIME
            return flint_context.from_dict({
                key: coefficient
                for key, coefficient in output.items()
                if coefficient
            })

        left_polynomial = flint_component(left[1])
        right_polynomial = flint_component(right[1])
        print(json.dumps({
            "phase": "resultant",
            "case": list(case),
            "seconds": round(time.perf_counter()-started, 3),
            "variable": str(elimination_variable),
            "component_indices": [left[0], right[0]],
            "profiles": [left[3][1], right[3][1]],
            "denominator_degrees": [left[3][2], right[3][2]],
        }, sort_keys=True), flush=True)
        resultant = left_polynomial.resultant(
            right_polynomial, str(elimination_variable)
        )
        resultant_text = resultant.str()
        resultant_terms = list(resultant.terms())
        univariate_context = fmpz_mod_poly_ctx(PRIME)
        resultant_coefficients = {}
        for monomial, coefficient in resultant.to_dict().items():
            if monomial[0] != 0:
                raise ValueError("resultant variable was not eliminated")
            resultant_coefficients[monomial[1]] = int(coefficient)
        maximum_exponent = max(resultant_coefficients, default=0)
        resultant_univariate = univariate_context([
            resultant_coefficients.get(exponent, 0)
            for exponent in range(maximum_exponent+1)
        ])
        variable_univariate = univariate_context([0, 1])
        root_gcd = resultant_univariate.gcd(
            pow(variable_univariate, PRIME, resultant_univariate)
            - variable_univariate
        )
        _, root_factors = root_gcd.factor()
        roots = []
        root_factor_degrees = []
        for factor, multiplicity in root_factors:
            degree = int(factor.degree())
            root_factor_degrees.append([degree, int(multiplicity)])
            if degree == 1:
                roots.append(
                    -int(factor[0])*pow(int(factor[1]), -1, PRIME)
                    % PRIME
                )

        def evaluate_base_polynomial(polynomial, value):
            return sum(
                int(coefficient)*pow(value, exponent, PRIME)
                for (exponent,), coefficient in polynomial.terms()
            ) % PRIME

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

        def specialize_component(
            component, free_variable, assignments, r_value
        ):
            free_index = all_targets.index(free_variable)
            coefficients = {}
            for exponents, coefficient in component.terms():
                denominator = evaluate_base_polynomial(
                    coefficient.denom, r_value
                )
                if denominator == 0:
                    return None
                scalar = (
                    evaluate_base_polynomial(coefficient.numer, r_value)
                    * pow(denominator, -1, PRIME)
                ) % PRIME
                for index, target_variable in enumerate(all_targets):
                    exponent = exponents[index]
                    if not exponent or index == free_index:
                        continue
                    scalar = (
                        scalar
                        * pow(assignments[target_variable], exponent, PRIME)
                    ) % PRIME
                exponent = exponents[free_index]
                coefficients[exponent] = (
                    coefficients.get(exponent, 0) + scalar
                ) % PRIME
            maximum = max(coefficients, default=0)
            return univariate_context([
                coefficients.get(exponent, 0)
                for exponent in range(maximum+1)
            ])

        def polynomial_field_roots(polynomial):
            if polynomial.is_zero():
                return None
            if int(polynomial.degree()) == 0:
                return []
            field_gcd = polynomial.gcd(
                pow(variable_univariate, PRIME, polynomial)
                - variable_univariate
            )
            _, factors = field_gcd.factor()
            values = []
            for factor, _ in factors:
                if int(factor.degree()) != 1:
                    raise ValueError("field-root gcd has a nonlinear factor")
                values.append(
                    -int(factor[0])*pow(int(factor[1]), -1, PRIME)
                    % PRIME
                )
            return sorted(values)

        def evaluate_univariate(polynomial, value):
            return sum(
                int(polynomial[index])*pow(value, index, PRIME)
                for index in range(int(polynomial.degree())+1)
            ) % PRIME

        def direct_boundary_fiber(r_value, elimination_value):
            assignments = {elimination_variable: elimination_value}
            equation_pairs = []
            for equation in equations:
                constant = specialize_component(
                    equation.constant,
                    secondary_variable,
                    assignments,
                    r_value,
                )
                linear = specialize_component(
                    equation.linear,
                    secondary_variable,
                    assignments,
                    r_value,
                )
                if constant is None or linear is None:
                    return {"status": "COEFFICIENT_BOUNDARY"}
                if not constant.is_zero() or not linear.is_zero():
                    equation_pairs.append((constant, linear))

            curve_values = []
            for coefficient in (
                coefficient_a, coefficient_b, coefficient_c
            ):
                denominator = evaluate_base_polynomial(
                    coefficient.denom, r_value
                )
                if denominator == 0:
                    return {"status": "CURVE_BOUNDARY"}
                curve_values.append(
                    evaluate_base_polynomial(coefficient.numer, r_value)
                    * pow(denominator, -1, PRIME)
                    % PRIME
                )
            curve_a, curve_b, curve_c = curve_values
            cuts = []
            for constant, linear in equation_pairs:
                cuts.append(
                    curve_a*constant*constant
                    - curve_b*constant*linear
                    + curve_c*linear*linear
                )
            for left_pair, right_pair in itertools.combinations(
                equation_pairs, 2
            ):
                cuts.append(
                    left_pair[0]*right_pair[1]
                    - left_pair[1]*right_pair[0]
                )
            nonzero_cuts = [cut for cut in cuts if not cut.is_zero()]
            if not nonzero_cuts:
                return {
                    "status": "NO_A_CUT",
                    "equation_pair_count": len(equation_pairs),
                }
            common_a = nonzero_cuts[0]
            for cut in nonzero_cuts[1:]:
                common_a = common_a.gcd(cut)
            a_roots = polynomial_field_roots(common_a)
            solutions = []
            for a_value in a_roots:
                b_polynomials = [
                    univariate_context([curve_c, curve_b, curve_a])
                ]
                for constant, linear in equation_pairs:
                    b_polynomials.append(univariate_context([
                        evaluate_univariate(constant, a_value),
                        evaluate_univariate(linear, a_value),
                    ]))
                common_b = b_polynomials[0]
                for polynomial in b_polynomials[1:]:
                    common_b = common_b.gcd(polynomial)
                b_roots = polynomial_field_roots(common_b)
                if b_roots:
                    solutions.append({"a": a_value, "b_roots": b_roots})
            return {
                "status": "CHECKED",
                "equation_pair_count": len(equation_pairs),
                "cut_count": len(nonzero_cuts),
                "a_cut_degree": int(common_a.degree()),
                "a_roots": a_roots,
                "solutions": solutions,
            }

        secondary_variable = next(
            value for value in remaining if value != elimination_variable
        )
        root_rows = []
        for r_value in sorted(roots):
            zero_guards = []
            denominator_guards = []
            for name, guard in guard_values:
                if evaluate_base_polynomial(guard.denom, r_value) == 0:
                    denominator_guards.append(name)
                elif evaluate_base_polynomial(guard.numer, r_value) == 0:
                    zero_guards.append(name)
            row = {
                "r": r_value,
                "zero_guards": zero_guards,
                "denominator_guards": denominator_guards,
            }
            if zero_guards or denominator_guards:
                row["status"] = "GUARD_BOUNDARY"
                root_rows.append(row)
                continue
            left_specialized = specialize_component(
                left[1], elimination_variable, {}, r_value
            )
            right_specialized = specialize_component(
                right[1], elimination_variable, {}, r_value
            )
            if left_specialized is None or right_specialized is None:
                row["status"] = "COEFFICIENT_BOUNDARY"
                root_rows.append(row)
                continue
            common = left_specialized.gcd(right_specialized)
            elimination_roots = polynomial_field_roots(common)
            row["elimination_roots"] = elimination_roots
            if not elimination_roots:
                row["status"] = "NO_ELIMINATION_ROOT"
                root_rows.append(row)
                continue
            projected_solutions = []
            for elimination_value in elimination_roots:
                assignments = {elimination_variable: elimination_value}
                cutter_constant = specialize_component(
                    cutter.constant,
                    secondary_variable,
                    assignments,
                    r_value,
                )
                cutter_linear = specialize_component(
                    cutter.linear,
                    secondary_variable,
                    assignments,
                    r_value,
                )
                cutter_profile = {
                    "constant_degree": (
                        None if cutter_constant is None
                        else int(cutter_constant.degree())
                    ),
                    "constant_zero": (
                        None if cutter_constant is None
                        else cutter_constant.is_zero()
                    ),
                    "linear_degree": (
                        None if cutter_linear is None
                        else int(cutter_linear.degree())
                    ),
                    "linear_zero": (
                        None if cutter_linear is None
                        else cutter_linear.is_zero()
                    ),
                }
                direct_boundary = None
                if (
                    cutter_constant is not None
                    and cutter_linear is not None
                    and cutter_constant.is_zero()
                    and cutter_linear.is_zero()
                ):
                    direct_boundary = direct_boundary_fiber(
                        r_value, elimination_value
                    )
                common_secondary = None
                coefficient_boundary = False
                for component in target_singular_components:
                    specialized = specialize_component(
                        component, secondary_variable, assignments, r_value
                    )
                    if specialized is None:
                        coefficient_boundary = True
                        break
                    if specialized.is_zero():
                        continue
                    common_secondary = (
                        specialized
                        if common_secondary is None
                        else common_secondary.gcd(specialized)
                    )
                if coefficient_boundary:
                    projected_solutions.append({
                        str(elimination_variable): elimination_value,
                        "status": "COEFFICIENT_BOUNDARY",
                        "cutter": cutter_profile,
                        "direct_boundary": direct_boundary,
                    })
                    continue
                secondary_roots = (
                    None if common_secondary is None
                    else polynomial_field_roots(common_secondary)
                )
                projected_solutions.append({
                    str(elimination_variable): elimination_value,
                    f"{secondary_variable}_roots": secondary_roots,
                    "cutter": cutter_profile,
                    "direct_boundary": direct_boundary,
                })
            row["projected_solutions"] = projected_solutions
            row["status"] = "PROJECTED_CHECKED"
            root_rows.append(row)
        unresolved_roots = []
        for row in root_rows:
            if row["status"] in (
                "GUARD_BOUNDARY", "NO_ELIMINATION_ROOT"
            ):
                continue
            if row["status"] != "PROJECTED_CHECKED":
                unresolved_roots.append(row["r"])
                continue
            for solution in row["projected_solutions"]:
                direct = solution.get("direct_boundary")
                if direct is not None:
                    if (
                        direct.get("status") != "CHECKED"
                        or direct.get("solutions")
                    ):
                        unresolved_roots.append(row["r"])
                        break
                    continue
                secondary_roots = solution.get(
                    f"{secondary_variable}_roots"
                )
                if secondary_roots != []:
                    unresolved_roots.append(row["r"])
                    break
        case_excluded = not unresolved_roots
        return {
            "epsilon": [epsilon_1, epsilon_2],
            "sigma": [sigma_c, sigma_o],
            "xi_index": xi_index,
            "pairing_index": pairing_index,
            "branch": branch,
            "status": "COMPLETE",
            "unit": case_excluded,
            "case_excluded": case_excluded,
            "unresolved_roots": sorted(set(unresolved_roots)),
            "resultant_nonzero": bool(resultant),
            "resultant_degrees": [
                int(value) for value in resultant.degrees()
            ],
            "resultant_terms": len(resultant_terms),
            "field_root_gcd_degree": int(root_gcd.degree()),
            "field_root_factor_degrees": root_factor_degrees,
            "field_roots": sorted(roots),
            "field_root_rows": root_rows,
            "elimination_variable": str(elimination_variable),
            "component_indices": [left[0], right[0]],
            "component_profiles": [left[3][1], right[3][1]],
            "denominator_degrees": [left[3][2], right[3][2]],
            "total_seconds": time.perf_counter()-started,
            "left_sha256": hashlib.sha256(
                left_polynomial.str().encode()
            ).hexdigest(),
            "right_sha256": hashlib.sha256(
                right_polynomial.str().encode()
            ).hexdigest(),
            "resultant_sha256": hashlib.sha256(
                resultant_text.encode()
            ).hexdigest(),
            "resultant_zlib_base64": base64.b64encode(
                zlib.compress(resultant_text.encode(), level=9)
            ).decode(),
        }

    reduced = [materialize(equation) for equation in equations]
    curve_rows = [
        (coefficient_a, ["b^2"]),
        (coefficient_b, ["b"]),
        (coefficient_c, []),
    ]
    curve_text, curve_denominator_degree = serialize_rows(curve_rows)
    curve = (curve_text, [2, 3], curve_denominator_degree)
    r_common = CommonPair(r)
    univariate_route_pairs = {
        "r": r_common,
        "t": t_pair,
        "r2_minus_1": r_common*r_common-1,
        "r2_plus_1": r_common*r_common+1,
        "t2_minus_1": t_pair*t_pair-1,
        "t2_plus_1": t_pair*t_pair+1,
        "t2_minus_r2": t_pair*t_pair-r_common*r_common,
        "t2_plus_r2": t_pair*t_pair+r_common*r_common,
    }
    univariate_route_guards = []
    for guard_name, guard in univariate_route_pairs.items():
        if guard.linear != base_field.zero:
            raise ValueError(f"univariate route guard {guard_name} depends on b")
        univariate_route_guards.append((guard_name, guard.constant.numer))

    def strip_route_factors(polynomial):
        route_removed = {}
        for guard_name, guard_polynomial in univariate_route_guards:
            removed = 0
            while True:
                route_gcd = polynomial.gcd(guard_polynomial)
                if route_gcd.degree() == 0:
                    break
                removed += route_gcd.degree()
                polynomial = polynomial.exquo(route_gcd)
            if removed:
                route_removed[guard_name] = removed
        return polynomial, route_removed

    parameter_cuts = []
    for equation_index, equation in enumerate(equations):
        constant_terms = equation.constant.terms()
        linear_terms = equation.linear.terms()
        if any(any(exponents) for exponents, _ in (*constant_terms, *linear_terms)):
            continue
        constant = constant_terms[0][1] if constant_terms else base_field.zero
        linear = linear_terms[0][1] if linear_terms else base_field.zero
        resultant = (
            coefficient_a*constant*constant
            - coefficient_b*constant*linear
            + coefficient_c*linear*linear
        )
        if resultant == base_field.zero:
            continue
        numerator = resultant.numer
        raw_degree = numerator.degree()
        leading_overlap_degree = numerator.gcd(linear.numer).degree()
        while True:
            leading_gcd = numerator.gcd(linear.numer)
            if leading_gcd.degree() == 0:
                break
            numerator = numerator.exquo(leading_gcd)
        after_leading_degree = numerator.degree()
        numerator, route_removed = strip_route_factors(numerator)
        boundary = constant.numer.gcd(linear.numer)
        boundary_raw_degree = boundary.degree()
        boundary, boundary_route_removed = strip_route_factors(boundary)
        boundary_factors = []
        if boundary.degree() > 0:
            _, factors = sp.factor_list(
                sp.Poly(boundary.as_expr(), r, modulus=PRIME)
            )
            boundary_factors = [
                {
                    "degree": factor.degree(),
                    "terms": len(factor.terms()),
                    "multiplicity": multiplicity,
                    "text": str(factor.as_expr()).replace("**", "^"),
                }
                for factor, multiplicity in factors
            ]
        parameter_cuts.append({
            "equation_index": equation_index,
            "text": base_polynomial(numerator),
            "degree": numerator.degree(),
            "terms": len(numerator.terms()),
            "raw_degree": raw_degree,
            "removed_boundary_degree": raw_degree-after_leading_degree,
            "route_removed_degree": after_leading_degree-numerator.degree(),
            "leading_overlap_degree": leading_overlap_degree,
            "leading_gcd_degree": numerator.gcd(linear.numer).degree(),
            "route_removed": route_removed,
            "boundary_raw_degree": boundary_raw_degree,
            "boundary_degree": boundary.degree(),
            "boundary_terms": len(boundary.terms()),
            "boundary_route_removed": boundary_route_removed,
            "boundary_factors": boundary_factors,
            "constant": constant,
            "linear": linear,
        })
    print(json.dumps({"phase": "materialized", "seconds": round(time.perf_counter()-started, 3)}), flush=True)

    cut_profiles = [
        {
            "equation_index": cut["equation_index"],
            "degree": cut["degree"],
            "terms": cut["terms"],
            "raw_degree": cut["raw_degree"],
            "removed_boundary_degree": cut["removed_boundary_degree"],
            "route_removed_degree": cut["route_removed_degree"],
            "leading_overlap_degree": cut["leading_overlap_degree"],
            "leading_gcd_degree": cut["leading_gcd_degree"],
            "route_removed": cut["route_removed"],
            "boundary_raw_degree": cut["boundary_raw_degree"],
            "boundary_degree": cut["boundary_degree"],
            "boundary_terms": cut["boundary_terms"],
            "boundary_route_removed": cut["boundary_route_removed"],
            "open_cut_sha256": hashlib.sha256(
                cut["text"].encode()
            ).hexdigest(),
            "boundary_factors": [
                {
                    **{key: value for key, value in factor.items()
                       if key != "text"},
                    "sha256": hashlib.sha256(
                        factor["text"].encode()
                    ).hexdigest(),
                }
                for factor in cut["boundary_factors"]
            ],
        }
        for cut in parameter_cuts
    ]
    use_projection = (
        len(parameter_cuts) == 1
        and parameter_cuts[0]["leading_gcd_degree"] == 0
    )
    if branch in ("target_singular", "rankone_singular"):
        projected = [
            materialize_component(value)
            for value in target_singular_components
            if value
        ]
        definitions = [
            f"poly p{index}={value[0]};"
            for index, value in enumerate(projected)
        ]
        generators = ",".join(
            f"p{index}" for index in range(len(projected))
        )
        solver_variables = remaining
        solver_equations = [value[1] for value in projected]
        solver_denominators = [value[2] for value in projected]
        program_body = f"ideal G={generators}; G=slimgb(G);"
        solver_mode = (
            "rankone_target_projection_singular"
            if branch == "rankone_singular"
            else "target_projection_singular"
        )
        cutter_index = target_singular_cutter_index
    elif branch == "boundary":
        if len(parameter_cuts) != 1:
            raise ValueError("boundary mode requires exactly one target-free cut")
        cut = parameter_cuts[0]
        if not 0 <= factor_index < len(cut["boundary_factors"]):
            raise ValueError("boundary factor index out of range")
        cutter_index = cut["equation_index"]
        boundary_equations = [
            curve,
            *(value for index, value in enumerate(reduced) if index != cutter_index),
        ]
        definitions = [
            *(f"poly q{index}={value[0]};" for index, value in enumerate(boundary_equations)),
            f"poly z0={cut['boundary_factors'][factor_index]['text']};",
        ]
        generators = ",".join((
            *(f"q{index}" for index in range(len(boundary_equations))),
            "z0",
        ))
        solver_variables = variables
        solver_equations = [value[1] for value in boundary_equations]
        solver_denominators = [value[2] for value in boundary_equations]
        program_body = f"ideal G={generators}; G=slimgb(G);"
        solver_mode = "linear_pair_boundary"
    elif branch in ("open", "complete") and use_projection:
        cut = parameter_cuts[0]
        cutter_index = cut["equation_index"]
        projected_components = [
            equation.constant*cut["linear"]-equation.linear*cut["constant"]
            for index, equation in enumerate(equations)
            if index != cutter_index
        ]
        projected = [materialize_component(value) for value in projected_components]
        open_definitions = [
            *(f"poly p{index}={value[0]};" for index, value in enumerate(projected)),
            f"poly z0={cut['text']};",
        ]
        open_generators = ",".join((
            *(f"p{index}" for index in range(len(projected))),
            "z0",
        ))
        if branch == "complete":
            boundary_equations = [
                curve,
                *(value for index, value in enumerate(reduced)
                  if index != cutter_index),
            ]
            boundary_definitions = [
                *(f"poly q{index}={value[0]};"
                  for index, value in enumerate(boundary_equations)),
                *(f"poly bf{index}={factor['text']};"
                  for index, factor in enumerate(cut["boundary_factors"])),
            ]
            boundary_generators = ",".join(
                f"q{index}" for index in range(len(boundary_equations))
            )
            boundary_blocks = []
            for index in range(len(cut["boundary_factors"])):
                boundary_blocks.append(f"""
ideal GB{index}={boundary_generators},bf{index}; GB{index}=slimgb(GB{index});
print("BOUNDARY_{index}_BEGIN");
print("BOUNDARY_{index}_DIM="+string(dim(GB{index})));
print("BOUNDARY_{index}_SIZE="+string(size(GB{index})));
if ((size(GB{index})==1) && (GB{index}[1]==1))
{{ print("BOUNDARY_{index}_UNIT=1"); }}
else {{ print("BOUNDARY_{index}_UNIT=0"); print(GB{index}); }}
print("BOUNDARY_{index}_END");
""")
            definitions = [*open_definitions, *boundary_definitions]
            solver_variables = variables
            solver_equations = {
                "open": [value[1] for value in projected],
                "boundary": [value[1] for value in boundary_equations],
            }
            solver_denominators = {
                "open": [value[2] for value in projected],
                "boundary": [value[2] for value in boundary_equations],
            }
            program_body = f"""
ideal GO={open_generators}; GO=slimgb(GO);
print("OPEN_BEGIN");
print("OPEN_DIM="+string(dim(GO)));
print("OPEN_SIZE="+string(size(GO)));
if ((size(GO)==1) && (GO[1]==1)) {{ print("OPEN_UNIT=1"); }}
else {{ print("OPEN_UNIT=0"); print(GO); }}
print("OPEN_END");
{''.join(boundary_blocks)}
"""
            solver_mode = "linear_pair_complete"
        else:
            definitions = open_definitions
            solver_variables = remaining
            solver_equations = [value[1] for value in projected]
            solver_denominators = [value[2] for value in projected]
            program_body = f"ideal G={open_generators}; G=slimgb(G);"
            solver_mode = "linear_pair_projection"
    else:
        definitions = [f"poly q0={curve[0]};"]
        definitions.extend(
            f"poly q{index+1}={polynomial[0]};"
            for index, polynomial in enumerate(reduced)
        )
        definitions.extend(
            f"poly z{index}={cut['text']};"
            for index, cut in enumerate(parameter_cuts)
        )
        generators = ",".join((
            *(f"q{index}" for index in range(1+len(reduced))),
            *(f"z{index}" for index in range(len(parameter_cuts))),
        ))
        solver_variables = variables
        solver_equations = [polynomial[1] for polynomial in (curve, *reduced)]
        solver_denominators = [polynomial[2] for polynomial in (curve, *reduced)]
        program_body = f"ideal G={generators}; G=slimgb(G);"
        solver_mode = "full_block"
    variable_names = ",".join(str(value) for value in solver_variables)
    if branch == "complete":
        report_body = 'print("COMPLETE_END");'
    else:
        report_body = """
print("BEGIN");
print("DIM="+string(dim(G)));
print("SIZE="+string(size(G)));
if ((size(G)==1) && (G[1]==1)) { print("UNIT=1"); }
else { print("UNIT=0"); print(G); }
print("END");
"""
    program = f"""
ring R={PRIME},({variable_names},r),(dp({len(solver_variables)}),dp(1));
option(redSB);
{chr(10).join(definitions)}
{program_body}
{report_body}
quit;
"""
    compile_seconds = time.perf_counter()-started
    print(json.dumps({
        "phase": "compiled",
        "case": list(case),
        "seconds": round(compile_seconds, 3),
        "mode": solver_mode,
        "variables": [str(value) for value in solver_variables],
        "equations": solver_equations,
        "outside_supports": equation_supports,
        "parameter_cuts": cut_profiles,
        "cleared_denominator_degrees": solver_denominators,
    }, sort_keys=True), flush=True)
    try:
        process = subprocess.run(
            ["Singular", "--quiet"],
            input=program,
            capture_output=True,
            text=True,
            timeout=180,
        )
    except subprocess.TimeoutExpired as error:
        partial_stdout = error.stdout or ""
        partial_stderr = error.stderr or ""
        if isinstance(partial_stdout, bytes):
            partial_stdout = partial_stdout.decode(errors="replace")
        if isinstance(partial_stderr, bytes):
            partial_stderr = partial_stderr.decode(errors="replace")
        return {
            "epsilon": [epsilon_1, epsilon_2],
            "sigma": [sigma_c, sigma_o],
            "xi_index": xi_index,
            "pairing_index": pairing_index,
            "branch": branch,
            "factor_index": factor_index,
            "status": "TIMEOUT",
            "compile_seconds": compile_seconds,
            "outside_supports": equation_supports,
            "parameter_cuts": cut_profiles,
            "mode": solver_mode,
            "partial_stdout": partial_stdout[-4000:],
            "partial_stderr": partial_stderr[-1000:],
            "definitions_sha256": hashlib.sha256(
                "\n".join(definitions).encode()
            ).hexdigest(),
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }
    stdout = process.stdout
    if branch == "complete":
        open_dimensions = re.findall(r"OPEN_DIM=(-?\d+)", stdout)
        open_sizes = re.findall(r"OPEN_SIZE=(\d+)", stdout)
        open_unit = bool(re.search(r"(?:^|\n)OPEN_UNIT=1(?:\n|$)", stdout))
        boundary_results = []
        for index, factor in enumerate(parameter_cuts[0]["boundary_factors"]):
            dimensions = re.findall(
                rf"BOUNDARY_{index}_DIM=(-?\d+)", stdout
            )
            sizes = re.findall(rf"BOUNDARY_{index}_SIZE=(\d+)", stdout)
            factor_unit = bool(re.search(
                rf"(?:^|\n)BOUNDARY_{index}_UNIT=1(?:\n|$)", stdout
            ))
            boundary_results.append({
                "factor_index": index,
                "factor_sha256": hashlib.sha256(
                    factor["text"].encode()
                ).hexdigest(),
                "unit": factor_unit,
                "dimension": int(dimensions[-1]) if dimensions else None,
                "basis_size": int(sizes[-1]) if sizes else None,
            })
        valid = (
            process.returncode == 0
            and "COMPLETE_END" in stdout
            and "OPEN_END" in stdout
            and all(f"BOUNDARY_{index}_END" in stdout
                    for index in range(len(boundary_results)))
            and "?" not in stdout
        )
        unit = open_unit and all(row["unit"] for row in boundary_results)
        return {
            "epsilon": [epsilon_1, epsilon_2],
            "sigma": [sigma_c, sigma_o],
            "xi_index": xi_index,
            "pairing_index": pairing_index,
            "branch": branch,
            "factor_index": factor_index,
            "status": "COMPLETE" if valid else "ERROR",
            "unit": unit,
            "open_unit": open_unit,
            "open_dimension": int(open_dimensions[-1]) if open_dimensions else None,
            "open_basis_size": int(open_sizes[-1]) if open_sizes else None,
            "boundary_results": boundary_results,
            "mode": solver_mode,
            "variables": [str(value) for value in solver_variables],
            "equations": solver_equations,
            "parameter_cuts": cut_profiles,
            "inverse_guard_count": len(inverse_guards),
            "compile_seconds": compile_seconds,
            "total_seconds": time.perf_counter()-started,
            "stdout": stdout[-30000:],
            "stderr": process.stderr[-2000:],
            "definitions_sha256": hashlib.sha256(
                "\n".join(definitions).encode()
            ).hexdigest(),
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }
    dimensions = re.findall(r"DIM=(-?\d+)", stdout)
    sizes = re.findall(r"SIZE=(\d+)", stdout)
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
    unit = bool(re.search(r"(?:^|\n)UNIT=1(?:\n|$)", stdout))
    return {
        "epsilon": [epsilon_1, epsilon_2],
        "sigma": [sigma_c, sigma_o],
        "xi_index": xi_index,
        "pairing_index": pairing_index,
        "branch": branch,
        "factor_index": factor_index,
        "status": "COMPLETE" if valid else "ERROR",
        "unit": unit,
        "dimension": int(dimensions[-1]) if dimensions else None,
        "basis_size": int(sizes[-1]) if sizes else None,
        "mode": solver_mode,
        "variables": [str(value) for value in solver_variables],
        "equations": [
            {"degree": profile[0], "terms": profile[1]}
            for profile in solver_equations
        ],
        "parameter_cuts": cut_profiles,
        "inverse_guard_count": len(inverse_guards),
        "compile_seconds": compile_seconds,
        "total_seconds": time.perf_counter()-started,
        "stdout": stdout[-30000:],
        "stderr": process.stderr[-2000:],
        "definitions_sha256": hashlib.sha256(
            "\n".join(definitions).encode()
        ).hexdigest(),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "input_polynomials": [] if unit else definitions,
    }


@app.local_entrypoint()
def main(
    signs: str = "-1:-1",
    lanes: str = "-1:-1",
    xi_indices: str = "3",
    pairing_indices: str = "0",
    branch: str = "target",
    factor_indices: str = "0",
    output_name: str = RESULT.name,
):
    selected_signs = tuple(
        tuple(int(item) for item in value.split(":"))
        for value in signs.split(",") if value
    )
    selected_lanes = tuple(
        tuple(int(item) for item in value.split(":"))
        for value in lanes.split(",") if value
    )
    selected_xi = tuple(int(value) for value in xi_indices.split(",") if value)
    selected_pairings = tuple(
        int(value) for value in pairing_indices.split(",") if value
    )
    if branch not in (
        "target", "target_singular", "rankone_singular",
        "rankone_profile", "rankone_resultant", "rankone_chain",
        "rankone_targetfree",
        "open", "boundary", "complete"
    ):
        raise ValueError("unsupported branch")
    selected_factors = (
        (-1,) if branch in (
            "target", "target_singular", "rankone_singular",
            "rankone_profile", "rankone_resultant", "rankone_chain",
            "rankone_targetfree",
            "open", "complete"
        )
        else tuple(int(value) for value in factor_indices.split(",") if value)
    )
    cases = tuple(
        (*source_signs, *target_signs, xi_index, pairing_index, branch, factor_index)
        for source_signs in selected_signs
        for target_signs in selected_lanes
        for xi_index in selected_xi
        for pairing_index in selected_pairings
        for factor_index in selected_factors
    )
    raw = list(decide_case.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]),
                "sigma": list(case[2:4]),
                "xi_index": case[4],
                "pairing_index": case[5],
                "branch": case[6],
                "factor_index": case[7],
                "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell14-target-projection-v1",
        "app": "rs-mca-positive-433-1b-cell14-target-projection",
        "scope": "Discovery-only generic target-dependent b projections.",
        "field": PRIME,
        "source_curve_sha256": hashlib.sha256(CURVE.read_bytes()).hexdigest(),
        "source_script_sha256": hashlib.sha256(
            Path(__file__).read_bytes()
        ).hexdigest(),
        "selection": {
            "signs": [list(value) for value in selected_signs],
            "lanes": [list(value) for value in selected_lanes],
            "xi_indices": list(selected_xi),
            "pairing_indices": list(selected_pairings),
            "branch": branch,
            "factor_indices": list(selected_factors),
        },
        "case_count": len(rows),
        "status_counts": {
            status: sum(row["status"] == status for row in rows)
            for status in sorted({row["status"] for row in rows})
        },
        "unit_count": sum(row.get("unit", False) for row in rows),
        "rows": rows,
    }
    output_path = DIRECTORY / Path(output_name).name
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(output_path),
        "status_counts": output["status_counts"],
        "unit_count": output["unit_count"],
        "failures": [
            [row.get("epsilon"), row.get("sigma"), row.get("xi_index"),
             row.get("pairing_index"), row.get("branch"), row.get("factor_index"),
             row.get("status"), row.get("unit")]
            for row in rows
            if row.get("status") != "COMPLETE" or not row.get("unit")
        ],
    }, sort_keys=True))
