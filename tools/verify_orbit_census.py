#!/usr/bin/env python3
"""Fail-closed reconciliation of the two critical-orbit censuses (Q0, 2026-07-26).

The repo carries TWO orbits, both correct, computed from different roots. They
were confused for one number, and the Convergence Ledger r1 header wrongly
declared one of them "stale". This verifier pins both and their exact delta so
the confusion cannot silently return.

  MATH ORBIT      req-ancestry (+ the alt-closure rule) of the two grand-challenge
                  nodes {mca_grand, list_grand}.  246 = 183 PROVED / 39 CONDITIONAL
                  / 24 TARGET.  This is what orbit/critical_dag.json, the radial
                  SVG, the published site, the partition law in verify_prize_dag.py,
                  and verify_critical_harness_coverage.py all measure.  Its 24
                  TARGETs are the mathematical leaves of the roadmap.

  SUBMISSION ORBIT  the same closure rooted at `prize`.  261 = 195 / 41 / 25.
                  Strict superset: MATH ORBIT + 15 packaging/bridge/Lean-harness
                  nodes (12 PROVED, 2 CONDITIONAL, 1 TARGET), enumerated below.
                  This is the Convergence Ledger's baseline and equals the
                  dominator set printed by verify_prize_dag.py's every-route
                  analysis (25 open dominators == the 25 submission-orbit TARGETs).

Neither census is stale; 261 - 246 = 15 is definitional, not drift. Consumers must
say WHICH orbit they mean. Burn-down of *mathematics* is the math orbit; the
"all-green DAG" end state is the submission orbit (it owns the dossier leaf).

When a count legitimately moves, widen the pin here with a dated comment and fix
the ledger header in the same commit — never delete an assert to get green.
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GRANDS = {"mca_grand", "list_grand"}
SUBMISSION_ROOT = "prize"

# E1 quantifier correction, 2026-07-26. The 14-node quantifier-pin/named-exhibit branch is
# background evidence; one family-uniform E1 TARGET replaces its two exhibit
# leaves on the live route.
EXPECTED_MATH = {"PROVED": 183, "CONDITIONAL": 39, "TARGET": 24}
EXPECTED_SUBMISSION = {"PROVED": 195, "CONDITIONAL": 41, "TARGET": 25}

# The submission spine: exactly the nodes reachable from `prize` but not from the
# grand challenges. Packaging, bridge ledgers, and the Lean/harness rails — no
# mathematical leaf of either prize problem lives here except by a wiring bug,
# which is what pinning this set by name detects.
EXPECTED_DELTA = {
    "bridge_ledger": "PROVED",
    "compiler": "PROVED",
    "dossier_partial": "PROVED",
    "envelope": "PROVED",
    "half_johnson_ca": "PROVED",
    "harness": "PROVED",
    "ld_bridge": "PROVED",
    "ldsw_ld_separation": "PROVED",
    "lean_existing": "PROVED",
    "lean_tier1": "PROVED",
    "mca_from_ca_reduction": "PROVED",
    "packaging": "CONDITIONAL",
    "pinned_row": "PROVED",
    "prize": "CONDITIONAL",
    "submission_quality_paper_dossier": "TARGET",
}

# The one TARGET on the submission spine is packaging, not mathematics: this is
# why the submission orbit has one more TARGET than the mathematical orbit.
NON_MATH_TARGET = "submission_quality_paper_dossier"

# ...and the two CONDITIONALs on the spine are likewise non-mathematical, so a
# conditional-dedup ledger over the 41 must account for 39 mathematical ones.
NON_MATH_CONDITIONALS = {"prize", "packaging"}


def orbit(nodes: dict, edges: list, seeds: set) -> set:
    """Req-ancestry closure of `seeds`, with the alt-closure rule shared by
    build_critical_orbit.py and verify_prize_dag.py's partition law."""
    rev: dict[str, list[str]] = defaultdict(list)
    for e in edges:
        if e.get("kind", "req") == "req":
            rev[e["to"]].append(e["from"])
    alt = [(e["from"], e["to"]) for e in edges if e.get("kind") == "alt"]

    crit = {s for s in seeds if s in nodes}
    stack = list(crit)
    while stack:
        for u in rev[stack.pop()]:
            if u not in crit:
                crit.add(u)
                stack.append(u)
    grew = True
    while grew:
        grew = False
        for u, v in alt:
            if (v in crit and u not in crit
                    and nodes[u]["status"] in ("PROVED", "PROVABLE")
                    and nodes[v].get("gate") == "any"):
                crit.add(u)
                grew = True
                stack = [u]
                while stack:
                    for x in rev[stack.pop()]:
                        if x not in crit:
                            crit.add(x)
                            stack.append(x)
    return crit


