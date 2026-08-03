# Prize Resolution Roadmap — r3, the date-free plan of record

> **OPERATING PROTOCOL:** The joint end-to-end goal is governed by
> `notes/JOINT_PRIZE_RESOLUTION_PROTOCOL.md`. This roadmap selects strategy;
> the protocol controls proof status, cross-repository custody, PR procedure,
> verification, computation, and the terminal completion audit.

Supersedes r2 and the divergence-era copy (snapshotted at
`notes/roadmap_r3_20260721/PRIZE_RESOLUTION_ROADMAP_pre_r3_snapshot.md`,
custody #104). Derived from the 18-agent review of 2026-07-21
(`notes/roadmap_r3_20260721/` — ROADMAP_R3.md, gap_matrix.md,
technique_dossier.md, completeness_critic.md); every number below survived
its adversarial fact-check. Deliberately DATE-FREE: sequencing is by GATES
(events and conditions), never by calendar. The dated snapshot is archival;
this file is the guide of record and is refreshed at gate events, not on a
clock. This document is not itself a proof and changes no node status.
Node-local `node.json` manifests are the editable graph source;
`dag.json` is their exact generated compatibility view.

Mission: fully resolve both Proximity Prize grand challenges (grand list +
grand MCA), or failing that, land the strongest honest partial posture the
spec's split-award structure supports. Lanes: our proofs; audit-gated Codex
integration; upstream mining/feeding (przchojecki/rs-mca). House laws in
force throughout: one-writer, custody (#104/#155), falsification-first,
compute law + the sub-5-minute self-auth time rule (Decision 5), claim
discipline (never over-claim upstream), forced-corrections authority
boundary. The current local execution envelope is the stricter intersection
of the time and spend limits: a route-deciding job must be conservatively
under five minutes total and under `$1`. Any valuable run above either limit,
with unknown cost, or liable to exhaust the remaining credit is recorded in
`notes/PRIZE_COMPUTE_REQUESTS.md` instead of launched. Every related upstream
PR must carry its live ledger entries in a distinct **Compute requests**
section so contributors with suitable compute can accept a declared budget.

---

## r3.1 GATE-EVENT ADDENDUM (2026-08-02): the pilot-campaign re-statement

The 32-pilot Opus campaign (six rounds, all coordinator-replayed before
banking; ledger `notes/pilots_20260802/CAMPAIGN_LEDGER.md`) plus the four
user ratifications re-shape the board. This addendum supersedes conflicting
track wordings below until the next full revision; census after the
coordinated-edit bundle (f72ca9e5): **math orbit 242 = 179/38/25**;
workflow of record: Fable (coordinator/auditor) + Opus pilots + Codex
worker; **Pro PAUSED** — former Pro asks run as internal adversarial
pilots with pre-registered kill lines; the user ratifies surfaced
decisions.

**The four ratifications (2026-08-02, all executed):** (1) band repair =
ROUTE T, a third generic column from the 13n^3 headroom, with d = h-1
folded in as a NAMED cascade tier of the band column [1, h-1] — executed
as the R2 three-way partition of record (band column | P-A1 exact-k
unchanged | P-B) + the new red TARGET `xr_graded_tangent_band_charge`
(<= 4n^3; B_tan untouched; 8n^3 never split); (2) PP4.0 =
compression-order class (lex canonical); (3) q-scope: (P1)
family-uniform governs the ultimate claim (the RowC 1/4 window obligation
was subsequently DISCHARGED — vacuous under the q-floor, rowc_window V1);
(4) PP5.0 working budget = 1/43.

**The seven hearts (what actually remains, per lane):**
1. **Band/occupancy** (the new TARGET's single open input): purely
   combinatorial escape form — "every ray support has >= 2 points in <= 2
   supports" implies occupancy; sub-items: zero-escape collapse
   (rank = 2m), V <= m/2 for non-collapsing systems. Definitions of
   record: `notes/BAND_LANE_DEFINITIONS.md`.
2. **P-A1 exact-k**: the peeling residual |K| (peeling lemma +
   locality-death law give the linear head (2R-1)/h + |K|).
3. **P-B**: adversarial planting only (field hypothesis NECESSARY;
   random side CLOSED by the q-floor; selector clause couples to PP4.0).
4. **F2**: the K1 mass obligations (O1)-(O3) (fixed-sector absorption
   REFUTED; antipodal descent lemma; (H-flat*) scope = generic
   frequencies) + the PP5.0 freeze.
5. **C1/C2'' (merged at junction 0)**: sparse v_2-aware certificates /
   count bounds (lattice route DECIDED dead; norm-gate package MINTED —
   4 background nodes, 4d546956; WCL fence = candidate fifth node).
6. **Crossing**: the w >= 2 boundary (PK1 proved at w=1, q-free; PK2:
   q-freeness is a w=1 phenomenon; official regime is q-dependent).
7. **Gamma confinement**: closed at j=1 (THEOREM Y + unconditional
   tangent gate); j >= 2 inherits the gate inequality X < 1 — one
   hypothesis, not two.

**Standing next steps (gate-sequenced):** band mint wave line-audit
(pilot drafting; then wire ev into the band TARGET); next pilot-round
anchor = unify |K| with the escape residual (both are covering
conditions on ray systems — likely ONE object); Codex 433-1b completion
from pin 454159b0 by status flow (K3 composition flips
rate_half_band_closure); #1143 export fallback (coordinator packages by
end 2026-08-02, surfaced to the maintainer first).

---
