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
DIRECT_FILES = {
    "staged": (
        "modal_review_m01_direct_singular_staged_timeout_output.json",
        "d21e707c9728259e4c3e44225167bc3928fbb37fc7d465eca6851d969cbe0384",
        1740,
    ),
    "monolithic": (
        "modal_review_m01_direct_singular_chunkless_timeout_output.json",
        "641e48ad765e58c42959a72206ac056c9e66b74cf7722bf2e36958a3e9c00333",
        1740,
    ),
    "chunked": (
        "modal_review_m01_direct_singular_certificate_output.json",
        "0d8e525bac83f54ca4623e5520c07214a9dbdce84a4b82e69a87b8202b0caf37",
        3540,
    ),
}
DIRECT_SOURCE_PINS = {
    "review_m01_direct_singular_certificate.sage":
        "3dbc9582186ab26f891b46c579565ccb796bde2a544b7de76ae4754afd50a7ba",
    "review_m01_direct_singular_certificate_modal.py":
        "6b75c78fee905a0707d6968ca2d3399dcbe9b986f4e2e767b0909575f246e04b",
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

for filename, expected in DIRECT_SOURCE_PINS.items():
    require(hashlib.sha256((NODE / filename).read_bytes()).hexdigest() == expected,
            f"direct source pin {filename}")

direct = {}
for name, (filename, expected, seconds) in DIRECT_FILES.items():
    raw = (NODE / filename).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == expected, f"direct {name} pin")
    direct[name] = json.loads(raw)
    result = direct[name]["result"]
    require(result["status"] == "TIMEOUT", f"direct {name} status")
    require(seconds <= result["seconds"] < seconds + 1, f"direct {name} cap")
    require(result["peak_kb"] < 4_800_000, f"direct {name} peak")
    require("QSLICE_BASIS_SIZE=168" in result["stdout_tail"],
            f"direct {name} qslice")
    require("J_BASIS_SIZE=174" in result["stdout_tail"],
            f"direct {name} J")

require("WZERO_SQUARE_TERMS=0" in direct["staged"]["result"]["stdout_tail"],
        "direct boundary closure")
chunked = direct["chunked"]["result"]
source = chunked["records"][0]
require(source["I_chunk_count"] == 148 and source["I_chunk_size"] == 1024,
        "direct chunk plan")
require(source["I"]["terms"] == 151178, "direct I terms")
require("I_CHUNK_PROGRESS=8/148" not in chunked["stdout_tail"],
        "direct chunk fence")

statement = (NODE / "statement.md").read_text(encoding="ascii")
replay = (NODE / "external_replay.md").read_text(encoding="ascii")
require("**status:** PROVABLE" in statement, "status")
for cell in ("M01-R11", "M02-R11"):
    require(cell in statement, f"residual {cell}")
for value in (COMMIT, PAYLOAD, *PINS):
    require(value in statement or value in replay, f"pin {value}")

print(
    "KB_C2_112_ALIGNED_POSITIVE_MOVING_REVIEW_GATE_PASS "
    f"residual=2 primary=13/14 parity_M01=PASS "
    f"direct_timeouts=3 chunked_I={source['I_chunk_count']}x{source['I_chunk_size']}"
)
