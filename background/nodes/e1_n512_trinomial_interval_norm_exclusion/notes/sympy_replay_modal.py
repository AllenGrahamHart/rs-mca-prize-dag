#!/usr/bin/env python3
"""Run the primary verifier on Modal with its repository paths preserved."""

from __future__ import annotations

import pathlib

import modal


REMOTE_ROOT = pathlib.PurePosixPath("/repo")
LOCAL_ROOT = (
    pathlib.Path(__file__).resolve().parents[4]
    if modal.is_local()
    else pathlib.Path(REMOTE_ROOT)
)
FILES = (
    "dag.json",
    "background/nodes/e1_n512_trinomial_interval_norm_exclusion/verify.py",
    "background/nodes/e1_n512_trinomial_interval_norm_exclusion/certificate.json",
    "background/nodes/e1_n512_trinomial_interval_norm_exclusion/source_pin.json",
    "background/nodes/e1_prime_field_l2_norm_collision_radius/statement.md",
    "background/nodes/e1_n512_four_singleton_collision_exclusion/statement.md",
    "critical/nodes/collision_norm_criterion/statement.md",
)

app = modal.App("e1-n512-trinomial-sympy-replay")
image = modal.Image.debian_slim().pip_install("sympy")
for relative_path in FILES:
    image = image.add_local_file(
        str(LOCAL_ROOT / relative_path),
        str(REMOTE_ROOT / relative_path),
    )


@app.function(image=image, cpu=1.0, memory=1024, timeout=60)
def replay() -> dict[str, object]:
    import resource
    import subprocess

    completed = subprocess.run(
        [
            "python3",
            "/repo/background/nodes/e1_n512_trinomial_interval_norm_exclusion/verify.py",
        ],
        capture_output=True,
        text=True,
        timeout=55,
        check=False,
    )
    return {
        "exit": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "peak_mb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss // 1024,
    }


@app.local_entrypoint()
def main() -> None:
    result = replay.remote()
    print(result["stdout"], end="")
    if result["stderr"]:
        print(result["stderr"], end="")
    print(f"E1_N512_SYMPY_MODAL exit={result['exit']} peak_mb={result['peak_mb']}")
    raise SystemExit(result["exit"])
