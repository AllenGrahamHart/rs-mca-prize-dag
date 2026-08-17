#!/usr/bin/env python3
"""Extract a shipped repository snapshot and run named verifier scripts."""

from __future__ import annotations

import json
import subprocess
import sys
import tarfile
from pathlib import Path


archive = next(Path(".").glob("*.tar.gz"))
root = Path("repo")
with tarfile.open(archive, "r:gz") as handle:
    handle.extractall(root, filter="data")

rows = []
for relative in sys.argv[1:]:
    result = subprocess.run(
        ["python3", relative],
        cwd=root,
        capture_output=True,
        text=True,
        timeout=240,
    )
    rows.append({
        "script": relative,
        "exit": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    })
    if result.returncode:
        print(json.dumps(rows, indent=2))
        raise SystemExit(result.returncode)

print(json.dumps(rows, indent=2))
