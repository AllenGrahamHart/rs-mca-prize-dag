# K3/SEM-QBC vs direct S/A/E: route-comparison decision dossier

- **Date:** 2026-08-12, coordinator session; fleet run `wf_ab6718ee-c54`
  (12 agents: 6 extraction, 4 adversarial assessment, judge + critic;
  reports in this directory, `01`-`12`).
- **Question:** which route banks the balanced-core stratum of the
  KoalaBear MCA row — K3 endpoint realization via SEM-QBC/Rec_2_4, or
  the direct same-owner S/A/E whole-line selector?
- **Fleet verdict:** **HYBRID**, medium confidence (`11-judge-verdict.json`).
- **Coordinator adjudication below:** HYBRID **stands**, with the shared
  spine slimmed by one item (see §2). This dossier executes, not
  overrides, the cycle-19 ruling "compare the two routes and pursue the
  shorter bankable theorem" (`notes/work_cycles/roadmap_r3/19-*.md`):
  the probes ARE the comparison; the divergent halves are funded only
  after they run.

## 1. The verdict in brief

Both skeptics independently converged on one claim: the two missing
theorems share a hard kernel (chronology-correct, slope-global,
first-match selection over an executable witness substrate), and the
routes genuinely diverge only at K3's endpoint realization
(no cheap probe; dies late) versus S/A/E's varying-core disjointness
(collision falsifier pre-registered by its own author). Bankability
points opposite ways: K3 flows through our living #1152 export on
uncontested ground; S/A/E deliverables land in Scott's unmerged pr1163
lineage where the forest compiler is pre-registered as HIS next move
(collision precedent: [[rs-mca-m2-export-collision]], the 2026-08-01
order-two collision protocol). Scores and the full argument:
`11-judge-verdict.json`.

## 2. The same-theorem audit (critic gap 2 — BLOCKING; run by the coordinator)

