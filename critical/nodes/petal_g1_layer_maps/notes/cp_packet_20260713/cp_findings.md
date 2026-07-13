# cp_findings — CLAUSE (P) proof worker, 2026-07-13
# Catch ledger continues from #167. Companion files: cp_statement.md,
# cp_proof.md, cp_verify.py (ramguard tiny, 59 PASS 0 FAIL full suite,
# every stage also replayed standalone), cp_report.md.

## HEADLINE

CLAUSE (P) — the petal family's last open mathematics — is PROVED AS POSED
by a support-rigidity counting theorem (cp_proof.md): at the floor band
`d >= ell(t_ch - 2)`, full-petal supports have `|S n Z| <= J = k+3-2t_ch`
and touched petals `m in {t_ch-1, t_ch}`; hence at most
`N_max = 2^{b0} (t_ch+1) S_J(k-1)` classes for EVERY received word, EVERY
field, EVERY scale class. At official rates <= 1/4 the band is EMPTY for
all contributors (J < 0); at rate 1/2, `J = 3` and the word-INDEPENDENT
atlas `{(D0, R) : |D0| >= 2(t_ch-2), R <= B}` covers everything with
weighted census `N_max ~ n^4/96 << (121/128) n^6` (binding official row
n = 2^41: 2^157.42 vs 2^245.92, margin 2^88.5). No open hypothesis is
consumed; received-word uniformity — the frontier.md extraction
obstruction — is dissolved at this band because the atlas does not depend
on the word at all.

## CATCHES #168-#171

- **#168 (LAYOUT ANCHORING IS LOAD-BEARING — new statement pin).** The
  floor band protects clause (P) ONLY as a per-layout notion. Under a
  layout-EXISTENTIAL reading ("floor-band w.r.t. some legal layout") the
  #145 odd-lift family re-enters: every `|S| = k+1` lift is re-basable
  into the floor band of a TAILORED layout (core = the `k'-1` fibers
  disjoint from its quotient support, plus the split point; petals = its
  own `k'` fibers; the spare-fiber count fits EXACTLY at rate 1/2), and
  the #145 kill `C(63,32) = 2^59.67 > (121/128)128^6 = 2^41.92`
  transports verbatim. Verified in vivo at (32,16,97): a z = 7, d = 0
  lift (maximally floor-EXCLUDED in the word's own layout) becomes
  d* = 14 >= 12, j* = 1, full-petal in its tailored layout; all 5967
  realized |S| = k+1 lifts are re-basable (cp_verify P6/M4). The packet
  therefore states and proves clause (P) layout-anchored (one fixed
  layout per row/word — the semantics of every banked measurement), and
  the pin is now explicit in cp_statement.md. Parallel to #145 one level
  up: after the band pin, the LAYOUT pin is the second load-bearing
  quantifier in the posing.

- **#169 (FLOOR-BAND RIGIDITY + GENERAL EMPTINESS LAW — the proof's
  engine).** For any layout with core `k-1`, disjoint 2-point petals,
  background `b0 <= 1`, any word, any field: floor band + full-petal +
  `|S| >= k+1` forces `j = |S n Z| <= J = k+3-2t_ch` and
  `m >= t_ch - 1` (two-line proof, cp_proof.md Lemma B). Consequences:
  (a) class census <= `2^{b0}(t_ch+1)S_J(k-1)` — word/q/scale-free;
  (b) the floor band is EMPTY for ALL contributors (not only the #145
  hazard family) iff `J < 0`; on even-k 2-power rows: nonempty <=> rate
  >= 1/2 (no such row attains the boundary 2k = n-2, parity — verified
  s = 3..24). This strengthens the banked law (bsra: "z0 >= 0 <=>
  2k >= n-1", derived for the lift family with half-integer t_ch) to
  every contributor; the printed boundary constant differs immaterially
  (n-1 vs n-2; no even-k 2-power row sits between). At rate 1/2, J = 3
  exactly at every row size: floor-band contributors agree on AT MOST 3
  core points. This one inequality separates both banked hazards from
  the floor band: #145's mass sits at j = 2z+1 <= 3 <=> z <= z0 (the
  banked caps), and #138's exponential periodic mass sits at j ~ 2z with
  z hypergeometric-large — never floor-band (in vivo: periodic floor
  count 0 at (32,16,97), 1 at (32,16,193)).

