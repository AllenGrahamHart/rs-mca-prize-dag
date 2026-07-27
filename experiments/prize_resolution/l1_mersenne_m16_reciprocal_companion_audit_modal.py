#!/usr/bin/env python3
"""Independent companion-matrix audit of the m=16 reciprocal elimination.

Unlike the primary certificate, this worker never forms Res(P_s,Z-W^16).
It obtains the characteristic polynomial of multiplication by W^16 from
matrix traces and Newton identities, then repeats the two small eliminants.
"""

from __future__ import annotations

import hashlib
import json
import resource
import subprocess
import time

import modal


APP_NAME = "l1-mersenne-m16-reciprocal-companion-audit"
P = 8191
M = 16
H = 15
EXPECTED = {
    "R12": "4d85a002b1a6859f596728ccb6a47946da5540bf2950ac5030e9aff9aa08f23d",
    "R13": "e9e428a171b0e4d421c2486eee0b7d2ad4fb2dc16eaabdf49ca126b52176a076",
    "G": "567ee9bf42f7ff97267c8a4b288bc4c4662688d17a1a65450df994ad120bfd94",
    "RAD": "42c76c6b52be5c2a1ced34377e1e469fd3b0114ed2d0156f2e443baf0e640a5e",
}

app = modal.App(APP_NAME)
image = modal.Image.debian_slim(python_version="3.12").run_commands(
    "apt-get update && "
    "DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends singular && "
    "rm -rf /var/lib/apt/lists/*"
)


def rising_binomial(index: int) -> str:
    if index == 0:
        return "1"
    product = "*".join(f"(s+{offset})" for offset in range(index))
    return f"({pow(__import__('math').factorial(index) % P, -1, P)})*({product})"


def emit(name: str) -> list[str]:
    return [f'print("L1_M16_AUDIT_{name}_BEGIN");', f"{name};", f'print("L1_M16_AUDIT_{name}_END");']


def singular_program() -> str:
    lines = [
        f"ring r={P},(z,t,s),lp;",
        "option(redSB);",
        f"matrix C[{H}][{H}];",
    ]
    for column in range(1, H):
        lines.append(f"C[{column + 1},{column}]=1;")
    for row in range(1, H + 1):
        coefficient_index = H + 1 - row
        lines.append(f"C[{row},{H}]=-({rising_binomial(coefficient_index)});")

    lines.extend(["matrix A=C*C;", "A=A*A;", "A=A*A;", "A=A*A;"])
    lines.append("matrix B=A;")
    trace = "+".join(f"B[{index},{index}]" for index in range(1, H + 1))
    lines.extend([f"poly p1={trace};", "poly q0=1;", "poly q1=-p1;"])
    for degree in range(2, H + 1):
        lines.append("B=B*A;")
        trace = "+".join(f"B[{index},{index}]" for index in range(1, H + 1))
        lines.append(f"poly p{degree}={trace};")
        terms = "+".join(
            f"q{degree - power}*p{power}" for power in range(1, degree + 1)
        )
        lines.append(f"poly q{degree}=-({terms})/{degree};")

    lines.extend(
        [
            'if (deg(q1)!=16 || deg(q2)!=32 || deg(q3)!=48) { print("L1_M16_AUDIT_LOW_ERROR"); quit; }',
            'if (deg(q12)!=192 || deg(q13)!=208 || deg(q14)!=224 || deg(q15)!=240) { print("L1_M16_AUDIT_HIGH_ERROR"); quit; }',
            "poly F1=q15*subst(q1,s,t)-q14;",
            "poly F2=q15*subst(q2,s,t)-q13;",
            "poly F3=q15*subst(q3,s,t)-q12;",
            "poly R12=resultant(F1,F2,t);",
            *emit("R12"),
            "poly R13=resultant(F1,F3,t);",
            *emit("R13"),
            "poly G=gcd(R12,R13);",
            *emit("G"),
            "poly GD=gcd(G,diff(G,s));",
            "poly RAD=G/GD;",
            *emit("RAD"),
            "poly EXPECTED_RAD=s*(s-1);",
            "int root_index;",
            "for (root_index=1; root_index<=15; root_index++) { EXPECTED_RAD=EXPECTED_RAD*(s+root_index); }",
            "poly DELTA=RAD-EXPECTED_RAD;",
            *emit("DELTA"),
            'print("L1_M16_AUDIT_META_BEGIN");',
            "deg(q15); size(q15);",
            "deg(R12); size(R12); deg(R13); size(R13);",
            "deg(G); size(G); deg(GD); size(GD); deg(RAD); size(RAD);",
            'print("L1_M16_AUDIT_META_END");',
            "quit;",
        ]
    )
    return "\n".join(lines) + "\n"


def extract(stdout: str, name: str) -> str | None:
    begin = f"L1_M16_AUDIT_{name}_BEGIN\n"
    end = f"\nL1_M16_AUDIT_{name}_END"
    if begin not in stdout or end not in stdout:
        return None
    return stdout.split(begin, 1)[1].split(end, 1)[0].strip()


def digest(stdout: str, name: str) -> str | None:
    value = extract(stdout, name)
    return hashlib.sha256(value.encode()).hexdigest() if value is not None else None


@app.function(image=image, cpu=1, memory=2048, timeout=195, max_containers=1)
def audit() -> dict[str, object]:
    program = singular_program()
    started = time.monotonic()
    try:
        process = subprocess.run(
            ["Singular", "-q"],
            input=program,
            text=True,
            capture_output=True,
            timeout=180,
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

    digests = {name: digest(stdout, name) for name in EXPECTED}
    delta = extract(stdout, "DELTA")
    matches = {name: digests[name] == EXPECTED[name] for name in EXPECTED}
    meta = extract(stdout, "META")
    complete = (
        not timed_out
        and returncode == 0
        and all(matches.values())
        and delta == "0"
        and meta is not None
    )
    result = {
        "app": APP_NAME,
        "status": "COMPLETE" if complete else ("TIMEOUT" if timed_out else "ERROR"),
        "p": P,
        "m": M,
        "h": H,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "seconds": round(time.monotonic() - started, 6),
        "peak_mb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss // 1024,
        "returncode": returncode,
        "digests": digests,
        "matches_primary": matches,
        "delta_zero": delta == "0",
        "meta": meta,
        "stdout_tail": stdout[-2000:] if not complete else "",
        "stderr_tail": stderr[-2000:],
    }
    print("L1_M16_COMPANION_AUDIT_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    return result


@app.local_entrypoint()
def main() -> None:
    print(json.dumps(audit.remote(), indent=2, sort_keys=True))
