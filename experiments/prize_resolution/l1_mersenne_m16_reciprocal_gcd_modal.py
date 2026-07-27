#!/usr/bin/env python3
"""Hard-capped exact gcd pilot for the official m=16 HNF reciprocal system.

The worker recomputes Q_s, forms R_12 and R_13, and tests whether the
squarefree part of their gcd divides s^8191-s. It returns every completed
stage even if a later stage reaches the subprocess timeout.
"""

from __future__ import annotations

import hashlib
import json
import resource
import subprocess
import time

import modal


APP_NAME = "l1-mersenne-m16-reciprocal-gcd"
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
    terms: list[str] = []
    rising = "1"
    factorial = 1
    for index in range(H + 1):
        if index:
            rising = f"({rising})*(s+{index - 1})"
            factorial = factorial * index % P
        coefficient = rising if index == 0 else f"({pow(factorial, -1, P)})*({rising})"
        terms.append(f"({coefficient})*w^{H - index}")
    return "+".join(terms)


def emit(name: str) -> list[str]:
    return [f'print("L1_M16_{name}_BEGIN");', f"{name};", f'print("L1_M16_{name}_END");']


def singular_program() -> str:
    lines = [
        f"ring r={P},(w,z,t,s),lp;",
        "option(redSB);",
        f"poly Ps={truncated_binomial()};",
        f"poly Q=resultant(Ps,z-w^{M},w);",
        "matrix qc=coeffs(Q,z);",
        "poly C=qc[1,1];",
        "poly q1=qc[15,1];",
        "poly q2=qc[14,1];",
        "poly q3=qc[13,1];",
        "poly q12=qc[4,1];",
        "poly q13=qc[3,1];",
        "poly q14=qc[2,1];",
        'if (nrows(qc)!=16) { print("L1_M16_PREFLIGHT_ROWS_ERROR"); quit; }',
        'if (qc[16,1]!=1) { print("L1_M16_PREFLIGHT_MONIC_ERROR"); quit; }',
        'if (deg(q1)!=16 || deg(q2)!=32 || deg(q3)!=48) { print("L1_M16_PREFLIGHT_LOW_ERROR"); quit; }',
        'if (deg(q12)!=192 || deg(q13)!=208 || deg(q14)!=224 || deg(C)!=240) { print("L1_M16_PREFLIGHT_HIGH_ERROR"); quit; }',
        "poly F1=C*subst(q1,s,t)-q14;",
        "poly F2=C*subst(q2,s,t)-q13;",
        "poly F3=C*subst(q3,s,t)-q12;",
        "poly R12=resultant(F1,F2,t);",
        *emit("R12"),
        "poly R13=resultant(F1,F3,t);",
        *emit("R13"),
        "poly G=gcd(R12,R13);",
        *emit("G"),
        "poly GD=gcd(G,diff(G,s));",
        "poly RAD=G/GD;",
        "poly RADGD=gcd(RAD,diff(RAD,s));",
        *emit("RAD"),
        "poly EXPECTED=s*(s-1);",
        "int root_index;",
        "for (root_index=1; root_index<=15; root_index++) { EXPECTED=EXPECTED*(s+root_index); }",
        "poly DELTA=RAD-EXPECTED;",
        *emit("DELTA"),
        "ideal IRAD=RAD;",
        "ideal BRAD=std(IRAD);",
        f"poly REM=reduce(s^{P}-s,BRAD);",
        *emit("REM"),
        'print("L1_M16_META_BEGIN");',
        "deg(Q); size(Q);",
        "deg(F1); size(F1); deg(F2); size(F2); deg(F3); size(F3);",
        "deg(R12); size(R12); deg(R13); size(R13);",
        "deg(G); size(G); deg(GD); size(GD);",
        "deg(RAD); size(RAD); deg(RADGD); size(RADGD);",
        "deg(REM); size(REM);",
        'print("L1_M16_META_END");',
        "quit;",
    ]
    return "\n".join(lines) + "\n"


def extract(stdout: str, name: str) -> str | None:
    begin = f"L1_M16_{name}_BEGIN\n"
    end = f"\nL1_M16_{name}_END"
    if begin not in stdout or end not in stdout:
        return None
    return stdout.split(begin, 1)[1].split(end, 1)[0].strip()


def artifact(stdout: str, name: str) -> dict[str, object] | None:
    value = extract(stdout, name)
    if value is None:
        return None
    encoded = value.encode()
    return {
        "bytes": len(encoded),
        "sha256": hashlib.sha256(encoded).hexdigest(),
        "zero": value == "0",
    }


@app.function(image=image, cpu=1, memory=2048, timeout=135, max_containers=1)
def pilot() -> dict[str, object]:
    program = singular_program()
    started = time.monotonic()
    base: dict[str, object] = {
        "app": APP_NAME,
        "p": P,
        "m": M,
        "h": H,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "raw_degree_bounds": {"R12": 11520, "R13": 15360},
    }
    print("L1_M16_GCD_INPUT " + json.dumps(base, sort_keys=True), flush=True)

    try:
        process = subprocess.run(
            ["Singular", "-q"],
            input=program,
            text=True,
            capture_output=True,
            timeout=120,
            check=False,
        )
        stdout = process.stdout
        stderr = process.stderr
        returncode: int | None = process.returncode
        timed_out = False
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout or ""
        stderr = error.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode(errors="replace")
        returncode = None
        timed_out = True

    names = ("R12", "R13", "G", "RAD", "DELTA", "REM")
    artifacts = {name: artifact(stdout, name) for name in names}
    radical_text = extract(stdout, "RAD")
    meta = extract(stdout, "META")
    complete = (
        not timed_out
        and returncode == 0
        and artifacts["DELTA"] is not None
        and artifacts["DELTA"]["zero"] is True
        and artifacts["REM"] is not None
        and artifacts["REM"]["zero"] is True
        and meta is not None
    )
    result = {
        **base,
        "status": "COMPLETE" if complete else ("TIMEOUT" if timed_out else "ERROR"),
        "returncode": returncode,
        "seconds": round(time.monotonic() - started, 6),
        "peak_mb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss // 1024,
        "artifacts": artifacts,
        "radical_text": radical_text,
        "meta": meta,
        "stdout_tail": stdout[-2000:] if not complete else "",
        "stderr_tail": stderr[-2000:],
    }
    print("L1_M16_GCD_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    return result


@app.local_entrypoint()
def main() -> None:
    print(json.dumps(pilot.remote(), indent=2, sort_keys=True))
