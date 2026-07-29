#!/usr/bin/env python3
"""Run the low-cofactor support verifier on a small Modal container."""

from __future__ import annotations

from pathlib import Path
import subprocess

import modal


ROOT = Path(__file__).resolve().parents[2]
VERIFIER = ROOT / "experiments/prize_resolution/e1_profile_36_mu1_mu2_support_decomposition.py"
DAG = ROOT / "dag.json"

app = modal.App("e1-profile-36-mu1-mu2-support-decomposition")
image = (
    modal.Image.debian_slim()
    .add_local_file(str(VERIFIER), "/repo/experiments/prize_resolution/verifier.py", copy=True)
    .add_local_file(str(DAG), "/repo/dag.json", copy=True)
)


@app.function(image=image, cpu=1.0, memory=128, timeout=60, max_containers=1)
def verify() -> str:
    result = subprocess.run(
        ["python3", "/repo/experiments/prize_resolution/verifier.py"],
        text=True,
        capture_output=True,
        timeout=45,
    )
    if result.returncode or result.stderr:
        raise RuntimeError(
            f"returncode={result.returncode}\nstdout={result.stdout}\nstderr={result.stderr}"
        )
    return result.stdout.strip()


@app.local_entrypoint()
def main() -> None:
    print(verify.remote())


if __name__ == "__main__":
    main()
