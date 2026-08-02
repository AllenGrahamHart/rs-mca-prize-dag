#!/usr/bin/env python3
"""Census deployed-field roots of every cell-5 certificate denominator."""

import json

import modal
from pathlib import Path


DIRECTORY = Path(__file__).parent
INPUTS = {
    "basis": DIRECTORY
    / "rate_half_kb_positive_433_1a_cell5_pair_function_field_julia_basis_result.json",
    "primitive_factor": DIRECTORY
    / "rate_half_kb_positive_433_1a_cell5_pair_primitive_polynomial_result.json",
    "factorization": DIRECTORY
    / "rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization_result.json",
    "maps": DIRECTORY
    / "rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map_result.json",
    "colored": DIRECTORY
    / "rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd_result.json",
    "guard_norms": DIRECTORY
    / "rate_half_kb_positive_433_1a_cell5_pair_guard_norms_result.json",
    "operator": DIRECTORY
    / "rate_half_kb_positive_433_1a_cell5_pair_localized_operator_merged_result.json",
}
REMOTE_INPUTS = {name: f"/root/cell5_{name}.json" for name in INPUTS}
CATEGORIES = (
    "basis", "primitive_factor", "maps", "colored", "guard_norms", "operator"
)

app = modal.App("rs-mca-positive-433-1a-cell5-specialization-poles")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .run_commands("julia -e 'using Pkg; Pkg.add([\"Nemo\"]); Pkg.precompile()'")
)
for name, path in INPUTS.items():
    image = image.add_local_file(path, REMOTE_INPUTS[name])


