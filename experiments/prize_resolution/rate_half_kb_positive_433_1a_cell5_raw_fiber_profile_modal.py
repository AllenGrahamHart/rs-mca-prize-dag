#!/usr/bin/env python3
"""Construct the guarded squared signed-pair algebra at eight raw fibers."""

import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
FILES = (
    "check_rate_half_kb_positive_433_1a_cell5_pair_generic_guard_units.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_localized_operator.py",
    "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py",
    "rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json",
)
REMOTE_DIRECTORY = "/root/cell5_raw"
PRIME = 2130706433
IOTA = 16711679
FIBERS = (
    16711680, 16903576, 100334506, 1332924776,
    1474082935, 1665662739, 1729517783, 1783507114,
)

app = modal.App("rs-mca-positive-433-1a-cell5-raw-fiber-profile")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .pip_install("sympy==1.14.0")
    .run_commands(
        "julia -e 'using Pkg; "
        'Pkg.add(["AbstractAlgebra", "Groebner"]); Pkg.precompile()\''
    )
)
for name in FILES:
    image = image.add_local_file(DIRECTORY / name, f"{REMOTE_DIRECTORY}/{name}")


@app.function(image=image, cpu=1.0, memory=4096, timeout=300, max_containers=8)
def profile(fiber):
    import hashlib
    import importlib
    import json
    import subprocess
    import sys
    import tempfile
    import time
    from pathlib import Path

    started = time.monotonic()
    if fiber not in FIBERS:
        raise RuntimeError("fiber outside raw-basis route")
    sys.path.insert(0, REMOTE_DIRECTORY)
    guards = importlib.import_module(
        "check_rate_half_kb_positive_433_1a_cell5_pair_generic_guard_units"
    )
    sparse = importlib.import_module(
        "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe"
    )
    atlas_raw = Path(
        REMOTE_DIRECTORY,
        "rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json",
    ).read_bytes()
    atlas = json.loads(atlas_raw)
    chart = {item["basis_index"]: item for item in atlas["c_charts"]}[2]

    a0 = (
        pow(fiber, 4, PRIME)
        - 2 * IOTA * pow(fiber, 3, PRIME)
        - 4 * IOTA * fiber * fiber
        - 2 * IOTA * fiber
        - 1
    ) % PRIME
    a1 = (-8 * IOTA * (pow(fiber, 4, PRIME) + 1)) % PRIME
    a2 = (
        -2 * pow(fiber, 4, PRIME)
        + 4 * IOTA * pow(fiber, 3, PRIME)
        - 24 * IOTA * fiber * fiber
        + 4 * IOTA * fiber
        + 2
    ) % PRIME
    primitive = [a0, a1, a2, a1, a0]
    inverse = pow(primitive[-1], -1, PRIME)
    primitive = guards.trim([inverse * value for value in primitive])
    environment = {"b": [0, 1], "t": [fiber]}
    r_leading = guards.expression_mod(atlas["r_chart"]["leading"], environment, primitive)
    r_constant = guards.expression_mod(atlas["r_chart"]["constant"], environment, primitive)
    r = guards.negate(
        guards.multiply_mod(r_constant, guards.inverse_mod(r_leading, primitive), primitive)
    )
    environment["r"] = r
    c_leading = guards.expression_mod(chart["leading"], environment, primitive)
    c_constant = guards.expression_mod(chart["constant"], environment, primitive)
    c = guards.negate(
        guards.multiply_mod(c_constant, guards.inverse_mod(c_leading, primitive), primitive)
    )
    environment["c"] = c
    a2_source, a0_source, _, _, _ = sparse.sparse_product_kernel()
    d_coefficients = [
        guards.expression_mod(str(value), environment, primitive)
        for value in a2_source
    ]
    n_coefficients = [
        guards.expression_mod(str(value), environment, primitive)
        for value in a0_source
    ]

    def literal(values):
        return "[" + ",".join(str(value) for value in values) + "]"

    assignments = [f"P=embed({literal(primitive)})"]
    assignments.extend(
        f"d{index}=embed({literal(value)})"
        for index, value in enumerate(d_coefficients)
    )
    assignments.extend(
        f"n{index}=embed({literal(value)})"
        for index, value in enumerate(n_coefficients)
    )
    program = "\n".join(
        (
            "using AbstractAlgebra, Groebner, SHA",
            f"F=GF({PRIME})",
            'R,(x1,x0,B,u)=polynomial_ring(F,["x1","x0","b","u"],internal_ordering=:degrevlex)',
            "function embed(coefficients)",
            "  return sum(R(coefficients[index+1])*B^index for index in 0:length(coefficients)-1)",
            "end",
            *assignments,
            f"delta=F({fiber})^2*(F({fiber})^2-1)",
            f"beta=-F({fiber})*(1+B)*(d0+d1*F({fiber})^2+d2*F({fiber})^4)",
            "D0=d0+d1*x0+d2*x0^2",
            "D1=d0+d1*x1+d2*x1^2",
            "N0=n0+n1*x0+n2*x0^2",
            "N1=n0+n1*x1+n2*x1^2",
            "Q0=x0*beta^2*(x0-1)^2",
            "Q1=x1*beta^2*(x1-1)^2",
            "g3=N1*D0+N0*D1",
            "h=Q1*D0^2-Q0*D1^2+4*delta^2*N0*D0*D1^2",
            "denominator_guard=u*D0*D1-1",
            "system=[P,g3,h,denominator_guard]",
            'println("RAW_FIBER_BASIS_START")',
            "basis=groebner(system;ordering=DegRevLex(),linalg=:deterministic,tasks=1)",
            "@assert isgroebner(basis;ordering=DegRevLex())",
            "unit_ideal=any(isone,basis)",
            "quotient_dimension=0",
            "quotient_basis=typeof(P)[]",
            "if !unit_ideal",
            "  @assert Groebner.dimension(basis)==0",
            "  global quotient_basis=Groebner.quotient_basis(basis;ordering=DegRevLex())",
            "  global quotient_dimension=length(quotient_basis)",
            "end",
            'open("/tmp/cell5_raw_basis.txt","w") do output',
            '  println(output,"BEGIN_BASIS")',
            "  for value in basis; println(output,value); end",
            '  println(output,"BEGIN_QUOTIENT")',
            "  for value in quotient_basis; println(output,value); end",
            "end",
            'println("RAW_FIBER_BASIS_COMPLETE dimension=",quotient_dimension)',
        )
    )
    header = {
        "fiber": fiber,
        "chart": 2,
        "primitive": primitive,
        "r": r,
        "c": c,
        "d_coefficients": d_coefficients,
        "n_coefficients": n_coefficients,
        "atlas_sha256": hashlib.sha256(atlas_raw).hexdigest(),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "scope": (
            "direct fixed-fiber Groebner basis for P,g3,h localized at D0*D1; "
            "no reducedness, colored edge, other sign, route, row, or Prize closure"
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
    marker = "RAW_FIBER_BASIS_COMPLETE dimension="
    valid = process.returncode == 0 and marker in process.stdout
    result = {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "returncode": process.returncode,
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "stdout": process.stdout[-4000:],
        "stderr": process.stderr[-4000:],
    }
    if valid:
        dimension = int(process.stdout.split(marker, 1)[1].splitlines()[0])
        lines = Path("/tmp/cell5_raw_basis.txt").read_text().splitlines()
        split = lines.index("BEGIN_QUOTIENT")
        basis_lines = lines[1:split]
        quotient_lines = lines[split + 1:]
        result.update(
            {
                "quotient_dimension": dimension,
                "basis_lines": basis_lines,
                "quotient_basis_lines": quotient_lines,
                "basis_sha256": hashlib.sha256("\n".join(basis_lines).encode()).hexdigest(),
                "quotient_basis_sha256": hashlib.sha256("\n".join(quotient_lines).encode()).hexdigest(),
            }
        )
    return result


@app.local_entrypoint()
def main(output: str = ""):
    results = []
    for result in profile.map(FIBERS, order_outputs=False):
        results.append(result)
        compact = {
            key: value
            for key, value in result.items()
            if key not in {"basis_lines", "quotient_basis_lines", "d_coefficients", "n_coefficients"}
        }
        print(json.dumps(compact, sort_keys=True), flush=True)
    results.sort(key=lambda item: FIBERS.index(item["fiber"]))
    if output:
        Path(output).write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