- **#170 (THE LIFT FAMILY DOES NOT EXHAUST THE APERIODIC FLOOR BAND).**
  Full floor-band full-petal censuses (candidate method, rigidity-
  complete, cross-validated against complete brute at n = 16):
  (16,8,97): 10 = 8 lifts + 1 non-lift aperiodic + 1 periodic;
  (32,16,97): 83 = 53 lifts + 30 non-lift aperiodic + 0 periodic;
  (32,16,193): 67 = 48 + 18 + 1;  (32,16,257): 63 = 53 + 10 + 0.
  The banked #145/#153 numbers (8/53/48) were LIFT-ONLY counts (bsr_check
  n_floor semantics) — correct as stated, but a clause-(P) atlas sized to
  the two-family cap alone (57 + 7 = 64 at (32,16)) would UNDERCOVER the
  demand (83 > 64). The non-lift branch is the rank-1 family of the
  parity dichotomy (cp_proof.md section 4: h = f0 + x_nf f1 =
  c L_{Y_full}, two parameters against >= 3 half-agreement conditions),
  and its counts decay with q exactly as that torus analysis predicts
  (30 -> 18 -> 10 at q = 97 -> 193 -> 257) while the lift counts stay
  binomial (53/48/53, q-free). The rigidity census prices BOTH branches
  with no q input; no consumer change needed. Consistency note for the
  ledger: the 372-cell "aperiodic accidents decay ~1/p" line now has a
  mechanism and a floor-band-exact instance ledger.

- **#171 (BELOW-TOP EXPOSURE UNDER THE FLOOR POSING — honesty flag for
  the P1 maintainer line).** Under P1 = floor (the posing), the wide
  minus floor full-petal APERIODIC lift mass — supply ~ C(n'-1,k') +
  C(n'-1,k'+1) minus the poly floor caps, e.g. ~2^59.67 - 1024 at
  (128,64), measured 92-93 percent realized at n = 32 across three
  primes — is OUTSIDE clause (P) and lands in petal_growth's "below-top
  contributions are separate obligations" bucket. The below-top evidence
  banked there (76-row Lemma-13 scan, "max exact count 1 below top") is
  per-chart residue-kernel metrics predating #145 and does not price this
  family; per-chart K4 lines remain true (the mass spreads over ~C(t,m)
  charts), but the below-top branch has no aggregate budget statement
  covering it. The owed P1 maintainer line should be requested with BOTH
  tables: floor => (P) is a theorem (this packet) + the below-top branch
  inherits the 2^59.67 family; wide => (P) is #145-false without a
  carve-out. Pre-registered falsifier (P)-3 unchanged.

## VERIFICATION RECORD (cp_verify.py, all ramguard tiny)

- Full suite: 59 PASS, 0 FAIL, 12.9 s. Stages also run standalone.
- P1 (16,8,97,consec): COMPLETE brute census (all C(16,9) subsets);
  rigidity holds on every floor-band full-petal class; candidate method
  == brute (method cross-validation); banked lift pin 8 reproduced;
  atlas coverage + per-chart <= t+1 (max 3).
- P2 (32,16,97,geom5): candidate census 83; rigidity clean; S2 identity;
  lift part == independent quotient-side method (53 == 53, banked pin);
  <= N_max = 10368; <= #153 caps on the lift part; per-chart max 8 <= 9.
- P3a (32,16,193,consec): bsra fresh-cell pin 48 reproduced; census 67.
- P3b (32,16,257,geom3): NEVER-banked cell; census 63; all checks clean.
- P4 non-coset layouts at (16,8,97): fiber_pairs (2 floor classes,
  nonvacuous) and shuffled seed 1 (0 floor classes — vacuously clean;
  the nonvacuous non-coset case is fiber_pairs): rigidity + candidate ==
  brute on complete censuses.
