#!/usr/bin/env python3
"""Fail-closed reconciliation of the two critical-orbit censuses (Q0, 2026-07-26).

The repo carries TWO orbits, both correct, computed from different roots. They
were confused for one number, and the Convergence Ledger r1 header wrongly
declared one of them "stale". This verifier pins both and their exact delta so
the confusion cannot silently return.

  MATH ORBIT      req-ancestry (+ the alt-closure rule) of the two grand-challenge
                  nodes {mca_grand, list_grand}.  239 = 167 PROVED / 40 CONDITIONAL
                  / 32 TARGET.  This is what orbit/critical_dag.json, the radial
                  SVG, the published site, the partition law in verify_prize_dag.py,
                  and verify_critical_harness_coverage.py all measure.  Its 32
                  TARGETs are the mathematical leaves of the roadmap.

  SUBMISSION ORBIT  the same closure rooted at `prize`.  254 = 179 / 42 / 33.
                  Strict superset: MATH ORBIT + 15 packaging/bridge/Lean-harness
                  nodes (12 PROVED, 2 CONDITIONAL, 1 TARGET), enumerated below.
                  This is the Convergence Ledger's baseline and equals the
                  dominator set printed by verify_prize_dag.py's every-route
                  analysis (33 open dominators == the 33 submission-orbit TARGETs).

Neither census is stale; 254 - 239 = 15 is definitional, not drift. Consumers must
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
# 2026-08-06 F2 ADMISSIBILITY REPAIR (6ab149e67): the old growing-order
# Myerson ladder was removed from the strict critical orbit because it proves a
# generated-field-guarded full-subset statement, not the official exact-slice
# consumer. This removes five PROVED nodes, one CONDITIONAL, and one TARGET,
# while the independently proved WCL (1,5) closure adds two PROVED nodes and
# removes one TARGET. Net from the prior pin: -3 PROVED / -1 CONDITIONAL /
# -1 TARGET. The 15-node submission spine is unchanged.
# 2026-08-06 EXACT-PREFIX CONSUMER REPAIR: u2c_giant_tnull_dichotomy was
# removed from the strict x4 chain after the locator-prefix scope theorem
# showed that its p-free/null census does not control the heaviest full prefix.
# The corrected maximum-prefix TARGET replaces it at the same leaf position;
# only the obsolete CONDITIONAL adapter leaves each orbit. The submission
# spine remains exactly 15 nodes.
# 2026-08-06 X4 OWNERSHIP REPAIR: the maximum-prefix leaf had conflated the
# structured moment/null pullback population with the primitive star-PTE
# residue, and the x4 amber silently reused MCA budget arithmetic. Two genuine
# list-side leaves are now explicit: primitive-star-to-u1 coverage and the
# summed per-word numerator. Net: +2 TARGET in both orbits; no theorem status
# changed and the 15-node submission spine is unchanged.
# 2026-08-06 DIRECT PRIMITIVE-SP RE-POSE: the exact-list consumer now
# requires the direct local general-star budget, matching upstream v13's SP
# input. The stronger F-4 minimalization/u1 route remains evidence rather
# than a mandatory requirement. Its detached ancestry contains five PROVED,
# five CONDITIONAL, and two TARGET nodes. The direct primitive leaf itself
# remains TARGET, and the 15-node submission spine is unchanged.
# 2026-08-07 CONJECTURE-F FALSE-GREEN REPAIR: two hidden assertions are now
# explicit TARGET leaves (higher-weight Face-4 payment, absolute-exponent
# packing, and the actual prize-consumer flat-scope compiler). Their four
# auto-discharged ancestors return from PROVED to CONDITIONAL. Net:
# -4 PROVED / +4 CONDITIONAL / +3 TARGET in both orbits;
# the 15-node submission spine is unchanged.
# 2026-08-07 CONSUMER-SCOPE DECOMPOSITION: the scope TARGET becomes a
# CONDITIONAL compiler over one narrower LIST TARGET and one proved exact SPI
# slope-fiber descriptor. The TARGET count is unchanged; each orbit gains one
# PROVED and one CONDITIONAL node. The submission spine remains 15 nodes.
# 2026-08-07 LIST ROUTE RETIREMENT: the prose-only conj_f edge from imgfib
# is replaced by the exact direct FPC5 payment leaf. The 26-node general-F
# branch (18 PROVED / 5 CONDITIONAL / 3 TARGET) leaves strict prize ancestry;
# the new FPC5 TARGET enters. Net in both orbits: -18 PROVED,
# -5 CONDITIONAL, -2 TARGET. The 15-node submission spine is unchanged.
# 2026-08-07 FPC5 OFFICIAL-CELL DECOMPOSITION: the broad FPC5 TARGET becomes
# a CONDITIONAL over three direct payment leaves. Fifteen already-proved PMA
# reduction nodes become strict suppliers. Net in both orbits:
# +15 PROVED, +1 CONDITIONAL, +2 TARGET; submission spine unchanged.
# The M=4,t=2 rate split then proves rate quarter by first-layout pair
# uniqueness and leaves one exact rate-half child. The parent TARGET becomes
# CONDITIONAL; first-layout domination and the new payment enter strict
# ancestry. Net: +2 PROVED, +1 CONDITIONAL, TARGET count unchanged.
# WAVE-48 INTEGRATION (2026-08-07, coordinator-verified): the Conjecture-F
# false-green repair (4 demotions verified against canonical texts) + LIST
# route retirement -> FPC5 program on critical. Orbit shrinks 247 -> 231
# (the retired conj_f subtree leaves via background); reds 25 -> 28 (the
# three FPC5 payment leaves replace broad flatness assumptions). Recomputed
# and pinned by the coordinator at the merge; audit:
# notes/wave24_integration_20260727/WAVE48_AUDIT_DRAFT.md.
# BAND DECOMPOSITION (2026-08-09, user-directed; plan
# notes/band_decomposition_plan_20260809.md, executed at the round-27
# bank): rate_half_band_closure TARGET -> CONDITIONAL (gate all) over
# two NEW critical TARGET children (rate_half_band_structural_surplus =
# the K3/workboard arm; rate_half_band_crossing_location = the RH-AC
# pose adopted from the round-27 draft). Orbit grows 231 -> 233; reds
# 28 -> 29 (net +1: the parent leaves the red count, two children
# enter). Recomputed and pinned by the coordinator at the surgery;
# audit trail: the four round-27 FABLE_AUDITs + the ledger
# "ROUND 27" entries.
# K3 PAYMENT DECOMPOSITION (2026-08-10): the structural-surplus TARGET becomes
# CONDITIONAL over an exact K3 ledger and independent review. The ledger is a
# CONDITIONAL composition over the positive-payment CONDITIONAL, orientation
# assembly TARGET, and exact allocation TARGET; the positive payment depends on
# the eleven-route TARGET. Net from the band pin: +3 TARGET / +3 CONDITIONAL.
# Proved raw workboard packets remain evidence-only and off strict ancestry.
# F2/F3 RULING (2026-08-10, user-delegated, round-30 seam hunt): the K3 arm
# (rate_half_band_structural_surplus) demoted req -> ev on rate_half_band_closure
# per the standing WP5 adjudication ("an ev-edge upgrade, not an amber") — the
# arm is an exhibit-scoped n=2^21 certificate serving no consumer bar. The
# partition law then moves the 7-node K3 subtree (structural_surplus + ledger +
# allocation + independent_review + orientation_assembly + complete_payment +
# remaining_route_payment; 3 CONDITIONAL / 4 TARGET) out of the critical orbit
# to background. The K3 program itself continues unchanged (Codex lane);
# re-promotion pre-registered on bridge + labels-to-slopes + row transport.
# Net from the wave-55 pin: -3 CONDITIONAL / -4 TARGET on both censuses.
EXPECTED_MATH = {"PROVED": 167, "CONDITIONAL": 37, "TARGET": 28}
EXPECTED_SUBMISSION = {"PROVED": 179, "CONDITIONAL": 39, "TARGET": 29}

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
    # submission conditional ledger over 42 must account for 40 mathematical ones.
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
