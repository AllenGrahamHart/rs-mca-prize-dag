# upr2: Fresh upstream-PR crosswalk survey (2026-07-21)

## Pins
- Upstream origin/main: 18cfc199 "Integrate M31 route-cut and Lean PR wave" — NO drift since prior pin.
  (Local checkout = 18cfc199 + our PR #1010 commit 17a7373c only.)
- Our repo: prize @ master e3698c2d.
- Open upstream PR queue (2026-07-21): ONLY TWO —
  - #1010 AllenGrahamHart (OURS): SS0.4 four-pair exact-integer replay audit. Scope TAKEN.
  - #1009 holmbuar: "Semantic M31 owner-or-shell compiler" — Lean (stdlib) M31 first-match owner
    interface C1–C8, executable residual filter, natural-scale target; CONDITIONAL on (SO3+7);
    OPEN deployed M31 residual. Lane: Lean formalization of M31 rooted-shell / first-match owner.
- Recently closed/integrated: #984–#1008 all closed (M31 route-cut + Lean wave integrated at
  18cfc199; earlier experimental wave at 57e39fba). So the previous "queue-owned lanes"
  (KoalaBear rank-nine #989-995, Mersenne scalar-descent #993, contributor-compute #999)
  are now TREE-owned, not queue-owned.

## His CURRENT priority structure (verbatim quotes)

### agents.md "remaining hard inputs ... v3 vocabulary" (the six-input checklist)
```
row-sharp finite Q / prefix max-fiber certificates;
exhaustive first-match atlas and residual chart coverage;
Sidon/Fourier payment or equivalent effective-image MI+MA proof;
residual ray compiler for higher-dimensional balanced cores;
exact extension and quotient payments;
one summed integer certificate for each adjacent deployed row.
```
"Agents should treat those items as the current proof checklist.  Work that does not reduce,
audit, formalize, or falsify one of them is secondary."

### agents.md "What counts as progress now" (ranked)
1. Lean formalization of grande_finale.tex / cs25_cap_v13_2.tex / rs_mca_thresholds.tex;
2. adversarial proof audits focused on the v3 remaining hard inputs (list as above);
3. proofs, counterexamples, or exact certificate packets for any one of those v3 inputs;
4. final computations and examples (bad-line moduli strata, primitive Boolean prefix fibers,
   image-scale Fourier/Sidon cuts, target reserves);
5. finite adjacent certificates for the deployed rows, with exact constants and replayable packets;
6. (only after threshold stable) Paper C protocol ledger.

### agents.md "Good first PRs"
1. "Write a small exact Q toy packet that tests `prob:row-sharp-q` on a row where the full fiber
   distribution can be enumerated."
2. "Produce a quotient/composite rung audit for one active `a+` row, with exact integer margins"
3. "Turn one residual BC chart into either a paid one-parameter pencil or a named
   higher-dimensional obstruction."
4. Lean theorem-statement target for row-sharp Q.
5. "Formalize one already-proved grande_finale local lemma ... such as the composite-prefix
   gcd(e,N) descent."
6. "Build a new exact adjacent example that prints L(a0), U(a0+1), B*, denominators, endpoint
   convention, and first-match cells."
7. "Audit one Paper D v13.2 finite inequality against its script or printed integer certificate."

### grande_finale.tex sec:exact-completion-ledger — the (F1)-(F4) obligations
"(F1) prove the row-sharp pruned Q bound of prob:row-sharp-q;
 (F2) certify that every residual MCA balanced-core chart is paid or reduces to the one-parameter
      moving-root theorem, and prove the separate arbitrary-word interior theorem for the list rows;
 (F3) pay the remaining extension projections with exact multiplicity; and
 (F4) run one integer verifier establishing (eq:exact-completion-certificate) for each row."
Ledger: U_total = U_paid + U_Q + U_BC + U_new (list rows: U_BC -> U_list-int).
prob:row-sharp-q: "max_z |P_Q(z)| <= R_Q^row binom(n,a_+)|B|^{-(a_+-K)}" with literal row constant.
prob:saturated-bc: residual balanced-core charts paid or decomposed into certified # of projective
pencils covered by thm:bc-moving-root; list rows need SEPARATE arbitrary-word interior theorem.
sec:finite-q-barrier: "the Mersenne-31 list row is the binding case: ... maximum-prefix-fiber
overhead may be at most 8.4152 times the full-slice average."
Full-budget Q overhead ceilings (eq:finite-q-ratios): 4807520.9295, 4226236.5253, 9.5722, 8.4152.
Average ceilings (eq:finite-average-ceilings): 57198030366, 65065153468, 1752700, 1993678.
B*: KB rows 274980728111395087 (target 2^-128); M31 rows 16777215 (target 2^-100).
Rows: n=2^21, K=2^20+1 (MCA), K=2^20 (list); w=a_+-K = 67471 (KB), 67447 (M31).

### towards-prize.md §0.4 (four adjacent pairs) — occupied by our #1010 (audit side)
### towards-prize.md §0.5 Falsifiability (verbatim)
"A counterexample to the conjectured envelope should not be vague.  It should produce one of two
explicit objects:  super-polynomial primitive prefix fiber; or super-polynomial primitive
split-pencil family.  Both are machine-checkable."
### towards-prize.md §3 useful-PR test: packet / reduce residual chart / reusable theorem /
"Does it audit the exact prize object, denominator, or endpooint convention?"
### readme.md remaining hard inputs = same six-input list as agents.md.

### finite_notes.md (grande_finale_work) open finite closure inputs (excerpt)
- refresh MCA row packets at active moved pair
- build the quotient image upper ledger (current rung audit is lower-floor only)
- M31 MCA non-firing tight watch item: Gceil c=2048, exact mass 12769758 vs B*=16777215,
  margin -0.3938 bit.

## Crosswalk findings (this session)

### F-A. DRAFT 2 IS CONSUMED BY HIS OWN TREE — RETIRE.
rs_mca_thresholds.tex @ HEAD, `cor:prize-window-compiler` ("Self-contained quadratic-range
target compiler"): for rho in {1/2,1/4,1/8,1/16}, n=2^e, B=floor(q/2^128), if
1 <= B <= M_rho(n) = min(r_rho(n)+1, n-k-1) then e_MCA(C,delta)<=2^-128 <=> floor(delta n)<=B-1,
"every such row is solved throughout the field window 2^128 <= q < 2^128 (M_rho(n)+1)".
EXACT NUMERIC CONFIRMATION (ramguard, exact ints/Decimal-80):
  r_rho(2^41)|_{rho=1/2} = 389500552608, M_rho = 389500552609 (== his table-B rate-1/2 row),
  window upper log2 = 166.50283441889553... == our draft-2 boundary "2^166.502834419";
  quadratic condition holds at r=B-1, fails at r=B (both checked exactly).
His statement is STRICTLY STRONGER than upr_draft_2 (all four rates, general dyadic n; also
self-contained, no BCIKS). Our wave-10 a_RH(q) = n - floor(q/2^128) + 1 is the rho=1/2
specialization. -> DRAFT 2 RETIRED as redundant. (Related: our banked node
mca_quadratic_prize_rows is itself a REPLAY of his thm:intro-prize-rows/QMS — vendored,
ledgered, not proposable as ours.)

### F-B. PROTH-ROW REPLAY CANDIDATE DEAD.
His tree already contains experimental/scripts/verify_proth_rows_certificate_audit.py
(integrated 2026-07-15, "Integrate frontier PR wave"): an "independent adversarial arithmetic
+ definition recomputation of the four certified Proth prime rows", stdlib big-int only, incl.
Proth witness, B=floor(p/2^128), B*==B. Exactly the genre our mca_quadratic_prize_rows replay
would offer. Overlap: TOTAL. Dead.

### F-C. NEAR-RATIONAL SUPPORT-WISE REFUTATION ALREADY REPAIRED UPSTREAM.
Our REFUTED node v13_2_near_rational_supportwise_payment (mu_8 subset F_17 exact
counterexample vs the proof step of cor:capfp-line; displayed inequality NOT refuted) — his
tree already has cap25_v13_near_rational_support_mismatch_audit.md + agents-log entry
("repair a near-rational support-mismatch overclaim ... the near-rational branch needs an
explicit support-wise first-match payment"). Already addressed. Dead as a new PR.

### F-D. HELD DRAFT 3 HAS A LATENT OVER-CLAIM — REDRAFT REQUIRED.
Draft 3 says "This is an EXPLICIT primitive prefix fiber". FALSE in his first-match sense:
rate_half_cyclic_rotated_prefix_floor is built on c | n/2, N=n/c, cyclic rotation mod Y^N-delta
— a QUOTIENT-SCALE construction; under his first-match ledger those fibers are assigned to the
QUOTIENT cell, not the primitive leaf. Correct v3 reframing: (i) an explicit super-polynomial
QUOTIENT-CELL prefix fiber => exact quotient payment (six-input #5) is load-bearing, and a
SS0.5 falsifier must be primitive precisely because non-primitive super-poly fibers exist and
are paid; (ii) the budget-3 split-pencil census (13 chambers, scroll branch EMPTY, 0/13
closed) as a worked example of the prob:saturated-bc chart-decomposition genre at OUR row.
Also must cite his rowsharp_q_external_calibration.md (his own falsifier-fleet packet: both
pre-registered falsifier hunts NEGATIVE at toy rows) and position relative to it.

### F-E. HGE4 -> SP crosswalk: PARTIAL, regime-mismatched, subordinated.
Our HGE4 chain (waves 17-18 audited) proves primitive shift-pair width EXCLUSIONS
(E_h^prim(m,p)=0 for m/4 <= h; swap class empty when m^(h-1) >= h^(m/4); etc.) with proved
interface N_h^strip <= SP_h^prim = n O_h^prim ("ordered top shift pairs after quotient-
pullback/full-fiber deletion" — the primitive top stratum of HIS SP ledger via the proved
weld dictionary). BUT: (1) our corridor scope is p prime, p == 1 mod n, p >= n^2 — his
deployed rows have p ~ 2^31 < n^2 = 2^42 (n=2^21), so no deployed-row claim possible;
(2) v3 thm:q-implies-sp: "a row-sharp max-fiber Q theorem automatically pays the primitive
SP ledger" — SP-side results are explicitly secondary in v3; (3) our own aggregate residual
sum_(h=4)^(m/4-1) E_h^prim <= (21/2)m^2 (ERT4'''') is OPEN. Verdict: lead-grade hold.

### F-F. Ratio spot-checks of his eq:finite-q-ratios (ramguard, exact Fractions):
B*/avg = 4807520.9295 / 4226236.5253 / 9.5722 / 8.4152 — all four match his printed values.

### F-G. Other lanes checked and NOT proposable:
- dli (dli_prime_weighted_large_block_support: U-weighted primitive-core count for
  x4_exactlist_staircase_split at our rows) — internal object, does NOT map to his
  U_list-int "arbitrary-word interior codeword-ray" obligation. DIFFERENT-LANE.
- WCL slots / weight-3/4 cyclotomic exclusions / C36 6^{n/4} / K4 / census-gate — internal
  lanes, no six-input consumes them (same verdict as 07-20 survey; v3 did not change it).
- XR (xr_highcore_collision_count: post-strip slope counts at our six clean-rate candidates;
  P3E5 first-shell exclusion) — our-row MCA residual lane, not his extension-payment object.
  DIFFERENT-LANE.
- L1 petal/PMA: mixed-petal red still TARGET (l1_mixed_petal_amplification, catch #212);
  #750 correction note already delivered the PMA heads-up. Fence carried.
- Lean (his #1 priority): we have no banked Lean assets; holmbuar #1009 owns the M31
  owner-shell Lean lane. Not ours to serve.

## Final ranking (see report), DON'T list, recommendation
1. Redrafted draft-3 (SS0.5 + quotient-payment calibration + BC-census example) — next
   submission AFTER #1010 triage; redraft mandatory (F-D fix).
2. Pruned-Q toy packet (his Good-first-PR #1 verbatim; the pruned/first-match distribution
   is absent in-tree — his calibration packet is raw-census) — NEW build on our banked
   rigidity/second-moment replay machinery; 1-2 sessions; final grep-sweep at submission.
3. HOLD: HGE4->SP exclusions (F-E).
RETIRED/DEAD: draft 2 (F-A), Proth replay (F-B), near-rational refutation (F-C).
DON'T (carried): no a_RH-as-SS0.4-safe-side; no n=2^21 safe-side entry (now tree-owned +
actively worked: kb_mca_1116048_first_match_ledger_v1 named open cells, M31 rooted-shell);
no L1 petal re-entry; no vendored-content proposals (import-ledger rows); no
budget-3/DSP8-as-closure. DON'T (new): never call the cyclic family "primitive"; stay out
of Lean M31 owner lane (#1009); don't submit Proth replay or near-rational refutation
(in-tree); pacing rule — one audit-genre PR in flight at a time (wait for #1010 triage).
TOP RECOMMENDATION: submit NOTHING new today; queue = redraft draft 3, build pruned-Q toy
packet in parallel; revisit after #1010 triage / next integration wave.
