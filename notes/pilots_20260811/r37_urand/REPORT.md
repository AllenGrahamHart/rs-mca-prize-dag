All five registered runs are done. Full report follows.

---

# REPORT — r37_urand (round 37)

## VERDICT

**U-RAND IS PRICED, AND THE PRICE IS THAT STATEMENT U IS FALSE. Not "unproven" — constructively false, at razor-faithful shape, on the razor's own domain type (a multiplicative subgroup `mu_n < F_q^*`), with exhaustive-census confirmation. The mechanism is not exotic: a bad slope reaching the syndrome through a codeword costs the adversary exactly `rho` net conditions on the `2(r+1)` free values of `(e_0,e_1)` on `W` — independent of the spend `t`, independent of the field, independent of `rho` in form. So the adversary can BUY U-rand slopes at a fixed exchange rate and stack them until the parameter budget runs out. I solve that linear system and exhibit the pencils: at `mu_20` the exhaustive census returns `T = (r+1) + j` EXACTLY for `j = 1,2,4,6,8` against a first moment of `0.25` (`g3_results.txt:57-61`), column-far at every row, and `j = 9` is unreachable — the parameter cap `floor((2(r+1)-1)/rho) = 8` attained on the nose, at three fields. At `mu_26`, `rho = 3`, the FULL census `C(26,10) = 5,311,735` returns `T = 17 = (r+1) + 6` with `T_fib = 11 = r+1`, column-far, against a first moment of `1.3e-4` — a factor 45,000 excess (`g5_results.txt:16-17`). At the razor the same count gives `j <= 126` with kernel dimension exactly `2` at `j = 126`, so:**

```
B_ca^far(k+2^34)  >=  r+1 + 126  =  1,082,331,758,719   (construction, modulo a
                                                         genericity lemma)
B_ca^far(k+2^34)  <=~ r+1 + 126                          (parameter count, heuristic)
```

**— i.e. U-rand is an ADDITIVE `O(n/rho) = O(128)` term, not a multiplicative blow-up, and the banked pin `B_ca^far(k+2^34) = r+1 EXACTLY` (`crossing_location:4483-4485`) must be withdrawn and replaced by `r+1 + Theta(n/rho)`. In bits nothing moves: `log2(r+1+126) = 39.977280`, identical to `log2(r+1)` to six decimals (`g5_results.txt:21,25`).**

Five results, each two-field-or-better:

1. **The exchange rate, three independent derivations, all agreeing on `rho-1`** (D1). Degree bookkeeping, linear algebra, and the geometry of `V_S = syn(F_q^S)` all give: a codeword-mediated slope is `rho` conditions on `(e_0,e_1)` and `rho-1` after the slope itself is counted as an unknown, **uniformly in the spend `t`**. Machine-confirmed by the attained caps at 4/7 cells.

2. **FENCE-1, unconditional and 100% measured.** `|S_gamma u W| <= R => c = 0`: no bad slope spending fewer than `rho+1-f` points off `W` can be U-rand. Zero violations in **297 analysed codeword-mediated incidences** across 14 (cell, field) rows, two shapes, two domain types (`g1_results.txt:45,82,119,139,193,230,267,304,341,378,458,491,533,570`, every row `MDS violations (wt(c)<R+1)=0`).

3. **The minimal-spend rigidity theorem, confirmed.** At `t = rho` the mediating codeword is forced to be a **minimum-weight** codeword with `W subset supp(c)`: `wt(c) = R+1` exactly at **18/18** minimal-spend incidences, two shapes, six fields (`g1_results.txt:17,22,26,29,30,33,35,36,41,42,58,63,74,165,170,187,223,248,467`). And `W subset supp(c)` held at **100% of all 297** incidences, not just the minimal-spend ones — stronger than I derived.

4. **THE rho=3 SYMMETRIC-T SECONDARY IS DECIDED, AND ANCHOR 1'S PARITY PREDICTION IS REFUTED.** It does not survive at `rho = 3`. The surviving carrier slopes at `rho = 3` and `rho = 4` are **exactly the fibre slopes**, both set inclusions True, excess **0**, at 2 fields x 2 shapes x 2 domain types (`g5_results.txt:5,7,9,11`). At `rho = 2` the same carrier carries an excess of **318** (`g5_results.txt:13`). The correct condition count is `ceil(rho/2)`, not `floor(rho/2)`. Bonus: anchor 1's unexplained `T = 336` at H2 is now **decomposed exactly** — `336 = 5` fibre `+ 323` carrier `+ 8` residual against a null of `7.59` (`g4_results.txt:9,12`), and on `mu_22` the carrier explains `330/330`, residual `0` (`g4_results.txt:84-85`).

5. **The `C(128,63)` correspondence: the two objects are NOT the same, and the cap does NOT transport — but the DEDUP does.** `C(128,63) = 2^124.149066`, `C(127,64) = 2^123.171434`, ratio exactly `128/65` (verified as an integer identity), `C(128,63) - C(127,64) = C(127,62)` (`g5_results.txt:38-42`).

`B_ca^far(k+2^34) < 2^128`: **NO.** I add no upper bound. I do add the first *constructive* improvement to the lower bound since LB1, and the first non-vacuous pricing of the last far-CA mode.

---

## MISSES FIRST

1. **MY OWN REGISTERED CONSTANT IS WRONG. I registered `log2(128/65) = 0.977488` (A-1); it is `0.977632`** (`g5_results.txt:43`). Off by `1.44e-4`. The *use* I registered it for — a pre-declared warning that it is NOT `log2((r+1)/2^39) = 0.977280` — is correct and the machine confirms `EQUAL? False`. But I stated a number blind and got it wrong in the fourth decimal, and I report it rather than quietly using the machine value. Anchor 2's miss 5 in a new costume: I nearly banked a numerological identity, and this time I registered the warning first.

2. **MY j-LADDER SKIPPED `j = 4,5` AT BOTH `rho = 4` CELLS, SO RUN 3's HEADLINE NUMBER "3" WAS A FLOOR MASQUERADING AS A MAXIMUM.** `g3_results.txt:45-51,80-85` reports `LARGEST j = 3` at `intZ n=34` and `mu_34` — but the ladder was `[1,2,3,6,7]`. Filling the gap in run 4 gives `j = 5` (`intZ`) and `j = 6` (`mu_34`, which is `floor(6.75)`, the cap attained) — `g4_results.txt:101-102,108-110`. **My own experimental design produced a two-fold understatement of my own headline.** Caught by re-reading my own ladder, not by anyone else.

3. **`intZ n=26 rho=3` AND `mu_26 rho=3` MISS THE PARAMETER CAP BY ONE AND I CANNOT SAY WHETHER THAT IS THE CAP OR MY SEARCH.** Cap `(2(r+1)-1)/rho = 7.000` exactly; observed max `j = 6` at both (`g3_results.txt:39,74`). Since `mu_34` went from `3` to `6` purely by raising `tries` from 6 to 25, the honest reading is **search-limited, not cap-limited** — but I did not re-run `rho = 3` with more tries and I do not claim `7` is unreachable. The cap is attained at 4/7 cells (`intZ n=20`: 8/8.5; `intZ n=24`: 10/10.5; `mu_20`: 8/8.5 at two fields; `mu_34`: 6/6.75) and one short at 3/7.

4. **THE `A-5` T_rand BOUND I REGISTERED IS FALSE AT ONE FIELD.** I registered "C1/F2 at `q >= 65537`: `T_rand` small (`<= 4`)". Measured `T_rand = 5` at `q = 65537` (`g1_results.txt:307`). Only the `q = 999983` row (`T_rand = 2`, `:344`) satisfies it. The `T_sym = 84 = C(9,3)` half hit exactly at three fields.

5. **MY OWN `R2j` PREDICTION — "any structured `T_rand` family will be a disguised `T_sym` family" (P = 0.55) — IS REFUTED BY MY OWN CONSTRUCTION.** The engineered pencils have `T_sym = 0` at every census row (`g3_results.txt:8-12,57-61`) and `T_rand = j`. The U-rand mechanism is **not** a symmetry mechanism: it needs no automorphism of `D`, it works on a generic domain, and it works at `rho = 3` where every symmetry mechanism is dead. I registered the wrong half at 0.55 and the right half (a genuinely non-symmetric structured family) at 0.30.

