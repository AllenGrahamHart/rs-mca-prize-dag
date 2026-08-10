#!/usr/bin/env python3
"""D4 census/validator impact of the drafted mca_safe rewire.

Rebuilds the req/ev/alt edge graph from node.json SHARDS ONLY (dag.json is
never opened, per the pilot's RAM discipline), reproduces the three pinned
numbers of tools/verify_conditional_propagation.py
(EXPECTED_TARGETS/EXPECTED_CONDITIONALS/EXPECTED_ROUNDS), then recomputes
them under the drafted surgery.

Surgery modelled:
  - remove req edge  rate_half_band_closure -> mca_safe
  - add    req edge  rate_half_half_distance_safe_bracket -> mca_safe

Read-only.  Writes nothing.
"""
from __future__ import annotations

import json
import os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
GRANDS = {"mca_grand", "list_grand"}


def load():
    nodes, req, ev, alt = {}, [], [], []
    for tier in ("critical", "background"):
        base = os.path.join(ROOT, tier, "nodes")
        if not os.path.isdir(base):
            continue
        for name in sorted(os.listdir(base)):
            p = os.path.join(base, name, "node.json")
            if not os.path.isfile(p):
                continue
            with open(p) as fh:
                d = json.load(fh)
            n = d["node"]
            nodes[n["id"]] = {"status": n.get("status"), "gate": n.get("gate"),
                              "tier": tier}
            for e in d.get("requires", []):
                req.append((e["from"], n["id"]))
            for e in d.get("evidence_for", []):
                ev.append((n["id"], e["to"]))
            for e in d.get("alternatives", []):
                alt.append((e["from"], n["id"]))
    return nodes, req, ev, alt


def orbit(nodes, req, alt):
    rev = defaultdict(list)
    for u, v in req:
        rev[v].append(u)
    crit = set(g for g in GRANDS if g in nodes)
    st = list(crit)
    while st:
        for u in rev[st.pop()]:
            if u not in crit:
                crit.add(u)
                st.append(u)
    grew = True
    while grew:
        grew = False
        for u, v in alt:
            if (v in crit and u not in crit and u in nodes
                    and nodes[u]["status"] in ("PROVED", "PROVABLE")
                    and nodes[v].get("gate") == "any"):
                crit.add(u)
                grew = True
                s2 = [u]
                while s2:
                    for x in rev[s2.pop()]:
                        if x not in crit:
                            crit.add(x)
                            s2.append(x)
    return crit, rev


def census(nodes, req, alt, tag):
    crit, rev = orbit(nodes, req, alt)
    targets = sorted(i for i in crit if nodes[i]["status"] == "TARGET")
    conds = sorted(i for i in crit if nodes[i]["status"] == "CONDITIONAL")
    proved = sorted(i for i in crit if nodes[i]["status"] == "PROVED")
    discharged = set(proved) | set(targets)
    rounds, changed = 0, True
    while changed:
        changed = False
        rounds += 1
        for i in conds:
            if i not in discharged and all(p in discharged
                                           for p in rev[i] if p in crit):
                discharged.add(i)
                changed = True
    stuck = [i for i in conds if i not in discharged]
    print(f"[{tag}] orbit={len(crit)} TARGET={len(targets)} "
          f"CONDITIONAL={len(conds)} PROVED={len(proved)} rounds={rounds} "
          f"stuck={stuck}")
    return crit, set(targets), set(conds), set(proved), rounds


def main():
    nodes, req, ev, alt = load()
    print(f"shards loaded: {len(nodes)} nodes, {len(req)} req edges, "
          f"{len(ev)} ev edges, {len(alt)} alt edges")
    c0 = census(nodes, req, alt, "BEFORE")

    req2 = [e for e in req
            if e != ("rate_half_band_closure", "mca_safe")]
    assert len(req2) == len(req) - 1, "the edge to remove was not found"
    req2.append(("rate_half_half_distance_safe_bracket", "mca_safe"))
    c1 = census(nodes, req2, alt, "AFTER ")

    for label, i in (("TARGET", 1), ("CONDITIONAL", 2), ("PROVED", 3)):
        entered = sorted(c1[i] - c0[i])
        left = sorted(c0[i] - c1[i])
        print(f"  {label}: entered={entered} left={left}")
    print(f"  rounds: {c0[4]} -> {c1[4]}")
    print("  orbit membership delta: entered="
          f"{sorted(c1[0] - c0[0])} left={sorted(c0[0] - c1[0])}")

    # prose-mention check #3 of verify_conditional_propagation.py, restricted
    # to the pair that the surgery puts at risk.
    def closure(seed, adj):
        out, st = set(), [seed]
        while st:
            for x in adj[st.pop()]:
                if x not in out:
                    out.add(x)
                    st.append(x)
        return out

    for tag, edges in (("BEFORE", req), ("AFTER ", req2)):
        rev, fwd = defaultdict(list), defaultdict(list)
        for u, v in edges:
            rev[v].append(u)
            fwd[u].append(v)
        anc = closure("mca_safe", rev)
        des = closure("mca_safe", fwd)
        evpar = {u for u, v in ev if v == "mca_safe"}
        rhbc = "rate_half_band_closure"
        ok = rhbc in anc or rhbc in evpar or rhbc in des
        print(f"[{tag}] check-3 for (mca_safe, {rhbc}): "
              f"ancestor={rhbc in anc} ev-parent={rhbc in evpar} "
              f"descendant={rhbc in des} -> {'benign' if ok else 'FIRES'}")


if __name__ == "__main__":
    main()
