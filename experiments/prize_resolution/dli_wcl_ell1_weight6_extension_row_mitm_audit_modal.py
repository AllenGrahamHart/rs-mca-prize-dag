#!/usr/bin/env python3
"""Independently replay four extension-row MITM records on Modal."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import modal


CPP = Path(__file__).with_name("dli_wcl_ell1_weight6_extension_row_mitm_audit.cpp")
PANEL = Path(__file__).with_name("dli_wcl_ell1_weight6_extension_row_mitm_result.json")
OUTPUT = Path(__file__).with_name("dli_wcl_ell1_weight6_extension_row_mitm_audit_result.json")

base = modal.Image.debian_slim().apt_install("g++")
image = (
    base.add_local_file(str(CPP), "/root/audit.cpp", copy=True)
    .run_commands("g++ -O3 -std=c++17 /root/audit.cpp -o /usr/local/bin/audit")
)
app = modal.App("rs-mca-wcl-ell1-weight6-extension-row-mitm-audit")


@app.function(image=image, cpu=1, memory=1024, timeout=60, max_containers=4)
def audit(p: int) -> dict[str, object]:
    process = subprocess.run(
        ["/usr/local/bin/audit", str(p)],
        check=True,
        capture_output=True,
        text=True,
        timeout=55,
    )
    return json.loads(process.stdout.strip().splitlines()[-1])


@app.local_entrypoint()
def main() -> None:
    data = json.loads(PANEL.read_text())
    rows = data["rows"]
    indices = [0, 63, 64, 127]
    primes = [rows[index]["p"] for index in indices]
    result = {
        "schema": "dli-wcl-ell1-weight6-extension-row-mitm-audit-v1",
        "status": "IN_PROGRESS",
        "indices": indices,
        "rows": [],
        "worker_errors": [],
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    for index, p, row in zip(
        indices,
        primes,
        audit.map(primes, order_outputs=True, return_exceptions=True),
    ):
        if isinstance(row, BaseException):
            result["worker_errors"].append({"index": index, "p": p, "error": repr(row)})
        else:
            row["index"] = index
            result["rows"].append(row)
        OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    result["status"] = "COMPLETE" if not result["worker_errors"] else "PARTIAL"
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "DLI_WCL_ELL1_WEIGHT6_EXTENSION_ROW_MITM_AUDIT "
        f"status={result['status']} rows={len(result['rows'])}/{len(indices)}"
    )
