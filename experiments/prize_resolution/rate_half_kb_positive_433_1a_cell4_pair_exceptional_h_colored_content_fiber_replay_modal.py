#!/usr/bin/env python3
"""Replay admissible colored-content fibers from the original equations."""

import hashlib
import json
from pathlib import Path
import re

import modal


DIRECTORY = Path(__file__).parent
PLANE = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_plane_kernel_flint_result.json"
HFACTOR = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_common_factor_6.txt"
LIVE = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_resultant_factor_2.txt"
LINEAR = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_w1_reconstruction_linear_factor_0.txt"
CONSTANT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_w1_reconstruction_constant_factor_1.txt"
REDUCTION = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_colored_x_reduce_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_colored_content_fiber_replay_result.json"
REMOTE = {
    PLANE: "/root/plane.json",
    HFACTOR: "/root/hfactor.txt",
    LIVE: "/root/live.txt",
    LINEAR: "/root/linear.txt",
    CONSTANT: "/root/constant.txt",
    REDUCTION: "/root/reduction.json",
}
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell4-h-colored-content-fibers")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
)
for local_path, remote_path in REMOTE.items():
    image = image.add_local_file(local_path, remote_path)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


@app.function(image=image, cpu=2.0, memory=8192, timeout=300)
def replay_content_fibers():
    from flint import fmpz_mod_poly_ctx

    variables = ("w0", "b", "t")
    context = fmpz_mod_poly_ctx(PRIME)

    def parse(value):
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
                match = re.fullmatch(r"(w0|b|t)(?:\^(\d+))?", factor)
                if match is None:
                    raise RuntimeError(f"cannot parse factor {factor!r}")
                variable, exponent = match.groups()
                exponents[variable] += int(exponent) if exponent else 1
            key = tuple(exponents[name] for name in variables)
            output[key] = (output.get(key, 0)+sign*coefficient) % PRIME
        return {key: coefficient for key, coefficient in output.items()
                if coefficient}

    def specialize(polynomial, variable_index, values):
        coefficients = {}
        for monomial, source_coefficient in polynomial.items():
            value = source_coefficient
            for index, point in values.items():
                value = value*pow(point, monomial[index], PRIME) % PRIME
            degree = monomial[variable_index]
            coefficients[degree] = (coefficients.get(degree, 0)+value) % PRIME
        maximum = max(coefficients, default=0)
        return context([
            coefficients.get(degree, 0) for degree in range(maximum+1)
        ])

    def evaluate(polynomial, values):
        total = 0
        for monomial, source_coefficient in polynomial.items():
            value = source_coefficient
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

    def root_from_text(text):
        compact = text.replace(" ", "")
        match = re.fullmatch(r"t\+(\d+)", compact)
        if match is None:
            raise RuntimeError(f"unexpected content factor {text!r}")
        return (-int(match.group(1))) % PRIME

    payload = json.loads(Path(REMOTE[PLANE]).read_text())["result"]
    reduction = json.loads(Path(REMOTE[REDUCTION]).read_text())["result"]
    content_roots = sorted({
        root_from_text(row["text"])
        for row in reduction["content"]["factors"]
        if row["shape"]["degrees"][-1] == 1
    })
    admissible_roots = [
        value for value in content_roots
        if value != 0 and pow(value, 2, PRIME) not in (1, PRIME-1)
    ]

    h = parse(Path(REMOTE[HFACTOR]).read_text().strip())
    original = {
        "plane": parse(payload["plane_polynomial"]),
        "linear": parse(Path(REMOTE[LINEAR]).read_text().strip()),
        "constant": parse(Path(REMOTE[CONSTANT]).read_text().strip()),
        "live": parse(Path(REMOTE[LIVE]).read_text().strip()),
    }
    normalized = {
        name: parse(row["polynomial"])
        for name, row in payload["normalized_coefficients"].items()
    }

    rows = []
    for t_value in admissible_roots:
        h_t = specialize(h, 0, {2: t_value})
        w0_roots, h_factors = linear_roots(h_t)
        row = {
            "t": t_value,
            "h_degree": int(h_t.degree()),
            "h_sha256": digest(str(h_t)),
            "h_factors": h_factors,
            "w0_rows": [],
        }
        for w0_value in w0_roots:
            b_polynomials = {
                name: specialize(polynomial, 1, {0: w0_value, 2: t_value})
                for name, polynomial in original.items()
            }
            common_b = b_polynomials["plane"]
            for name in ("linear", "constant", "live"):
                common_b = common_b.gcd(b_polynomials[name])
            b_roots, b_factors = linear_roots(common_b)
            w0_row = {
                "w0": w0_value,
                "common_b_degree": int(common_b.degree()),
                "common_b_sha256": digest(str(common_b)),
                "common_b_factors": b_factors,
                "b_rows": [],
            }
            for b_value in b_roots:
                bt = {1: b_value, 2: t_value}
                coefficient_values = {
                    name: evaluate(polynomial, bt)
                    for name, polynomial in normalized.items()
                }

                def polynomial(prefix):
                    return context([
                        coefficient_values[f"{prefix}{index}"]
                        for index in range(3)
                    ])

                a2 = polynomial("a2")
                a0 = polynomial("a0")
                k = coefficient_values["b10"]
                w = context([0, 1])
                d0 = int(a2(w0_value))
                n0 = int(a0(w0_value))
                product = a0*d0+n0*a2
                sum_cut = (
                    k*k*w0_value*(1-w0_value)*(1-w0_value)*a2*a2
                    -k*k*w*(1-w)*(1-w)*d0*d0
                    -4*n0*d0*a2*a2
                )
                pair_gcd = product.gcd(sum_cut)
                w1_roots, pair_factors = linear_roots(pair_gcd)
                b_row = {
                    "b": b_value,
                    "d0_zero": d0 == 0,
                    "n0_zero": n0 == 0,
                    "k_zero": k == 0,
                    "pair_gcd_degree": int(pair_gcd.degree()),
                    "pair_gcd_sha256": digest(str(pair_gcd)),
                    "pair_factors": pair_factors,
                    "w1_rows": [],
                }
                for w1_value in w1_roots:
                    b_row["w1_rows"].append({
                        "w1": w1_value,
                        "d1_zero": int(a2(w1_value)) == 0,
                        "n1_zero": int(a0(w1_value)) == 0,
                    })
                w0_row["b_rows"].append(b_row)
            row["w0_rows"].append(w0_row)
        rows.append(row)

    return {
        "status": "COMPLETE",
        "field": PRIME,
        "content_linear_roots": content_roots,
        "admissible_content_roots": admissible_roots,
        "rows": rows,
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell4-pair-exceptional-h-colored-content-fiber-replay-v1",
        "scope": (
            "Exact replay of every admissible linear t-content fiber removed "
            "from the colored H reduction, starting from H and the original "
            "P,L,M,F equations before the squared DE+/DE- pair. Unsquared "
            "labels, colored BE, unrelated leading charts, orbit, and Prize "
            "claims remain separate."
        ),
        "artifact_sha256": {
            path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in REMOTE
        },
        "result": replay_content_fibers.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    result = output["result"]
    summary = [{
        "t": row["t"],
        "w0_count": len(row["w0_rows"]),
        "b_count": sum(len(item["b_rows"]) for item in row["w0_rows"]),
        "w1_count": sum(
            len(b_row["w1_rows"])
            for item in row["w0_rows"] for b_row in item["b_rows"]
        ),
    } for row in result["rows"]]
    print(json.dumps({
        "result": str(RESULT),
        "status": result["status"],
        "admissible_content_roots": result["admissible_content_roots"],
        "summary": summary,
    }, sort_keys=True))
