All deliverables are executed. Returning the full REPORT verbatim, as the brief directs.

---

**Headline for relay:** **the last two `m=4` routes are both closed to the level this lane can reach, and the closure is a REVERSAL of round 37's central open question.** (A) Sporadic sharing is not a route at all: I prove a **dichotomy** — the coincidence scheme `Z` of the tuple map is either FINITE (sporadic) or contains a curve, and a curve forces Lüroth; there is no intermediate "correspondence" case, because a non-factoring symmetric `(2,2)`-correspondence has transitive closure larger than `9 = deg Psi`, so any `Psi` constant on it is CONSTANT (measured: component sizes `min 25, max 143, mean 102` of 258 at `q=257`, against **exactly 3** for every Bezoutian). And the sporadic cost is a **flat deficit of 20 that is INDEPENDENT of the sharing pattern** — the pattern-dependence cancels exactly between the incidence layer and the slope layer — putting the first moment at `10^-15.3`, i.e. **round 36's `<1e-4` price was optimistic by eleven orders of magnitude, not conservative.** (B) The determinantal solve WORKS: prescribing 7 edges and solving the remaining 4 simultaneously by iterated gcd, I find **80 raw solutions of the 11-merge resultant system in 700,000 draws at two fields** — the operation round 37's incremental fence cannot perform. **Every single one is degenerate. Zero legal.** The two dominant degenerate components are a fibre with an identically-zero cubic and a slope of hypergraph degree 8 (round 36's own MISS-5 artefact). And **3 free merges beyond the 8-merge state — which round 37 reported had "never been observed" — occur 80 times at rate `1.2e-4`**, always degenerately. Best legal `|slopes| = 14` at `q=193` AND `q=257`, both arms, both designs: **third round, third instrument, identical ceiling.** **No compute-law breach this round** — the two-round bare-`python3` streak ends.

---

# REPORT — r38_sporadic_det (round 38)

## VERDICT (first)

**`m = 4` is NOT DECIDED. No witness, no theorem, no exclusion. But both untouched routes are now priced with derivations rather than guesses, and round 37's one genuinely open question — "does the dim-4 variety have `F_q`-points the incremental fence cannot see?" — is answered: it does, and they are all degenerate.**

```text
D2 -- THE DETERMINANTAL 11-MERGE SOLVE, POOLED (two fields, two designs)

  draws (clean design, max p_v <= 2)          440,000   (240k @193, 200k @257)
  draws (saturated design, first run)         260,000   (@193)
  8-merge states reached                      674,393
  RAW solutions of the 11-merge system             80
  VERIFIED (MISS-2 guard G1-G3)                     0
  guard kills, clean design, all 4 arms:
      G1 fibre with an identically-zero cubic      39   (q193c:45,65 q257c:45,65)
      G3 slope of hypergraph degree 8              26        "
      G2 not 3 distinct P^1 slopes                  2        "
      G3 slope of hypergraph degree 3               1        "
  BEST LEGAL |slopes|   q=193 : 14 / 14  (armA/armB, q193c:48,68)
                        q=257 : 14 / 14              (q257c:48,68)
                        r36 : 14      r37 : 14      -> THIRD TIE

  FREE MERGES BEYOND THE 8-MERGE STATE (r37's functional, matched, at scale)
      q=193 clean  {0:107575, 1:7409, 2:142, 3:28}  mean .0675 (q193c:42)
                   {0:107898, 1:7155, 2:141, 3:16}  mean .0650 (q193c:62)
      q=257 clean  {0: 92142, 1:4651, 2: 79, 3:11}  mean .0500 (q257c:42)
                   {0: 92690, 1:4655, 2: 77, 3:13}  mean .0498 (q257c:62)
      r37 measured {0:104, 1:11} / {0:128, 1:11}, mean .096/.079, MAX 2
      -> 3 free merges OCCUR, 80 times, rate 1.19e-4.  r37's "3 has never
         been observed, by me or by r36's 40000 draws" is REFUTED as a count
         and CONFIRMED as a conclusion: all 80 are guard-illegal.

D1 -- THE SPORADIC TAXONOMY (derived before any search)
  demand ladder   D = 11 + 3(t_D-8) + 2(t_M-1) - delta   (b:17, 0 mismatches)
  t_D >= 8 always; = 8 iff (n1,n2,n3) = (0,0,8)          (b:9)
  t_D=9 : EXACTLY 2 patterns, both D=14   t_D=10 : EXACTLY 4, all D=17  (b:12-14)
  slot-count-23 recheck: delta shifts EVERY pattern equally -> uniform stays
     the unique minimiser at every delta                  (b:20-27)
  SPORADIC DEFICIT = 20 - delta, INDEPENDENT of (n1,n2,n3) (b:45, 0 mismatches)
  first moment, q=193 : (0,0,8) 10^-15.35 ; largest (1,4,5) 10^-13.07 (b:36,54)
  pattern-independent slope FLOOR s >= 12 vs target 13     (b:62)
  correspondence route : DEAD by derivation + measurement  (b:74,79-80,128-129)
  order-3 Moebius route: EXHAUSTIVELY DEAD, max 6 of 8 stable triples, 2 fields
                                                           (b:177,194)
```

Five results, in decreasing order of how much they move the board.

1. **The sporadic/uniform DICHOTOMY, with no third case — this closes the brief's "weaker factoring" question negatively.** Let `Z = closure{(x,y) : x != y, Psi(x) = Psi(y)}`. `Z` is finite (sporadic) or contains a curve. A curve `C` forces `Psi` constant on the transitive closure of `C`; that closure is either an equivalence relation (Lüroth: the fibre relation of a map `w`) or too large. Measured, both fields: a **generic** symmetric `(2,2)`-correspondence has largest transitive-closure component `mean 102.2, max 143` of 258 at `q=257` and `mean 67.8` at `q=193` (`d1_taxonomy_results_b.txt:79,128`); a **Bezoutian** `C_w` has largest component **exactly 3, in 60/60 trials at both fields** (`:80,129`). Since `deg Psi <= 3(m-1) = 9`, any component of size `> 9` forces `Psi` constant. And the fibre-product locus is a **hypersurface**: the Jacobian of `(P,Q) -> Bez(P,Q)` has rank **5 of 6 in 200/200 random points at both fields** (`:74,123`), so `{C_w}` has projective dimension 4 in `P^5`. **A `(3,3)`-correspondence carries 8 triples only when it IS a map's fibre relation.**

2. **The sporadic cost ledger is FLAT, and round 36's price was optimistic by 11 dex.** With `deg_x <= 9`, `Psi in P^39`; a class of size `s` at value `tau` costs `3s` linear conditions minus 3 free `tau` parameters; the slope layer needs `3 t_D - delta - 13` merges. Total:
   > `39 + 3 t_D - 72 - (3 t_D - delta - 13) = -20 + delta`, **verified with 0 mismatches over `t_D in [8,24]`, `delta in {0..3}`** (`:45`).

   The `t_D`-dependence **cancels exactly**: the incidence layer gets cheaper by 3 per extra class and the slope layer gets dearer by 3. Pattern-dependence survives only in the discrete count `N`, which varies by `< 1.6` dex across the band. First moment `N * q^-20`: `10^-15.35` for `(0,0,8)`, `10^-13.07` for the largest, `(1,4,5)` (`:36,40,54`). Round 36 priced sporadic at `< 1e-4` (`r36 REPORT.md:342`).

