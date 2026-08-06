#!/usr/bin/env python3
"""Run one bounded, checkpointed CADO-NFS attempt on WCL tail 191."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


NORM_TEXT = (
    "648504938724625892617537595827566622528651020454874372151735040370"
    "465231483079169"
)
NORM = int(NORM_TEXT)
CADO_COMMIT = "9bb8fc0799bbaaf0b47a1edf573ecf5e0cf8e46a"
CADO_IMAGE = (
    "registry.gitlab.inria.fr/cado-nfs/cado-nfs/factoring-full@"
    "sha256:d89bc19b6a1a9dd00b8c95cd97d60faca73ecbfc3ea71b5e20ec0403b1b3fc10"
)
WORKDIR = Path("/work/tail191-cado-portable-v1")
LOG_FILE = WORKDIR / "cado.log"
REMOTE_RESULT_FILE = WORKDIR / "result.json"
OUTPUT = Path(__file__).with_name("tail191_cado_portable_result.json")
INNER_SECONDS = 1_200

app = modal.App("rs-mca-wcl15-tail191-cado-nfs")
image = modal.Image.from_registry(CADO_IMAGE, add_python="3.11")
volume = modal.Volume.from_name("rs-mca-wcl-tail191-cado-v1", create_if_missing=True)


def extract_proper_divisors(root: Path) -> list[str]:
    import re

    candidates = set()
    for path in root.rglob("*"):
        try:
            if not path.is_file() or path.stat().st_size > 2_000_000:
                continue
            text = path.read_text(errors="ignore")
        except OSError:
            continue
        for token in re.findall(r"(?<!\d)\d{10,}(?!\d)", text):
            value = int(token)
            if 1 < value < NORM and NORM % value == 0:
                candidates.add(value)
                candidates.add(NORM // value)
    return [str(value) for value in sorted(candidates)]


@app.function(
    image=image,
    cpu=16,
    memory=32768,
    timeout=1500,
    max_containers=1,
    volumes={"/work": volume},
)
def run_cado() -> dict[str, object]:
    import os
    import shutil
    import signal
    import subprocess
    import time

    started = time.monotonic()
    volume.reload()
    WORKDIR.mkdir(parents=True, exist_ok=True)
    cado_executable = shutil.which("cado-nfs.py")
    if cado_executable is None:
        raise RuntimeError(("cado-nfs.py absent from official image PATH", os.environ["PATH"]))
    command = [
        cado_executable,
        NORM_TEXT,
        "-t",
        "16",
        "--workdir",
        str(WORKDIR),
    ]
    timed_out = False
    forced_kill = False
    with LOG_FILE.open("a") as log:
        log.write(
            f"\nWRAPPER_START commit={CADO_COMMIT} epoch={time.time()} "
            f"command={json.dumps(command)}\n"
        )
        log.flush()
        process = subprocess.Popen(
            command,
            stdout=log,
            stderr=subprocess.STDOUT,
            text=True,
            start_new_session=True,
        )
        try:
            return_code = process.wait(timeout=INNER_SECONDS)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(process.pid, signal.SIGINT)
            try:
                return_code = process.wait(timeout=60)
            except subprocess.TimeoutExpired:
                forced_kill = True
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    return_code = process.wait(timeout=20)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    return_code = process.wait(timeout=10)
        log.write(
            f"WRAPPER_END epoch={time.time()} return_code={return_code} "
            f"timed_out={timed_out} forced_kill={forced_kill}\n"
        )
        log.flush()

    proper_divisors = extract_proper_divisors(WORKDIR)
    for divisor_text in proper_divisors:
        divisor = int(divisor_text)
        if NORM % divisor:
            raise AssertionError(("nondivisor output", divisor_text))
    files = []
    total_bytes = 0
    for path in WORKDIR.rglob("*"):
        if not path.is_file():
            continue
        size = path.stat().st_size
        total_bytes += size
        files.append({"path": str(path.relative_to(WORKDIR)), "bytes": size})
    files.sort(key=lambda row: row["path"])
    inventory_hash = hashlib.sha256()
    for row in files:
        inventory_hash.update(f"{row['path']}:{row['bytes']}\n".encode())
    parameter_snapshots = [
        row["path"] for row in files if ".parameters_snapshot." in row["path"]
    ]
    log_tail = LOG_FILE.read_text(errors="replace").splitlines()[-120:]
    split_found = bool(proper_divisors)
    result = {
        "schema": "wcl15-tail191-cado-v1",
        "status": "DIVISOR_FOUND" if split_found else "PARTIAL",
        "norm": NORM_TEXT,
        "norm_bits": NORM.bit_length(),
        "cado_commit": CADO_COMMIT,
        "cado_image": CADO_IMAGE,
        "command": command,
        "inner_seconds_cap": INNER_SECONDS,
        "return_code": return_code,
        "timed_out": timed_out,
        "forced_kill": forced_kill,
        "proper_divisors": proper_divisors,
        "split_found": split_found,
        "parameter_snapshots": parameter_snapshots,
        "work_files": len(files),
        "work_bytes": total_bytes,
        "file_inventory_digest": inventory_hash.hexdigest(),
        "largest_files": sorted(files, key=lambda row: row["bytes"], reverse=True)[:20],
        "log_tail": log_tail,
        "seconds": round(time.monotonic() - started, 6),
    }
    result["result_digest"] = hashlib.sha256(
        json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    temporary = Path(str(REMOTE_RESULT_FILE) + ".tmp")
    temporary.write_text(json.dumps(result, sort_keys=True) + "\n")
    temporary.replace(REMOTE_RESULT_FILE)
    volume.commit()
    return result


@app.local_entrypoint()
def main() -> None:
    result = run_cado.remote()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "WCL15_TAIL191_CADO "
        + json.dumps(
            {
                key: result[key]
                for key in (
                    "status",
                    "return_code",
                    "timed_out",
                    "forced_kill",
                    "proper_divisors",
                    "split_found",
                    "parameter_snapshots",
                    "work_files",
                    "work_bytes",
                    "seconds",
                    "result_digest",
                )
            },
            sort_keys=True,
        )
    )
