#!/usr/bin/env python3
"""Exact regular-fiber pilot for the signed-pair/colored-edge gcd."""

import json
import sys
import warnings
from pathlib import Path

import sympy as sp
from sympy.utilities.exceptions import SymPyDeprecationWarning


warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)


HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import check_rate_half_kb_positive_433_1a_cell5_pair_generic_guard_units as guards
import check_rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map as maps
import check_rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization as factors
from rate_half_kb_positive_433_1a_cell5_sparse_edge_probe import sparse_product_kernel


P = guards.PRIME
T = guards.FIBER
ZERO = [0]
ONE = [1]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def base_gcd(left, right):
    left, right = guards.trim(left), guards.trim(right)
    while right != ZERO:
        _, remainder = guards.divmod_poly(left, right)
        left, right = right, remainder
    inverse = pow(left[-1], -1, P)
    return guards.trim([inverse * value for value in left])


def irreducible(modulus):
    degree = len(modulus) - 1
    if degree == 1:
        return True
    x = [0, 1]
    power = x
    checkpoints = {}
    for index in range(1, degree + 1):
        power = guards.power_mod(power, P, modulus)
        checkpoints[index] = power
    if guards.subtract(checkpoints[degree], x) != ZERO:
        return False
    prime_divisors = {
        divisor
        for divisor in range(2, degree + 1)
        if degree % divisor == 0
        and all(divisor % candidate for candidate in range(2, int(divisor**0.5) + 1))
    }
    return all(
        base_gcd(guards.subtract(checkpoints[degree // divisor], x), modulus)
        == ONE
        for divisor in prime_divisors
    )


def ef_add(left, right, modulus):
    return guards.reduce_mod(guards.add(left, right), modulus)


def ef_negate(value, modulus):
    return guards.reduce_mod(guards.negate(value), modulus)


def ef_subtract(left, right, modulus):
    return ef_add(left, ef_negate(right, modulus), modulus)


def ef_multiply(left, right, modulus):
    return guards.multiply_mod(left, right, modulus)


def ef_scale(value, scalar, modulus):
    return guards.reduce_mod([scalar * item for item in value], modulus)


def ep_trim(polynomial):
    result = [item[:] for item in polynomial]
    while len(result) > 1 and result[-1] == ZERO:
        result.pop()
    return result


def ep_constant(value):
    return [value]


def ep_add(left, right, modulus):
    size = max(len(left), len(right))
    return ep_trim([
        ef_add(
            left[index] if index < len(left) else ZERO,
            right[index] if index < len(right) else ZERO,
            modulus,
        )
        for index in range(size)
    ])


def ep_negate(polynomial, modulus):
    return ep_trim([ef_negate(value, modulus) for value in polynomial])


def ep_subtract(left, right, modulus):
    return ep_add(left, ep_negate(right, modulus), modulus)


def ep_multiply(left, right, modulus):
    result = [ZERO] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] = ef_add(
                result[left_index + right_index],
                ef_multiply(left_value, right_value, modulus),
                modulus,
            )
    return ep_trim(result)


def ep_scale(polynomial, value, modulus):
    return ep_trim([ef_multiply(item, value, modulus) for item in polynomial])


def ep_power(polynomial, exponent, modulus):
    result = ep_constant(ONE)
    while exponent:
        if exponent & 1:
            result = ep_multiply(result, polynomial, modulus)
        polynomial = ep_multiply(polynomial, polynomial, modulus)
        exponent >>= 1
    return result


def ep_divmod(dividend, divisor, modulus):
    dividend = ep_trim(dividend)
    divisor = ep_trim(divisor)
    require(divisor != [ZERO], "zero extension-polynomial divisor")
    quotient = [ZERO] * max(1, len(dividend) - len(divisor) + 1)
    inverse = guards.inverse_mod(divisor[-1], modulus)
    while dividend != [ZERO] and len(dividend) >= len(divisor):
        shift = len(dividend) - len(divisor)
        scale = ef_multiply(dividend[-1], inverse, modulus)
        quotient[shift] = scale
        for index, value in enumerate(divisor):
            dividend[index + shift] = ef_subtract(
                dividend[index + shift],
                ef_multiply(scale, value, modulus),
                modulus,
            )
        dividend = ep_trim(dividend)
    return ep_trim(quotient), dividend


def ep_gcd(left, right, modulus):
    left, right = ep_trim(left), ep_trim(right)
    while right != [ZERO]:
        _, remainder = ep_divmod(left, right, modulus)
        left, right = right, remainder
    inverse = guards.inverse_mod(left[-1], modulus)
    return ep_scale(left, inverse, modulus)


def setup(chart_index=2):
    coordinate_maps, _, _, _ = maps.verify()
    generic_factors, _ = factors.verify()
    atlas = json.loads(guards.ATLAS.read_text())
    chart = {item["basis_index"]: item for item in atlas["c_charts"]}[
        chart_index
    ]
    a2, a0, _, _, _ = sparse_product_kernel()
    return coordinate_maps, generic_factors, atlas, chart, [str(x) for x in a2], [str(x) for x in a0]


def split_specialized_factor(polynomial):
    s = sp.symbols("s")
    expression = sum(
        coefficient * s**index for index, coefficient in enumerate(polynomial)
    )
    _, factorization = sp.factor_list(sp.Poly(expression, s, modulus=P))
    result = []
    for factor, multiplicity in factorization:
        require(multiplicity == 1, "specialized factor is not squarefree")
        monic = factor.monic()
        coefficients = [
            int(monic.nth(index)) % P
            for index in range(monic.degree() + 1)
        ]
        require(irreducible(coefficients), "finite-field factor is not irreducible")
        result.append(coefficients)
    return result


def main(chart_index=2):
    coordinate_maps, generic_factors, atlas, chart, a2_text, a0_text = setup(
        chart_index
    )
    specialized_maps = {
        name: [maps.evaluate_fraction(record, T) for record in records]
        for name, records in coordinate_maps.items()
    }
    rows = []
    for factor_index, generic_factor in enumerate(generic_factors, start=1):
        specialized_parent = guards.trim([
            factors.evaluate_rational(value, T) for value in generic_factor
        ])
        finite_factors = split_specialized_factor(specialized_parent)
        parent_rows = []
        for finite_index, modulus in enumerate(finite_factors, start=1):
            b = guards.reduce_mod(specialized_maps["b"], modulus)
            x0 = guards.reduce_mod(specialized_maps["x0"], modulus)
            x1 = guards.reduce_mod(specialized_maps["x1"], modulus)
            environment = {"b": b, "t": [T]}
            r = ef_negate(
            ef_multiply(
                guards.expression_mod(atlas["r_chart"]["constant"], environment, modulus),
                guards.inverse_mod(
                    guards.expression_mod(atlas["r_chart"]["leading"], environment, modulus),
                    modulus,
                ),
                modulus,
            ),
            modulus,
        )
            environment["r"] = r
            c = ef_negate(
            ef_multiply(
                guards.expression_mod(chart["constant"], environment, modulus),
                guards.inverse_mod(
                    guards.expression_mod(chart["leading"], environment, modulus),
                    modulus,
                ),
                modulus,
            ),
            modulus,
        )
            environment["c"] = c
            d = [guards.expression_mod(text, environment, modulus) for text in a2_text]
            n = [guards.expression_mod(text, environment, modulus) for text in a0_text]
            delta = [T * T * (T * T - 1) % P]
            delta_squared = ef_multiply(delta, delta, modulus)
            t_squared = [T * T % P]
            t_fourth = [pow(T, 4, P)]
            d_at_t_squared = ef_add(
            d[0],
            ef_add(
                ef_multiply(d[1], t_squared, modulus),
                ef_multiply(d[2], t_fourth, modulus),
                modulus,
            ),
            modulus,
        )
            beta = ef_negate(
            ef_multiply(
                ef_multiply([T], ef_add(ONE, b, modulus), modulus),
                d_at_t_squared,
                modulus,
            ),
            modulus,
        )
            d0 = ef_add(d[0], ef_add(ef_multiply(d[1], x0, modulus), ef_multiply(d[2], ef_multiply(x0, x0, modulus), modulus), modulus), modulus)
            n0 = ef_add(n[0], ef_add(ef_multiply(n[1], x0, modulus), ef_multiply(n[2], ef_multiply(x0, x0, modulus), modulus), modulus), modulus)
            q0_squared = ef_multiply(
            x0,
            ef_multiply(
                ef_multiply(beta, beta, modulus),
                ef_multiply(ef_subtract(x0, ONE, modulus), ef_subtract(x0, ONE, modulus), modulus),
                modulus,
            ),
            modulus,
        )

            pair = [
            ef_multiply(delta_squared, ef_multiply(n0, n0, modulus), modulus),
            ZERO,
            ef_subtract(
                ef_scale(
                    ef_multiply(delta_squared, ef_multiply(n0, d0, modulus), modulus),
                    2,
                    modulus,
                ),
                q0_squared,
                modulus,
            ),
            ZERO,
            ef_multiply(delta_squared, ef_multiply(d0, d0, modulus), modulus),
        ]
            e = [ZERO, ONE]
            b_plus_e = ep_add(ep_constant(b), e, modulus)
            sum_squared = ep_power(b_plus_e, 2, modulus)
            product = ep_scale(e, b, modulus)
            A = ep_subtract(ep_constant(n[2]), ep_scale(product, d[2], modulus), modulus)
            B = ep_subtract(ep_constant(n[1]), ep_scale(product, d[1], modulus), modulus)
            C = ep_subtract(ep_constant(n[0]), ep_scale(product, d[0], modulus), modulus)
            scaled_sum = ep_scale(sum_squared, delta_squared, modulus)
            beta_squared = ef_multiply(beta, beta, modulus)
            q0 = ep_negate(ep_scale(scaled_sum, ef_multiply(d[0], d[0], modulus), modulus), modulus)
            q1 = ep_subtract(
            ep_constant(beta_squared),
            ep_scale(scaled_sum, ef_scale(ef_multiply(d[0], d[1], modulus), 2, modulus), modulus),
            modulus,
        )
            q2 = ep_subtract(
            ep_constant(ef_scale(beta_squared, -2, modulus)),
            ep_scale(
                scaled_sum,
                ef_add(
                    ef_multiply(d[1], d[1], modulus),
                    ef_scale(ef_multiply(d[0], d[2], modulus), 2, modulus),
                    modulus,
                ),
                modulus,
            ),
            modulus,
        )
            q3 = ep_subtract(
            ep_constant(beta_squared),
            ep_scale(scaled_sum, ef_scale(ef_multiply(d[1], d[2], modulus), 2, modulus), modulus),
            modulus,
        )
            q4 = ep_negate(ep_scale(scaled_sum, ef_multiply(d[2], d[2], modulus), modulus), modulus)
            r1 = ep_add(
            ep_add(
                ep_multiply(q4, ep_add(ep_negate(ep_power(B, 3, modulus), modulus), ep_scale(ep_multiply(ep_multiply(A, B, modulus), C, modulus), [2], modulus), modulus), modulus),
                ep_multiply(q3, ep_multiply(A, ep_subtract(ep_power(B, 2, modulus), ep_multiply(A, C, modulus), modulus), modulus), modulus),
                modulus,
            ),
            ep_add(
                ep_negate(ep_multiply(q2, ep_multiply(ep_power(A, 2, modulus), B, modulus), modulus), modulus),
                ep_multiply(q1, ep_power(A, 3, modulus), modulus),
                modulus,
            ),
            modulus,
        )
            r0 = ep_add(
            ep_add(
                ep_multiply(q4, ep_add(ep_negate(ep_multiply(ep_power(B, 2, modulus), C, modulus), modulus), ep_multiply(A, ep_power(C, 2, modulus), modulus), modulus), modulus),
                ep_multiply(q3, ep_multiply(ep_multiply(A, B, modulus), C, modulus), modulus),
                modulus,
            ),
            ep_add(
                ep_negate(ep_multiply(q2, ep_multiply(ep_power(A, 2, modulus), C, modulus), modulus), modulus),
                ep_multiply(q0, ep_power(A, 3, modulus), modulus),
                modulus,
            ),
            modulus,
        )
            compact = ep_add(
            ep_subtract(
                ep_multiply(A, ep_power(r0, 2, modulus), modulus),
                ep_multiply(B, ep_multiply(r0, r1, modulus), modulus),
                modulus,
            ),
            ep_multiply(C, ep_power(r1, 2, modulus), modulus),
            modulus,
        )
            colored, remainder = ep_divmod(compact, ep_power(A, 3, modulus), modulus)
            require(remainder == [ZERO], f"factor {factor_index} nonexact A^3 division")
            common = ep_gcd(pair, colored, modulus)
            row = {
                "factor": factor_index,
                "generic_factor_degree": len(specialized_parent) - 1,
                "finite_factor": finite_index,
                "finite_factor_degree": len(modulus) - 1,
                "finite_factor_polynomial": modulus,
                "coordinates": {"b": b, "x0": x0, "x1": x1, "r": r, "c": c},
                "pair_degree": len(ep_trim(pair)) - 1,
                "colored_degree": len(colored) - 1,
                "gcd_degree": len(common) - 1,
                "gcd": common,
            }
            rows.append(row)
            parent_rows.append(row)
        for row in parent_rows:
            row["generic_factor_has_coprime_piece"] = any(
                item["gcd_degree"] == 0 for item in parent_rows
            )
    print(json.dumps({"status": "COMPLETE", "fiber": T, "rows": rows}, sort_keys=True))


if __name__ == "__main__":
    main()
