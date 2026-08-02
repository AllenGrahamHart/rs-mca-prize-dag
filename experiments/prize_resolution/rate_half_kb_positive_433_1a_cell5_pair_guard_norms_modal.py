#!/usr/bin/env python3
"""Compute exact guard norms and deployed-field roots for cell 5."""

import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
FACTORIZATION = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization_result.json"
)
COORDINATE_MAP = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map_result.json"
)
ATLAS = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json"
REMOTE_FACTORIZATION = "/root/cell5_pair_primitive_factorization.json"
REMOTE_COORDINATE_MAP = "/root/cell5_pair_primitive_coordinate_map.json"
REMOTE_ATLAS = "/root/cell5_lift_atlas.json"

app = modal.App("rs-mca-positive-433-1a-cell5-pair-guard-norms")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .run_commands(
        "julia -e 'using Pkg; "
        "Pkg.add([\"AbstractAlgebra\", \"Nemo\"]); Pkg.precompile()'"
    )
    .add_local_file(FACTORIZATION, REMOTE_FACTORIZATION)
    .add_local_file(COORDINATE_MAP, REMOTE_COORDINATE_MAP)
    .add_local_file(ATLAS, REMOTE_ATLAS)
)


def fraction_expression(record):
    return f"make_fraction({record['numerator']},{record['denominator']})"


def atlas_expression(text):
    return text.replace("**", "^")


