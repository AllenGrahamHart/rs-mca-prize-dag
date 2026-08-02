# Pilot report: FM3 mechanism (Opus 5 subagent, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable
(HTML entities restored). Coordinator verification and adopted posture:
FABLE_AUDIT.md alongside.

---

# FM3 MECHANISM — lane P-B, 2026-08-02

## HEADLINE

**The named mechanism ("global block + pairwise birthday") is quantitatively FALSE and is replaced.** The real mechanism is a **coordinate-marginal tilt produced by greedy depletion**, and it is reproduced to within 10-35% by a **parameter-free model with no fitted input**. The global block is only the saturated head of that tilt, not the mechanism.

**And the mechanism does not scale.** The controlling statistic is the standardised gap `(K - chi)/sigma`, where `chi = SUM_i p_i^2` is the mean pairwise core of the selected family. Across **all 15 measured shapes it is 0.54-2.83**; at official RowC scale (n = 1024, m = 4, h = 5, q ~ 1.3e11) the same model gives **18.0-20.4**, i.e. `P[core >= K] ~ 2^-83` against `|Gamma| ~ 2^37`, so `|Gamma| . P ~ 2^-46 << 1`. **At official scale Gamma_hi is empty and Gamma_lo = Gamma for every order — the support-keyed collapse is a small-`q/n` phenomenon.** FM3 in any form that concludes "Gamma_lo is small" is therefore **not available at official scale**, and I recommend the lane re-target from partitioning Gamma to bounding |Gamma|.

A second, immediately actionable correction: **the hash null controls are themselves support-keyed orders.** PP4.0 must freeze the **compression class** (lex/colex under any coordinate permutation — greedy coordinate-sequential orders), not "support-keyed", or the freeze admits the RED nulls.

---

## 1. MECHANISM VERDICT — the quantitative decomposition

Null ladder, applied to every banked family (`fm3_mine.py` -> `MINE.json`; ratio observed/model, 1.00 = perfect):

| null | what it models | obs/model, 4 densest n=32 pts | obs/model, all 12 |
|---|---|---|---|
| **N0** uniform A-subsets | nothing | **1.2 - 2157** | 1.2 - 2157 |
| **N1** global block `B` + uniform residual (the *named* mechanism) | block only | **2.34 - 2157** | 1.0 - 2157 |
| **N2** coordinate-marginal-matched max-entropy (conditional Bernoulli, exact overlap DP) | full marginal profile | **0.78 - 0.94** | 0.74 - 2.55 |
| **N3** greedy-depletion chain, **no fitted parameter** | derived from (n,A,q,h) alone | **0.78 - 1.35** | 0.78 - 6.9 |

- **N1 is dead.** At Q9/ORD-LEX the excess over uniform is x1771; the block (|B| = 11 < K = 16) explains a factor 3.08 of it. For **ORD-COLEX, ORD-VALCOLEX, ORD-ERRLEX the block is 0** and N1 explains a factor **1.0** of an excess of x2021, x2157, x1971. The naive-birthday concern in the brief is confirmed and its repair is not the block.
- **N2 is the mechanism.** Knowing only the per-coordinate selection frequencies `p_i` reproduces the entire concentration excess. `E[core] = SUM p_i^2`; measured 14.01 at Q9/LEX against the uniform floor `A^2/n = 10.125` (Cauchy-Schwarz minimum). COLEX has no block but a hard **window** (`p_i = 0` above coordinate 23), which is the same effect through the complement.
- **N3 says where the tilt comes from.** With `nu(i,a) = C(n-i, A-a)/q^h` and inclusion probability `(1-e^{-nu_in})/(1-e^{-nu_in-nu_out})`, the greedy Markov chain reproduces the observed marginal profile coordinate-by-coordinate (L1 error 0.35-0.94 over 32 coordinates at dense points) and the observed `P[core >= K]` to within 0.78-1.35. **Nothing is fitted.**

**Population factorisation** (`fm3_pop.py` -> `POP.json`, complete enumeration of Q1/Q2/Q3/Q7/Q8/Q10/Q11/R1):

`P_sel = P_unif x STRUCT x TILT`

