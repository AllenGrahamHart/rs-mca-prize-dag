#!/usr/bin/env python3
"""Test source-only endpoint cuts on the global cell-9 common curve."""

import hashlib
import itertools
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
STRUCTURE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_global_common_result.json"
)
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_compact_kernel_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_endpoint_compatibility_result.json"
)
REMOTE_STRUCTURE = "/root/structure.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell9-endpoint-compatibility")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(STRUCTURE, REMOTE_STRUCTURE)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=300, max_containers=8)
def decide(case):
    import sympy as sp

    epsilon, endpoint = case
    t, r, c, b = sp.symbols("t r c b")
    variables = (t, r, c, b)
    structure = json.loads(Path(REMOTE_STRUCTURE).read_text())
    structure_row = next(
        row for row in structure["rows"] if row["epsilon"] == list(epsilon)
    )
    basis = [item["expression"] for item in structure_row["lex_basis"]]
    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    kernel_row = next(
        row for row in kernel_payload["rows"]
        if row["epsilon"] == list(epsilon)
    )
    kernel = [sp.sympify(item["expression"]) for item in kernel_row["kernel"]]
    a_coefficients = kernel[:3]
    b_coefficients = kernel[3:6]
    beta_0, beta_1 = kernel[6:]
    label = -t*t
    a_value = sp.expand(sum(value*label**index
                            for index, value in enumerate(a_coefficients)))
    b_value = sp.expand(sum(value*label**index
                            for index, value in enumerate(b_coefficients)))
    beta_value = sp.expand(beta_0 + beta_1*label)
    endpoint_value = b if endpoint == "b" else c
    cut = sp.expand(
        (endpoint_value**2*a_value + b_value)**2
        - label*(beta_0 + beta_1*label)**2*endpoint_value**2
    )

    def singular(expression):
        return str(
            sp.Poly(expression, *variables, modulus=PRIME).as_expr()
        ).replace("**", "^")

    definitions = "\n".join(
        f"poly k{index}={expression};"
        for index, expression in enumerate(basis, start=1)
    )
    guard = (
        "r*t*b*c*(b-1)*(b+1)*(c-1)*(c+1)*(b-c)*(b+c)"
        "*(r^2-1)*(r^2+1)*(t^2-1)*(t^2+1)"
        "*(t^2-r^2)*(t^2+r^2)"
    )
    program = f"""
ring R={PRIME},(z,t,r,c,b),(dp(1),dp(4));
option(redSB);
{definitions}
poly av={singular(a_value)};
poly bv={singular(b_value)};
poly betav={singular(beta_value)};
poly cut={singular(cut)};
ideal Base=k1,k2,k3,k4,k5,k6,k7,z*({guard})-1; Base=slimgb(Base);
ideal Den=Base,av; Den=slimgb(Den);
ideal Ind=Base,av,bv; Ind=slimgb(Ind);
ideal Null=Base,av,bv,betav; Null=slimgb(Null);
ideal G=Base,cut; G=slimgb(G);
print("BEGIN");
print("BASE_DIM="+string(dim(Base))); print("BASE_SIZE="+string(size(Base)));
print("DEN_DIM="+string(dim(Den))); print("DEN_SIZE="+string(size(Den)));
if ((size(Den)==1) && (Den[1]==1)) {{ print("DEN_UNIT=1"); }}
else {{ print("DEN_UNIT=0"); }}
print("IND_DIM="+string(dim(Ind))); print("IND_SIZE="+string(size(Ind)));
if ((size(Ind)==1) && (Ind[1]==1)) {{ print("IND_UNIT=1"); }}
else {{ print("IND_UNIT=0"); }}
print("NULL_DIM="+string(dim(Null))); print("NULL_SIZE="+string(size(Null)));
if ((size(Null)==1) && (Null[1]==1)) {{ print("NULL_UNIT=1"); }}
else {{ print("NULL_UNIT=0"); }}
print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); }}
ideal Er=eliminate(G,z*t*c*b); Er=slimgb(Er);
print("ER_DIM="+string(dim(Er))); print("ER_SIZE="+string(size(Er)));
print("ER_BEGIN"); Er; print("ER_END");
ring L={PRIME},(z,c,b,t,r),lp;
option(redSB);
ideal GL=fglm(R,G);
ideal NL=fglm(R,Null);
print("GL_BEGIN"); print("GL_SIZE="+string(size(GL))); GL; print("GL_END");
print("NL_BEGIN"); print("NL_SIZE="+string(size(NL))); NL; print("NL_END");
print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=270,
        )
    except subprocess.TimeoutExpired as error:
        def decode(value):
            return (value.decode(errors="replace") if isinstance(value, bytes)
                    else value or "")
        return {
            "epsilon": list(epsilon), "endpoint": endpoint,
            "status": "TIMEOUT", "partial_stdout": decode(error.stdout)[-3000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }
    stdout = process.stdout

    def integer(label_name):
        match = re.search(rf"(?:^|\n){label_name}=(-?\d+)", stdout)
        return int(match.group(1)) if match else None

    elimination = re.search(r"ER_BEGIN\n(.*?)\nER_END", stdout, re.DOTALL)

    def lex_basis(name):
        block = re.search(rf"{name}_BEGIN\n(.*?)\n{name}_END", stdout, re.DOTALL)
        if not block:
            return []
        return [
            "".join(value.split())
            for value in re.findall(
                rf"^{name}\[\d+\]=(.*?)(?=^{name}\[\d+\]=|\Z)",
                block.group(1), re.MULTILINE | re.DOTALL,
            )
        ]

    def factor_profile(expression):
        if not expression:
            return []
        converted = re.sub(r"([a-zA-Z])(\d+)", r"\1**\2", expression)
        converted = re.sub(r"(?<=\d)(?=[a-zA-Z])", "*", converted)
        polynomial = sp.Poly(sp.sympify(converted), r, modulus=PRIME)
        _, factors = sp.factor_list(polynomial.as_expr(), r, modulus=PRIME)
        return [{
            "degree": int(sp.Poly(factor, r, modulus=PRIME).degree()),
            "multiplicity": multiplicity,
            "expression": str(sp.Poly(factor, r, modulus=PRIME).monic().as_expr()),
        } for factor, multiplicity in factors]

    compatibility_lex = lex_basis("GL")
    kernel_null_lex = lex_basis("NL")
    polynomial = sp.Poly(cut, *variables, modulus=PRIME)
    denominator = sp.Poly(a_value, *variables, modulus=PRIME)
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
    return {
        "epsilon": list(epsilon), "endpoint": endpoint,
        "status": "COMPLETE" if valid else "ERROR",
        "base_dimension": integer("BASE_DIM"),
        "base_basis_size": integer("BASE_SIZE"),
        "denominator_dimension": integer("DEN_DIM"),
        "denominator_basis_size": integer("DEN_SIZE"),
        "denominator_unit": "DEN_UNIT=1" in stdout,
        "indeterminate_dimension": integer("IND_DIM"),
        "indeterminate_basis_size": integer("IND_SIZE"),
        "indeterminate_unit": "IND_UNIT=1" in stdout,
        "kernel_null_dimension": integer("NULL_DIM"),
        "kernel_null_basis_size": integer("NULL_SIZE"),
        "kernel_null_unit": "NULL_UNIT=1" in stdout,
        "dimension": integer("DIM"), "basis_size": integer("SIZE"),
        "unit": "UNIT=1" in stdout,
        "r_elimination_dimension": integer("ER_DIM"),
        "r_elimination_size": integer("ER_SIZE"),
        "r_elimination": (
            "".join(elimination.group(1).split()) if elimination else None
        ),
        "compatibility_lex_basis": compatibility_lex,
        "compatibility_r_factors": factor_profile(
            compatibility_lex[0] if compatibility_lex else None
        ),
        "kernel_null_lex_basis": kernel_null_lex,
        "kernel_null_r_factors": factor_profile(
            kernel_null_lex[0] if kernel_null_lex else None
        ),
        "a_value_degree": int(denominator.total_degree()),
        "a_value_terms": len(denominator.terms()),
        "a_value_sha256": hashlib.sha256(
            str(denominator.as_expr()).encode()
        ).hexdigest(),
        "cut_degree": int(polynomial.total_degree()),
        "cut_terms": len(polynomial.terms()),
        "cut_sha256": hashlib.sha256(str(polynomial.as_expr()).encode()).hexdigest(),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stderr": process.stderr[-1000:],
    }


@app.local_entrypoint()
def main():
    signs = tuple(itertools.product((-1, 1), repeat=2))
    cases = tuple(itertools.product(signs, ("b", "c")))
    rows = list(decide.map(cases, order_outputs=True))
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell9-endpoint-compatibility-v1",
        "field": PRIME,
        "scope": (
            "Exact source-only BF/CF compatibility ideals on the global cell-9 "
            "common curve; no residual matching or endpoint exclusion claim."
        ),
        "source_structure_sha256": hashlib.sha256(STRUCTURE.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [{key: row.get(key) for key in (
            "epsilon", "endpoint", "status", "denominator_unit",
            "indeterminate_unit", "kernel_null_unit", "dimension",
            "basis_size", "unit",
            "r_elimination_dimension",
            "r_elimination_size", "cut_degree", "cut_terms",
        )} for row in rows],
    }, sort_keys=True))
