#!/usr/bin/env python3
"""Fail-closed check of the C3-3 result (2026-07-26): the math orbit's
CONDITIONALs carry ZERO independent mathematical work.

Claim, in three parts, all pinned here:

  1. Granting every math-orbit TARGET discharges EVERY math-orbit CONDITIONAL by
     pure gate propagation (all req-parents discharged), reaching a fixpoint in a
     pinned number of rounds.
  2. No math-orbit CONDITIONAL has an open req-parent OUTSIDE the math orbit, so
     nothing off-orbit is hiding in the propagation.
  3. Every open node NAMED in a CONDITIONAL's own prose is an ancestor (a wired
     hypothesis), an ev-parent (wired evidence), or a descendant (a benign
     consumer back-reference) -- EXCEPT for a pinned list of 12 mentions, each
     audited 2026-07-26 and found explicitly fenced as non-consumed, historical,
     or parenthetical.  A NEW unrelated mention fails this check and forces a
     re-audit, because that is exactly how an unwired hypothesis would appear.

Consequence: the remaining mathematics of the math orbit is exactly its TARGETs.
The Convergence Ledger's "Definition of DONE" second conjunct ("41 CONDITIONALs
discharged against a deduped joint hypothesis set") is IMPLIED by the first on our
side of the tree -- there is no separate hypothesis set of ours left to dedup.

If a count legitimately moves, widen the pin with a dated comment; never delete an
assert to get green.
"""

from __future__ import annotations

import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GRANDS = {"mca_grand", "list_grand"}
# WAVE-24 (2026-07-27) re-pricing after the proof_sketch re-grade: 23 -> 24 TARGETs
# (unsafe_crossing_family_instantiation), 36 -> 38 CONDITIONALs (the demoted cluster).
# WAVE-26 repaired averaged_xr and restored xr_gvn as the unresolved TARGET.
# 2026-08-02 Route T added xr_graded_tangent_band_charge: 24 -> 25 TARGETs.
# 2026-08-03 SL-2 decomposition moved that parent to CONDITIONAL and replaced
# it with one exact TARGET leaf: targets stay 25, conditionals 38 -> 39.
# The round-12 maximality correction wraps that leaf in the exact locator
# residual: targets stay 25, conditionals 39 -> 40.
# The joint-rank split replaces that residual TARGET by an amber router over
# two exact leaves: targets 25 -> 26, conditionals 40 -> 41.
# The later F2 and direct-SP scope repairs removed stale conditional ancestry.
# 2026-08-07 Conjecture-F false-green repair adds three TARGETs and restores
# four parents to CONDITIONAL; the longer chain adds one propagation round.
# The consumer-scope decomposition then replaces one scope TARGET by one
# narrower LIST TARGET, one proved SPI descriptor, and one CONDITIONAL
# compiler: TARGETs stay 28 and CONDITIONALs rise by one.
# LIST route retirement then removes the detached general-F ancestry and adds
# the direct FPC5 leaf: 26 TARGETs, 34 CONDITIONALs, and one fewer propagation
# round.
EXPECTED_TARGETS = 26
EXPECTED_CONDITIONALS = 34
EXPECTED_ROUNDS = 8

# Audited 2026-07-26.  Each entry: (conditional, mentioned open node, why benign).
AUDITED_UNRELATED = {
    ("aperiodic_zero_at_crossing", "rate_half_band_closure"),
    ("knife_edge_census", "census_dodge_selection"),
    ("list_adjacency_closing", "ww_row_envelope_clause"),
    ("list_grand", "rate_half_band_closure"),
    ("xr_clean_residual_any_gate", "rigidity_kernel"),
    ("xr_smallcore_spread_count", "rigidity_kernel"),
    ("xr_smallcore_spread_count", "rk_rigidity_kernel"),
    ("xr_smallcore_spread_count", "shared_census_kernel"),
}

errors: list[str] = []


