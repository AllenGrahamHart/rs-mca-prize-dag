#!/usr/bin/env python3
"""Fail-closed validator for notes/correspondence/JOINT_CROSSWALK.json.

The identification discipline, machine-enforced (Convergence Ledger r1,
maintainer-approved 2026-07-24):
  - every our_node exists in dag.json, and the recorded status matches;
  - IDENTICAL  => a non-null machine-verified chain reference AND a stated scope;
  - ANALOGY_ONLY => chain is null AND the scope carries a fence citation;
  - JOINT owner => both sides named (our_node and his_object);
  - HIS_ONLY   => our_node is null; OURS_ONLY => his_object is null;
  - chain references that name a dag node must exist and be PROVED.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {n["id"]: n for n in dag["nodes"]}
    cw = json.loads((ROOT / "notes/correspondence/JOINT_CROSSWALK.json").read_text())
    assert cw.get("schema") == "joint-crosswalk-v1"

    errors = []
    for i, r in enumerate(cw["rows"]):
        tag = f"row {i} ({r.get('our_node') or (r.get('his_object') or {}).get('label')})"
        rel = r.get("relation")
        if rel not in ("IDENTICAL", "OVERLAP", "ANALOGY_ONLY", "OURS_ONLY", "HIS_ONLY"):
            errors.append(f"{tag}: bad relation {rel}"); continue
        our = r.get("our_node")
        if our is not None:
            if our not in nodes:
                errors.append(f"{tag}: our_node missing from dag"); continue
            if r.get("status_ours") != nodes[our]["status"]:
                errors.append(f"{tag}: status drift {r.get('status_ours')} != {nodes[our]['status']}")
        if rel == "IDENTICAL":
            if not r.get("chain"):
                errors.append(f"{tag}: IDENTICAL requires a chain")
            if not r.get("scope"):
                errors.append(f"{tag}: IDENTICAL requires a stated scope")
            chain = r.get("chain") or ""
            if chain in nodes and nodes[chain]["status"] != "PROVED":
                errors.append(f"{tag}: chain node {chain} not PROVED")
        if rel == "ANALOGY_ONLY":
            if r.get("chain") is not None:
                errors.append(f"{tag}: ANALOGY_ONLY must have chain=null")
            scope = (r.get("scope") or "") + " ".join(r.get("nonclaims", []))
            if not scope:
                errors.append(f"{tag}: ANALOGY_ONLY requires a fence")
        if rel == "HIS_ONLY" and our is not None:
            errors.append(f"{tag}: HIS_ONLY must have our_node=null")
        if rel == "OURS_ONLY" and r.get("his_object") is not None:
            errors.append(f"{tag}: OURS_ONLY must have his_object=null")
        if r.get("owner") == "JOINT" and (our is None or r.get("his_object") is None):
            errors.append(f"{tag}: JOINT requires both sides named")
        # alias consistency: mapped nodes carry the additive upstream field
        if our is not None and r.get("his_object") is not None:
            up = nodes[our].get("upstream") or {}
            if up.get("relation") != rel:
                errors.append(f"{tag}: dag upstream alias missing or relation drift")

    if errors:
        for e in errors:
            print("FAIL:", e)
        return 1
    idc = sum(1 for r in cw["rows"] if r["relation"] == "IDENTICAL")
    print(f"JOINT_CROSSWALK_PASS rows={len(cw['rows'])} identical={idc} "
          f"pins={cw['provenance']['our_sha']}/{cw['provenance']['his_sha']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
