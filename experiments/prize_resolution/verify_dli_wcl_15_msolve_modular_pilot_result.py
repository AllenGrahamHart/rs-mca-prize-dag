#!/usr/bin/env python3
"""Check the bounded WCL (1,5) msolve handoff record."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
RESULT = HERE / "dli_wcl_15_msolve_modular_pilot_result.json"
FLINT_RESULT = HERE / "dli_wcl_15_flint_quotient_result.json"
PROGRAM = HERE / "dli_wcl_15_msolve_modular_pilot_modal.py"
EXPECTED_INPUT = "c7b87cdf08b13210480aa6d6cad4a0774247328954c81757226277bca54f46cf"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    result = json.loads(RESULT.read_text(encoding="utf-8"))
    flint = json.loads(FLINT_RESULT.read_text(encoding="utf-8"))
    program_hash = hashlib.sha256(PROGRAM.read_bytes()).hexdigest()

    require(result["status"] == "INCOMPLETE_TIMEOUT", "status")
    require(result["program_sha256"] == program_hash, "program hash")
    require(result["input_sha256"] == EXPECTED_INPUT, "input hash")
    require(
        result["coefficient_term_counts"]
        == flint["stage8"]["coefficient_term_counts"],
        "term counts",
    )
    require(
        result["coefficient_content_sha256"]
        == flint["stage8"]["content_sha256"],
        "coefficient hashes",
    )

    current = result["authoritative_run"]
    comparison = result["comparison_run"]
    require(current["msolve_version"] == "0.10.1", "current engine")
    require(comparison["msolve_version"] == "0.7.5", "comparison engine")
    require(current["algebra_timeout_seconds"] == 210, "current timeout")
    require(comparison["algebra_timeout_seconds"] == 240, "comparison timeout")
    for run in (current, comparison):
        require(run["unit_ideal_mod_p"] is None, "false verdict")
        require(run["returncode"] == -15, "termination code")
        require(run["output_bytes"] == 0, "unexpected basis")
        require(run["all_containers_stopped"] is True, "live container")

    requests = (ROOT / "notes/PRIZE_COMPUTE_REQUESTS.md").read_text(encoding="utf-8")
    roadmap = (ROOT / "notes/PRIZE_RESOLUTION_ROADMAP.md").read_text(encoding="utf-8")
    require("CR-004-MSOLVE-LONG" in requests, "external request missing")
    require(EXPECTED_INPUT in requests and EXPECTED_INPUT in roadmap, "handoff hash")
    require("no mathematical verdict" in requests, "scope language")

    print(
        "DLI_WCL_15_MSOLVE_MODULAR_PILOT_RECORD_PASS "
        "engines=0.7.5,0.10.1 status=INCOMPLETE_TIMEOUT containers=stopped"
    )


if __name__ == "__main__":
    main()