def census(nodes: dict, ids: set) -> dict:
    return dict(Counter(nodes[i]["status"] for i in ids))


def main() -> int:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {n["id"]: n for n in dag["nodes"]}
    edges = dag["edges"]
    errors: list[str] = []

    math_ids = orbit(nodes, edges, GRANDS)
    sub_ids = orbit(nodes, edges, {SUBMISSION_ROOT})
    math_census = census(nodes, math_ids)
    sub_census = census(nodes, sub_ids)

    if math_census != EXPECTED_MATH:
        errors.append(f"math-orbit census drift: {math_census} != {EXPECTED_MATH}")
    if sub_census != EXPECTED_SUBMISSION:
        errors.append(f"submission-orbit census drift: {sub_census} != {EXPECTED_SUBMISSION}")

    # Containment is the structural claim: the submission orbit is the math orbit
    # plus packaging. If a grand-challenge ancestor ever escapes the prize orbit,
    # the DAG has a severed route and no census below means anything.
    escaped = sorted(math_ids - sub_ids)
    if escaped:
        errors.append(f"math orbit not contained in submission orbit: {escaped}")

    delta = {i: nodes[i]["status"] for i in sorted(sub_ids - math_ids)}
    if delta != EXPECTED_DELTA:
        added = sorted(set(delta) - set(EXPECTED_DELTA))
        dropped = sorted(set(EXPECTED_DELTA) - set(delta))
        moved = sorted(i for i in set(delta) & set(EXPECTED_DELTA)
                       if delta[i] != EXPECTED_DELTA[i])
        errors.append(
            f"submission-spine drift: added={added} dropped={dropped} status_moved={moved}")

    # The named non-math nodes must actually be the non-math ones on the spine.
    if NON_MATH_TARGET not in delta or delta.get(NON_MATH_TARGET) != "TARGET":
        errors.append(f"{NON_MATH_TARGET} is no longer the submission spine's TARGET")
    spine_conditionals = {i for i, s in delta.items() if s == "CONDITIONAL"}
    if spine_conditionals != NON_MATH_CONDITIONALS:
        errors.append(f"submission-spine CONDITIONALs drift: {sorted(spine_conditionals)}")

    # The roadmap's mathematical-leaf count is an arithmetic consequence,
    # not an independent count: assert it rather than trusting prose.
    math_targets = sorted(i for i in math_ids if nodes[i]["status"] == "TARGET")
    if len(math_targets) != EXPECTED_MATH["TARGET"]:
        errors.append(
            "mathematical-leaf count drift: "
            f"{len(math_targets)} != {EXPECTED_MATH['TARGET']}"
        )
    if NON_MATH_TARGET in math_targets:
        errors.append(f"{NON_MATH_TARGET} leaked into the math orbit")

    # orbit/critical_dag.json is a build product of the math orbit; a stale copy
    # silently republishes wrong counts to the site.
    built = json.loads((ROOT / "orbit" / "critical_dag.json").read_text())
    built_ids = {n["id"] for n in built["nodes"]}
    if built_ids != math_ids:
        errors.append(
            "orbit/critical_dag.json out of sync with dag.json — rerun "
            f"tools/build_critical_orbit.py (only_in_build={sorted(built_ids - math_ids)}, "
            f"only_in_dag={sorted(math_ids - built_ids)})")
    else:
        label_census = dict(Counter(n["label"] for n in built["nodes"]))
        want = {"PROVED": EXPECTED_MATH["PROVED"],
                "CONDITIONAL": EXPECTED_MATH["CONDITIONAL"],
                "UNPROVED": EXPECTED_MATH["TARGET"]}
        if label_census != want:
            errors.append(f"critical_dag.json label drift: {label_census} != {want}")

    if errors:
        for e in errors:
            print("FAIL:", e)
        return 1

    print(
        "ORBIT_CENSUS_PASS "
        f"math={len(math_ids)}({math_census['PROVED']}/{math_census['CONDITIONAL']}/"
        f"{math_census['TARGET']}) "
        f"submission={len(sub_ids)}({sub_census['PROVED']}/{sub_census['CONDITIONAL']}/"
        f"{sub_census['TARGET']}) "
        f"spine={len(delta)} math_leaves={len(math_targets)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
