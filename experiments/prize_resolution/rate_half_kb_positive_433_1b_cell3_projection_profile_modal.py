#!/usr/bin/env python3
"""Profile exact factors and reciprocal quotients of the cell-3 projections."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
STRUCTURE = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_compact_structure_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_projection_profile_result.json"
REMOTE_STRUCTURE = "/root/structure.json"
PRIME = 2130706433
IOTA = 16711679

app = modal.App("rs-mca-positive-433-1b-cell3-projection-profile")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0", "sympy==1.14.0")
    .add_local_file(STRUCTURE, REMOTE_STRUCTURE)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=300)
def profile():
    import sympy as sp
    from flint import fmpz_mod_mpoly_ctx

    payload = json.loads(Path(REMOTE_STRUCTURE).read_text())
    t, r, c, b, x = sp.symbols("t r c b x")
    variables = (t, r, c, b)
    factor_context = fmpz_mod_mpoly_ctx.get(["t", "r", "c", "b"], PRIME)

    def summary(expression, polynomial_variables=variables):
        polynomial = sp.Poly(expression, *polynomial_variables, modulus=PRIME)
        text = str(polynomial.as_expr())
        return {
            "degree": polynomial.total_degree(),
            "terms": len(polynomial.terms()),
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
            "expression": text,
        }

    def monic(expression):
        return sp.Poly(expression, *variables, modulus=PRIME).monic().as_expr()

    def factor_profile(expression):
        sympy_polynomial = sp.Poly(expression, *variables, modulus=PRIME)
        polynomial = factor_context.from_dict({
            monomial: int(coefficient) % PRIME
            for monomial, coefficient in sympy_polynomial.terms()
        })
        coefficient, factors = polynomial.factor()
        reconstruction = factor_context.constant(int(coefficient))
        rows = []
        for factor, multiplicity in factors:
            reconstruction *= factor**multiplicity
            text = factor.str()
            rows.append({
                "degrees": [int(value) for value in factor.degrees()],
                "total_degree": int(factor.total_degree()),
                "terms": len(list(factor.terms())),
                "sha256": hashlib.sha256(text.encode()).hexdigest(),
                "expression": text,
                "multiplicity": int(multiplicity),
            })
        if reconstruction != polynomial:
            raise RuntimeError("factor reconstruction failed")
        return {
            "coefficient": int(coefficient) % PRIME,
            "factors": rows,
        }

    def reciprocal_quotient(expression, variable):
        polynomial = sp.Poly(expression, variable)
        degree = polynomial.degree()
        coefficients = [polynomial.coeff_monomial(variable**index)
                        for index in range(degree + 1)]
        palindromic = all(
            sp.Poly(coefficients[index] - coefficients[degree - index],
                    *variables, modulus=PRIME).is_zero
            for index in range(degree + 1)
        )
        if not palindromic or degree % 2:
            return {"palindromic": palindromic, "degree": degree}
        middle = degree // 2
        traces = [sp.Integer(2), x]
        for _ in range(2, middle + 1):
            traces.append(sp.expand(x * traces[-1] - traces[-2]))
        quotient = coefficients[middle]
        for offset in range(1, middle + 1):
            quotient += coefficients[middle + offset] * traces[offset]
        quotient = sp.Poly(
            quotient,
            x,
            *(value for value in variables if value != variable),
            modulus=PRIME,
        ).as_expr()
        reconstructed = sp.together(
            variable**middle * quotient.subs(x, variable + 1 / variable)
        )
        reconstructed = sp.Poly(
            sp.cancel(reconstructed), *variables, modulus=PRIME
        ).as_expr()
        exact = sp.Poly(
            reconstructed - expression, *variables, modulus=PRIME
        ).is_zero
        return {
            "palindromic": True,
            "degree": degree,
            "exact_reconstruction": exact,
            "quotient": summary(
                quotient,
                (x, *(value for value in variables if value != variable)),
            ),
            "quotient_factorization": factor_profile(quotient.subs(x, variable)),
        }

    representatives = [row for row in payload["rows"] if row["chart"] == 0]
    rows = []
    etr_by_sign = {}
    for row in representatives:
        projections = {}
        for name, records in row["projections"].items():
            if len(records) != 1:
                raise RuntimeError(f"unexpected {name} projection size")
            expression = sp.sympify(records[0]["expression"])
            variable = b if name in ("ebt", "erb") else c if name == "erc" else None
            projections[name] = {
                "factorization": factor_profile(expression),
                "reciprocal": (
                    reciprocal_quotient(expression, variable)
                    if variable is not None else None
                ),
            }
            if name == "etr":
                etr_by_sign[tuple(row["epsilon"])] = monic(expression)
        rows.append({"epsilon": row["epsilon"], "projections": projections})

    base_sign = (-1, -1)
    base = etr_by_sign[base_sign]
    sign_equivalences = {}
    units = (1, -1, IOTA, -IOTA)
    for target_sign, target in sorted(etr_by_sign.items()):
        witnesses = []
        for r_scale in units:
            for t_scale in units:
                transformed = monic(base.subs({r: r_scale * r, t: t_scale * t}))
                if sp.Poly(transformed - target, *variables, modulus=PRIME).is_zero:
                    witnesses.append({"r_scale": r_scale, "t_scale": t_scale})
        sign_equivalences[str(target_sign)] = witnesses

    return {
        "status": "COMPLETE",
        "field": PRIME,
        "rows": rows,
        "etr_sign_equivalences_from_minus_minus": sign_equivalences,
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell3-projection-profile-v1",
        "scope": (
            "Exact factor, reciprocal, and sign-equivalence profile of the "
            "cell-3 compact projections; no outside or route claim."
        ),
        "source_structure_sha256": hashlib.sha256(STRUCTURE.read_bytes()).hexdigest(),
        "result": profile.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "status": output["result"].get("status"),
        "sign_equivalences": output["result"].get(
            "etr_sign_equivalences_from_minus_minus"
        ),
        "projections": [
            {
                "epsilon": row["epsilon"],
                "profiles": {
                    name: {
                        "factors": len(value["factorization"]["factors"]),
                        "reciprocal": (
                            value["reciprocal"].get("palindromic")
                            if value["reciprocal"] else None
                        ),
                        "quotient": (
                            [value["reciprocal"]["quotient"]["degree"],
                             value["reciprocal"]["quotient"]["terms"]]
                            if value["reciprocal"]
                            and value["reciprocal"].get("quotient") else None
                        ),
                    }
                    for name, value in row["projections"].items()
                },
            }
            for row in output["result"].get("rows", [])
        ],
    }, sort_keys=True))
