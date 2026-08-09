#!/usr/bin/env python3
"""Replay deployed points of the cell-9 endpoint and kernel-null schemes."""

import hashlib
import itertools
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
SOURCE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_endpoint_compatibility_result.json"
)
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_compact_kernel_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_endpoint_replay_result.json"
)
REMOTE_SOURCE = "/root/endpoint_compatibility.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell9-endpoint-replay")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(SOURCE, REMOTE_SOURCE)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=180, max_containers=8)
def replay(case):
    import re

    import sympy as sp

    epsilon, endpoint = case
    z, c, b, t, r = sp.symbols("z c b t r")
    variables = {"z": z, "c": c, "b": b, "t": t, "r": r}

    def parse_singular(text):
        expression = 0
        for term in re.findall(r"[+-]?[^+-]+", text):
            sign = -1 if term.startswith("-") else 1
            unsigned = term.lstrip("+-")
            digits = re.match(r"\d*", unsigned).group()
            monomial = sp.Integer(sign * int(digits or "1"))
            suffix = unsigned[len(digits):]
            consumed = ""
            for name, exponent in re.findall(r"([zcbtr])(\d*)", suffix):
                monomial *= variables[name] ** int(exponent or "1")
                consumed += name + exponent
            if consumed != suffix:
                raise RuntimeError(f"unparsed Singular monomial: {term}")
            expression += monomial
        return expression

    def roots(expression, variable, substitutions=None):
        value = expression.subs(substitutions or {})
        polynomial = sp.Poly(value, variable, modulus=PRIME)
        _, factors = sp.factor_list(polynomial.as_expr(), variable,
                                    modulus=PRIME)
        output = []
        for factor, _ in factors:
            row = sp.Poly(factor, variable, modulus=PRIME)
            if row.degree() != 1:
                continue
            leading, constant = (
                int(coefficient) % PRIME for coefficient in row.all_coeffs()
            )
            output.append(-constant * pow(leading, -1, PRIME) % PRIME)
        return sorted(set(output))

    def linear_value(expression, variable, substitutions):
        polynomial = sp.Poly(expression.subs(substitutions), variable,
                             modulus=PRIME)
        if polynomial.degree() != 1:
            raise RuntimeError(f"nonlinear recovery for {variable}")
        leading, constant = (
            int(coefficient) % PRIME for coefficient in polynomial.all_coeffs()
        )
        return -constant * pow(leading, -1, PRIME) % PRIME

    def enumerate_basis(text_basis):
        basis = [parse_singular(value) for value in text_basis]
        if len(basis) != 5:
            raise RuntimeError("unexpected lex basis size")
        points = []
        for r_value in roots(basis[0], r):
            values = {r: r_value}
            t_value = linear_value(basis[1], t, values)
            values[t] = t_value
            for b_value in roots(basis[2], b, values):
                values[b] = b_value
                c_value = linear_value(basis[3], c, values)
                values[c] = c_value
                z_value = linear_value(basis[4], z, values)
                values[z] = z_value
                require_zero = all(
                    int(sp.Poly(item, z, c, b, t, r, modulus=PRIME)
                        .eval(values)) % PRIME == 0
                    for item in basis
                )
                if not require_zero:
                    raise RuntimeError("recovered point misses lex basis")
                guards = (
                    r_value, t_value, b_value, c_value,
                    b_value-1, b_value+1, c_value-1, c_value+1,
                    b_value-c_value, b_value+c_value,
                    r_value*r_value-1, r_value*r_value+1,
                    t_value*t_value-1, t_value*t_value+1,
                    t_value*t_value-r_value*r_value,
                    t_value*t_value+r_value*r_value,
                )
                points.append({
                    "r": r_value, "t": t_value, "b": b_value,
                    "c": c_value, "z": z_value,
                    "guard_nonzero": all(value % PRIME for value in guards),
                })
                del values[z]
                del values[c]
                del values[b]
        return points

    source = json.loads(Path(REMOTE_SOURCE).read_text())
    source_row = next(
        row for row in source["rows"]
        if row["epsilon"] == list(epsilon) and row["endpoint"] == endpoint
    )
    compatibility_points = enumerate_basis(source_row["compatibility_lex_basis"])
    null_points = enumerate_basis(source_row["kernel_null_lex_basis"])

    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    kernel_row = next(
        row for row in kernel_payload["rows"]
        if row["epsilon"] == list(epsilon)
    )
    kernel = [sp.sympify(item["expression"]) for item in kernel_row["kernel"]]
    a_coefficients = kernel[:3]
    b_coefficients = kernel[3:6]
    beta_0, beta_1 = kernel[6:]

    generic_points = []
    overlap_points = []
    for point in compatibility_points:
        substitutions = {r: point["r"], t: point["t"],
                         b: point["b"], c: point["c"]}
        values = [int(item.subs(substitutions)) % PRIME for item in kernel]
        label = -point["t"]*point["t"] % PRIME
        a_value = sum(values[index]*pow(label, index, PRIME)
                      for index in range(3)) % PRIME
        b_value = sum(values[index+3]*pow(label, index, PRIME)
                      for index in range(3)) % PRIME
        beta_value = (values[6] + values[7]*label) % PRIME
        if a_value == 0:
            if b_value or beta_value:
                raise RuntimeError("cleared-cut point has partial kernel zero")
            overlap_points.append(point)
            continue
        missing = b_value*pow(a_value, -1, PRIME) % PRIME
        source_sum = (
            label*beta_value*beta_value*pow(a_value, -2, PRIME)
        ) % PRIME
        endpoint_value = point[endpoint]
        compatibility = (
            pow((endpoint_value*endpoint_value + missing) % PRIME, 2, PRIME)
            - source_sum*endpoint_value*endpoint_value
        ) % PRIME
        if compatibility:
            raise RuntimeError("generic point fails endpoint compatibility")
        generic_points.append({
            **point, "missing": missing, "source_sum": source_sum,
        })

    def point_key(point):
        return tuple(point[name] for name in ("r", "t", "b", "c"))

    null_keys = {point_key(point) for point in null_points}
    require_overlap = {point_key(point) for point in overlap_points}
    if require_overlap != null_keys:
        raise RuntimeError("compatibility/null overlap mismatch")
    return {
        "epsilon": list(epsilon), "endpoint": endpoint,
        "status": "COMPLETE",
        "compatibility_point_count": len(compatibility_points),
        "generic_point_count": len(generic_points),
        "generic_points": generic_points,
        "kernel_null_point_count": len(null_points),
        "kernel_null_points": null_points,
        "all_guards_nonzero": all(
            point["guard_nonzero"]
            for point in [*compatibility_points, *null_points]
        ),
    }


@app.local_entrypoint()
def main():
    signs = tuple(itertools.product((-1, 1), repeat=2))
    cases = tuple(itertools.product(signs, ("b", "c")))
    rows = list(replay.map(cases, order_outputs=True))
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell9-endpoint-replay-v1",
        "field": PRIME,
        "scope": (
            "Complete deployed-point replay of the cell-9 BF/CF compatibility "
            "and shared kernel-null schemes; no residual matching claim."
        ),
        "source_compatibility_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [{key: row.get(key) for key in (
            "epsilon", "endpoint", "status", "compatibility_point_count",
            "generic_point_count", "kernel_null_point_count",
            "all_guards_nonzero",
        )} for row in rows],
    }, sort_keys=True))
