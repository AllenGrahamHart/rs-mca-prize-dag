#!/usr/bin/env python3
"""Verify the pinned PR #1149 twelve-cell orbit review."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
LEDGER = NODE / "modal_review_output.json"
LEDGER_SHA256 = "473710b935f7866f185e6ad9a0938a3a49215031c30c54e19a023a22dcacd6d5"
PAIR_LEDGER = NODE / "modal_pair_sweep_output.json"
PAIR_LEDGER_SHA256 = "dd10ce59f9ee4f8ed414b9905bdeab661c6ae4fcdf85d9003ab2b9139295b245"
COMMIT = "55ac3e07477bd7a768190a3e755f22b0d44354b0"
PAYLOAD = "4adc4187bb5794ed70fce122055fb94916974c1adacf9451237aff002ebfd63e"
PINS = (
    "1b4e7b8c6c284f5bdfa1634d54bfc6aafc188adea21c9c4578e21d766ca6125b",
    "d64dfd1a2806eec3d4788eb3c4b990f87bb8655fa9cf91d83393bd217dd7fddb",
    "4c66a081e4fe0a821c96326489698df6a22e4c1281efc34005cbdf5b525a8b04",
    "a1fa5172dc1643cc9b72894fa2110f2e90a54558a2975b9519a25328f9b4057b",
)
EXPECTED_GROUPS = {
    frozenset(("F04-R02", "F07-R02")),
    frozenset(("F04-R11", "F07-R11")),
    frozenset(("F04-R20", "F07-R20")),
    frozenset(("F05-R02", "F06-R02")),
    frozenset(("F05-R11", "F06-R11")),
    frozenset(("F05-R20", "F06-R20")),
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


raw = LEDGER.read_bytes()
require(hashlib.sha256(raw).hexdigest() == LEDGER_SHA256, "ledger pin")
ledger = json.loads(raw)
require(ledger["upstream_commit"] == COMMIT, "commit")
require(ledger["counts"] == {
    "FAIL": 0,
    "PASS": 12,
    "REMOTE_ERROR": 0,
    "TIMEOUT": 0,
}, "review counts")

fingerprints = {}
for row in ledger["results"]:
    require(row["status"] == "PASS", f"cell {row['cell']}")
    summary = row["summary"]
    require(summary["cell_id"] == row["cell"], "cell identity")
    result = summary["resultant_metric"]
    degree = result["degree"]
    require(degree in (38, 42), "resultant degree")
    require(result["terms"] == (2464 if degree == 38 else 3679), "terms")
    names = ("AF_minus_CD", "AE_minus_BD", "BF_minus_CE")
    core_hashes = tuple(
        summary["blocks"][name]["factor_metrics"][-1]["metric"]["sha256"]
        for name in names
    )
    key = (result["sha256"], core_hashes)
    fingerprints.setdefault(key, set()).add(row["cell"])

groups = {frozenset(group) for group in fingerprints.values()}
require(groups == EXPECTED_GROUPS, "six orbit groups")
require(all(len(group) == 2 for group in groups), "pair sizes")

pair_raw = PAIR_LEDGER.read_bytes()
require(hashlib.sha256(pair_raw).hexdigest() == PAIR_LEDGER_SHA256, "pair ledger")
pair_ledger = json.loads(pair_raw)
require(pair_ledger["counts"] == {
    "EXPECTED_REJECT": 10,
    "FAIL": 0,
    "PASS": 2,
    "REMOTE_ERROR": 0,
    "TIMEOUT": 0,
}, "pair sweep counts")
for row in pair_ledger["results"]:
    require(
        row["status"] == ("PASS" if row["pair"] == [0, 1] else "EXPECTED_REJECT"),
        f"row-pair scope {row['cell']} {row['pair']}",
    )

a, b, c, d, e, f, w = sp.symbols("a b c d e f w")
p = a * w**2 + b * w + c
q = d * w**2 + e * w + f
u = a * f - c * d
v = a * e - b * d
z = b * f - c * e
r = u**2 - v * z
identities = (
    sp.resultant(p, q, w) - r,
    d * p - a * q + v * w + u,
    sp.together(v**2 * p.subs(w, -u / v) - a * r),
    sp.together(v**2 * q.subs(w, -u / v) - d * r),
    a * z - b * u + c * v,
)
require(all(sp.expand(value) == 0 for value in identities), "identities")

proof = (NODE / "proof.md").read_text(encoding="ascii")
for value in (COMMIT, PAYLOAD, LEDGER_SHA256, *PINS):
    require(value in proof, f"pin {value}")

print(
    "KB_C2_112_ALIGNED_POSITIVE_FIXED_ORBIT_COMPRESSION_PASS "
    f"cells=12 orbits={len(groups)} identities={len(identities)} "
    f"quadratic_pairs=2/12 payload={PAYLOAD}"
)
