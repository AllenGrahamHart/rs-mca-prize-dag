#!/usr/bin/env python3
"""Capped Singular route pilot for the pruned WCL (1,5) unit ideal.

This tests one modular Groebner basis for the exact 52-variable, 54-equation
straight-line presentation. A unit basis is route evidence only; it is not a
characteristic-zero or integer Nullstellensatz certificate. Timeout is a
representation fence. Resources are one CPU, 2 GiB, one container, and a
60-second outer timeout, with no volume writes or retries.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import time

import modal


APP_NAME = "dli-wcl-15-pruned-singular-pilot"
MODULUS = 32003

app = modal.App(APP_NAME)
image = modal.Image.debian_slim(python_version="3.12").apt_install("singular")


def polynomial_sum(terms: list[str]) -> str:
    kept = [term for term in terms if term not in {"", "0"}]
    return "+".join(kept) if kept else "0"


def variables_and_equations() -> tuple[list[str], list[str]]:
    w, s, m = 5, 2, 8
    variables = ["c0", "c1", "b"]
    variables += [f"v{t}_{j}" for t in range(s + 1, m) for j in range(w)]
    variables += [f"q{t}_{j}" for t in range(s, m) for j in range(w - 1)]

    g = ["-1", "c0^2-2*b", "2*c0*c1-b^2",
         "c1^2+2*c0", "2*c1", "1"]

    def value(t: int) -> list[str]:
        if t == s:
            return ["0", "0", "0", "0", "1"]
        if t == m:
            return ["1", "0", "0", "0", "0"]
        return [f"v{t}_{j}" for j in range(w)]

    equations = []
    for t in range(s, m):
        current = value(t)
        following = value(t + 1)
        quotient = [f"q{t}_{j}" for j in range(w - 1)]
        for degree in range(2 * w - 1):
            terms = []
            for i in range(w):
                j = degree - i
                if 0 <= j < w and current[i] != "0" and current[j] != "0":
                    terms.append(f"({current[i]})*({current[j]})")
            if degree < w and following[degree] != "0":
                terms.append(f"-({following[degree]})")
            for i in range(w + 1):
                j = degree - i
                if 0 <= j < w - 1 and g[i] != "0":
                    terms.append(f"-({g[i]})*({quotient[j]})")
            equations.append(polynomial_sum(terms))

    assert len(variables) == 52
    assert len(equations) == 54
    return variables, equations


def singular_program() -> str:
    variables, equations = variables_and_equations()
    return "\n".join(
        [
            f"ring r={MODULUS},({','.join(variables)}),dp;",
            "option(redSB);",
            f"ideal I={','.join(equations)};",
            'print("WCL15_STD_BEGIN");',
            "ideal J=std(I);",
            'print("WCL15_STD_END");',
            "print(size(J));",
            'if (size(J)==1 && J[1]==1) { print("WCL15_UNIT"); }',
            'else { print("WCL15_NONUNIT"); }',
            "quit;",
        ]
    ) + "\n"


@app.function(image=image, cpu=1, memory=2048, timeout=60, max_containers=1)
def pilot() -> dict[str, object]:
    program = singular_program()
    digest = hashlib.sha256(program.encode()).hexdigest()
    began = time.monotonic()
    checkpoint = {
        "app": APP_NAME,
        "modulus": MODULUS,
        "variables": 52,
        "equations": 54,
        "program_sha256": digest,
    }
    print("WCL15_SINGULAR_INPUT " + json.dumps(checkpoint, sort_keys=True),
          flush=True)
    try:
        process = subprocess.run(
            ["Singular", "-q"],
            input=program,
            text=True,
            capture_output=True,
            timeout=48,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        result = {
            **checkpoint,
            "status": "TIMEOUT",
            "unit_ideal_mod_p": None,
            "stdout_tail": (error.stdout or "")[-2000:],
            "stderr_tail": (error.stderr or "")[-2000:],
            "seconds": time.monotonic() - began,
        }
        print("WCL15_SINGULAR_RESULT " + json.dumps(result, sort_keys=True),
              flush=True)
        return result

    stdout = process.stdout
    unit = "WCL15_UNIT" in stdout
    result = {
        **checkpoint,
        "status": "COMPLETE" if process.returncode == 0 else "ERROR",
        "returncode": process.returncode,
        "unit_ideal_mod_p": unit if process.returncode == 0 else None,
        "stdout_tail": stdout[-2000:],
        "stderr_tail": process.stderr[-2000:],
        "seconds": time.monotonic() - began,
    }
    print("WCL15_SINGULAR_RESULT " + json.dumps(result, sort_keys=True),
          flush=True)
    return result


@app.local_entrypoint()
def main() -> None:
    print(json.dumps(pilot.remote(), indent=2, sort_keys=True))
