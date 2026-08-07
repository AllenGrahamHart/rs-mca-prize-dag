#!/usr/bin/env python3
"""Check the narrowed PR #1144 balanced-pair review gate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
COMMIT = "05ff2348de8f2c0f99683875ff12a9a79dcf21ec"
PAYLOAD = "343b691abab47586545aca75393bea1e1fff1dfb63537f059e4faef341893145"
PINS = (
    "da9273a631a0f88056ba57433fc5ff2c9ced4f223e0aa6ad515744c765431855",
    "659772381a053d2f0e0598a0dfc91502065b07c6685f0fdebb22486f8bf6c41b",
    "13fab1b9fc1c77b7cc880f52194ab212c040eab946edc851f24891de09ff71a0",
    "2ed13fbab353d0ac3017fa31cab68de3f3b66f190061ba63fd277dbdc7958675",
    "14130c7ebd867487e28393fc815dc99e150626b19b6e7f88baba449792cbf6ff",
)
FILES = {
    "primary": (
        "modal_review_output.json",
        "71c116c5bc1fccf5ce104a92948e91ebca66a90c685b13399362a258b68183e0",
    ),
    "sage107": (
        "modal_review_m01_sage107_output.json",
        "00df65da9fbd5894bb01e757eb0733f8d94325efe7ceca12ea0f3674d382abcd",
    ),
    "official109": (
        "modal_review_m01_sage109_official_output.json",
        "5d52e98c77bcff36182989d1a5896d2b51aba765407a543477a95f5e0dff2ddc",
    ),
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


loaded = {}
for name, (filename, expected) in FILES.items():
    raw = (NODE / filename).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == expected, f"{name} pin")
    loaded[name] = json.loads(raw)

primary = loaded["primary"]
require(primary["upstream_commit"] == COMMIT, "primary commit")
require(primary["counts"] == {
    "FAIL": 1,
    "PASS": 13,
    "REMOTE_ERROR": 0,
    "TIMEOUT": 0,
}, "primary count")
rows = {row["name"]: row for row in primary["results"]}
require(rows["M01-R11"]["status"] == "FAIL", "M01 status")
require("RecursionError" in rows["M01-R11"]["stderr_tail"], "M01 failure")
require(rows["parity-M01"]["status"] == "PASS", "M01 parity")
require(rows["python-normal"]["status"] == "PASS", "Python replay")
require(PAYLOAD in rows["python-normal"]["stdout_tail"], "payload")
require("mutations=29" in rows["python-normal"]["stdout_tail"], "mutations")

for name in ("sage107", "official109"):
    row = loaded[name]["result"]
    require(row["name"] == "M01-R11" and row["status"] == "FAIL", name)
    require("RecursionError" in row["stderr_tail"], f"{name} failure")

timeout = json.loads(
    (NODE / "modal_review_m01_libsingular_sage109_timeout.json").read_text()
)
require(timeout["status"] == "TIMEOUT", "libSingular timeout")
require(timeout["subprocess_timeout_seconds"] == 1740, "timeout cap")
require(timeout["replacement_count"] == 2, "backend replacement fence")

statement = (NODE / "statement.md").read_text(encoding="ascii")
replay = (NODE / "external_replay.md").read_text(encoding="ascii")
require("**status:** PROVABLE" in statement, "status")
for cell in ("M01-R11", "M02-R11"):
    require(cell in statement, f"residual {cell}")
for value in (COMMIT, PAYLOAD, *PINS):
    require(value in statement or value in replay, f"pin {value}")

print(
    "KB_C2_112_ALIGNED_POSITIVE_MOVING_REVIEW_GATE_PASS "
    f"residual=2 primary=13/14 parity_M01=PASS timeout={timeout['subprocess_timeout_seconds']}"
)