Line-by-line mapping of the WLCS obligations (`03-sae-spec.md` §1,
N1163 §5 blockquote) onto the SEM-QBC/Rec_2_4 conditions
(`01-semqbc-spec.md` §1, #1159 conditions (1)-(6) + (COV)/(FIB)/fence):

| # | SEM-QBC side | WLCS side | verdict |
|---|---|---|---|
| A | S1: executable typed `P_Q`,`P_BC` witness relations | W9: "actual explanation states" defining the input records | **SHARED** — same substrate (cycle-19 compiler); #1159 §5(ii)-(iii) typing/parsing criticisms bind both |
| B | (1) soundness: certificate reconstructs actual witness | selector input soundness | **SHARED** |
| C | (4) K=k+1 prefix envelope <-> deg<k adapter incl. boundary | same substrate at K=k+1=1048577 | **SHARED** — the d1=67473 record adjudicates both |
| D | (FIB): section + exact fiber constants per terminal | "projection fibers and add-back multiplicities in distinct-slope units" | **SHARED** (shape and units identical) |
| E | (6)/fence: route every unrouted BC slope to owner/paid/U_new | T3/T4 residual-label emission, totality | **SHARED SHAPE** — build the routing-table/fence machinery generically, parameterized by cell and residual labels |
| F | (5) support preservation, exact-m subsupport guards | adapter transport invariants (partially PROVED via the #1163 adapter import) | **SHARED**, partially discharged |
| G | (3) slope-global **Q** exclusion | T1 earlier-owner adjudication over the six structural branches (tangent, common-support, quotient, extension, degree-drop, common-GCD) | **SAME SHAPE, DIFFERENT CONTENT** — see below |
| H | (COV) coverage of the frozen (2,4)-slice, anti-tautology | W2 totality over common-core records | divergent content, shared anti-tautology discipline |
| I | End_{2,4} endpoint realization (Q=6,s=6,u=2), conjugacy transport | — | **K3-ONLY** (the T5 hard step) |
| J | — | W4: canonical-core disjoint forest across varying cores | **S/A/E-ONLY** (the L5 hard step) |
| K | K3 allocation arithmetic (the CONDITIONAL ledger nodes) | W8: 31-reserve / eq:owner-target / thm:conditional-final regeneration with 2w | **PARALLEL, not shared** — each route's own global summation |

**Adjudication of judge falsifier 1** ("WLCS can treat Q as a black box
without executable P_Q"): row G shows it fires PARTIALLY. WLCS's T1
list is the six structural branches, not the Q/BC priority map — and
several branches carry banked per-slope theorems (2w translation for
common-support; the `n-a' <= t` tangent guard; thm:global-block), so
WLCS's earlier-owner burden is lighter than SEM-QBC's Q exclusion. The
consequence claimed by the falsifier ("HYBRID loses its justification")
does **not** follow: rows A-F remain consumed verbatim by both routes.
Resolution: **slope-global Q exclusion moves OUT of the shared spine
into the K3 divergent half** (raising its priced depth), and a
"six-branch earlier-owner adjudication table" (mostly assembly of
banked theorems) joins the S/A/E half. HYBRID stands on rows A-F.

## 3. Primary-source check on Jo's transfer (critic gap 3 — NOTE; closed)

`RS_MCA_Paving_v9.2.tex` (pr1163) lines 2255-2309 + 2365-2397 read
directly. `lem:jo-shortening-map` (SH1) and
`thm:jo-shortening-transfer` (SH2) match #1163 §4's reproduction
exactly: multiplier `C(n,t)/C(a,t)` at agreement `a=m`, `t<k` scope,
and the telescoping remark is verbatim ("the two binomial ratios
telescope"). Structural point now primary-source-grounded: Jo shortens
by a CHOSEN set S inside every witness support and pays the double
count; the #1163 adapter cancels the RECORD-INTRINSIC core C
(intersection of maximal supports) and pays none — which is why the
staircase route survives the 3765-bit wall that blocks SH2 at c=4131.

## 4. Remediation of the remaining critic gaps

- **Gap 1 (BLOCKING):** the skeptic and advocate reports the verdict
  cites are banked in this directory (`07`-`10`). Closed.
- **Gap 4 (NOTE):** the "two-witness Q-collision probe" (judge
  falsifier 3) is now DEFINED as probe P4, K3-half, one packet:
  over a small field, attempt to construct one slope carrying both an
  active shifted-lattice BC certificate and a Q-prefix-family witness;
  success without an available priority-repair theorem kills
  slope-global exclusion as posed. Scheduled AFTER the three shared
  probes, only if the K3 half is selected.
- **Gap 5 (NOTE):** R-1 reconciliation stated in the header. Closed.
- **Gap 6a (NOTE):** the `Q2` quadratic cover (guard non-transplant
  residual, #1155: "the correct next obligation" for cell-11 orbit
  closure) is added to the K3 divergent half's price. 6b: K3's
  bankability score note corrected — cell 11 has NO external replay
  (`cell11_complete_exclusion` evidence is internal-only); the two
  exact replays cover cell-5 xi3 and the raw workboard, and the review
  node stays TARGET.
- **Gap 7 (NOTE):** the hedge's coordination protocol is the
  m2-export-collision protocol (memory `rs-mca-m2-export-collision`,
  2026-08-01). Cited.

## 5. The decision instrument (pre-registered)

Three probes, ~3 packets total, jointly decisive; two serve both routes:

- **P1 (S/A/E, decisive for L1):** reserve-arithmetic replay of
  `thm:conditional-final` (GF:7089-7110) + `eq:owner-target`
  (GF:7032-7036) with `2w=134944` replacing `+1`, integer-only under
  ramguard. Outcome prices the chronology regeneration: containment
  theorem vs re-derived target `B_*-134975-(n-g)` vs open-ended
  owner-localization re-derivation (the latter = S/A/E half
  dead-priced per judge falsifier 2).
- **P2 (shared):** boundary-record K-adapter test — hand-adjudicate the
  actual `d1=67473` record (#1159 Thm 4.1) under a candidate
  K=k+1-prefix-to-deg<k adapter. Owner change on the extra interior
  coefficient kills SEM-QBC condition (4) as posed FOR BOTH routes.
- **P3 (shared, mandatory regression):** feed the #1160 67,472-slope
  globally-affine line through the cycle-19 `P_BC` certificate
  relation; any acceptance kills the definition at deployed scale.

Spine work that proceeds regardless (consumed verbatim by either
winner): typed executable `P_BC` (and `P_Q` if the K3 half is chosen)
with a parsing verifier on one actual certificate (fixes #1159
§5(ii)-(iii)); soundness; the K-adapter; the hostile-control
regressions; distinct-slope fiber discipline; generic fence machinery
(row E). Kill conditions for HYBRID itself: judge falsifiers 2-5
(`11-judge-verdict.json`), with falsifier 1 resolved in §2.

## 6. Status

Banked as the comparison instrument. The route COMMITMENT (adopting
HYBRID + probe order) and the hedge (shipping P1's result as a
threshold note into the #1160/#1163 lineage with a coordination ping
to Scott — outward-facing) are surfaced to the user for ratification
per standing rules; no probe has been run and no outward action taken
at banking time.
