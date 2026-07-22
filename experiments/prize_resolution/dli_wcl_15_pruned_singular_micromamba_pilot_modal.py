#!/usr/bin/env python3
"""Minimal-image Singular pilot for the pruned WCL (1,5) unit ideal.

The first committed version benchmarked one global ``dp`` standard basis.
This successor eliminates the 49 deterministic lift variables directly and
computes the exact intersection with the three-variable base ring. A modular
unit result is evidence that integer certificate reconstruction is viable;
it is not itself the required characteristic-zero certificate.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import time

import modal


APP_NAME = "dli-wcl-15-pruned-singular-micromamba-pilot"
MODULUS = 32003
ALGEBRA_TIMEOUT = 240
METHOD = "eliminate_49_auxiliaries"

app = modal.App(APP_NAME)
image = modal.Image.micromamba(python_version="3.12").micromamba_install(
    "singular",
    channels=["conda-forge"],
)


def polynomial_sum(terms: list[str]) -> str:
    kept = [term for term in terms if term not in {"", "0"}]
    return "+".join(kept) if kept else "0"


def variables_and_equations() -> tuple[list[str], list[str]]:
    w, s, m = 5, 2, 8
    variables = ["c0", "c1", "b"]
    variables += [f"v{t}_{j}" for t in range(s + 1, m) for j in range(w)]
    variables += [f"q{t}_{j}" for t in range(s, m) for j in range(w - 1)]

    g = [
        "-1",
        "c0^2-2*b",
        "2*c0*c1-b^2",
        "c1^2+2*c0",
        "2*c1",
        "1",
    ]

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
    auxiliary_product = "*".join(variables[3:])
    return "\n".join(
        [
            f"ring r={MODULUS},({','.join(variables)}),dp;",
            "option(redSB);",
            f"ideal I={','.join(equations)};",
            'print("WCL15_ELIM_BEGIN");',
            f"ideal J=eliminate(I,{auxiliary_product});",
            'print("WCL15_ELIM_END");',
            "print(size(J));",
            'if (size(J)==1 && J[1]==1) { print("WCL15_UNIT"); }',
            'else { print("WCL15_NONUNIT"); }',
            "quit;",
        ]
    ) + "\n"


def output_tail(value: str | bytes | None) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        value = value.decode("utf-8", errors="replace")
    return value[-2000:]


@app.function(image=image, cpu=1, memory=2048, timeout=300, max_containers=1)
def pilot() -> dict[str, object]:
    program = singular_program()
    checkpoint = {
        "app": APP_NAME,
        "modulus": MODULUS,
        "variables": 52,
        "equations": 54,
        "algebra_timeout": ALGEBRA_TIMEOUT,
        "method": METHOD,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
    }
    print("WCL15_SINGULAR_INPUT " + json.dumps(checkpoint, sort_keys=True), flush=True)
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
        print("WCL15_SINGULAR_RESULT " + json.dumps(result, sort_keys=True), flush=True)
        return result

    result = {
        **checkpoint,
        "status": "COMPLETE" if process.returncode == 0 else "ERROR",
        "returncode": process.returncode,
        "unit_ideal_mod_p": (
            "WCL15_UNIT" in process.stdout if process.returncode == 0 else None
        ),
        "stdout_tail": process.stdout[-2000:],
        "stderr_tail": process.stderr[-2000:],
        "seconds": time.monotonic() - began,
    }
    print("WCL15_SINGULAR_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    return result


@app.local_entrypoint()
def main() -> None:
    print(json.dumps(pilot.remote(), indent=2, sort_keys=True))
