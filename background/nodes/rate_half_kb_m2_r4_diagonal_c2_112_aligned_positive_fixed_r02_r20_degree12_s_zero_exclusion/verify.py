#!/usr/bin/env python3
"""Fail-closed verifier for all fixed degree-12 s=0 exclusions."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent / "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_r20_degree12_leading_branch_decomposition"
FILES = {
    "modal_degree12_s_zero_output.json": "59ada35152d8cb19764f778f2f41c6769c5565cc749c0e3e677eb1c742d864c1",
    "modal_degree12_s_zero_f05_output.json": "85465a07e18a6872772ca3b02e8314c599f5dab8f029e6b4290070d0fdf636dc",
    "modal_degree12_s_zero_f06_f07_output.json": "7c77592e57370d40cffe7181c28d98051e7d3f06bbdeba77f4ba48d7659b6427",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def done(row: dict[str, object]) -> dict[str, object] | None:
    return next((record for record in row.get("records", []) if record.get("phase") == "DONE"), None)


def validate(payloads: list[dict[str, object]]) -> None:
    rows = [row for payload in payloads for row in payload["results"]]
    require(len(rows) == 8, "literal cell count")
    require(
        {row["cell"] for row in rows}
        == {
            f"{assignment}-{target}"
            for assignment in ("F04", "F05", "F06", "F07")
            for target in ("R02", "R20")
        },
        "literal cell set",
    )
    representative = {
        "F04": ("5b07627ec18114d36bf3190d4cfa3bd0c5abe9ee45f76d72e10f6e3a84c2ab1b", "ad25aa76da20b93a168d9cc75347688d7c405441ce4770f62e2552b534c68910"),
        "F07": ("5b07627ec18114d36bf3190d4cfa3bd0c5abe9ee45f76d72e10f6e3a84c2ab1b", "ad25aa76da20b93a168d9cc75347688d7c405441ce4770f62e2552b534c68910"),
        "F05": ("a16b5cb9613f097c828602233c052672dda16df8427ecc5d9fd57c475407c94d", "8149fcf72e6c3bda2a922dd1d2874bcc128d2272344e7568dde3287708fbc0fe"),
        "F06": ("a16b5cb9613f097c828602233c052672dda16df8427ecc5d9fd57c475407c94d", "8149fcf72e6c3bda2a922dd1d2874bcc128d2272344e7568dde3287708fbc0fe"),
    }
    for row in rows:
        terminal = done(row)
        require(row["status"] == "PASS" and terminal is not None, f"completion {row['cell']}")
        assignment = row["cell"].split("-")[0]
        selected_hash, basis_hash = representative[assignment]
        require(terminal["selected_sha256"] == selected_hash, f"selected {row['cell']}")
        require(terminal["basis_sha256"] == basis_hash and terminal["basis_size"] == 2, f"basis {row['cell']}")
        require(terminal["dimension"] == 1 and not terminal["unit_ideal"], f"dimension {row['cell']}")
        require(terminal["localizer_nilpotence_index"] == 1, f"localizer {row['cell']}")
        require(len(terminal["localizer_steps"]) == 14 and terminal["localizer_steps"][-1]["zero"], f"localizer steps {row['cell']}")
        require(terminal["terminal"] == "DEGREE12_S_ZERO_EMPTY", f"terminal {row['cell']}")


def main() -> None:
    payloads = []
    for name, expected_hash in FILES.items():
        path = PARENT / name
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected_hash, f"hash {name}")
        payload = json.loads(path.read_text())
        require(payload["counts"]["FAIL"] == 0 and payload["counts"]["TIMEOUT"] == 0, f"counts {name}")
        payloads.append(payload)
    validate(payloads)
    mutant = copy.deepcopy(payloads)
    done(mutant[0]["results"][0])["localizer_nilpotence_index"] = None
    rejected = False
    try:
        validate(mutant)
    except AssertionError:
        rejected = True
    require(rejected, "mutation rejection")
    print("KB_C2_112_FIXED_R02_R20_DEGREE12_S_ZERO_PASS cells=8 mutations=1/1")


if __name__ == "__main__":
    main()
