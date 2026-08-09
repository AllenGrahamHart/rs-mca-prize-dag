#!/usr/bin/env python3
"""Independently audit all field roots used by the cell-11 parallel-DE norms."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
NORM = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_parallel_de_four_basis_norm_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_parallel_de_norm_frobenius_audit_result.json"
)
REMOTE_NORM = "/root/norm.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell11-parallel-de-frobenius-audit")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(NORM, REMOTE_NORM)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=240, max_containers=8)
def audit(key):
    import sympy as sp
    from sympy.polys.domains import ZZ
    from sympy.polys.galoistools import (
        gf_factor_sqf,
        gf_gcd,
        gf_pow_mod,
        gf_sub,
    )

    epsilon_1, epsilon_2, cut_kind = key
    payload = json.loads(Path(REMOTE_NORM).read_text())
    row = next(
        item for item in payload["rows"]
        if item["epsilon"] == [epsilon_1, epsilon_2]
        and item["cut_kind"] == cut_kind
    )
    r = sp.symbols("r")

    def root_profile(profile):
        expression = sp.sympify(profile["expression"])
        polynomial = sp.Poly(expression, r, modulus=PRIME)
        text = str(polynomial.as_expr())
        if hashlib.sha256(text.encode()).hexdigest() != profile["sha256"]:
            raise RuntimeError("polynomial digest mismatch")
        coefficients = [
            int(value) % PRIME for value in polynomial.all_coeffs()
        ]
        if polynomial.is_zero:
            return None
        if polynomial.degree() == 0:
            return []
        x_to_p = gf_pow_mod([1, 0], PRIME, coefficients, PRIME, ZZ)
        root_gcd = gf_gcd(
            coefficients,
            gf_sub(x_to_p, [1, 0], PRIME, ZZ),
            PRIME,
            ZZ,
        )
        _, factors = gf_factor_sqf(root_gcd, PRIME, ZZ)
        roots = []
        for factor in factors:
            if len(factor) != 2:
                raise RuntimeError("nonlinear factor in root part")
            roots.append(
                -int(factor[1]) * pow(int(factor[0]), -1, PRIME) % PRIME
            )
        return sorted(set(roots))

    target_roots = root_profile(row["target_norm"]["numerator"])
    guard_roots = set()
    visits = 1
    signatures = {row["target_norm"]["numerator"]["sha256"]}
    for guard in row["inverse_guards"]:
        for side in ("numerator", "denominator"):
            profile = guard[side]
            signatures.add(profile["sha256"])
            values = root_profile(profile)
            visits += 1
            if values is not None:
                guard_roots.update(values)
    candidate_roots = sorted(set(target_roots or ()) | guard_roots)
    if target_roots != row["target_roots"]:
        raise RuntimeError("target-root mismatch")
    if len(guard_roots) != row["guard_root_count"]:
        raise RuntimeError("guard-root mismatch")
    if candidate_roots != row["candidate_roots"]:
        raise RuntimeError("candidate-union mismatch")
    return {
        "epsilon": [epsilon_1, epsilon_2],
        "cut_kind": cut_kind,
        "status": "COMPLETE",
        "profile_visits": visits,
        "unique_profiles": len(signatures),
        "target_roots": target_roots,
        "guard_roots": sorted(guard_roots),
        "candidate_roots": candidate_roots,
    }


@app.local_entrypoint()
def main():
    payload = json.loads(NORM.read_text())
    keys = tuple(
        (*row["epsilon"], row["cut_kind"]) for row in payload["rows"]
    )
    raw = list(audit.map(keys, order_outputs=True, return_exceptions=True))
    rows = []
    for key, result in zip(keys, raw):
        if isinstance(result, BaseException):
            rows.append({
                "epsilon": list(key[:2]),
                "cut_kind": key[2],
                "status": "REMOTE_ERROR",
                "error": repr(result),
            })
        else:
            rows.append(result)
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-cell11-parallel-de-"
            "norm-frobenius-audit-v1"
        ),
        "field": PRIME,
        "method": "galoistools gcd(f,r^p-r) and square-free root-part factor",
        "source_norm_sha256": hashlib.sha256(NORM.read_bytes()).hexdigest(),
        "complete": (
            len(rows) == 8
            and all(row.get("status") == "COMPLETE" for row in rows)
        ),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "complete": output["complete"],
        "rows": len(rows),
        "profile_visits": sum(row.get("profile_visits", 0) for row in rows),
        "unique_profiles": sum(row.get("unique_profiles", 0) for row in rows),
        "candidate_roots": sum(len(row.get("candidate_roots", []))
                               for row in rows),
    }, sort_keys=True))
