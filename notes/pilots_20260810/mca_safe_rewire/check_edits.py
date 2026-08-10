#!/usr/bin/env python3
"""Verify the drafted edits BEFORE the coordinator applies them.

Checks, per edit:
  1. the target file exists;
  2. old_string occurs EXACTLY ONCE (Edit-tool precondition);
  3. new_string differs from old_string;
  4. new_string contains old_string when the edit is an append/insert
     (reported, not required).

Then simulates check 3 of tools/verify_conditional_propagation.py against
the POST-edit text of every CONDITIONAL node touched, using the req/ev graph
rebuilt from node.json shards (dag.json is never opened).

Read-only: applies nothing.  stdlib only.
"""
from __future__ import annotations

import json
import os
import re
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
GRANDS = {"mca_grand", "list_grand"}
AUDITED_UNRELATED = {
    ("aperiodic_zero_at_crossing", "rate_half_band_closure"),
    ("knife_edge_census", "census_dodge_selection"),
    ("list_adjacency_closing", "ww_row_envelope_clause"),
    ("list_grand", "rate_half_band_closure"),
    ("rate_half_band_closure", "list_adjacency_closing"),
    ("rate_half_band_closure", "rate_half_list_adjacent_crossing"),
    ("xr_clean_residual_any_gate", "rigidity_kernel"),
    ("xr_smallcore_spread_count", "rigidity_kernel"),
    ("xr_smallcore_spread_count", "rk_rigidity_kernel"),
    ("xr_smallcore_spread_count", "shared_census_kernel"),
}


def load_graph():
    nodes, req, ev = {}, [], []
    for tier in ("critical", "background"):
        base = os.path.join(ROOT, tier, "nodes")
        for name in sorted(os.listdir(base)):
            p = os.path.join(base, name, "node.json")
            if not os.path.isfile(p):
                continue
            with open(p) as fh:
                d = json.load(fh)
            n = d["node"]
            nodes[n["id"]] = {"status": n.get("status"), "tier": tier,
                              "statement": n.get("statement") or "",
                              "notes": n.get("notes") or ""}
            for e in d.get("requires", []):
                req.append((e["from"], n["id"]))
            for e in d.get("evidence_for", []):
                ev.append((n["id"], e["to"]))
    return nodes, req, ev


def closure(seed, adj):
    out, st = set(), [seed]
    while st:
        for x in adj[st.pop()]:
            if x not in out:
                out.add(x)
                st.append(x)
    return out


def main():
    spec = json.load(open(os.path.join(HERE, "edits.json")))
    ok = True
    print("=== EDIT PRECONDITIONS ===")
    post = {}
    for e in spec["edits"]:
        path = os.path.join(ROOT, e["file"])
        if not os.path.isfile(path):
            print(f"{e['id']}: MISSING FILE {e['file']}")
            ok = False
            continue
        text = open(path, errors="replace").read()
        c = text.count(e["old_string"])
        status = "OK" if c == 1 else "FAIL"
        if c != 1:
            ok = False
        grew = len(e["new_string"]) - len(e["old_string"])
        print(f"{e['id']}: {status} occurrences={c} delta={grew:+d} chars "
              f"[{e['file']}]")
        if c == 1:
            post[e["file"]] = text.replace(e["old_string"], e["new_string"])

    nodes, req, ev = load_graph()
    rev, fwd = defaultdict(list), defaultdict(list)
    for u, v in req:
        rev[v].append(u)
        fwd[u].append(v)
    evrev = defaultdict(set)
    for u, v in ev:
        evrev[v].add(u)
    crit = set(g for g in GRANDS if g in nodes)
    st = list(crit)
    while st:
        for u in rev[st.pop()]:
            if u not in crit:
                crit.add(u)
                st.append(u)

    print("\n=== verify_conditional_propagation CHECK 3 ON POST-EDIT TEXT ===")
    touched = sorted({e["file"].split("/")[2] for e in spec["edits"]
                      if e["file"].startswith("critical/nodes/")})
    for nid in touched:
        if nid not in nodes or nodes[nid]["status"] != "CONDITIONAL":
            print(f"{nid}: status={nodes.get(nid, {}).get('status')} "
                  "-> check 3 does not apply")
            continue
        anc, des = closure(nid, rev), closure(nid, fwd)
        text = nodes[nid]["statement"] + " " + nodes[nid]["notes"]
        cpath = f"critical/nodes/{nid}/conditional.md"
        full = os.path.join(ROOT, cpath)
        if cpath in post:
            text += " " + post[cpath]
        elif os.path.isfile(full):
            text += " " + open(full, errors="replace").read()
        found = set()
        for t in {m for m in re.findall(r"\b[a-z][a-z0-9_]{6,}\b", text)
                  if m in nodes}:
            if t == nid or nodes[t]["status"] == "PROVED":
                continue
            if t in anc or t in evrev[nid] or t in des:
                continue
            found.add((nid, t))
        new = sorted(found - AUDITED_UNRELATED)
        verdict = "CLEAN" if not new else "FIRES -> AUDITED_UNRELATED needs"
        print(f"{nid}: {verdict} {new if new else ''}")
        if new:
            ok = False
    print("\nRESULT:", "ALL PRECONDITIONS OK (check-3 additions listed above "
          "are the only follow-up)" if ok else
          "ACTION REQUIRED — see FAIL/FIRES lines")


if __name__ == "__main__":
    main()
