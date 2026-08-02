#!/usr/bin/env python3
"""Exact generic signed-pair/colored-edge gcds, sharded by primitive factor."""

import hashlib
import json
import re
from pathlib import Path

import modal


HERE = Path(__file__).parent
MAPS = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map_result.json"
)
FACTORS = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization_result.json"
)
ATLAS = HERE / "rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json"
KERNEL = HERE / "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
REMOTE_MAPS = "/root/cell5_coordinate_maps.json"
REMOTE_FACTORS = "/root/cell5_primitive_factors.json"
REMOTE_ATLAS = "/root/cell5_lift_atlas.json"
REMOTE_KERNEL = "/root/cell5_sparse_edge_probe.py"

EXPECTED_MAPS_SHA256 = (
    "001c959648176669651c87a913f2c830ad425a4f1e240041cc4edeb63d69a009"
)
EXPECTED_FACTORS_SHA256 = (
    "00c4a7f0c90726b91b2310fa184d5eaf0ca3fab2b4d6a6ada1a4e1ae10f75cae"
)

app = modal.App("rs-mca-positive-433-1a-cell5-colored-generic-gcd")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .run_commands(
        "julia -e 'using Pkg; Pkg.add([\"Nemo\"]); Pkg.precompile()'"
    )
    .pip_install("sympy==1.14.0")
    .add_local_file(MAPS, REMOTE_MAPS)
    .add_local_file(FACTORS, REMOTE_FACTORS)
    .add_local_file(ATLAS, REMOTE_ATLAS)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


def _fraction(record):
    return f"make_fraction({record['numerator']},{record['denominator']})"


def _julia_expression(expression, replacements=("b", "bcoord")):
    result = expression.replace("**", "^")
    for source, target in zip(replacements[::2], replacements[1::2]):
        result = re.sub(rf"\b{re.escape(source)}\b", target, result)
    return result