6. **THE INTEGER-COLLINEAR MINIMAL-SPEND FAMILY IS AN ARTEFACT OF THE STAND-IN DOMAIN AND I ALMOST REPORTED IT AS THE HEADLINE.** `g2_results.txt:9-13,20-24,31-35` exhibits exactly one field-size-independent minimal-spend U-rand slope at 3 of 4 negation-closed `rho = 2` cells — `gamma = -1/4`, `-37/28`, `-3/16`, each an exact **rational**, each verified by the direct pencil test at two fields — and **0 at all three non-negation-closed controls** (`:50,58,66`) and **0 at every `rho = 3,4` cell** (`:74,82,90,98,106`). It is beautiful and it is a fact about *integer* collinearity in `D = {+-1..+-m}`. **The razor's `D` is a multiplicative subgroup of `F_q^*`; "integer collinearity" is not a property it has.** I claim **ZERO POWER** for its transport (ZP-13). The transportable result is the construction, which is pure linear algebra.

7. **NO PROOF THAT THE CONSTRUCTION TRANSPORTS TO THE RAZOR.** The dimension count is exact at razor parameters (unknowns `2(r+1)+126 = 2,164,663,517,312`, equations `126(rho+1) = 2,164,663,517,310`, kernel `>= 2`). What is NOT proved is that the coefficient matrix has full rank there, nor that a kernel vector exists satisfying the four genericity side-conditions (`lambda_i != 0`, `chi` injective on `W`, `gamma_i` not a fibre slope, column-farness). At every cell I could reach, a valid vector was found within 60 random draws. **This is one genericity lemma short of an unconditional lower-bound improvement, and I say so rather than claim the bound.**

8. **NO RAZOR-SCALE MEASUREMENT, AS REGISTERED.** All machine numbers at `q <= 999983`, `R <= 17`, `rho <= 4`, `r <= 13`. Registered `q <= 999983` in advance specifically so no widening would be needed (anchor 1 miss 9, anchor 2 miss 7) — and **no widening occurred**.

9. **ONE CENSUS ROW IS COLUMN-CLOSE AND IS EXCLUDED.** `g1_results.txt:9` — C1/F1 at `q = 101` has 1 common locator, `mu_1 = 12.35`. Reported, flagged in-line by the script (`ROW EXCLUDED FROM CONCLUSIONS`), used for nothing. Anchor 1's miss 8, reproduced.

10. **`T_rand` AT `rho >= 3` STILL HAS NO EXHAUSTIVE CENSUS EXCEPT ONE.** I got exactly one: `C(26,10) = 5,311,735` at `mu_26` (`g5_results.txt:17`), which anchor 1 declared out of reach (its ZP-10). `C(28,11) = 21,474,180` and `C(34,13) = 9.3e8` remain out of reach. So the `rho = 4` construction is verified slope-by-slope but its **column-farness and total `T` are unmeasured** — declared (ZP-4), not hidden.

11. **NO BOUND.** `B_ca^far(k+2^34) < 2^128` remains **NO**. Registered B-12 at 0.03.

---

## CATCH-24A SUBTRACTIONS (own-repo greps before every novelty claim)

Every recursive grep carried, at search level: `--exclude-dir=r37_third_solve --exclude-dir=r37_share3_gap --exclude-dir=r37_mint_drafts --exclude-dir=pilots_20260802 --exclude-dir=prize-codex-work --exclude-dir=.git --exclude-dir=__pycache__ --exclude=dag.json`. Sibling names taken from `CONSTRAINTS.md:38-39`, never from an `ls`. Hyphenated and infixed variants included (`codeword[- ]?mediated`, `type[- ]?2`, `min[- ]?distance spend`, `S_gamma *\\ *W`).

