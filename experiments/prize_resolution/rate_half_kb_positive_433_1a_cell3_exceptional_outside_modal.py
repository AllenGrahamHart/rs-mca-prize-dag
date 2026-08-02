#!/usr/bin/env python3
"""Test necessary outside families at the two cell-3 exceptional points."""

import hashlib
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
KERNEL = DIRECTORY / "rate_half_kb_positive_433_1a_cell3_kernel_reduction_result.json"
POINTS = DIRECTORY / "rate_half_kb_positive_433_1a_cell3_exceptional_point_lift_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell3_exceptional_outside_result.json"
REMOTE_KERNEL = "/root/cell3_kernel_reduction.json"
REMOTE_POINTS = "/root/cell3_exceptional_points.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell3-exceptional-outside")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(KERNEL, REMOTE_KERNEL)
    .add_local_file(POINTS, REMOTE_POINTS)
)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


@app.function(image=image, cpu=1.0, memory=2048, timeout=150, max_containers=2)
def test_point(point):
    kernel = json.loads(Path(REMOTE_KERNEL).read_text())["result"]

    def evaluate_compact(value):
        total = 0
        for raw_term in re.findall(r"[+-]?[^+-]+", value):
            sign = 1
            term = raw_term
            if term.startswith("+"):
                term = term[1:]
            elif term.startswith("-"):
                sign = -1
                term = term[1:]
            match = re.match(r"\d+", term)
            coefficient = int(match.group(0)) if match else 1
            term = term[match.end():] if match else term
            monomial = coefficient
            while term:
                match = re.match(r"([crbt])(\d*)", term)
                if match is None:
                    raise RuntimeError(f"cannot parse {term!r}")
                variable, exponent = match.groups()
                monomial = monomial*pow(
                    point[variable], int(exponent) if exponent else 1, PRIME
                ) % PRIME
                term = term[match.end():]
            total = (total + sign*monomial) % PRIME
        return total

    coefficients = {
        name: evaluate_compact(value)
        for name, value in kernel["reduced_coefficients"].items()
    }
    if not any(coefficients.values()) or coefficients["b10"] != (-coefficients["b11"]) % PRIME:
        raise RuntimeError("invalid exceptional kernel")
    common_labels = (
        1,
        point["t"]**2 % PRIME,
        PRIME-1,
        point["r"]**2 % PRIME,
        (-point["r"]**2) % PRIME,
    )

    def common_definitions(roots):
        lines = []
        for index, root in enumerate(roots):
            lines.extend((
                f"poly D{index}={coefficients['a20']}+{coefficients['a21']}*{root}^2+{coefficients['a22']}*{root}^4;",
                f"poly N{index}={coefficients['a00']}+{coefficients['a01']}*{root}^2+{coefficients['a02']}*{root}^4;",
                f"poly Q{index}={root}*({coefficients['b10']}+{coefficients['b11']}*{root}^2);",
            ))
        return "\n".join(lines)

    pair_guards = ["z0", "z1", "D0", "D1", "z0^2-z1^2"]
    for root in ("z0", "z1"):
        pair_guards.extend(f"{root}^2-{label}" for label in common_labels)
    pair_program = f"""
ring R={PRIME},(u,z0,z1),(dp(1),dp(2));
option(redSB);
{common_definitions(('z0', 'z1'))}
poly f0=N1*D0+N0*D1;
poly f1=Q0^2*D1^2-Q1^2*D0^2-4*N0*D0*D1^2;
poly guard={'*'.join(f'({value})' for value in pair_guards)};
ideal I=f0,f1,u*guard-1; ideal G=std(I);
print("BEGIN_PAIR"); print(dim(G)); print(size(G));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }} else {{ print("UNIT=0"); }}
print("END_PAIR"); quit;
"""
    pair_process = subprocess.run(
        ["Singular", "--quiet"], input=pair_program, capture_output=True,
        text=True, timeout=60,
    )
    pair_stdout = pair_process.stdout
    pair_valid = pair_process.returncode == 0 and "END_PAIR" in pair_stdout and "?" not in pair_stdout
    pair_unit = pair_valid and "UNIT=1" in pair_stdout
    family = None
    if not pair_unit:
        roots = ("z0", "z1", "z2")
        family_guards = ["z0", "z1", "z2", "D0", "D1", "D2"]
        for left in range(3):
            for right in range(left + 1, 3):
                family_guards.append(f"z{left}^2-z{right}^2")
        for root in roots:
            family_guards.extend(f"{root}^2-{label}" for label in common_labels)
        family_program = f"""
ring R={PRIME},(u,z0,z1,z2),(dp(1),dp(3));
option(redSB);
{common_definitions(roots)}
poly cross=Q1*D0-Q0*D1;
poly f0=N1*D0+N0*D1;
poly f1=Q0^2*D1^2-Q1^2*D0^2-4*N0*D0*D1^2;
poly f2=2*N2*D0*D1-{point['b']}*D2*cross;
poly f3=-2*Q2*D0*D1-2*{point['b']}*D0*D1*D2-D2*cross;
poly guard={'*'.join(f'({value})' for value in family_guards)};
ideal I=f0,f1,f2,f3,u*guard-1; ideal G=std(I);
print("BEGIN_FAMILY"); print(dim(G)); print(size(G));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }} else {{ print("UNIT=0"); }}
print("END_FAMILY"); quit;
"""
        family_process = subprocess.run(
            ["Singular", "--quiet"], input=family_program,
            capture_output=True, text=True, timeout=75,
        )
        family_stdout = family_process.stdout
        family = {
            "status": "COMPLETE" if (
                family_process.returncode == 0
                and "END_FAMILY" in family_stdout
                and "?" not in family_stdout
            ) else "ERROR",
            "unit": "UNIT=1" in family_stdout,
            "program_sha256": digest(family_program),
            "stdout": family_stdout[-20000:],
            "stderr": family_process.stderr[-4000:],
        }
    return {
        "status": "COMPLETE" if pair_valid else "ERROR",
        "point": point,
        "coefficients": coefficients,
        "common_labels": list(common_labels),
        "pair": {
            "status": "COMPLETE" if pair_valid else "ERROR",
            "unit": pair_unit,
            "program_sha256": digest(pair_program),
            "stdout": pair_stdout[-20000:],
            "stderr": pair_process.stderr[-4000:],
        },
        "family": family,
    }


@app.local_entrypoint()
def main():
    point_bytes = POINTS.read_bytes()
    points = json.loads(point_bytes)["result"]["deployed_points"]
    rows = list(test_point.map(points, order_outputs=True, return_exceptions=True))
    normalized = []
    for point, row in zip(points, rows):
        if isinstance(row, BaseException):
            normalized.append({"point": point, "status": "REMOTE_ERROR", "error": repr(row)})
        else:
            normalized.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell3-exceptional-outside-v1",
        "scope": (
            "Exact necessary DE+/DE- and, if needed, DE+/DE-/BE tests at the "
            "two deployed cell-3 exceptional common points; unit excludes only "
            "those points."
        ),
        "source_points_sha256": hashlib.sha256(point_bytes).hexdigest(),
        "rows": normalized,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {
                "point": row.get("point"),
                "status": row.get("status"),
                "pair_unit": row.get("pair", {}).get("unit"),
                "family_unit": (row.get("family") or {}).get("unit"),
            }
            for row in normalized
        ],
    }, sort_keys=True))