- **The population is essentially unbiased.** Q1: marginals in [0.3737, 0.3758] vs 0.375, `SUM p_i^2 = 2.2500` = `A^2/n` to 4 dp. R1: [0.3318, 0.3349] vs 0.3333, `P_pop[core>=K] = 4.573e-3` vs hypergeometric 4.744e-3 (ratio **0.96**).
- **STRUCT** (pencil algebra, selector-independent) = 0.65 - 3.5 at h = 2,3; **10.8** at F3a (q = 4993); **2.8** at Q11 (m = 4, h = 5) where 41% of the whole population *is* the designed fibre family.
- **TILT** (the selector) = 1.0 - 838. The hash nulls sit at TILT = 0.76 - 1.6, i.e. statistically indistinguishable from the population — a clean control.
- Structure of the realised >=K pairs: the symmetric difference is **flat over the non-block coordinates** (2-6% each, 0% inside the block) and the slope gaps are unstructured (23-55 distinct gaps, near-flat). No hidden pairing to exploit.

**Residual second-order term (honest).** The isolated-vertex formula `(1-P)^{live-1}` under-predicts the measured retention by x2-x50 even when fed the *observed* `P`. The >=K-pair graph is over-dispersed (hubs + isolated vertices). This clustering, not `P`, sets the last factor in |Gamma_lo| and is **not** modelled.

---

## 2. PREDICTION vs MEASUREMENT (pre-registered)

`PREDICTIONS.json` was written and frozen **before** R1/R2/R3 were run (`fm3_predict.py` refuses to overwrite it). Scored by `fm3_score.py` -> `SCORE.json`.

| point | n | q | K | A | \|W_z\| | why chosen |
|---|---|---|---|---|---|---|
| R1 | **24** | 73 | 6 | 8 | 138 | new domain size; density-matched to R2 |
| R2 | 32 | 641 | 8 | 10 | 159 | same shape as Q4/5/6, density-matched to R1 |
| R3 | 32 | 97 | **12** | 14 | **50105** | density *identical* to Q9, different rate |

| claim | verdict | evidence |
|---|---|---|
| C1 retention <= 0.15, all support-keyed | **PASS** | max 0.0309 (R3/COLEX) |
| C2 null retention >= 0.75 at R3 | **PASS** | 1.000, 1.000 |
| C3 `P[core>=K]` inside `[P/2, 2P]` for LEX+COLEX at R2, R3 | **FAIL at R2** | R3 both YES; R2 LEX 0.01172 vs band [0.0025,0.0100], COLEX 0.00861 vs [0.0020,0.0078] — model under-predicts x2.2 at low density, the known bias direction |
| C4 n-degradation: `P(R1,n=24) > 2.P(R2,n=32)` at matched density | **PASS** | 0.0921 vs 0.0117, **ratio 7.86** (model said 18.1) |
| C5 block `\|B\|_100` within +-1 | **PASS 3/3 exactly** | 2/2, 2/2, 8/8 (and `\|B\|_90` 3/3, 3/3, 9/9) |
| C6 density is *not* the controlling variable | **PASS** | R3 `P = 0.0730` vs Q9 `P = 0.0533` at **identical** 50105 witnesses/slope, ratio 1.371 > 1.25 |

`E[core]` predictions were accurate to **<= 1.2%** at all 15 order x point combinations (e.g. 10.209 predicted / 10.252 measured at R3/LEX).

**C4 and C6 together kill the density framing.** Density is not the variable; the greedy block deficit is.

---

## 3. FM3 — the draft

**Definition (compression order).** `<` is a *compression order* if there is a permutation `pi` of `D` and `eps in {in, out}` such that for every non-empty family `F` of A-subsets, `min_< F` is obtained by scanning `pi(1), pi(2), ...` and taking the `eps`-branch whenever it is non-empty. Lex, colex, value-lex, value-colex and reverse-lex are exactly these. **Blake2b-of-the-bitmask is support-keyed but is not a compression order.**

**Definition (greedy profile, block, deficit).** `nu(i,a) = C(n-i, A-a)/q^h`; `pi(i,a) = (1-e^{-nu(i+1,a+1)})/(1-e^{-nu(i+1,a+1)-nu(i+1,a)})`; `p_i` the marginals of the induced chain; `chi = SUM p_i^2`, `sigma^2 = SUM p_i^2(1-p_i^2)`. Saturated block `L* = max{L : C(n-L, A-L) >= q^h.log|Gamma|}`; block deficit `d = K - L*`.

