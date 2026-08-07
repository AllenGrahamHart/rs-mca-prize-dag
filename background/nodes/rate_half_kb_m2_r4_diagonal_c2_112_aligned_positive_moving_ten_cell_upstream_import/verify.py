#!/usr/bin/env python3
"""Verify the ten-cell subset of the independent PR #1144 review ledger."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
GATE = NODE.parent / (
    "rate_half_kb_m2_r4_diagonal_c2_112_"
    "aligned_positive_moving_upstream_review_gate"
)
LEDGER = GATE / "modal_review_output.json"
LEDGER_SHA256 = "71c116c5bc1fccf5ce104a92948e91ebca66a90c685b13399362a258b68183e0"
COMMIT = "05ff2348de8f2c0f99683875ff12a9a79dcf21ec"
PAYLOAD = "343b691abab47586545aca75393bea1e1fff1dfb63537f059e4faef341893145"
DIRECT = {
    "M00-R02",
    "M00-R20",
    "M01-R02",
    "M01-R20",
    "M03-R02",
    "M03-R11",
    "M03-R20",
}
CLOSED = DIRECT | {"M00-R11", "M02-R02", "M02-R20"}
REQUIRED = DIRECT | {
    "transport",
    "import",
    "parity-M03",
    "python-normal",
    "python-optimized",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


raw = LEDGER.read_bytes()
require(hashlib.sha256(raw).hexdigest() == LEDGER_SHA256, "review ledger pin")
ledger = json.loads(raw)
require(ledger["upstream_commit"] == COMMIT, "commit pin")
rows = {row["name"]: row for row in ledger["results"]}
require(REQUIRED <= rows.keys(), "missing review case")
for name in REQUIRED:
    require(rows[name]["status"] == "PASS", f"review case {name}")
for name in DIRECT | {"transport", "import", "parity-M03"}:
    require(
        "PASS aligned-positive moving closure compiler" in rows[name]["stdout_tail"],
        f"Sage marker {name}",
    )
require(PAYLOAD in rows["python-normal"]["stdout_tail"], "payload")
require("mutations=29" in rows["python-normal"]["stdout_tail"], "mutations")
require(
    "optimized Python execution is refused" in rows["python-optimized"]["stderr_tail"],
    "optimized refusal",
)
require("M01-R11" not in CLOSED and "M02-R11" not in CLOSED, "scope fence")
require(len(CLOSED) == 10, "cell count")

statement = (NODE / "statement.md").read_text(encoding="ascii")
for cell in CLOSED:
    require(cell in statement, f"missing closed cell {cell}")
for cell in ("M01-R11", "M02-R11"):
    require(cell in statement and "does not claim" in statement, f"residual {cell}")

print(
    "KB_C2_112_ALIGNED_POSITIVE_MOVING_TEN_CELL_IMPORT_PASS "
    f"cells={len(CLOSED)} direct={len(DIRECT)} payload={PAYLOAD} mutations=29/29"
)
