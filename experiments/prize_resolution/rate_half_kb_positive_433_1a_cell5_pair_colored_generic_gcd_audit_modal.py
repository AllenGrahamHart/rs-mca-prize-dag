#!/usr/bin/env python3
"""Independent exact audit of the cell-5 generic colored-gcd certificates."""

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).parent
FACTORS = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization_result.json"
)
CERTIFICATE = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd_result.json"
)
REMOTE_FACTORS = "/root/cell5_primitive_factors.json"
REMOTE_CERTIFICATE = "/root/cell5_colored_generic_gcd.json"
EXPECTED_FACTORS_SHA256 = (
    "00c4a7f0c90726b91b2310fa184d5eaf0ca3fab2b4d6a6ada1a4e1ae10f75cae"
)
EXPECTED_CERTIFICATE_SHA256 = (
    "710b438062fc2e80f5c7b14ffb987d8f36a02d4b57953b30419bb320b88877a7"
)
NAMES = (
    "PAIR",
    "COLORED",
    "COMMON",
    "BEZOUT_PAIR",
    "BEZOUT_COLORED",
    "GUARD_PART",
    "OUTSIDE",
)

app = modal.App("rs-mca-positive-433-1a-cell5-colored-gcd-audit")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .run_commands(
        "julia -e 'using Pkg; Pkg.add([\"Nemo\"]); Pkg.precompile()'"
    )
    .add_local_file(FACTORS, REMOTE_FACTORS)
    .add_local_file(CERTIFICATE, REMOTE_CERTIFICATE)
)


def fraction_literal(record):
    return f"make_fraction({record['numerator']},{record['denominator']})"


def build_program(factor_index, factor_payload, certificate_payload):
    factor_rows = sorted(
        [row for row in factor_payload["factors"] if row["factor"] == factor_index],
        key=lambda row: row["coefficient_degree"],
    )
    factor_degree = factor_rows[0]["factor_degree"]
    certificate = certificate_payload[factor_index - 1]
    if certificate["factor"] != factor_index:
        raise RuntimeError("certificate factor order mismatch")
    records = certificate["records"]
    assignments = []
    for name in NAMES:
        selected = [row for row in records if row["name"] == name]
        if not selected:
            raise RuntimeError(f"missing {name} certificate records")
        maximum = max(row["e_degree"] for row in selected)
        assignments.append(f"{name}=[zero(R) for index in 0:{maximum}]")
        assignments.extend(
            f"{name}[{row['e_degree'] + 1}]=smod({name}[{row['e_degree'] + 1}]"
            f"+{fraction_literal(row)}*s^{row['s_degree']})"
            for row in selected
        )
        assignments.append(f"{name}=ptrim({name})")
    factor_assignments = [
        f"phi += {fraction_literal(row)}*s^{row['coefficient_degree']}"
        for row in factor_rows
    ]
    expected_common = "guard" if factor_index != 4 else "pconstant(one(R))"
    return "\n".join(
        (
            "using Nemo, SHA",
            "F=GF(2130706433)",
            'T,t=polynomial_ring(F,"t")',
            "K=fraction_field(T)",
            'R,s=polynomial_ring(K,"s")',
            "function make_fraction(numeratorCoefficients,denominatorCoefficients)",
            "  numerator=T([F(value) for value in numeratorCoefficients])",
            "  denominator=T([F(value) for value in denominatorCoefficients])",
            "  return numerator//denominator",
            "end",
            "phi=zero(R)",
            *factor_assignments,
            f"@assert degree(phi)=={factor_degree}",
            "@assert leading_coefficient(phi)==K(1)",
            "smod(value)=rem(R(value),phi)",
            "function ptrim(value)",
            "  result=copy(value)",
            "  while length(result)>1 && iszero(result[end]); pop!(result); end",
            "  return result",
            "end",
            "pconstant(value)=[smod(value)]",
            "function padd(left,right)",
            "  result=[zero(R) for index in 1:max(length(left),length(right))]",
            "  for index in eachindex(result)",
            "    a=index<=length(left) ? left[index] : zero(R)",
            "    b=index<=length(right) ? right[index] : zero(R)",
            "    result[index]=smod(a+b)",
            "  end",
            "  return ptrim(result)",
            "end",
            "pneg(value)=ptrim([smod(-item) for item in value])",
            "psub(left,right)=padd(left,pneg(right))",
            "function pmul(left,right)",
            "  result=[zero(R) for index in 1:(length(left)+length(right)-1)]",
            "  for i in eachindex(left), j in eachindex(right)",
            "    result[i+j-1]=smod(result[i+j-1]+left[i]*right[j])",
            "  end",
            "  return ptrim(result)",
            "end",
            *assignments,
            "bezout=",
            "  padd(pmul(BEZOUT_PAIR,PAIR),pmul(BEZOUT_COLORED,COLORED))",
            "@assert bezout==COMMON",
            "guard=[-one(R),zero(R),one(R)]",
            f"@assert COMMON=={expected_common}",
            f"@assert GUARD_PART=={expected_common}",
            "@assert OUTSIDE==pconstant(one(R))",
            (
                f'println("COLORED_GENERIC_GCD_AUDIT_PASS factor={factor_index} '
                f'factor_degree={factor_degree} common=",'
                '(length(COMMON)==1 ? "one" : "e2_minus_1"))'
            ),
        )
    )


