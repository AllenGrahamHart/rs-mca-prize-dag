#!/usr/bin/env python3
"""Hard-capped Singular pilot for the live m=16 HNF eliminant R_12.

This is a representation and cost pilot, not a proof certificate. It builds
the exact official-characteristic polynomial Q_s and only the first
eliminant Res_t(F_1,F_2). It returns degree, term count, a text digest, wall
time, and peak child RSS. No retry or second eliminant is launched.
"""

from __future__ import annotations

import hashlib
import json
import resource
import subprocess
import time

import modal


APP_NAME = "l1-mersenne-m16-r12-singular-pilot"
P = 8191
M = 16
H = M - 1

app = modal.App(APP_NAME)
image = modal.Image.debian_slim(python_version="3.12").run_commands(
    "apt-get update && "
    "DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends singular && "
    "rm -rf /var/lib/apt/lists/*"
)


def truncated_binomial() -> str:
    terms = []
    rising = "1"
    factorial = 1
    for r in range(H + 1):
        if r:
            rising = f"({rising})*(s+{r - 1})"
            factorial = factorial * r % P
        coefficient = rising if r == 0 else f"({pow(factorial, -1, P)})*({rising})"
        terms.append(f"({coefficient})*w^{H - r}")
    return "+".join(terms)


def singular_program() -> str:
    # coeffs(Q,z) is ordered from z^0 upward. For h=15, q_j is row 16-j.
    return "\n".join(
        [
            f"ring r={P},(w,z,t,s),lp;",
            "option(redSB);",
            f"poly Ps={truncated_binomial()};",
            f"poly Q=resultant(Ps,z-w^{M},w);",
            "matrix qc=coeffs(Q,z);",
            "poly C=qc[1,1];",
            "poly q1=qc[15,1];",
            "poly q2=qc[14,1];",
            "poly q14=qc[2,1];",
            "poly q13=qc[3,1];",
            'if (nrows(qc)!=16) { print("L1_M16_R12_PREFLIGHT_ROWS_ERROR"); quit; }',
            'if (qc[16,1]!=1) { print("L1_M16_R12_PREFLIGHT_MONIC_ERROR"); quit; }',
            'if (deg(q1)!=16) { print("L1_M16_R12_PREFLIGHT_Q1_ERROR"); quit; }',
            'if (deg(q2)!=32) { print("L1_M16_R12_PREFLIGHT_Q2_ERROR"); quit; }',
            'if (deg(q13)!=208) { print("L1_M16_R12_PREFLIGHT_Q13_ERROR"); quit; }',
            'if (deg(q14)!=224) { print("L1_M16_R12_PREFLIGHT_Q14_ERROR"); quit; }',
            'if (deg(C)!=240) { print("L1_M16_R12_PREFLIGHT_C_ERROR"); quit; }',
            "poly F1=C*subst(q1,s,t)-q14;",
            "poly F2=C*subst(q2,s,t)-q13;",
            "poly R12=resultant(F1,F2,t);",
            'print("L1_M16_R12_META_BEGIN");',
            "nrows(qc);",
            "size(Q);",
            "deg(q1);",
            "deg(q2);",
            "deg(q13);",
            "deg(q14);",
            "deg(C);",
            "deg(F1);",
            "size(F1);",
            "deg(F2);",
            "size(F2);",
            "deg(R12);",
            "size(R12);",
            'print("L1_M16_R12_META_END");',
            'print("L1_M16_R12_POLY_BEGIN");',
            "R12;",
            'print("L1_M16_R12_POLY_END");',
            "quit;",
        ]
    ) + "\n"


@app.function(image=image, cpu=1, memory=2048, timeout=180, max_containers=1)
def pilot() -> dict[str, object]:
    program = singular_program()
    started = time.monotonic()
    base = {
        "app": APP_NAME,
        "p": P,
        "m": M,
        "h": H,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "raw_degree_bound": 11520,
    }
    print("L1_M16_R12_INPUT " + json.dumps(base, sort_keys=True), flush=True)

    def tail(value: str | bytes | None) -> str:
        if value is None:
            return ""
        if isinstance(value, bytes):
            value = value.decode(errors="replace")
        return value[-2000:]

    try:
        process = subprocess.run(
            ["Singular", "-q"],
            input=program,
            text=True,
            capture_output=True,
            timeout=165,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        result = {
            **base,
            "status": "TIMEOUT",
            "seconds": round(time.monotonic() - started, 6),
            "peak_mb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss // 1024,
            "stdout_tail": tail(error.stdout),
            "stderr_tail": tail(error.stderr),
        }
        print("L1_M16_R12_RESULT " + json.dumps(result, sort_keys=True), flush=True)
        return result

    stdout = process.stdout
    begin = "L1_M16_R12_POLY_BEGIN\n"
    end = "\nL1_M16_R12_POLY_END"
    complete = process.returncode == 0 and begin in stdout and end in stdout
    polynomial = stdout.split(begin, 1)[1].split(end, 1)[0].strip() if complete else ""
    meta = ""
    meta_begin = "L1_M16_R12_META_BEGIN\n"
    meta_end = "\nL1_M16_R12_META_END"
    if meta_begin in stdout and meta_end in stdout:
        meta = stdout.split(meta_begin, 1)[1].split(meta_end, 1)[0].strip()
    result = {
        **base,
        "status": "COMPLETE" if complete else "ERROR",
        "returncode": process.returncode,
        "seconds": round(time.monotonic() - started, 6),
        "peak_mb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss // 1024,
        "meta": meta,
        "r12_text_bytes": len(polynomial.encode()),
        "r12_text_sha256": hashlib.sha256(polynomial.encode()).hexdigest() if polynomial else None,
        "stdout_tail": stdout[-2000:] if not complete else "",
        "stderr_tail": process.stderr[-2000:],
    }
    print("L1_M16_R12_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    return result


@app.local_entrypoint()
def main() -> None:
    print(json.dumps(pilot.remote(), indent=2, sort_keys=True))