@app.function(image=image, cpu=1.0, memory=8192, timeout=300, max_containers=5)
def generic_gcd(factor_index):
    import importlib.util
    import subprocess
    import tempfile
    import time

    started = time.monotonic()
    map_raw = Path(REMOTE_MAPS).read_bytes()
    factor_raw = Path(REMOTE_FACTORS).read_bytes()
    atlas_raw = Path(REMOTE_ATLAS).read_bytes()
    kernel_raw = Path(REMOTE_KERNEL).read_bytes()
    if hashlib.sha256(map_raw).hexdigest() != EXPECTED_MAPS_SHA256:
        raise RuntimeError("coordinate-map packet hash mismatch")
    if hashlib.sha256(factor_raw).hexdigest() != EXPECTED_FACTORS_SHA256:
        raise RuntimeError("primitive-factor packet hash mismatch")
    if factor_index not in range(1, 6):
        raise RuntimeError("factor index must lie in 1..5")

    map_payload = json.loads(map_raw)
    factor_payload = json.loads(factor_raw)
    atlas = json.loads(atlas_raw)
    maps = {item["name"]: sorted(item["coordinates"], key=lambda row: row["degree"])
            for item in map_payload}
    factor_rows = sorted(
        [row for row in factor_payload["factors"] if row["factor"] == factor_index],
        key=lambda row: row["coefficient_degree"],
    )
    factor_degree = factor_rows[0]["factor_degree"]
    if len(factor_rows) != factor_degree + 1:
        raise RuntimeError("factor coefficient coverage mismatch")

    specification = importlib.util.spec_from_file_location("cell5_kernel", REMOTE_KERNEL)
    kernel_module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(kernel_module)
    a2, a0, _, _, _ = kernel_module.sparse_product_kernel()
    a2_text = [_julia_expression(str(value)) for value in a2]
    a0_text = [_julia_expression(str(value)) for value in a0]
    r_chart = atlas["r_chart"]
    c_chart = {row["basis_index"]: row for row in atlas["c_charts"]}[2]

    factor_assignments = [
        f"phi += {_fraction(row)}*s^{row['coefficient_degree']}"
        for row in factor_rows
    ]
    coordinate_assignments = []
    for name in ("x1", "x0", "b"):
        target = "bcoord" if name == "b" else name
        coordinate_assignments.append(f"{target}=zero(R)")
        coordinate_assignments.extend(
            f"{target} += {_fraction(row)}*s^{row['degree']}"
            for row in maps[name]
        )
        coordinate_assignments.append(f"{target}=smod({target})")

    program = "\n".join(
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
            "function sinv(value)",
            "  value=smod(value)",
            "  @assert !iszero(value)",
            "  g,u,v=gcdx(value,phi)",
            "  @assert degree(g)==0",
            "  return smod(u*inv(coeff(g,0)))",
            "end",
            *coordinate_assignments,
            "@assert smod(x1+2*x0+3*bcoord-s)==zero(R)",
            (
                "r=smod(-(" + _julia_expression(r_chart["constant"])
                + ")*sinv(" + _julia_expression(r_chart["leading"]) + "))"
            ),
            (
                "c=smod(-(" + _julia_expression(c_chart["constant"])
                + ")*sinv(" + _julia_expression(c_chart["leading"]) + "))"
            ),
            f"d=[smod({a2_text[0]}),smod({a2_text[1]}),smod({a2_text[2]})]",
            f"n=[smod({a0_text[0]}),smod({a0_text[1]}),smod({a0_text[2]})]",
            "delta=smod(t^2*(t^2-1))",
            "delta2=smod(delta^2)",
            "dAtT2=smod(d[1]+d[2]*t^2+d[3]*t^4)",
            "beta=smod(-t*(1+bcoord)*dAtT2)",
            "d0=smod(d[1]+d[2]*x0+d[3]*x0^2)",
            "n0=smod(n[1]+n[2]*x0+n[3]*x0^2)",
            "q0sq=smod(x0*beta^2*(x0-1)^2)",
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
            "pscale(value,scalar)=ptrim([smod(item*scalar) for item in value])",
            "function ppow(value,exponent)",
            "  result=pconstant(one(R))",
            "  while exponent>0",
            "    if isodd(exponent); result=pmul(result,value); end",
            "    value=pmul(value,value); exponent=exponent>>1",
            "  end",
            "  return result",
            "end",
            "function pdivrem(dividend,divisor)",
            "  dividend=ptrim(dividend); divisor=ptrim(divisor)",
            "  @assert !(length(divisor)==1 && iszero(divisor[1]))",
            "  quotient=[zero(R) for index in 1:max(1,length(dividend)-length(divisor)+1)]",
            "  leadingInverse=sinv(divisor[end])",
            "  while !(length(dividend)==1 && iszero(dividend[1])) && length(dividend)>=length(divisor)",
            "    shift=length(dividend)-length(divisor)",
            "    scale=smod(dividend[end]*leadingInverse)",
            "    quotient[shift+1]=smod(quotient[shift+1]+scale)",
            "    for index in eachindex(divisor)",
            "      dividend[index+shift]=smod(dividend[index+shift]-scale*divisor[index])",
            "    end",
            "    dividend=ptrim(dividend)",
            "  end",
            "  return ptrim(quotient),dividend",
            "end",
            "function pxgcd(left,right)",
            "  oldR,r=ptrim(left),ptrim(right)",
            "  oldS,ss=pconstant(one(R)),pconstant(zero(R))",
            "  oldT,tt=pconstant(zero(R)),pconstant(one(R))",
            "  while !(length(r)==1 && iszero(r[1]))",
            "    q,newR=pdivrem(oldR,r)",
            "    oldR,r=r,newR",
            "    oldS,ss=ss,psub(oldS,pmul(q,ss))",
            "    oldT,tt=tt,psub(oldT,pmul(q,tt))",
            "  end",
            "  scale=sinv(oldR[end])",
            "  return pscale(oldR,scale),pscale(oldS,scale),pscale(oldT,scale)",
            "end",
            "pair=[smod(delta2*n0^2),zero(R),smod(2*delta2*n0*d0-q0sq),zero(R),smod(delta2*d0^2)]",
            "evar=[zero(R),one(R)]",
            "sum2=ppow(padd(pconstant(bcoord),evar),2)",
            "product=pscale(evar,bcoord)",
            "A=psub(pconstant(n[3]),pscale(product,d[3]))",
            "B=psub(pconstant(n[2]),pscale(product,d[2]))",
            "C=psub(pconstant(n[1]),pscale(product,d[1]))",
            "scaledSum=pscale(sum2,delta2)",
            "q0=pneg(pscale(scaledSum,smod(d[1]^2)))",
            "q1=psub(pconstant(smod(beta^2)),pscale(scaledSum,smod(2*d[1]*d[2])))",
            "q2=psub(pconstant(smod(-2*beta^2)),pscale(scaledSum,smod(d[2]^2+2*d[1]*d[3])))",
            "q3=psub(pconstant(smod(beta^2)),pscale(scaledSum,smod(2*d[2]*d[3])))",
            "q4=pneg(pscale(scaledSum,smod(d[3]^2)))",
            "r1=padd(padd(pmul(q4,padd(pneg(ppow(B,3)),pscale(pmul(pmul(A,B),C),K(2)))),pmul(q3,pmul(A,psub(ppow(B,2),pmul(A,C))))),padd(pneg(pmul(q2,pmul(ppow(A,2),B))),pmul(q1,ppow(A,3))))",
            "r0=padd(padd(pmul(q4,padd(pneg(pmul(ppow(B,2),C)),pmul(A,ppow(C,2)))),pmul(q3,pmul(pmul(A,B),C))),padd(pneg(pmul(q2,pmul(ppow(A,2),C))),pmul(q0,ppow(A,3))))",
            "compact=padd(psub(pmul(A,ppow(r0,2)),pmul(B,pmul(r0,r1))),pmul(C,ppow(r1,2)))",
            "colored,coloredRemainder=pdivrem(compact,ppow(A,3))",
            "@assert length(coloredRemainder)==1 && iszero(coloredRemainder[1])",
            "common,bezoutPair,bezoutColored=pxgcd(pair,colored)",
            "@assert padd(pmul(bezoutPair,pair),pmul(bezoutColored,colored))==common",
            "guard=[-one(R),zero(R),one(R)]",
            "guardPart,guardU,guardV=pxgcd(common,guard)",
            "outside,outsideRemainder=pdivrem(common,guardPart)",
            "@assert length(outsideRemainder)==1 && iszero(outsideRemainder[1])",
            "function coefficient_list(value)",
            '  if iszero(value); return "0"; end',
            '  return join([string(coeff(value,index)) for index in 0:degree(value)],",")',
            "end",
            "function emit(name,value)",
            "  for eDegree in 0:(length(value)-1)",
            "    coefficient=value[eDegree+1]",
            "    if iszero(coefficient)",
            '      println(name,"\\t",eDegree,"\\t",0,"\\t",0,"\\t",1)',
            "    else",
            "      for sDegree in 0:degree(coefficient)",
            "        scalar=coeff(coefficient,sDegree)",
            '        println(name,"\\t",eDegree,"\\t",sDegree,"\\t",coefficient_list(numerator(scalar)),"\\t",coefficient_list(denominator(scalar)))',
            "      end",
            "    end",
            "  end",
            "end",
            'open("/tmp/cell5_colored_generic_gcd.txt","w") do io',
            "  redirect_stdout(io) do",
            '    emit("PAIR",pair)',
            '    emit("COLORED",colored)',
            '    emit("COMMON",common)',
            '    emit("BEZOUT_PAIR",bezoutPair)',
            '    emit("BEZOUT_COLORED",bezoutColored)',
            '    emit("GUARD_PART",guardPart)',
            '    emit("OUTSIDE",outside)',
            "  end",
            "end",
            (
                f'println("COLORED_GENERIC_GCD_COMPLETE factor={factor_index} '
                f'factor_degree={factor_degree} pair_degree=",length(pair)-1,'
                '" colored_degree=",length(colored)-1," gcd_degree=",length(common)-1,'
                '" guard_part_degree=",length(guardPart)-1,'
                '" outside_degree=",length(outside)-1)'
            ),
        )
    )
    header = {
        "factor": factor_index,
        "factor_degree": factor_degree,
        "coordinate_map_sha256": hashlib.sha256(map_raw).hexdigest(),
        "primitive_factorization_sha256": hashlib.sha256(factor_raw).hexdigest(),
        "lift_atlas_sha256": hashlib.sha256(atlas_raw).hexdigest(),
        "sparse_kernel_sha256": hashlib.sha256(kernel_raw).hexdigest(),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "scope": (
            "exact gcd over F_2130706433(t)[s]/phi_j between the DE+ signed-pair "
            "necessary polynomial and the BE colored-edge necessary eliminant; "
            "exceptional t fibers, other matching cells, and the Prize claims remain open"
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
                timeout=270,
            )
        except subprocess.TimeoutExpired as error:
            return {
                **header,
                "status": "TIMEOUT",
                "elapsed_seconds": time.monotonic() - started,
                "stdout": (error.stdout or "")[-4000:],
                "stderr": (error.stderr or "")[-4000:],
            }
    marker = f"COLORED_GENERIC_GCD_COMPLETE factor={factor_index}"
    valid = process.returncode == 0 and marker in process.stdout
    result = {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "returncode": process.returncode,
        "elapsed_seconds": time.monotonic() - started,
        "stdout": process.stdout[-4000:],
        "stderr": process.stderr[-4000:],
    }
    if valid:
        records = []
        for line in Path("/tmp/cell5_colored_generic_gcd.txt").read_text().splitlines():
            name, e_degree, s_degree, numerator, denominator = line.split("\t")
            records.append(
                {
                    "name": name,
                    "e_degree": int(e_degree),
                    "s_degree": int(s_degree),
                    "numerator": [int(value) for value in numerator.split(",")],
                    "denominator": [int(value) for value in denominator.split(",")],
                }
            )
        result["records"] = records
    return result


@app.local_entrypoint()
def main(factors: str = "1,2,3,4,5", output: str = ""):
    indices = [int(value) for value in factors.split(",") if value]
    if not indices or any(value not in range(1, 6) for value in indices):
        raise ValueError("factors must be a comma-separated subset of 1..5")
    results = []
    for result in generic_gcd.map(indices, order_outputs=True):
        results.append(result)
        compact = {key: value for key, value in result.items() if key != "records"}
        print(json.dumps(compact, sort_keys=True), flush=True)
    if output:
        Path(output).write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
