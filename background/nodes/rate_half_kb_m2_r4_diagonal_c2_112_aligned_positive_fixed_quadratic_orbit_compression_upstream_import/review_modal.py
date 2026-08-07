#!/usr/bin/env python3
"""Independent sharded review of the PR #1149 quadratic orbit compiler."""

from __future__ import annotations

import json
from pathlib import Path

import modal


APP_NAME = "rs-mca-k3-pr1149-fixed-orbit-review"
UPSTREAM = "https://github.com/przchojecki/rs-mca.git"
COMMIT = "55ac3e07477bd7a768190a3e755f22b0d44354b0"
SCRIPT = (
    "/repo/experimental/scripts/"
    "compile_kb_mca_v4_m2_aligned_positive_fixed_frontier_v1.sage"
)
CERTIFICATE = (
    "/repo/experimental/data/certificates/"
    "kb-mca-v4-m2-aligned-positive-fixed-frontier-v1/"
    "kb_mca_v4_m2_aligned_positive_fixed_frontier_v1.json"
)
OUTPUT = Path(__file__).resolve().parent / "modal_review_output.json"
CELLS = tuple(
    f"F{assignment:02d}-R{target}"
    for assignment in range(4, 8)
    for target in ("02", "11", "20")
)

app = modal.App(APP_NAME)
image = (
    modal.Image.from_registry("sagemath/sagemath:10.9")
    .apt_install("git", "python3", "python-is-python3")
    .run_commands(
        "git init /repo",
        f"git -C /repo remote add origin {UPSTREAM}",
        "git -C /repo fetch --depth=1 origin "
        "pull/1149/head:refs/remotes/origin/pr1149",
        "git -C /repo checkout --detach refs/remotes/origin/pr1149",
    )
)


@app.function(
    image=image,
    cpu=1,
    memory=8192,
    timeout=660,
    max_containers=12,
)
def review_cell(cell: str) -> dict[str, object]:
    import hashlib
    import os
    import resource
    import subprocess
    import time

    environment = dict(os.environ)
    environment["HOME"] = "/tmp/sage-home"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    os.makedirs(environment["HOME"], exist_ok=True)
    began = time.monotonic()
    command = [
        "sage",
        SCRIPT,
        "--cell",
        cell,
        "--quadratic-compress",
        "0",
        "1",
        "--check",
        "--summary",
    ]
    try:
        completed = subprocess.run(
            command,
            cwd="/repo",
            env=environment,
            capture_output=True,
            text=True,
            timeout=600,
            check=False,
        )
        stdout = completed.stdout
        stderr = completed.stderr
        status = "FAIL"
        detail = "nonzero return code"
        summary = None
        if completed.returncode == 0:
            lines = [line for line in stdout.splitlines() if line.startswith("{")]
            if len(lines) == 1:
                summary = json.loads(lines[0])
                certificate = json.loads(Path(CERTIFICATE).read_text())
                groups = certificate["quadratic_route"]["literal_orbit_groups"]
                group = next(group for group in groups if cell in group)
                expected = certificate["quadratic_route"]["group_fingerprints"][
                    "|".join(group)
                ]
                resultant = summary["resultant_metric"]
                observed_resultant = [
                    resultant["degree"],
                    resultant["terms"],
                    resultant["sha256"],
                ]
                names = ("AF_minus_CD", "AE_minus_BD", "BF_minus_CE")
                observed_cores = [
                    summary["blocks"][name]["factor_metrics"][-1]["metric"][
                        "sha256"
                    ]
                    for name in names
                ]
                if (
                    summary["cell_id"] == cell
                    and summary["terminal"]
                    == "EXACT_QUADRATIC_RESULTANT_COMPRESSION_NECESSARY_ONLY"
                    and observed_resultant == expected["resultant"]
                    and observed_cores == expected["cores_U_V_Z"]
                ):
                    status = "PASS"
                    detail = "exact certificate fingerprints"
                else:
                    detail = "fingerprint mismatch"
            else:
                detail = f"JSON record count {len(lines)}"
        return {
            "cell": cell,
            "status": status,
            "detail": detail,
            "returncode": completed.returncode,
            "seconds": round(time.monotonic() - began, 6),
            "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            "summary": summary,
            "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
            "stdout_tail": stdout[-2000:],
            "stderr_tail": stderr[-2000:],
        }
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout or ""
        stderr = error.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode(errors="replace")
        return {
            "cell": cell,
            "status": "TIMEOUT",
            "detail": "600-second subprocess cap",
            "returncode": None,
            "seconds": round(time.monotonic() - began, 6),
            "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            "summary": None,
            "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
            "stdout_tail": stdout[-2000:],
            "stderr_tail": stderr[-2000:],
        }


@app.local_entrypoint()
def main() -> None:
    rows = list(review_cell.map(CELLS, return_exceptions=True))
    normalized = []
    for cell, row in zip(CELLS, rows):
        if isinstance(row, BaseException):
            normalized.append(
                {"cell": cell, "status": "REMOTE_ERROR", "error": repr(row)}
            )
        else:
            normalized.append(row)
    output = {
        "schema": "kb-c2-112-pr1149-fixed-orbit-modal-review-v1",
        "app": APP_NAME,
        "upstream_commit": COMMIT,
        "sage": "official SageMath 10.9",
        "case_count": len(CELLS),
        "counts": {
            status: sum(row["status"] == status for row in normalized)
            for status in ("PASS", "FAIL", "TIMEOUT", "REMOTE_ERROR")
        },
        "results": normalized,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output["counts"], sort_keys=True))
    print(f"wrote {OUTPUT}")