@app.function(image=image, cpu=1.0, memory=4096, timeout=300)
def compute_factor(factor_index):
    import hashlib
    import json
    import subprocess
    import tempfile
    import time

    started = time.monotonic()
    factor_raw = Path(REMOTE_FACTORIZATION).read_bytes()
    map_raw = Path(REMOTE_COORDINATE_MAP).read_bytes()
    atlas_raw = Path(REMOTE_ATLAS).read_bytes()
    factor_payload = json.loads(factor_raw)
    map_payload = json.loads(map_raw)
    atlas = json.loads(atlas_raw)
    if factor_payload["status"] != "COMPLETE" or factor_payload["returncode"] != 0:
        raise RuntimeError("primitive factorization is incomplete")
    if atlas["characteristic"] != 2130706433 or atlas["iota"] != 16711679:
        raise RuntimeError("lift-atlas field mismatch")
    factors = {}
    for record in factor_payload["factors"]:
        factors.setdefault(record["factor"], []).append(record)
    if set(factors) != set(range(1, 6)) or factor_index not in factors:
        raise RuntimeError("primitive-factor coverage mismatch")
    factor_records = sorted(
        factors[factor_index], key=lambda item: item["coefficient_degree"]
    )
    factor_degree = factor_records[0]["factor_degree"]
    if [item["coefficient_degree"] for item in factor_records] != list(
        range(factor_degree + 1)
    ):
        raise RuntimeError("factor coefficient coverage mismatch")
    maps = {}
    for shard in map_payload:
        if shard["status"] != "COMPLETE" or shard["returncode"] != 0:
            raise RuntimeError("coordinate map is incomplete")
        maps[shard["name"]] = sorted(
            shard["coordinates"], key=lambda item: item["degree"]
        )
    if set(maps) != {"b", "x0", "x1"}:
        raise RuntimeError("coordinate-map coverage mismatch")
    if any([item["degree"] for item in records] != list(range(24)) for records in maps.values()):
        raise RuntimeError("coordinate degree coverage mismatch")
    charts = {item["basis_index"]: item for item in atlas["c_charts"]}
    if 2 not in charts:
        raise RuntimeError("chart-2 formula missing")

    factor_assignments = [
        f"phi += {fraction_expression(item)}*s^{item['coefficient_degree']}"
        for item in factor_records
    ]
    map_assignments = []
    for name in ("b", "x0", "x1"):
        map_assignments.append(f"{name}=zero(R)")
        map_assignments.extend(
            f"{name} += {fraction_expression(item)}*s^{item['degree']}"
            for item in maps[name]
        )
        map_assignments.append(f"{name}=rem({name},phi)")
    r_chart = atlas["r_chart"]
    c_chart = charts[2]
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
            "function inverse_mod(value,modulus)",
            "  g,left,_=gcdx(value,modulus)",
            "  @assert degree(g)==0",
            "  return rem(left*inv(leading_coefficient(g)),modulus)",
            "end",
            "function coefficient_list(value)",
            '  if iszero(value); return "0"; end',
            '  return join([string(coeff(value,index)) for index in 0:degree(value)],",")',
            "end",
            "function power_mod_poly(base,exponent,modulus)",
            "  result=one(T)",
            "  base=rem(base,modulus)",
            "  while exponent>0",
            "    if isodd(exponent); result=rem(result*base,modulus); end",
            "    exponent >>= 1",
            "    if exponent>0; base=rem(base*base,modulus); end",
            "  end",
            "  return result",
            "end",
            "function base_roots(value)",
            "  value=value*inv(leading_coefficient(value))",
            "  if degree(value)==0; return Int[]; end",
            "  linear=gcd(value,power_mod_poly(t,2130706433,value)-t)",
            "  roots=Int[]",
            "  for (piece,multiplicity) in factor(linear)",
            "    @assert degree(piece)==1 && multiplicity==1",
            "    root=-coeff(piece,0)*inv(coeff(piece,1))",
            "    push!(roots,parse(Int,string(root)))",
            "  end",
            "  sort!(roots)",
            "  @assert length(roots)==degree(linear)",
            "  return roots",
            "end",
            "phi=zero(R)",
            *factor_assignments,
            "@assert degree(phi)==%d" % factor_degree,
            "phi=phi*inv(leading_coefficient(phi))",
            *map_assignments,
            f"rLeading=R({atlas_expression(r_chart['leading'])})",
            f"rConstant=R({atlas_expression(r_chart['constant'])})",
            "r=rem(-rConstant*inverse_mod(rLeading,phi),phi)",
            f"cLeading=R({atlas_expression(c_chart['leading'])})",
            f"cConstant=R({atlas_expression(c_chart['constant'])})",
            "c=rem(-cConstant*inverse_mod(cLeading,phi),phi)",
            "iota=R(16711679)",
            "oneR=one(R)",
            "tR=R(t)",
            "guards=Tuple{String,String,Any}[]",
            'push!(guards,("chart","r-leading",rLeading))',
            'push!(guards,("chart","c-leading",cLeading))',
            'push!(guards,("common","t-1",tR-oneR))',
            'push!(guards,("common","t+1",tR+oneR))',
            'push!(guards,("common","r-1",r-oneR))',
            'push!(guards,("common","r+1",r+oneR))',
            'push!(guards,("common","r-iota",r-iota))',
            'push!(guards,("common","r+iota",r+iota))',
            'push!(guards,("common","t-r",tR-r))',
            'push!(guards,("common","t+r",tR+r))',
            'push!(guards,("common","t-iota*r",tR-iota*r))',
            'push!(guards,("common","t+iota*r",tR+iota*r))',
            'push!(guards,("common","t-iota",tR-iota))',
            'push!(guards,("common","t+iota",tR+iota))',
            'push!(guards,("common","r",r))',
            'push!(guards,("common","t",tR))',
            'push!(guards,("common","b",b))',
            'push!(guards,("common","c",c))',
            'push!(guards,("common","b-1",b-oneR))',
            'push!(guards,("common","b+1",b+oneR))',
            'push!(guards,("common","c-1",c-oneR))',
            'push!(guards,("common","c+1",c+oneR))',
            'push!(guards,("common","c-b",c-b))',
            'push!(guards,("common","b+c",b+c))',
            "rFourth=rem(r^4,phi)",
            'for (name,value) in (("x0",x0),("x1",x1))',
            '  push!(guards,("outside_squared",name,value))',
            '  push!(guards,("outside_squared",name*"-1",value-oneR))',
            '  push!(guards,("outside_squared",name*"-t^4",value-tR^4))',
            '  push!(guards,("outside_squared",name*"-r^4",value-rFourth))',
            "end",
            "@assert length(guards)==32",
            'open("/tmp/cell5_guard_norms.tsv","w") do output',
            "  for (family,name,value) in guards",
            "    value=rem(value,phi)",
            "    normValue=resultant(phi,value)",
            "    numeratorValue=numerator(normValue)",
            "    denominatorValue=denominator(normValue)",
            "    numeratorRoots=base_roots(numeratorValue)",
            "    denominatorRoots=base_roots(denominatorValue)",
            '    println(output,family,"\\t",name,"\\t",coefficient_list(numeratorValue),"\\t",coefficient_list(denominatorValue),"\\t",join(numeratorRoots,","),"\\t",join(denominatorRoots,","))',
            "  end",
            "end",
            f'println("GUARD_NORMS_COMPLETE factor={factor_index} degree={factor_degree} records=32")',
        )
    )
    header = {
        "factor": factor_index,
        "factor_degree": factor_degree,
        "factorization_sha256": hashlib.sha256(factor_raw).hexdigest(),
        "coordinate_map_sha256": hashlib.sha256(map_raw).hexdigest(),
        "lift_atlas_sha256": hashlib.sha256(atlas_raw).hexdigest(),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "scope": (
            "exact norms and deployed-field rational roots of the 30 declared "
            "guards and two chart denominators on one generic primitive residue "
            "factor; no complete exceptional-fiber or cell closure"
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
            def decoded(value):
                if isinstance(value, bytes):
                    return value.decode("utf-8", errors="replace")
                return value or ""

            return {
                **header,
                "status": "TIMEOUT",
                "elapsed_seconds": round(time.monotonic() - started, 6),
                "stdout": decoded(error.stdout)[-4000:],
                "stderr": decoded(error.stderr)[-4000:],
            }
    valid = (
        process.returncode == 0
        and f"GUARD_NORMS_COMPLETE factor={factor_index}" in process.stdout
    )
    result = {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "returncode": process.returncode,
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "stdout": process.stdout[-4000:],
        "stderr": process.stderr[-4000:],
    }
    if valid:
        records = []
        for line in Path("/tmp/cell5_guard_norms.tsv").read_text().splitlines():
            family, name, numerator, denominator, numerator_roots, denominator_roots = line.split("\t")
            records.append(
                {
                    "family": family,
                    "guard": name,
                    "numerator": [int(value) for value in numerator.split(",")],
                    "denominator": [int(value) for value in denominator.split(",")],
                    "numerator_roots": (
                        [int(value) for value in numerator_roots.split(",")]
                        if numerator_roots
                        else []
                    ),
                    "denominator_roots": (
                        [int(value) for value in denominator_roots.split(",")]
                        if denominator_roots
                        else []
                    ),
                }
            )
        if len(records) != 32:
            raise RuntimeError("guard norm output coverage mismatch")
        result["records"] = records
    return result


@app.local_entrypoint()
def main(output: str = "", factors: str = "1,2,3,4,5"):
    selected = [int(value) for value in factors.split(",") if value]
    if not selected or len(set(selected)) != len(selected) or any(
        value not in range(1, 6) for value in selected
    ):
        raise ValueError("factors must be distinct values from 1 through 5")
    results = list(compute_factor.map(selected, order_outputs=True))
    for result in results:
        compact = {key: value for key, value in result.items() if key != "records"}
        print(json.dumps(compact, sort_keys=True), flush=True)
    if output:
        Path(output).write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
