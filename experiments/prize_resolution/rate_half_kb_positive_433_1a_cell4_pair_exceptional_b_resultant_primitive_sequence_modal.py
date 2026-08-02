#!/usr/bin/env python3
"""Sequentially refine the primitive cell-4 exceptional projection."""

import hashlib
import json
from pathlib import Path
import subprocess
import tarfile

import modal


DIRECTORY = Path(__file__).parent
ARCHIVE = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_primitive_sources.tar.gz"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_primitive_sequence_result.json"
REMOTE_ARCHIVE = "/root/primitive_sources.tar.gz"
REMOTE_DIRECTORY = Path("/root/primitives")
PRIME = 2130706433
POINTS = [(s, u) for total in range(5) for s in range(total+1)
          for u in (total-s,)]
BASE_POINTS = [(s, 0) for s in range(5)]
EXTRA_POINTS = [point for point in POINTS if point[1] != 0]

app = modal.App("rs-mca-positive-433-1a-cell4-exceptional-b-primitive-sequence")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(ARCHIVE, REMOTE_ARCHIVE)
)


def filename(point):
    return (
        "rate_half_kb_positive_433_1a_cell4_pair_exceptional_"
        f"b_resultant_primitive_{point[0]}_{point[1]}.txt"
    )


@app.function(image=image, cpu=4.0, memory=16384, timeout=330)
def run_sequence():
    REMOTE_DIRECTORY.mkdir(exist_ok=True)
    with tarfile.open(REMOTE_ARCHIVE, "r:gz") as archive:
        archive.extractall(REMOTE_DIRECTORY, filter="data")
    polynomials = {
        point: (REMOTE_DIRECTORY / filename(point)).read_text().strip()
        for point in POINTS
    }
    definitions = "\n".join(
        f"poly r_{s}_{u}={polynomials[(s, u)]};"
        for s, u in POINTS
    )
    base_names = ",".join(f"r_{s}_{u}" for s, u in BASE_POINTS)
    stages = [
        f"ideal I0={base_names};\nideal G0=slimgb(I0);\n"
        "print(\"BEGIN_STAGE_0\"); print(dim(G0)); print(size(G0)); "
        "if (dim(G0)==0) { print(vdim(G0)); } print(\"END_STAGE_0\");"
    ]
    for index, (s, u) in enumerate(EXTRA_POINTS, start=1):
        previous = f"G{index-1}"
        current = f"G{index}"
        stages.append(
            f"ideal I{index}={previous},r_{s}_{u};\n"
            f"ideal {current}=slimgb(I{index});\n"
            f"print(\"BEGIN_STAGE_{index}_{s}_{u}\"); "
            f"print(dim({current})); print(size({current})); "
            f"if (dim({current})==0) {{ print(vdim({current})); }} "
            f"if ((size({current})==1) && ({current}[1]==1)) "
            "{ print(\"UNIT=1\"); } else { print(\"UNIT=0\"); } "
            f"print(\"END_STAGE_{index}_{s}_{u}\");"
        )
    program = f"""
ring R={PRIME},(w0,t),(dp(2));
option(redSB);
{definitions}
print("BEGIN_INPUT"); print(deg(r_0_0)); print(size(r_0_0));
print(deg(r_0_1)); print(size(r_0_1)); print("END_INPUT");
{"\n".join(stages)}
print("END_SEQUENCE");
quit;
"""
    header = {
        "field": PRIME,
        "points": [list(point) for point in POINTS],
        "base_points": [list(point) for point in BASE_POINTS],
        "extra_points": [list(point) for point in EXTRA_POINTS],
        "source_sha256": {
            f"{s}_{u}": hashlib.sha256(polynomials[(s, u)].encode()).hexdigest()
            for s, u in POINTS
        },
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
    }
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=300,
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""
        stdout = decoded(error.stdout)
        return {
            **header, "status": "TIMEOUT",
            "completed_stages": stdout.count("END_STAGE_"),
            "partial_stdout": stdout[-50000:],
            "partial_stderr": decoded(error.stderr)[-4000:],
        }
    stdout = process.stdout
    complete = (
        process.returncode == 0 and "END_SEQUENCE" in stdout and "?" not in stdout
    )
    return {
        **header, "status": "COMPLETE" if complete else "ERROR",
        "completed_stages": stdout.count("END_STAGE_"),
        "unit": "UNIT=1" in stdout,
        "stdout": stdout[-50000:], "stderr": process.stderr[-4000:],
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell4-pair-exceptional-b-resultant-primitive-sequence-v1",
        "scope": (
            "Exact sequential ideal refinement by all fifteen primitive "
            "unisolvent resultant evaluations. Unit excludes every residual "
            "projection outside the common gcd; nonunit or timeout records "
            "only completed stages and makes no common-root, colored, orbit, "
            "or Prize claim."
        ),
        "source_archive_sha256": hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),
        "result": run_sequence.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    result = output["result"]
    print(json.dumps({
        "result": str(RESULT), "status": result.get("status"),
        "completed_stages": result.get("completed_stages"),
        "unit": result.get("unit"),
        "stdout": result.get("stdout", result.get("partial_stdout", ""))[-8000:],
    }, sort_keys=True))
