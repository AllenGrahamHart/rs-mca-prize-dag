# Wave-8 fresh-context replay audit — Codex v4 PMA campaign (+ rate-half floors, DLI WCL slots, XR)

Auditor session 2026-07-16. PIN: **ae2e5dd54bdcf2b6b5c7b3d8a031184196720962** (v4 worktree
/home/u2470931/smooth-read-solomin/prize-codex-resolution-v4-20260713, branch
codex/full-prize-resolution-v4-20260713; HEAD == pin at audit start).
Master baseline: /home/u2470931/smooth-read-solomin/prize (read-only), with TODAY's minted red
`l1_mixed_petal_amplification` (TARGET, catch #212) + imgfib CONDITIONAL.
Map: notes/kernel_basis/WAVE8_SURVEY.md. Catch numbering LOCAL (w8-C1...).
READ-ONLY discipline: all pin content via `git show ae2e5dd5:<path>`; replays from scratchpad
mini-tree w8_tree/ under tools/ramguard tiny (Modal for heavy); no writes to either repo.
PROCEDURAL NOTE: HEAD == pin for the entire audit (re-checked at close); no post-pin
contamination. Deliverables beside this file: w8_checks.py (consolidated driver, ALL_PASS =
23 standalone + 9 mini-tree verifiers + independent cross-check), w8_tree/ (pinned
mini-tree), w8_pma_verifiers/ (28 pinned verifier copies), w8_ratehalf_crosscheck.py,
w8b_* (DLI sub-audit scripts: Pocklington/norm/orbit/weight-6 independent recomputations,
flip forensics), w8c_tree/ (XR sub-audit mini-tree). Cluster-3 heavy replay ran on Modal
(16GiB): DLI_WCL_ELL2_WEIGHT5_NORM_GCD_EXCLUSION_PASS orbits=1514 gcds=507 roots=168
prime_nodes=282 max_v2=18 negative_controls=3/3.

## VERDICT LINE

All four audited clusters are importable: Cluster 1 (mixed-petal core: both refutations
HAND-TRACED SOUND, 28/28 verifiers PASS, re-pose faithful-with-crosswalk); Cluster 2
(rate-half list floors SOUND — retires the entire Grand-List-Decoding half of
rate_half_band_closure with 75.08 bits of margin at the cap); Cluster 3 (DLI: slot (2,5)
CLOSED, certificate replayed on Modal + independently spot-checked, six-slot residual ->
five; packaging flip REFUSED, mechanism = auto_discharge sweep); Cluster 4 (XR: NO #158
violation — the fenced RowC-1/16 rank-4 sub-case is legitimately PAID by a new covering-free
theorem; frontier becomes rank >= 5,5,5 / 17,17,15). Guard outcomes: (a) no live
pma_wide_residual conditioning; (b) Linnik family OUTSIDE imgfib's reserve — NO T-KILL,
imgfib survives CONDITIONAL; (c) re-posed target faithful, crosswalk required (different
bucket decomposition, no goalpost shift). 13 local catches w8-C1..C13; custody repairs
specified per file. Cluster A (C36) DEFERRED to wave-9.

Master baselines pinned (re-read this session):
- master dag: pma_wide_residual TARGET (dag-only, NO node folder), petal_mixed_amplification
  CONDITIONAL (background; conditional.md predicates {pma_aux_list_reduction PROVED,
  pma_johnson_regime PROVED, pma_wide_residual}), imgfib CONDITIONAL,
  l1_mixed_petal_amplification TARGET (critical, consumer imgfib), rate_half_band_closure
  TARGET (gate=all), dli_wcl_zone_coverage TARGET (background/nodes/, six-slot residual
  (1,5),(1,6),(2,5),(2,6),(2,7),(4,9) in official_terminal_attack.md), packaging CONDITIONAL
  (gate=all, DELIBERATE), dli_dyadic_k_core REFUTED, dli_marginal_baseline100_coverage TARGET.
- master imgfib statement: "#ImgFib_U(k+sigma) <= n^B once sigma*log2(q_D) >=
  (1+eps)*log2 C(n,k+sigma) and the quotient profile is budgeted" — the entropy reserve IS in
  the master statement (this is what guard (b) is measured against).

v4 vs master dag delta (computed at pin): 690 nodes v4 vs 622 master; 69 NEW nodes (all
PROVED); 1 master node absent in v4 (l1_mixed_petal_amplification — post-fork mint, NOT a
removal); 3 status flips: pma_wide_residual TARGET->REFUTED, petal_mixed_amplification
CONDITIONAL->TARGET, packaging CONDITIONAL->PROVED (REFUSED, see Cluster 3).

---

## CLUSTER 1 — MIXED-PETAL CORE (E3+E6 refutations + re-pose + ~28 PROVED pma_* nodes)

### Verifier replay status (all at pin, ramguard tiny, scratchpad copies/mini-tree)

ALL 28 cluster verifiers PASS at pin:
petal_reserve_rich_fiber_reduction (checks=901 rows=128 min_rich=53 mutations=2),
pma_arbitrary_petal_source_realizability (PASS, mutations=4),
pma_b11_first_match_router (7176 checks), pma_coset_subtwoell_saturation_exclusion
(861,239 rank triples, mutations=3), pma_exact_periodic_owner (128 rows + mutation guards),
pma_full_petal_band_composition (1,053,052 shapes, mutations=3),
pma_official_rate_small_source_degree_sieve (rows=2,086,800, mutations=5),
pma_petal_pattern_root_pinning_ledger (mutations=2), pma_quotient_closure_scope (859 checks),
pma_saturated_mixed_support_kernel (60 patterns, mutations=4), pma_sigma_one_b11_scope
(18,753 checks), pma_sigma_one_d3_background_payment (385), pma_sigma_one_d3_diffuse_
hyperplane_reduction (7029), pma_sigma_one_d3_full_petal_payment (2875),
pma_sigma_one_d3_reciprocal_quadratic_obstruction (33 checks, first=2^22),
pma_sigma_one_d4_generic_source_obstruction (mean_floor_bits=104 vs n6_bits=97, mutations=2),
pma_sigma_one_dyadic_near_coset_owner (615), pma_sigma_one_first_layout_domination (128 rows),
pma_sigma_one_index_two_core_owner (398), pma_sigma_one_low_defect_payment (1154),
pma_sigma_one_odd_lift_boundary_owner (260, mutation_trips=32), pma_sigma_one_paired_core_
abundance (mean_floor_bits=22285), pma_sigma_one_paired_core_normalization (constructed=90),
pma_sigma_one_post_top_allowance (330, mutation_trips=64), pma_sigma_one_variable_defect_
exact_hit_floor (mean_bits=51115 vs n3000_bits=48001), pma_source_paving_bridge (33),
pma_three_petal_mu_basis_reduction (17,680 hilbert checks, mutations=6),
pma_three_petal_projective_johnson_bound (half_paid=8,776,918 half_tail=1,909,782, mutations=5).
Fail-open hygiene: every verifier checked carries nonemptiness asserts and mutation controls
(counts listed); none is a cannot-fail certificate (e.g. d3-RQ checks the threshold first=2^22
both directions).

### Refutation 1 (b9beb6e8): pma_sigma_one_d4_generic_source_obstruction — HAND-TRACED SOUND

(q,n,k)=(65537^2,65536,32768) valid official row (n|q-1 exact). Construction P=1+L_{C\D}W,
|D|=4, deg W<=4; R=W/L_D; agreement on petal point y in T_i iff c_i=R(y). Traced and verified:
(G1) admissible-W count q^4(q-H_0), H_0=C(L,2)+L+5 — each forbidden condition is a NONZERO
linear hyperplane in the 5 coefficients (nonzeroness of collision functional via W=1, W=X
tests: forces y=z); (G2) injection-conditional avoidance 1-2(M-6)/(Q_0-6) (marginal of
unselected label uniform on Q_0-6 unused values, 2 forbidden per petal); exact-six events
disjoint per (D,W), (D,W)->P injective (exact core miss set recovers D, then W=(P-1)/L_{C\D});
(G3) exact integer comparison REPLAYED (numerator 328 bits vs n^6*denominator; mean floor
2^104 > n^6=2^97). Owner escapes traced: (i) agreement set size k+1 ODD => no nontrivial
stabilizer in the cyclic 2-group (orbits = cosets, even size); (ii) dyadic interval
[k-s_n, k+1+s_n], s_n=128, contains only size k=2^15; balanced core caps coset hits at
k/2+6=16390, misses 16379>128 => outside QOWN_cosgrow; (iii) odd-lift killed by the core
antipodal pair {x,-x} with U=1 (2xV(x^2)=0 contradiction). Contradiction chain: all >n^6
codewords primitive+post-owner => in Top ⊔ Post; #Top<=N_top and B_post=n^6-N_top =>
#Post>B_post. Refutes the finite clause of pma_wide_residual as posed. VERDICT: IMPORT-CLEAN.

### Refutation 2 (74225111): pma_sigma_one_d3_reciprocal_quadratic_obstruction — HAND-TRACED SOUND

H order n=2^s, G index-2, A=H\G (union of antipodal pairs since -1 in G). Q(x)=x^{-1}+rx,
r in A: nonzero+injective on A (Q(x)=0 => r=-x^{-2} in G; Q(x)=Q(y) => r=(xy)^{-1} in G).
W=(P*L_D-rL_S)/X: constant term cancels (L_D(0)=-prod(D)=-r*prod(S), L_S(0)=-prod(S)),
degree-5 terms cancel (rX^5 both) => deg W<=3. (2) W(x)=Q(x)L_D(x) on S; fails off S by
-rL_S(x)/x != 0; (3) W(d)=-rL_S(d)/d != 0 on D. Triple count >= N(N-3)/6 (ordered N(N-1)
minus 2N degenerates, /6). Background averaging => (5) binom(M,5)(N-6)(N-3)/6. pi-averaging:
full-petal escape <=10/M (W-Q(x)L_D nonzero cubic with root x => <=2 more roots), antipodal
agreement <=5/M (Q injective) => factor (1-15/M) => RQ-LB exact. (S,D)->f=L_{C\D}W injective
(nonvanishing core positions recover D; (1) recovers S). Trivial stabilizer: every nontrivial
subgroup of cyclic 2-group contains -1; selected antipodes forced non-agreeing. Verifier:
threshold first=2^22 replayed + full p=97,n=32 fixture (exists, diffuse, primitive, agreement
>= k+1). VERDICT: IMPORT-CLEAN. Consequence traced: kills any universal per-sunflower n^6
diffuse payment (count is Theta(n^7)-scale; matches upper reduction #DIFF_30 <
16(k-1)^2*binom((n-k)/2,5) ~ n^7 from d3_diffuse_hyperplane_reduction).

### GUARD (a) — pma_wide_residual conditioning: PASS (with one master-side surgery obligation)

v4's own petal_mixed_amplification was flipped CONDITIONAL->TARGET in the same campaign
(conditional.md replaced by a re-pose record listing pma_wide_residual as the retired
premise). At pin, dag reverse-dependency scan: NO v4 node conditions on pma_wide_residual as
a live premise; its statement.md is an explicit tombstone ("records the route that was
falsified... not a live proof target"). The two obstruction nodes list pma_wide_residual as
CONSUMER (i.e., they refute it), which is correct orientation. MASTER-side obligation: master's
background/nodes/petal_mixed_amplification/conditional.md STILL closes from pma_wide_residual
=> that closure must be broken on import (pma_wide_residual TARGET->REFUTED + petal_mixed_
amplification CONDITIONAL->TARGET), exactly as the survey said. Anything on master that would
consume petal_mixed_amplification's CONDITIONAL status inherits this break — imgfib's demotion
to CONDITIONAL-on-l1_mixed_petal_amplification (catch #212) already anticipates it.

### GUARD (b) — Linnik family INSIDE or OUTSIDE imgfib's reserve: OUTSIDE (imgfib survives; NO T-KILL)

Three independent reasons, all traced:
1. The exponential floor (pma_sigma_one_variable_defect_exact_hit_floor, d=n/8, a=d+2,
   q=p^2 with Linnik prime p=-1 mod n, p<=n^A) lives at sigma=1 with generated field size
   POLYNOMIAL in n. Master's imgfib reserve = "sigma*log2(q_D) >= (1+eps)*log2 C(n,k+sigma)".
   At sigma=1, q<=n^{2A}: LHS ~ 2A log2 n, RHS ~ n bits — reserve fails by ~n bits. The
   family is outside the master claim.
2. The mechanism cannot be transported inside: the count pays 1/q per extra agreement
   (numerator q-degree d+1 vs denominator q-degree a=d+2); making the reserve hold at
   sigma=1 requires q >= 2^{~n}, where the floor bound 3^{n/4}/(4q) (and the true first
   moment ~ C(K,d)C(M,a)2^a/q) collapses to 0.
3. STRUCTURAL separation (petal_reserve_rich_fiber_reduction, PROVED, replayed): at the
   reserve/lower cutoff, ell=sigma+1 >= Cn/log n forces ell > M (M <= (n-k+1)/ell ~ log n),
   and the ENTIRE collision-free class (R injective on petal points — which is exactly what
   all three sigma-one floor constructions are) is EMPTY once ell > M. Hand-traced: r<=d
   (background hits are roots of W), h+r>=ell+d => h>=ell; collision-free => h<=M. Also
   yields m_rich >= ceil(ell^2/(n-k+1)) = Omega(n/log^2 n) — any reserve-scale
   counterexample must produce a source-coupled rational-value fiber of that size in ONE
   petal. This is the correct re-posed reserve-scale obstruction and the imgfib-survives
   theorem. VERDICT: IMPORT-CLEAN, and it should be wired as evidence INTO master's
   l1_mixed_petal_amplification node (node-local notes rule).
External input: Linnik least-prime theorem (cited: Xylouris arXiv:0906.2749, any absolute
exponent suffices) — citation-fenced, acceptable as a classical import; flag it in the node's
import note as the single classical dependency of the sigma-one floor corollary.

### GUARD (c) — narrowed-target faithfulness: FAITHFUL-WITH-CROSSWALK (no goalpost shift, but NOT the same bucket)

v4's re-posed petal_mixed_amplification (critical/nodes/.../statement.md at pin) preserves:
imgfib consumer, the imgfib hypotheses verbatim ("polynomial generated-field, entropy-reserve,
and lower-cutoff hypotheses stated in imgfib"), quotient-profile budgeting ("every
non-polynomial natural-scale profile is charged once"), and explicitly refuses to claim below
the reserve ("does not... demand a uniform polynomial outside the stated reserve"). Falsifier
preserved and strengthened (reserve-admissible super-poly family for every fixed B). So: no
goalpost shift.
BUT the v4 target is the whole POST-TOP-BAND bucket in the carried-source-layout first-match
architecture (= below-floor full petals + mixed + diffuse partial petals), whereas master's
l1_mixed_petal_amplification is ONLY the mixed/diffuse-partial bucket (master's clause (P) +
K4 + census gate already close full-petal top-band AND below-top on master's own chain). The
two decompositions are DIFFERENT and non-conflicting. Import consequences:
- v4's open full-petal strata (M=4 t=2, larger-M full petals, rate-half three-petal tail)
  are NOT new open content for master's l1 red — on master they are owned by the clause-(P)
  chain; they are open only inside v4's alternative architecture.
- The part of v4 that PAYS master's l1 bucket: pma_saturated_mixed_support_kernel +
  pma_petal_pattern_root_pinning_ledger (every bounded (t*ell-h)+max(0,2d+1-h) region
  polynomial at the lower cutoff — this covers mixed/partial-petal patterns, not just full),
  petal_reserve_rich_fiber_reduction (reserve-scale fiber forcing), and the sigma-one floors
  as mandatory lower fences. The l1 red's open content narrows to: u+e -> infinity
  mixed/partial profiles with a source-coupled Omega(n/log^2 n) rich fiber.
- The re-posed statement must NOT replace master's l1 statement (custody law): wire as a
  sibling/child decomposition with a crosswalk note in BOTH nodes.

### Load-bearing PROVED support nodes — hand-trace results

HAND-TRACED SOUND (full proof trace, every displayed identity/inequality re-derived):
1. pma_saturated_mixed_support_kernel — all 6 sections: exact kernel parametrization
   (dim s-d-1); largest-class rank bound via Phi=(W_F-c_*F)/L_Y (rank >= a_*-1, = a_* unless
   the exceptional full-petal case lambda=0, a_*=ell); exact-defect saturation gcd(F,W)=1 +
   pairwise-coprime fibers + principal common-factor re-encoding exclusion (L_{C\D}W =
   L_{C\D_0}W_0 identity verified); dual-RS/Hankel equivalence (Lagrange top-coefficient
   M_j(y), induction both directions); maximal rank min(d,w) (d<w: WG-BF deg<=2d vanishing on
   >=2d+2 points; d>=w: WQ-AF deg<=s-2, F|Q degree contradiction); canonical lexicographic
   core-root pinning C(k-1, max(0,d-w)) (K_D=span(L_D), rank m-1 functionals, injectivity of
   R(F)). IMPORT-CLEAN. This is the wave's central lemma.
2. pma_petal_pattern_root_pinning_ledger — h>d from threshold + b<ell; selected-support rank
   transfer legitimate (maximal-rank proof needs only deg-d kernel locator + deg<=d partner +
   coprimality); W uniquely determined by c_iF(y) at h>d points; background agreements =
   background roots of W (no background factor); aggregation C(M,t)C(t*ell,h)C(k-1,e), e =
   max(0,2d+1-h); region bound (E+1)n^{E+2}2^M <= (E+1)n^{E+2+1/C_0} at the cutoff (M <=
   log2(n)/C_0). IMPORT-CLEAN. NOTE FOR l1 WIRING: the ledger covers ARBITRARY petal patterns
   (mixed + partial + full) — this is the piece that pays bounded-(u+e) regions of master's
   l1 bucket.
3. pma_full_petal_band_composition — (FPC1)-(FPC6) all re-derived; top band => t in {M-1,M}
   (the m_chi=M vs t distinction is honest — refuses the false m_chi=t bridge); M<=3 closed,
   M=4 leaves t in {2,3}; e=0 branch composition with the ledger correct. Depends on master-
   proved petal_growth (top band) + planted-receiver two-class exhaustion (t>=2). IMPORT-CLEAN.
4. pma_three_petal_mu_basis_reduction — syzygy dictionary bijection (alpha_i cyclic
   differences, sum alpha_i = sum alpha_i c_i = 0; converse construction inverse); mu-basis
   theory self-contained over the PID (free rank-2 kernel, minimal mu+nu, leading-vector
   independence, predictable degree, cross product r=h*L with h a unit, mu+nu=ell); (HF)
   filtration. IMPORT-CLEAN.
5. pma_three_petal_projective_johnson_bound — (PJ2) via determinant identity
   F_pW_q-F_qW_p=kappa*L_1L_2L_3 (common root => 2 nonzero vectors in a 1-dim kernel =>
   H_12(x)=0, deg H_12<=e-1, H_12 nonzero by primitivity); Johnson double count re-derived;
   rate-1/4 positivity J=(N-d)^2+N(3ell-N)>0 with N<3ell from 3k+1=4ell+b; 16n^3 assembly
   (12n^3 upper + 4n lower); rate-half (PJ7) expansion re-derived exactly. IMPORT-CLEAN.
6. pma_official_rate_small_source_degree_sieve — source equation (r-1)k+1=M*ell+b; M<=r-2 =>
   ell>=k+1 => d<ell (no strict branch). Trivially sound. IMPORT-CLEAN.
7. pma_exact_periodic_owner — invariant agreement set = union of K_M-cosets; owner injective
   (two codewords sharing M*h_M >= a > k-1 agreement points are equal); C(N,h_M) count +
   Pascal ratio. IMPORT-CLEAN.
8. pma_sigma_one_dyadic_near_coset_owner — (L-CORE) mechanism: (L-e)+(k-L+e)=k interpolation
   points determine the codeword; official corollary interval matches the d4 escape argument
   exactly (dyadic L in [k-s_n, k+1+s_n] => L=k only). IMPORT-CLEAN. Architecture coherence
   verified: the d3-RQ >n^6 family IS owned by this owner (unbalanced core G\{b}, 4 misses at
   scale L=k=N) — which is exactly why the d4 obstruction uses a BALANCED core to escape.
   The two refutations + owner are mutually consistent.
9. pma_sigma_one_first_layout_domination — (FL1): a Post codeword not planted in layout 1 is
   carried there (universal core-defect carriage), so later-first codewords are among the M
   anchors of layout 1. IMPORT-CLEAN.
10. pma_sigma_one_post_top_allowance — TP-PART/TP-CAP bookkeeping; N_top=2(t_ch+1)S_3(k-1) at
    rate 1/2, N_top=0 else; "first" carried layout load-bearing (statement explicitly refuses
    the layout-existential reading). The d4 contradiction needs only the cap #Top<=N_top —
    membership ambiguity Top vs Post is immaterial. IMPORT-CLEAN.
11. pma_sigma_one_d3_diffuse_hyperplane_reduction — barycentric 5-point nullspace => (DH)
    hyperplane, nonzeroness via distinct labels; fixed-hyperplane split-cubic count < K^2/2
    (exceptional-pair grid lemma 2K-1 re-derived); aggregate 16(k-1)^2*C((n-k)/2,5) ~ n^7.
    IMPORT-CLEAN.
12. pma_sigma_one_variable_defect_exact_hit_floor — full trace (see guard (b)): hyperplane
    count H_d, injection probabilities, (K-d)+a=k+1 odd, coset-miss arithmetic
    k/2-d-1 >= s_n+2, odd-lift pair contradiction, Linnik corollary with q=p^2 generating
    field; C(K,d)>=3^d and 2^aC(M,a)>=3^a checked at d=n/8. Single classical import: Linnik
    (Xylouris, arXiv:0906.2749, any absolute exponent). IMPORT-CLEAN.
13. petal_reserve_rich_fiber_reduction — full trace (see guard (b)). IMPORT-CLEAN; wire as
    node-local evidence into master's l1_mixed_petal_amplification.

REPLAYED + STATEMENT-CONSISTENT (verifier PASS with mutation controls; statements cross-read
against the wide_residual tombstone + re-pose which quote their exact bounds; proof.md not
line-by-line hand-traced this wave — flag as normal-depth structural audit):
pma_sigma_one_low_defect_payment (B_low<n^5/1024), pma_sigma_one_d3_background_payment
(C(k-1,3)floor(C(n-k,3)/4)<n^6/9216), pma_sigma_one_d3_full_petal_payment
(C(k-1,3)((n-k)/2)C(n-k-2,2)<n^6/1536), pma_sigma_one_index_two_core_owner,
pma_sigma_one_odd_lift_boundary_owner (C(N,k/2+1)<3Q_2(k+2), source-level predicate, unique
split point), pma_sigma_one_paired_core_normalization (phi_C fiber signature (2,...,2,1)),
pma_sigma_one_paired_core_abundance (>n^6 paired cores at (65537,65536,32768) — note this is
q=65537 PRIME row, distinct from the d4 row q=65537^2), pma_sigma_one_b11_scope,
pma_b11_first_match_router, pma_quotient_closure_scope (QCLOSE=empty resolution),
pma_source_paving_bridge (threshold exactly kappa+sigma vs upstream PR #764 chart),
pma_coset_subtwoell_saturation_exclusion (861,239 rank triples replayed),
pma_arbitrary_petal_source_realizability, pma_exact_periodic_owner official corollary,
pma_sigma_one_dyadic_near_coset_owner official corollary (FINITE-COS < 2^{7n/64} < Q_2(k+2)).

### Cluster 1 verdict

- b9beb6e8 (d4 obstruction + pma_wide_residual REFUTED flip): IMPORT-CLEAN.
- 74225111 (d3-RQ obstruction + diffuse route cut): IMPORT-CLEAN.
- Re-posed petal_mixed_amplification: IMPORT-WITH-REPAIRS (custody: v4 REPLACED master's
  statement.md/conditional.md in place — master must MERGE: keep master text, append the v4
  re-pose as a dated addendum + the conditional.md gets a refutation record appended, never
  deleted; plus the l1 crosswalk note, see guard (c) and surgery spec).
- ~28 PROVED pma_*/petal_reserve nodes: IMPORT-CLEAN (13 hand-traced, 15 replayed+consistent).
- pma_wide_residual node folder: IMPORT-CLEAN as REFUTED tombstone (its statement.md
  honestly preserves the refuted route text; master's dag-only TARGET statement must be
  preserved in the folder as the original claim record — see surgery spec).

---

## CLUSTER 2 — RATE-HALF LIST FLOORS (2af18dfd + 5bf2cbb0) — SOUND; RETIRES THE GRAND-LIST HALF

### Hand-trace: rate_half_cyclic_rotated_prefix_floor (5bf2cbb0) — SOUND

Construction fully traced: Q=D^c is a coset of the order-N subgroup, y^N=delta on Q; one-wrap
rotation R_A(Y)=rem_{Y^N-delta}(Y^{N-d}P_A(Y)) verified (deg = 3N/2 <= 2N-1); expansion (3)
re-derived; L_A=L_0(X)R_A(X^c) has disjoint degree blocks [ic, ic+s] since s<c; the >=k part
depends only on (a_0..a_{d-1}) — indices N-d..N-1 from the unwrapped sum plus the FIXED
delta*a_m at index N/2 (no overlap since N-d >= N/2+1); a_0 = +-prod(A) confined to ONE
multiplicative coset of size N => only N*q^{d-1} prefix vectors; pigeonhole over C(N-1,m)
subsets => class of >= ceil(C(N-1,m)/(Nq^{d-1})) locators sharing the high part U; codeword
-E_A agrees with U exactly on the vanishing set of L_A = T_0 (s pts) + m full c-fibers
(disjoint, b_0 excluded) = exactly n/2+dc+s positions; distinct A => distinct codewords.
Interleaving: diagonal (U,...,U) vs (-E_A,...,-E_A) preserves COLUMN agreement support =
exactly the common-support/interleaved-list semantics of the prize object. Radius
monotonicity: agreement exactly k+sigma* >= k+sigma keeps every witness in every band list.

### Parameter/threshold audit (independent, w8_ratehalf_crosscheck.py — PASS)

- Agreement identity EXACT: d*c+s = 2048*2^22 + 2,978,146 = 8,592,912,738 = sigma*.
- log2 C(524287,264192) = 524254.0796 (lgamma, independent of v4 code).
- Cyclic boundary (128+log2C-log2 N)/2048 = 256.036659973 > 256 => (CR3) holds through the
  ENTIRE official field range q < 2^256; margin at q=2^256 = 75.079624 bits. REPRODUCED.
- Fixed-tail boundary (128+log2C)/2049 = 255.9209759026 < 256 => the fixed-tail floor alone
  does NOT cover the cap (honest partial; superseded by the cyclic rotation which saves one
  full field coefficient, q^d -> Nq^{d-1}). REPRODUCED.
- qcore gap at cap: 128 - log2 C(127,64) = 4.8286 bits — REPRODUCES master's own
  witness-hunt record "theorem-capped 4.73-4.83 bits short of the razor need" (catch #102
  lane), confirming the trigger convention matches master's razor accounting.

### Trigger legitimacy (the decisive check)

The unsafe trigger used is list count > q/2^128. The PRIZE SPEC (rs-mca-prize-spec memory,
read from proximityprize.org 2026-06-24) defines Grand List Decoding as
|Lambda(C^{==m}, delta*)| <= 2^-128*|F| for the m-fold interleaved code at CONSTANT m. So
count > q/2^128 for ordinary AND every constant common-support arity is EXACTLY the official
list-unsafe condition — not a proxy. Master's razor brief documents only the MCA conversion
trigger "list > (q-n)/k => MCA failure"; v4's trigger-separation note (q/2^128 list vs ~q/k
MCA conversion) is correct and important: the two thresholds are different objects, and v4's
guard sentence ("must not reuse the list threshold q/2^128 as an MCA surrogate") should be
imported verbatim.

### Verifier replays (mini-tree, pin content)

- cyclic verify.py PASS: toy_d1=(5005,313,315) toy_d2=(3003,2,6) cap_count_bits=524255
  cap_list_bits=204 q_boundary=256.036659972895 margin=75.079624489. Toy = FULL small-field
  realization: builds locators, rotates, checks exact root sets, counts agreements
  point-by-point, checks bucket >= pigeonhole floor, checks distinctness, and carries a
  constant_is_necessary control (the a_0 coset restriction must matter). Exemplary fail-open
  hygiene.
- cyclic verify_audit.py PASS: support_checks=3472 constant_checks=21 (independent audit
  verifier, same margins).
- fixed-tail verify.py PASS: toy_total=5005 toy_pigeonhole=26 toy_bucket=45
  q_boundary=255.9209759026303 qcore_gap=4.8285658.

### What this retires / what remains of rate_half_band_closure

RETIRED (on import): the ENTIRE Grand-List-Decoding half of the rate-1/2 battlefield node —
ordinary list AND every constant interleaving arity, every admissible field q < 2^256, the
whole residual band 2^33 < sigma <= sigma* is list-UNSAFE (witness count > q/2^128 at
sigma*, propagated down-band by monotonicity). Combined with master's banked safe side above
sigma*, the rate-1/2 LIST crossing is DETERMINED and adjacent: list_adjacency_closing can
consume the PROVED cyclic node directly and leave rate_half_band_closure entirely.
REMAINS (the re-scoped red): the support-wise MCA/CA crossing through the same band on the
MCA trigger (epsilon_mca <= 2^-128; conversion threshold ~q/k) and the distinct-slope
ledger — i.e., the Grand-MCA half only, consumed by adjacency_closing and mca_safe. The red
stays TARGET; one of its two grand-path consumers is severed and fed by a theorem.

### Custody

- QUALITY.md: v4 changes are APPEND-ONLY execution logs (2 dated blocks) — import verbatim. OK.
- statement.md / conditional.md / proof.md of rate_half_band_closure: IN-PLACE REWRITES
  (master's battlefield text replaced by the re-scoped MCA/CA text). Catch w8-C2. Import as
  dated narrowing addenda preserving master's original statement text (the #160-style
  repair); the re-scope itself is mathematically justified, only the custody form is wrong.
- list_adjacency_closing/conditional.md: predicate swap rate_half_band_closure ->
  rate_half_cyclic_rotated_prefix_floor + rewritten closing paragraph. The swap is a GENUINE
  STRUCTURAL CHOICE on a CONDITIONAL closure — per the forced-corrections rule it must be
  surfaced to master, not silently imported; recommendation: ACCEPT (the new predicate is
  PROVED and strictly stronger wiring), applied as a dated addendum noting the old predicate.
- P6_RATEHALF_SIBLING.md edit: IN-PLACE header rewrite ("THE rate-1/2 battlefield node...
  NEW covering mechanism" -> "Historical MCA/list brief... needed only for MCA/CA") + one
  body line. Same w8-C2 treatment: dated re-scope note appended, original header preserved.
- list_adjacency_closing/statement.md: append-only new section "Rate-half split (2026-07-14)"
  — merges as-is. OK.

### Cluster 2 verdict

- 5bf2cbb0 (cyclic rotated prefix floor): IMPORT-WITH-REPAIRS (node folder + dag node
  IMPORT-CLEAN; the master-file re-scopes converted to addenda per w8-C2). THE single
  highest-value import of the wave, as the survey predicted.
- 2af18dfd (fixed-tail prefix floor): IMPORT-CLEAN as evidence/history (PROVED, honest
  partial, superseded by the cyclic node; keep its ev edges).

### imgfib wiring at pin (Cluster 1 addendum)

v4 imgfib CONDITIONAL from SEVEN wired predicates: l1_program_frontier,
pma_exact_periodic_owner, petal_growth, petal_mixed_amplification (the open TARGET), conj_f,
dyadic_profile_evaluation, payment_completeness. The conditional text is careful: the
saturated-kernel + ledger + band composition "may be used inside that premise but do not
replace it"; no refuted n^6 subledger assumed; the near-coset absorption is finite-track only
("At general reserve no such finite absorption is imported"). verify_scope_repair.py REPLAYED
in mini-tree: PASS 140/140 with mutation controls (projective-Johnson-stays-evidence,
backward-petal-edge-rejected). The v4 imgfib statement.md is an in-place REWRITE of master's
— but the rewrite makes "polynomial-size generated field q_D" and "sigma >= C n/log2 n"
EXPLICIT hypotheses (master's dag text has only the entropy inequality). This narrowing is
exactly what guard (b) needs (the sigma-one exponential floor makes the huge-q sigma=1 corner
unclaimable-by-this-chain; not refuted, but unproven). See catch w8-C3: import as a dated
SCOPE addendum and surface the narrowing as a genuine master choice (recommend ACCEPT —
master's own l1 red already says "above the corrected reserve").

---

## CLUSTER 3 — DLI WCL SLOTS (9688c6ad + 760f4a68 + satellites) — SUB-AUDIT COMPLETE, GATED

Sub-audit complete (full report in the task record). My gates, run independently: (i) the
9688c6ad dag.json forensics — confirmed exactly TWO gate="all" CONDITIONAL->PROVED flips ride
the commit (packaging AND list_safe) with no node files touched, packaging's four req parents
(compiler/harness/dossier_partial/bridge_ledger) PROVED on both repos, master's packaging
CONDITIONAL kept deliberately; (ii) the pin-state resolution — 8aeec4be (the mid-campaign
master merge) flipped list_safe BACK to CONDITIONAL when it synced imgfib's demotion, so at
pin only the packaging flip survives (v4 pin list_safe = CONDITIONAL = master). Headline
results (sub-auditor evidence; its own independent recomputations listed):

1. **(2,5) SLOT CLOSED — 9688c6ad IMPORT-WITH-REPAIRS.** The router argument hand-traced
   sound by the sub-auditor (sign absorption into an antipodal-free 5-subset of mu_1024;
   scale a root to 1; u+v=-1 + cubic-moment identity => pair = roots of T^2-vT+B; membership
   via B^M=1 and Dickson D_M(v,B)=2; integral clearing to F=C^M-v^M, G=E_M-2v^M in
   Z[zeta_1024]; evaluation at omega is a ring surjection so a supporting q divides
   gcd(|Norm F|,|Norm G|); odd dilation is a Galois automorphism => one orbit representative
   suffices). Modal replay PASS: orbits=1514 gcds=507 roots=168 prime_nodes=282 max_v2=18
   negative_controls=3/3. Independent spot checks (sub-auditor's own code, different
   implementation paths): 7 Pocklington nodes re-verified from scratch; ALL 168 roots
   BPSW-re-primality-checked + max v_2(p-1)=18 independently recomputed (vs official gate
   v_2(q-1)>=41 — margin 23 doubling levels); 3 orbit norm-gcds recomputed via flint with
   exact string equality; the 1,514-orbit census independently reproduced (representative
   set == ledger set); scalar product-formula cross-checks at p=12289, 40961. The certified
   claim covers ALL prime factors (not only q<2^256), so the statement's q<2^256 restriction
   is harmless understatement.
2. **(2,6) REDUCED — 760f4a68 (+0087b00a) IMPORT-CLEAN.** Triple-cubic router + division-free
   doubling recurrences; probe verifier PASS (rows=20 primes=16 max_v2=10 controls=2/2);
   13 candidates incl. production M=1024 (1,2,3) re-verified by fresh recurrence
   implementation. Slot remains OPEN (reduced to a finite certified candidate list —
   <=1,550,336 pair-products each with two explicit cyclotomic norm obstructions).
3. **Weight-3 assumption mapping: EXACT MATCH, no catch.** The weight-6 router assumes (req
   edge present) master's PROVED dli_wcl_ell2_weight3_ambient_exclusion — the ORDER-1024
   ell=2 node, NOT the order-512 ell=1 dli_wcl_weight3_ambient_exclusion; the norm covers
   all conjugate order-1024 embeddings, exactly what the saturation step needs. Both master
   node trees byte-identical in v4.
4. **Packaging flip (w8-C1) mechanism found: tools/auto_discharge.py** (v4-only, invoked by
   tools/dag_commit.sh before every commit) flips any all-green-req CONDITIONAL to PROVED to
   a fixpoint; intermediate commits bypassed dag_commit.sh, so pending discharges swept
   silently into the unrelated DLI commit. Aggravating: its regression artifacts are written
   to a nonexistent path (tools/../nodes/), so flips are one-way and traceless — the
   advertised regression rule is dead code. REFUSE the packaging flip on import (master's
   CONDITIONAL is a deliberate standing choice); do NOT import auto_discharge/dag_commit
   behavior implicitly with dag.json.
5. **Master bookkeeping consistency: CLEAN.** The closure matches master's slot definition
   (ell=2 <=> order-1024 roots <=> first two odd power sums vanish — same convention as
   master's ell2_weight4_newton node); residual update six -> FIVE slots
   (1,5),(1,6),(2,6),(2,7),(4,9); WCL-ZONE stays TARGET. official_terminal_attack.md +
   zone statement.md changes are STRICTLY ADDITIVE appends (no custody violation in this
   cluster). C1' interaction clean: dli_dyadic_k_core stays REFUTED, no repair claimed; the
   full-spectrum polymer majorant explicitly replaces the refuted truncated C1' route and
   uses the kill rows (q=63361, 65921) as fences only; dli_marginal_baseline100_coverage
   stays TARGET (majorants prove implications toward it without asserting the budget);
   matching-truncation caps 51/85/113/<=127 derive from proved exclusions only (85 consumes
   the new (2,5) closure via an explicit req edge; clique-transfer I <= (1+P/K)^K
   hand-traced by sub-auditor).
6. Satellites ccb553c5/99e06891/1f38d814/dc41eb7b/22119f50/f55f2be0: IMPORT-CLEAN, all
   verifiers PASS locally (exact lines in the task record).
7. Sub-audit catches adopted: w8-C10 (auto_discharge path bug/dead regression — do not
   import the tool); w8-C11 (weight-6 probe negative controls partly tautological —
   cosmetic; load-bearing checks real); w8-C12 (weight-5 verify.py trusts the ledger + a
   hash-pinned Modal digest rather than recomputing norms locally — mitigated by the
   independent recomputation this wave; importer keeps notes/verify_resultants_remote.py
   --full --verify-only wired); w8-C13 (cosmetic: 9688c6ad drops dag.json trailing newline).
8. Import file lists (self-contained; all via `git show ae2e5dd5:<path>`):
   - dli_wcl_ell2_weight5_norm_gcd_exclusion: background/nodes/dli_wcl_ell2_weight5_norm_
     gcd_exclusion/{statement.md,proof.md,verify.py,notes/verify_resultants_remote.py};
     experiments/prize_resolution/{dli_wcl_pair_norm_gcd_probe_modal.py,
     dli_wcl_ell2_weight5_norm_gcd_certificate_result.json (1.67MB),
     dli_wcl_ell2_weight5_norm_gcd_prime_cert_modal.py,
     dli_wcl_ell2_weight5_norm_gcd_prime_cert_result.json.gz,
     dli_wcl_ell2_weight5_norm_gcd_replay_result.json}; ADDITIVE appends to
     background/nodes/dli_wcl_zone_coverage/{official_terminal_attack.md ("Norm-gcd closure
     (2026-07-14)"), statement.md ("NORM-GCD UPDATE")}; dag: new node + edges
     {ideal_index->norm_gcd req; norm_gcd->zone_coverage ev; norm_gcd->matching_truncation
     req} + zone notes + matching-truncation statement K=102->85; EXCLUDING the
     packaging/list_safe flips.
   - dli_wcl_ell2_weight5_pair_quadratic_router: background/nodes/.../{statement.md,
     proof.md,verify.py}; background/nodes/dli_wcl_zone_coverage/weight5_orbit_route_
     fence.md; experiments/prize_resolution/{dli_wcl_weight5_orbit_probe_modal.py,
     dli_wcl_weight5_orbit_probe_result.json}.
   - dli_wcl_ell2_weight5_pair_ideal_index_obstruction: background/nodes/.../{statement.md,
     proof.md,verify.py}; experiments/prize_resolution/{dli_wcl_pair_ideal_index_probe_
     modal.py, dli_wcl_pair_ideal_index_probe_result.json}. (Node honestly records its own
     certificate as incomplete; superseded by the norm route — import as history.)
   - dli_wcl_ell2_weight6_triple_cubic_router: background/nodes/.../{statement.md,proof.md,
     result.md,verify.py,notes/verify_norm_gcd_probe.py}; experiments/prize_resolution/
     {dli_wcl_ell2_weight6_norm_gcd_probe_modal.py, ..._result.json}; zone weight-six
     appendix sections; dag req edge dli_wcl_ell2_weight3_ambient_exclusion -> router.
   - dli_full_spectrum_polymer_majorant: background/nodes/.../{statement.md,proof.md,
     verify.py,route_fence.md}.
   - dli_primitive_matching_truncation_majorant: background/nodes/.../{statement.md,
     proof.md,verify.py} (+ the 9688c6ad statement bump K=102->85).
   - Common bookkeeping merged not copied: tools/verifier_manifest.json,
     experiments/prize_resolution/modal_verifier_replay.json + ledger.md,
     notes/PRIZE_RESOLUTION_ROADMAP.md, orbit/* regenerables. Do NOT import
     tools/auto_discharge.py / dag_commit.sh behavior.
   - Master-side ledger update on import: official_terminal_attack.md six-slot residual ->
     FIVE slots (1,5),(1,6),(2,6),(2,7),(4,9) via the v4 additive append; WCL-ZONE stays
     TARGET.

## CLUSTER 4 — XR (17 commits, 16 new PROVED nodes) — SUB-AUDIT COMPLETE, GATED

Sub-audit (full report in the task record; every verifier replayed locally, all PASS with
mutation controls; four load-bearing proofs hand-traced by the sub-auditor). My gate: I
independently reproduced the pivotal AZC arithmetic — floor(C(1024,3)*958/C(6,3)) =
8,546,941,849 < 8,589,934,592 = 8n^3 (margin 0.5005%) and the rank-5 failure ratio 145.127 —
both match. Headline results:

1. **3b187648 implements catch #158 faithfully** (retro-scopes the old rank-4 "closed on all
   six rows" claims to "five rows + covered branches; line-free/line-uncovered sub-case
   open"), THEN 6470eb3a pays the fenced sub-case with NEW covering-free mathematics:
   xr_affine_core_all_zero_charge (|P|*C(Delta-r+a-1,a) <= C(N,a)*(r+1), strengthening the
   final factor N-a to r+1). Sub-auditor hand-traced it sound (persistent-coordinate cap,
   disjoint nonpersistent zero sets => M_T <= r+1, incidence count). NO #158 VIOLATION
   anywhere in the cluster — the #158 RowC-1/16 rank-4 sub-case is LEGITIMATELY DISCHARGED,
   and all rank-five claims use the correct anti-#158 pattern (counterexample CONTAINS a rich
   subfamily; no coverage premise).
2. All 16 nodes IMPORT-CLEAN mathematically; P-A/P-B stay TARGET (no status changes; every
   node declines promotion). New honest frontier on import: min open selector rank >= 5,5,5
   (RowC) and >= 17,17,15 (prize) for BOTH reds; wave-5's {4*} star is removed. RowC rank-5
   deficiency pairs reduced to 14/70/323 (P-A), 8/49/274 (P-B); P-B (0,0) outright paid; the
   shared residual object is the coherent GRS4 split-pencil census (+ rank-2 chart
   first-match audit + (u,v) pairs u<=60, v<=7).
3. CUSTODY (w8-C7): TEN in-place rewrites of master-shared files (both dag statements for
   P-A/P-B, cogirth node dag statement/result.md/route_limit.md/verify.py output semantics,
   P-A attack/claim_contract/dependency_subdag/frontier). All content justified by AZC but
   every one must become a dated addendum/superseding entry on import. AGGRAVATED item:
   3b187648 REWORDED a wave-6 AUDITOR NOTE inside cogirth result.md (dropped its leading
   clause) — auditor notes are never edited; restore verbatim + append (precedent matters).
4. Master-side latent catch (w8-C8, independent of import): master's OWN dag statement for
   xr_affine_core_cogirth_ray_bound still carries the pre-#158 "closes the complete
   high-core rank-four branch on all six rows" sentence, contradicting master's P-A dag
   statement and the node's own w6-noted result.md. Fix on master regardless; v4's corrected
   wording is the right text.
5. Pin note (w8-C9, minor): the AZC RowC-1/16 rank-4 margin is only 0.5005% — any re-pin of
   (h, R, 8n^3 budget) must re-run that arithmetic; add a pin note to the node on import.
6. Verdict: whole cluster IMPORT-WITH-REPAIRS (repairs = the ten custody addenda + w8-C9 pin
   note); 16 node folders verbatim (4 files each + dag entries + manifest lines); pure
   appends to the two QUALITY notes/ledger/roadmap merge as-is.

## V3 TAIL — 77485270 boundary-divisor fence (read directly at the v3 worktree)

Confirmed a DIAGNOSTIC/FENCE, not a theorem: exact reduction of a residual (2,5) relation to
f(T)=T^5+aT^3+bT-c | T^1024-1 (Newton e_1=e_3=0 re-checked: p_1=p_3=0 => e_1=0, e_3=0 for
5 roots), plus a Singular resource ladder showing the elimination route computationally
saturated. The note itself says "not a proof that the elimination system has no
official-characteristic point" — honest. SUPERSEDED in purpose by v4's 9688c6ad (2,5)
closure. VERDICT: OPTIONAL-FYI import of boundary_divisor_route.md (+2 Modal scripts +
results) into master's dli_wcl_zone_coverage notes as negative-route documentation. The two
v3 C36 commits (020d1a71, f477a948) are subsumed by v4 Cluster A — DEFERRED with Cluster A.

## CLUSTER A (C36 f3_h3 chain, 22 commits) — DEFERRED

Out of this wave's priority budget (task scope: clusters 1-3 + XR if budget). 17 new PROVED
f3_h3_* nodes ending at f3_h3_local_cluster_valuation remain UNAUDITED — do not import ahead
of a wave-9 audit; no master decision this week depends on them (f3_h3_mobius_excess_half
stays TARGET regardless).

## GUARD OUTCOMES (the three the banking session needs)

1. pma_wide_residual conditioning: PASS — no v4 node conditions on it as a live premise (dag
   reverse-scan at pin: all 21 in-edges are kind=ev; only out-edge is ev->petal_mixed_
   amplification as history; statement.md is an explicit tombstone). Master-side: the import
   MUST break master's background/nodes/petal_mixed_amplification/conditional.md closure
   ({aux_list, johnson, wide_residual}) in the same surgery that flips pma_wide_residual to
   REFUTED — otherwise master carries a conditional closure on a refuted premise.
2. Linnik-family refutation vs imgfib reserve: OUTSIDE — NO T-KILL. Three independent traced
   reasons (poly-field family fails master's entropy inequality by ~n bits at sigma=1; the
   mechanism pays 1/q per extra agreement so it dies at reserve-scale q; the PROVED
   petal_reserve_rich_fiber_reduction shows the entire collision-free class is EMPTY at the
   cutoff since ell>M). imgfib stays CONDITIONAL and viable, PROVIDED master adopts (or
   already means) the polynomial-generated-field + lower-cutoff scoping (w8-C3 addendum).
3. Narrowed-target faithfulness: FAITHFUL-WITH-CROSSWALK — no goalpost shift (consumer,
   reserve hypotheses, quotient budgeting, falsifier all preserved or strengthened), but the
   v4 target is the POST-TOP-BAND superset bucket in the carried-layout architecture, NOT
   master's l1 mixed/partial-only bucket. Import as sibling decomposition with a crosswalk
   note both ways; v4's open full-petal strata (M=4 t in {2,3} rate-half tail, larger-M) are
   NOT new open content for master's l1 (owned there by the clause-(P) chain).

## DEFERRED VERIFICATIONS (pre-registered expectations, wave-7 style)

1. Cluster A (C36 f3_h3 chain, 22 commits / 17 nodes) — wave-9. Expectation: the linear
   chain replays end-to-end; the load-bearing endpoint is f3_h3_local_cluster_valuation
   (v_p(e^U_n)=V_n(p)>=Z_9 with row-wise cap V_n(p)<=(150/17)n^2 => C36', boundary-row p^6
   Hensel certificate). Falsifier: any chain link whose verifier is a cannot-fail
   certificate or whose citation fence (414f383e/2734658f/9cf4ebbd) hides a load-bearing
   external estimate.
2. Modal census artifacts pma_d3r0/d4r0 (experiments/prize_resolution/) — evidence-only,
   not replayed this wave (the refutations carry standalone verifiers + small-field
   fixtures). Expectation: censuses reproduce populated diffuse (3,0)/(4,0) cells at the
   toy rows with counts consistent with n^7-scaling route evidence.
3. Any DLI certificate replay marked DEFERRED by the Cluster-3 sub-audit (see below).
4. Proof.md line-by-line traces for the 15 "REPLAYED + STATEMENT-CONSISTENT" Cluster-1
   support nodes (normal-depth this wave). Expectation: no surprises — their exact bounds
   are quoted and consumed consistently by the three hand-traced consumers; any error would
   have surfaced as an inconsistency there or in the 128-row symbolic verifiers.

## CATCHES (w8-C#, local numbering; banking session maps to global)

- w8-C1 (REFUSAL, flagged by survey, mechanism from sub-audit): `packaging`
  CONDITIONAL->PROVED flip riding 9688c6ad. REFUSE the flip on import regardless of
  mechanism — master's packaging CONDITIONAL is a deliberate standing choice (amber-invariant
  warning). See Cluster 3 for forensics.
- w8-C2 (custody): in-place rewrites of master's critical/nodes/rate_half_band_closure/
  {statement.md, conditional.md, proof.md} (battlefield text replaced by MCA/CA re-scope).
  Repair: dated narrowing addenda preserving master text; QUALITY.md append-blocks import
  verbatim; list_adjacency_closing predicate swap surfaced as a deliberate (recommended)
  choice.
- w8-C3 (custody + genuine choice): in-place rewrite of master's critical/nodes/imgfib/
  {statement.md, conditional.md}. The content (explicit poly-field + lower-cutoff hypotheses;
  seven-predicate closure) is sound and REQUIRED by the sigma-one floors; the form violates
  the merge law. Repair: dated scope addendum; surface the narrowing decision.
- w8-C4 (custody): v4 MOVED petal_mixed_amplification background->critical, DELETED the
  background folder, and REPLACED statement.md + conditional.md. Repair: master keeps its
  background folder, appends the re-pose as a dated addendum + a "re-pose record" appendix to
  conditional.md (v4's own conditional.md text is a good base for that appendix); the
  background->critical move is a master layout choice to surface (master's l1 red already
  occupies the critical slot for this content).
- w8-C5 (structural): v4 has NO l1_mixed_petal_amplification node (post-fork mint, catch
  #212). All imported pma_*/petal_reserve edges into the mixed-petal content must be
  RE-TARGETED on master: evidence edges to BOTH petal_mixed_amplification (as at pin) and
  l1_mixed_petal_amplification (new, per the crosswalk); nothing at pin references the l1
  node, so no v4 edge can be trusted to carry that wiring.
- w8-C6 (minor, bookkeeping): two different official rows both named "(65537...)" in the
  campaign: the d4 obstruction row is q=65537^2 (n=65536) while paired-core abundance uses
  the PRIME row q=65537 (n=65536). Both valid (n | q-1 in both); import texts must not
  conflate them (the wide_residual tombstone quotes both correctly).

## IMPORT SURGERY SPEC (exact; statements MERGED never replaced; all paths relative to repo
root; all v4 content taken at pin ae2e5dd5)

### Step 0 — ordering constraint (do FIRST, before any other master work consumes
petal_mixed_amplification's CONDITIONAL)

The refutation core must land atomically: items 1-4 below in one commit, so master never
holds {pma_wide_residual REFUTED} together with {petal_mixed_amplification CONDITIONAL on it}.

### A. Mixed-petal core (Cluster 1)

1. NEW NODE FOLDERS, copied verbatim from pin (background/nodes/<id>/ each with
   statement.md/proof.md/verify.py and where present audit.md/claim_contract.md/
   dependency_subdag.md): pma_sigma_one_d4_generic_source_obstruction,
   pma_sigma_one_d3_reciprocal_quadratic_obstruction,
   pma_sigma_one_variable_defect_exact_hit_floor, petal_reserve_rich_fiber_reduction,
   pma_saturated_mixed_support_kernel, pma_petal_pattern_root_pinning_ledger,
   pma_full_petal_band_composition, pma_three_petal_mu_basis_reduction,
   pma_three_petal_projective_johnson_bound, pma_official_rate_small_source_degree_sieve,
   pma_coset_subtwoell_saturation_exclusion, pma_arbitrary_petal_source_realizability,
   pma_sigma_one_low_defect_payment, pma_sigma_one_d3_background_payment,
   pma_sigma_one_d3_full_petal_payment, pma_sigma_one_d3_diffuse_hyperplane_reduction,
   pma_sigma_one_dyadic_near_coset_owner, pma_sigma_one_odd_lift_boundary_owner,
   pma_sigma_one_index_two_core_owner, pma_sigma_one_paired_core_normalization,
   pma_sigma_one_paired_core_abundance, pma_sigma_one_first_layout_domination,
   pma_sigma_one_post_top_allowance, pma_sigma_one_b11_scope, pma_b11_first_match_router,
   pma_quotient_closure_scope, pma_source_paving_bridge; plus critical/nodes/
   pma_exact_periodic_owner/ (only node the campaign placed critical — keep placement).
   Dag entries + PROVED statuses + refs as at pin. (~189 files total for clusters A+D of
   this spec; exact list = `git ls-tree -r ae2e5dd5 --name-only | grep -E
   '^(background|critical)/nodes/(pma_|petal_reserve_rich|petal_mixed_amplification|
   rate_half_cyclic|rate_half_fixed)'`.)
2. pma_wide_residual: create background/nodes/pma_wide_residual/ from pin (statement.md,
   refutation.md, attack.md, frontier.md, claim_contract.md, dependency_subdag.md) BUT
   prepend to statement.md a "MASTER ORIGINAL STATEMENT (preserved)" block carrying master's
   dag statement text verbatim ("RESTATED after the pullback counterexample... THE PRIMITIVE
   RESIDUAL — non-pullback, non-low-defect wide sub-Johnson lists are polynomial...").
   Refutation record must name BOTH kills: (i) master's polynomial-uniform reading refuted
   by pma_sigma_one_variable_defect_exact_hit_floor (exponential primitive wide-sub-Johnson
   residual at sigma=1 on poly-field rows — the floor family is non-pullback, d=n/8 is not
   low-defect, and it is inside the wide regime d^2 <= d|T|); (ii) the campaign's sharpened
   finite n^6 Post allocation refuted by pma_sigma_one_d4_generic_source_obstruction.
   Dag status TARGET->REFUTED; keep key:true history.
3. petal_mixed_amplification (background/nodes/, master folder KEPT): status
   CONDITIONAL->TARGET; statement.md gets dated addendum block = the full v4 re-posed
   statement (pin critical/nodes/petal_mixed_amplification/statement.md body); conditional.md
   gets appended "RE-POSE RECORD (2026-07-1x, wave-8 audited)" = v4's conditional.md body
   (why the old implication was retired + surviving-inputs list). Surface to master: whether
   to mirror v4's background->critical move (recommend NO — master's critical slot for this
   content is l1_mixed_petal_amplification; keep petal_mixed_amplification background with
   the crosswalk).
4. imgfib: statement.md + conditional.md get dated SCOPE/CLOSURE addenda (v4 bodies) after
   master's text (w8-C3); copy critical/nodes/imgfib/verify_scope_repair.py + notes/
   mixed_petal_scope_audit_20260714.md from pin; surface the explicit-hypotheses narrowing
   (recommend ACCEPT).
5. CROSSWALK (w8-C5, node-local notes rule): add to critical/nodes/
   l1_mixed_petal_amplification/ a note "v4_pma_crosswalk.md": (a) v4's post-top-band target
   is a SUPERSET decomposition (includes full-petal strata master owns via clause (P));
   (b) what pays PART of the l1 bucket: root-pinning ledger (every bounded u+e mixed/partial
   region), saturated kernel (fixed-support charge), reserve rich-fiber reduction (any
   reserve-scale counterexample needs an Omega(n/log^2 n) source-coupled value fiber in ONE
   petal — importable as the l1 attack's sharpest structural fence); (c) the sigma-one floors
   as mandatory lower fences for any finite-row ledger; (d) l1 open content after import =
   u+e->infinity mixed/partial profiles with rich-fiber forcing. Mirror one paragraph into
   the petal_mixed_amplification addendum. Update l1 statement.md "Known evidence" (append,
   dated): the wave-8 audit outcome + that the naive-induction killer is now complemented by
   the collision-free-emptiness theorem.
6. NEW EDGES on master: ev edges as at pin for all imported nodes (21 ev edges into
   pma_wide_residual; consumer edges to petal_mixed_amplification; ev edges
   {d4_obstruction, variable_defect_floor, rich_fiber_reduction} -> imgfib) PLUS new ev
   edges {pma_petal_pattern_root_pinning_ledger, pma_saturated_mixed_support_kernel,
   petal_reserve_rich_fiber_reduction, pma_sigma_one_variable_defect_exact_hit_floor}
   -> l1_mixed_petal_amplification (not at pin; w8-C5).
7. Census artifacts (evidence, not load-bearing — the verifiers carry the proofs):
   experiments/prize_resolution/{modal_pma_d3r0_census.py, modal_pma_d4r0_census.py,
   pma_d3r0_census_results.json, pma_d4r0_census_results.json} verbatim.
8. verifier_manifest: register the 28 verify.py + verify_scope_repair.py with hashes
   computed on the REPAIRED statement files (addendum blocks change statement.md hashes).
9. Classical-import ledger: record Linnik/Xylouris (arXiv:0906.2749) as the single external
   theorem consumed by pma_sigma_one_variable_defect_exact_hit_floor's corollary (finite
   theorem is self-contained).

### B. Rate-half list floors (Cluster 2)

1. NEW: critical/nodes/rate_half_cyclic_rotated_prefix_floor/ (7 files incl. verify.py +
   verify_audit.py) + background/nodes/rate_half_fixed_tail_prefix_floor/ (4 files), verbatim
   from pin; dag entries PROVED; edges: fixed_tail --ev--> {band_closure, cyclic_floor};
   cyclic_floor --ev--> band_closure; cyclic_floor --req--> list_adjacency_closing.
2. rate_half_band_closure: QUALITY.md append the two v4 execution-log blocks verbatim;
   statement.md/conditional.md/proof.md get dated "[LIST-SIDE RETIREMENT + MCA/CA RE-SCOPE
   (wave-8 audited)]" addenda carrying the v4 bodies, master text preserved (w8-C2); import
   notes/rate_half_trigger_separation_modal.py into the node notes dir. The trigger-
   separation guard sentence ("must not reuse the list threshold q/2^128 as an MCA
   surrogate") goes into the addendum verbatim.
3. list_adjacency_closing/conditional.md: surface-and-apply the predicate swap
   (rate_half_band_closure -> rate_half_cyclic_rotated_prefix_floor) as a dated addendum
   recording the old predicate; statement.md pin delta likewise. P6_RATEHALF_SIBLING.md pin
   delta (append-style) verbatim.
4. Node stays TARGET; gate=all recompute afterward MUST NOT flip anything (list_adjacency_
   closing stays CONDITIONAL — its other predicates are unchanged; verify before commit).

### C. Refused / deferred

- packaging CONDITIONAL->PROVED: REFUSED (w8-C1) — strip from any dag delta applied.
- Cluster A (17 f3_h3_* nodes), Cluster C XR nodes pending sub-audit gate below, Cluster F
  roadmap merge (FYI — merge integration notes r54-r93 + the PR #755-#775 adoption-gate
  table at leisure), Cluster G echo-duplicates: skip.
- v3 fence note: optional background/nodes/dli_wcl_zone_coverage-notes import (see V3 TAIL).
