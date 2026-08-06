#!/usr/bin/env python3
"""Bounded rational unit-lift pricing pilot for WCL slot `(1,6)`."""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import modal


APP_NAME = "rs-mca-wcl16-delta6-rational-lift-pricing"
OUTPUT = Path(__file__).with_name("delta6_lift_pricing_result.json")

app = modal.App(APP_NAME)
image = modal.Image.debian_slim(python_version="3.12").run_commands(
    "apt-get update",
    (
        "DEBIAN_FRONTEND=noninteractive apt-get install -y "
        "--no-install-recommends singular"
    ),
    "rm -rf /var/lib/apt/lists/*",
)


def singular_program() -> str:
    return r'''
ring source=0,(y,e2,e1,e0,b1,b0),(lp(1),dp(5));
option(redSB);
poly E=y^3+e2*y^2+e1*y+e0;
poly B=b1*y+b0;
poly G=E^2-y*B^2;
ideal Gbasis=std(G);
poly q=y;
int i;
int began=timer;
print("WCL16_STAGE_REMAINDER_BEGIN");
for (i=1; i<=8; i=i+1)
{
  q=reduce(q*q,Gbasis);
}
q=q-1;
matrix C=coef(q,y);
int remainder_ms=timer-began;
int coefficient_count=ncols(C);
int coefficient_terms=0;
int coefficient_max_terms=0;
int coefficient_max_degree=0;
for (i=1; i<=coefficient_count; i=i+1)
{
  coefficient_terms=coefficient_terms+size(C[2,i]);
  if (size(C[2,i])>coefficient_max_terms)
  {
    coefficient_max_terms=size(C[2,i]);
  }
  if (deg(C[2,i])>coefficient_max_degree)
  {
    coefficient_max_degree=deg(C[2,i]);
  }
}
print("WCL16_REMAINDER_MS="+string(remainder_ms));
print("WCL16_COEFFICIENT_COUNT="+string(coefficient_count));
print("WCL16_COEFFICIENT_TERMS="+string(coefficient_terms));
print("WCL16_COEFFICIENT_MAX_TERMS="+string(coefficient_max_terms));
print("WCL16_COEFFICIENT_MAX_DEGREE="+string(coefficient_max_degree));
if (coefficient_count!=6)
{
  print("WCL16_BAD_COEFFICIENT_COUNT");
  quit;
}
ideal I=C[2,1],C[2,2],C[2,3],C[2,4],C[2,5],C[2,6];
print("WCL16_STAGE_LIFT_BEGIN");
int lift_began=timer;
matrix T;
ideal J=liftstd(I,T);
int lift_ms=timer-lift_began;
int unit_column=0;
for (i=1; i<=size(J); i=i+1)
{
  if (J[i]==1) { unit_column=i; }
}
matrix Z=matrix(I)*T-matrix(J);
int identity_bad=0;
for (i=1; i<=ncols(Z); i=i+1)
{
  if (Z[1,i]!=0) { identity_bad=identity_bad+1; }
}
int ti;
int tj;
int transform_terms=0;
int transform_max_terms=0;
int transform_max_degree=0;
for (ti=1; ti<=nrows(T); ti=ti+1)
{
  for (tj=1; tj<=ncols(T); tj=tj+1)
  {
    transform_terms=transform_terms+size(T[ti,tj]);
    if (size(T[ti,tj])>transform_max_terms)
    {
      transform_max_terms=size(T[ti,tj]);
    }
    if (deg(T[ti,tj])>transform_max_degree)
    {
      transform_max_degree=deg(T[ti,tj]);
    }
  }
}
print("WCL16_STAGE_LIFT_END");
print("WCL16_LIFT_MS="+string(lift_ms));
print("WCL16_BASIS_SIZE="+string(size(J)));
print("WCL16_UNIT_COLUMN="+string(unit_column));
print("WCL16_IDENTITY_BAD="+string(identity_bad));
print("WCL16_TRANSFORM_ROWS="+string(nrows(T)));
print("WCL16_TRANSFORM_COLS="+string(ncols(T)));
print("WCL16_TRANSFORM_TERMS="+string(transform_terms));
print("WCL16_TRANSFORM_MAX_TERMS="+string(transform_max_terms));
print("WCL16_TRANSFORM_MAX_DEGREE="+string(transform_max_degree));
if (unit_column>0 && identity_bad==0)
{
  print("WCL16_COMPLETE_UNIT");
}
else
{
  print("WCL16_COMPLETE_NONUNIT");
}
quit;
'''.lstrip()


def parse_markers(stdout: str) -> dict[str, int]:
    prefix = "WCL16_"
    parsed: dict[str, int] = {}
    for line in stdout.splitlines():
        if not line.startswith(prefix) or "=" not in line:
            continue
        key, value = line.split("=", 1)
        try:
            parsed[key.removeprefix(prefix).lower()] = int(value)
        except ValueError:
            continue
    return parsed


@app.function(image=image, cpu=2, memory=4096, timeout=90, max_containers=1)
def pilot() -> dict[str, object]:
    program = singular_program()
    checkpoint: dict[str, object] = {
        "schema": "wcl16-delta6-rational-lift-pricing-v1",
        "app": APP_NAME,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "field": "Q",
        "variables": 5,
        "remainder_coefficients_expected": 6,
        "singular_timeout_seconds": 60,
    }
    print("WCL16_INPUT " + json.dumps(checkpoint, sort_keys=True), flush=True)
    started = time.monotonic()
    try:
        process = subprocess.run(
            ["Singular", "-q", "--ticks-per-sec=1000"],
            input=program,
            text=True,
            capture_output=True,
            timeout=60,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout or ""
        stderr = error.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode(errors="replace")
        stage = (
            "LIFT"
            if "WCL16_STAGE_LIFT_BEGIN" in stdout
            else "REMAINDER"
        )
        result = {
            **checkpoint,
            "status": f"TIMEOUT_{stage}",
            "markers": parse_markers(stdout),
            "stdout_tail": stdout[-4000:],
            "stderr_tail": stderr[-4000:],
            "seconds": round(time.monotonic() - started, 6),
        }
        print("WCL16_RESULT " + json.dumps(result, sort_keys=True), flush=True)
        return result

    stdout = process.stdout
    if "WCL16_COMPLETE_UNIT" in stdout:
        status = "COMPLETE_UNIT"
    elif "WCL16_COMPLETE_NONUNIT" in stdout:
        status = "COMPLETE_NONUNIT"
    elif "WCL16_BAD_COEFFICIENT_COUNT" in stdout:
        status = "BAD_COEFFICIENT_COUNT"
    else:
        status = "ERROR"
    result = {
        **checkpoint,
        "status": status,
        "returncode": process.returncode,
        "markers": parse_markers(stdout),
        "stdout_tail": stdout[-4000:],
        "stderr_tail": process.stderr[-4000:],
        "seconds": round(time.monotonic() - started, 6),
    }
    print("WCL16_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    return result


@app.local_entrypoint()
def main() -> None:
    result = pilot.remote()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("WCL16_LOCAL_RESULT " + json.dumps(result, sort_keys=True))
