#!/usr/bin/env python3
"""Run the affine Burnside orbit verifier on one small Modal container."""

from __future__ import annotations

from pathlib import Path
import subprocess

import modal


ROOT = Path(__file__).resolve().parents[2]
VERIFIER = ROOT / "experiments/prize_resolution/e1_profile_36_affine_burnside_orbits.py"

app = modal.App("e1-profile-36-affine-burnside-orbits")
image = modal.Image.debian_slim().add_local_file(
    str(VERIFIER), "/repo/verifier.py", copy=True
)


@app.function(image=image, cpu=1.0, memory=128, timeout=60, max_containers=1)
def verify() -> str:
    result = subprocess.run(
        ["python3", "/repo/verifier.py"],
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