def check(cond: bool, msg: str) -> None:
    if not cond:
        errors.append(msg)


def closure(seed: str, adj: dict) -> set:
    out, st = set(), [seed]
    while st:
        for x in adj[st.pop()]:
            if x not in out:
                out.add(x)
                st.append(x)
    return out


def main() -> int:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {n["id"]: n for n in dag["nodes"]}
    rev, fwd = defaultdict(list), defaultdict(list)
    for e in dag["edges"]:
        if e.get("kind", "req") == "req":
            rev[e["to"]].append(e["from"])
            fwd[e["from"]].append(e["to"])
    evrev = defaultdict(set)
    for e in dag["edges"]:
        if e.get("kind") == "ev":
            evrev[e["to"]].add(e["from"])

    crit = set(g for g in GRANDS if g in nodes)
    st = list(crit)
    while st:
        for u in rev[st.pop()]:
            if u not in crit:
                crit.add(u)
                st.append(u)
    alt = [(e["from"], e["to"]) for e in dag["edges"] if e.get("kind") == "alt"]
    grew = True
    while grew:
        grew = False
        for u, v in alt:
            if (v in crit and u not in crit
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

    targets = sorted(i for i in crit if nodes[i]["status"] == "TARGET")
    conds = sorted(i for i in crit if nodes[i]["status"] == "CONDITIONAL")
    check(len(targets) == EXPECTED_TARGETS, f"TARGET count drift: {len(targets)}")
    check(len(conds) == EXPECTED_CONDITIONALS, f"CONDITIONAL count drift: {len(conds)}")

    # --- 1. propagation ---------------------------------------------------
    discharged = {i for i in crit if nodes[i]["status"] == "PROVED"} | set(targets)
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
    check(not stuck, f"CONDITIONALs NOT discharged by propagation: {stuck} "
                     "-- these carry independent work and the C3-3 result is void")
    check(rounds == EXPECTED_ROUNDS, f"propagation round count drift: {rounds}")

    # --- 2. no off-orbit open blocker -------------------------------------
    external = sorted({(i, p) for i in conds for p in rev[i]
                       if p not in crit and nodes[p]["status"] != "PROVED"})
    check(not external, f"math CONDITIONAL blocked from off-orbit: {external}")

    # --- 3. unwired-hypothesis audit --------------------------------------
    found = set()
    for i in conds:
        anc, des = closure(i, rev), closure(i, fwd)
        folder = next((ROOT / t / "nodes" / i for t in ("critical", "background")
                       if (ROOT / t / "nodes" / i).is_dir()), None)
        text = (nodes[i].get("statement") or "") + " " + (nodes[i].get("notes") or "")
        if folder is not None:
            cf = folder / "conditional.md"
            if cf.is_file():
                text += " " + cf.read_text(errors="replace")
        for t in {m for m in re.findall(r"\b[a-z][a-z0-9_]{6,}\b", text) if m in nodes}:
            if t == i or nodes[t]["status"] == "PROVED":
                continue
            if t in anc or t in evrev[i] or t in des:
                continue
            found.add((i, t))
    new = sorted(found - AUDITED_UNRELATED)
    gone = sorted(AUDITED_UNRELATED - found)
    check(not new, f"NEW unrelated open mention(s) in a CONDITIONAL's prose: {new} "
                   "-- re-audit: this is how an unwired hypothesis appears")
    check(not gone, f"audited unrelated mention(s) vanished: {gone} -- refresh the pin")

    if errors:
        for e in errors:
            print("FAIL:", e)
        return 1

    print(
        "CONDITIONAL_PROPAGATION_PASS "
        f"targets={len(targets)} conditionals={len(conds)} "
        f"discharged_by_propagation={len(conds)}/{len(conds)} rounds={rounds} "
        f"offorbit_blockers=0 audited_unrelated_mentions={len(AUDITED_UNRELATED)} "
        "=> remaining mathematics = the TARGETs alone"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