> ### FM3 (CONJECTURE) — compression-selector overlap concentration
>
> Let `(u,v)` be a strip-free, globally generic pencil over `D = mu_n < F_q^*`, `W_z = {S : |S| = A, deg(f_z - L_S) < K}`, `Gamma = {z : W_z != EMPTY}`, `<` a compression order, `S_z = min_< W_z`. Assume
>
> **(H)** *(equidistribution)* for every partial pattern `P` on the coordinates and every `z`,
> `#{S in W_z : S contains P_in, S disjoint P_out} = C(n-|P|, A-|P_in|)/q^h . (1+o(1))` whenever the main term exceeds `(log q)^2`.
>
> Then:
> **(i) profile.** All but `o(|Gamma|)` selected supports contain `{pi(1),...,pi(L*)}`, and the selected coordinate marginals are `p`.
> **(ii) overlap law.** The pairwise-core law of `{S_z}` equals, up to an absolute constant `C_0`, the law of `SUM_i Bern(p_i^2)` conditioned on both draws having size `A`. Write `P* = P[SUM_i Bern(p_i^2) >= K]`.
> **(iii) conclusion.** `|Gamma_lo| <= C_1 |Gamma| exp(-c_1 |Gamma| P*)`; in particular `|Gamma_lo| <= 8n^3` **provided**
> `|Gamma| . P*(n,A,K,q,h) >= c_1^{-1} log(C_1|Gamma|/8n^3)`. **(STAR)**
>
> Measured constants: `C_0 in [0.74, 1.35]` for `|W_z| >= 1700`, `<= 2.6` for `|W_z| >= 300`; `c_1 in [0.1, 1]`.

**Why this shape and not the others.**

- **(a) global block + residual pigeonhole — refuted twice.** Quantitatively (section 1). And structurally: `Gamma_lo` is a constant-weight code with pairwise intersections `<= K-1`, so the packing bound gives `|Gamma_lo| <= C(n-L*, K-L*)/C(A-L*, K-L*)`. At Q9 that is 969 (below 8n^3 = 262144, so it *would* work); at n = 1024 it is `~2^180 >> 8n^3`. The block never reaches `K`: `d = K - L*` is 3-8 at every measured point, and `L*` depends on the density and rate but **not on n**, while `K = rate.n`. So `d` grows linearly in `n` — the withdrawn K-prefix conjecture is not merely false at small scale, it is *asymptotically* false in the direction that matters.
- **(b) density threshold — refuted.** As an "every" statement it fails at the densest points (`Gamma_lo` = 1/97, 11/193, 3/97, never 0). As a *density* statement it fails by construction: C6 (same density, different `P`) and C4 (same density, different `n`, factor 7.9).
- **(c) exchange/swap — does not close.** The algebra is clean: if `S in W_z`, `S' in W_w`, `z != w`, `|S ^ S'| = A - m` (the maximum, L2), then `L_{S^S'} = G.X^{m(a-1)} + r` with `deg r < K` — the core is the root set of a member of a `K`-dimensional affine family. But `<`-minimality is *per slope*: swapping `m` points moves you to a different `W_w` in which the swapped set competes with `|W_w| ~ C(n,A)/q^h` others, and nothing makes it minimal there. The data confirms there is nothing to harvest: N3 already assumes the two selections are **independent** given the profile and is accurate to 10-35%, so there is no exchange-induced correlation left over.

**What (H) actually is.** It is an equidistribution statement for elementary symmetric functions of subsets of `mu_n` — Weil/character-sum type, not known. Under (H) everything in FM3 is a computation. **(H) is the whole content of FM3**, and it should be posed as such rather than hidden.

---

## 4. FALSIFIER HUNT — and the one that succeeds

Frozen predictions in `FALSIFY_PRED.json` before running (`fm3_falsify.py`).

| falsifier | design | result |
|---|---|---|
| **F1a/b/c** Q9 parameters, core grown 2->4->6->8, fibres 8->7->6->5 | mechanism says `(g,a,b)` is invisible | **SURVIVED.** `\|B\| = 11` predicted and measured at all three; `E[core]` 14.02 predicted vs 14.01/14.08/13.90; `Gamma_lo` = 1, 0, 0 of 97 (Q9: 1) |
| **F2a/b** Q4 parameters, `(g,a,b)` = (4,3,12), (6,2,10) | same | **SURVIVED.** `\|B\| = 5` predicted/measured; `Gamma_lo` = 0, 0 of 97 |
| **F3a** n=32, q=4993, `q/n = 156` (banked grid: 3-14) | the prior pilot's biggest flagged gap | **SURVIVED but reframes the claim.** `Gamma_lo` = 25/4280 under LEX — **but also 40/4280 and 45/4280 under the hash nulls and 29/4280 under POLYLEX.** TILT = 1.5. At large `q/n` the low retention is not a selector effect at all: it is `live.P` ~ 11 with `P` set by the *population*. |
| **N-scaling (R1 vs R2)** | matched density, n 24->32 | **THE FALSIFIER THAT SUCCEEDS.** `P` drops x7.9 for an 8-coordinate step. Extrapolated by the same validated model: rate 1/4 at matched density gives `P` = 6.0e-3 (n=40), 6.5e-5 (n=64), 4.9e-10 (n=128), 3.3e-80 (n=1024). |

