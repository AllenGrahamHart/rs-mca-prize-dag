#!/usr/bin/env python3
"""Find small exact generating subsets of the cell-9 guarded lex ideal."""

import hashlib
import itertools
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
SOURCE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_sign_structure_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_lex_subset_scout_result.json"
)
REMOTE_SOURCE = "/root/cell9_compact_pivot.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell9-lex-subset-scout")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(SOURCE, REMOTE_SOURCE)
)


def source_basis(payload, epsilon):
    rows = [
        row for row in payload["rows"]
        if row["cell"] == 9 and row["epsilon"] == list(epsilon)
        and row["chart"] == 1 and row["status"] == "COMPLETE"
    ]
    if not rows:
        raise RuntimeError(f"missing completed cell-9 chart-1 row for {epsilon}")
    bases = {
        tuple(item["expression"] for item in row["lex_basis"])
        for row in rows
    }
    if len(bases) != 1:
        raise RuntimeError("chart-1 pivots do not have one common lex basis")
    basis = next(iter(bases))
    if len(basis) != 7 or any(value is None for value in basis):
        raise RuntimeError("unexpected cell-9 lex basis")
    return basis


@app.function(image=image, cpu=1.0, memory=2048, timeout=180, max_containers=8)
def test_subset(case):
    epsilon, indices = case
    payload = json.loads(Path(REMOTE_SOURCE).read_text())
    basis = source_basis(payload, epsilon)
    definitions = "\n".join(
        f"poly k{index}={value};" for index, value in enumerate(basis)
    )
    selected = ",".join(f"k{index}" for index in indices)
    program = f"""
ring L={PRIME},(c,b,t,r),lp;
option(redSB);
{definitions}
ideal K={','.join(f'k{index}' for index in range(len(basis)))};
K=std(K);
ideal Q={selected}; Q=std(Q);
print("BEGIN");
print("QSIZE="+string(size(Q)));
for (int row=1; row<=size(K); row++) {{
  print("R="+string(row-1)+":"+string(reduce(K[row],Q)));
}}
print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=160,
        )
    except subprocess.TimeoutExpired:
        return {
            "epsilon": list(epsilon), "indices": list(indices),
            "status": "TIMEOUT",
        }
    stdout = process.stdout
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
    remainders = []
    for match in re.finditer(r"(?:^|\n)R=(\d+):(.*?)(?=\nR=|\nEND)", stdout,
                             re.DOTALL):
        remainders.append({
            "index": int(match.group(1)),
            "expression": "".join(match.group(2).split()),
        })
    qsize = re.search(r"(?:^|\n)QSIZE=(\d+)", stdout)
    exact = (
        len(remainders) == len(basis)
        and all(row["expression"] == "0" for row in remainders)
    )
    return {
        "epsilon": list(epsilon),
        "indices": list(indices),
        "status": "COMPLETE" if valid else "ERROR",
        "exact": exact,
        "quotient_basis_size": int(qsize.group(1)) if qsize else None,
        "remainders": remainders,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stderr": process.stderr[-1000:],
    }


@app.local_entrypoint()
def main():
    payload = json.loads(SOURCE.read_text())
    signs = tuple(itertools.product((-1, 1), repeat=2))
    subsets = tuple(
        (0, 1, *tail)
        for size in range(1, 5)
        for tail in itertools.combinations(range(2, 7), size)
    )
    cases = tuple(itertools.product(signs, subsets))
    rows = list(test_subset.map(cases, order_outputs=False))
    rows.sort(key=lambda row: (
        row["epsilon"], len(row["indices"]), row["indices"]
    ))
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell9-lex-subset-scout-v1",
        "field": PRIME,
        "scope": (
            "Exact unsaturated generating-subset scout inside the already "
            "guard-saturated cell-9 chart-1 lex ideal; no localization, outside, "
            "cell, route, K3, or Prize claim."
        ),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "basis_sha256": {
            str(epsilon): hashlib.sha256(
                "\n".join(source_basis(payload, epsilon)).encode()
            ).hexdigest()
            for epsilon in signs
        },
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "tested": len(rows),
        "statuses": {
            status: sum(row["status"] == status for row in rows)
            for status in sorted({row["status"] for row in rows})
        },
        "exact": [
            [row["epsilon"], row["indices"]]
            for row in rows if row.get("exact")
        ],
    }, sort_keys=True))
