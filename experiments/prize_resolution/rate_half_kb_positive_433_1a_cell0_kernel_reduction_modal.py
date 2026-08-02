#!/usr/bin/env python3
"""Reduce the cell-0 common coefficient kernel on its two lex branches."""

import hashlib
import json
from pathlib import Path
import subprocess

import modal


DIRECTORY = Path(__file__).parent
PROBE = DIRECTORY / "rate_half_kb_positive_433_1a_outside_edge_specialization_probe.py"
BASE = DIRECTORY / "rate_half_kb_positive_433_1a_product_base_rank_compiler.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell0_kernel_reduction_result.json"
REMOTE_PROBE = "/root/rate_half_kb_positive_433_1a_outside_edge_specialization_probe.py"
REMOTE_BASE = "/root/rate_half_kb_positive_433_1a_product_base_rank_compiler.py"
PRIME = 2130706433
BRANCH_ROOTS = (1547071505, 583634934)

app = modal.App("rs-mca-positive-433-1a-cell0-kernel-reduction")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(PROBE, REMOTE_PROBE)
    .add_local_file(BASE, REMOTE_BASE)
)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


@app.function(image=image, cpu=2.0, memory=4096, timeout=180)
def reduce_kernel():
    import functools
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from rate_half_kb_positive_433_1a_outside_edge_specialization_probe import (
        common_kernel,
    )

    a2, a0, b1, common_gcd, _ = common_kernel(0, -1, -1)
    names = ("a20", "a21", "a22", "a00", "a01", "a02", "b10", "b11")
    expressions = (*a2, *a0, *b1)
    r, c, b, t = sp.symbols("r c b t")

    def singular(expression):
        return str(
            sp.Poly(expression, r, c, b, t, modulus=PRIME).as_expr()
        ).replace("**", "^")

    definitions = "\n".join(
        f"poly {name}={singular(expression)};"
        for name, expression in zip(names, expressions)
    )
    reductions = "\n".join(
        f'print("{name}"); print(reduce({name},G));'
        for name in names
    )
    branch_reductions = "\n".join(
        (
            f'print("BEGIN_BRANCH_{root}");\n'
            + "\n".join(
                f'print("{name}"); '
                f'print(subst(reduce({name},G),b,{root})); '
                f'print(subst(subst(reduce({name},G),b,{root}),t,2));'
                for name in names
            )
            + f'\nprint("END_BRANCH_{root}");'
        )
        for root in BRANCH_ROOTS
    )
    program = f"""
ring R={PRIME},(r,c,b,t),lp;
option(redSB);
ideal L=
b2-6b+1,
ct4-16711679c-1056997377bt4-8355839bt2+1065353216b+1056997377t4-8355839t2-1065353216,
cb-33423356ct2-3c+16711680bt2-16711679b-16711680t2-16711679,
r+16711679t2;
ideal G=std(L);
{definitions}
print("BEGIN_REDUCTIONS");
{reductions}
print("END_REDUCTIONS");
{branch_reductions}
quit;
"""
    header = {
        "field": PRIME,
        "cell": 0,
        "epsilon": [-1, -1],
        "input_shape": {
            name: {
                "degree": sp.Poly(
                    expression, r, c, b, t, modulus=PRIME
                ).total_degree(),
                "terms": len(sp.Poly(
                    expression, r, c, b, t, modulus=PRIME
                ).terms()),
            }
            for name, expression in zip(names, expressions)
        },
        "common_gcd_shape": {
            "degree": sp.Poly(common_gcd, t, r, c, b,
                              modulus=PRIME).total_degree(),
            "terms": len(sp.Poly(common_gcd, t, r, c, b,
                                 modulus=PRIME).terms()),
        },
        "program_sha256": digest(program),
    }
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=145,
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""

        return {
            **header,
            "status": "TIMEOUT",
            "partial_stdout": decoded(error.stdout)[-50000:],
            "partial_stderr": decoded(error.stderr)[-4000:],
        }
    stdout = process.stdout
    valid = (
        process.returncode == 0
        and "END_REDUCTIONS" in stdout
        and all(f"END_BRANCH_{root}" in stdout for root in BRANCH_ROOTS)
        and "?" not in stdout
    )
    branch_rational_coefficients = []
    for root in BRANCH_ROOTS:
        denominator_c = root - 33423356 * t**2 - 3
        numerator_c = -(
            16711680 * root * t**2
            - 16711679 * root
            - 16711680 * t**2
            - 16711679
        )
        c_value = numerator_c / denominator_c
        substitutions = {
            r: -16711679 * t**2,
            c: c_value,
            b: root,
        }
        coefficients = {}
        rational_polynomials = {}
        for name, expression in zip(names, expressions):
            numerator, denominator = sp.fraction(
                sp.cancel(expression.subs(substitutions))
            )
            numerator_poly = sp.Poly(numerator, t, modulus=PRIME)
            denominator_poly = sp.Poly(denominator, t, modulus=PRIME)
            numerator_factors = sp.factor_list(numerator_poly)
            denominator_factors = sp.factor_list(denominator_poly)
            rational_polynomials[name] = (numerator_poly, denominator_poly)
            coefficients[name] = {
                "numerator": str(numerator_poly.as_expr()),
                "denominator": str(denominator_poly.as_expr()),
                "numerator_degree": numerator_poly.degree(),
                "denominator_degree": denominator_poly.degree(),
                "numerator_factors": [
                    {
                        "polynomial": str(factor.monic().as_expr()),
                        "degree": factor.degree(),
                        "multiplicity": multiplicity,
                    }
                    for factor, multiplicity in numerator_factors[1]
                ],
                "denominator_factors": [
                    {
                        "polynomial": str(factor.monic().as_expr()),
                        "degree": factor.degree(),
                        "multiplicity": multiplicity,
                    }
                    for factor, multiplicity in denominator_factors[1]
                ],
                "value_at_t2": (
                    int(numerator_poly.eval(2))
                    * pow(int(denominator_poly.eval(2)) % PRIME, -1, PRIME)
                ) % PRIME,
            }
        denominator_lcm = functools.reduce(
            sp.lcm, (pair[1] for pair in rational_polynomials.values())
        ).monic()
        cleared = {}
        for name, (numerator_poly, denominator_poly) in rational_polynomials.items():
            multiplier = denominator_lcm.exquo(denominator_poly)
            cleared[name] = sp.Poly(
                numerator_poly.as_expr() * multiplier.as_expr(),
                t, modulus=PRIME,
            )
        common_numerator = functools.reduce(sp.gcd, cleared.values()).monic()
        common_factorization = sp.factor_list(common_numerator)
        normalized = {}
        for name, polynomial in cleared.items():
            quotient = polynomial.exquo(common_numerator)
            factorization = sp.factor_list(quotient)
            normalized[name] = {
                "polynomial": str(quotient.as_expr()),
                "degree": quotient.degree(),
                "terms": len(quotient.terms()),
                "factors": [
                    {
                        "polynomial": str(factor.monic().as_expr()),
                        "degree": factor.degree(),
                        "multiplicity": multiplicity,
                    }
                    for factor, multiplicity in factorization[1]
                ],
                "value_at_t2": int(quotient.eval(2)) % PRIME,
            }
        branch_rational_coefficients.append({
            "b": root,
            "c_numerator": str(sp.Poly(
                numerator_c, t, modulus=PRIME
            ).as_expr()),
            "c_denominator": str(sp.Poly(
                denominator_c, t, modulus=PRIME
            ).as_expr()),
            "coefficients": coefficients,
            "common_scale": {
                "numerator": str(common_numerator.as_expr()),
                "numerator_degree": common_numerator.degree(),
                "numerator_factors": [
                    {
                        "polynomial": str(factor.monic().as_expr()),
                        "degree": factor.degree(),
                        "multiplicity": multiplicity,
                    }
                    for factor, multiplicity in common_factorization[1]
                ],
                "denominator": str(denominator_lcm.as_expr()),
                "denominator_degree": denominator_lcm.degree(),
            },
            "normalized_coefficients": normalized,
        })
    return {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "branch_roots": list(BRANCH_ROOTS),
        "branch_rational_coefficients": branch_rational_coefficients,
        "stdout": stdout[-50000:],
        "stderr": process.stderr[-4000:],
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell0-kernel-reduction-v1",
        "scope": (
            "Exact reduction of the unique common coefficient kernel on "
            "the two cell-0 lex branches; no outside, route, K3, or Prize claim."
        ),
        "result": reduce_kernel.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "status": output["result"].get("status"),
        "branches": output["result"].get("branch_roots", []),
    }, sort_keys=True))