- P5 (16,4,97) rate 1/4: COMPLETE brute — 51 contributor classes exist,
  floor band EMPTY in vivo (the emptiness is the band, not vacuity of the
  cell); arithmetic law replayed at (32,12) and official n = 2^42..2^44.
- P6 mutations, REQUIRED-TO-TRIP all trip: M1 widening the band one petal
  admits 550 realized classes with j = 5 > 3 (rigidity is band-sharp);
  M2 dropping the m = t_ch - 1 stratum undercounts 1 < 10; M3 corrupting
  one petal value shifts the census 83 -> 41; M4 = the #168 demo (above).
- P7 exact bigint: budget fit at ALL rate-1/2 rows s = 3..44 (worst
  margin 2^12 at s = 3); binding official row n = 2^41 margin 2^88;
  official rows 2^42..2^44 empty; rates <= 1/4 empty s = 13..44; #153
  caps 993 + 31 = 1024 <= N_max = 2,754,048 at (128,64); parity law;
  Newton == Lagrange interpolation self-test.

## CONSISTENCY vs THE BANKED LEDGER

- All four banked floor pins reproduce: 8 (16,8,97), 53 (32,16,97),
  48 (32,16,193), 0 (32,12,97 — via the emptiness law + banked
  measurement; complete in-vivo emptiness verified at (16,4,97)).
- #153 caps embed (993+31 <= N_max); z <= z0 <=> j <= 3 is the same
  inequality as Lemma B's J = 3 on the lift family.
- The g1a falsification (#138) is untouched and untouchable here: its
  exponential mass is periodic, wide-band, j-large — outside the floor
  band; clause (D) (column-priced periodic branch) is unaffected.
- The P3-curse (#139) does not bind: floor-band charts hold up to
  t_ch + 1 classes (ell = 2 official charts, not ell' = 1 descended
  ones), and the demanded family is poly by rigidity — the curse's
  premise (exponential demanded family) fails, in the good direction.
- #141 (weights are poly, not O(1)): honored — the census is weighted at
  m_chi + 1 = t_ch + 1 ~ n/4 per chart, and still clears by 2^88.

## NOT DONE / OPTIONAL STRENGTHENINGS (none blocking)

- A rigorous per-word upper bound O(poly(n)/q) for the non-lift floor
  branch (rank-1 torus first moment) — would sharpen #170's decay from
  measured to proved; NOT needed (the rigidity census already pays it).
- The house fresh-context audit replay before PROVED lands in dag.json
  (house law; this packet is audit-ready: staged verifier, banked pins,
  required-to-trip mutations, complete-census cross-validations).

---

## AUDIT ANNOTATIONS (cpa banking, 2026-07-13; verdict SOUND, catches
## assigned #172-#176)

- cpa-C2 = catch #173 (evidence relabel): the #168 sentence "all 5967
  realized |S| = k+1 lifts are re-basable (cp_verify P6/M4)" overstates
  the verifier's role — cp_verify P6/M4 checks n_rebasable > 0 and
  re-bases ONE witness; the universal claim rests on the spare-fiber
  counting of cp_proof.md section 5 (exact: k'-1 spare fibers at rate
  1/2; audit re-derived). Read the evidence as "arithmetic + one
  in-vivo witness".
- cpa-C1 = catch #172: cp_verify's two P1 atlas lines are tautological
  (no discriminating power); the discriminating coverage mutation is
  cpa_checks.py NM3 (banked alongside, REQUIRED-TO-TRIP, trips).
- cpa-C3 = catch #174: lift-subfamily nonemptiness assert added to
  run_cell_32 at banking (62 PASS post-repair).
- cpa-C4 = catch #175: the dag surgery block's "2k >= n-1" print is
  the odd-k formalization artifact; operational law 2k >= n-2;
  divergence witnessed OUT of scope at (10,4,11) (3 realized floor
  lifts vs predicted empty); in scope both collapse to 2k >= n.
  Corrected in the dag statement addendum at banking.
- cpa-C5 = catch #176 (scope-mass observation): mixed-petal floor mass
  is 4x full-petal at (16,8,97) (43 vs 10) — explicitly outside clause
  (P) and outside the top-band obligation; recorded, nothing dropped.
