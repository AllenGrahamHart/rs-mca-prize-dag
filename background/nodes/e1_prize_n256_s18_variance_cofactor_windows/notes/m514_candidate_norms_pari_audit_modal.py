#!/usr/bin/env python3
"""Independent PARI replay of all 184 m=514 candidate resultants."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
CENSUS = HERE / "m514_low_variance_census_result.json"
PRIMARY = HERE / "m514_candidate_norms_result.json"
OUTPUT = HERE / "m514_candidate_norms_pari_audit_result.json"

image = (
    modal.Image.debian_slim()
    .apt_install("pari-gp")
    .add_local_file(str(CENSUS), "/root/census.json", copy=True)
    .add_local_file(str(PRIMARY), "/root/primary.json", copy=True)
)
app = modal.App("e1-prize-m514-candidate-norms-pari-audit")


@app.function(image=image, cpu=1.0, memory=512, timeout=60)
def audit() -> dict[str, object]:
    census = json.loads(Path("/root/census.json").read_text())
    primary = json.loads(Path("/root/primary.json").read_text())
    witnesses = [
        witness for witness in census["witnesses"]
        if int(witness["root_exponent"]) >= 0
    ]
    commands = []
    for witness in witnesses:
        terms = []
        for position, coefficient in zip(
            witness["positions"], witness["coefficients"]
        ):
            terms.append(f"({int(coefficient)})*x^{int(position)}")
        polynomial = "+".join(terms)
        commands.append(f"print(abs(polresultant(x^128+1,{polynomial})))")
    completed = subprocess.run(
        ["gp", "-fq"],
        input="\n".join(commands) + "\nquit\n",
        capture_output=True,
        check=True,
        text=True,
        timeout=52,
    )
    pari_norms = [int(line) for line in completed.stdout.splitlines() if line.strip()]
    primary_norms = [int(row["norm"]) for row in primary["rows"]]
    assert len(pari_norms) == len(primary_norms) == 184
    assert pari_norms == primary_norms
    lower, upper = map(int, primary["prize_interval"])
    candidates = [norm // 514 for norm in pari_norms]
    return {
        "schema": "e1-prize-m514-candidate-norms-pari-audit-v1",
        "complete": True,
        "row_count": len(pari_norms),
        "distinct_norm_count": len(set(pari_norms)),
        "primary_match": True,
        "minimum_candidate": min(candidates),
        "maximum_candidate": max(candidates),
        "interval_row_count": sum(lower <= value <= upper for value in candidates),
    }


@app.local_entrypoint()
def main() -> None:
    result = audit.remote()
    result["census_sha256"] = hashlib.sha256(CENSUS.read_bytes()).hexdigest()
    result["primary_sha256"] = hashlib.sha256(PRIMARY.read_bytes()).hexdigest()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "M514_CANDIDATE_NORMS_PARI_AUDIT "
        f"complete={result['complete']} rows={result['row_count']} "
        f"match={result['primary_match']} interval={result['interval_row_count']}"
    )
