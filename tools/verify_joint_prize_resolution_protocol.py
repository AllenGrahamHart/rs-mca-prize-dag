#!/usr/bin/env python3
"""Fail-closed structural checks for the joint resolution protocol."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = ROOT / "notes" / "JOINT_PRIZE_RESOLUTION_PROTOCOL.md"


def require(text, anchor):
    assert anchor in text, f"missing protocol anchor: {anchor}"


checks = 0
required_files = (
    PROTOCOL,
    ROOT / "notes" / "PRIZE_RESOLUTION_ROADMAP.md",
    ROOT / "notes" / "convergence_ledger_20260724" / "CONVERGENCE_LEDGER_R1.md",
    ROOT / "notes" / "correspondence" / "JOINT_CROSSWALK.json",
    ROOT / "notes" / "PRIZE_COMPUTE_REQUESTS.md",
    ROOT / "dag.json",
)
for path in required_files:
    assert path.is_file(), f"missing protocol dependency: {path.relative_to(ROOT)}"
    checks += 1

protocol = PROTOCOL.read_text()
for heading in (
    "## 1. Mission and terminal condition",
    "## 2. Authority and workspace custody",
    "## 3. Work-cycle selection",
    "## 4. Mathematical and DAG status discipline",
    "## 5. Falsification and threshold relocation",
    "## 6. Crosswalk and two-axis status",
    "## 7. Harvest procedure",
    "## 8. Outbound PR procedure",
    "## 9. Verification and reproducibility",
    "## 10. RAM and computation law",
    "## 11. Governance and shared completion",
):
    require(protocol, heading)
    checks += 1

for anchor in (
    "`list_grand`, `mca_grand`, and `prize` are unconditionally `PROVED`",
    "No `TARGET`,",
    "returned numerator safe and the adjacent numerator unsafe",
    "status_ours: mathematical truth in our DAG",
    "status_his: upstream bankability/acceptance",
    "Never widen a scoped identification silently",
    "current F2",
    "zero-prefix only",
    "current L1 identification is `e=0`",
    "rate-half band/Q row is analogy-only",
    "Normally keep at most two open PRs",
    "conservative total wall time is below five minutes",
    "conservative total cost is below `$1`",
    "INCOMPLETE: evidence only, no status change",
    "An adversarial completion audit",
):
    require(protocol, anchor)
    checks += 1

dag = json.loads((ROOT / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
for terminal in ("list_grand", "mca_grand", "prize"):
    assert terminal in nodes, f"missing terminal node: {terminal}"
    checks += 1

crosswalk = json.loads(
    (ROOT / "notes" / "correspondence" / "JOINT_CROSSWALK.json").read_text()
)
assert crosswalk["schema"] == "joint-crosswalk-v1"
checks += 1
relations = {"IDENTICAL", "OVERLAP", "ANALOGY_ONLY", "OURS_ONLY", "HIS_ONLY"}
for row in crosswalk["rows"]:
    assert row["relation"] in relations
    if row["our_node"] is not None:
        assert row["our_node"] in nodes
    checks += 1

roadmap = (ROOT / "notes" / "PRIZE_RESOLUTION_ROADMAP.md").read_text()
ledger = (
    ROOT / "notes" / "convergence_ledger_20260724" / "CONVERGENCE_LEDGER_R1.md"
).read_text()
compute = (ROOT / "notes" / "PRIZE_COMPUTE_REQUESTS.md").read_text()
for text in (roadmap, ledger, compute):
    require(text, "JOINT_PRIZE_RESOLUTION_PROTOCOL.md")
    checks += 1

print(f"JOINT_PRIZE_RESOLUTION_PROTOCOL_PASS checks={checks}")
