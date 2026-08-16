#!/usr/bin/env python3
"""Replay the K72 theorem packets from a content-pinned Modal archive."""

from __future__ import annotations

import json
import subprocess
import tarfile
from pathlib import Path


archive_path = next(Path(".").glob("*.tar.gz"))
root = Path("repo")
with tarfile.open(archive_path, "r:gz") as archive:
    archive.extractall(root, filter="data")

scripts = (
    "background/nodes/rate_half_mca_sparse_circuit_completion_stratified_fixed_union_charge/verify.py",
    "background/nodes/rate_half_mca_sparse_circuit_completion_stratified_fixed_union_charge/verify_audit.py",
    "background/nodes/rate_half_mca_sparse_circuit_k72_nested_carrier_flag_router/verify.py",
    "background/nodes/rate_half_mca_sparse_circuit_k72_nested_carrier_flag_router/verify_audit.py",
    "background/nodes/rate_half_mca_rank_five_flat_circuit_coupling/verify.py",
    "background/nodes/rate_half_mca_rank_five_flat_circuit_coupling/verify_audit.py",
    "background/nodes/rate_half_mca_rank11_k72_carrier_flag_split_section_census/verify.py",
    "background/nodes/rate_half_mca_rank11_k72_carrier_flag_split_section_census/verify_audit.py",
)
results = {}
for script in scripts:
    run = subprocess.run(
        ["python3", script],
        cwd=root,
        capture_output=True,
        text=True,
        timeout=240,
    )
    results[script] = {
        "exit": run.returncode,
        "stdout": run.stdout.strip(),
        "stderr": run.stderr.strip(),
    }
    if run.returncode != 0:
        print(json.dumps(results, indent=2, sort_keys=True))
        raise SystemExit(run.returncode)

print(json.dumps(results, indent=2, sort_keys=True))
