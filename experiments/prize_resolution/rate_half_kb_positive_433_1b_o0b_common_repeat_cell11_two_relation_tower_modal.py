#!/usr/bin/env python3
"""Certify two-relation complete-intersection towers for cell 11."""

from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import time

import modal


DIRECTORY = Path(__file__).parent
INPUT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_symmetric_tower_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_two_relation_tower_result.json"
)
REMOTE_INPUT = "/root/input.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-o0b-cell11-two-relation-tower")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(INPUT, REMOTE_INPUT)
)


def explicit_polynomial(text):
    terms = []
    for raw in re.findall(r"[+-]?[^+-]+", text):
        match = re.fullmatch(r"([+-]?)(\d*)((?:[ryx]\d*)*)", raw)
        if not match:
            raise ValueError(f"unsupported compact monomial: {raw}")
        sign, coefficient, monomial = match.groups()
        factors = []
        if coefficient:
            factors.append(coefficient)
        for variable, exponent in re.findall(r"([ryx])(\d*)", monomial):
            factors.append(variable if not exponent else f"{variable}^{exponent}")
        body = "*".join(factors) if factors else "1"
        terms.append(("-" if sign == "-" else "+") + body)
    return "".join(terms).lstrip("+")


@app.function(image=image, cpu=1.0, memory=2048, timeout=120, max_containers=8)
def certify(row):
    started = time.perf_counter()
    lines = row["tower_output"].splitlines()
    compact = [line.rstrip(",") for line in lines[2:] if line.strip()]
    polynomials = [explicit_polynomial(value) for value in compact]
    quadratic_index = 1
    definitions = "\n".join(
        f"poly f{index}={value};" for index, value in enumerate(polynomials)
    )
    program = f"""
ring R={PRIME},(z,r,y,x),(dp(1),lp);
option(redSB);
{definitions}
poly chart=x*y*(x-1)*(x+1);
ideal H=f0,f1,f2,f3;
ideal C0=H,chart; ideal C=std(C0);
ideal HL0=H,z*chart-1; ideal HL=std(HL0);
ideal J0=f0,f{quadratic_index},z*chart-1; ideal J=std(J0);
print("CHART_BEGIN"); print(reduce(1,C)); print("CHART_END");
print("CHART_DIM="+string(dim(C))); print("CHART_SIZE="+string(size(C)));
if (dim(C)==0) {{ print("CHART_VDIM="+string(vdim(C))); }};
print("DIMS="+string(dim(HL))+","+string(dim(J)));
print("SIZES="+string(size(HL))+","+string(size(J)));
print("R0_BEGIN"); print(reduce(f0,J)); print("R0_END");
print("R1_BEGIN"); print(reduce(f1,J)); print("R1_END");
print("R2_BEGIN"); print(reduce(f2,J)); print("R2_END");
print("R3_BEGIN"); print(reduce(f3,J)); print("R3_END");
print("END"); quit;
"""
    process = subprocess.run(
        ["Singular", "--quiet"], input=program, capture_output=True,
        text=True, timeout=90,
    )

    def between(left, right):
        match = re.search(rf"{left}\n(.*?)\n{right}", process.stdout, re.DOTALL)
        return "".join(match.group(1).split()) if match else None

    chart_remainder = between("CHART_BEGIN", "CHART_END")
    remainders = [between(f"R{index}_BEGIN", f"R{index}_END")
                  for index in range(4)]
    dimensions = re.search(r"DIMS=(-?\d+),(-?\d+)", process.stdout)
    sizes = re.search(r"SIZES=(\d+),(\d+)", process.stdout)

    def value(label):
        found = re.search(rf"{label}=(-?\d+)", process.stdout)
        return int(found.group(1)) if found else None

    valid = (
        process.returncode == 0 and "END" in process.stdout
        and "?" not in process.stdout
        and remainders == ["0"] * 4 and dimensions and sizes
    )
    return {
        "epsilon": row["epsilon"], "bc_sign": row["bc_sign"],
        "status": "COMPLETE" if valid else "ERROR",
        "chart": "x*y*(x-1)*(x+1)",
        "chart_zero_remainder": chart_remainder,
        "closure_chart_boundary_dimension": value("CHART_DIM"),
        "closure_chart_boundary_basis_size": value("CHART_SIZE"),
        "closure_chart_boundary_vdim": value("CHART_VDIM"),
        "plane_relation": compact[0],
        "quadratic_relation": compact[quadratic_index],
        "quadratic_relation_index": quadratic_index,
        "localized_full_dimension": int(dimensions.group(1)) if dimensions else None,
        "localized_two_relation_dimension": int(dimensions.group(2)) if dimensions else None,
        "localized_full_size": int(sizes.group(1)) if sizes else None,
        "localized_two_relation_size": int(sizes.group(2)) if sizes else None,
        "full_generators_mod_two_relation": remainders,
        "generic_extension_degree": 6 if row["bc_sign"] == -1 else 4,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stderr": process.stderr[-2000:],
        "stdout_on_error": process.stdout[-8000:] if not valid else None,
        "seconds": time.perf_counter() - started,
    }


@app.local_entrypoint()
def main():
    payload = json.loads(INPUT.read_text())
    cases = tuple(payload["rows"])
    raw = list(certify.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": case["epsilon"], "bc_sign": case["bc_sign"],
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-o0b-common-repeat-"
            "cell11-two-relation-tower-v1"
        ),
        "scope": (
            "Bidirectional localized ideal certificate for degree-six BC- "
            "and degree-four BC+ symmetric function-field towers."
        ),
        "source_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
        "status_counts": dict(sorted(Counter(
            row["status"] for row in rows
        ).items())),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT), "status_counts": output["status_counts"],
        "rows": [{
            "epsilon": row["epsilon"], "bc_sign": row["bc_sign"],
            "status": row["status"],
            "chart": row.get("chart_zero_remainder"),
            "dimensions": [row.get("localized_full_dimension"),
                           row.get("localized_two_relation_dimension")],
            "remainders": row.get("full_generators_mod_two_relation"),
            "degree": row.get("generic_extension_degree"),
            "seconds": row.get("seconds"),
        } for row in rows],
    }, sort_keys=True))