| # | claim | grep | banked? | verdict |
|---|---|---|---|---|
| 1 | Statement U, `T = T_fib+T_sym+T_rand`, U-sym killed at razor `rho`, U-rand unpriced, `U => B_ca^far = r+1` | `-rniE "statement u\|T_rand\|U-rand"` | **YES** — `critical/nodes/rate_half_band_crossing_location/statement.md:4476-4494`, `:4592-4594`, `:4639` (round 36, coordinator-audited) | **SUBTRACTED — this brief's own provenance.** My additive part is the REFUTATION of U and the pricing of U-rand |
| 2 | "codeword-mediated mode", "reaches the syndrome through a codeword" | `-rniE "codeword[- ]?mediated\|through a codeword"` | **YES** — `crossing_location:4639`; `r36_hrlow/REPORT.md:31,247,275,337` | **SUBTRACTED — round 36's phrase and framing** |
| 3 | **"one support pays for at most one slope"** (my R2e(iii) "each `V_S` contributes at most one slope") | `-rniE "at most one slope"` | **YES** — `critical/nodes/counting_frame/statement.md:9` and `critical/nodes/v8_ledger/statement.md:9` (Paper D v12 quotient-support ledger, PROVED-cited); also `background/nodes/rate_half_far_ca_rider_reduction/proof.md:28` | **SUBTRACTED IN FULL — this is Paper D's, not mine.** My geometric restatement (`l subset V_S <=> column-close`) adds only vocabulary |
| 4 | **the minimum-distance spend `\|S_gamma \ W\| >= (R+1) - \|W\|`** (my FENCE-1's inequality) | `-rniE "min[a-z]* [- ]?distance spend"`, `-rniE "S_gamma *\\\\ *W"` | **YES** — named as the baseline at `background/nodes/rate_half_type2_fr_two_type1_fibre_spend_calibration/statement.md:48` ("a valid algebraic improvement over the minimum-distance spend") and `background/nodes/rate_half_fr_canonical_min_pair_union_bound/statement.md:50`; spend floors `(TFC3)/(TFC4)` at `:35,43`; `crossing_location:787` `min \|S_gamma\W\|=m+2` | **SUBTRACTED — the INEQUALITY is banked** (in the FR/type-2 lane at strict-endpoint parameters `N=16m, rho=4m-1, a=7m-1`, which anchor 2 proved VACUOUS on the far-CA bracket and which I did not import). **ADDITIVE:** its instantiation at razor shape with the FORCED `\|W\| = r+1` (giving `t >= rho+1-f`), its CONTRAPOSITIVE as a fence (`\|S u W\| <= R => c = 0 =>` fibre), and 297/297 measurement |
| 5 | `(C2)` per-slope spend floor `(R+1)-w*`, vacuous by sign on the bracket | `-rniE "R\+1 *- *\|W\|\|R\+1-w\*"` | **YES** — `crossing_location:3615`; `r35_fg_razor/REPORT.md:144,163` | **SUBTRACTED, and it is a SCOPE FENCE I obeyed** (ZP-8): I imported nothing from the type-2 ledger; my spend law is derived here from MDS distance alone |
| 6 | **adversarial engineering saturating at a dimension count ("`sigma` conditions per alignment against `2n` dof")** — the METHOD of my parameter cap | `-rniE "dimension count.*dof\|2n dof"` | **YES** — `critical/nodes/xr_smallcore_spread_count/node.json:9` (F5-A2: "adversarial spread engineering saturates at `Theta(n)` (0.55n measured across 3 scales; dimension count ... confirmed), the dimension argument is a proof lead for the floor"); `f5_sunflower_pencil_lemma/node.json:7` ("engineered pencil-stacking absorbed by the tangent strip exactly as predicted") | **SUBTRACTED — the METHODOLOGY is banked in the xr/F5 lane** (different object: aligned aperiodic supports, spread families). **ADDITIVE:** the far-CA instantiation, the exact exchange rate `rho` per slope, its spend-independence, and the razor value 126 |
| 7 | MDS `wt >= n-K+1`, minimum-weight codewords, "no triple collinear" | `-rniE "MDS\|minimum[- ]weight codeword"` | **YES** — `critical/nodes/rate_half_list_adjacent_crossing/statement_sections/11-h1-s3-addendum.md:26,38,47` (LIST lane: list members of a received word). Also `notes/literature_map_20260726/deep_read_plan.json:266` flags Chen–Zhang line/ball as dominating headliner E | **SUBTRACTED — textbook + banked in the list lane.** My objects (bad slopes of a Hankel pencil, cosets of the RS code) are different; the `P^2` collinearity of `chi_Y(W)` is a different plane and a different incidence |
| 8 | `C(128,63)`-vs-`C(127,64)`, ratio `128/65`, "~0.98 bits, ONE binomial step, not equal, correspondence still to check" | `-rnE "C\(12[78], *6[345]\)\|128,63\|127,64"` | **YES** — `crossing_location:4427`, `:4493-4494` (round 36's own flag, coordinator hand-checked); the plateau at `crossing_location:688-700`, `rate_half_band_closure/statement.md:379`, `node.json:9` | **SUBTRACTED — the relation and the ratio are banked.** **ADDITIVE:** the exact integer verification, the identification of both objects, and the transport verdict (dedup yes, cap no) |
| 9 | the Lam–Leung + nesting cap on the coset/qcore supply plateau | same grep | **YES** — `rate_half_band_closure/node.json:9` (witness-hunt recon 2026-07-12) | **SUBTRACTED.** My use is a *negative* one: it does not transport to `T_sym` |
| 10 | `B_ca^far(k+2^34) >= r+1 = 2^39.9773`, LB1 | `-rnE "B_ca\^?far"` | **YES** — `crossing_location:654-656` | **SUBTRACTED.** I reproduce `1,082,331,758,593 = 2^39.977280` exactly (`g5_results.txt:21`) and my construction ADDS `+126` to it |
| 11 | **`u = h_gamma + c` with `c` in the RS code; the far-CA count as "cosets of an MDS code with a leader of weight `<= r`"** | `-rniE "e_0 *\+ *gamma *e_1 *\+"`, greps 1-2 | round 36 NAMES the mode ("through a codeword") but states no algebra; **zero hits for any decomposition, any `c`-side degree bookkeeping, any coset-leader framing** | **ADDITIVE** |
| 12 | **the `rho-1` over-determination law, uniform in the spend; `chi_Y : W -> P^2` as the `c`-side analogue of `chi`; the minimal-spend minimum-weight rigidity** | greps 1,2,6,7 | **ZERO HITS** | **ADDITIVE** |
| 13 | **the parameter cap `T_rand <=~ 2(r+1)/rho`, razor value 126; the `f`-optimisation showing `f = 1` optimal** | `-rniE "2r/rho\|2\(r\+1\)/rho"` | **ZERO HITS** | **ADDITIVE** (method subtracted at #6) |
| 14 | **the refutation of Statement U; a far-CA count above `r+1` that survives at `rho >= 3`** | `-rniE "U (is\|was) (false\|refuted)"`, `-rniE "beyond r\+1"` | **ZERO HITS** | **ADDITIVE — the round's headline** |
| 15 | **the `(X-x_0)P(X^2)` symmetric-`T` carrier and the `ceil(rho/2)` condition count** | `-rniE "symmetric-?T\|parity derivation"` | round 36's `floor(rho/2)` derivation is banked at `crossing_location:4472,4487` **as an unmeasured GAP**; the carrier itself has **zero hits** | **ADDITIVE — and it REFUTES the banked derivation** |

**Genuinely additive this round:** (a) the codeword decomposition `u = h_gamma + c` and the identification of the far-CA count with coset-leader weights of an MDS code; (b) FENCE-1 as a fence (the inequality subtracted at #4); (c) the `rho-1` over-determination law with three independent derivations and its spend-independence; (d) `chi_Y : W -> P^2` and the `rho+1`-collinearity criterion; (e) the minimal-spend minimum-weight rigidity, and the empirical `W subset supp(c)` at 100%; (f) the U-rand **construction**, its exhaustive-census verification, and the parameter cap `2(r+1)/rho` with razor value 126 (method subtracted at #6); (g) the refutation of Statement U; (h) the `ceil(rho/2)` symmetric-`T` count, the death at `rho = 3`, and the exact decomposition of anchor 1's `T = 336`; (i) the `C(128,63)` transport verdict.

---

## D1 — THE ALGEBRA OF A CODEWORD-MEDIATED SLOPE

### D1.1 The code, and what `c != 0` costs

With `syn(u)_m = sum_{x in D} u(x) v_x x^m`, `m = 0..R-1`:

```
C := ker syn = { g|_D : deg g <= k-1 },   an [n,k] MDS code,  d_min = R+1.
```

(`sum_x v_x x^j = 0` for `j <= n-2` kills every moment when `deg g <= k-1`; dimensions match.) So for a bad slope `gamma` with error `u` (`supp u subset S_gamma`, `wt u <= r`) and the forced common-support data `h_gamma := (e_0 + gamma e_1)|_W`:

```
u = h_gamma + c ,   c in C .      c = 0  <=>  fibre slope.
```

**The cost of `c != 0`, exactly.** `supp(c) subset S_gamma u W`, so `wt(c) >= R+1` forces

```
t := |S_gamma \ W|  >=  R+1-|W|  =  rho+1-f    ( = rho at f = 1 ).
```

**FENCE-1 (unconditional).** Contrapositive: `|S_gamma u W| <= R => c = 0 => supp(h_gamma) subset S_gamma n W subset W`, and `gamma` is a fibre slope with a locator inside `W`. **Measured: 297/297 codeword-mediated incidences satisfy it, zero MDS violations, 14 (cell,field) rows, 2 shapes, 2 domain types** (`g1_results.txt:45,82,119,139,193,230,267,304,341,378,458,491,533,570`); the per-row `min t` is `2 = rho+1-f` at 10 rows and `>= 3` at 4 (`:14,51,88,125,162,199,236,273,310,347,388,407,427,464,539`).

**Degree bookkeeping.** `c = g|_D` vanishes on `D \ (S u W)`, so `g = Z*m` with `Z = prod_{y in D\(SuW)}(x-y)` and `deg m <= |W|+t-R-1`. The prescribed values on `W \ S` (size `f+t`) give `f+t` equations in `(|W|+t-R)` coefficients of `m` **plus** the unknown `gamma`, and the system is **linear in `(m, gamma)` jointly**:

```
   (f+t) - (|W|+t-R) - 1  =  R - r - 1  =  rho - 1 ,     INDEPENDENT OF t AND f.
```

**Three independent derivations agree.** (i) the above; (ii) the affine system `m(x)Z(x) + e_0(x) + gamma e_1(x) = 0` on `W\S`; (iii) geometry: put `V_S := syn(F_q^S)`. Then `gamma` is bad via `S` iff the affine line `l = {y_0+gamma y_1}` meets `V_S`; column-far iff no `V_S` contains `l` (whence Paper D's "one support, one slope", subtraction #3); at `f = 1`, `l subset V_W` and `syn|_{F_q^W}` is an isomorphism onto `V_W`; and

```
|S u W| <= R   =>  V_S n V_W = V_{SnW}     ( codim_{V_W} = |W\S|; = 1 for S subset W — this IS chi )
|S u W| >= R+1 =>  codim_{V_W}(V_S n V_W) = rho  generically.
```

**The fibre/codeword transition is exactly the jump `codim 1 -> codim rho`: the effective fibre parameter jumps from `f` to `rho`.**

### D1.2 The `c`-side analogue of `chi`: `chi_Y : W -> P^2`

At `f = 1` and minimal spend `t = rho`, `wt(u) <= r` forces `|A| >= t+1` where `A = {x in W : c(x) = -h_gamma(x)}`, hence `|supp(c) n W| >= R+1-t = |W|`, hence

> **MINIMAL-SPEND RIGIDITY.** `c` is a **minimum-weight** codeword: `wt(c) = R+1` exactly, `W subset supp(c)`, and `c = lambda * Z_Y|_D` with `Y = D \ supp(c)`, `|Y| = k-1`, `Y n W = empty`.

**Measured: `wt(c) = R+1` and `minwt: True` and `W <= supp(c): True` at 18/18 minimal-spend incidences, two shapes (`|W| = 9` -> `wt(c) = 11 = R+1`; `|W| = 11` -> `wt(c) = 13 = R+1`), six fields** (`g1_results.txt:17,22,26,29,30,33,35,36,41,42,58,63,74,165,170,187,223,248,467`). **A-7 HIT.** And `|supp(c) n W| = |W|` at **100% of all 297** incidences, including every large-spend one — stronger than derived.

Consequently, defining

```
chi_Y : W -> P^2 ,   x |-> [ Z_Y(x) : e_0(x) : e_1(x) ] ,
```

**`gamma` is U-rand at minimal spend iff some line of `P^2` meets `chi_Y(W)` in at least `rho+1` points.** `chi` is the degeneration `Z_Y == 0`, where the demand drops to `>= f = 1` point. **`chi` asks for a fibre of size `f`; `chi_Y` asks for a collinear set of size `rho+1`.** That is the answer to D1's question, and the rank condition on the `(rho+1) x 3` matrix `[Z_Y|_A, e_0|_A, e_1|_A]` is `rho-1` conditions — the third derivation of the same number.

**Exact criterion (the census oracle).** `S` gives a bad slope iff `M_0 sigma_S` and `M_1 sigma_S` are proportional in `F_q^rho = V_W/(V_S n V_W)`; `T_rand = 0` iff that `2 x rho` matrix has rank 2 for every `S` with `|S u W| >= R+1`.

---

## D2 — THE CENSUS

Exhaustive sweeps of all `C(n,r)` split locators; every row prints `4rho<R`, `a>R+1`, `a-1>r` and every row is **FAITHFUL** (`g1_results.txt:6,155,382,401,420,495`).

**C1 = `n=20,k=10,R=10,rho=2,r=8,a=12`, `D = {+-1..+-10}`** (anchor 1's H1 shape). `mu_1 = 12.3488, 1.03423, 0.123733, 0.00125794, 2.93288e-05, 1.25974e-07` — **reproduces anchor 1 and anchor 2 exactly** (A-3 HIT).

| family | `q` | `T` | `T_fib` | `T_sym` | `T_rand` | null `q*mu_1` | far? | ref |
|---|---|---|---|---|---|---|---|---|
| F1 (LB1) | 349 | 225 | 9 | 0 | 216 | 361 | far | `:48` |
| F1 | 1009 | 120 | 9 | 0 | 111 | 125 | far | `:85` |
| F1 | 10007 | 22 | 9 | 0 | 13 | 12.59 | far | `:122` |
| F1 | 65537 | **9** | **9** | 0 | **0** | 1.92 | far | `:142` |
| F1 | 999983 | **9** | **9** | 0 | **0** | 0.126 | far | `:148` |
| F2 (`d=2`) | 10007 | 104 | 9 | 84 | 11 | 12.59 | far | `:270` |
| F2 | 65537 | **98** | 9 | **84** | 5 | 1.92 | far | `:307` |
| F2 | 999983 | **95** | 9 | **84** | 2 | 0.126 | far | `:344` |
| K1/F2 control `D={1..20}` | 65537 | 10 | 9 | **0** | 1 | 1.92 | far | `:386` |
| K1/F2 control | 999983 | **9** | 9 | **0** | **0** | 0.126 | far | `:394` |

**C2 = `n=24,k=12,R=12,rho=2,r=10,a=14`** (second shape): F1 `T=206/37` with `T_rand=195/26` vs null `195.99/29.93` (`:424,461`); F2 `T=506/369` with `T_sym=326/329` and `T_rand=169/29` vs null `195.99/29.93` (`:499,536`).

**Answers.**

- **Anchor 1's `T = 98` and `T = 95` are now decomposed**: `98 = 9 + 84 + 5`, `95 = 9 + 84 + 2`. The `84 = C(m-1, r/2-1) = C(9,3)` is exactly its even-locator count, now separated from the residue by construction rather than by inference.
- **`T_rand` on GENERIC pencils is Poisson-null-compatible.** At 10/10 far rows `T_rand` lies inside the registered envelope `null + 3 sqrt(null) + 3`; at 6/10 it is within a factor 2 of the null; it goes to **0** at both large fields for LB1 and for the non-negation-closed control. **A-8 HIT.** This is the evidence base the fence would need.
- **But the null is a MEAN and `B_ca^far` is a MAX** (MISS-2 guard clause 6). The same functional on **engineered** pencils returns `T_rand = 8` against a null of `0.126` (`g3_results.txt:12`) and `T_rand = 6` against a null of `1.3e-4` (`g5_results.txt:17`). **A clean null at generic pencils is not a fence.**
- **A third structured `T_rand` family EXISTS, and there are two of them.** (i) *Accidental/arithmetic*: exactly one field-size-independent minimal-spend slope at 3 of 4 negation-closed `rho=2` cells (`gamma = -1/4`, `-37/28`, `-3/16`; `g2_results.txt:11,22,33`), each verified by the direct pencil test at two fields (`:12-13,23-24,34-35`), **0 at all three controls** (`:50,58,66`) and **0 at every `rho = 3,4` cell** (`:74,82,90,98,106`). Zero power for razor transport (ZP-13). (ii) *Constructed*: see D3. **B-1 HIT.**
- **Spend histograms.** The accidental `T_rand` population spreads over `t = 2..8` in a null-like way (`:50,87,124`); the structured populations concentrate at `t = rho` exactly. **A-9: HIT for the accidental part, MISS for the structured part.**

---

## D3 — THE FENCE ATTEMPT AND THE TWO SECONDARIES

### D3.1 (a) The fence attempt — and why it becomes a counterexample

**What lands unconditionally: FENCE-1** (D1.1). It is a genuine partial fence in the brief's sense — *`T_rand = 0` for every slope outside the named exceptional set `{S : |S u W| >= R+1}`* — proof-shaped (two lines from MDS distance), 297/297 measured. **B-2' HIT.**

**What does NOT land: the full fence.** I attempted the natural conditional fence *"if for every `(k-1)`-subset `Y` disjoint from `W` the image `chi_Y(W)` has no `rho+1` collinear points then `T_rand^{min} = 0`"*. The hypothesis is exactly right — and it is **FALSE**, because the adversary chooses `(e_0,e_1)`, hence chooses the collinearity.

**THE CONSTRUCTION.** Fix `j` configurations `(P_i, A_i, gamma_i)` with `P_i subset D\W`, `|P_i| = rho`, `A_i subset W`, `|A_i| = rho+1`, `Y_i = (D\W)\P_i`, and solve the **linear** system

```
   lambda_i Z_{Y_i}(x) + e_0(x) + gamma_i e_1(x) = 0    for all x in A_i , i = 1..j
   unknowns  : e_0,e_1 on W  (2(r+1))  +  lambda_1..lambda_j
   equations : j(rho+1)
   kernel    >= 2(r+1) - j*rho          =>  j <= (2(r+1)-1)/rho .
```

Then keep any kernel vector with `lambda_i != 0`, `chi` injective on `W`, and `gamma_i` not a fibre slope, build `(y_0,y_1)`, and census.

| domain | `n` | `rho` | `r` | cap `(2(r+1)-1)/rho` | max `j` attained | census | ref |
|---|---|---|---|---|---|---|---|
| `{+-1..+-10}` | 20 | 2 | 8 | 8.50 | **8** | `T = 9+j` at `j=1,2,4,6,8`, column-FAR, null `0.126` | `g3:8-15` |
| `{+-1..+-12}` | 24 | 2 | 10 | 10.50 | **10** | verified slopes only | `g3:21-27` |
| `{+-1..+-13}` | 26 | 3 | 10 | 7.00 | 6 | — | `g3:33-39` |
| `{+-1..+-17}` | 34 | 4 | 13 | 6.75 | **5** | — | `g3:45-51`, `g4:101-103` |
| **`mu_20 < F_500041`** | 20 | 2 | 8 | 8.50 | **8** | **`T = 9+j` at `j=1,2,4,6,8`, T_fib=9, T_sym=0, column-FAR, null `0.2519`** | `g3:57-63` |
| **`mu_20 < F_900001`** | 20 | 2 | 8 | 8.50 | **8** | third field | `g4:115-117` |
| **`mu_26 < F_500111`** | 26 | 3 | 10 | 7.00 | 6 | — | `g3:69-74` |
| **`mu_26 < F_200201`** | 26 | 3 | 10 | 7.00 | **6** | **FULL CENSUS `C(26,10)=5,311,735`: `T=17`, `T_fib=11=r+1`, `T_rand=6`, excess `+6`, 6/6 engineered present, column-FAR, null `1.325e-4`** | `g5:16-17` |
| **`mu_34 < F_500107`** | 34 | 4 | 13 | 6.75 | **6** | — | `g4:108-110` |

**`T = (r+1) + j` EXACTLY, at every census row, on both domain types, at three fields.** **B-10 HIT, B-11 HIT.**

> **STATEMENT U IS FALSE.** There are column-far, razor-faithful pencils, on the razor's own domain type, with bad slopes admitting **no** locator inside `W`. The banked implication "`U => B_ca^far(k+2^34) = r+1` EXACTLY" (`crossing_location:4483-4485`) has a false antecedent.

**The pricing that replaces the fence.** The exchange rate is `rho` conditions per U-rand slope, spend-independent (D1.1), so

```
T  <=~  (r+1)  +  (2(r+1)-1)/rho          [f = 1]
```

and optimising over `f` (`T_fib <= r/f+1`, budget `2(r+f)`) keeps `f = 1` optimal: `T <= 2^39.977280 / 2^38.977280 / 2^37.977280 / 2^22.977 / 2^7.577` at `f = 1,2,4,2^17,2^34` (`g5_results.txt:30-34`). **At the razor:**

```
(2(r+1)-1)/rho = 126.0000000001  ->  j <= 126      (kernel dim exactly 2 at j = 126;
2(r+1)/(rho-1) = 126.0000000075       2r/rho = 126   negative at j = 127)
B_ca^far(k+2^34)  >=  r+1 + 126 = 1,082,331,758,719 = 2^39.977280
```

(`g5_results.txt:23-26`). **A-2 HIT on all three forms.** The prize question is untouched: `(r+1+126)/2^39 = 1.968750000 = 2^0.977279924` (`g5_results.txt:36`), against `(r+1)/2^39 = 2^0.977280`.

### D3.2 (b) The `rho = 3` symmetric-`T` cell — ANCHOR 1's PREDICTION IS REFUTED

On a negation-closed `D` with `n` even, `v_{-x} = -v_x`; with `T = -T` and `e_1 = x^2 e_0` the error is even, so **`y_m = 0` for every even `m`** — verified True at 10/10 cells (`g4_results.txt:7,17,26,35,44,53,62,71,80,90`). Row `i` of the pencil then couples only `sigma_j` with `i+j` odd, and **rows `2s` and `2s+1` carry the SAME vector `Z^(s) = (y_{2s+1}, y_{2s+3}, ...)`**, acting on `sigma^o` and `sigma^e` respectively. On the carrier `sigma = (X-x_0)P(X^2)` (root set `(A u -A) u {x_0}`, degree exactly `r`) one has `sigma^o = p`, `sigma^e = -x_0 p`, so both blocks collapse to the same conditions on `p`:

```
independent conditions = ceil(rho/2)   ->   over-determination on gamma = ceil(rho/2) - 1.
```

**NOT `floor(rho/2)`.** Anchor 1's derivation (`crossing_location:4472,4487`) predicts survival at `rho = 3`; mine predicts death. The measurement:

| cell | domain | `rho` | `r` | `#A` | carrier slopes | fibre slopes | **excess** | ref |
|---|---|---|---|---|---|---|---|---|
| `n=22` | `{+-1..+-11}` | 2 | 9 | `C(11,4)=330` | 323 (both `q`) | 5 | **318** | `g4:9,19`; `g5:13` |
| `n=26` | `{+-1..+-13}` | 2 | 11 | `C(13,5)=1287` | 1264 / 1276 | 6 | **~1270** | `g4:28,37` |
| `mu_22 < F_300191` | subgroup | 2 | 9 | 330 | **330** | 5 | **325** | `g4:82` |
| `n=28` | `{+-1..+-14}` | **3** | 11 | `C(14,5)=2002` | **6** | **6** | **0** | `g4:46,55`; `g5:5,7` |
| `mu_28 < F_300301` | subgroup | **3** | 11 | 2002 | **6** | 6 | **0** | `g4:92` |
| `n=34` | `{+-1..+-17}` | **4** | 13 | `C(17,6)=12376` | **7** | **7** | **0** | `g4:64,73`; `g5:9,11` |

At `rho = 3` and `rho = 4`, **`carrier subset fibre: True` AND `fibre subset carrier: True`, EXCESS = 0**, at 2 fields x 2 shapes (`g5_results.txt:5,7,9,11`). At `rho = 2` the same test gives `carrier subset fibre: False`, excess `318` (`:13`).

> **The symmetric-`T` mechanism is DEAD at `rho >= 3`. Anchor 1's parity prediction (survival at `rho = 3`) is REFUTED; its death prediction at `rho >= 4` is confirmed but for the wrong reason. The correct count is `ceil(rho/2)`, and the `M >= rho` threshold in the banked dichotomy should read `M >= 2rho-1` for this carrier (`ceil(rho/M) = 1` is the wrong normalisation when the two parity blocks fuse).**

**Bonus — anchor 1's `T = 336` decomposed exactly.** `g4_results.txt:12`: full census `C(22,9) = 497,420` at `q = 65537` gives `T = 336`, `T_fib = 5`, carrier explains `323`, residual `8` against a null of `7.59`. On `mu_22` the carrier explains `330/330`, residual `0`, null `1.657` (`g4_results.txt:85`).

### D3.3 (c) The `C(128,63)` correspondence — identified, and the verdict is NO

Both objects live on the same index set (the `128` cosets of `mu_{2^34}` in `D`) at the same scale `M = rho = 2^34`, and they are **different subset-counts**:

```
banked qcore plateau  = C(n/M - 1, k/M) = C(127,64)  = 2^123.171434   (CODEWORDS: P_A = L_T0(X^k - L_A),
                                                                       ww_lower_witnesses, sigma = M-1)
T_sym carrier at M=rho = C(n/rho, r/rho) = C(128,63) = 2^124.149066   (LOCATORS: r/rho = 63 of 128 orbits)
```

Exact integer facts (`g5_results.txt:38-42`): `C(127,63) = C(127,64)` (True); `C(128,63)*65 = C(127,64)*128` (True, so the ratio is exactly `128/65 = 1.9692307692`); `C(128,63) - C(127,64) = C(127,62)` (True).

**Verdict — the cap does NOT transport (B-4 MISS as registered).** The banked cap is a **supply** cap on a *construction class* (char-0 coset/dressing/perturbation witnesses, `rate_half_band_closure/node.json:9`), proved by Lam–Leung plus nesting. `T_sym` needs an **upper bound on how many orbit-invariant locators are bad slopes**, which the carrier size does not supply and the plateau cap does not address. Two different quantifiers on two different objects.

**What DOES transport, and it is worth banking.** The Lam–Leung **nesting/dedup** ("order-`2M` cosets ARE pairs of order-`M` cosets, so multi-scale families dedup to `C(127,64)` ALONE; any sum-over-scales double-counts"). Applied to `T_sym`: **the orbit-invariant locator families at different scales `M | n` do NOT add — summing `C(n/M, r/M)` over `M` double-counts.** Consequence: the `M`-threshold cannot be evaded by aggregating scales, which is precisely the loophole a `T_sym` upper-bound campaign would otherwise have to close. `T_sym` inherits a proved **dedup**, not a proved **cap**.

**Numerology fence, registered in advance and confirmed:** `log2(128/65) = 0.977632` is **not** `log2((r+1)/2^39) = 0.977280` (`g5_results.txt:43`, `EQUAL? False`). Two different `0.977`s. (My blind value `0.977488` was wrong — miss 1.)

---

## D4 — VERDICT AND THE FAR-CA RESIDUAL MAP

### D4.1 Verdict

**U-RAND: PRICED, AND THE PRICE REFUTES U.** What is resolved:

- **Statement U is FALSE** (D3.1), constructively, on `mu_n`, with exhaustive census at `rho = 2` and `rho = 3`.
- **The far-CA count is `r+1 + Theta(n/rho)`, not `r+1`.** Lower: construction, `+126` at the razor, modulo one genericity lemma. Upper: parameter count, heuristic, same `126`.
- **U-sym is dead at `rho >= 3`**, now measured, not derived — and anchor 1's derivation of *why* is wrong (D3.2).
- **FENCE-1 is the surviving fence**, unconditional and exact: no near-`W` slope is codeword-mediated.
- **The first moment remains at zero power in both directions**: it is right about generic pencils (10/10 rows inside the envelope) and wrong by a factor `4.5e4` about the engineered one at `rho = 3`.
- **The `C(128,63)` check is done**: cap no, dedup yes.

`B_ca^far(k+2^34) < 2^128`: **NO.**

### D4.2 The far-CA residual map after this round

- **R-U — REFUTED as posed. Retire it.** Replace with **R-URATE**: *is the exchange rate `rho` conditions per codeword-mediated slope tight?* i.e. prove `T_rand <= 2(r+1)/rho` (or find a cheaper mechanism). The whole far-CA count now hinges on this single number, and it is a clean, self-contained linear-algebra question about the rank of the `j(rho+1) x (2(r+1)+j)` incidence matrix.
- **R-USYM — CLOSE IT.** Dead at `rho >= 3` on the named carrier, two fields, two shapes, two domain types. What remains is only the carrier-exhaustiveness question (ZP-4): is `(X-x_0)P(X^2)` the *only* parity-collapsing carrier at odd `r`?
- **R-GENERICITY (new, and it is the whole gap between a heuristic and a theorem).** Prove that at razor parameters the construction's matrix has full rank `j(rho+1)` and that a kernel vector exists with `lambda_i != 0`, `chi` injective, `gamma_i` off the fibre, column-far. Each is an open condition; each held at 60/60 draws at every reachable cell. **This converts `B_ca^far(k+2^34) >= r+1+126` from constructive-modulo-genericity to unconditional.**
- **R-HRLOW, R-PSTAR-INTERMEDIATE** — remain retired (round 36). **R-FG-RAZOR** — unchanged, still downgraded. **R-KER, R-DEEP, R-LINEDEGREE** — unchanged.

### D4.3 FLAGS FOR THE COORDINATOR (AUDIT-AND-DRAFT — no surgery applied)

1. **`crossing_location:4482-4488` — STATEMENT U MUST BE MARKED REFUTED, AND THE PIN WITHDRAWN.** "U implies `B_ca^far(k+2^34) = r+1 = 2^39.977280` EXACTLY" now has a false antecedent. Suggested repair: keep U as a *definition* of the fibre-only stratum, mark it FALSE as a theorem, and replace the pin with "`B_ca^far(k+2^34) = r+1 + Theta(n/rho)`; constructive floor `r+1+126` modulo genericity; heuristic cap `r+1+126`." **I flag; I do not apply.**
2. **`crossing_location:4472,4487` — the `floor(rho/2)` parity derivation is WRONG; the count is `ceil(rho/2)`.** Consequence: the symmetric-`T` mechanism dies at `rho = 3`, not `rho = 4`. Evidence: `g5_results.txt:5,7,9,11` (excess 0, both inclusions True, 2 fields x 2 shapes x 2 domain types) against `g5_results.txt:13` (excess 318 at `rho = 2`). The razor conclusion is unaffected (it gains `2^33` conditions of slack); the *statement* is wrong.
3. **`crossing_location:4479-4480` — "`T_sym` needs an automorphism of order `>= rho`; `T_rand` is moment-priced (zero power)" — the second clause is now false and the first is mis-normalised.** `T_rand` has a mechanism that needs no automorphism at all, and the `M`-threshold for the fused-parity carrier is `M >= 2rho-1`, not `M >= rho`.
4. **`crossing_location:4427,4493-4494` — the `C(128,63)` CHECK IS DONE.** Suggested one-liner: "identified: `C(128,63)` counts orbit-invariant LOCATORS, `C(127,64)` counts qcore CODEWORDS; ratio exactly `128/65`; the Lam–Leung+nesting **cap does not transport**, the **dedup does** (multi-scale `T_sym` families collapse to one scale). `log2(128/65) = 0.977632 != 0.977280`."
5. **The banked "minimum-distance spend" deserves a far-CA pointer.** `rate_half_type2_fr_two_type1_fibre_spend_calibration/statement.md:48` names it as the baseline it improves on, inside the FR/type-2 lane that is vacuous on the bracket. At razor shape with the forced `|W| = r+1` it is **not** vacuous: it gives `t >= rho`, and it is the only unconditional fence in the far-CA lane. One cross-reference sentence would stop a future round re-deriving it (as I did).
6. **`counting_frame/statement.md:9` / `v8_ledger/statement.md:9` are the right home for the `V_S` geometric restatement** ("one support pays for at most one slope" = "column-far means no `V_S` contains the syndrome line"). Optional, cosmetic.

### D4.4 Cross-pilot flag (I did NOT read any sibling)

For whoever holds the counting-frame / v8-ledger / upper-bound lanes: **the far-CA bad-slope count is a coset-leader problem for an MDS code, and the adversary's currency is `2(r+1)` field elements at `rho` per slope.** Any far-CA upper-bound argument that prices only the *fibre* stratum is bounded below by `r+1` and is therefore off by an additive `Theta(n/rho)`, which is `126` at the razor and `Theta(n)` at small `rho`. Two consequences: (i) *`T <= r+1` is unprovable at razor shape* — do not spend on it; (ii) the right target is the **rank of the engineering matrix**, `j(rho+1) x (2(r+1)+j)`, which is a finite, self-contained linear-algebra question and the only thing standing between a heuristic and `B_ca^far(k+2^34) = r+1 + Theta(n/rho)` as a theorem. Also: the adversarial-dimension-count methodology is already banked in the xr/F5 lane (`xr_smallcore_spread_count/node.json:9`, F5-A2, "saturates at `Theta(n)` ... the dimension argument is a proof lead for the floor") — **the same method now fires in far-CA, and it fires as a counterexample rather than a floor.**

---

## PREDICTIONS vs OUTCOMES

| id | registered | outcome |
|---|---|---|
| B-1 | `T_rand` carries a structured mechanism, P = 0.30 | **HIT, twice.** An accidental integer family (`g2:11,22,33`) and a CONSTRUCTED one (`g3`, `g5:17`) |
| B-2 | full fence (`T_rand = 0` provably), P = 0.10 | **MISS — correctly priced low, and REFUTED rather than merely unproved** |
| B-2' | partial proof-shaped fence, P = 0.80 | **HIT — FENCE-1**, 297/297 |
| B-3 | `rho = 3` symmetric-`T` SURVIVES, P = 0.62 | **MISS — it dies.** Excess 0, both inclusions True, `g5:5,7` |
| B-3' | dies at `rho = 4`, P = 0.78 | **HIT** (`g5:9,11`) — but for the `ceil` reason, not the `floor` reason |
| B-4 | the `C(128,63)` cap transports, P = 0.25 | **MISS — correctly priced low.** Cap no, dedup yes |
| B-5 | U's status improves to one-mode-open-with-evidence, P = 0.70 | **HIT AND SUPERSEDED** — U is not one-mode-open, it is FALSE |
| B-6 | FENCE-1 at 100%, P = 0.93 | **HIT — 297/297**, zero MDS violations |
| B-7 | minimal-spend rigidity at 100%, P = 0.72 | **HIT — 18/18**, and `W subset supp(c)` at 297/297 (stronger) |
| B-8 | `T_rand` null-compatible at C1, P = 0.60 | **HIT — 10/10 rows inside the envelope**, and 6/10 within a factor 2 |
| B-9 | spend concentrates at `t = rho`, P = 0.40 | **SPLIT — MISS for the accidental population** (null-like spread), **HIT for the structured** (all at `t = rho`) |
| B-10 | I can construct a U-rand slope, P = 0.75 | **HIT**, 7 cells, 2 domain types |
| B-11 | it stacks to `j >= 3`, P = 0.45 | **HIT far beyond** — `j = 10` at `intZ n=24`, `j = 8` at `mu_20` at 2 fields |
| B-12 | `B_ca^far < 2^128` moves, P = 0.03 | **HIT — it did not** |
| B-13 | >= 1 banked statement needs correction, P = 0.75 | **HIT — four** (flags 1-4) |
| B-14 | >= 1 of my own predictions refuted by my own runs, P = 0.70 | **HIT — three** (B-3, R2j, A-5) |
| A-1 | `C(127,64)=C(127,63)`; ratio `128/65`; `log2 C(127,64)=123.1714`; `log2 C(128,63)=124.1489`; `log2(128/65)=0.977488`; NOT equal to `0.977280` | **5/6 HIT** (`123.171434`, `124.149066`, ratio exact, `C(127,63)=C(127,64)`, `EQUAL? False`). **1 MISS: `log2(128/65) = 0.977632`, not `0.977488`** (miss 1) |
| A-2 | `r+1 = 1,082,331,758,593 = 2^39.977280`; `2(r+1)/(rho-1) = 126.0000000075` floor 126; `2r/rho = 126`; `n/rho=128`, `r/rho=63` | **HIT, all five exactly** (`g5:21-24`) |
| A-3 | C1 `mu_1` = 12.349, 1.0342, 0.12373, 0.0012579, 2.9329e-05, 1.2597e-07 | **HIT 6/6 exactly** (`g1:9,47,84,121,141,147`) |
| A-4 | C1/F1 at `q >= 65537`: `T = T_fib = 9`, `T_sym = T_rand = 0` | **HIT at both fields** (`g1:142,148`) |
| A-5 | C1/F2: `T_fib=9`, `T_sym=84=C(9,3)`, `T_rand <= 4`, `T in {93..98}` | **PARTIAL: `T_fib`/`T_sym`/`T` all HIT** (`98`, `95`); **`T_rand <= 4` MISS at `q=65537`** (`=5`) |
| A-6 | FENCE-1 at 100% of codeword-mediated incidences | **HIT — 297/297**, 2 shapes, 2 domain types |
| A-7 | minimal-spend `wt(c) = R+1` and `W subset supp(c)` | **HIT 18/18**, 2 shapes, 6 fields |
| A-8 (semi-blind) | `T_rand` inside `null + 3sqrt(null) + 3` at >= 4 rows | **HIT at 10/10 far rows** — for GENERIC pencils only; blown by `64x` and `4.5e4x` on engineered ones (reported as the MISS-2 point, not as a failure) |
| A-9 (semi-blind) | `t`-histogram of `T_rand` indistinguishable from null | **SPLIT** — see B-9 |
| A-10 | `T_sym(rho=3) > 0`, `T_sym(rho=4) = 0`, 2 fields each | **MISS on the first half** (`rho=3` excess is 0), **HIT on the second** |
| A-11 | K1 control: `T_sym = 0`, `T <= 12` at `q >= 65537` | **HIT** — `T = 10` and `T = 9`, `T_sym = 0` (`g1:386,394`) |
| MISS-2 guard | max-not-mean; emptiness never promoted; codim != emptiness; moment zero power both ways; four functionals never equated; averaging over pencils forbidden as evidence | **HELD, and clause 6 did the work.** Every `T`/`T_fib`/`T_sym`/`T_rand` is an exact exhaustive count; the null is used only as a descriptor and is explicitly shown failing by `4.5e4` on the object that matters; the `rho-1` codimension is never promoted to emptiness — indeed the construction shows a codim-`(rho-1)` locus is NON-empty; and no union-bound-over-pencils statement appears anywhere |

---

## ZERO-POWER DECLARATIONS

1. **ZP-1 (registered, no widening).** No razor-scale computation exists. All machine numbers at `q <= 999983` (as registered — no widening was needed or taken), `R <= 17`, `rho <= 4`, `r <= 13`. Every razor number is a closed-form evaluation.
2. **ZP-2 (registered).** Zero power from any non-faithful cell. Every row prints `4rho<R`, `a>R+1`, `a-1>r`; all True at every row used. The one column-close row (`g1:9`) is excluded by the script itself.
3. **ZP-3 (registered).** The first-moment / Poisson model has zero power in both directions. It is right about generic pencils and wrong by `4.5e4` about the engineered one (`g5:17`). No `E[T]` supports any verdict.
4. **ZP-4 (registered).** **Exhaustive total-`T` censuses exist only at `C(20,8)`, `C(22,9)`, `C(24,10)` and `C(26,10)`.** The `rho = 4` construction is verified slope-by-slope (`g4:108-110`) but its **column-farness and total `T` are UNMEASURED**. The `rho = 3,4` symmetric-`T` evidence is a complete sweep of a NAMED carrier plus the exact fibre comparison — **not** a total count. "There is no `T_sym` at `rho = 3`" is NOT supported; "there is none on the `(X-x_0)P(X^2)` carrier" is.
5. **ZP-5 (registered).** The parameter cap cannot be tested at razor scale. Its small-cell values (`8.5/10.5/7.0/6.75`) are attained at 4/7 cells and missed by one at 3/7 (search-limited, miss 3). **Zero power on the razor value `126` as a bound.**
6. **ZP-6 (registered).** **Codimension/dimension counting is not a proof.** The `rho-1` law and the `2(r+1)/rho` cap price `T_rand`; they do not bound it. The construction is the *other* direction and is real, but see ZP-7.
7. **ZP-7 (new, and the round's main gap).** **The construction's transport to razor parameters is NOT proved.** The dimension count is exact there (kernel `>= 2` at `j = 126`, negative at `j = 127`); the full-rank and genericity side-conditions are not. I state `B_ca^far(k+2^34) >= r+1+126` as **constructive-modulo-genericity**, never as proved.
8. **ZP-8 (registered scope fence).** The type-2 ledger `(C2)/(C3)/(C4)` was **not imported**; it is vacuous by sign on the bracket. Every bound here derives from MDS distance, pigeonhole, or degree counting in this document. `q_crit`, `theta_1 = 127.977457`, `theta_2 = 63.988728` are razor-row constants and were not used as row-level constants.
9. **ZP-9 (registered).** Every structural claim carries >= 2 fields. Two-field confirmations: FENCE-1 (14 rows), minimal-spend rigidity (6 fields), the `rho=3/4` symmetric-`T` death (2 fields x 2 shapes x 2 domains), the construction (3 fields on `mu_20`), the integer-collinear hits (pencil test at 2 fields each).
10. **ZP-10 (registered).** No sibling round-37 directory was read; no `ls` of the parent was run.
11. **ZP-11 (registered).** `T_sym` classification tested **only** the automorphism `x -> -x`. A codeword-mediated slope carried by a different automorphism of `D` would be counted in `T_rand`. Declared in advance; the construction's `T_sym = 0` rows should be read with this caveat (though the construction needs no automorphism at all).
12. **ZP-12 (registered).** Both `C(128,63)` and `C(127,64)` were computed as exact integers and both objects identified from banked text (`ww_lower_witnesses/node.json:7` for the qcore witnesses, `rate_half_band_closure/node.json:9` for the cap). Where the banked definition was not verbatim recoverable in a bounded window I say "different object", not "not the same theorem".
13. **ZP-13 (new).** **The integer-collinear minimal-spend family has ZERO POWER for the razor.** It is a property of integer arithmetic on `D = {+-1..+-m}`; the razor's `D` is a multiplicative subgroup of `F_q^*` where the notion does not exist. Three hits, `n = 1` per cell. Reported as a phenomenon, used for no conclusion.
14. **ZP-14 (new).** Zero power over `char F_q` and over non-prime `q`: every field used is an odd prime. Frobenius/subfield mechanisms for `c` are **declared unmeasured**.
15. **ZP-15 (new).** The `mu_n` cells use `q ~ 2e5..9e5` with `n | q-1`. I claim zero power over the *arithmetic* of the razor's subgroup (`n = 2^41`, 2-power order, `q > 2^128`); what the `mu_n` cells establish is that the construction does not depend on the domain being a set of small integers.

---

## MEASURED FUNCTIONALS

Registered and measured: the exact total bad-slope count `T` by exhaustive sweep of all `C(n,r)` split locators, with the four-way split `T_fib`/`T_sym`/`T_rand` and the per-slope minimum spend `t = |S\W|`, at 14 (cell, field) rows across C1, C2, K1, `mu_20`, `mu_22`, `mu_26` and the 4 constructed families; column-farness by the same sweep (common-locator count) at every row; `mu_1 = C(n,r)/q^rho`, `q*mu_1`, and the incidence null `C(n,r) q^{1-rho}`; the mediating codeword `c = u - h_gamma` recovered by solving `syn(u) = y_0+gamma y_1` on `S` (Gaussian elimination) at 297 incidences, with `wt(c)`, `|supp(c) n W|`, the verification `syn(c) = 0`, the MDS test `wt(c) >= R+1`, and the minimum-weight test `wt(c) = R+1`; the spend histogram over non-fibre slopes at every row; the exact integer-collinearity census of the minimal-spend carrier (`#Y * C(|W|,rho+1)` configurations, `4620` to `9,699,690`) over **Z** with exact rational `(lambda, gamma)` extraction, plus the independent direct pencil test `(M_0+gamma M_1)sigma = 0` at two fields per hit; the engineering kernel `2(r+1)+j - j(rho+1)` with the four genericity side-conditions and slope-by-slope verification; the symmetric-`T` parity structure `y_m = 0` for even `m` at 10 cells; the `(X-x_0)P(X^2)` carrier sweep (`4620` to `272,272` locators per cell) with the `x_0`-independence test and the exact fibre-slope comparison `{-1/t^2 : t in T}`; and the razor closed forms `r+1`, `log2(r+1)`, `n/rho`, `r/rho`, `k/rho`, `(2(r+1)-1)/rho`, `2(r+1)/(rho-1)`, `2r/rho`, `rho-1`, `ceil(rho/2)-1`, the `f`-optimisation `r/f+1+(2(r+f)-1)/rho` at five `f`, `C(128,63)`, `C(127,64)`, `C(127,63)`, `C(127,62)`, the ratio identity, `log2 C(n,r)`, and `log2 mu_1` at `q = 2^128, 2^167, 2^256`.

Independent cross-checks against the anchors that came out **exact**: C1's six `mu_1` values; `T = 98` at `q=65537` and `T = 95` at `q=999983` for the `d=2` family; `T_sym = 84 = C(9,3)`; `T = 336` at H2; `T_1 = r+1 = 9` for LB1; `T_1 = (r+1)/2` for the symmetric-`T` family; `r+1 = 1,082,331,758,593 = 2^39.977280`; `log2 C(n,r) = 2,198,635,969,270.39`; `log2 mu_1 = -3.872863e8 / -6.704022e11 / -2.199411e12`; `C(127,64) = 2^123.171434` against the banked `2^123.1714`.

Registered but **not** measured: char-2 and non-prime `q` (ZP-14); the `rho = 4` constructed pencil's total `T` and column-farness (ZP-4); any razor-scale quantity (ZP-1); automorphisms of `D` other than `x -> -x` (ZP-11). All four were declared in advance or are declared here; none is silently absent.

---

## COMPLIANCE

`CONSTRAINTS.md` read first, `PREREG.md` second, then the **two named anchors only** (`notes/pilots_20260811/r36_hrlow/REPORT.md`, `notes/pilots_20260811/r35_fg_razor/REPORT.md`) — and **nothing else**: no grep, no `ls`, no interpreter invocation, no third read — before the `## Pilot registrations` block (R1 dictionary + faithfulness-gated cell table, R2a-R2j falsifiable derivations, R3's seven brief-mandated priors + eight supporting priors + eleven A-predictions, R4's six-clause MISS-2 guard, R5's twelve zero-power pre-declarations, R6 deliverable registrations with falsifiers F-1/F-2/F-3, R7 compute plan) was appended to `PREREG.md` with the **Edit tool**. **No registration was edited afterwards.** The block discloses that every R2 derivation and every razor constant in R3-A was computed **in head** from the anchors before writing, and marks A-8/A-9 **semi-blind**.

**COMPUTE LAW: 5 interpreter invocations, 5 under `tools/ramguard`, ZERO breaches, zero bare `python3` for any purpose** — including patching, probing, no-ops and empty heredocs (every file creation and edit went through the Write/Edit tools). All from the repo root, with a literal `--`, all `local` with an explicit `RAMGUARD_TIMEOUT=290`: (1) `g1_census.py all`; (2) `g2_minspend.py`; (3) `g3_construct.py`; (4) `g4_sym.py`; (5) `g5_close.py`. That is under the `<= 6` I registered; the reserve invocation was not needed and was not used. Stdlib only (`sys`, `math`, `random`, `itertools`, `fractions`). No Modal, no network, no git, no subagents.

**RESULTS-FILE RULES (the new round-36 rules): OBEYED.** Every one of `g1_results.txt`, `g2_results.txt`, `g3_results.txt`, `g4_results.txt`, `g5_results.txt` is opened with `open(path, "a")` — **append mode, never a blind `"w"`** — and flushed after every emit, so a timeout would have preserved partial results. **No results-producing run was piped through `head`**: all five were piped through `tail -n N`, and every file was inspected afterwards with `grep -n` and `sed -n`. Zero SIGPIPE losses; zero runs produced nothing.

**IMPORTED-SCRIPT RULE: NOT TRIGGERED, and deliberately so.** I imported and executed **zero** banked scripts, and there is no `import` of any local module anywhere — every helper (`inv`, `vvals`, `sigma_of`, `slope_of`, `kernel`, `isprime`, `subgroup_ordered`) is **duplicated into each of the five files**, which is the anti-import pattern round 36's close recommended. Had I copied a banked script I would have grepped it for `open(`/`write`/results paths and repointed them with the Edit tool before the first import, as pre-committed in R7. All five scripts are fresh implementations against the anchors' conventions (`v_x = 1/prod_{y!=x}(x-y)`, `y_m = sum_x e(x)v_x x^m`, `M_r(y) = (y_{i+j})`, low-to-high order, split locators of degree exactly `r`, (HS1)/(HS3)), validated against ten published anchor numbers listed under MEASURED FUNCTIONALS.

**WRITE DISCIPLINE:** every file creation and edit via the Write/Edit tools. No `sed -i`, no `awk -i`, no `perl -i`, no `tee`, no shell redirection of any kind onto any file. Read-only shell (`grep`, `sed -n`, `tail`, `echo`) for inspection only. **One disclosed convenience:** a single `cd` into my own pilot directory for a read-only multi-file `grep -n` of my own results files.

**RAM DISCIPLINE:** file-at-a-time; **`dag.json` never opened**; `critical/nodes/rate_half_band_crossing_location/statement.md` (4,600+ lines) read only through **four bounded windows** (16, 25, 21, 21 lines at `:4420-4435`, `:4476-4500`, `:4630-4650`, `:686-706`, `:650-666`) plus line-numbered greps; `rate_half_band_closure/statement.md` through one 19-line window; `rate_half_type2_fr_two_type1_fibre_spend_calibration/statement.md` through one 60-line window; `11-h1-s3-addendum.md` through one 31-line window; `rate_half_ca_hankel_split_pencil_equivalence/statement.md` by grep only. Every locator sweep is a streaming DFS carrying `O(r)` retained state per node (the coefficient vector is built incrementally, so `C(26,10) = 5,311,735` never materialises); all results checkpointed in append mode; no run approached the memory ceiling.

**QUARANTINE:** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` never opened at any line. **No round-37 sibling was read, opened, or listed** — `r37_third_solve`, `r37_share3_gap`, `r37_mint_drafts` were taken **by name** from `CONSTRAINTS.md:38-39` and excluded at search level on every recursive grep, together with `pilots_20260802`, `prize-codex-work`, `.git`, `__pycache__` and `--exclude=dag.json`. **I never ran `ls`, `find`, or any listing on the parent directory** — CONSTRAINTS supplied the names, so no listing deviation was needed. No path containing `prize-codex-` was touched. The `r36_*`, `r35_*`, `r34_*`, `rh_*` and earlier pilot dirs are readable under CONSTRAINTS; I read exactly the two anchors in them and my greps surfaced lines from `r35_fg_razor/REPORT.md` and `rh_fr_algebraic/REPORT.md`, both within the permitted set.

**WRITE SCOPE:** every write is inside `notes/pilots_20260811/r37_urand/` — `PREREG.md` (registrations appended), `g1_census.py`, `g1_results.txt`, `g2_minspend.py`, `g2_results.txt`, `g3_construct.py`, `g3_results.txt`, `g4_sym.py`, `g4_results.txt`, `g5_close.py`, `g5_results.txt`. **No `dag/`, `nodes/`, `critical/`, `background/` or `tools/` file was created, edited, or touched**; no git operation of any kind; no scratch file outside the pilot directory; nothing in `/tmp`. **AUDIT-AND-DRAFT respected: no node surgery applied** — the six corrections this round forces (four of them substantive, including the withdrawal of a banked pin) are flagged in D4.3 for the coordinator, not made.