3. **The determinantal solve reaches the variety — and finds only degenerate points.** Prescribe 7 edges (rank 14, kernel dim 2 in `130000/130000` and `120000/120000` draws, every cell), then each residual edge `(i,j)` gives `D_ij(gamma) = A_i B_j - A_j B_i`, a binary form of degree `<= 6`; a common `alpha` solves all four at once. **80 raw solutions, 0 legal.** The measured rate is `1.1e-4` to `2.3e-4`, **10-27x ABOVE** the naive design prediction (`q193c:39,59`; `q257c:39,59`), and it scales as `~q^-2.1` (pooled `1.83e-4 -> 1.20e-4`, ratio 1.53 against `q^-2`'s 1.77 and `q^-3`'s 2.36) — **the signature of a codimension-2 degenerate component, not the codimension-3 honest one.**

4. **Two named degenerate components, one of which is round 36's own artefact.** (i) `w(t_i)^T Psi = 0`: a fibre whose cubic vanishes identically, so every edge at that fibre merges trivially — 39 of 68 clean-design kills. (ii) a slope of **hypergraph degree 8**, a common root of all eight cubics — 26 of 68. That second one is *exactly* the false positive round 36's MISS-2 guard killed (`r36 REPORT.md:77`). **A resultant system that is satisfiable is not a configuration**, and the excess over the naive count is entirely the degenerate locus.

5. **The exhaustive order-3 Möbius fence, which repairs round 36's R1.7.** Round 36 argued *"gcd(3,64)=1, so `mu_64` has no order-3 element"* (`r36 REPORT.md:159`) — that excludes MULTIPLICATIVE order-3 elements only, and `64 = 3*21 + 1` makes 1 fixed point plus 21 triples numerically legal for an order-3 **Möbius** map. Exhaustively, over all `83328` cyclic-deduped candidates (`sigma^3` fixes 3 points hence `sigma^3 = id`), the maximum number of `sigma`-stable triples inside `mu_64` is **6, against a need of 8, at both fields** (`:177,194`) — and it is not 0, which is the part I did not predict. Separately `|Stab_{PGL_2}(mu_64)| = 128` with **zero elements of order 3**, order histogram `{1:1, 2:65, 4:2, 8:4, 16:8, 32:16, 64:32}`, identical at both fields (`:181,183,198,200`).

---

## MISSES FIRST

1. **MY REGISTERED SOLVE RATE R4.4 IS WRONG, AND THE ERROR IS A MATHEMATICAL ONE I SHOULD HAVE SEEN BEFORE REGISTERING.** I registered `6^4/q^3 = 1.84e-4` from the raw resultant degree 6. But if slope `g` is prescribed on an edge at vertex `i`, then **every** `Psi` in the kernel has `R(t_i,g) = 0`, so both kernel basis cubics vanish at `g` and `D_ij` vanishes there **identically**. Those roots are forced AND guard-illegal. The genuine degree is `6 - p_i - p_j`, so the design-dependent rate is `400/q^3 = 5.56e-5` at best and `81/q^3 = 1.13e-5` for the clean design I ended up using. **My registered degree is the raw degree, not the legal one, and the registered rate is 3-16x optimistic.** Discovered by the smoke run, not by derivation.

2. **MY FIRST PRODUCTION DESIGN WAS THE WORST POSSIBLE ONE, AND IT MANUFACTURED 11 OF ITS 12 SOLUTIONS.** Maximising the score picks designs with a vertex at `p_v = 3`; three prescribed conditions pin `u(t_v)` into a **1-dimensional** space, so the pencil carries **exactly one** `alpha` with `u(t_v) = 0` — a fibre with an identically-zero cubic. The score-400 design saturates **three** vertices, and `11` of its `12` raw solutions sat on that component (`d2_solve_results_q193.txt:39,59`). I ran 260,000 draws on it before diagnosing this. The guard caught every one, but **the design error is mine and it burned a full compute run.**

3. **MY REGISTERED GUARD CLAUSE G1 WAS MATHEMATICALLY WRONG AND WAS REJECTING LEGAL CONFIGURATIONS — AND THE REPO ALREADY BANKS THE CORRECTION.** I registered *"the `gamma^3` coefficient `U~(t_i) != 0` for all `i`"*. But `PGL_2` acts **freely** on the slope line — round 37's own intrinsic count `12 - 11 + 3 = 4` uses exactly that freedom (`r37 REPORT.md:192`) — so `U~(t) = 0` is not a degeneracy, it is the slope `gamma = infinity`, and a change of chart makes it finite. I corrected the verifier mid-round to the **projective** slope line `P^1`. Worse: `background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_sharp_pair_exclusion/audit.md:17` already says *"The projective formulation covers a possible slope at infinity"*. **I registered a wrong guard and then rediscovered a banked practice.** (The corrected guard changed nothing in the end — the same configurations died on other clauses — but that is luck, not method.)

4. **I DID NOT SEARCH SPORADIC SHARING. I PRICED IT.** The brief's D1 asks for *"a TARGETED search of the cheapest pattern only (two fields)"*. What I delivered is the **incidence cost table** (cost 9 per prescribed triple with random `tau`, budget 4 of 8, `40/40` draws at both fields, `:95-96,144-145`), the derived optimal-`tau` budget 6, and an exactness lemma. The actual 8-triple sporadic search is a **rank-`<=39` determinantal condition on a `72x40` matrix, codimension 33 on 24 `tau`-parameters** — out of stdlib reach, and sampling cannot see a `10^-15` event. **I state this as a refusal, not as a negative result.**

5. **MY "CHEAPEST PATTERN" PRIOR IS BACKWARDS.** I assumed the uniform pattern is the cheapest sporadic one. Measured, the first moment **increases** with `t_D` (`N` grows faster than the merge conditions cost), so the largest is `(1,4,5)` at `10^-13.07`, **2.3 dex above** uniform's `10^-15.35` (`:36,40,54`). The brief's "cheapest pattern" is therefore a *low*-sharing pattern — which is a re-labelling of the banked `(SPLIT-4)`/`(QUAD-4)` classes, already searched-negative. **The pattern I targeted is not the pattern my own ledger nominates.**

6. **MY `N(1,1,7)` PRIOR IS OFF BY 1.6 DEX.** Registered `~10^30.1 +/- 0.3`; measured `10^31.74` (`:38`). `N(0,0,8)` was a HIT (`10^30.36` vs registered `10^30.4`, `:36`). R9.1 pre-registered that a count would be off; this is it.

7. **MY RATE MODEL IS REFUTED IN THE SAME DIRECTION AS ROUNDS 36 AND 37's — TOO LOW BY 10-27x — BUT FOR A DIFFERENT REASON.** R9.2 predicted the miss would come from multiplicative structure in the real-pencil `t_i`. It did not: **arms A and B are statistically indistinguishable** (`2.33e-4` vs `1.33e-4` at `q=193`; `1.10e-4` vs `1.30e-4` at `q=257`), so R5.1's arithmetic-vs-geometric discriminator resolves **GEOMETRIC**. The excess is degenerate components. **I got the direction right and the mechanism wrong.**

