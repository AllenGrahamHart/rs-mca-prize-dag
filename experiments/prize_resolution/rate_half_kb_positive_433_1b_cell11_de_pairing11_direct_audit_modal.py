#!/usr/bin/env python3
"""Run the independent cell-5 pairing-11 direct replay on Modal."""

import hashlib
import importlib.util
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
AUDITOR = DIRECTORY / "rate_half_kb_positive_433_1b_cell11_common_f_resultant_audit.py"
PRIMARY = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_de_pairing11_"
    "template_adapter_result.json"
)
ROOTS = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_de_pairing11_"
    "frobenius_roots_result.json"
)
TOWER = DIRECTORY / "rate_half_kb_positive_433_1b_cell11_four_basis_tower_result.json"
KERNEL = DIRECTORY / "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_de_pairing11_direct_audit_result.json"
)
REMOTE_AUDITOR = "/root/auditor.py"
REMOTE_PRIMARY = "/root/primary.json"
REMOTE_ROOTS = "/root/roots.json"
REMOTE_TOWER = "/root/tower.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell11-de-pairing11-direct-audit")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(AUDITOR, REMOTE_AUDITOR)
    .add_local_file(PRIMARY, REMOTE_PRIMARY)
    .add_local_file(ROOTS, REMOTE_ROOTS)
    .add_local_file(TOWER, REMOTE_TOWER)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=300)
def audit():
    spec = importlib.util.spec_from_file_location("cell11_auditor", REMOTE_AUDITOR)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    primary = Path(REMOTE_PRIMARY)
    return module.audit_result(
        result=primary,
        root_result=Path(REMOTE_ROOTS),
        primary_paths={"pairing11": primary},
        tower_path=Path(REMOTE_TOWER),
        kernel_path=Path(REMOTE_KERNEL),
        pairing=11,
        xi_values=(0, 2),
        matching=((0, 4), (1, 5), (2, 3)),
    )


@app.local_entrypoint()
def main():
    summary = audit.remote()
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell11-de-pairing11-direct-audit-v1",
        "field": PRIME,
        "method": "independent Frobenius-root and direct finite-row replay",
        "source_sha256": {
            "auditor": hashlib.sha256(AUDITOR.read_bytes()).hexdigest(),
            "primary": hashlib.sha256(PRIMARY.read_bytes()).hexdigest(),
            "roots": hashlib.sha256(ROOTS.read_bytes()).hexdigest(),
            "tower": hashlib.sha256(TOWER.read_bytes()).hexdigest(),
            "kernel": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        },
        "summary": summary,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"result": str(RESULT), "summary": summary}, sort_keys=True))
