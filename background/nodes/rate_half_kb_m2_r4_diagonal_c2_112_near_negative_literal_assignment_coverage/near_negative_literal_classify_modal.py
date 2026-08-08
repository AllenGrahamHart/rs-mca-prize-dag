"""Run reduced near-negative literal cells on Modal."""

from __future__ import annotations

import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "near_negative_literal_classify.sage"
app = modal.App("rs-mca-k3-near-negative-literal")
image = (
    modal.Image.from_registry("sagemath/sagemath:10.9")
    .apt_install("python3", "python-is-python3")
    .add_local_file(SOURCE, "/near_negative_literal_classify.sage", copy=True)
)


@app.function(image=image, cpu=2, memory=2048, timeout=360)
def classify(cell: str, saturation_mode: str) -> dict[str, object]:
    import hashlib
    import os
    import resource
    import subprocess
    import time

    environment = dict(os.environ)
    environment["HOME"] = "/tmp/sage-home"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["NEAR_NEGATIVE_CELL"] = cell
    environment["NEAR_NEGATIVE_SATURATION_MODE"] = saturation_mode
    os.makedirs(environment["HOME"], exist_ok=True)
    started = time.monotonic()
    try:
        completed = subprocess.run(
            ["sage", "/near_negative_literal_classify.sage"],
            env=environment,
            capture_output=True,
            text=True,
            timeout=330,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout.decode() if isinstance(error.stdout, bytes) else (error.stdout or "")
        stderr = error.stderr.decode() if isinstance(error.stderr, bytes) else (error.stderr or "")
        return {
            "status": "TIMEOUT",
            "returncode": None,
            "seconds": round(time.monotonic() - started, 6),
            "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            "payload": None,
            "partial_components": [],
            "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
            "stdout_tail": stdout[-20000:],
            "stderr_tail": stderr[-20000:],
        }
    payloads = []
    components = []
    for line in completed.stdout.splitlines():
        if line.startswith("NEAR_NEGATIVE_COMPONENT_JSON "):
            components.append(json.loads(line.split(" ", 1)[1]))
        if line.startswith("NEAR_NEGATIVE_LITERAL_JSON "):
            payloads.append(json.loads(line.split(" ", 1)[1]))
    return {
        "status": "PASS" if completed.returncode == 0 and payloads else "FAIL",
        "returncode": completed.returncode,
        "seconds": round(time.monotonic() - started, 6),
        "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        "payload": payloads[-1] if payloads else None,
        "partial_components": components,
        "stdout_sha256": hashlib.sha256(completed.stdout.encode()).hexdigest(),
        "stdout_tail": completed.stdout[-20000:],
        "stderr_tail": completed.stderr[-20000:],
    }


@app.local_entrypoint()
def main(cell: str = "", assignment: str = "", saturation_mode: str = "rabinowitsch") -> None:
    if saturation_mode not in ("rabinowitsch", "sequential"):
        raise ValueError(saturation_mode)
    assignments = (
        tuple(assignment.split(","))
        if assignment
        else (
            "F00", "F01", "F02", "F03", "F04", "F05",
            "F06", "F07", "M00", "M01", "M02", "M03",
        )
    )
    cells = (
        (cell,)
        if cell
        else tuple(
            f"{name}-{root}"
            for name in assignments
            for root in ("A", "TA", "OB", "OI")
        )
    )
    calls = {name: classify.spawn(name, saturation_mode) for name in cells}
    results = {name: calls[name].get() for name in cells}
    output = {
        "schema": "kb-c2-112-near-negative-literal-modal-v1",
        "saturation_mode": saturation_mode,
        "results": results,
    }
    suffix = cell.lower() if cell else assignment.lower().replace(",", "_") if assignment else "all"
    if saturation_mode == "sequential":
        suffix = f"{suffix}_sequential"
    output_path = HERE / f"near_negative_literal_{suffix}_output.json"
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        name: {
            "status": row["status"],
            "terminal": (row["payload"] or {}).get("terminal"),
            "seconds": row["seconds"],
            "components": len(row["partial_components"]),
        }
        for name, row in results.items()
    }, sort_keys=True))
    print(f"wrote {output_path}")
