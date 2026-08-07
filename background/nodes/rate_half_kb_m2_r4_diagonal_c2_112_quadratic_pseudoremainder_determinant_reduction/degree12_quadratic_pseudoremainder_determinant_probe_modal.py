#!/usr/bin/env python3
"""Run source quadratic pseudo-remainder determinant probes on Modal."""

from __future__ import annotations

import json
import os
from pathlib import Path

import modal


MODE = os.environ.get("DEGREE12_QUADRATIC_PREM_MODE", "metrics")
APP_NAME = f"rs-mca-k3-degree12-quadratic-prem-determinant-{MODE}"
UPSTREAM = "https://github.com/przchojecki/rs-mca.git"
COMMIT = "55ac3e07477bd7a768190a3e755f22b0d44354b0"
HERE = Path(__file__).resolve().parent
BALANCED = (
    HERE.parent
    / "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_balanced_quadratic_branch_reduction"
)
LIBRARY = BALANCED / "branch_core.sage"
SCRIPT = HERE / "degree12_quadratic_pseudoremainder_determinant_probe.sage"
OUTPUT = HERE / f"modal_degree12_quadratic_prem_determinant_{MODE}_output.json"
if MODE == "metrics":
    CASES = tuple(
        {"cell": "F04-R02", "divisor": divisor, "groebner": False}
        for divisor in ("A0", "B0")
    )
elif MODE == "groebner_b0":
    CASES = (
        {
            "cell": "F04-R02",
            "divisor": "B0",
            "groebner": True,
            "projective_field": False,
        },
    )
elif MODE == "global_saturation_b0":
    CASES = (
        {
            "cell": "F04-R02",
            "divisor": "B0",
            "groebner": False,
            "global_saturation": True,
        },
    )
elif MODE == "global_saturation_all_b0":
    CASES = tuple(
        {
            "cell": f"{assignment}-{target}",
            "divisor": "B0",
            "groebner": False,
            "global_saturation": True,
            "skip_elimination": True,
        }
        for assignment in ("F04", "F05", "F06", "F07")
        for target in ("R02", "R20")
    )
elif MODE == "fiber_search_b0":
    CASES = (
        {
            "cell": "F04-R02",
            "divisor": "B0",
            "groebner": False,
            "fiber_search": True,
            "fiber_limit": 2,
        },
    )
elif MODE == "fiber_f_p6_b0":
    CASES = (
        {
            "cell": "F04-R02",
            "divisor": "B0",
            "groebner": False,
            "fiber_search": True,
            "fiber_limit": 64,
            "field_degree": 6,
        },
    )
elif MODE == "linear_s_f_p6_b0":
    LINEAR_S_ROOTS = (
        1691727589,
        2130706429,
        1804255948,
        1065353214,
        675900418,
    )
    CASES = tuple(
        {
            "cell": "F04-R02",
            "divisor": "B0",
            "groebner": False,
            "fiber_search": True,
            "fiber_start": root,
            "fiber_limit": 1,
            "field_degree": 6,
        }
        for root in LINEAR_S_ROOTS
    )
elif MODE in ("fiber_factor_b0", "fiber_factor_b0_s3"):
    factor_start = 1 if MODE == "fiber_factor_b0" else 3
    CASES = (
        {
            "cell": "F04-R02",
            "divisor": "B0",
            "groebner": False,
            "fiber_search": True,
            "factor_fibers": True,
            "fiber_start": factor_start,
            "fiber_limit": 1,
            "field_degree": 1,
        },
    )
else:
    raise ValueError(f"unsupported mode: {MODE}")

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
    .add_local_file(LIBRARY, "/branch_core.sage")
    .add_local_file(SCRIPT, "/degree12_quadratic_pseudoremainder_determinant_probe.sage")
)


@app.function(image=image, cpu=4, memory=32768, timeout=900, max_containers=8)
def run_case(case: dict[str, object]) -> dict[str, object]:
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
        "/degree12_quadratic_pseudoremainder_determinant_probe.sage",
        "--cell",
        str(case["cell"]),
        "--divisor",
        str(case["divisor"]),
    ]
    if case["groebner"]:
        command.append("--groebner")
    if case.get("global_saturation"):
        command.append("--global-saturation")
    if case.get("skip_elimination"):
        command.append("--skip-elimination")
    if case.get("fiber_search"):
        command.append("--fiber-search")
        command.extend(("--fiber-start", str(case.get("fiber_start", 1))))
        command.extend(("--fiber-limit", str(case["fiber_limit"])))
        command.extend(("--field-degree", str(case.get("field_degree", 1))))
    if case.get("factor_fibers"):
        command.append("--factor-fibers")
    try:
        completed = subprocess.run(
            command,
            cwd="/repo",
            env=environment,
            capture_output=True,
            text=True,
            timeout=(
                780
                if case["groebner"]
                or case.get("fiber_search")
                or case.get("global_saturation")
                else 300
            ),
            check=False,
        )
        records = []
        for line in completed.stdout.splitlines():
            if line.startswith("{"):
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
        done = next((row for row in records if row.get("phase") == "DONE"), None)
        return {
            **case,
            "status": "PASS" if completed.returncode == 0 and done else "FAIL",
            "returncode": completed.returncode,
            "seconds": round(time.monotonic() - began, 6),
            "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            "records": records,
            "stdout_sha256": hashlib.sha256(completed.stdout.encode()).hexdigest(),
            "stdout_tail": completed.stdout[-10000:],
            "stderr_tail": completed.stderr[-10000:],
        }
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout or ""
        stderr = error.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode(errors="replace")
        records = []
        for line in stdout.splitlines():
            if line.startswith("{"):
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
        return {
            **case,
            "status": "TIMEOUT",
            "seconds": round(time.monotonic() - began, 6),
            "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            "records": records,
            "stdout_tail": stdout[-10000:],
            "stderr_tail": stderr[-10000:],
        }


@app.local_entrypoint()
def main() -> None:
    rows = list(run_case.map(CASES, return_exceptions=True))
    normalized = []
    for case, row in zip(CASES, rows):
        if isinstance(row, BaseException):
            normalized.append({**case, "status": "REMOTE_ERROR", "error": repr(row)})
        else:
            normalized.append(row)
    output = {
        "schema": "kb-c2-112-fixed-degree12-quadratic-prem-determinant-modal-v1",
        "app": APP_NAME,
        "upstream_commit": COMMIT,
        "counts": {
            status: sum(row["status"] == status for row in normalized)
            for status in ("PASS", "FAIL", "TIMEOUT", "REMOTE_ERROR")
        },
        "results": normalized,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output["counts"], sort_keys=True))
    print(f"wrote {OUTPUT}")
