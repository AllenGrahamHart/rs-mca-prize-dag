#!/usr/bin/env python3
"""Staged common-curve quotient pilot for the cell-5 signed families."""

import hashlib
import json
from pathlib import Path
import subprocess

import modal


DIRECTORY = Path(__file__).parent
COMMON = DIRECTORY / "rate_half_kb_positive_433_1a_common_vieta_compiler.py"
KERNEL = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
REMOTE_COMMON = "/root/rate_half_kb_positive_433_1a_common_vieta_compiler.py"
REMOTE_KERNEL = "/root/rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
PRIME = 2130706433
IOTA = 16711679

app = modal.App("rs-mca-positive-433-1a-cell5-signed-family-qring")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMMON, REMOTE_COMMON)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=1.0, memory=4096, timeout=240, max_containers=2)
def test_family(payload):
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from rate_half_kb_positive_433_1a_cell5_sparse_edge_probe import (
        sparse_product_kernel,
    )
    from rate_half_kb_positive_433_1a_common_vieta_compiler import compile_cell

    family, presentation = payload
    common_variables, equations, metadata = compile_cell(
        5, -1, -1, strip_fast=True
    )
    t, r, c, b = common_variables
    base_variables = (t, r, c, b)
    chart = equations[:3]
    guards = [
        metadata["labels"][left]-metadata["labels"][right]
        for left in range(5) for right in range(left+1, 5)
    ]
    guards.extend((
        r, t, b, c, b-1, b+1, c-1, c+1, c-b, b+c,
    ))
    guard_product = sp.prod(guards)

    a2, a0, _, _, _ = sparse_product_kernel()
    delta = t**2 * (t**2-1)
    beta = -t * (1+b) * sum(
        a2[index] * t**(2*index) for index in range(3)
    )
    source = sp.symbols("z2")
    endpoint_quotient = None
    if family == "E":
        source_label = source**2
        source_denominator = sum(
            a2[index] * source_label**index for index in range(3)
        )
        source_numerator = sum(
            a0[index] * source_label**index for index in range(3)
        )
        source_q = source*beta*(source_label-1)
        endpoint = sp.expand(
            delta*(b**2*source_denominator+source_numerator)+b*source_q
        )
        endpoint_quotient, endpoint_remainder = sp.div(
            sp.Poly(endpoint, source, *base_variables, modulus=PRIME),
            sp.Poly(
                2*b*t*(t**2-1)*(source-t),
                source, *base_variables, modulus=PRIME,
            ),
        )
        if not endpoint_remainder.is_zero:
            raise RuntimeError("known BE endpoint factor")
        endpoint_quotient = endpoint_quotient.monic().as_expr()

    def singular(expression):
        return str(sp.Poly(
            sp.expand(expression), *base_variables, modulus=PRIME
        ).as_expr()).replace("**", "^")

    def singular_source(expression):
        return str(sp.Poly(
            sp.expand(expression), source, *base_variables, modulus=PRIME
        ).as_expr()).replace("**", "^")

    scale = "b" if family == "E" else "c"
    if presentation == "pair":
        quotient_variables = "z0,z1,y,v,t,r,c,b"
        source_count = 2
    elif presentation in {"unsquared", "endpoint"}:
        quotient_variables = "z0,z1,z2,y,v,t,r,c,b"
        source_count = 3
    else:
        quotient_variables = "z0,z1,z2,t,r,c,b"
        source_count = 3
    program = [
        f"ring L={PRIME},(s,t,r,c,b),(dp(1),dp(4));",
        "option(redSB);",
        *[f"poly common{index}={singular(value)};"
          for index, value in enumerate(chart)],
        f"poly guard={singular(guard_product)};",
        "ideal S=common0,common1,common2,s*guard-1;",
        "ideal E=eliminate(S,s);",
        f"ring R={PRIME},({quotient_variables}),dp;",
        "option(redSB);",
        "ideal ER=imap(L,E);",
        "ideal Gc=std(ER);",
        'print("COMMON"); print(dim(Gc)); print(size(Gc));',
        "qring Q=Gc;",
        *[f"poly d{index}={singular(value)};" for index, value in enumerate(a2)],
        *[f"poly n{index}={singular(value)};" for index, value in enumerate(a0)],
        f"poly delta={singular(delta)};",
        f"poly beta={singular(beta)};",
    ]
    for index in range(source_count):
        program.extend((
            f"poly D{index}=d0+d1*z{index}^2+d2*z{index}^4;",
            f"poly N{index}=n0+n1*z{index}^2+n2*z{index}^4;",
            f"poly Q{index}=z{index}*beta*(z{index}^2-1);",
        ))
    if presentation == "pair":
        cuts = (
            "N0-y*v*D0",
            "Q0+(y+v)*delta*D0",
            "N1+y*v*D1",
            "Q1+(y-v)*delta*D1",
        )
    elif presentation == "unsquared":
        cuts = (
            "N0-y*v*D0",
            "Q0+(y+v)*delta*D0",
            "N1+y*v*D1",
            "Q1+(y-v)*delta*D1",
            f"N2-{scale}*v*D2",
            f"Q2+({scale}+v)*delta*D2",
        )
    elif presentation == "endpoint":
        if endpoint_quotient is None:
            raise RuntimeError("endpoint presentation is implemented for E")
        program.append(f"poly endpoint={singular_source(endpoint_quotient)};")
        cuts = (
            "N0-y*v*D0",
            "Q0+(y+v)*delta*D0",
            "N1+y*v*D1",
            "Q1+(y-v)*delta*D1",
            "endpoint",
            f"Q2+({scale}+v)*delta*D2",
        )
    else:
        cuts = (
            "N1*D0+N0*D1",
            "Q0^2*D1^2-Q1^2*D0^2-4*N0*delta^2*D0*D1^2",
            f"2*N2*delta*D0*D1-{scale}*D2*(Q1*D0-Q0*D1)",
            f"-2*Q2*D0*D1-2*{scale}*delta*D0*D1*D2"
            "-D2*(Q1*D0-Q0*D1)",
        )
    for index, cut in enumerate(cuts):
        program.append(f"poly cut{index}={cut};")
    program.append('print("CUTS");')
    for index in range(len(cuts)):
        program.append(f"print(deg(cut{index})); print(size(cut{index}));")
    program.extend((
        f"ideal I={','.join(f'cut{index}' for index in range(len(cuts)))};",
        "ideal G=std(I);",
        'if (reduce(1,G)==0) { print("UNIT"); } else { print("NONUNIT"); }',
        "print(dim(G)); print(size(G));",
        "quit;",
    ))
    program_text = "\n".join(program)
    header = {
        "family": family,
        "presentation": presentation,
        "scale": scale,
        "program_sha256": hashlib.sha256(program_text.encode()).hexdigest(),
    }
    try:
        process = subprocess.run(
            ["Singular", "-q"], input=program_text, capture_output=True,
            text=True, timeout=190,
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""

        return {
            **header,
            "status": "TIMEOUT",
            "stdout": decoded(error.stdout)[-4000:],
            "stderr": decoded(error.stderr)[-4000:],
        }
    valid_output = (
        process.returncode == 0
        and "?" not in process.stdout
        and ("UNIT" in process.stdout or "NONUNIT" in process.stdout)
    )
    return {
        **header,
        "status": "COMPLETE" if valid_output else "ERROR",
        "stdout": process.stdout[-4000:],
        "stderr": process.stderr[-4000:],
    }


@app.local_entrypoint()
def main(families: str = "E,F", presentation: str = "endpoint"):
    selected = tuple(value for value in families.split(",") if value)
    if not selected or not set(selected) <= {"E", "F"}:
        raise ValueError("families must contain E and/or F")
    if presentation not in {"pair", "endpoint", "unsquared", "target-free"}:
        raise ValueError(
            "presentation must be pair, endpoint, unsquared, or target-free"
        )
    if presentation == "endpoint" and "F" in selected:
        raise ValueError("endpoint presentation is currently implemented for E")
    print(json.dumps({
        "scope": (
            "fixed cell-5/sign-row saturated common-qring pilot; no outside "
            "denominator saturation, route, row, or Prize conclusion"
        ),
        "results": list(test_family.map(
            [(family, presentation) for family in selected]
        )),
    }, sort_keys=True))
