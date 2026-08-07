#!/usr/bin/env python3
"""Exhaust WCL (1,6) on the certified first-64 split-prime panel."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import modal


CPP = Path(__file__).with_name("dli_wcl_ell1_weight6_admissible_mitm.cpp")
PANEL = Path(__file__).with_name("dli_wcl_terminal_weight5_mitm_result.json")
OUTPUT = Path(__file__).with_name("dli_wcl_ell1_weight6_admissible_mitm_result.json")

base = modal.Image.debian_slim().apt_install("g++")
image = (
    base.add_local_file(str(CPP), "/root/search.cpp", copy=True)
    .run_commands("g++ -O3 -std=c++17 /root/search.cpp -o /usr/local/bin/search")
)
app = modal.App("rs-mca-wcl-ell1-weight6-admissible-mitm")


@app.function(image=image, cpu=1, memory=1024, timeout=60, max_containers=64)
def search(p: int) -> dict[str, object]:
    process = subprocess.run(
        ["/usr/local/bin/search", str(p)],
        check=True,
        capture_output=True,
        text=True,
        timeout=55,
    )
    if process.stderr:
        print(process.stderr, end="")
    return json.loads(process.stdout.strip().splitlines()[-1])


@app.local_entrypoint()
def main(single: int = 0) -> None:
    if single:
        print(json.dumps(search.remote(single), sort_keys=True))
        return

    panel = json.loads(PANEL.read_text())
    primes = [int(row["q"]) for row in panel["primes"]]
    result = {
        "schema": "dli-wcl-ell1-weight6-admissible-mitm-panel-v1",
        "status": "IN_PROGRESS",
        "primes": primes,
        "rows": [],
        "worker_errors": [],
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    for prime, row in zip(
        primes,
        search.map(primes, order_outputs=True, return_exceptions=True),
    ):
        if isinstance(row, BaseException):
            result["worker_errors"].append({"p": prime, "error": repr(row)})
        else:
            result["rows"].append(row)
        OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    result["status"] = "COMPLETE" if not result["worker_errors"] else "PARTIAL"
    result["relation_count"] = sum(row["status"] == "FOUND" for row in result["rows"])
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "DLI_WCL_ELL1_WEIGHT6_ADMISSIBLE_MITM "
        f"status={result['status']} rows={len(result['rows'])}/{len(primes)} "
        f"relations={result['relation_count']}"
    )
