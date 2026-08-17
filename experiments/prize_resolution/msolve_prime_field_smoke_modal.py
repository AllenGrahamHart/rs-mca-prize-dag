#!/usr/bin/env python3
"""Smoke-test the Modal msolve package and its unit-ideal output format."""

import json
from pathlib import Path
import subprocess
import tempfile

import modal


PRIME = 2130706433

app = modal.App("rs-mca-msolve-prime-field-smoke")
image = (
    modal.Image.from_registry("debian:trixie-slim", add_python="3.12")
    .apt_install("msolve")
)


@app.function(image=image, cpu=1.0, memory=512, timeout=60)
def smoke():
    version = subprocess.run(
        ["msolve", "-V"], capture_output=True, text=True, timeout=10
    )
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        source = root / "unit.ms"
        output = root / "unit.out"
        source.write_text(f"x\n{PRIME}\nx,\nx-1\n")
        process = subprocess.run(
            ["msolve", "-t", "1", "-g", "2", "-f", str(source),
             "-o", str(output)],
            capture_output=True, text=True, timeout=30,
        )
        return {
            "version_returncode": version.returncode,
            "version_stdout": version.stdout,
            "version_stderr": version.stderr,
            "returncode": process.returncode,
            "stdout": process.stdout,
            "stderr": process.stderr,
            "output": output.read_text() if output.exists() else "",
        }


@app.local_entrypoint()
def main():
    result = smoke.remote()
    print(json.dumps(result, sort_keys=True))
