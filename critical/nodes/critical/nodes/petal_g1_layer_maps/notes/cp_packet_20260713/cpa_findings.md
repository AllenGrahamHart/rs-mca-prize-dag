# cpa_findings — fresh-context ADVERSARIAL AUDIT of cp_packet_20260713
# (clause (P) of petal_g1_layer_maps). 2026-07-13.
# Catches numbered cpa-C# (LOCAL numbers; banking session assigns globals).
# Companions: cpa_report.md (verdict + link table), cpa_checks.py
# (independent battery, 6 stages, 37 PASS 0 FAIL, all ramguard tiny).

## VERDICT: SOUND (see cpa_report.md)

No blocking finding. No mathematical defect found anywhere in the packet.
Two cosmetic wording/hygiene repairs (cpa-C1, cpa-C2) and two dag-side
annotations for the banking surgery (cpa-C4, plus confirmation that the
packet's own surgery item 3 is genuinely needed). Every load-bearing claim
was re-derived by hand and re-verified with independently written
machinery (different census method, different interpolation, different
lift test) — all packet numbers reproduce exactly.

## Context established (read-only)

- Packet: critical/nodes/petal_g1_layer_maps/notes/cp_packet_20260713/.
- Operative posing: notes/bsr_repose_20260713/bsr_g1prime_statement.md
  CLAUSE (P) + BAND PIN (#145); audit record bsra_findings.md (#150-#155);
  dag.json petal_g1_layer_maps statement (surgery block of 2026-07-13).
- cp_verify.py replayed end-to-end under ramguard tiny: 59 PASS 0 FAIL,
  matching the packet's record line for line (10-class complete census at
  (16,8,97); 83/67/63 at the three 32-cells; 51 contributors / 0 floor at
  (16,4,97); worst budget margin 2^12 at s=3; binding-row margin 2^88;
  M1-M4 all trip with the packet's printed numbers).
- Consumers read: petal_growth dag statement + conditional.md (pin P1:
  "the floor's band is d >= M(t-2), t = petal count" — the fixed-layout
  band), petal_k4_primitive_bound (PROVED, chart-level m+1),
  petal_small_scale_staircase_census (PROVED; periodic branch, COL-priced,
  layout-free support-size band {k+2, k+4}).
- bsr_check.py n_floor loop (lines 325-338) read: it tallies floor-band
  membership ONLY over odd_wide (the odd-lift family) — the banked
  53/48/8 floor pins are LIFT-ONLY counts, exactly as cp catch #170 says.
- g1a_findings.md headline read: the #138 falsification mass is the
  periodic (scale >= 2) band family at descended charts; the P3-curse
  (#139) is the reading-A ell' = 1 one-member-per-chart phenomenon — the
  packet's "why the curse does not bind here" remark is faithful.

## Independent verification highlights (cpa_checks.py, 37 PASS 0 FAIL)

- A1: boundary/emptiness arithmetic re-derived; official rows n=2^42..44
  have J = -(2^41-3), -(6*2^40-3), -(14*2^40-3) < 0; rate-1/2 J == 3 for
  all s; rates <= 1/4 empty for all s = 13..44; the 2k = n-2 boundary cell
  is parity-impossible on even-k 2-power rows (s = 3..24 exhaustive).
- A1 (the boundary dispute, RESOLVED): at the OUT-OF-SCOPE cell (10,4)
  (even k, 2k = n-2) the packet's operational law (t_ch = (n-k)/2, floor
  band nonempty, J = 1, z0 = 0) and bsra's printed law ("z0 >= 0 <=>
  2k >= n-1", predicting empty) genuinely disagree — and IN VIVO at
  (10,4,11,consec) THREE aperiodic floor-band full-petal lifts realize.
  The packet's Lemma A remark (catch #169 boundary note) is CORRECT;
  bsra's printed constant is a half-integer-formalization artifact (its
  t_ch = (n-k+1)/2 is the odd-k petal count, not the even-k one, which I
  re-derived from the layout construction). In scope both collapse to
  2k >= n — immaterial, exactly as the packet says.
- A2: Lemma B verified EXHAUSTIVELY as pure combinatorics over 1770
  layout shapes (n <= 64, any k parity, b0 <= 1): zero violations of
  j <= J, m in {t-1, t}; the corner (j = J, m = t-1, s_r = 0) sits at
  |S| = k+1 exactly in every shape (identity J + 2(t-1) = k+1 — the
  bounds are sharp, no off-by-one anywhere); the m = t-2 stratum is
  arithmetically impossible (max reach k + b0 - 1 < k+1).
- A3: exact bigint, own code: N_max <= (121/128) n^6 at every rate-1/2
  row s = 3..44 (worst margin 2^12 at s = 3); binding row n = 2^41:
  log2 N_max = 157.4150, log2 budget = 245.9189, margin = 88.5038 (the
  packet's 157.42 / 245.92 / 88.50 exact to 2 d.p.); N_max/(n^4/96) =
  1.0000; (128,64): N_max = 2,754,048, #153 caps 993 + 31 = 1024 embed;
  kill arithmetic C(63,32) = 2^59.6686 > (121/128)128^6 = 2^41.9189.
- A4: INDEPENDENT complete census at (16,8,97,consec) via the k-SUBSET
  method (packet used (k+1)-subsets), Lagrange-only interpolation, and a
  FUNCTIONAL lift test ((x+a)f(x) + (x-a)f(-x) = 0 on H, derived
  independently): 130 classes total, floor census 10 = 8 lifts + 1
  accidental + 1 periodic (the #170 split), rigidity clean, atlas
  coverage clean, per-chart max 3 <= 5, both strata m in {3,4} and both
  retained flavors s_r in {0,1} realized. (16,4,97): 51 classes, floor
  EMPTY (both packet numbers).
- A5: independent audit at (32,16,97,geom5): census 83 = 53 lifts + 30
  accidental + 0 periodic; quotient-side lift recount (6435 independent
  interpolations) agrees set-exactly with the candidate-side lift set;
  per-chart max 8 <= 9 over 38 charts; N_max = 10368.
- A6: three NEW auditor-designed mutations, all REQUIRED-TO-TRIP, all
  trip: NM1 (j-bound tightened to J-1: 8 realized classes at j = 3 —
  the J boundary is exercised from below), NM2 (dropping the m = t
  stratum undercounts 9 < 10 — complement of packet M2), NM3 (mutant
  atlas index |D0| >= thr+2 leaves 9 realized classes uncovered — the
  coverage check acquires discriminating power the packet's tautological
  P1 version lacks, see cpa-C1).

## CATCHES

- **cpa-C1 (cosmetic — verifier hygiene, cp_verify.py stage P1).** The
  two P1 "atlas" checks are tautological: "P1 atlas coverage: every
  class's (D0,R) chart is in the index" tests d >= 2(t-2) on rows that
  floor_split ALREADY filtered by d >= 2(t-2) (the check cannot fail),
  and "P1 atlas chart legality" is only emitted when it fails (silent
  PASS, contributes no line). Neither can produce a false PASS on a
  broken atlas because the atlas is definitional — but per the #137
  discipline these two PASS lines carry no discriminating power. Repair:
  replace with a mutation-style coverage check (cpa_checks.py NM3 is a
  drop-in: a thr+2 index must fail coverage, and does, 9 classes).
- **cpa-C2 (cosmetic — evidence-labelling overstatement, cp_findings.md
  / cp_report.md).** cp_findings #168 says "all 5967 realized |S| = k+1
  lifts are re-basable (cp_verify P6/M4)". cp_verify P6/M4 checks
  n_rebasable > 0 and re-bases ONE witness (z = 7, d = 0 -> d* = 14);
  the universal claim rests on the spare-fiber counting in cp_proof
  section 5 (at rate 1/2 the spare-fiber count is exactly k'-1 — the
  arithmetic is airtight; I re-derived it), not on the verifier. Repair:
  relabel the evidence "arithmetic + one in-vivo witness"; or loop the
  re-basing over all 5967 (cheap). No mathematical content at risk.
- **cpa-C3 (observation — a narrow per-cell fail-open window, cp_verify
  stage P3b).** The never-banked cell (32,16,257) asserts census
  nonemptiness but has no nonemptiness assertion on the LIFT subfamily;
  if quotient_lift_census silently returned empty there, "lift censuses
  agree" could pass vacuously at that cell (P2/P3a's pins 53/48 guard the
  shared code path globally, so this is a per-cell window only).
  Suggested: add `len(lifts) > 0` at P3b.
- **cpa-C4 (repair — dag-side text annotation; sharpens the packet's own
  #169 remark and surgery item 3).** The CURRENT dag.json
  petal_g1_layer_maps surgery block prints "structural law z0 >= 0 <=>
  2k >= n-1, verified across all shapes" (bsra's constant). The
  operational-t_ch truth is 2k >= n-2, and the two genuinely diverge out
  of scope: at (10,4,11) — 2k = n-2 — the printed law predicts an empty
  floor band while THREE aperiodic floor-band full-petal lifts realize
  in vivo (cpa_checks A1). In scope (even-k 2-power rows) both collapse
  to 2k >= n (parity; verified exhaustively s = 3..24). When the banking
  session folds cp_statement into the node, the "2k >= n-1" print should
  be corrected (or annotated) alongside the packet's surgery item 3 on
  the #153 line, so the node text is not internally inconsistent with
  the new (P-i). bsra_findings.md itself can take a one-line annotation
  in the house style (cf. the #155 annotation already appended there).
  Also confirmed: NO other dag node cites the #153 cap as a full-band
  account (the only other "#153" in dag.json is the unrelated "envelope"
  node title, a WP-numbering reference, not the catch); the packet's
  surgery item 3 (relabel the cap LIFT-ONLY, full-band = the rigidity
  census) is needed exactly at the G1 statement line and nowhere else.
- **cpa-C5 (observation — scope mass, quantifies the declared scope-out).**
  At (16,8,97) the floor band holds 53 contributors, of which only 10
  are full-petal: the mixed-petal floor-band mass (43 classes) is 4x the
  full-petal one at the smallest cell. Mixed-petal is EXPLICITLY outside
  clause (P) and outside petal_growth's top-band obligation ("mixed-petal
  and below-top are separate obligations, untouched" — dag statement), so
  nothing is falsified and nothing is silently dropped; recorded so the
  banking session sees the declared-out mass is not small. Consistent
  with cp_proof section 6's non-claims.

## Fidelity findings (no catch needed — verified faithful)

- **#168 consumer-semantics check (the mission's CRITICAL item):** the
  consumers need the LAYOUT-ANCHORED reading and only that.
  petal_growth/conditional.md pin P1 defines the band against THE layout
  ("t = petal count" of the carried layout); the dag petal_growth
  statement's "top-defect band d >= M(t-2)" is the same fixed-layout
  band; K4 is chart-level (the atlas charts satisfy its hypotheses:
  m_chi = t_ch, d >= 2(t_ch-2), |R0| <= 1 < 2); the census gate consumes
  the support-size band {k+2, k+4} via COL/clause (D) — layout-free. NO
  consumer statement reads the band layout-existentially. The packet's
  constructive refutation of the existential reading (tailored-layout
  re-basing) is verified: kill arithmetic exact (A3), witness re-basing
  replayed (cp_verify P6/M4). BANKING CONDITION: the #168 pin must land
  in the dag statement text (the packet's surgery item 1 does this) —
  without the pin the clause is ambiguous and one disambiguation is
  FALSE.
- **#171 below-top honesty flag:** faithful. The wide-minus-floor
  full-petal lift mass (d < 2(t_ch-2), |S| = k+1) is below-top under the
  floor posing; petal_growth's below-top evidence (76-row Lemma-13 scan,
  "max exact count 1") is a per-chart metric that neither prices nor
  contradicts a ~2^59.67 family spread over ~C(t,m) charts. The
  obligation gap is real, correctly attributed, and pre-registered as
  the P1 maintainer item. Not a defect of clause (P) as posed.
- **#170 lift-only recalibration:** confirmed at the source (bsr_check
  n_floor tallies odd_wide only) and by my independent censuses (A4/A5:
  full floor censuses 10/83 vs lift parts 8/53). The banked pins were
  correct AS lift counts; the packet's full-band rigidity census is the
  first full-band account. A cap-sized atlas would indeed undercover
  (83 > 57 + 7 = 64 at (32,16,97)).
- **#138/#139 consistency:** the periodic floor-band mass is measured
  0/1/0 at the three 32-cells (my A5: 0 at (32,16,97)); nothing in the
  packet rests on "never" — periodic classes are inside N_max anyway.
  The P3-curse non-binding remark matches the g1a source (curse lives at
  ell' = 1 reading-A descended charts; these are ell = 2 official charts
  holding up to t_ch + 1 classes — measured max 8).

## DEFERRED

None. Every check fit ramguard tiny (largest single stage ~15 s); Modal
was not needed.
