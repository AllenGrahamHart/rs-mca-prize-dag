#!/usr/bin/env python3
"""Enumerate finite H-colored fibers through the signed-pair lift."""

import hashlib
import json
from pathlib import Path
import re

import modal


DIRECTORY = Path(__file__).parent
PLANE = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_plane_kernel_flint_result.json"
HFACTOR = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_common_factor_6.txt"
BLIFT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_b_gcd_polynomial.txt"
COLORED = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_colored_x_reduce_polynomial.txt"
FROBENIUS = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_colored_coefficient_frobenius_result.json"
REDUCTION = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_colored_x_reduce_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_colored_candidate_atlas_result.json"
REMOTE = {
    PLANE: "/root/plane.json",
    HFACTOR: "/root/hfactor.txt",
    BLIFT: "/root/blift.txt",
    COLORED: "/root/colored.txt",
    FROBENIUS: "/root/frobenius.json",
    REDUCTION: "/root/reduction.json",
}
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell4-h-colored-candidate-atlas")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
)
for local_path, remote_path in REMOTE.items():
    image = image.add_local_file(local_path, remote_path)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


@app.function(image=image, cpu=4.0, memory=8192, timeout=300)
def build_atlas():
    from flint import fmpz_mod_poly_ctx

    univariate_context = fmpz_mod_poly_ctx(PRIME)

    def parse(value, variables):
        output = {}
        for raw_term in re.findall(r"[+-]?[^+-]+", value.replace(" ", "")):
            sign = 1
            term = raw_term
            if term.startswith("+"):
                term = term[1:]
            elif term.startswith("-"):
                sign = -1
                term = term[1:]
            coefficient = 1
            exponents = {name: 0 for name in variables}
            for factor in term.split("*"):
                if factor.isdigit():
                    coefficient = coefficient*int(factor) % PRIME
                    continue
                match = re.fullmatch(
                    rf"({'|'.join(variables)})(?:\^(\d+))?", factor
                )
                if match is None:
                    raise RuntimeError(f"cannot parse factor {factor!r}")
                variable, exponent = match.groups()
                exponents[variable] += int(exponent) if exponent else 1
            key = tuple(exponents[name] for name in variables)
            output[key] = (output.get(key, 0)+sign*coefficient) % PRIME
        return {key: coefficient for key, coefficient in output.items()
                if coefficient}

    def specialize_univariate(polynomial, variable_index, values):
        coefficients = {}
        for monomial, coefficient in polynomial.items():
            value = coefficient
            for index, point in values.items():
                value = value*pow(point, monomial[index], PRIME) % PRIME
            degree = monomial[variable_index]
            coefficients[degree] = (coefficients.get(degree, 0)+value) % PRIME
        maximum = max(coefficients, default=0)
        return univariate_context([
            coefficients.get(degree, 0) for degree in range(maximum+1)
        ])

    def evaluate(polynomial, values):
        total = 0
        for monomial, coefficient in polynomial.items():
            value = coefficient
            for index, point in values.items():
                value = value*pow(point, monomial[index], PRIME) % PRIME
            total = (total+value) % PRIME
        return total

    def linear_roots(polynomial):
        _, factors = polynomial.factor()
        roots = []
        rows = []
        for factor, multiplicity in factors:
            degree = int(factor.degree())
            row = {
                "degree": degree,
                "multiplicity": int(multiplicity),
                "sha256": digest(str(factor)),
            }
            if degree == 1:
                root = (-int(factor[0])*pow(int(factor[1]), -1, PRIME)) % PRIME
                roots.append(root)
                row["root"] = root
            rows.append(row)
        return sorted(set(roots)), rows

    def root_from_text(text, variable):
        compact = text.replace(" ", "")
        if compact == variable:
            return 0
        match = re.fullmatch(rf"{variable}\+(\d+)", compact)
        if match is None:
            raise RuntimeError(f"unexpected linear factor {text!r}")
        return (-int(match.group(1))) % PRIME

    plane_payload = json.loads(Path(REMOTE[PLANE]).read_text())["result"]
    frobenius_payload = json.loads(Path(REMOTE[FROBENIUS]).read_text())["result"]
    reduction_payload = json.loads(Path(REMOTE[REDUCTION]).read_text())["result"]

    h = parse(Path(REMOTE[HFACTOR]).read_text().strip(), ("w0", "t"))
    colored_full = parse(
        Path(REMOTE[COLORED]).read_text().strip(), ("x", "w0", "t")
    )
    if {monomial[0] for monomial in colored_full} != {4}:
        raise RuntimeError("colored projection is not exactly x^4 C")
    colored = {
        (monomial[1], monomial[2]): coefficient
        for monomial, coefficient in colored_full.items()
    }
    blift = parse(Path(REMOTE[BLIFT]).read_text().strip(), ("w0", "b", "t"))
    plane = parse(plane_payload["plane_polynomial"], ("b", "t"))
    rn = parse(plane_payload["r_numerator"], ("b", "t"))
    rd = parse(plane_payload["r_denominator"], ("b", "t"))
    normalized = {
        name: parse(row["polynomial"], ("b", "t"))
        for name, row in plane_payload["normalized_coefficients"].items()
    }

    root_factors = frobenius_payload["base_field_root_gcd"]["factors"]
    t_roots = sorted(root_from_text(row["text"], "x") for row in root_factors)
    content_roots = {
        root_from_text(row["text"], "t")
        for row in reduction_payload["content"]["factors"]
        if row["shape"]["degrees"][-1] == 1
    }

    rows = []
    for t_value in t_roots:
        t_guard = (
            t_value == 0
            or pow(t_value, 2, PRIME) in (1, PRIME-1)
        )
        h_t = specialize_univariate(h, 0, {1: t_value})
        c_t = specialize_univariate(colored, 0, {1: t_value})
        common = h_t.gcd(c_t)
        w0_roots, common_factors = linear_roots(common)
        row = {
            "t": t_value,
            "t_guard": t_guard,
            "content_exceptional": t_value in content_roots,
            "h_degree": int(h_t.degree()),
            "colored_degree": int(c_t.degree()),
            "common_degree": int(common.degree()),
            "common_sha256": digest(str(common)),
            "common_factors": common_factors,
            "w0_rows": [],
        }
        for w0_value in w0_roots:
            lift_b = specialize_univariate(
                blift, 1, {0: w0_value, 2: t_value}
            )
            lift_degree = int(lift_b.degree())
            if lift_degree != 1 or int(lift_b[1]) == 0:
                row["w0_rows"].append({
                    "w0": w0_value,
                    "lift_degree": lift_degree,
                    "lift_sha256": digest(str(lift_b)),
                    "status": "LIFT_LEADING_EXCEPTION",
                })
                continue
            b_value = (-int(lift_b[0])*pow(int(lift_b[1]), -1, PRIME)) % PRIME
            bt = {0: b_value, 1: t_value}
            coefficient_values = {
                name: evaluate(polynomial, bt)
                for name, polynomial in normalized.items()
            }

            def polynomial(prefix):
                return univariate_context([
                    coefficient_values[f"{prefix}{index}"]
                    for index in range(3)
                ])

            a2 = polynomial("a2")
            a0 = polynomial("a0")
            k = coefficient_values["b10"]
            w = univariate_context([0, 1])
            d0 = int(a2(w0_value))
            n0 = int(a0(w0_value))
            d1 = a2
            n1 = a0
            product = n1*d0+n0*d1
            sum_cut = (
                k*k*w0_value*(1-w0_value)*(1-w0_value)*d1*d1
                -k*k*w*(1-w)*(1-w)*d0*d0
                -4*n0*d0*d1*d1
            )
            pair_gcd = product.gcd(sum_cut)
            w1_roots, pair_factors = linear_roots(pair_gcd)

            rd_value = evaluate(rd, bt)
            rn_value = evaluate(rn, bt)
            r_guard_values = set()
            if rd_value != 0:
                r2 = rn_value*rn_value*pow(rd_value*rd_value % PRIME, -1, PRIME) % PRIME
                r_guard_values = {r2, (-r2) % PRIME}
            fixed_guards = {0, 1, PRIME-1, pow(t_value, 2, PRIME)} | r_guard_values
            w0_row = {
                "w0": w0_value,
                "b": b_value,
                "plane_zero": evaluate(plane, bt) == 0,
                "lift_degree": lift_degree,
                "w0_source_guard": w0_value in fixed_guards,
                "r_denominator_zero": rd_value == 0,
                "d0_zero": d0 == 0,
                "n0_zero": n0 == 0,
                "k_zero": k == 0,
                "pair_gcd_degree": int(pair_gcd.degree()),
                "pair_gcd_sha256": digest(str(pair_gcd)),
                "pair_factors": pair_factors,
                "w1_rows": [],
            }
            for w1_value in w1_roots:
                w0_row["w1_rows"].append({
                    "w1": w1_value,
                    "w1_source_guard": w1_value in fixed_guards,
                    "w1_equals_w0": w1_value == w0_value,
                    "d1_zero": int(a2(w1_value)) == 0,
                    "n1_zero": int(a0(w1_value)) == 0,
                })
            row["w0_rows"].append(w0_row)
        rows.append(row)

    return {
        "status": "COMPLETE",
        "field": PRIME,
        "t_root_count": len(t_roots),
        "content_linear_roots": sorted(content_roots),
        "rows": rows,
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell4-pair-exceptional-h-colored-candidate-atlas-v1",
        "scope": (
            "Exact finite specialization atlas for H=C=0, the generic "
            "linear b lift, original squared-label source guards, and the "
            "signed DE+/DE- pair. Content and lift-leading exceptional "
            "fibers, unsquared labels, colored BE replay, orbit, and Prize "
            "claims remain separate."
        ),
        "artifact_sha256": {
            path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in REMOTE
        },
        "result": build_atlas.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    result = output["result"]
    summary = []
    for row in result["rows"]:
        summary.append({
            "t": row["t"],
            "t_guard": row["t_guard"],
            "content_exceptional": row["content_exceptional"],
            "common_degree": row["common_degree"],
            "w0_count": len(row["w0_rows"]),
            "w1_count": sum(
                len(w0_row.get("w1_rows", [])) for w0_row in row["w0_rows"]
            ),
        })
    print(json.dumps({
        "result": str(RESULT),
        "status": result["status"],
        "t_root_count": result["t_root_count"],
        "summary": summary,
    }, sort_keys=True))
