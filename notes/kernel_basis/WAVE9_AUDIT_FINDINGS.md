# Wave-9 fresh-context replay audit — Codex v4 post-wave-8 tail (rate-half MCA, WCL (2,6), PMA tail ladder, C36/HGE4 touches)

Auditor session 2026-07-17. PIN: **4442ffd5be176520a8db8cb093dcdcb133ad7816** (v4 worktree
/home/u2470931/smooth-read-solomin/prize-codex-resolution-v4-20260713, branch
codex/full-prize-resolution-v4-20260713; HEAD == pin at audit start). Scope = 25 commits
ae2e5dd5..4442ffd5. Master baseline: /home/u2470931/smooth-read-solomin/prize (read-only),
wave-8 import landed. Catch numbering LOCAL (w9-C#). READ-ONLY both repos; all pin content via
`git show 4442ffd5:<path>`; replays from scratchpad mini-tree w9_tree/ under tools/ramguard
tiny (Modal for heavy). Deliverables beside this file: w9_checks.py (independent constants +
conversion toy, ALL PASS), w9_dag_delta.py + w9_percommit_status.py (dag forensics),
w9_dags/ (per-commit dag.json dumps), w9_tree/ (pinned node-file mini-tree).

## VERDICT LINE (updated as clusters complete)

- CLUSTER 1 (rate-half MCA, 4 commits): **IMPORT-WITH-REPAIRS — and the decisive answer is
  NEITHER "closed" NOR "conditionally reduced onto new poses": the MCA/CA half of the
  rate-half red is NOT closed; it is re-posed (justifiedly) as a FIELD-DEPENDENT
  adjacent-certificate frontier after v4 REFUTED the former fixed crossing at sigma*+1.**
  Three new PROVED nodes (pole floor + 2 exact reductions), all hand-traced sound, all
  verifiers PASS, constants independently reproduced. No new TARGET/CONJECTURE minted
  anywhere in the wave (the suspected `dli_harmonic_conductor_ledger` DOES NOT EXIST at pin).
  Major cross-wave consequence: the wave-8-imported "banked safe side above sigma* /
  list crossing DETERMINED" sentences on MASTER are now known to be overclaims (v4's own
  scope audit found the safe side was planning prose; v4's s=c-1 floor proves points above
  sigma* UNSAFE). Wave-8 addenda need correction addenda (w9-C2/w9-C3).
- CLUSTER 2 (WCL (2,6) recursive-norm closure): **IMPORT-WITH-REPAIRS (hygiene-only) —
  SLOT (2,6) CLOSED on every official row; residual becomes FOUR slots
  (1,5),(1,6),(2,7),(4,9).** Quotient + saturation + double-zero branch hand-traced sound;
  census independently reproduced EXACTLY (404,740; all histograms); ALL 3,163 batch
  candidate digests + aggregate + representative digest reproduced from scratch (Modal);
  the 510 structural cases proven = exactly the antipodal-mirror family c=512+a+b; 2
  recorded prime exponents recomputed independently; full Pocklington graph re-validated
  locally (6/6 mutations). Trust gap w9-C10 (bulk norm values digest-pinned) mirrors
  w8-C12, mitigated.
- CLUSTER 3 (PMA tail ladder): **IMPORT-WITH-REPAIRS (custody-only) — five PROVED
  reduction nodes, chain hand-traced end-to-end, 5/5 verifiers PASS; reduces v4's
  rate-half M=4,t=3 tail to ONE exact guarded split-divisor atom (bijection, no loss);
  fixture self-repair verified necessary (old row had J=3>0) and correct (new row J=0).
  NO change to master's l1 red open-content sentence (clause-(P)-side stratum).**
