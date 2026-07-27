#!/usr/bin/env python3
"""Run the exact Z/32 nested-set route probe for E33 profile (4,5,1)."""

from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
REMOTE_SOURCE = "/root/e33_profile451_nested_probe.cpp"
REMOTE_BINARY = "/root/e33_profile451_nested_probe"

app = modal.App("e1-n256-e33-profile451-nested-probe")
image = (
    modal.Image.debian_slim()
    .apt_install("g++")
    .add_local_file(
        HERE / "e33_profile451_nested_probe.cpp", REMOTE_SOURCE, copy=True
    )
    .run_commands(f"g++ -O3 -std=c++17 {REMOTE_SOURCE} -o {REMOTE_BINARY}")
)


@app.function(image=image, cpu=1.0, memory=512, timeout=60)
def run_probe() -> str:
    import subprocess

    completed = subprocess.run(
        [REMOTE_BINARY],
        check=True,
        capture_output=True,
        text=True,
        timeout=55,
    )
    return completed.stdout.strip()


@app.local_entrypoint()
def main() -> None:
    print(run_probe.remote())