@app.function(image=image, cpu=1.0, memory=4096, timeout=300, max_containers=5)
def compute_category(category):
    import ast
    import hashlib
    import json
    import re
    import subprocess
    import tempfile
    import time

    started = time.monotonic()
    if category not in CATEGORIES:
        raise RuntimeError("unknown denominator category")

    def trim(polynomial):
        polynomial = [value % 2130706433 for value in polynomial]
        while len(polynomial) > 1 and polynomial[-1] == 0:
            polynomial.pop()
        return polynomial

    def add(left, right):
        return trim([
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
            for index in range(max(len(left), len(right)))
        ])

    def negate(value):
        return trim([-item for item in value])

    def multiply(left, right):
        output = [0] * (len(left) + len(right) - 1)
        for left_index, left_value in enumerate(left):
            for right_index, right_value in enumerate(right):
                output[left_index + right_index] = (
                    output[left_index + right_index] + left_value * right_value
                ) % 2130706433
        return trim(output)

    def power(value, exponent):
        output = [1]
        while exponent:
            if exponent & 1:
                output = multiply(output, value)
            exponent >>= 1
            if exponent:
                value = multiply(value, value)
        return output

    def parse_polynomial(text):
        def visit(node):
            if isinstance(node, ast.Constant) and isinstance(node.value, int):
                return [node.value]
            if isinstance(node, ast.Name) and node.id == "t":
                return [0, 1]
            if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
                return negate(visit(node.operand))
            if isinstance(node, ast.BinOp):
                if isinstance(node.op, ast.Add):
                    return add(visit(node.left), visit(node.right))
                if isinstance(node.op, ast.Sub):
                    return add(visit(node.left), negate(visit(node.right)))
                if isinstance(node.op, ast.Mult):
                    return multiply(visit(node.left), visit(node.right))
                if isinstance(node.op, ast.Pow):
                    if not isinstance(node.right, ast.Constant) or not isinstance(
                        node.right.value, int
                    ):
                        raise RuntimeError("nonintegral basis denominator exponent")
                    return power(visit(node.left), node.right.value)
            raise RuntimeError(f"unsupported denominator syntax {type(node).__name__}")

        return trim(visit(ast.parse(text.replace("^", "**"), mode="eval").body))

    def collect_structured(value, output):
        if isinstance(value, dict):
            for key, child in value.items():
                if (
                    key == "denominator"
                    and isinstance(child, list)
                    and child
                    and all(isinstance(item, int) for item in child)
                ):
                    output.append(trim(child))
                collect_structured(child, output)
        elif isinstance(value, list):
            for child in value:
                collect_structured(child, output)

    source_names = {
        "basis": ("basis",),
        "primitive_factor": ("primitive_factor", "factorization"),
        "maps": ("maps",),
        "colored": ("colored",),
        "guard_norms": ("guard_norms",),
        "operator": ("operator",),
    }[category]
    raws = {name: Path(REMOTE_INPUTS[name]).read_bytes() for name in source_names}
    denominators = []
    if category == "basis":
        payload = json.loads(raws["basis"])
        if not isinstance(payload, list) or len(payload) != 1:
            raise RuntimeError("basis packet shape mismatch")
        for line in payload[0]["basis_lines"]:
            texts = re.findall(r"//\(([^()]*)\)", line)
            if len(texts) != line.count("//"):
                raise RuntimeError("unparsed basis denominator")
            denominators.extend(parse_polynomial(text) for text in texts)
    else:
        for raw in raws.values():
            collect_structured(json.loads(raw), denominators)
    if not denominators or any(value == [0] for value in denominators):
        raise RuntimeError("empty or zero denominator census")
    occurrence_count = len(denominators)
    counts = {}
    for value in denominators:
        key = tuple(value)
        counts[key] = counts.get(key, 0) + 1
    unique = sorted(counts, key=lambda value: (len(value), value))
    assignments = [
        f"push!(polynomials,T([F(value) for value in {list(value)}]))"
        for value in unique
    ]
    program = "\n".join(
        (
            "using Nemo",
            "F=GF(2130706433)",
            'T,t=polynomial_ring(F,"t")',
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
            "polynomials=typeof(t)[]",
            *assignments,
            f"@assert length(polynomials)=={len(unique)}",
            'open("/tmp/cell5_specialization_poles.tsv","w") do output',
            "  for (index,value) in enumerate(polynomials)",
            "    roots=base_roots(value)",
            '    println(output,index,"\\t",degree(value),"\\t",join(roots,","))',
            "  end",
            "end",
            f'println("SPECIALIZATION_POLES_COMPLETE category={category} unique={len(unique)}")',
        )
    )
    header = {
        "category": category,
        "source_sha256": {
            name: hashlib.sha256(raw).hexdigest() for name, raw in raws.items()
        },
        "occurrences": occurrence_count,
        "unique_denominators": len(unique),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "scope": (
            "exact deployed-field rational roots of every coefficient denominator "
            "in one cell-5 certificate category; no norm-zero, vertical-fiber, "
            "sign-row, cell, or Prize closure"
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
        and f"SPECIALIZATION_POLES_COMPLETE category={category}" in process.stdout
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
        output = {}
        for line in Path("/tmp/cell5_specialization_poles.tsv").read_text().splitlines():
            index, degree, roots = line.split("\t")
            output[int(index)] = {
                "degree": int(degree),
                "roots": [int(value) for value in roots.split(",")] if roots else [],
            }
        if set(output) != set(range(1, len(unique) + 1)):
            raise RuntimeError("denominator result coverage mismatch")
        result["records"] = [
            {
                "denominator": list(value),
                "occurrences": counts[value],
                **output[index],
            }
            for index, value in enumerate(unique, start=1)
        ]
    return result


@app.local_entrypoint()
def main(output: str = "", categories: str = ",".join(CATEGORIES)):
    selected = [value for value in categories.split(",") if value]
    if not selected or len(set(selected)) != len(selected) or any(
        value not in CATEGORIES for value in selected
    ):
        raise ValueError("categories must be a distinct subset of the declared categories")
    results = list(compute_category.map(selected, order_outputs=True))
    for result in results:
        compact = {key: value for key, value in result.items() if key != "records"}
        print(json.dumps(compact, sort_keys=True), flush=True)
    if output:
        Path(output).write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
