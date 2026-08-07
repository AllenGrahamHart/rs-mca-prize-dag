#!/usr/bin/env python3
"""Replay the compact arithmetic and provenance contract for PR #1141."""

from pathlib import Path


NODE = Path(__file__).resolve().parent
PRIME = 2130706433
COMMIT = "826c0e7610604d550b8dd9b772c197a4e660e525"
PAYLOAD = "51572f4d190a3bceb31494ae7ee48f6b026346413ae398d2da4f7b1da1402438"
PINS = {
    "certificate": "4cfbc86bdf1c295e832fa23414d2a7b98ebc5a05bfe2cc88e0ecbf076c5e7925",
    "sage": "e65439765b029443f8f309da74e4195ba7cd96db9f1d0c89145d3582e3d04061",
    "python": "80ab8beb9a4644b6d6779918c679baff440552bcd3c3134b4b405438c194cb4a",
    "note": "b3aca650fc8f2f41f99e59d17fe2df926ab7a7fb4895cae6f20127c802b2c1d0",
}
ROWS = (
    (940017546, 317112865, 1161791022, 627736383),
    (940017546, 462252474, 145305698, 1796550960),
    (584912723, 1671616282, 297746731, 555560394),
    (584912723, 134663927, 1672091025, 1334100861),
    (1190675975, 309729886, 1997957961, 2008265187),
    (1190675975, 1042061214, 2038553966, 1196113770),
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def norm(a, slope, constant):
    return (constant * constant - a * slope * constant + slope * slope) % PRIME


for index, (a, slope, constant, expected) in enumerate(ROWS):
    require(norm(a, slope, constant) == expected, f"norm row {index}")
    require(expected != 0, f"nonzero row {index}")

statement = (NODE / "statement.md").read_text(encoding="ascii")
proof = (NODE / "proof.md").read_text(encoding="ascii")
replay = (NODE / "external_replay.md").read_text(encoding="ascii")
for value in (COMMIT, PAYLOAD, *PINS.values()):
    require(value in proof or value in replay, f"missing pin {value}")
for assignment in ("F02", "F03"):
    for target in ("R02", "R11", "R20"):
        require(f"{assignment}-{target}" in statement, f"cell {assignment}-{target}")
require("26/26" in replay, "mutation replay")

print(
    "KB_C2_112_ALIGNED_POSITIVE_F02_F03_UPSTREAM_IMPORT_PASS "
    f"cells=6 norms={len(ROWS)} payload={PAYLOAD} mutations=26/26"
)