**The successful falsifier, stated exactly.** The quantity in (STAR) is `|Gamma|.P*`. It is **3.5-11.4 at every one of the 21 measured points** — remarkably invariant across `q in [17, 4993]`, `n in [16,32]`, `|W_z| in [1.8, 50105]`, `|Gamma| in [17, 4280]`. The model gives, at official RowC 1/4 (`n=1024, K=256, A=261, m=4, h=5, q ~ 1.3e11`): `L* = 229`, `chi = 230.9`, `sigma = 1.23`, `(K-chi)/sigma = 20.4`, `log2 P* = -82.8`, **`log2(|Gamma|.P*) = -45.9`**. RowC 1/2: `(K-chi)/sigma = 18.0`, `log2(|Gamma|.P*) = -40.0`. **(STAR) fails by 40-46 binary orders of magnitude.**

This is corroborated by a **selector-independent, model-free count**: the expected number of >=K-core partners of *any* witness anywhere in the population is
`Pi = SUM_{c=K}^{A-m} C(A,c).C(n-A, A-c)/q^{h-1}`,
which is `2^{-73.5}` at RowC 1/4 with `q = 1.3e11`, and already `2^{-4.4}` at the prior pilot's own "first budget-testable" point (n = 44, rate 1/2, q = 1.33e6). Below 1, **no selector can build a Gamma_hi** — the pairs simply are not in the population. Measured `Pi` against the true population partner count: ratio 0.97-5.3 at h = 2,3 (R1 0.97, Q1 1.13, Q2 1.47, Q3 1.58, Q7 1.94, Q10 1.80, Q8 5.27).

**Verdict on FM3 as a general theorem: dead at official scale.** It is true (conditionally on (H)) in the regime `(K-chi)/sigma = O(1)`, which is exactly the banked grid, and false outside it. A pencil-specific version does not rescue it either: F1/F2 show the pencil shape is invisible to the mechanism, and the *only* structure that produces abundant >=K pairs is the fibre-type sub-population — which is 41% of the population at Q11 (`Pi` under-estimates by x55 there) but `C(104,52)/2^689 ~ 2^{-588}` of it at official scale, and which the selector demonstrably never picks (`intended_is_first_match = 0` wherever there is competition).

---

## 5. CONNECTION CHECK (read-only; nothing modified)

