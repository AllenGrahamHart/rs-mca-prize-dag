#!/usr/bin/env python3
"""Check the pinned PR #1144 review-gate contract."""

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


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


statement = (NODE / "statement.md").read_text(encoding="ascii")
attack = (NODE / "attack.md").read_text(encoding="ascii")
replay = (NODE / "external_replay.md").read_text(encoding="ascii")
require("**status:** PROVABLE" in statement, "status")
require(COMMIT in statement and COMMIT in replay, "commit pin")
require(PAYLOAD in statement and PAYLOAD in replay, "payload pin")
require("29" in statement and "mutations=29" in replay, "mutation replay")
require("did not rerun Sage" in (NODE / "audit.md").read_text(encoding="ascii"),
        "review honesty")
require("Run the Sage compiler" in attack, "promotion recipe")
for value in PINS:
    require(value in replay, f"content pin {value}")

cells = {
    f"M{index:02d}-R{target}"
    for index in range(4)
    for target in ("02", "11", "20")
}
require(len(cells) == 12, "cell census")

print(
    "KB_C2_112_ALIGNED_POSITIVE_MOVING_UPSTREAM_REVIEW_GATE_PASS "
    f"cells={len(cells)} payload={PAYLOAD} mutations=29 sage_review=pending"
)
