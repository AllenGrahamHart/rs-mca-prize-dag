#!/usr/bin/env python3
"""Finite-algebra pilot for the cell-5 signed-pair frontier."""

import hashlib
import json
import math
from pathlib import Path
import subprocess

import modal


DIRECTORY = Path(__file__).parent
COMMON = DIRECTORY / "rate_half_kb_positive_433_1a_common_vieta_compiler.py"
KERNEL = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
REMOTE_COMMON = "/root/rate_half_kb_positive_433_1a_common_vieta_compiler.py"
REMOTE_KERNEL = "/root/rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
IOTA = 16711679
SMALL_CHART_PRIME = 65521
DEPLOYED_PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell5-finite-algebra")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMMON, REMOTE_COMMON)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=300)
def analyze(characteristic, method):
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from rate_half_kb_positive_433_1a_cell5_sparse_edge_probe import (
        sparse_product_kernel,
    )
    from rate_half_kb_positive_433_1a_common_vieta_compiler import compile_cell

    if characteristic == DEPLOYED_PRIME:
        iota = IOTA
    else:
        iota = int(min(sp.sqrt_mod(-1, characteristic, all_roots=True)))
    variables, equations, metadata = compile_cell(
        5, -1, -1, strip_fast=True, prime=characteristic, iota=iota
    )
    t, r, c, b = variables
    chart = equations[:3]
    guards = [
        metadata["labels"][left] - metadata["labels"][right]
        for left in range(5) for right in range(left + 1, 5)
    ]
    guards.extend((r, t, b, c, b - 1, b + 1, c - 1, c + 1, c - b, b + c))
    guard_product = sp.prod(guards)
    a2, a0, _, _, _ = sparse_product_kernel()
    delta = t**2 * (t**2 - 1)
    beta = -t * (1 + b) * sum(
        a2[index] * t**(2 * index) for index in range(3)
    )

    def singular(expression):
        return str(sp.Poly(
            sp.expand(expression), t, r, c, b, modulus=characteristic
        ).as_expr()).replace("**", "^")

    initial = [
        f"ring L={characteristic},(s,t,r,c,b),(dp(1),dp(4));",
        "option(redSB);",
        *(f"poly common{index}={singular(value)};"
          for index, value in enumerate(chart)),
        f"poly guard={singular(guard_product)};",
        "ideal S=common0,common1,common2,s*guard-1;",
        "ideal E=eliminate(S,s);",
        f"ring R={characteristic},(z0,z1,y,v,t,r,c,b),dp;",
        "option(redSB);",
        "ideal ER=imap(L,E);",
        "ideal G=std(ER);",
        'print("AFFINE_COMMON"); print(dim(G)); print(size(G));',
    ]
    if method == "affine-basis":
        body = ['print("AFFINE_BASIS"); print(G);']
    elif method == "deployed-eliminate":
        body = [
            f"ring Z={characteristic},(r,c,b,t),(dp(2),dp(2));",
            "option(redSB);",
            "ideal H=std(imap(R,G));",
            'print("DEPLOYED_BLOCK_BASIS"); print(dim(H)); print(size(H));',
            "ideal J=eliminate(H,r*c);",
            "ideal GJ=std(J);",
            'print("DEPLOYED_BT_ELIMINATION");',
            "print(dim(GJ)); print(size(GJ));",
            "for (int i=1; i<=size(GJ); i++)",
            "{",
            "  print(deg(GJ[i])); print(size(GJ[i]));",
            "}",
            "poly bpoly=GJ[1];",
        ]
        for index in range(5):
            derivative = "bpoly"
            for _ in range(index):
                derivative = f"diff({derivative},b)"
            body.extend((
                f"poly coefficient{index}=subst({derivative},b,0)"
                f"/{math.factorial(index)};",
            ))
        body.extend((
            (
                "poly reciprocal4=coefficient0*b^4+coefficient1*b^3"
                "+coefficient2*b^2+coefficient3*b+coefficient4;"
            ),
            (
                "poly quadratic_lift=coefficient0*(b^4+2*b^2+1)"
                "+coefficient1*(b^3+b)"
                "+(coefficient2-2*coefficient0)*b^2;"
            ),
            'print("DEPLOYED_RECIPROCAL");',
            "print(reciprocal4-bpoly==0); print(quadratic_lift-bpoly==0);",
            'print("DEPLOYED_BPOLY"); print(bpoly);',
        ))
    elif method == "deployed-lifts":
        body = [
            f"ring Z={characteristic},(r,c,b,t),(dp(2),dp(2));",
            "option(redSB);",
            "ideal H=std(imap(R,G));",
            'print("DEPLOYED_BLOCK_BASIS"); print(dim(H)); print(size(H));',
            "ideal EC=std(eliminate(H,r));",
            'print("DEPLOYED_C_LIFT"); print(dim(EC)); print(size(EC));',
            "for (int j=1; j<=size(EC); j++)",
            "{ print(deg(EC[j])); print(size(EC[j])); }",
            "print(EC);",
            "ideal ER2=std(eliminate(H,c));",
            'print("DEPLOYED_R_LIFT"); print(dim(ER2)); print(size(ER2));',
            "for (int k=1; k<=size(ER2); k++)",
            "{ print(deg(ER2[k])); print(size(ER2[k])); }",
            "print(ER2);",
        ]
    elif method == "deployed-lift-denominators":
        body = [
            f"ring Z={characteristic},(r,c,b,t),(dp(2),dp(2));",
            "option(redSB);",
            "ideal H=std(imap(R,G));",
            "ideal BT=std(eliminate(H,r*c));",
            "poly bpoly=BT[1];",
            "ideal EC=std(eliminate(H,r));",
            "ideal ER2=std(eliminate(H,c));",
            "poly cEquation=EC[2];",
            "poly rEquation=ER2[2];",
            "poly cLeading=diff(cEquation,c);",
            "poly rLeading=diff(rEquation,r);",
            "poly cConstant=subst(cEquation,c,0);",
            "poly rConstant=subst(rEquation,r,0);",
            'print("DEPLOYED_LIFT_LINEARITY");',
            "print(cEquation-c*cLeading-cConstant==0);",
            "print(rEquation-r*rLeading-rConstant==0);",
            "poly cResultant=resultant(bpoly,cLeading,b);",
            "poly rResultant=resultant(bpoly,rLeading,b);",
            'print("DEPLOYED_LIFT_DENOMINATORS");',
            "print(deg(cResultant)); print(size(cResultant)); print(cResultant);",
            "print(deg(rResultant)); print(size(rResultant)); print(rResultant);",
        ]
    else:
        body = [
            f"ring K=({characteristic},t),(r,c,b),dp;",
            "option(redSB);",
            "ideal H=std(imap(R,G));",
            'print("GENERIC_FIBER");',
            "print(dim(H)); print(size(H)); print(vdim(H));",
        ]
        if method == "generic-basis":
            body.extend(('print("GENERIC_BASIS");', "print(H);"))
        elif method == "generic-minass":
            body.extend((
                'LIB "primdec.lib";',
                "list C=minAssGTZ(H);",
                'print("GENERIC_COMPONENT_COUNT"); print(size(C));',
                "for (int i=1; i<=size(C); i++)",
                "{",
                "  ideal Gi=std(C[i]);",
                '  print("GENERIC_COMPONENT");',
                "  print(i); print(dim(Gi)); print(size(Gi)); print(vdim(Gi));",
                "}",
            ))
        else:
            body.extend((
                f"ring KL=({characteristic},t),(r,c,b),lp;",
                "option(redSB);",
                "ideal HL=fglm(K,H);",
                "poly bpoly=HL[1];",
                "poly cvalue=reduce(c,HL);",
                "poly rvalue=reduce(r,HL);",
                'print("FINITE_ALGEBRA");',
                "print(size(HL)); print(vdim(HL)); print(deg(bpoly));",
            ))
            for index in range(9):
                derivative = "bpoly"
                for _ in range(index):
                    derivative = f"diff({derivative},b)"
                body.extend((
                    f"poly coefficient_poly{index}=subst({derivative},b,0);",
                    f"number coefficient{index}="
                    f"leadcoef(coefficient_poly{index})/{math.factorial(index)};",
                ))
            reciprocal = "+".join(
                f"coefficient{index}*b^{8-index}" for index in range(9)
            )
            reciprocal4 = "+".join(
                f"coefficient{index}*b^{4-index}" for index in range(5)
            )
            body.extend((
                f"poly reciprocal={reciprocal};",
                f"poly reciprocal4={reciprocal4};",
                (
                    "poly quartic_lift=b^8+4*b^6+6*b^4+4*b^2+1"
                    "+coefficient1*(b^7+3*b^5+3*b^3+b)"
                    "+(coefficient2-4)*(b^6+2*b^4+b^2)"
                    "+(coefficient3-3*coefficient1)*(b^5+b^3)"
                    "+(coefficient4-2*coefficient2+2)*b^4;"
                ),
                (
                    "poly quadratic_lift=b^4+2*b^2+1"
                    "+coefficient1*(b^3+b)"
                    "+(coefficient2-2)*b^2;"
                ),
                'print("RECIPROCAL");',
                "print(reciprocal-bpoly==0); print(quartic_lift-bpoly==0);",
                "print(reciprocal4-bpoly==0); print(quadratic_lift-bpoly==0);",
            ))
            if method == "lex":
                body.extend((
                    'print("LEX_LEDGER");',
                    "print(deg(HL[1])); print(size(HL[1]));",
                    "print(deg(HL[2])); print(size(HL[2]));",
                    "print(deg(HL[3])); print(size(HL[3]));",
                ))
            else:
                body.extend((
                    f"ring A=({characteristic},t),(z0,z1,y,v,b),(dp(4),dp(1));",
                    "option(redSB);",
                    "poly bpoly0=imap(KL,bpoly);",
                    "ideal B=std(bpoly0);",
                    "poly c=reduce(imap(KL,cvalue),B);",
                    "poly r=reduce(imap(KL,rvalue),B);",
                    *(f"poly d{index}=reduce({singular(value)},B);"
                      for index, value in enumerate(a2)),
                    *(f"poly n{index}=reduce({singular(value)},B);"
                      for index, value in enumerate(a0)),
                    f"poly delta={singular(delta)};",
                    f"poly beta=reduce({singular(beta)},B);",
                    "poly D0=d0+d1*z0^2+d2*z0^4;",
                    "poly D1=d0+d1*z1^2+d2*z1^4;",
                    "poly N0=n0+n1*z0^2+n2*z0^4;",
                    "poly N1=n0+n1*z1^2+n2*z1^4;",
                    "poly Q0=z0*beta*(z0^2-1);",
                    "poly Q1=z1*beta*(z1^2-1);",
                    "poly cut0=reduce(N0-y*v*D0,B);",
                    "poly cut1=reduce(Q0+(y+v)*delta*D0,B);",
                    "poly cut2=reduce(N1+y*v*D1,B);",
                    "poly cut3=reduce(Q1+(y-v)*delta*D1,B);",
                    'print("FINITE_PAIR_CUTS");',
                    "print(deg(cut0)); print(size(cut0));",
                    "print(deg(cut1)); print(size(cut1));",
                    "print(deg(cut2)); print(size(cut2));",
                    "print(deg(cut3)); print(size(cut3));",
                    "ideal P=bpoly0,cut0,cut1,cut2,cut3;",
                    "ideal GP=slimgb(P);",
                    'print("FINITE_PAIR_BASIS");',
                    "print(dim(GP)); print(size(GP)); print(vdim(GP));",
                    (
                        'if (reduce(1,GP)==0) { print("UNIT"); } '
                        'else { print("NONUNIT"); }'
                    ),
                ))

    program = "\n".join((*initial, *body, "quit;"))
    header = {
        "characteristic": characteristic,
        "iota": iota,
        "method": method,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "scope": (
            "relation-preserving cell-5 common finite algebra and optional "
            "signed-pair pilot; no source-guard saturation, colored edge, "
            "route, row, or Prize conclusion"
        ),
    }
    timeout = 240 if method == "finite-pair" else 120
    try:
        process = subprocess.run(
            ["Singular", "-q"], input=program, capture_output=True,
            text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""

        return {
            **header,
            "status": "TIMEOUT",
            "stdout": decoded(error.stdout)[-12000:],
            "stderr": decoded(error.stderr)[-4000:],
        }
    expected = {
        "affine-basis": "AFFINE_BASIS",
        "deployed-eliminate": "DEPLOYED_RECIPROCAL",
        "deployed-lifts": "DEPLOYED_R_LIFT",
        "deployed-lift-denominators": "DEPLOYED_LIFT_DENOMINATORS",
        "generic-basis": "GENERIC_BASIS",
        "generic-minass": "GENERIC_COMPONENT_COUNT",
        "lex": "LEX_LEDGER",
        "finite-pair": "FINITE_PAIR_BASIS",
    }[method]
    valid = (
        process.returncode == 0
        and "?" not in process.stdout
        and expected in process.stdout
    )
    return {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "returncode": process.returncode,
        "stdout": process.stdout[-12000:],
        "stderr": process.stderr[-4000:],
    }


@app.local_entrypoint()
def main(characteristic: int = SMALL_CHART_PRIME, method: str = "lex"):
    if characteristic != DEPLOYED_PRIME and (
        characteristic < 3 or characteristic >= 2**29 or characteristic % 4 != 1
    ):
        raise ValueError(
            "small characteristic must be odd, below 2^29, and 1 mod 4"
        )
    if characteristic == DEPLOYED_PRIME and method not in {
        "affine-basis", "deployed-eliminate", "deployed-lifts",
        "deployed-lift-denominators",
    }:
        raise ValueError(
            "Singular function fields require characteristic below 2^29; "
            "only affine-basis is supported at the deployed prime"
        )
    methods = {
        "affine-basis", "deployed-eliminate", "deployed-lifts",
        "deployed-lift-denominators", "generic-basis",
        "generic-minass", "lex", "finite-pair",
    }
    if method not in methods:
        raise ValueError(f"method must be one of {sorted(methods)}")
    print(json.dumps(analyze.remote(characteristic, method), sort_keys=True))
