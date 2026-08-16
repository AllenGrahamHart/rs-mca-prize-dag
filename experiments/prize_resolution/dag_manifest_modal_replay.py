#!/usr/bin/env python3
"""Compile and verify a content-pinned DAG manifest archive on Modal."""

from __future__ import annotations

import hashlib
import json
import subprocess
import tarfile
from pathlib import Path


archive_path = next(Path(".").glob("*.tar.gz"))
root = Path("repo")
with tarfile.open(archive_path, "r:gz") as archive:
    archive.extractall(root, filter="data")

commands = [
    ("python3", "tools/compile_dag.py", "--write"),
    ("python3", "tools/verify_dag_manifests.py"),
]
if (root / "tools/verify_prize_dag.py").is_file():
    commands.append(("python3", "tools/verify_prize_dag.py"))
results = []
for command in commands:
    run = subprocess.run(
        command,
        cwd=root,
        capture_output=True,
        text=True,
        timeout=240,
    )
    results.append({
        "command": " ".join(command),
        "exit": run.returncode,
        "stdout": run.stdout.strip(),
        "stderr": run.stderr.strip(),
    })
    if run.returncode != 0:
        print(json.dumps(results, indent=2, sort_keys=True))
        raise SystemExit(run.returncode)

dag_bytes = (root / "dag.json").read_bytes()
dag = json.loads(dag_bytes)
print(json.dumps({
    "dag_sha256": hashlib.sha256(dag_bytes).hexdigest(),
    "nodes": len(dag["nodes"]),
    "edges": len(dag["edges"]),
    "bytes": len(dag_bytes),
    "commands": results,
}, indent=2, sort_keys=True))
