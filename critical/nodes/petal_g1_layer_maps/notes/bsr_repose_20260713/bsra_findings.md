# bsra_findings — fresh-context DESIGN AUDIT of the branch-split re-pose packet
# (bsr_repose_20260713; auditor context, 2026-07-13; catch ledger continues from #149)
# Artifacts: bsra_audit.py (independent battery), bsra_fm2.py (repaired FM2),
# bsra_replay_out.txt (bsr_check replay). All runs ramguard tiny.

## VERDICT: SOUND-WITH-REPAIRS
All four load-bearing claims independently verified (chains re-derived from the
banked PROVED nodes, arithmetic recomputed exact, fresh cell + fresh mutations
live). Five repairs, none touching the mathematical core; the most consequential
is a MISSED CONSUMER in the D4 fate audit (#150). Surgery may proceed once the
repairs are folded into the drafts.

## Replay + independent battery results

- bsr_check.py replayed (ramguard tiny): exit 0, 55 PASS, ALL CHECKS PASS —
  matches the packet's banked record, incl. MC1 216 / MC2 350 trips, dominance
  excess 2^-691, ratios 1.000977/1.001955, gate cap exactly 4.0000.
- bsra_audit.py (independent implementation, not derived from bsr_check):
  A1-A9 all confirm; two initial FAILs were MY harness errors (see A1/FM2
  notes below), both resolved.
- FRESH CELL (32,16,193,consec) — unbanked prime AND unbanked smode for the
  shape: S2 identity holds; census nonempty (#137): 56 band classes at a'=9,
  0 at a'=10, 5907 odd lifts; COL cap holds on realized cells ((2,18): 56 <=
  C(16,9)); clause-(D) chain B=56 <= N_DD=56 <= 6435 <= 719*Q at a'=9 (atlas
  SHARP at a fresh cell, consistent with the packet's bonus P4 finding);
  minimal-chart injectivity holds; odd lifts end-to-end verified (aperiodic,
  full-petal, wide-band always); floor-band 48 <= 57+7 (two-family cap, #153);
  wide mass 5907 of supply 6435 — binomial scale at a fresh prime (q-freeness
  in vivo).
- FRESH MUTATION FM1 (#133 made live): layer-normalized labels c_i/(y_i-y_nf)
  break the S2 identity AND shift the census (56 -> 35) — the specific
  plausible implementation error is detected, not just random corruption (MC3).
- FRESH MUTATION FM2 (U1 margin made live): on 3430 synthesized band charts
  with m'=d'+2, the one-unit degree relaxation (deg <= k') admits >= 2 members
  on 3412 charts, while the UNRELAXED U0 line holds <= 1 member on ALL 3430 —
  margin-exactly-1 confirmed in vivo at a fresh cell. (My first FM2 scanned
  only realized-class charts — zero m'=d'+2 classes at the fresh cell — a
  vacuous-harness bug on MY side, repaired by synthesizing charts.)

## CLAIM 1 — LEMMA COL: VERIFIED (theorem; word-free)

Exact consumption chain (re-derived link by link):
1. c(S) = M >= 2  =>  S = union of A/M full M-fibers, empty tail: the
   stabilizer partition theorem, PROVED at petal_g2_support_forcing (FLIP ->
   PROVED 2026-07-12, hand-replayed + exhaustive Z_8/Z_16/Z_32) — the exact
   clause COL(i) cites. NOT the qrl T-lemmas (those are non-load-bearing, as
   the packet says).
2. #classes <= C(n/M, A/M): fiber-union injection — counts ALL possible
   supports, hence word-free (no G1 supply, no chart, no atlas consumed). ✓
3. classes = supports, multiplicity 1: petal_g3_full_support_codeword_
   injectivity (PROVED): |S| = A >= k+1 > deg pins the codeword. ✓
4. Ratio identity C(n',h) = C(n'-1,h) * n'/(n'-h), n'/(n'-h) = n/(n-A):
   verified symbolically over a full sweep (A1) — elementary Pascal. ✓
5. Cap at P1-OWN cells: A_own = M*ceil((k+1)/M) <= k+M (all M, incl. M !| k);
   M <= t => n - A_own >= n-k-t = t (sigma=1) => n/(n-A_own) <= 2/(1-rho)
   <= 4 at rho <= 1/2, UNIFORM IN n. Attained exactly 4 at rho=1/2, M=t.
   Realized per-rate maxima over the official grid: {1/2: 4, 1/4: 2,
   1/8: 4/3, 1/16: 4/3} — the bound is generous below rate 1/2. ✓
6. In-vivo: independent re-sweep (A9) of all 372 banked records x 6 tags
   (514 profile cells): zero COL violations, multiplicity 1 everywhere,
   max classes/Q = 4/3, max support saturation = 2/3 (the (8,3,17) cell:
   4 classes of 6 possible fiber-unions — confirmed on the raw JSON). ✓

What the gate still needs: ONLY the D3/#149 landing (QA.22 M <= t extension
against imgfib's reserve). COL closes the count side unconditionally,
including odd k, all layouts, all band filters at consumed cells. Confirmed.

CATCH #151 (statement repair): COL(v) "M <= t is PRECISELY the nondegeneracy
boundary" is an overstatement — the iff holds only when M | k. Counterexample
(n,k,M) = (32,8,16): M = 16 > t = 12 yet A_own = 16 <= n-M, Q = C(1,1) = 1
nonzero (cap 2). Inside the official grid the same occurs at rho <= 1/4
(e.g. rho=1/16 rows: M = n/2 > t has a nondegenerate own cell, Q != 0).
The LOAD-BEARING direction (every dyadic M <= t own cell nondegenerate) is
TRUE (verified grid-wide, A1) and is all the lemma uses; the above-t
nondegenerate cells belong to the M > t composite anyway. Repair: reword (v)
to "for M | k the boundary is exact; for all M <= t the column is nonzero;
M !| k own cells above t exist and are the composite's".

## CLAIM 2 — CLAUSE (D): VERIFIED (proposed PROVED is justified)

- Coverage: realized band class S' (y_nf in S', |S'| in {k'+1,k'+2}) is
  DD-consistent (its member IS an interpolant); z >= 1 (y_nf in core''
  under reading A); z <= k'-1 (z = k' forces g = 0, |agr| = k' < k'+1 — csp
  U2's empty-chart case); m' = |S'|-z <= d'+2. Legal band chart by
  construction. ✓ (consumes csp Claims audited PACKET-SOUND per
  conditional.md — the exact hypothesis 3-C needed is what (D) supplies.)
- Injectivity: S' = W u P recoverable => distinct classes, distinct charts;
  cardinality consumption needs only this (U1 uniqueness is for the G3
  per-chart structure). ✓
- Cardinality: |A'_{a'}| <= #{a'-supports containing y_nf} = C(n'-1,a'-1). ✓
- Ratio: C(n'-1,a'-1)/C(n'-1,a') = a'/(n'-a'); independent grid recompute
  (A5): max = 2050/2046 = 1.001955 at s=13, rho=1/2, a'=k'+2 — the packet's
  1.00196 claim exact. Even C_col = 2 closes; 719 confirmed = floor(n^6/
  C(n+6,6)) at s = 41..44 (and, FYI, also at s=40 and s=45 — not knife-edge).
- g1a instances recomputed EXACT (A2), all four, with the F4 hypothesis
  q >= 2n'^2 verified per instance (s=13 field 33710081 >= 2*4096^2 —
  barely, and legitimately): old form violated by +52.8 / +3975.0 / +61.3 /
  +181.8 bits (packet's "54" is bit-length rounding of 52.8); column form
  fits with margins 33.5 / 47.0 / 146.5 / 275.5 bits — the stated 33-275-bit
  window is exact. Per-profile caps hold at every instance. ✓
- DD-atlas coverage argument + chain reproduced at the fresh cell (A6). ✓
- Scope honesty: k even / sigma=1 / chart words only — immaterial for the
  gate (COL covers the rest); correctly stated in both drafts. ✓

## CLAIM 3 — CLAUSE (P) POSING / #145: ARITHMETIC VERIFIED

- C(63,32) = 916312070471295267 = 2^59.67 exact; (121/128)*128^6 =
  121*2^35 = 4157528342528 = 2^41.92 exact. The inequality (wide-band
  pre-falsification at (128,64), every q) holds by 17.7 bits. ✓
  CATCH #154a (cosmetic): the packet prints "~2^41.3" (bsr_g1prime_statement,
  bsr_falsifiers via lg_frac bit-length, and the dag.json G1 statement);
  true value 2^41.92. Direction and force unaffected.