8. **THE `(SAT4)` DEGENERATE-FIBRE DOOR IS UNRESOLVED FOR A THIRD ROUND.** I derived its exact ledger effect (`D = 11 - delta`, and the ranking is `delta`-invariant, `:20-27`), which is more than round 37 had — but like round 37 (its MISS 9) **I never opened the banked `(SAT4)` statement to check whether `O >= 2` is legal.** It remains the cheapest live route and neither of three rounds has checked it.

9. **ARM A IS A NARROW SAMPLE OF "REAL" PENCILS.** 79 lines at `q=193` and **15** at `q=257` (`q193c:26`, `q257c:26`). The `q=257` arm-A conclusion rests on 15 pencils. It is the complete constant-norm supply (matching round 37's exhaustive `79 / 15`), but it is not a sample of *all* pencils, only of that family.

10. **NO `G` WAS BUILT; NOTHING IS GATED BY BANK 2's VERIFIER; `biv_core.py` WAS NEITHER COPIED NOR RUN.** No `W` on actual points, no per-side split, no outside completion, no bivariate system, no `|W| = 27` check, no `mu(x)` check at the middles. Rounds 36 (MISS 9) and 37 (MISS 10) carried this; **so do I, unchanged.**

11. **LAYER A WAS NOT RUN; `(SAT3)`-CONDITIONALITY IS UNTOUCHED; `m = 1` WAS NOT EXERCISED.** Fourth consecutive round.

12. **THE COINCIDENCE CURVE AND THE ORDER-3 MÖBIUS EXCLUSION ARE BANKED MACHINERY IN THIS REPO AND I DID NOT KNOW IT WHEN I REGISTERED R1.1-R1.3.** See CATCH-24A — this is the round's load-bearing subtraction.

---

## CATCH-24A — own-repo subtraction, run BEFORE every novelty claim

Every grep carried, at the **SEARCH** level, `--exclude-dir=r38_side_door --exclude-dir=r38_urate_genericity --exclude-dir=r38_cauchy_lattice --exclude-dir=pilots_20260802 --exclude-dir=prize-codex-1 --exclude-dir=prize-codex-2 --exclude-dir=prize-codex-3 --exclude-dir=.git --exclude-dir=__pycache__` **and `--exclude=dag.json`**. Hyphenated and infixed variants searched separately.

| object | in-repo prior | verdict |
|---|---|---|
| **the bidegree-`(2,2)` coincidence curve AND the order-3 Möbius exclusion — my R1.1/R1.2/R1.3** | **`notes/roadmap/sections/07-tracks.md:827`: *"A nonzero recovery kernel would put `2e` ordered exceptional pairs on one bidegree-`(2,2)` rational-map coincidence curve ... geometric reducibility would instead force an order-three Mobius deck map, whose only subgroup-heavy forms are incompatible with the order-`2^41` group"*; and `background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_official_trigonal_subgroup_exclusion/result.md:5`* — an entire PROVED node built on the same two devices.* `"coincidence curve"` = 8 files; `"Mobius deck"` = 8; `"order-three Mobius"` = 6; `"deck map"` = 10** | **HEAVILY BANKED — the round's load-bearing subtraction.** The repo already runs *my exact dichotomy* (curve-of-coincidences `=>` degree-3 map `=>` order-3 Möbius deck map `=>` incompatible with the `2`-power subgroup) on a **different object** (exceptional pairs on the Hankel distance-three packet, not `(BIV-CURVE)` tuple sharing) and a **different group** (order `2^41`, not `mu_64`). **I claim NO credit for the device.** New here: (a) the transfer to `(BIV-CURVE)` `m=4` sharing; (b) the **exhaustive finite** version (`83328` candidates, two fields, max 6 stable triples) rather than a bound; (c) the `|Stab(mu_64)| = 128` computation that repairs r36's R1.7. |
| the **projective slope line** / slope at infinity | **`background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_sharp_pair_exclusion/audit.md:17`: *"The projective formulation covers a possible slope at infinity"*;** also `..._distance_three_e1_hankel_design_route_fence/statement.md:68`, `..._bivariate_deficiency_clone_kernel_reduction/audit.md:13`. `"slope at infinity"` = 3 files | **BANKED PRACTICE, and I got it wrong first** (MISS 3). Claimed as nothing; reported as a registration error corrected mid-round. |
| `"sporadic (non-factoring) sharing"` | **`critical/nodes/rate_half_band_crossing_location/statement.md:4606, 4918, 5056`: the lane's own critical node already names it as the last untouched `m=4` route, priced `< 1e-4`**; `notes/pilots_20260811/r37_mint_drafts/share3_luroth_template/statement.md:113` | **BANKED AS THE OPEN ITEM — and re-priced here.** The term and the item are upstream. New: the taxonomy, the flat deficit 20, and the dichotomy that makes it the *only* alternative. |
| `Bezoutian` | `"Bezoutian"` = 3 files, of which the only non-mine is `notes/pilots_20260811/r36_sat3_on_l2/PREREG.md:293` — and inspection shows it is **a term in that pilot's own subtraction-grep list**, not a claimed object. `"Bezout"` = 195 files (textbook) | **term pre-exists in the pilot corpus; the object is classical.** Used, not claimed. The only content is that `Bez` has Jacobian rank 5, i.e. `{C_w}` is a hypersurface. |
| `"excess component"` | `critical/nodes/rate_half_band_crossing_location/statement.md`, `notes/pilots_20260811/r35_l2_gate/{REPORT,PREREG}.md`, `r37_mint_drafts/l2_nonempty_theorem/*` — **7 files** | **BANKED VOCABULARY, and it is the right frame for my D2 result.** Used, not claimed. |
| `"determinantal"`; `"hypergraph degree"`; `"prescribable"` | 85 / 8 / 7 files. `"prescribable"` is round 37's own coinage (`r37 REPORT.md:249`) | **banked methodology.** `"hypergraph degree"` is round 36's functional and I reuse its verifier semantics. |
| `"transitive closure"`, `"coincidence scheme"`, `"pattern-independent"`, `"degenerate-component"`, `"free merge"` (unhyphenated) | `"transitive closure"` = **1 file: my own script**; `"coincidence scheme"` = **0**; `"pattern-independent"` = **0**; `"pattern independent"` = **0**; `"free merge"` = 3, all mine or r37's | claimed new **as terminology only**. `"free-merge"` (hyphenated) = 7 files and the non-mine one is `r37 REPORT.md` — **round 37's functional, matched and re-measured here**, not invented. |
| Lüroth / the pullback lattice; `(OV)`/`(OUT-m)`/`(DEG-m)`; the demand law; the rational normal curve; the twisted cubic; the Segre count; `K_{4,4}` minus a perfect matching; the constant-norm family | `background/nodes/f_weight2_inverse/statement.md:9`; `critical/nodes/payment_completeness/statement.md:21`; `critical/nodes/rate_half_band_crossing_location/statement.md:3279-3311`; `background/nodes/rate_half_ca_hankel_endpoint_rational_normal_kernel_curve/statement.md:37` — all quoted at `r36 REPORT.md:117-125` and `r37 REPORT.md:106-114` | **BANKED — inherited wholesale from rounds 34-37. I re-derive nothing and claim nothing.** Pre-declared as zero-power item Z6. |

---

## D1 — THE SPORADIC TAXONOMY

### D1.1 The ladder (registered R2.1-R2.3, all HIT)

`slots = 3 t_D - delta + (m-2) t_M`, `rho = 15`, `D = slots - rho`; `(OV)` caps class size at `m-1 = 3` (`r36 D1.3`). Point conservation `n_1 + 2n_2 + 3n_3 = 24` gives `24 <= 3 t_D`, so

> **`t_D >= 8`, with equality iff `(n_1,n_2,n_3) = (0,0,8)`, and `D = 11 + 3(t_D-8) + 2(t_M-1) - delta`** — verified with **0 mismatches** over `t_D in [8,24]`, `t_M in {1,2,3}`, `delta in {0..3}` (`d1_taxonomy_results_b.txt:17`).

61 patterns satisfy the point equation. `t_D = 9` admits **exactly two**, `(0,3,6)` and `(1,1,7)`, both `D = 14`; `t_D = 10` admits **exactly four**, all `D = 17` (`:12-14`). Registered R2.3 verbatim; HIT.

### D1.2 The brief's slot-count-23 recheck — answered NO

`delta` shifts **every** pattern by the same `-delta`, so the ranking is `delta`-invariant (`:20-27`):

```text
 delta=0 (slots 26): t_D=8 D=11   t_D=9 D=14   t_D=10 D=17
 delta=1 (slots 25):        D=10          D=13           D=16
 delta=3 (slots 23):        D= 8          D=11           D=14
```

A `t_D=9` pattern needs `delta >= 3` merely to **tie** the uniform pattern's `delta=0` demand. Against the *measured* legal supply 10/9 (`r36 D2.2`) no non-uniform pattern survives at any `delta`; against round 36's nominal supply 12 one becomes admissible at `delta >= 2`, which is an **admissibility** statement only. **Round 36's `n_3 = 8` forcing survives the degenerate-fibre recheck intact.**

### D1.3 Derived in-round (NOT pre-registered): a pattern-independent slope floor

`X'_gamma = sum_{tuples ni gamma} k(tuple) <= 2m-2 = 6`, and `sum_gamma X'_gamma = 3 * sum_c |c| = 72`. Hence

> **`s >= 12` for EVERY pattern, uniform or not** (`:62`), against a target `s <= 13`.

The entire `m=4` `D`-part therefore lives in the two-value window `s in {12,13}`, and **no choice of sharing pattern can widen it by a single slope.** This is post-hoc and graded as such.

### D1.4 The cost ledger, and the correspondence question

The deficit derivation and its cancellation are in VERDICT item 2. The correspondence answer is VERDICT item 1. Two further fences:

- **Monomial-lattice mechanisms give only 2-power multiplicities.** If `Psi_a(x) = x^{r_a} f_a(x^d)` then `Psi(eta x) ~ Psi(x)` for `eta in mu_e` iff all `eta^{r_a}` agree, i.e. `e | 64`. Achievable multiplicities `{2,4,8,16,32,64}` — **3 is unreachable**, and the only one under the `(OV)` cap is `e = 2`, the banked `(SPLIT-4)+sigma(-x)` class (`:115,164`). This generalises `gcd(3,64)=1` from group actions to the whole monomial-structured family.
- **The exactness lemma (proved, not sampled).** For any `k <= deg+1 = 10` distinct points the evaluation `c -> (Psi(x_1),..,Psi(x_k))` is **surjective** (Vandermonde rank `k` per component), so the free coincidence rate of a random `Psi` on any `k`-set is **exactly** `(q^4-1)(q-1)^{k-1}/q^{4k}`, with **no `mu_64` structure effect**: `2.79e-4` expected free pairs and `7.98e-10` expected free triples per `Psi` at `q=193` (`:108`). **Counting is not dead at the single-class level here; it is exact.** Structure can only enter through the joint 24-point Vandermonde, which is a 33-codimension determinantal question I did not solve (MISS 4).

### D1.5 The targeted search that WAS run — the sporadic incidence cost table

Two fields, 40 draws of 8 disjoint random triples each, `Psi in P^39`:

```text
   rank  0 -> cost {9: 40}      rank 27 -> cost {9: 40}
   rank  9 -> cost {9: 40}      rank 36 -> cost {4: 40}   (b:95, 144)
   max triples prescribable with a NONZERO Psi (random tau) : {4: 40}
```

Random `tau` costs **9** per triple, budget `floor(39/9) = 4`; optimal `tau` costs `9 - 3 = 6`, budget `floor(39/6) = 6` — **against a demand of 8.** The residual 2 triples must be free, at `7.98e-10` each. This is the sporadic analogue of round 37's Segre fence and it is **wider**: the uniform route buys all 48 incidence conditions with the 7 parameters of `w`, which is precisely what the dichotomy says sporadic cannot do.

---

## D2 — THE DETERMINANTAL 3-IN-3 SOLVE

### D2.1 The residual count — the brief's premise is corrected (R4.2, HIT)

The brief states *"the family after 8 prescribed merges is EXPLICIT with kernel dim 2"*. By round 37's own cost table (7 edges at cost 2 = rank 14; the 8th costs 1 = rank 15, `r37 REPORT.md:209`), **8 prescribed merges leave kernel dim `16-15 = 1` — a single point of `P^15`, no free parameter.** The kernel-dim-2 state is the **7**-prescribed state, with ONE projective parameter and **FOUR** residual conditions. Measured: kernel dim exactly 2 in **`500,000 / 500,000` draws across every cell** (`q193c:34,54`; `q257c:34,54`). Registered before any search; **HIT, and it is three, not four, residual conditions only if one reads the brief's count.**

Three independent dimension counts agree at **4**: `15 - 11`; round 37's intrinsic `12 - 11 + 3`; and my new `(slope, scale)` chart — 8 cubics `f_i = s_i prod_{gamma in S_i}(X-gamma)` must satisfy the 4 left-kernel relations of the `8x4` matrix `[w(t_i)]`, i.e. **16 linear conditions on `13 + 8 = 21` parameters, 20 projective, `20 - 16 = 4`** (R4.5).

### D2.2 The degrees (R4.3), and the forced-root correction

On the pencil `Psi = alpha A + B` each coefficient of `R(t_i,.)` is linear in `(alpha,beta)`, so `Res_gamma` (the `6x6` Sylvester determinant of two cubics, degree 3 in each) is a **binary form of degree 6**. **Registered `<= 6`; HIT.** But the *legal* degree is `6 - p_i - p_j` (MISS 1), so the design matters:

```text
score = prod over residual edges of (6 - p_i - p_j);  rate ~ score/q^3
  unrestricted best 400, degrees (4,4,5,5)  -- SATURATES p_v = 3, REJECTED
  clean best (max p_v <= 2)  81, degrees (3,3,3,3), 3 subsets -- USED
  measured non-forced roots per residual edge: mean 0.967-0.981, four cells
                              (q193c:36-37,56-57 ; q257c:36-37,56-57)
```

All degrees `<= 6`; the solve is four gcd's on degree-`<=6` polynomials over `F_q`. **Stdlib-feasible with a very wide margin: 700,000 complete solves in under 10 minutes of ramguarded wall time.**

### D2.3 The sweep and its outcome

Merge graph `K_{4,4}` minus a perfect matching minus one edge, degrees `(3,3,3,2 | 3,3,3,2)` — unique up to isomorphism; what is swept is the assignment of the 8 fibre values to its 8 vertices, the 7-edge prescription subset, and 7 random slopes. Arm A draws `t_i` from the exhaustive constant-norm census (`651` slice cubics at every field, `79` lines with `>= 8` disjoint complete fibres at `q=193` with histogram `{8:70, 9:4, 10:3, 12:2}`, `15` at `q=257` with `{8:11, 9:4}` — **reproducing round 37's `79 / 15` exactly**, `q193c:24-28`, `q257c:24-28`). Arm B draws `t_i` at random.

**Result: 80 raw solutions, 0 legal, at two fields.** Full guard tallies and free-merge distributions are in the VERDICT block. The two arms are statistically indistinguishable, so **R5.1's discriminator resolves: the fence is GEOMETRIC, not arithmetic.**

### D2.4 The solvability rate, stated exactly on the swept sample

```text
              draws     raw solutions    rate        design-predicted
 q=193 arm A  120,000        28          2.333e-4        1.127e-5
 q=193 arm B  120,000        16          1.333e-4        1.127e-5
 q=257 arm A  100,000        11          1.100e-4        4.772e-6
 q=257 arm B  100,000        13          1.300e-4        4.772e-6
 pooled q=193 240,000        44          1.833e-4
 pooled q=257 200,000        24          1.200e-4     ratio 1.53
                                   q^-2 predicts 1.77 ; q^-3 predicts 2.36
 LEGAL rate, all cells:  0 / 440,000   ->  < 6.8e-6 at 95% confidence
```

---

## D3 — RECONCILIATION

**Round 37's fence needs its scope tightened in one direction and is confirmed in the other.**

- **Its own caveat is confirmed, and I confirm it against its own text.** Round 37 wrote that its budget of 8 *"bounds what an INCREMENTAL LINEAR instrument can prescribe. It does not bound the variety"* (`r37 REPORT.md:82`). My instrument performs exactly the operation it says a myopic scan cannot: a simultaneous solve of the residual conditions. **It works.** 80 times, at two fields, the 11-merge resultant system is satisfied. So the fence is correctly scoped as written — but round 37's *reading* of its free-merge data was too strong.
- **Round 37's free-merge count is REFUTED.** It reported free-merge support on `{0,1}` with *"maximum EVER observed, all runs: 2"* and *"Three has never been observed, by me or by round 36's 40000 ALLOC draws per field"* (`r37 REPORT.md:29,214`). **Three free merges occur 80 times in 674,393 eight-merge states, rate `1.19e-4`, at both fields.** Its sample was 115 and 128 states; mine is 674,393. The `0/1/2` shape is reproduced with means `0.050-0.068` against its `0.096/0.079`.
- **Round 37's CONCLUSION is confirmed, on a different mechanism.** All 80 are guard-illegal. So `|slopes| = 24 - merges` reaching 13 is not blocked by the *supply* of free merges — it is blocked by the fact that the extra merges land on **degenerate components** of the 11-merge variety.
- **The exact relationship between the dim-4 variety, its `F_q`-points, and the budget-8 locus.** The budget-8 locus is a `dim 7` family (`15 - 8`), reachable incrementally. `V`, the 11-merge variety, has `dim 4` — round 37's MISS 6 flagged the tension between "`dim 4`" and "budget 8" as unresolved. **Resolution: `V` is NOT irreducible, and the components my instrument reaches are all degenerate.** Two are named: `V_1 = {Psi : w(t_i)^T Psi = 0}` (codim 4, so `dim 11` — vastly larger than 4, an excess component that satisfies every edge at fibre `i` vacuously) and `V_2`, the locus with a slope of hypergraph degree 8. The measured `q^-2.1` scaling of the hit rate pins the reachable part at **codimension 2** in my 8-dim sampling family, not the codimension 3 an honest `dim 4` component would give. **The `dim = 4` count is realised by degeneracy.**

> **EXCLUSION CONJECTURE (C38), stated with falsifiers.** *The 11-merge variety `V subset P^15` has no `F_q`-point at which all eight slope cubics are non-degenerate with 3 distinct `P^1`-roots, no slope of hypergraph degree `> 2`, and pair multiplicity `1` — for `q = 193` and `q = 257`.* Equivalently: `(SHARE3-4)` cannot reach `|slopes| = 13`, and the `m=4` ceiling of 14 is a property of `V`, not of any instrument.
> **FALSIFIERS.** (F1) any verified 13-slope `Psi` at either field; (F2) a legal solution found by a full Gröbner solve of the 11 resultant conditions on `P^15` (the operation still out of stdlib reach); (F3) a non-degenerate component of `V` exhibited by primary decomposition; (F4) a legal solution under the degenerate-fibre slot count 23, where 10 merges suffice — **`(SAT4)` legality is unchecked for a third round (MISS 8) and this is the falsifier I would try first.**
> **Graded: a CONJECTURE on a 440,000-draw two-field sample under a named design, NOT an exclusion and NOT a theorem.**

---

## D4 — VERDICT AND THE `m`-BOUNDARY OF RECORD

```text
m = 1  : structurally disjoint, not exercised
         (critical/nodes/rate_half_band_crossing_location/statement.md:585-588)
m = 2  : REALIZABLE (two-field witness)      m = 3 : REALIZABLE (r34)
m = 4  : OPEN.  SEVEN classes searched-negative.  BOTH remaining routes now
         priced by derivation:
   * SPORADIC (non-factoring): deficit 20, first moment 10^-15.3 at q=193;
     no correspondence route (dichotomy); no order-3 Moebius route
     (exhaustive, max 6 of 8, two fields); no monomial-lattice route
     (2-powers only).  PRICED, NOT SEARCHED at the joint level.
   * (SHARE3-4) 13 slopes: the determinantal solve reaches the variety;
     80 raw solutions, 0 legal, two fields, 700k draws.  Best legal 14.
m = 5  : OPEN, not easier (r35: 7/15, 6/15)
m >= 7 : Cauchy-Schwarz binds; pencil classes die for q >~ 10^4 (CONDITIONAL)

CHANGED THIS ROUND
 * sporadic sharing : priced <1e-4 (r36, never searched) -> deficit 20, flat
   in the pattern, first moment 10^-15.3  [11 dex WORSE than banked]
 * the correspondence loophole : open -> CLOSED by dichotomy + measurement
 * r36's R1.7 argument : incomplete -> REPAIRED (dihedral stabiliser 128)
 * r37's "3 free merges never observed" : REFUTED (80 events, rate 1.2e-4)
 * r37's "does V have F_q-points the fence cannot see?" : YES, ALL DEGENERATE
 * the m=4 slope window : s in {12,13} is a pattern-independent floor
UNCHANGED
 * m = 4 is OPEN.  Best legal |slopes| = 14, third round, third instrument.
```

**CROSS-PILOT FLAG (written self-contained; I read no sibling `r38_*` directory and never `ls`-ed the parent).**

> **Four transportable items.** (1) **A prescribed condition poisons the elimination that follows it.** Every slope I prescribed became an automatic, guard-illegal root of every downstream resultant, cutting the legal degree from 6 to `6 - p_i - p_j`. Any lane that prescribes incidences and then eliminates should **factor out the prescribed locus before counting solutions**, or it will price its own search 3-16x optimistically. (2) **Maximising a Bezout score selects for degeneracy.** My highest-scoring design saturated three vertices and manufactured 11 of its 12 "solutions" on a component where a whole fibre vanishes. **Score the design by its degenerate locus, not only by its degree.** (3) **A resultant system that is satisfiable is not a configuration** — 80 raw solutions, 0 legal, and the two dominant kill modes were *both* previously-named artefacts in this lane. Any lane reporting "the simultaneous system has solutions" must run the structural verifier on the actual object. (4) **Check the chart before writing the guard.** My `U~(t) != 0` clause was rejecting the legitimate slope `gamma = infinity`; `PGL_2` acts freely on that line and the repo already banks the projective formulation (`..._quadratic_gap_four_sharp_pair_exclusion/audit.md:17`).

**Recommended node work (AUDIT-AND-DRAFT; I applied nothing, and I edited nothing outside my own directory).**

1. **Re-price sporadic (non-factoring) sharing** at `statement.md:4606, 4918, 5056`: the deficit is **20**, INDEPENDENT of `(n_1,n_2,n_3)`, first moment `10^-15.3` at `q=193` — **withdraw the `< 1e-4` figure**, which is optimistic by 11 dex.
2. **Bank the sporadic/uniform dichotomy**: `Z` finite XOR `Z` contains a curve `=>` Lüroth. No correspondence route: a non-factoring symmetric `(2,2)` has transitive-closure components far exceeding `deg Psi = 9`; `{C_w}` is a hypersurface in `P^5` (Bezoutian Jacobian rank 5/6, 200/200, two fields).
3. **Repair `(SHARE3-m)`'s no-order-3 clause**: `gcd(3,64)=1` excludes multiplicative order-3 elements only. The correct statement is `|Stab_{PGL_2}(mu_N)| = 2N` (dihedral, a 2-group), plus the exhaustive fact that **no order-3 Möbius map carries more than 6 stable triples of `mu_64`** at `q = 193, 257`.
4. **Bank the pattern-independent slope floor `s >= 12`** from `sum_gamma X'_gamma = 72 <= 6s`, and the ladder `D = 11 + 3(t_D-8) + 2(t_M-1) - delta` with its `delta`-invariance.
5. **Correct round 37's free-merge entry**: 3 free merges beyond the 8-merge state occur at rate `1.19e-4` (80 of 674,393 states, two fields) — its "never observed" is a small-sample artefact. **Keep its conclusion**: every such event is guard-illegal.
6. **Bank the degenerate decomposition of the 11-merge variety** and conjecture C38 with its four falsifiers.
7. **OPEN `(SAT4)` — third round of asking.** Is `O >= 2` legal? If yes the slot count drops to 23, 10 merges suffice, and round 36 already achieved 10. **Cheapest live route to a witness; unopened by three rounds.**
8. **Bank the forced-root and design-scoring lessons** as method notes on the `(SHARE3-m)` template.

---

## PREDICTIONS vs OUTCOMES

| registered (`PREREG.md`, "## Pilot registrations") | outcome |
|---|---|
| R1.1 dichotomy sporadic XOR uniform, `P=0.85` | **HIT (derivation + measurement)** — `b:79-80,128-129` |
| R1.2 `P(correspondence-sharing exists legally) = 0.07` | **resolved NO** — `{C_w}` is a hypersurface, Jacobian rank 5/6 (`b:74,123`); non-factoring forms carry no `Psi` |
| R1.3 no order-3 `sigma`, `P=0.90` | **HIT — exhaustively, max 6 of 8, two fields** (`b:177,194`); I did **not** predict that 6 is reachable |
| R1.3 `\|Stab(mu_64)\| = 128`, dihedral | **HIT exactly**, order histogram, 0 elements of order 3 (`b:181-183,198-200`) |
| R2.2 the ladder, uniform unique minimiser, `P=0.92` | **HIT — 0 mismatches** (`b:9,17`) |
| R2.3 exactly 2 patterns at `t_D=9`, exactly 4 at `t_D=10`, `P=0.85` | **HIT verbatim** (`b:12-14`) |
| R2.4 `delta`-invariance; `P(non-uniform survives at measured supply) = 0.03` | **HIT / resolved NO** (`b:20-27`) |
| R3.4 deficit `-20 + delta`, pattern-independent, `P=0.80` | **HIT — 0 mismatches** (`b:45`) |
| R3.5 `N(0,0,8) ~ 10^30.4` | **HIT — `10^30.36`** (`b:36`) |
| R3.5 `N(1,1,7) ~ 10^30.1 +/- 0.3` | **MISS — `10^31.74`, off by 1.6 dex** (`b:38`) |
| R3.5 `M ~ 10^-15.3`; `P(within 2 dex) = 0.55` | **HIT for the uniform pattern** (`b:36`); **but the ORDERING is backwards (MISS 5)** |
| R3.7 no structured sporadic sub-family with deficit `< 20`, `P=0.75` | **stands** — monomial lattices give 2-powers only (`b:115,164`); **F-R3 did NOT fire** |
| R4.2 rank `2r`, kernel dim 2 at `r=7`; the brief's "8 merges, kernel 2" is a slip, `P=0.85` | **HIT — 500,000/500,000 draws, four cells** |
| R4.3 residual degree `<= 6`, `P=0.85`; stdlib-feasible, `P=0.97` | **HIT on the RAW degree; the LEGAL degree is `6-p_i-p_j` (MISS 1).** Feasibility: **HIT, 700k solves** |
| R4.4 rate `1296/q^3 = 1.84e-4`; `P(within 10x) = 0.55` | **PARTIAL** — measured `1.1e-4` to `2.3e-4`, within 2x of the registered *number* but for the wrong reason; the design rate is `1.13e-5` and the excess is degeneracy |
| R4.5 the third dimension count = 4, `P=0.85` | **HIT** — `20 - 16 = 4`, agreeing with both banked counts |
| R5.1 `P(arms differ by >10x) = 0.35` | **resolved NO** — indistinguishable; **the fence is GEOMETRIC** |
| R5.2 `P(13-slope solution, arm A) = 0.20` / arm B `0.45` / any `0.22` | **all resolved NO** — 0 of 440,000 clean draws |
| R5.2 `P(dim-4 variety has `F_q`-points at q=193) = 0.60` | **HIT — YES, 80 of them; and all degenerate** |
| R5.4 expected best `\|slopes\| = 14`; `P(=14) = 0.50` | **HIT — exactly 14, both fields, both arms, both designs** |
| R6 MISS-2 guard G1-G5 | **USED, FIRED 80 TIMES.** G1 killed 39, G3 killed 27, G2 killed 2. **But G1 as registered was WRONG (MISS 3)** and was corrected to the projective slope line mid-round |
| R7 zero-power declarations | **HONOURED** — see below |
| R8 blind priors | all resolved above |
| R9.1 expected a registered count to be off by a small integer | **HIT — `N(1,1,7)` (MISS 6)**; the dimension counts 39, `-20`, 4, `2r` all held |
| R9.2 expected the rate to be too low, via multiplicative structure | **HIT on direction, WRONG on mechanism (MISS 7)** — degenerate components, and arms A/B agree |
| R9.3 expected the guard to kill raw hits incl. a slope collision | **HIT — 26 slope-degree-8 kills, r36's own artefact** |
| R9.4 expected the brief's "kernel dim 2 after 8 merges" to be its slip | **HIT** (R4.2) |
| R9.5 expected no witness; pre-committed to reporting the exact rate | **HIT and HONOURED** (D2.4) |

---

## ZERO-POWER DECLARATIONS

1. **Nothing this round decides `m = 4`.** D2's negative is a SAMPLED negative over a named merge graph, named designs (3 clean subsets), named pencils, and 440,000 clean draws at two fields. **It is not an exclusion of the 11-merge variety and not a decision of `m=4`.** Conjecture C38 is a conjecture with four named falsifiers.
2. **The deficit-20 count is a NAIVE FIRST MOMENT of exactly the kind round 36's MISS 3 refuted by 3400x. It has ZERO power to exclude sporadic sharing.** F-R3 remains live: exhibit any sporadic family with deficit `< 20`.
3. **Sporadic sharing was PRICED, NOT SEARCHED at the joint level** (MISS 4). The incidence cost table is a random-`tau` measurement; the optimal-`tau` budget 6 is derived, not measured; the 8-triple question is a codimension-33 determinantal solve I did not perform.
4. **The dimension counts do not establish non-emptiness of a NON-degenerate component.** I exhibited only degenerate `F_q`-points. I did not run a primary decomposition and I have no proof that a non-degenerate component is empty.
5. **My instrument reaches only the part of `V` meeting 7-prescribed-edge lines under 3 named designs.** A different design, a 6-prescribed/`P^3` solve, or a full Gröbner solve could reach components mine cannot. **The 100%-degenerate finding is a property of the swept sample.**
6. **The taxonomy is conditional on `(OV)`, `(OUT-m)`, `(DEG-m)` and the banked `rho = 4m-1`, `T_2 = rho` accounting, which is POSED with coordinator corrections** (`r36` ZP-10). It inherits that status. The `s >= 12` floor is post-hoc.
7. **The correspondence result is about symmetric bidegree-`(2,2)` forms and the transitive-closure mechanism**, measured on 60 forms per family per field. It is a derivation supported by measurement, not a theorem with a written proof.
8. **The order-3 Möbius result IS exhaustive** over all order-3 Möbius maps with a 3-cycle in `mu_64` (`sigma^3` fixes 3 points hence `sigma^3 = id`, so the enumeration is complete) — **at `q = 193` and `q = 257` only.**
9. **Arm A is the complete constant-norm supply, not a sample of all pencils** (79 / 15 lines). Nothing here bears on non-constant-norm pencils.
10. **Two fields is not `q`-uniformity.** No claim at official scale `q ~ 2^167`. The measured `q`-scaling (`q^-2.1`) describes the DEGENERATE locus, not the honest one.
11. **No `G` was built.** No outside completion, no bivariate system, no `\|W\| = 27` on actual points, no per-side split, no `mu(x)` at the middles. **`biv_core.py` and `share3_pencil.py` were NOT imported and NOT run: nothing this round is gated by bank 2's verifier.**
12. **Layer A was not run; `(SAT3)`-conditionality is untouched; `(SAT4)` legality is unchecked; `m = 1` was not exercised.**
13. **I claim NO credit for** Lüroth / the pullback lattice, the bidegree-`(2,2)` coincidence curve, the order-three Möbius deck map, the projective slope formulation, the rational normal curve, the twisted cubic, the Segre count, `(SPLIT-m)`/`(OV)`/`(OUT-m)`/`(DEG-m)`, the demand law, the constant-norm family, `K_{4,4}` minus a perfect matching, or the excess-component vocabulary. All banked (CATCH-24A).

---

## MEASURED FUNCTIONALS (CATCH-19C)

`m, N=16m, rho=4m-1, R=8m, T=rho+2, T_1=2, T_2=rho, a=7m-1, delta=m-1`; `|S_g ^ S_h| = m-1`, `|S_g D S_h| = 6m`; `X_gamma, X'_gamma, X''_gamma`; the shared-tuple hypergraph, its degree sequence and pair multiplicity; `k`, `(n_1,n_2,n_3)`; the tuple map `Psi`, its Lüroth degree, `w`, the constant-norm pencil and its complete-fibre count; `|slopes| = 24 - merges`; the incidence tensor and the bidegree-`(3,3)` form `R(t,gamma)`. **New here:** the tuple-class count `t_D` and the middle-class count `t_M`; the **degenerate-fibre count `delta`** and the slot law `3t_D - delta + (m-2)t_M`; the **demand ladder** and its `delta`-invariance; the **discrete pattern count `N`** and the **sporadic first moment**; the **sporadic deficit** `-20 + delta` and its pattern-independence; the **pattern-independent slope floor** `s >= 12`; the **coincidence scheme `Z`** and its finite/curve dichotomy; the **Bezoutian Jacobian rank** (5 of 6); the **transitive-closure component-size distribution** of `{S(x,y)=0}` on `P^1(F_q)`, generic vs Bezoutian; the **`sigma`-stable-triple histogram** over all order-3 Möbius maps and its maximum; `|Stab_{PGL_2}(mu_64)|` **and its order histogram**; the **sporadic incidence rank cost** conditioned on current rank, and the random-`tau` prescribable-triple budget; the **exact free-coincidence rate** `(q^4-1)(q-1)^{k-1}/q^{4k}`; the **prescription-set score** `prod(6 - p_i - p_j)` and its distribution over all `C(11,7)` subsets; the **non-forced root count per residual edge**; the **kernel-dim histogram at 7 prescribed edges**; the **common-`alpha` count per draw** and the measured **solvability rate** with its `q`-scaling exponent; the **free-merge distribution beyond the 8-merge state** (the round's key functional, matched to round 37); the **guard-outcome tally by clause**; the **legal `|slopes|` histogram** and its minimum. **Registered but not measured:** the joint sporadic 8-triple system (MISS 4); the optimal-`tau` budget 6 (derived only); `(SAT4)` legality; the split sub-case by search; any completion, bivariate system, per-side point split, `mu(x)` at the middles, or layer A.

---

## COMPLIANCE

**Registrations.** R0-R9 were appended to `PREREG.md` under `## Pilot registrations` with the **Edit tool in three parts**, after reading **exactly** the two named anchors (`r36_m4_nonsplit/REPORT.md`, `r37_share3_gap/REPORT.md`) and **before any other read, any grep, any `ls`, and any interpreter invocation**. The entire D1 taxonomy — the slot law, the ladder, the `delta`-invariant recheck, the near-uniform enumeration, the dichotomy, the correspondence count, the stabiliser repair, and the deficit-20 cancellation — and the entire D2 degree derivation — the residual parameter count, the correction to the brief's premise, the degree-6 bound, the gcd instrument, and the third dimension count — were derived **before any search**, as the brief required. The five blind priors the brief demanded are registered as a table with an expected-outcome phrase. **No post-registration addenda.** All five registration errors (R4.4's rate, R6's G1 clause, R3.5's `N(1,1,7)` and its pattern ordering, and the un-registered `s >= 12` floor) are reported as outcomes and misses, **not edited**.

**Compute law — NO BREACH. THE PRE-BASH CHECKLIST WAS APPLIED TO EVERY BASH CALL.** Nine interpreter invocations, **all nine** `RAMGUARD_TIMEOUT=290 tools/ramguard local -- python3 ...` from the repo root with the literal `--`: `d1_taxonomy.py` x2 (tags `a`, `b`), `d2_solve.py` x7 (tags `smoke`, `smoke2`, `smoke3`, `smoke4`, `q193`, `q193c`, `q257c`). **There was no bare `python3` invocation of any kind — not for patching, not for probes, and no empty-heredoc no-op between edits.** I scanned every command string before every Bash call as the checklist directs; the non-interpreter calls were `ls`, `grep`, `sed -n` (read-only), `wc`, `pgrep`, and one `until`-loop wait. **Ramguard status: all nine clean exits, zero wall kills, zero memory kills**; longest run 278.5 s (`q193`), which is inside the 290 s limit. Stdlib only (`sys`, `math`, `random`, `time`, `collections`, `itertools`); no third-party imports, no Modal, no network, no git, **no subagents spawned**. **The two-round bare-`python3` streak (r36 MISS 1, r37 MISS 1) ends here.**

**Write discipline — NO BREACH.** Every file edit went through the **Write/Edit tools** (`PREREG.md` x3, `d1_taxonomy.py` x1 create + 1 edit, `d2_solve.py` x1 create + 11 edits). **No `sed -i`, no `awk -i`, no `perl -i`, no `tee`, no shell redirection onto any file, and no in-place shell stream edit of anything.** One read-only `sed -n '818,840p'` was used to inspect a banked roadmap section; it writes nothing. Scripts wrote only their own results and checkpoint files.

**Results-file rules — HONOURED.** Every results file is opened in **append** mode **and** versioned per run by an argv tag: `d1_taxonomy_results_{a,b}.txt`, `d2_solve_results_{smoke,smoke2,smoke3,smoke4,q193,q193c,q257c}.txt`; `d2_solve_ckpt.txt` is append-only. **No rerun can erase a previous run's data** (round 36's MISS 8 does not recur). **No results-producing run was piped through `head`.** Runs were piped through `tail`, which consumes its entire input and cannot SIGPIPE early; and in every case the script had already written and `flush()`-ed its results file before printing, so no output was ever at risk. All long runs were read from their own results files, not from a pipe.

**Imported-script rule — NOT TRIGGERED, and declared.** **I imported and executed ZERO banked scripts.** No script was copied from `r34_*`, `r35_*`, `r36_*`, `r37_*`, `rh_*` or anywhere else, so no output-path audit was required and none was performed. Both scripts are new code written this round; every `open(...)` in them is hard-coded to the absolute path `notes/pilots_20260811/r38_sporadic_det/` and I duplicated the `mu`, rank, nullspace and polynomial helpers per file so that **no import exists between my own files either**. Round 37 recorded that `share3_pencil.py` writes at module level and round 35 was breached by exactly that; **I did not open, copy, or import it, nor `biv_core.py`.** The consequence is stated in MISS 10 and ZP-11: nothing this round is gated by bank 2's verifier.

**RAM discipline.** `dag.json` was **never opened**, and **every recursive grep carried `--exclude=dag.json`** in addition to the full `--exclude-dir` set. File-at-a-time reads; the only large statement file touched (`critical/nodes/rate_half_band_crossing_location/statement.md`, >5000 lines) was accessed **only** through `grep -n`, never read. The two banked node files inspected were read through one bounded `sed -n` window and one `grep -n`. All computation is small: the largest object is the 651-point constant-norm slice and its line dictionary (a few MB) inside a `local` 1G cgroup; the `16`-dimensional linear algebra is trivial. Every driver checkpoints in append mode.

**Quarantine — CLEAN.** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` was **never opened and never appeared in any tool output**. **`notes/pilots_20260811/` was never `ls`-ed**; the only directory listed was my own, by exact path, plus `tools/ramguard` by exact path. **None of `r38_side_door`, `r38_urate_genericity`, `r38_cauchy_lattice` was read, listed, or named by any tool** — all three were carried as `--exclude-dir` at the **SEARCH** level on every recursive grep, together with `pilots_20260802`, `prize-codex-1/2/3`, `.git` and `__pycache__`. **No output filtering after traversal was used at any point.** No path containing `prize-codex-` was touched. Sibling-pilot files opened were the two named anchors only; `r36_sat3_on_l2/PREREG.md:293`, `r37_mint_drafts/share3_luroth_template/statement.md:113` and `r35_l2_gate/*` appeared as grep **hits with line context** (all `r35_*`/`r36_*`/`r37_*`, explicitly readable) and none was opened as a file.

**Write scope.** Every write is inside `notes/pilots_20260811/r38_sporadic_det/`: `PREREG.md` (registrations), two new scripts, ten results files, one checkpoint file — **14 entries, and no `REPORT.md`**. **No** `dag/`, `nodes/`, `critical/`, `background/`, `experiments/` or `tools/` edits; no git; the session scratchpad was not used and no scratch file went to `/tmp`. The eight node-work items in D4 are **recommendations only — nothing was applied** (AUDIT-AND-DRAFT).

**Method discipline.** Own-repo greps (CATCH-24A) preceded every novelty claim, **including hyphenated and infixed variants** (`free merge` vs `free-merge`, `coincidence scheme` vs `coincidence-scheme`, `Moebius` vs `Mobius`, `order-3` vs `order-three`, `pattern-independent` vs `pattern independent`, `Bezoutian` vs `bezoutian` vs `Bezout`, `transitive closure` vs `transitive-closure`), and every low-count hit was **inspected rather than counted** — which is how the `Bezoutian` hit turned out to be a term inside another pilot's own subtraction-grep list rather than a claimed object. The greps produced **seven live subtractions, one load-bearing and one that reversed a registered guard**: the bidegree-`(2,2)` coincidence curve *and* the order-three Möbius deck map are a PROVED banked node plus a roadmap entry, and the projective slope formulation is banked practice that my registered G1 clause contradicted. **Two-field confirmation on every structural claim** (`F_193` / `F_257`) on all of D1 and all of D2. Every quantifier claim carries a `file:line`. Every max-quantified claim carries a zero-power declaration and its budget. The round's self-caught errors — the forced-root degree error, the degeneracy-maximising design that manufactured 11 of 12 solutions, the wrong affine-chart guard, the backwards pattern-ordering prior, the 1.6-dex `N` miss, and above all the **80 raw solutions that the MISS-2 guard killed** — are reported as errors, in the misses section, ahead of the results.

**`REPORT.md`.** The brief pre-declares that the harness refuses this write, so I did not spend a tool call attempting it; **the directory contains 14 entries and no `REPORT.md`**, and this report is returned verbatim as the final message per the brief's fallback clause.
