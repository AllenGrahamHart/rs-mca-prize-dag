#!/usr/bin/env python3
"""Native quotient-ring Singular pilot for the WCL (1,5) endpoint.

This computes Y^256 modulo the proved monic degree-five divisor directly,
extracts its five base-variable coefficients, and computes a modular basis
only in that three-variable ideal. A modular unit result is route evidence,
not the required characteristic-zero integer certificate.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import time

import modal


APP_NAME = "dli-wcl-15-quotient-singular-pilot"
MODULUS = 32003
ALGEBRA_TIMEOUT = 240
METHOD = "native_quotient_then_three_variable_std"

app = modal.App(APP_NAME)
image = modal.Image.micromamba(python_version="3.12").micromamba_install(
    "singular",
    channels=["conda-forge"],
)


def singular_program() -> str:
    return """\
ring r=32003,(Y,c0,c1,b),(lp(1),dp(3));
option(redSB);
poly A=Y^2+c1*Y+c0;
poly G=Y*A^2-(b*Y+1)^2;
ideal GB=G;
poly V=Y;
int t;
for (t=1; t<=8; t=t+1)
{
  V=reduce(V*V,GB);
  print("WCL15_QSTEP");
  print(t);
  print(size(V));
}
poly W=V-1;
poly R0=subst(W,Y,0);
W=(W-R0)/Y;
poly R1=subst(W,Y,0);
W=(W-R1)/Y;
poly R2=subst(W,Y,0);
W=(W-R2)/Y;
poly R3=subst(W,Y,0);
W=(W-R3)/Y;
poly R4=subst(W,Y,0);
W=(W-R4)/Y;
if (W!=0) { print("WCL15_BAD_Y_DEGREE"); quit; }
print("WCL15_REMAINDER_TERMS");
print(size(R0));
print(size(R1));
print(size(R2));
print(size(R3));
print(size(R4));
ideal I=R0,R1,R2,R3,R4;
print("WCL15_BASE_STD_BEGIN");
ideal J=std(I);
print("WCL15_BASE_STD_END");
print(size(J));
if (size(J)==1 && J[1]==1) { print("WCL15_UNIT"); }
else { print("WCL15_NONUNIT"); }
quit;
"""


def output_tail(value: str | bytes | None) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        value = value.decode("utf-8", errors="replace")
    return value[-4000:]


@app.function(image=image, cpu=1, memory=2048, timeout=300, max_containers=1)
def pilot() -> dict[str, object]:
    program = singular_program()
    checkpoint = {
        "app": APP_NAME,
        "modulus": MODULUS,
        "method": METHOD,
        "algebra_timeout": ALGEBRA_TIMEOUT,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
    }
    print("WCL15_QUOTIENT_INPUT " + json.dumps(checkpoint, sort_keys=True), flush=True)
    began = time.monotonic()
    try:
        process = subprocess.run(
            ["Singular", "-q"],
            input=program,
            text=True,
            capture_output=True,
            timeout=ALGEBRA_TIMEOUT,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        result = {
            **checkpoint,
            "status": "TIMEOUT",
            "unit_ideal_mod_p": None,
            "stdout_tail": output_tail(error.stdout),
            "stderr_tail": output_tail(error.stderr),
            "seconds": time.monotonic() - began,
        }
        print("WCL15_QUOTIENT_RESULT " + json.dumps(result, sort_keys=True), flush=True)
        return result

    stdout = process.stdout
    unit = "WCL15_UNIT" in stdout
    result = {
        **checkpoint,
        "status": "COMPLETE" if process.returncode == 0 else "ERROR",
        "returncode": process.returncode,
        "unit_ideal_mod_p": unit if process.returncode == 0 else None,
        "stdout_tail": output_tail(stdout),
        "stderr_tail": output_tail(process.stderr),
        "seconds": time.monotonic() - began,
    }
    print("WCL15_QUOTIENT_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    return result


@app.local_entrypoint()
def main() -> None:
    print(json.dumps(pilot.remote(), indent=2, sort_keys=True))