- Floor-band cap at (128,64): t_ch = 32, z0 = 1, cap = 1 + 31*32 = 993 for
  the |S| = k+1 family — EXACT. ✓
  CATCH #153: the |S| = k+3 lifts (|agr| = k'+1, d = 2(m-2) exactly — on the
  wide-band boundary, same z <= z0 floor gate) are capped by
  sum_{z<=z0} C(k'-1,z) C(t_ch, k'+1-z) = 31 more at (128,64) (total 1024,
  still << n^2), 7 at (32,16), 3 at (16,8). bsr_check P3's n_floor COUNTS
  both sub-families but caps with the k+1-only formula — conservative
  direction (spurious FAIL possible, false PASS impossible; measured values
  fit anyway: 53 <= 57, 48 <= 57 fresh). Repair: state the two-family cap in
  clause (P)'s band pin and in bsr_check.
- Rate <= 1/4 emptiness is STRUCTURAL, not just measured: floor band needs
  core deficiency d = 2(k'-1-z) >= 2(t_ch-2), i.e. z <= z0 = (k'-1)-(t_ch-2);
  with core size k-1 and t_ch = (n-k+1)/2, z0 >= 0 <=> 2k >= n-1. So at
  rho = 1/2 the family reaches the floor band (poly cap), at rho <= 1/4 its
  MAXIMUM depth 2(k'-1) falls short of the floor 2(t_ch-2) — empty by
  arithmetic for every q, every label vector. Verified as a law across all
  shapes s = 4..19 x four rates (A3). The measured 0 at (32,12,97) is the
  z0 = -3 instance. ✓ This is the table the P1 maintainer line needs.
- Odd-lift wide-band membership: d = 2(m-1) (|S|=k+1) resp. 2(m-2) (k+3)
  >= 2(m-2) always — algebraic, verified (A3), and end-to-end at the fresh
  cell (5907/6435 = 92% supply realized at q=193, reproducing the q-free
  binomial scale at a second prime). ✓
- Note (fold into #154): the P2/#145 "prize" instances use q = 2^128, 2^256
  as arithmetic stand-ins (2^128 != 1 mod 512, not legal fields); fine here
  since no field ops are performed — the legal-field windows are g1a's own.

## CLAIM 4 — #148 LEDGER/K4 PACKAGE: VERIFIED

- (64/63)(121/128) = 121/126 exact; primitive-only 121/128 < 1 exact. ✓
- The geometric ledger's hypothesis ("each scale-M class injects into a
  primitive quotient-row family of size <= C(n/M)^6") is g1a-unsatisfiable
  on the petal lane: at descended chart words the scale-M band class count
  itself is >= C(n'-1,k')/(4q(k'+1)) (g1a F4, hypotheses verified) —
  exponential >> C(n')^6, so no such injection family exists (pigeonhole).
  Node stays PROVED (true implication), petal edge retires. ✓
- The periodic mass is not orphaned: it lands on the profile clause (D1
  seam), gate cells [2,t] by COL, M > t by the replayed composite, ranges
  disjoint in (M,A), each class charged once at its exact-scale cell —
  the #102 dedup dissolution is correct (partition). ✓

CATCH #150 (the one consequential repair — D4's consumer audit is
INCOMPLETE): grep-audit of dag.json finds a consumer of the OLD weighted
n^6 form + the 64/63 rider that bsr_consistency D4 does NOT list:
**petal_g1_k4_scale_reserve** (CONDITIONAL) — "assume G1 supplies a finite
paid atlas with sum(m_chi+1) <= (121/128) n^6 [on every rate-preserving
quotient row n >= 256] ... the intrinsic geometric ledger then bounds ...
(121/126) n^6 ... proves the small-scale census conditional only on weighted
G1" — ev-wired as the ALTERNATE route to the census gate (with its partner
**petal_descent_classification_bridge**, TARGET). Its hypothesis is exactly
the g1a-falsified clause: unsatisfiable at fiber-rich descended chart words.
Left unhandled, the re-promoted gate keeps a dead CONDITIONAL wired as its
alternate supplier. SURGERY SPEC ADDITION: (a) node-local note + edge
retirement for petal_g1_k4_scale_reserve (hypothesis g1a-unsatisfiable
post-#138; same fate wording as the ledger's D4.2); (b) re-pose or retire
petal_descent_classification_bridge (its only consumer was the alternate
route); (c) add both to the D4 fate table. No packet claim is falsified by
this — it is a completeness gap in the fate audit.

CATCH #152 (wiring precision, two sentences): SUCCESSOR-A x G1'(D) prices
the {k+2, k+4}-band cells ONLY — i.e. own cells (2, k+2) and (4, k+4) plus
the csp cell (2, k+4). At official rows (k a 2-power) scale-M >= 8 classes
have |S| = k+M (multiple of M), never in {k+2, k+4}; they descend (L0) to
|S'| = k'+M/2 OUTSIDE A'(u1)'s consumed band. Hence: (a) the gate
re-promotion supplier map's "same cells, chart words: SUCCESSOR-A x G1'(D)"
overstates — the M >= 8 own cells are COL-ONLY; (b) bsr_successor_rewire's
"the aggregate over all scale-M cells, M in [2, t], bounded by the same
count" is FALSE under a literal cells-reading and must be band-scoped as in
csp Claim 3-C ("the aggregate of scale-M subclasses OF THE {k+2,k+4} BAND").
No mathematical failure — COL covers every consumed cell and csp C is
correctly scoped at its source; but the two draft sentences would mislead
the G3-compiler wiring if consumed literally.

CATCH #154 (numeric presentation, collected): (a) 2^41.3 -> 2^41.92 (three
places); (b) bsr_g1prime (D).2 "~350x margin against the trivial bound" vs
findings D4 "~700x" — per-profile the margin is 717.6x, the two-profile
aggregate is 359.1x; pick one and label it; (c) "violated by 54..3976 bits"
— exact 52.8..3975.0 (bit-length rounding); (d) q = 2^128/2^256 stand-in
note above.

## The QA.22 / D3 owed item — pre-computation CONFIRMED, statement fixed

- Dominance re-derived independently (A4): max over s = 13..20 x 4 rates of
  sum_{dyadic 4 <= M <= t} Q_M(A_own) / Q_2(k+2) = 2^-691.0, attained at
  (s, rate) = (13, 1/16) — the 2^-691 pre-computation is RIGHT, and the
  excess is the M = 4 term as stated. Maximal rows: log2(Q_4/Q_2) =
  -5.498e11 < -2^30 (replay). 719 = floor(n^6/C(n+6,6)) at s = 41..44 exact.
- What the extension must state (the single gate-promoting item): extend
  dyadic_profile_evaluation's budgeted profile ledger from dyadic M > t to
  ALL dyadic 2 <= M <= t at the P1-OWN cells (M, A_own(M)),
  A_own(M) = M*ceil((k+1)/M), each priced 719 * Q_M(A_own) — plus the
  (2, k+4) csp-band cell at 719 * Q_2(k+4) if consumed — and re-run the
  QA.22 exact evaluation on the full official grid (s = 13..44, four rates)
  showing imgfib's reserve absorbs the extended ledger; by first-scale
  dominance the added mass is <= (1 + 2^-691) * 719 * Q_2(k+2) per band
  cell. Falsifier F(G)-3 as pre-registered. This is a computation in a
  PROVED node's machinery — correctly classified as a landing item, not a
  design hole.

## Link-by-link surgery spec status (with repairs folded)

1. Mint G1' (P)+(D) per bsr_g1prime_statement: SOUND — fix #154a/b numbers;
   add the #153 two-family floor cap to the BAND PIN paragraph.
2. Rewrite SUCCESSOR-A conditional.md per bsr_successor_rewire: SOUND —
   band-scope the aggregate sentence (#152b).
3. Mint Lemma COL node (supplier -> petal_small_scale_staircase_census):
   SOUND — reword clause (v) (#151).
4. Gate re-promotion TARGET -> CONDITIONAL (PROVED-pending-audit on D3):
   SOUND — supplier map: mark M >= 8 own cells COL-only (#152a).
5. petal_growth r3 route edit + ledger edge retirement + node-local notes:
   SOUND — ADD petal_g1_k4_scale_reserve edge retirement + node-local note
   and petal_descent_classification_bridge re-pose/retire (#150).
6. Queue QA.22 M <= t extension: statement as above; pre-computation right.
7. P1 maintainer line with the #145 table: the table is now bulletproof —
   floor band poly/empty law z0 >= 0 <=> 2k >= n-1 included.
8. #148 ledger update (64/63 rider deletion, 121/128 alone): VERIFIED.

## Catches minted this audit

- #150 missed consumer: petal_g1_k4_scale_reserve (+ descent bridge), the
  ev-wired ALTERNATE gate route, consumes the g1a-dead weighted form +
  64/63 rider — must be added to the surgery spec's fate table.
- #151 COL(v) "precisely the boundary" iff only for M | k; counterexample
  (32,8,16); load-bearing direction intact.
- #152 SUCCESSOR-A secondary-supplier band scoping (two sentences; M >= 8
  own cells are COL-only).
- #153 floor-band cap must include the |S| = k+3 lift sub-family (+31 at
  (128,64), total 1024; conservative in bsr_check, claims unaffected).
- #154 numeric presentation collection (2^41.92; 718x vs 359x; 52.8 bits;
  prize-q stand-ins).

> #155 ANNOTATION (2026-07-13, qme audit): the 2^-691 dominance constant printed in this file is a lg_frac rounding artifact — the exact worst excess is 2^-690.2765..2^-690.2766 at (13, 1/16); honest grid constant (1 + 2^-690). The qme packet carries the corrected form; this record is annotated, not rewritten.

> #175 ANNOTATION (2026-07-13, cpa audit at clause-(P) banking): the structural law printed in this record as "z0 >= 0 <=> 2k >= n-1" is an odd-k formalization artifact (its t_ch = (n-k+1)/2 is the odd-k petal count). The operational even-k law is 2k >= n-2, and the two genuinely diverge OUT of scope: at (10,4,11) three aperiodic floor-band full-petal lifts realize where the printed law predicts empty (cpa_checks.py A1, in-vivo). In scope (even-k 2-power rows) both collapse to 2k >= n by parity — every in-scope claim in this record is unaffected. This record is annotated, not rewritten.