- CLUSTER 4 (C36/HGE4/weight-5 streaming): HGE4 contract files IMPORT-CLEAN (dag statement
  byte-identical to master incl. catches #99/#100; RAW-NG interface sound); two new f3_h3
  PROVED nodes (root bound = proof-type, PGL2 fence = fence-type) verifiers PASS but
  DEFERRED with the unaudited wave-8 Cluster A chain they depend on; the two f3_h3 dag
  statement changes are stale-dag-to-file SYNCS (verified byte-level); weight-5 (1,5)
  streaming = INFRA-IN-FLIGHT, no claims, DEFER with pre-registered expectations.

## DAG-STATUS-DELTA TABLE (ae2e5dd5 -> 4442ffd5, computed per-commit)

Net delta: 690 -> 702 nodes; **12 NEW nodes, ALL PROVED; 0 removed; NET STATUS FLIPS: ZERO;
27 new edges, 0 removed.** No auto_discharge sweep fires in this range (packaging, list_safe
etc. all UNCHANGED). Statement-text changes on 5 existing nodes (see custody).

New nodes (status PROVED, layer):
| node | commit | consumer(s) |
|---|---|---|
| pma_ratehalf_core_triple_excess_reduction | 0469c8c2 | petal_mixed_amplification (ev); req <- pma_three_petal_projective_johnson_bound |
| pma_ratehalf_source_aligned_gcd_excess | d4d5b376 | pma chain (req of core_triple) |
| pma_ratehalf_source_crossratio_fiber_reduction | 2e02fcd2 | pma chain |
| pma_ratehalf_two_petal_support_fiber_reduction | d4bcebea | pma chain |
| dli_wcl_ell2_weight6_split16_counterfixture | b06971bf | dli_wcl_zone_coverage (ev) |
| dli_wcl_ell2_weight6_recursive_norm_exclusion | 17617e41 | zone (ev) + dli_primitive_matching_truncation_majorant (req-parent) |
| pma_ratehalf_complement_linear_slice_reduction | deb8d257 | pma chain end + shared_census_kernel (ev) |
| f3_h3_pgl2_conjugacy_route_fence | 9fbb4612 | f3_h3_mobius_excess_half (ev) |
| f3_h3_local_cancellation_root_bound | e7967d2c | f3_h3_mobius_excess_half (ev); req <- f3_h3_local_cluster_valuation (UNAUDITED wave-8 Cluster A!) |
| rate_half_cyclic_simple_pole_mca_floor | 15db64d9 | rate_half_band_closure (ev); req <- rate_half_cyclic_rotated_prefix_floor |
| rate_half_mca_sparse_layer_reduction | 4f4d81eb | rate_half_band_closure (ev) |
| rate_half_sparse_pinning_rigidity | 4442ffd5 | rate_half_band_closure (ev) |

TRANSIENT FLIP (self-corrected inside the range, documented for the record):
- rate_half_band_closure TARGET -> PROVED at 15db64d9 ("closes the node"), REVERTED
  PROVED -> TARGET at 56c25337 eight minutes later after v4's own "consumer-backward scope
  audit" found the claimed downstream safe side did not exist as a theorem. NOT an
  auto_discharge artifact (manual flip with proof text, manually reverted). At pin: TARGET.

Statement-field changes on existing dag nodes (custody: addenda on import, law #104):
- rate_half_band_closure.statement — re-posed twice; final = RH-ADJ field-dependent frontier.
- rate_half_cyclic_rotated_prefix_floor.statement — cap instantiation s=2,978,146 -> s=c-1
  (sigma_max=8,594,128,895); general theorem unchanged (always all 0<s<c).
- petal_mixed_amplification.statement — Cluster 3 (rate-half tail sub-bucket status).
- f3_h3_product_fiber_codegree_budget.statement, f3_h3_uniform_product_fiber_stepanov.statement
  — Cluster 4 touches.

---

## CLUSTER 1 — RATE-HALF MCA (15db64d9 + 56c25337 + 4f4d81eb + 4442ffd5)

### The decisive determination (task question (a))

**NOT A CLOSURE, AND NOT A CONDITIONAL REDUCTION ONTO NEW POSES.** The exact arc:

1. **15db64d9** mints `rate_half_cyclic_simple_pole_mca_floor` (PROVED, background/):
   quantitative simple-pole conversion of the wave-8 cyclic deep list into an MCA/CA
   bad-slope floor `epsilon_ca, epsilon_mca >= E(q,L_q) = L_q(q-n)/(q(q-n+kL_q)) > 2^-83
   > 2^-128` for every official rate-half field q < 2^256 and every excess
   1 <= sigma <= sigma_max = 8,594,128,895. Commit ALSO flipped rate_half_band_closure
   TARGET->PROVED on the belief "the downstream safe-side predicates already own the edge
   above sigma*".
2. **56c25337** REVERTS the flip: v4's own scope audit found the "banked safe side above
   sigma*" was PLANNING PROSE, not an in-repo theorem — "Paper D's proved pincer stops at
   half the distance and the local clean-rate safe theorem [r2_clean_rates] excludes rate
   1/2". Node re-posed as exactly the safe inequality (RH-SAFE):
   epsilon_mca(C, 1-(k+sigma*+1)/n) <= 2^-128.
3. **4f4d81eb** REFUTES (RH-SAFE) outright: the cyclic construction's pigeonhole count is
   independent of the residual-prefix size s, so taking the maximal legal s=c-1 gives the
   SAME deep list at excess dc+c-1 = 8,594,128,895 > sigma*+1; the pole conversion then makes
   sigma*+1 (and everything through sigma_max) MCA/CA-unsafe. Adds refutation.md, re-poses
   the node as the field-dependent adjacent-certificate frontier (RH-ADJ):
   produce row-computable a_RH(q) with B_mca(a_RH(q)) <= floor(q/2^128) < B_mca(a_RH(q)-1),
   with proved bracket a_RH(q) >= k + 8,594,128,896 (RH-BRACKET). Mints
   `rate_half_mca_sparse_layer_reduction` (PROVED): exact lossless identity
   B_mca(a) = max(B_ca^far(a), S_sparse(a)) (MS1).
4. **4442ffd5** mints `rate_half_sparse_pinning_rigidity` (PROVED): sparse-side structure —
   at a=k+tau every non-tangent bad slope forces support e >= tau+1, an ambiguity polynomial
   z = h*prod(X-x) with deg h <= e-tau-1 over >= a-e roots off-support (PR2), and a coupled
   match budget T >= A-e+tau+1+u (PR3); <= e tangent slopes, and for q >= 2^168 the whole
   tangent contribution fits the budget (PR4: r <= 2^40-1 <= floor(q/2^128)).

**EXACT RESIDUAL OF THE RED AT PIN (the leaf set):** rate_half_band_closure stays TARGET —
one red, re-posed; NO new TARGET/CONJECTURE nodes anywhere (all 12 new nodes PROVED;
`dli_harmonic_conductor_ledger` does not exist in the pin dag — grep count 0). The open
content is now exactly:
- locate a field-dependent candidate a_RH(q) >= k + sigma_0 + 1 (sigma_0 = 8,594,128,895);
- prove the two safe-side numerators there: B_ca^far(a_RH) <= floor(q/2^128) (plain
  correlated-agreement upper problem for column-far pairs) AND S_sparse(a_RH) <=
  floor(q/2^128) (budget-restricted sparse mutual layer; for q >= 2^168 only the coupled
  non-tangent system (PR1)-(PR3) remains; for 2^128 < q < 2^168 the tangent term must also
  be counted — PR4 does not cover that slice);
- prove the adjacent lower witness at a_RH-1 (the pole floor reaches only sigma_0; a NEW
  lower family is needed at any candidate beyond it).

### Guard (b) — trigger legitimacy: PASS

The MCA trigger object used is the distinct-bad-slope count vs floor(q/2^128) — exactly
epsilon_mca <= 2^-128, the prize MCA object — obtained from the list by the EXACT conversion
E(q,L) (collision pricing at a good pole + Cauchy-Schwarz), NOT by threshold substitution.
Three independent confirmations: (i) statement/claim_contract explicitly disclaim identifying
the thresholds and record that the convenient trigger `L > (q-n)/k` FAILS here (verify.py
audit prints trigger_q_over_k_fails=1: L_q ~ 2^203.08 < (q-n)/k ~ 2^216 at the cap — the
conversion is load-bearing, no surrogate); (ii) the collision charge is priced exactly
(log2 M_q = 203.0794 vs log2 L_q = 203.0796 — 0.00019 bits paid); (iii) the wave-8 guard
sentence's two-triggers separation is preserved (conversion loses (q-n)/(q-n+kL), not free).
Caveat honestly noted: floor(q/2^128) appears on BOTH sides (list budget and MCA slope
budget) — that is the prize's own numerology, not a surrogate reuse; the OBJECTS differ and
are converted exactly.

### Question (c) — status flip audit: JUSTIFIED AT PIN

Net flip: NONE (TARGET at base, TARGET at pin). The transient TARGET->PROVED->TARGET arc is
manual, documented in QUALITY.md, self-corrected by v4's own scope audit; not an
auto_discharge sweep (no gate="all" mechanics; band_closure was TARGET not CONDITIONAL).
The FINAL re-pose (fixed-band determination -> field-dependent adjacent certificate) is a
GENUINE goalpost move but a FORCED one: the old pose presumed sigma* is the crossing, and
that presumption is now refuted by theorem. Import as dated addenda (w9-C1), never as
statement replacement.

### Question (d) — hand-traces + replays: ALL SOUND / ALL PASS

- `rate_half_cyclic_simple_pole_mca_floor` HAND-TRACED SOUND end-to-end: pole trick
  (f_alpha=U/(x-alpha), g_alpha=-1/(x-alpha); folded word at z=P_i(alpha) agrees with
  (P_i(X)-P_i(alpha))/(X-alpha) in C on every agreement point); g_alpha-no-explanation lemma
  ((X-alpha)G+1 has >k roots but value 1 at alpha); CA-bad -> MCA-bad chain (mutual is the
  stronger conclusion); collision average over q-n poles (<= k*C(L,2) colliding pairs total,
  P_i-P_j nonzero deg <= k); sum r_j^2 <= L + kL(L-1)/(q-n); Cauchy-Schwarz M >=
  L(q-n)/(q-n+kL); E increasing in L; identity 1/E(q,lambda_q) = Nq^d/B + kq/(q-n) exact;
  q/(q-n) <= n+1 for integer q > n. s=c-1 legitimacy INDEPENDENTLY RE-DERIVED from the
  wave-8-audited construction: degree blocks [ic, ic+c-1] tile (disjoint for any s<c); the
  >=k part depends only on (a_0..a_{d-1}) for any s<c (blocks i >= N/2 - s/c => i >= N/2
  for all s<c; a_{N/2}=delta fixed); T_0 = any s-subset of the excluded b_0-fiber (size c)
  => s=c-1 admissible; count C(N-1,m)/(Nq^{d-1}) manifestly s-free.
- `rate_half_mca_sparse_layer_reduction` HAND-TRACED SOUND: column-far case (bad iff line
  close, since mutual extension would contradict column-far); column-close case (translation
  by p_1+gamma*p_2 bijects witnesses and mutual extensions; sparse pair with
  |supp(e1) u supp(e2)| <= r); converse inclusions give equality (MS1).
- `rate_half_sparse_pinning_rigidity` HAND-TRACED SOUND: tangent count <= A <= e (one slope
  per active coordinate); forced active match (else (z,0) explains the witness mutually);
  z != 0 for non-tangent; root count off support >= n-e-r = a-e => normal form (PR2) with
  deg h <= e-tau-1 (e <= tau => no nonzero z => all bad slopes tangent); mismatch partition
  (A-T)+u+w_out <= r; root count k-1 >= n-e-r+(A-T)+u => (PR3); 2^168-128=40 arithmetic (PR4).
- Verifier replays (ramguard tiny, mini-tree + pin dag.json): 6/6 PASS —
  pole floor verify.py (toy=(3,2,3) exhaustive p=17 replay incl. two-sided cap asserts
  `<2^53 and not <2^52`, `<2^82 and not <2^81`) + verify_audit.py (list_bits=204
  bad_slope_bits=204 required_list_bits=129 trigger_q_over_k_fails=1); cyclic floor
  verify.py (cap_margin_bits=75.079624489, boundary 256.036659972895 — unchanged by the
  s=c-1 edit) + verify_audit.py (support_checks=3472 constant_checks=21); sparse layer
  verify.py (EXHAUSTIVE tiny rows (3,3,1),(3,3,2): B_mca == max(B_far,B_sparse) at every
  agreement, far-case lemma close_slopes==bad asserted); pinning rigidity verify.py
  (bad_witnesses=7760 nontangent=2400 tangent_bits=40). Fail-open hygiene present in all
  (nonempty populations, two-sided asserts, dag-edge checks).
- Independent constants (w9_checks.py, own code): log2 C(524287,264192)=524254.0796;
  sigma*=2048*2^22+2,978,146=8,592,912,738; sigma_0=2048*2^22+2^22-1=8,594,128,895
  (delta = 1,216,157); boundary (128+log2B-log2N)/2048 = 256.0366599729 > 256; list margin
  75.0796 bits at cap; N*Q^2048 < 2^53*B two-sided; k(n+1) < 2^82 two-sided; bad-slope
  count M_cap: log2 = 203.0794, exceeds q/2^128 by ~75.079 bits; L_cap*k < Q-n (trigger
  separation); E > 2^-83 verified in exact integers at q = n+1, 3(n+1), 2^200, 2^256; own
  p=19/n=16/k=3 conversion toy PASS (12 line-word checks, g-lemma at every pole,
  collision-average promise).

### Cross-wave consequence (the biggest master-side item of the wave)

The s=c-1 lemma applies verbatim to the LIST object too: the SAME deep list exceeds
q/2^128 at excess sigma_0 > sigma*, so the rate-half LIST unsafe edge also extends past
sigma* and the list crossing is NOT at sigma*/sigma*+1. Consequently on MASTER (wave-8
import):
- rate_half_band_closure/statement.md addendum sentence "With the banked safe side, the
  rate-1/2 LIST crossing is DETERMINED" — OVERCLAIM (no safe-side theorem exists; and the
  claimed crossing point is now refuted). Needs a dated correction addendum.
- list_adjacency_closing/conditional.md PREDICATE SWAP paragraph "the residual band's list
  crossing is determined by theorem, so the list-side hypothesis is discharged" — OVERCLAIM:
  the theorem supplies only the UNSAFE side; the rate-half list SAFE side has no owner
  (master's own rate_half_coverage_gap + list_corridor_ledger scope: clean rates only;
  sigma* was only the corridor map's MEAN-crossing estimate). Needs correction addendum;
  the conditional claim of list_adjacency_closing is NOT currently deliverable for the
  rate-half row without a new safe-side input.
- v4's OWN list_adjacency_closing/conditional.md at pin STILL carries the stale sentence
  "The banked list-safe side above sigma* supplies the next agreement index" — v4 internal
  inconsistency (w9-C4): v4 corrected the MCA texts but not the list assembly text.

### Custody (cluster 1)

- v4 in-place rewrites of master-shared files (import as dated addenda, master text
  preserved): rate_half_band_closure/{statement.md (rewritten twice), conditional.md,
  proof.md}; rate_half_cyclic_rotated_prefix_floor/{statement.md, proof.md, verify.py,
  claim_contract.md} (s=c-1 re-instantiation — content forced, form= addendum);
  adjacency_closing/conditional.md, mca_safe/conditional.md, mca_grand/conditional.md
  (predicate-role rewording); P6_RATEHALF_SIBLING.md + notes/pro_brief_razor.md
  (superseded banners — these are APPEND-style, importable as-is).
- QUALITY.md: 15db64d9 EDITED a prior execution-log block in place ("This closes the list
  branch, not the red node." -> "This closed the list branch but, at that time, not the red
  node..."). Historical log blocks are append-only — restore original sentence + append
  (w9-C5, minor).
- New node folders rate_half_cyclic_simple_pole_mca_floor (7 files),
  rate_half_mca_sparse_layer_reduction (6), rate_half_sparse_pinning_rigidity (6):
  IMPORT-CLEAN verbatim (background/ placement as at pin).
- tools/conjectural_mca_delta.py: rate-half branch retired (returns no value; explicit
  refutation note). Import: YES (regression check re-scoped to clean rates + historical-
  candidate-inside-unsafe-interval check).

### Cluster 1 verdict

IMPORT-WITH-REPAIRS. The three new PROVED nodes are IMPORT-CLEAN. The re-pose of
rate_half_band_closure is mathematically FORCED (refutation is unconditional) but must land
as dated addenda; the wave-8 addenda on master need the w9-C2/C3 correction addenda; the l
ist-side "determined" claims must be retracted to "unsafe side proved through sigma_0;
safe side open, field-dependent". The red is STRICTLY NARROWED (safe side exactly reduced to
two numerator objects + tangent slice), and the unsafe bracket STRICTLY EXTENDED
(+1,216,157 excesses), but remains OPEN.

---

## CLUSTER 2 — WCL (2,6) RECURSIVE-NORM CLOSURE (b06971bf + 17617e41 + 9359b038 + 619aa6ea)

**SLOT VERDICT: (2,6) CLOSED on every official row — IMPORT-WITH-REPAIRS (repairs are
hygiene-only). Residual of record becomes FOUR slots (1,5),(1,6),(2,7),(4,9).**

### The argument (hand-traced SOUND)

1. Quotient (proof section 1): the rebasing symmetry (a,b,c) -> (-a, b-a, c-3a) (and the
   y-analogue) leaves F, G literally invariant (w_i -> w_i/x^2, x^1024=1 — re-derived);
   odd Galois dilation conjugates them (norm-invariant). Exponent map re-derived
   independently (x'=1/x, y'=y/x, d'=d/x^3). Orbit coverage sound.
2. Obstructions: w_i = u*z_i are roots of T^3 - sigma T^2 + theta T - prod with
   sigma=-u^2, theta=u(uA-B-d), prod=du^3 (re-derived: C=(uA-B-d)/u equals the
   Newton-forced e_2 from the cubic-moment relation — identity u^3-(1+x^3+y^3)=3uA-3B
   re-derived); doubling identities e1(w^2)=e1^2-2e2, e2(w^2)=e2^2-2e3e1, e3(w^2)=e3^2
   re-derived; F = e1(w^1024)-3u^1024, G = e2(w^1024)-3u^2048 (NOTE: proof.md's "T_1024"
   is the PAIR-PRODUCT elementary symmetric, not the power sum p_2048 — see w9-C7).
3. Saturation soundness: official relation => ring surjection Z[zeta_1024] -> F_q kills
   both => q | gcd(|NormF|,|NormG|); q | Norm(u) would give an odd-conjugate u=0 = an
   official reduced weight-3 order-1024 relation, excluded by the PROVED (master-imported)
   dli_wcl_ell2_weight3_ambient_exclusion (dependency correctly the ell=2/order-1024 node);
   so gcd-removal of Norm(u) is sound and official q must divide g_sat.
4. Nonzero branch: 404,230 candidates, complete PARI factorizations, 443 primes, ALL with
   v_2(p-1) <= 18 < 41 => no official q. Recursive norm identity
   Res(X^n+1,f) = Res(Y^(n/2)+1, f_0^2 - Y f_1^2) re-derived (root pairing +-alpha);
   X^512+1 => nine halvings ("nine polynomial squares" consistent).
5. Double-zero branch (the 510): F=G=0 identically => e1(v)=e2(v)=3, e3(v)=d^1024=1 for
   v_i=z_i^1024 => (T-1)^3 => z_i in mu_1024 (re-derived); complement sum -u => six-term
   ZERO SUM of 1024th roots; power-of-two vanishing-sum lemma (induction on the degree-2
   tower — classical, correctly proved) => antipodal pair => violates the reduced-support
   guard. WHAT EXCLUDES THE 510: they are EXACTLY the antipodal-mirror family
   c = 512+a+b (complement = {-1,-x,-y}) — verified independently, see below.

### Independent verification (w9_c2_census.py + w9_c2_digest.py — my own code)

- Legal pairs: 521,220 = C(1023,2) - 1022 - 511 (analytic + brute) — EXACT.
- Pair orbits: 1,514 with size histogram {2:2,4:4,8:10,16:22,32:46,64:94,128:190,256:382,
  512:764} summing to 521,220 — EXACT (independent BFS).
- Combined census: **404,740 orbits reproduced EXACTLY** by an independent union-find over
  the 1,550,336 presentations (rebasings + pair-stabilizer action on c); presentation
  multiplicity histogram matches EXACTLY (16 classes, weighted sum = 1,550,336).
- Structural identification (new mathematical fact, useful for the master import note):
  the 510 double-zero candidates are EXACTLY the mirror-family orbits (c=512+a+b; one per
  pair orbit pre-quotient, 1,514 -> 510 after the 3-way rebasing quotient); every ledger
  structural candidate satisfies c ≡ 512+a+b (mod 1024) and the ledger set == my computed
  mirror-orbit set.
- Candidate-file digest closure (Modal): rebuilt the canonical candidate list with the
  production canonicalization; representative digest 677871a7... matches; ALL 3,163
  per-batch candidate_digests match the ledger; aggregate_candidate_digest matches;
  anchors (1,2,26),(1,2,31),(1,2,515) are genuine canonical candidates.
- Modular valuation spot checks (Teichmuller lift mod q^3, my own doubling code):
  candidate (1,2,26) at q=65537: v(NormF)=v(NormG)=2, min=2 == ledger exponent 2;
  (1,2,31): v=1/1 == exponent 1; 65537 never divides Norm(u) on these (saturation
  survival); structural (1,2,515) vanishes at ALL 512 embeddings @12289; generic control
  does not. NOTE (documented): F- and G-divisibility may come from DIFFERENT embeddings —
  gcd certificate is a conservative superset of the same-embedding official semantics; fine
  for exclusion.
- Verifier replays: node verify.py PASS locally under ramguard tiny (full 626-node
  Pocklington graph re-validation with real Fermat/gcd witness checks, recursion, trial
  division < 10^4 exact; batch coverage contiguity; digest chains; v_2 recomputed from the
  443 primes; 6/6 mutation controls trip). split16 verify.py PASS (q=65537, order/AF/S16
  checks, 6 mutations).

### b06971bf (split16 counterfixture) as history import: IMPORT-CLEAN

Genuine guarded weight-6 double relation over GF(65537) (E={0,180,211,585,852,903},
omega=3^64; v_2(q-1)=16 < 41): proves the slot is NONEMPTY at low valuation, so any closure
MUST be gated on v_2(q-1)>=41 — exactly what the norm certificate delivers (max v_2 found
= 18, and 65537 itself appears among the 443 supporting primes; coherent). Honest scope
section ("not an official WCL counterexample"). Route-cut node, correctly ev-wired to the
zone.

### Consistency with master's ledger

- Deps: dli_wcl_ell2_weight3_ambient_exclusion + dli_wcl_ell2_weight6_triple_cubic_router
  both PROVED on master (wave-8 import) — edge orientation correct (router req-> exclusion).
- official_terminal_attack.md: new "Weight-six recursive-norm closure (2026-07-16)" section
  is additive; residual updated five -> FOUR slots (1,5),(1,6),(2,7),(4,9). TWO small
  in-place tense edits of prior history text ("The current residual set is" -> "Before...,
  the residual set was"; "remains open" -> "remained open at that checkpoint") — content-
  neutral but see w9-C6 (append-only law).
- dli_primitive_matching_truncation_majorant: req edge added FROM the new exclusion, but
  the majorant statement still says K=85 at ell=2 (valid but unsharpened; closing (2,6)
  supports K=floor(512/7)=73). The edge is forward-wiring; no unsoundness (larger K =
  weaker, still-true bound). Minor note w9-C8.
- Trust gap (mirror of w8-C12): the local verifier trusts the per-batch NORM/FACTOR values
  via digests pinned to the production Modal run (full sweep ~44 CPU-h, ap-Sjm8psGJ...);
  full re-sweep beyond audit budget — DEFERRED, mitigated by: candidate-file digest closure
  (above), 2-candidate valuation recomputation, 510-structural exact identification, and
  the in-worker factor-product==value assertions + fail-closed batches. Importer keeps
  notes/verify_full_remote.py wired.

### Cluster 2 catches/hygiene

- w9-C6 (hygiene): two in-place tense edits in official_terminal_attack.md history text
  (convert to addendum phrasing on import or accept as content-neutral with a note).
- w9-C7 (documentation): proof.md's "T_1024" notation reads like a power sum; production
  code (and the correct converse argument) uses the PAIR-PRODUCT elementary symmetric
  e2(w^1024). Suggest one clarifying sentence in the imported proof.md addendum. (Both
  choices are mathematically workable; the shipped one is consistent everywhere.)
- w9-C8 (minor wiring): majorant req edge added without the K=85->73 sharpening.
- w9-C9 (hygiene, flagged by the task): commits 17617e41 and 9359b038 have MALFORMED TITLES
  (title line is a "Co-Authored-By: Claude Opus 4.8" trailer; the real subject is lost).
  History import should reference them by SHA with a descriptive note.

### Cluster 2 import file list (verbatim from pin 4442ffd5)

- background/nodes/dli_wcl_ell2_weight6_recursive_norm_exclusion/{statement.md, proof.md,
  result.md, verify.py, dependency_subdag.md, notes/verify_full_remote.py,
  notes/verify_certificate_modal.py}
- background/nodes/dli_wcl_ell2_weight6_split16_counterfixture/{statement.md, proof.md,
  verify.py, audit.md, certificate.json, claim_contract.md, dependency_subdag.md}
- experiments/prize_resolution/{dli_wcl_ell2_weight6_recursive_norm_full_result.json (5.8MB),
  dli_wcl_ell2_weight6_recursive_norm_prime_cert_result.json.gz,
  dli_wcl_ell2_weight6_recursive_norm_full_modal.py,
  dli_wcl_ell2_weight6_candidate_orbits_modal.py,
  dli_wcl_ell2_weight6_recursive_factor_pilot_modal.py,
  dli_wcl_ell2_weight6_recursive_norm_benchmark_modal.py,
  dli_wcl_ell2_weight6_recursive_norm_prime_cert_modal.py,
  dli_wcl_ell2_weight6_norm_gcd_probe_modal.py (update), ..._probe_result.json}
- dag: 2 new PROVED nodes + 5 edges {router->exclusion req; weight3 dep per node header;
  exclusion->zone ev; split16->zone ev; router->split16 req; exclusion->matching_majorant
  req}; zone official_terminal_attack.md + statement.md updates as ADDENDA with w9-C6 tense
  repair; residual ledger five -> four slots on master's file of record.
- tools/verifier_manifest.json + modal_verifier_replay.json entries merged not copied.

---

## CLUSTER 3 — PMA RATE-HALF TAIL LADDER (0469c8c2, 27ee6406, d4d5b376, 2e02fcd2, d4bcebea, deb8d257, 36b3c932)

**VERDICT: IMPORT-WITH-REPAIRS (custody-only). Five new PROVED reduction nodes, chain
hand-traced end-to-end, all verifiers PASS. The ladder reduces the v4-architecture rate-half
M=4,t=3 full-petal tail to ONE exact guarded object; it does NOT change master's
l1_mixed_petal_amplification open-content sentence (the rate-half full-petal tail is
clause-(P)-side on master per wave-8 guard (c)).**

### The chain (each node consumes the previous; all ev into petal_mixed_amplification)

1. `pma_ratehalf_core_triple_excess_reduction` (0469c8c2; req <- three_petal_projective_
   johnson_bound): fixing a touched triple identifies contributors with an ordinary core
   RS list (N=4ell+b-2, K_0=ell+b-1, m=2ell+b+a-2); Johnson-denominator identity (CT3)
   m^2-N(K_0-1)=ell(4a-b+2)+a^2+2ab-4a RE-DERIVED (grid-verified in w9_checks); three
   contributors force overlap bonus B_3>=2(K_0-1)+3a (pointwise counting re-derived), which
   after gcd removal forces a nonconstant rational map phi=A_0/B_0 with
   |phi^-1({0,1,inf}) cap (C\T)|>=2r+3a, hence r>=3a (fiber counting re-derived). Absent
   such a certificate: <=2 per cell => <=8n per source. HAND-TRACED SOUND.
2. `pma_ratehalf_source_aligned_gcd_excess` (d4d5b376): the CRT/Euclid construction
   L_C E_c = P_* + L Y exposes y=-P_*/L as a 3-dimensional source quotient code of min
   weight K_0 (injectivity traced); the excess certificate becomes the exact gcd identity
   u_12+u_13+u_23-tau >= 2(K_0-1)+3a via inclusion-exclusion on exact agreement sets
   (all four gcd-degree=intersection-size identities re-derived, L_C squarefree).
   HAND-TRACED SOUND.
3. `pma_ratehalf_source_crossratio_fiber_reduction` (2e02fcd2): affine label invariance
   (H'=alpha H+beta Q_0 re-derived from L_C=P_0+LQ_0) => labels normalize to (0,1,lambda);
   quotient mod RS(C,K_0) is 2-dimensional (constant-label line = intersection, degree
   argument traced); CRT idempotent factorizations P_2=L_1L_3R_2, P_3=L_1L_2R_3 (divisibility
   traced); weighted overlap identity sum max(0,r_x-1) = gcd bonus; exceptional set B_3
   (=core zeros of R_3, <=ell-1) removed at weight 2 => residual >= 2b+3a-2 incidences,
   each voting the unique lambda via (XR6). HAND-TRACED SOUND (incl. the "charging
   exceptional points once is invalid" guard).
4. `pma_ratehalf_two_petal_support_fiber_reduction` (d4bcebea): exact bijection between
   contributors and guarded m-subsets S: V_S=rem_{L_2}(L_3R_2 L_S^{-1}), Phi(S)=
   rem_{L_3}(L_S V_S (L_2R_3)^{-1})=lambda, deg V_S<=ell-a, gcd(V_S,L_C/L_S)=1
   (mod-L_2/mod-L_3 congruences + degree bound deg V_S <= 3ell+b-2-m = ell-a re-derived).
   NORMAL-DEPTH SOUND.
5. `pma_ratehalf_complement_linear_slice_reduction` (deb8d257 + 36b3c932; req <- two_petal +
   three_petal_mu_basis_reduction; ev -> shared_census_kernel): E_c=L_1*Etilde with Etilde a
   unit mod M=L_2L_3; the cell is in exact bijection with the split-divisor atom (LS6)
   {D|L_C monic, deg D=2ell-a, deg rem_M(D*Etilde)<=ell-a, gcd(D,rem_M(D*Etilde))=1};
   unguarded slice W_(lambda,a) has dim ell-a+1 (unit-automorphism argument traced); the
   36b3c932 mu-basis reconciliation (LS8-LS10) shows the truncated slice dimension equals
   the wave-8 mu-basis freedom (ell-2a+2 in the live branch) — the coordinate change does
   not shrink the freedom (honest no-free-lunch note). NORMAL-DEPTH SOUND.

### Fixture repair (27ee6406) — VERIFIED NECESSARY AND CORRECT

The original 0469c8c2 route-cut fixture row (ell,b,a)=(8,7,1) has J=3>0 (MY independent
check: 8*(-1)+1+14-4=3; equivalently 22^2-37*13=3) — OUTSIDE the nonpositive-J tail, hence
useless as a tail route cut. The repair moves it to the first J=0 tail row (11,7,1):
J=0 exact, (N,K_0,m)=(49,17,28), bonus 35=2*16+3 — all reproduced in w9_checks. At pin the
fixture is correct and the scope text is honest ("arbitrary core word... no rational-word
source lift is supplied or certified" — route cut, not a PMA counterexample).

### Verifier replays (ramguard tiny): 5/5 PASS

core_triple (map_cases=289 tail_cells=3,755,175 zero_j=254 smooth fixture replayed exactly:
order=100 core=49 bonus=35 agreement=28 J=0; mutations=7); gcd_excess (source_words=4913
min_weight=4 aligned_cases=2000 mutations=7); crossratio (affine_cases=400 votes=122
tail 35=20+15 mutations=8); two_petal (lambdas=15 supports=35 contributors=1 hostile_layouts=4
mutations=7); linear_slice (supports=525 guarded=1 slice_dim=11 codim=11 a3_dims=9/7
mutations=7). Nonempty populations + mutation controls everywhere.

### Roadmap/statement claims checked

- "M<=6 at 1/8, M<=14 at 1/16 have no strict full-petal residual": exactly the wave-8-audited
  rate sieve corollary (M<=r-2 => ell>=k+1 > d) — re-verified arithmetically in w9_checks.
- "no rate-quarter M=4,t=3 branch remains": the wave-8-audited projective-Johnson positivity;
  unchanged in this range.
- The petal_mixed_amplification statement growth (dag 783->956 chars; statement.md +~130
  lines over the 7 commits) is the ladder-status record; final open list in v4's
  architecture: "source-coupled rate-half certificates (now = the (SF7)/(LS6) atom),
  M=4,t=2, larger-M full petals, partial petals". Custody: in-place edits of v4's re-posed
  statement — on master these fold into the wave-8 surgery's dated addendum, TAKEN AT THE
  WAVE-9 PIN (supersedes the wave-8-pin version of the same addendum).

### Effect on master's l1 red

NONE on the open-content sentence (u+e -> infinity mixed/partial profiles with
Omega(n/log^2 n) rich-fiber forcing) — this ladder lives in the full-petal M=4,t=3 stratum,
which master owns via the clause-(P) chain (wave-8 guard (c)). Import value for master: (i)
evidence/crosswalk — add one paragraph to l1's v4_pma_crosswalk.md noting the v4-side
rate-half tail is now an exact one-parameter split-divisor atom; (ii) the new ev edge
pma_ratehalf_complement_linear_slice_reduction -> shared_census_kernel correctly identifies
the atom as a BC/SCK-type split-in-subspace object — useful wiring for the BC lane.

---

## CLUSTER 4 — C36 + HGE4 FIRST TOUCHES AND WEIGHT-5 STREAMING (characterize + verdict/DEFER)

1. **e7967d2c — f3_h3_local_cancellation_root_bound (PROVED, background/): PROOF-type;
   DEFER import (dependency-gated).** Localizes hidden cancellation in the C36 local-cluster
   valuation: F_t(C)=e_{r_0}(C-b_1..C-b_U) has exact reduced degree r_0=U-9 (leading coeff
   binom(U,r_0) != 0 mod p), overvaluation kappa_gamma>0 iff F_t(c_gamma)=0 mod Pfrak => at
   most U-9 first-order cancellation residues; at U=10 the unique residue is the mean of the
   b_i. Honest nonclaim ("not a bound for Z_9... C36' still needs the main joint
   count/weight theorem"). Verifier PASS (checks=1757). BUT its req parent is
   f3_h3_local_cluster_valuation — the endpoint of wave-8's UNAUDITED Cluster A chain
   (deferred by wave-8, still unaudited). Import must wait for the Cluster-A audit; take
   this node in the same batch. Pre-registered expectation: the DVR/elementary-symmetric
   argument is self-contained modulo the parent's kappa_gamma definition; falsifier = the
   parent's overvaluation object not matching (CR2)'s local form.
2. **9fbb4612 — f3_h3_pgl2_conjugacy_route_fence (PROVED, background/): FENCE-type;
   DEFER with Cluster A (deps are Cluster-A nodes).** Proves the product-fiber family
   f_t(X)=1+t/(X-1) and quotient-fiber family g_q(X)=1+q(X-1) are PGL2-conjugate only at
   the isolated multiplier q=-1 (f_t ~ g_{-1} iff t is a square), pays the isolated
   contribution X_{-1}<198 n^{4/3} (17X_{-1} < (1683/200)n^2), and re-poses the residual as
   (CF3) 17*sum_{t != 1,-1}(P(t)-18)_+ R(t) <= (58317/200)n^2. Honest fence scope ("rules
   out converting C36' to one ordinary shifted-energy problem by direct PGL2 conjugacy";
   does NOT rule out non-conjugacy correspondences). Verifier PASS (checks=2026). C36 red
   stays TARGET; open range n^2 <= p <= 6^{n/4} unchanged.
3. **Also in-range on the C36 lane (bookkeeping, no substance):** the dag statements of
   f3_h3_uniform_product_fiber_stepanov (37 -> 33 n^{2/3}) and
   f3_h3_product_fiber_codegree_budget (R(s/t)+1 -> R(s/t), D_H+n-1 -> D_H) are
   DAG-TO-FILE SYNCS — the node FILES already carried the sharp forms at ae2e5dd5 (checked
   byte-level); only the stale dag entries were updated, plus a 5-line cross-reference
   append to the codegree statement.md. The future Cluster-A audit must take these nodes at
   the wave-9 pin.
4. **2ef01fdc — HGE4 norm-gate contract repair: IMPORT-CLEAN (contract files only).**
   dag statement byte-identical to master's (incl. catches #99/#100 verbatim); the commit
   creates the missing node contract FILES (statement.md transcribing NG-COUNT, the five
   deletion columns, posedness rule "3/5 deletions operational — a counterexample must
   implement U2-boundary + DLI/skew first", nonclaims incl. "NG-ZERO is not claimed") and
   adds RAW-NG (pre-deletion count <= 14n^3) as a SOUND sufficient interface (deletion
   monotonicity => N_strip <= N_raw — trivially correct). No goalpost move, no status
   change (TARGET). Verifier PASS (monotonicity_cases=441). Master can import the three
   files into its own f3_hge4_norm_gate_count folder directly.
5. **Weight-5 streaming state (26beb2d7, f2a8060b, 29abd2cd, e3ac81c1, da465600, 982cf29d):
   INFRA-IN-FLIGHT; DEFER (nothing to audit yet).** This is the terminal ell=1 weight-5
   sweep (slot (1,5)): ORDER=512, 2,296,920 affine classes, representative file sha-pinned,
   pilot result (60k lines) shows sampled rows with max_v2(p-1)=21 so far, factor-time
   percentiles, 8 generic-norm controls, errors=[]; the other five commits are worker-shape/
   timeout/streaming hardening. NO dag node minted; NO claim made at pin. Pre-registered
   expectations for the eventual (1,5) audit: same certificate shape as (2,5)/(2,6)
   (complete class coverage + digest chains + saturated norm gcds + recursive Pocklington
   graph + max v_2(p-1) < 41 + a structurally-identified zero branch); falsifiers: any
   eligible (v_2 >= 41) factor, non-contiguous coverage, or a structural branch without a
   char-0 exclusion argument. Pilot's max_v2=21 is consistent with closure but proves
   nothing yet.
6. **d84e6def — roadmap-only commit ("Align roadmap with upstream v13 focus"): FYI-import.**
   Contains the upstream v13 adoption-gate table updates (incl. the rate_half_band_closure
   task row consistent with the cluster-1 re-pose).

---

## CATCHES (w9-C#, local numbering)

- w9-C1 (custody, cluster 1): rate_half_band_closure statement.md/conditional.md/proof.md
  rewritten IN PLACE twice in-range (PROVED pose, then RH-ADJ pose); on master both re-poses
  land as ONE dated addendum with master text preserved (supersedes/extends the wave-8
  addendum). Same for the cyclic node's s=c-1 re-instantiation and the
  adjacency_closing/mca_safe/mca_grand conditional rewordings.
- w9-C2 (wave-8 self-correction, master-side): master's wave-8 addendum sentence "With the
  banked safe side, the rate-1/2 LIST crossing is DETERMINED" is an OVERCLAIM — v4's scope
  audit (56c25337) found the safe side above sigma* was planning prose (no in-repo theorem;
  Paper D pincer stops at half distance; r2_clean_rates excludes rate 1/2), and the s=c-1
  floor proves list-unsafety THROUGH sigma_0=8,594,128,895 > sigma*. Master needs a dated
  correction addendum: list unsafe side proved through sigma_0; list safe side OPEN
  (field-dependent); crossing NOT determined.
- w9-C3 (same, list_adjacency_closing): master's PREDICATE SWAP addendum "the list-side
  hypothesis is discharged" overclaims — the PROVED cyclic floor supplies only the UNSAFE
  side; the rate-half list SAFE side has no owner post-swap. Correction addendum + the
  conditional's claim scope for the rate-half row must be marked bracket-grade until a safe
  side lands.
- w9-C4 (v4 internal inconsistency, cluster 1): v4's OWN list_adjacency_closing/
  conditional.md at pin still says "The banked list-safe side above sigma* supplies the next
  agreement index" — contradicted by v4's own refutation.md. Do NOT import that sentence;
  flag to Codex.
- w9-C5 (custody, minor): 15db64d9 edited a PRIOR QUALITY.md execution-log block in place
  ("This closes the list branch, not the red node." -> retrospective wording). Log blocks
  are append-only: restore + append on import.
- w9-C6 (hygiene, cluster 2): two in-place tense edits of history text in
  official_terminal_attack.md (content-neutral; convert to addendum phrasing on import).
- w9-C7 (documentation, cluster 2): proof.md's "T_1024" is the PAIR-PRODUCT elementary
  symmetric e2(w^1024) (per production code), not the power sum p_2048 the notation
  suggests; one clarifying sentence in the import addendum. (Independently confirmed the
  e2 version is what the certificate computes AND that both formulations force roots of
  unity; the shipped one is consistent everywhere.)
- w9-C8 (minor wiring, cluster 2): req edge recursive_norm_exclusion ->
  dli_primitive_matching_truncation_majorant added WITHOUT the K=85 -> 73 sharpening
  (statement unchanged; still sound since larger K is weaker). Either apply the sharpening
  on import (K=floor(512/7)=73 at ell=2, with the (2,6) closure as its justification) or
  drop the edge until used.
- w9-C9 (hygiene): commits 17617e41 and 9359b038 have MALFORMED TITLES (title line = a
  Co-Authored-By trailer; subject lost). Reference by SHA + descriptive note in import
  records.
- w9-C10 (trust-gap note, cluster 2, mirrors w8-C12): the (2,6) certificate's per-candidate
  norm values/factorizations are digest-pinned to the production Modal run (~44 CPU-h);
  full re-sweep DEFERRED. Mitigations delivered this wave: complete candidate-file
  reproduction (all 3,163 batch candidate digests + aggregate + representative digest
  matched from scratch), independent 2-candidate valuation recomputation matching recorded
  exponents, exact identification of all 510 structural cases as the mirror family, local
  full Pocklington/coverage/v_2 validation with 6/6 mutation trips.

## DEFERRED VERIFICATIONS (pre-registered)

1. Wave-8 Cluster A (17 f3_h3_* nodes) + this wave's two f3_h3 additions (root bound,
   PGL2 fence) + the two dag-sync nodes — audit as ONE batch at the wave-9 pin (or later).
   Expectations unchanged from wave-8 item 1; add: (CR2) must match the parent's exact
   overvaluation object; the fence's X_{-1} constants (198 n^{4/3}, 1683/200, 58317/200)
   must recompute from the Cluster-A Stepanov constants (33 n^{2/3} file-form).
2. Full (2,6) norm-sweep replay (w9-C10) — only if the slot ever becomes load-bearing
   beyond zone bookkeeping; the certificate is otherwise audit-complete.
3. Weight-5 (1,5) terminal sweep — audit when a node/claim lands (expectations in
   Cluster 4 item 5).
4. Post-pin commits (7 already at audit close: 19d19f93, 0b313b01, eb553b92, ce16a7fc,
   e86b0b88, 568178b8, d4e37c9a — all rate-half safe-side/bracket work, 07-17 22:13+,
   plus uncommitted working-tree changes on rate_half_band_closure) — WAVE-10 SCOPE.
   Expectation: they attack exactly the (RH-ADJ) safe-side numerators this wave posed;
   watch for a re-flip of rate_half_band_closure and for any "safe curve" claim that
   silently reuses corridor-conjecture material as theorem.

## IMPORT SURGERY SPEC (exact; statements MERGED never replaced; all v4 content at pin
4442ffd5; ordering: Cluster 2 and 3 are independent; Cluster 1 SHOULD land in the same
master session as the w9-C2/C3 correction addenda so master never carries the corrected
claims and the refutation separately)

### A. Rate-half MCA (Cluster 1)

1. NEW NODE FOLDERS verbatim from pin: background/nodes/rate_half_cyclic_simple_pole_mca_
   floor/ (7 files), background/nodes/rate_half_mca_sparse_layer_reduction/ (6),
   background/nodes/rate_half_sparse_pinning_rigidity/ (6). Dag: 3 PROVED entries + edges
   {cyclic_rotated_prefix_floor -> simple_pole_mca_floor req; simple_pole_mca_floor ->
   band_closure ev; mca_sparse_layer_reduction -> band_closure ev;
   sparse_pinning_rigidity -> band_closure ev}.
2. rate_half_cyclic_rotated_prefix_floor (master node, PROVED): dated addendum "MAXIMAL-
   PREFIX INSTANTIATION (wave-9 audited)" carrying the s=c-1 lemma + sigma_max, band
   "1 <= sigma <= sigma_max"; verify.py updated to the pin version (cap_arithmetic with
   old_sigma+1 <= sigma assert); claim_contract quantifier line updated via addendum.
   Statement dag field: append the sigma_max sentence, do not delete sigma* history.
3. rate_half_band_closure (master, stays TARGET): dated addendum "FIXED-CROSSING REFUTATION
   + FIELD-DEPENDENT RE-POSE (wave-9 audited)" = the pin statement.md body (RH-ADJ,
   RH-BRACKET, RH-SPLIT, pinning-rigidity paragraph) + refutation.md copied verbatim as a
   NEW file + the pin proof.md/conditional.md bodies as addenda; w9-C2 correction paragraph
   in the same addendum (list side: unsafe through sigma_0, safe side open, wave-8
   "DETERMINED" sentence corrected in place-of-record via dated note, original preserved);
   QUALITY.md: append the two 2026-07-17 blocks, restore the w9-C5 edited sentence.
   Dag statement field: replace with the pin RH-ADJ text APPENDED to master's current text
   per house convention for dag statements (master's dag keeps a single statement string —
   recommend the pin text + "[HISTORY: previous poses preserved in statement.md]").
4. list_adjacency_closing (master): w9-C3 correction addendum to conditional.md ("the
   rate-half list SAFE side is not owned; adjacent claim bracket-grade for the rate-half row
   until a safe-side theorem lands; the unsafe witness now reaches sigma_0"); do NOT import
   v4's stale banked-safe-side sentence (w9-C4).
5. adjacency_closing/mca_safe/mca_grand conditionals: dated addenda with the pin texts
   (predicate role = "rate_half_band_closure supplies the complete field-dependent adjacent
   certificate"; pole floor = lower bracket only, not an upper input). P6_RATEHALF_
   SIBLING.md + notes/pro_brief_razor.md superseded banners import as-is (append-style).
   tools/conjectural_mca_delta.py: pin version (rate-half branch retired).
6. verifier_manifest entries for the 3 new verify.py + the updated cyclic verify.py (hashes
   on REPAIRED statement files).

### B. WCL (2,6) (Cluster 2)

File list in the Cluster 2 section above. Dag deltas: 2 PROVED nodes + 5 edges + zone
addenda + residual five -> FOUR slots in master's official_terminal_attack.md (additive
section, w9-C6 tense repair); w9-C8 decision surfaced (recommend: apply K=73 sharpening as
a dated statement addendum to dli_primitive_matching_truncation_majorant citing the (2,6)
closure; else drop the req edge). Register verify.py + notes scripts in the manifest;
merge modal_verifier_replay.json entries.

### C. PMA ladder (Cluster 3)

1. NEW NODE FOLDERS verbatim: background/nodes/pma_ratehalf_{core_triple_excess_reduction,
   source_aligned_gcd_excess, source_crossratio_fiber_reduction,
   two_petal_support_fiber_reduction, complement_linear_slice_reduction}/ (audit.md +
   claim_contract.md + dependency_subdag.md + proof.md + statement.md + verify.py each).
   Dag: 5 PROVED entries + the 10 edges as at pin (chain req edges; ev into
   petal_mixed_amplification; ev complement_linear_slice -> shared_census_kernel; req
   three_petal_projective_johnson_bound -> core_triple; req three_petal_mu_basis_reduction
   -> complement_linear_slice).
2. petal_mixed_amplification (master background/ folder, per wave-8 w8-C4 layout): the
   wave-8 surgery's dated re-pose addendum is UPDATED to the wave-9 pin body of v4's
   critical/nodes/petal_mixed_amplification/statement.md (which now includes the ladder
   section and the corrected open list); same for attack.md/claim_contract.md/
   conditional.md/dependency_subdag.md pin deltas (addendum form). petal dag statement:
   pin text as dated append.
3. l1_mixed_petal_amplification (master critical/): APPEND one paragraph to
   v4_pma_crosswalk.md: the v4-side rate-half full-petal tail is now an exact one-parameter
   guarded split-divisor atom (LS6) with lambda cross-ratio normalization; NOT new open
   content for l1 (clause-(P)-side stratum); the atom is a BC/SCK-type object (ev edge into
   shared_census_kernel) — potential shared attack surface.

### D. Cluster 4

- 2ef01fdc HGE4 contract files: copy critical/nodes/f3_hge4_norm_gate_count/{statement.md,
  claim_contract.md, verify.py} verbatim into master's folder (dag statement unchanged);
  manifest entries.
- f3_h3 nodes (root bound + fence + dag syncs): DO NOT IMPORT until the Cluster-A audit;
  record in the Cluster-A audit queue at the wave-9 pin.
- Weight-5 streaming: no import (no claims); optionally mirror the experiment scripts as
  inactive files if master wants the infra staged.
- d84e6def roadmap deltas: FYI merge.

## PROCEDURAL NOTE

Pin 4442ffd5 held for ALL content reads (`git show 4442ffd5:<path>` throughout; diffs on
pinned SHAs). At audit close the v4 worktree HEAD had MOVED to d4e37c9a (7 post-pin commits,
07-17 22:13+, all rate-half safe-side work) with uncommitted changes in the worktree —
NO contamination of this audit (no working-tree reads of v4); post-pin range is wave-10
scope. One compute-law slip early in the session (a bare `python3 -c` json inspect inside a
pipe, small parse, no incident) — flagged for the record; all replays and checks ran under
ramguard tiny or Modal per the law. Deliverables: w9_findings.md (this file), w9_checks.py
(C1 constants + conversion toy + C3 tail arithmetic — ALL PASS), w9_c2_census.py
(independent pair/combined census + mirror identification + valuation spot checks — ALL
PASS), w9_c2_digest.py (candidate-file digest closure — PASS on Modal), w9_dag_delta.py +
w9_percommit_status.py + w9_dags/ (dag forensics), w9_tree/ (pinned file mini-tree).
