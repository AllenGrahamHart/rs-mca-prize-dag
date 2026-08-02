#!/usr/bin/env python3
"""Lexicographically triangularize the 470-point primitive residual."""

import hashlib
import json
from pathlib import Path
import subprocess
import tarfile

import modal


DIRECTORY = Path(__file__).parent
ARCHIVE = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_primitive_sources.tar.gz"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_primitive_lex_result.json"
TPOLY = DIRECTORY / "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_primitive_tpoly.txt"
REMOTE_ARCHIVE = "/root/primitive_sources.tar.gz"
REMOTE_DIRECTORY = Path("/root/primitives")
PRIME = 2130706433
POINTS = [(s, u) for total in range(5) for s in range(total+1)
          for u in (total-s,)]

app = modal.App("rs-mca-positive-433-1a-cell4-exceptional-b-primitive-lex")
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
def triangularize():
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
    names = ",".join(f"r_{s}_{u}" for s, u in POINTS)
    program = f"""
ring R={PRIME},(w0,t),(dp(2));
option(redSB);
{definitions}
ideal I={names};
ideal G=slimgb(I);
print("BEGIN_DP"); print(dim(G)); print(size(G)); print(vdim(G)); print("END_DP");
ring L={PRIME},(w0,t),lp;
option(redSB);
ideal GL=fglm(R,G);
print("BEGIN_LEX"); print(dim(GL)); print(size(GL)); print(vdim(GL));
poly tpoly=GL[1];
print(deg(tpoly)); print(size(tpoly)); print("END_LEX");
print("BEGIN_TPOLY"); print(tpoly); print("END_TPOLY");
quit;
"""
    header = {
        "field": PRIME,
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
            "dp_emitted": "END_DP" in stdout,
            "partial_stdout": stdout[-50000:],
            "partial_stderr": decoded(error.stderr)[-4000:],
        }
    stdout = process.stdout
    complete = (
        process.returncode == 0 and "END_TPOLY" in stdout and "?" not in stdout
    )
    output = {
        **header, "status": "COMPLETE" if complete else "ERROR",
        "stdout": stdout[-50000:], "stderr": process.stderr[-4000:],
    }
    if complete:
        output["t_polynomial"] = stdout.split(
            "BEGIN_TPOLY\n", 1
        )[1].split("\nEND_TPOLY", 1)[0].strip()
    return output


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell4-pair-exceptional-b-resultant-primitive-lex-v1",
        "scope": (
            "Exact FGLM triangularization of the fifteen-row primitive "
            "residual. A complete t eliminant supports a separate deployed-"
            "root census; timeout or error makes no point, common-root, "
            "colored, orbit, or Prize claim."
        ),
        "source_archive_sha256": hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),
        "result": triangularize.remote(),
    }
    result = output["result"]
    polynomial = result.pop("t_polynomial", None)
    if polynomial is not None:
        TPOLY.write_text(polynomial+"\n")
        result["t_polynomial_file"] = TPOLY.name
        result["t_polynomial_sha256"] = hashlib.sha256(
            polynomial.encode()
        ).hexdigest()
        result["t_polynomial_file_sha256"] = hashlib.sha256(
            TPOLY.read_bytes()
        ).hexdigest()
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT), "status": result.get("status"),
        "t_polynomial_file": result.get("t_polynomial_file"),
        "stdout": result.get("stdout", result.get("partial_stdout", ""))[-4000:],
    }, sort_keys=True))
