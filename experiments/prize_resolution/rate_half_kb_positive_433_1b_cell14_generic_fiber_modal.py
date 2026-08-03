#!/usr/bin/env python3
"""Exact curve-fiber outside ideals for positive 433-1b cell 14.

The quadratic common curve is reduced exactly before the outside equations
are serialized.  A target-free paired equation then separates its open
projection from the finite exceptional parameter fibers.
"""

import hashlib
import itertools
import json
from pathlib import Path
import re
import subprocess
import time

import modal


DIRECTORY = Path(__file__).parent
CURVE = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_curve_kernel_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_generic_fiber_result.json"
REMOTE_CURVE = "/root/curve.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell14-generic-fiber")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
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
    a_pair, u_pair, v_pair, f_pair = (
        target[a], target[u], target[v], target[f]
    )
    remaining = tuple(value for value in (a, u, v, f) if value != primary)
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
            if exponents[all_targets.index(primary)] != 0:
                raise ValueError("eliminated target variable survived substitution")
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
    if branch == "boundary":
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
    xi_indices: str = "0",
    pairing_indices: str = "0",
    branch: str = "open",
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
    if branch not in ("open", "boundary", "complete"):
        raise ValueError("branch must be open, boundary, or complete")
    selected_factors = (
        (-1,) if branch in ("open", "complete")
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
        "schema": "rate-half-kb-positive-433-1b-cell14-generic-fiber-v2",
        "app": "rs-mca-positive-433-1b-cell14-generic-fiber",
        "scope": "Exact linear-pair open projections and finite boundary-factor ideals.",
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
