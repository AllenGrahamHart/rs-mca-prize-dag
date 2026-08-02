#!/usr/bin/env python3
"""Compile and test the target-free cell-4 family on its plane chart."""

import hashlib
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
PLANE = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_plane_kernel_flint_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_plane_target_free_family_result.json"
REMOTE_PLANE = "/root/cell4_plane_kernel_flint.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell4-plane-target-free-family")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("python-flint==0.8.0")
    .add_local_file(PLANE, REMOTE_PLANE)
)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


@app.function(image=image, cpu=2.0, memory=8192, timeout=300)
def analyze_family():
    from flint import fmpz_mod_mpoly_ctx

    source_bytes = Path(REMOTE_PLANE).read_bytes()
    payload = json.loads(source_bytes)["result"]
    context = fmpz_mod_mpoly_ctx.get(["z0", "z1", "z2", "b", "t"], PRIME)
    z0, z1, z2, b, _ = context.gens()

    def parse_polynomial(value):
        output = {}
        compact = value.replace(" ", "")
        for raw_term in re.findall(r"[+-]?[^+-]+", compact):
            sign = 1
            term = raw_term
            if term.startswith("+"):
                term = term[1:]
            elif term.startswith("-"):
                sign = -1
                term = term[1:]
            coefficient = 1
            exponents = {name: 0 for name in ("z0", "z1", "z2", "b", "t")}
            for factor in term.split("*"):
                if factor.isdigit():
                    coefficient = coefficient*int(factor) % PRIME
                    continue
                match = re.fullmatch(r"(z0|z1|z2|b|t)(?:\^(\d+))?", factor)
                if match is None:
                    raise RuntimeError(f"cannot parse factor {factor!r}")
                variable, exponent = match.groups()
                exponents[variable] += int(exponent) if exponent else 1
            key = tuple(exponents[name] for name in ("z0", "z1", "z2", "b", "t"))
            output[key] = (output.get(key, 0)+sign*coefficient) % PRIME
        return context.from_dict({key: coefficient for key, coefficient in
                                  output.items() if coefficient})

    coefficients = {
        name: parse_polynomial(row["polynomial"])
        for name, row in payload["normalized_coefficients"].items()
    }

    def evaluate(prefix, root):
        return coefficients[f"{prefix}0"] + coefficients[f"{prefix}1"]*root**2 \
            + coefficients[f"{prefix}2"]*root**4

    roots = (z0, z1, z2)
    d0, d1, d2 = [evaluate("a2", root) for root in roots]
    n0, n1, n2 = [evaluate("a0", root) for root in roots]
    q0, q1, q2 = [root*(coefficients["b10"]+coefficients["b11"]*root**2)
                  for root in roots]
    cross = q1*d0-q0*d1
    raw = (
        n1*d0+n0*d1,
        q0*q0*d1*d1-q1*q1*d0*d0-4*n0*d0*d1*d1,
        2*n2*d0*d1-b*d2*cross,
        -2*q2*d0*d1-2*b*d0*d1*d2-d2*cross,
    )
    plane = parse_polynomial(payload["plane_polynomial"])
    plane_leading = parse_polynomial(payload["plane_leading_coefficient"])

    def coefficient_at_b_degree(polynomial, degree):
        return context.from_dict({
            (monomial[0], monomial[1], monomial[2], 0, monomial[4]):
                int(coefficient)
            for monomial, coefficient in polynomial.to_dict().items()
            if monomial[3] == degree
        })

    def pseudo_remainder(polynomial):
        remainder = polynomial
        steps = 0
        while int(remainder.degrees()[3]) >= 4:
            old_degree = int(remainder.degrees()[3])
            leading = coefficient_at_b_degree(remainder, old_degree)
            remainder = plane_leading*remainder-leading*b**(old_degree-4)*plane
            if int(remainder.degrees()[3]) >= old_degree:
                raise RuntimeError("pseudo-division did not lower b degree")
            steps += 1
        return remainder, steps

    reduced = [pseudo_remainder(equation) for equation in raw]
    equations = [row[0] for row in reduced]
    equation_text = [equation.str() for equation in equations]
    equation_shapes = [
        {"degrees": [int(value) for value in equation.degrees()],
         "total_degree": int(equation.total_degree()),
         "terms": len(list(equation.terms())),
         "pseudo_steps": reduced[index][1]}
        for index, equation in enumerate(equations)
    ]
    coefficient_definitions = "\n".join(
        f"poly {name}={row['polynomial']};"
        for name, row in payload["normalized_coefficients"].items()
    )
    family_definitions = "\n".join(
        f"poly f{index}={value};" for index, value in enumerate(equation_text)
    )
    program = f"""
ring R={PRIME},(u0,u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,
 z0,z1,z2,b,t),(dp(13),dp(3),dp(2));
option(redSB);
poly plane={payload['plane_polynomial']};
{coefficient_definitions}
poly D0=a20+a21*z0^2+a22*z0^4;
poly D1=a20+a21*z1^2+a22*z1^4;
poly D2=a20+a21*z2^2+a22*z2^4;
{family_definitions}
poly rn={payload['r_numerator']}; poly rd={payload['r_denominator']};
poly cn={payload['c_numerator']}; poly cd={payload['c_denominator']};
poly rd2=rd*rd; poly rn2=rn*rn;
poly exceptionalScale={payload['denominator_scale']}
 *({payload['common_projective_scale']})
 *({payload['plane_leading_coefficient']})
 *({payload['projected_common_scale']});
poly cg0=t*b*rn*cn*(b-1)*(b+1);
poly cg1=(cn-cd)*(cn+cd)*(b*cd-cn)*(b*cd+cn);
poly cg2=(1-t^2)*(1+t^2);
poly cg3=(rd2-rn2)*(rd2+rn2);
poly cg4=(t^2*rd2-rn2)*(t^2*rd2+rn2);
poly sg0=z0*z1*z2*(z0^2-z1^2)*(z0^2-z2^2)*(z1^2-z2^2);
poly sg1=(z0^2-1)*(z0^2-t^2)*(z0^2+1)
 *(z0^2*rd2-rn2)*(z0^2*rd2+rn2);
poly sg2=(z1^2-1)*(z1^2-t^2)*(z1^2+1)
 *(z1^2*rd2-rn2)*(z1^2*rd2+rn2);
poly sg3=(z2^2-1)*(z2^2-t^2)*(z2^2+1)
 *(z2^2*rd2-rn2)*(z2^2*rd2+rn2);
print("BEGIN_SHAPES");
print(deg(f0)); print(size(f0)); print(deg(f1)); print(size(f1));
print(deg(f2)); print(size(f2)); print(deg(f3)); print(size(f3));
print("END_SHAPES");
ideal I=plane,f0,f1,f2,f3,
 u0*exceptionalScale-1,
 u1*cg0-1,u2*cg1-1,u3*cg2-1,u4*cg3-1,u5*cg4-1,
 u6*sg0-1,u7*sg1-1,u8*sg2-1,u9*sg3-1,
 u10*D0-1,u11*D1-1,u12*D2-1;
ideal G=slimgb(I);
print("BEGIN_LOCALIZED"); print(dim(G)); print(size(G));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); }}
print("END_LOCALIZED"); quit;
"""
    header = {
        "field": PRIME, "cell": 4, "epsilon": [-1, -1],
        "source_plane_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "equation_shapes": equation_shapes,
        "equation_sha256": [digest(value) for value in equation_text],
        "program_sha256": digest(program),
    }
    try:
        process = subprocess.run(["Singular", "--quiet"], input=program,
                                 capture_output=True, text=True, timeout=250)
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""
        partial_stdout = decoded(error.stdout)[-50000:]
        return {
            **header, "status": "TIMEOUT",
            "shapes_emitted": "END_SHAPES" in partial_stdout,
            "partial_stdout": partial_stdout,
            "partial_stderr": decoded(error.stderr)[-4000:],
        }
    stdout = process.stdout
    valid = process.returncode == 0 and "END_LOCALIZED" in stdout and "?" not in stdout
    return {
        **header, "status": "COMPLETE" if valid else "ERROR",
        "unit": "UNIT=1" in stdout,
        "stdout": stdout[-50000:], "stderr": process.stderr[-4000:],
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell4-plane-target-free-family-v1",
        "scope": (
            "Four target-free guard-saturated DE+/DE-/BE identities on the "
            "compact cell-4 plane chart; unit proves this chart empty, while "
            "nonunit or timeout makes no orbit, route, K3, or Prize claim."
        ),
        "result": analyze_family.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    result = output["result"]
    print(json.dumps({
        "result": str(RESULT), "status": result.get("status"),
        "unit": result.get("unit"), "shapes_emitted": result.get("shapes_emitted"),
        "equation_shapes": result.get("equation_shapes"),
    }, sort_keys=True))