Under the adjudicated R2 semantics (`Gamma_hi = {core >= K}`, P-A1's predicate widened to "shares a core of size **at least** k"), my `Gamma_lo` is computed exactly as `{z : max_{w!=z}|S_z ^ S_w| <= K-1}`, so the draft's conclusion composes with the R2 partition **without modification**. `intersection_stats` in the banked pilot already uses the `>= K` convention.

What it demands of the P-A1 side (`xr_tangent_support_mismatch_bridge/statement.md:24`: *"Assuming the two printed `8n^3` bounds gives `16n^3` for this branch"*):

1. **The partition never compresses.** `|Gamma_hi| + |Gamma_lo| = |Gamma|` identically. At every measured dense point FM3's mechanism routes **96/97, 182/193, 641/641, 4255/4280** slopes into Gamma_hi — i.e. essentially the entire live set lands on P-A1. So the P-A1 obligation FM3 creates is, in practice, `|Gamma| <= 8n^3` — the same bound P-B was trying to avoid proving.
2. **At official scale the routing reverses and vanishes.** `Gamma_hi = EMPTY`, so `|Gamma_lo| = |Gamma|`, and P-B alone must carry `|Gamma| <= 8n^3`.
3. **Either way the binding constraint is `|Gamma| <= 16n^3` — a bound on the number of live slopes.** The R2 partition is a routing device with no compressive content. I recommend the lane re-target from *partitioning* Gamma to *bounding* |Gamma| for split-fibre pencils, and that the adversarial audit's `M = 1.3e11` vs `16n^3 = 1.7e10` be re-examined on that footing. **This is a surfaced finding for coordinator/maintainer adjudication, not a status change.**

Also for PP4.0: **freeze the compression class, not "support-keyed".** `ORD-HASH-pb-null-01/02` key on `mask.to_bytes(8,'little')` — they *are* support-keyed total orders, and they are the RED controls (retention 0.79-1.00). The distinguishing property is greedy coordinate-sequential minimality (lex/colex under any coordinate permutation), which is what all five collapsing orders are and no null is.

---

## 6. FILE INVENTORY

All inside `notes/pilots_20260802/pb_fm3_mechanism/`:

- `fm3_mine.py` -> `MINE.json` — full pairwise-core histograms, per-coordinate marginals, blocks at 100/99/90%, and the four-null ladder (N0 hypergeometric, N1 block+residual, N2 conditional-Bernoulli with exact overlap DP, N3 parameter-free greedy) for all 12 banked cases x 9 orders.
- `fm3_table.py` — renders the four decomposition tables.
- `fm3_scale.py` -> `SCALE.json` — Poisson-binomial vs exact-DP cross-check, n-scaling at rates 1/4 and 1/2, official-scale extrapolation, and the model-free population partner count `Pi`.
- `fm3_predict.py` -> **`PREDICTIONS.json`** (frozen pre-registration; the script refuses to overwrite it).
- `fm3_new.py` -> `sel_R{1,2,3}_*.json`, `k1_R{1,2,3}.json` — the three new points, run through the **imported** banked enumerator/selector (`k1_orders.py`); no logic forked.
- `fm3_score.py` -> `SCORE.json` — prediction scoring, 5/6 registered claims PASS.
- `fm3_falsify.py` -> **`FALSIFY_PRED.json`** (frozen), `k1_F{1a,1b,1c,2a,2b}.json`, `sel_F*_*.json`; `F3A_STATS.json` for the 4280-slope point.
- `fm3_pop.py` -> `POP.json` — complete population enumeration and tilt factorisation for Q1, Q2, Q3, Q7, Q8, Q10, Q11, R1.
- `fm3_summary.py` -> `EVIDENCE.json` — the consolidated 21-point evidence table.

Nothing outside this directory was written or modified; `pb_selector_orders/` and `pb_split_fibre_selector/` were imported read-only. No commits, no pushes, nothing m2-related. Everything ran under `tools/ramguard local --`.

---

## 7. HONEST CAVEATS

1. **The official-scale verdict is a model extrapolation, not a measurement.** The greedy model is parameter-free and validated at 15 shapes (block sizes exact 3/3 pre-registered and +-1 at 12/12 banked; `E[core]` to <= 1.2%; `P[core>=K]` to 0.78-1.35 at `|W_z| >= 1700`), but n = 32 -> 1024 is a 5-doubling extrapolation.
2. **The extrapolation is conservative in the right direction.** At n <= 32 the Poisson-binomial approximation used for large `n` **over**-estimates the exact `P` by x1.0-6.2 (growing with the sigma-gap), so the true official-scale `P` is smaller than quoted and `|Gamma|.P*` is smaller still.
3. **Equidistribution (H) is assumed throughout, and I found one place it fails.** At Q11 (m = 4, h = 5 — the only officially-*shaped* point) the measured population partner count is 10.99 against `Pi = 0.200`, a x55 failure, because 41% of that tiny population is the designed fibre family. That failure mode provably decays (`C(104,52)/2^689 ~ 2^{-588}` at official scale) but it is a real, measured breakdown of (H) and the extrapolation rests on the claim that it is a small-population artifact.
4. **Nothing measured has both the official fibre shape (m = 4, h = 5) and real selector competition.** Q11 has `|W_z| = 1.8` and TILT = 1.03 — no selection effect at all. This is the same gap the prior pilot flagged; I did not close it and it is not closeable at n <= 32 (it needs `C(n,A) >> q^4`).
5. **The clustering term is unmodelled.** `|Gamma_lo|` is set by the over-dispersion of the >=K-pair graph, which the independence formula misses by x2-50. Constant `c_1` in FM3(iii) is fitted from data, not derived.
6. **The `Pi < 1` regime is not directly reachable.** `Pi < 1` with `|W_z| > 1` requires `[C(A,h)C(n-A,h)]^{h/(h-1)} < C(n,A)`, first satisfied with real competition around **n ~ 44-48** — outside the 1G law. The queued native/bit-packed n = 44/48 run should be **re-scoped**: its target is not the budget clause but `Pi`, and the sharp pre-registered prediction is that at n = 44, rate 1/2, q = 1.33e6, `Pi = 2^{-4.4} < 1` and therefore `Gamma_lo = Gamma` **for every order including lex** — a single measurement that would confirm or destroy this report's central claim.
7. **C3 failed at R2**: the model under-predicts `P` by x2.2 at `|W_z| ~ 159`, consistent with the banked low-density bias. The model is an accurate mechanism description above ~1700 witnesses/slope and only an order-of-magnitude one below ~300.
8. **I did not attempt to prove (H) or any part of FM3.** Everything above is measurement plus a validated heuristic model.
