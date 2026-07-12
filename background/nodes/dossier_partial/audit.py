#!/usr/bin/env python3
"""Gate-check the partial dossier and its exhaustive non-claims manifest."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DOSSIER = ROOT / "notes" / "dossier" / "PARTIAL_DOSSIER.md"
MANIFEST = ROOT / "notes" / "dossier" / "PARTIAL_DOSSIER_MANIFEST.json"


def multiplicative_order(value: int, modulus: int) -> int:
    current = 1
    for order in range(1, modulus + 1):
        current = current * value % modulus
        if current == 1:
            return order
    raise AssertionError("order not found")


def main() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    by_id = {node["id"]: node for node in dag["nodes"]}
    manifest = json.loads(MANIFEST.read_text())
    text = DOSSIER.read_text()
    normalized_text = " ".join(text.split()).lower()

    for node_id in manifest["required_proved_artifacts"]:
        if by_id[node_id].get("status") != "PROVED":
            raise AssertionError((node_id, by_id[node_id].get("status")))

    critical = json.loads((ROOT / "orbit" / "critical_dag.json").read_text())
    open_truth = {node["id"] for node in critical["nodes"] if node["label"] == "UNPROVED"}
    if set(manifest["open_truth_leaves"]) != open_truth:
        raise AssertionError("dossier non-claims do not match the critical orbit")

    q = 17**32
    assert q // (1 << 128) == 6
    assert 6 * (1 << 128) < q < 7 * (1 << 128)
    assert multiplicative_order(17, 512) == 32
    for phrase in (
        "This is not a full prize resolution.",
        "LD_sw(C,506)=7 > B*=6 >= LD_sw(C,507)=6",
        "largest safe closed integer-grid radius is `5/512`",
        "boundary supremum is",
        "Typed analytic targets are non-claims",
    ):
        if " ".join(phrase.split()).lower() not in normalized_text:
            raise AssertionError(f"missing dossier phrase: {phrase}")
    if "the full prize is resolved" in normalized_text:
        raise AssertionError("forbidden full-prize claim")
    print(f"PARTIAL_DOSSIER_AUDIT_PASS open_truth_leaves={len(open_truth)} tier1=proved")


if __name__ == "__main__":
    main()