@app.function(image=image, cpu=1.0, memory=4096, timeout=180, max_containers=5)
def audit_factor(factor_index):
    import subprocess
    import tempfile
    import time

    started = time.monotonic()
    factor_raw = Path(REMOTE_FACTORS).read_bytes()
    certificate_raw = Path(REMOTE_CERTIFICATE).read_bytes()
    if hashlib.sha256(factor_raw).hexdigest() != EXPECTED_FACTORS_SHA256:
        raise RuntimeError("primitive-factor packet hash mismatch")
    if hashlib.sha256(certificate_raw).hexdigest() != EXPECTED_CERTIFICATE_SHA256:
        raise RuntimeError("generic-gcd certificate hash mismatch")
    if factor_index not in range(1, 6):
        raise RuntimeError("factor index must lie in 1..5")
    factor_payload = json.loads(factor_raw)
    certificate_payload = json.loads(certificate_raw)
    program = build_program(factor_index, factor_payload, certificate_payload)
    header = {
        "factor": factor_index,
        "factorization_sha256": hashlib.sha256(factor_raw).hexdigest(),
        "certificate_sha256": hashlib.sha256(certificate_raw).hexdigest(),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "scope": (
            "independent exact replay of the returned generic Bezout identity "
            "and its common-factor support; source-equation reconstruction and "
            "exceptional t fibers remain separate"
        ),
    }
    with tempfile.NamedTemporaryFile(mode="w", suffix=".jl") as handle:
        handle.write(program)
        handle.flush()
        try:
            process = subprocess.run(
                ["julia", "--startup-file=no", handle.name],
                capture_output=True,
                text=True,
                timeout=150,
            )
        except subprocess.TimeoutExpired as error:
            return {
                **header,
                "status": "TIMEOUT",
                "elapsed_seconds": time.monotonic() - started,
                "stdout": (error.stdout or "")[-2000:],
                "stderr": (error.stderr or "")[-2000:],
            }
    marker = f"COLORED_GENERIC_GCD_AUDIT_PASS factor={factor_index}"
    return {
        **header,
        "status": (
            "COMPLETE"
            if process.returncode == 0 and marker in process.stdout
            else "ERROR"
        ),
        "returncode": process.returncode,
        "elapsed_seconds": time.monotonic() - started,
        "stdout": process.stdout[-2000:],
        "stderr": process.stderr[-2000:],
    }


@app.local_entrypoint()
def main(factors: str = "1,2,3,4,5", output: str = ""):
    indices = [int(value) for value in factors.split(",") if value]
    if not indices or any(value not in range(1, 6) for value in indices):
        raise ValueError("factors must be a comma-separated subset of 1..5")
    results = list(audit_factor.map(indices, order_outputs=True))
    for result in results:
        print(json.dumps(result, sort_keys=True), flush=True)
    if output:
        Path(output).write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
