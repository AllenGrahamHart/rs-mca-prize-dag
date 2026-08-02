#!/usr/bin/env python3
"""Decide every deployed cell-14 linear exceptional scale in the common ideal."""

import hashlib
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
SCOUT = DIRECTORY / "rate_half_kb_positive_433_1a_remaining_lex_scout_result.json"
FACTORS = DIRECTORY / "rate_half_kb_positive_433_1a_cell14_exceptional_scale_factor_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell14_exceptional_common_charts_result.json"
REMOTE_SCOUT = "/root/remaining_lex_scout.json"
REMOTE_FACTORS = "/root/cell14_exceptional_scales.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell14-exceptional-common-charts")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(SCOUT, REMOTE_SCOUT)
    .add_local_file(FACTORS, REMOTE_FACTORS)
)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


@app.function(image=image, cpu=1.0, memory=2048, timeout=120, max_containers=5)
def decide_chart(t_value):
    scout = json.loads(Path(REMOTE_SCOUT).read_text())
    row = next(
        item for item in scout["rows"]
        if item.get("cell") == 14
        and item.get("order") == ["c", "r", "b", "t"]
    )
    basis = re.findall(r"^GP\[\d+\]=(.*)$", row["stdout"], re.MULTILINE)
    if len(basis) != 8:
        raise RuntimeError("unexpected cell-14 lex basis")
    program = f"""
ring R={PRIME},(u,c,r,b,t),(dp(1),dp(4));
option(redSB);
ideal L={','.join(basis)};
poly l0=1; poly l1=t^2; poly l2=-1; poly l3=r^2; poly l4=-r^2;
poly guard=(l0-l1)*(l0-l2)*(l0-l3)*(l0-l4)
 *(l1-l2)*(l1-l3)*(l1-l4)*(l2-l3)*(l2-l4)*(l3-l4)
 *r*t*b*c*(b-1)*(b+1)*(c-1)*(c+1)*(b-c)*(b+c);
ideal I=L,t-{t_value},u*guard-1;
ideal G=std(I);
print("BEGIN_CHART"); print(dim(G)); print(size(G));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); if (size(G)<80) {{ G; }} }}
print("END_CHART");
quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=95,
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""

        return {
            "t": t_value,
            "status": "TIMEOUT",
            "program_sha256": digest(program),
            "partial_stdout": decoded(error.stdout)[-20000:],
            "partial_stderr": decoded(error.stderr)[-4000:],
        }
    stdout = process.stdout
    valid = process.returncode == 0 and "END_CHART" in stdout and "?" not in stdout
    return {
        "t": t_value,
        "status": "COMPLETE" if valid else "ERROR",
        "unit": "UNIT=1" in stdout,
        "guard_trivial": (
            t_value == 0 or pow(t_value, 2, PRIME) in (1, PRIME - 1)
        ),
        "program_sha256": digest(program),
        "stdout": stdout[-20000:],
        "stderr": process.stderr[-4000:],
    }


@app.local_entrypoint()
def main():
    factor_bytes = FACTORS.read_bytes()
    roots = [
        row["t"]
        for row in json.loads(factor_bytes)["result"]["linear_roots"]
    ]
    raw_rows = list(decide_chart.map(
        roots, order_outputs=True, return_exceptions=True,
    ))
    rows = []
    for root, row in zip(roots, raw_rows):
        if isinstance(row, BaseException):
            rows.append({"t": root, "status": "REMOTE_ERROR", "error": repr(row)})
        else:
            rows.append(row)
    rows.sort(key=lambda row: row["t"])
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell14-exceptional-common-charts-v1",
        "scope": (
            "Exact original-common-ideal decisions at every deployed linear "
            "root of the cell-14 chart scales; no outside, orbit, or Prize claim."
        ),
        "source_factor_sha256": hashlib.sha256(factor_bytes).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {
                "t": row.get("t"),
                "status": row.get("status"),
                "unit": row.get("unit"),
                "guard_trivial": row.get("guard_trivial"),
            }
            for row in rows
        ],
    }, sort_keys=True))
