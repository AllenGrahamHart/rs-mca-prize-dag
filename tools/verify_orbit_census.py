#!/usr/bin/env python3
"""Fail-closed reconciliation of the two critical-orbit censuses (Q0, 2026-07-26).

The repo carries TWO orbits, both correct, computed from different roots. They
were confused for one number, and the Convergence Ledger r1 header wrongly
declared one of them "stale". This verifier pins both and their exact delta so
the confusion cannot silently return.

  MATH ORBIT      req-ancestry (+ the alt-closure rule) of the two grand-challenge
                  nodes {mca_grand, list_grand}.  246 = 179 PROVED / 41 CONDITIONAL
                  / 26 TARGET.  This is what orbit/critical_dag.json, the radial
                  SVG, the published site, the partition law in verify_prize_dag.py,
                  and verify_critical_harness_coverage.py all measure.  Its 26
                  TARGETs are the mathematical leaves of the roadmap.

  SUBMISSION ORBIT  the same closure rooted at `prize`.  261 = 191 / 43 / 27.
                  Strict superset: MATH ORBIT + 15 packaging/bridge/Lean-harness
                  nodes (12 PROVED, 2 CONDITIONAL, 1 TARGET), enumerated below.
                  This is the Convergence Ledger's baseline and equals the
                  dominator set printed by verify_prize_dag.py's every-route
                  analysis (26 open dominators == the 26 submission-orbit TARGETs).

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

# Q0 census, 2026-07-26, at prize master dd9b862d (dag.json: 1222 nodes).
# REPRICED 2026-07-27 (wave-24 Codex integration): the e1 chain + zone_b/mca_unsafe/
# unsafe_at_crossing were demoted after the proof_sketch re-grade proved the cited
# sections say CONJECTURAL / typicality, not PROVED (notes/PROOF_SKETCH_PROVENANCE.md).
# Was 201/36/23 (260); the demotions also drop 19 e1 nodes off the critical path.
# 2026-07-27 (sketch-tagged re-grade): averaged_xr was a FALSE GREEN (no conditional.md;
# its sole req PRESUPPOSED the claim; own sketch.md said PROVABLE; source says only
# "looks provable") -> TARGET, cascading averaged_slope_conversion / xr_gvn /
# averaged_occupancy_... -> CONDITIONAL. Was 180/38/24.
# WAVE-26 (2026-07-27): averaged_xr CLOSED — Codex rederived Przemek's own exact
# fixed-slope pair moment (m1_average_support_collinearity.md @674503f7) and replayed
# it with an independent verifier, so the false green became a real one; the two
# cascade nodes returned to PROVED. xr_gvn went the other way (CONDITIONAL -> TARGET):
# the exact moment does NOT supply its multi-exchange Cauchy-Schwarz chain, so that
# edge is evidence-only. Net: reds 25 -> 24. Was 177/39/25.
# ROUTE-T REPRICE (2026-08-02, coordinated edit f72ca9e5): the new
# xr_graded_tangent_band_charge TARGET is a mathematical leaf.  The unchanged
# 15-node submission spine therefore raises both orbit TARGET counts by one.
# SL-2 DECOMPOSITION (2026-08-03): the monolithic Route-T target becomes
# CONDITIONAL on one new TARGET leaf. The proved reduction is evidence-only and
# remains off-orbit. This adds one CONDITIONAL while preserving 25 TARGETs.
# ROUND-12 MAXIMALITY CORRECTION: SL-2 becomes CONDITIONAL on the exact
# maximal selected locator residual. Two new proved coordinate nodes are
# evidence-only, so this again adds one CONDITIONAL and preserves the leaves.
# 2026-08-03 JOINT-RANK SPLIT: the maximal-locator residual becomes
# CONDITIONAL on two alternative TARGET leaves (full joint rank and deficient
# forced-common-root kernel). The rational-direction payment is evidence-only.
# Net: +1 CONDITIONAL and +1 TARGET in both orbits.
EXPECTED_MATH = {"PROVED": 181, "CONDITIONAL": 41, "TARGET": 25}
EXPECTED_SUBMISSION = {"PROVED": 193, "CONDITIONAL": 43, "TARGET": 26}

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
# conditional-dedup ledger over the 43 must account for 41 mathematical ones.
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

# WAVE-47 REPRICE (2026-08-07): dli_wcl_slot_1_5_emptiness TARGET -> PROVED
# (Codex proof + auditor Burnside closure of the census trust root, coordinator
# replay); dli_wcl_weight4_ambient_exclusion promoted background -> critical
# (forced by the adopted slot wiring, partition law). 246=179/41/26 -> 247=181/41/25;
# submission 261=191/43/27 -> 262=193/43/26. A RED CLOSED.
