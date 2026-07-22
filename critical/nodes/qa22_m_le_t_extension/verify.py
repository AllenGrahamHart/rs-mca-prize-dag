#!/usr/bin/env python3
"""Registered replay wrapper for the QA.22 exact-grid proof packet."""

from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "qme_verify.py"
BANKED = HERE / "qme_verify_out.txt"

PINS = {
    "qme_verify.py": "1603897cd6594bd3fdf0e1cb077acc3759c4e9acd9a3349b92023b78b01fd9f2",
    "qme_verify_out.txt": "2e6f8cba3f8249b2d8c8dffc9cc0c08190584c631744d8d57528d5ff2b0ea176",
    "qme_statement.md": "367d236513826bddba7f6836dd801bf613d573a853880ace8b6616d2584ed499",
    "qme_proof.md": "457f44f2c94d8ffd85e925c9217caf719330004ad255b907caf05bf32cc1421d",
    "qme_claim_contract.md": "916e6460ece7f033ae181e76e8ec883bfc765b269b5cf07ab3e005b5eff0d008",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    for name, expected in PINS.items():
        actual = hashlib.sha256((HERE / name).read_bytes()).hexdigest()
        require(actual == expected, f"hash drift: {name}")

    completed = subprocess.run(
        [sys.executable, str(SOURCE)],
        cwd=HERE,
        capture_output=True,
        text=True,
        timeout=45,
    )
    require(completed.returncode == 0, completed.stdout + completed.stderr)
    require(completed.stderr == "", f"unexpected stderr: {completed.stderr[-1000:]}")
    require(completed.stdout == BANKED.read_text(), "replay differs from banked output")
    require(completed.stdout.count("[PASS]") == 26, "PASS count drift")
    require("[FAIL]" not in completed.stdout, "failed packet check")
    require(completed.stdout.rstrip().endswith("RESULT: ALL CHECKS PASS"), "bad result tail")
    print(
        "QA22_M_LE_T_EXTENSION_PASS "
        "rows=128 own_cells=3392 checks=26 mutations=5 pinned=5"
    )


if __name__ == "__main__":
    main()
