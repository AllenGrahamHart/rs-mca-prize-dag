The harness refused the `REPORT.md` write (subagent policy), so per the brief I return the full report text verbatim below.

**Headline for relay:** **(SAT3) is REALIZABLE** — the vacuity branch is dead. I exhibit, exhaustively at `m=1, q=17` (16 families, all realizing) and at five more fields, a genuine column-far Hankel pencil on the strict `A=3` profile with `T = rho+2`, satisfying (SAT1)–(SAT5) exactly. CATCH-24C is settled: the lanes count the *same* `T` (PROVED via (HS3)), but **LB1 does not transfer** — it lives in the full-column-rank branch. Deliverables (4 scripts + 4 results files) are in `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260811/rh_sat3_realizability/`.

---

# REPORT — rh_sat3_realizability (round 33)

## VERDICT (first)

**(SAT3) IS REALIZABLE. The failure hypothesis is NOT vacuous, the conditional stack does NOT close for free, and the route is CALIBRATED — not vacuously closed.**

I exhibit, at `m = 1` and over **six** fields, an explicit **column-far syndrome Hankel pencil** on the strict `A = 3` profile with

```text
rho = 3, N = 16, R = k = 8, r = rho = 3, A = R+1-2rho = 3,
e = m = 1, s = 0, delta = m-1 = 0, O = 0,
T = 5 = rho+2                                   <-- (SAT3)
```

satisfying **(SAT1)–(SAT5) exactly** (deficit identity `sum_x (m-d_x) = 1 = 1+O`, 15 of 16 columns parameter-saturated). A replayable witness over `F_17`, `D = F_17^*`, `k = 8`, `r = 3`:

```text
y_0 = [16, 1, 2, 12, 12, 7, 10, 6]
y_1 = [14, 10, 2, 14,  0, 10, 12, 1]
supported finite slopes 0, 1, 13, 14, 16 with locator sets
  {8,10,15}, {1,2,5}, {4,6,16}, {3,7,11}, {9,12,13}
```

At `q = 17` the search is **EXHAUSTIVE**: exactly **16** locator families reach `T = rho+2`, and **all 16** carry a non-degenerate column-far Hankel realization at generic rank `rho` (`d1_m1_results.txt`, `d2_realize_results.txt`). It is not a small-field artifact: with the evaluation domain `D` *designed* rather than fixed, a realization appears on the **first** random pencil draw at `q = 1009, 2003, 10007` (`d3_results.txt`), and the explicit Kummer family `Q_Z = X^rho + Z` reproduces it at `q = 67, 73` (`d4_ladder_results.txt`).

Three consequences, in decreasing order of how much they change the plan:

1. **A ROUTE FENCE ON PROOFS (the main deliverable).** The axiom system `(SAT1)–(SAT5)` together with `(SAT3)` has a **model**. Therefore **no `m`-uniform consequence of `(SAT1)–(SAT5)` can ever refute `(SAT3)`**. Every candidate proof of the strict target must use `m >= 2` (or `m >= 3`) explicitly, and my witness is the **regression test** that detects the failure. Round 31's `(NEWCAP)` passes this test — its `Lmin(0) = (N-1)C(m,2)+C(m-1,2)` vanishes at `m = 1`, degenerating to the trivial `w* <= 2rho`, which my witness attains with equality.
2. **The whole counting stack is TIGHT at `m = 1`, simultaneously.** The witness attains `(MI2) = 5`, `(ERC2) = 5`, `(ERC4) = 4e+1 = 5`, and `(AO1) = T1cap + CAP = 2 + 3 = 5` with the measured split `T_1 = 2`, `T_2 = 3` — every inequality in the chain is an equality on a real object. So the residual factor `9/4` is **not** slack that any argument tight at `m = 1` can remove.
3. **The strict target `T <= rho+1` is FALSE at `m = 1`.** This does not contradict any PROVED node — the official corollary's domain is `r <= R/2-2` (`minimal_index_budget/statement.md:59-61`) and my witness sits at `r = R/2-1`, the row that corollary explicitly leaves open (`:82-84`) — but it does show the bound `T <= r+1` **cannot be extended one step** into the strict row.

**CATCH-24C, settled (D1's first obligation).** The two lanes count the **same functional** `T` — this is a PROVED equivalence, not a guess. But **LB1's realizing configuration does not transfer**: LB1 lives in the **full-column-rank branch** (`generic rank = r+1`), which is disjoint from the `A = 3` rank-deficient branch `(SAT)` is about. Details in D1. My registered R2 is therefore a **partial miss**: counts reconcile, configurations do not.

**What did NOT happen.** No T-cap theorem. No `m >= 2` realization of `(SAT3)` (the `e = m` construction is untouched at every `m >= 2`). F1 did **not** fire (`a* = w* = 6 = 7m-1` exactly).

---

## MISSES FIRST

1. **R2 registered at 0.70 is a PARTIAL MISS, and the miss is the interesting part.** I predicted that reconciliation would show LB1 realizing `T = rho+1` inside the `A = 3` stratum, one slope short of the failure size. The *number* is right for a trivial reason (`r = rho` on the strict row, so `r+1 = rho+1` is a numerical coincidence), but the *configuration* is in the wrong branch: LB1's locator sets are the `r+1` subsets of size `r` of an `(r+1)`-set (the petal structure, `rh_farca_upper/REPORT.md:152`), which forces `d_x = r = 4m-1` at every core point — impossible under `d_x <= e = m` for `m >= 1`. LB1's pencil therefore has **generic corank 0**, the branch the node handles separately (`minimal_index_budget/statement.md:62`, "the full-column-rank branch is already proved"). **LB1 contributes nothing to `(SAT3)` realizability**, and my brief's hypothesis that it might is refuted.

2. **P2 registered "P(T = rho+2 realizable) = 0.12" — I was wrong, and I was wrong in the direction that costs the campaign a free win.** It is realizable, and cheaply. I had priced vacuity at `0.08` for the theorem and `0.55` for a T-cap *candidate*; the T-cap candidate I can now pose is strictly weaker than what I registered wanting, because it must be `m`-dependent and can no longer be uniform.

3. **NOTHING IN THIS ROUND TOUCHES `m >= 2`.** The `(SAT1)` profile has `e = m`; every object I constructed at `m >= 2` has `e = 1`, which `(ERC2)` **already closes** (`exceptional_root_charge/statement.md:70-73`: "For every `1<=e<=m-1` … `(ERC2)` gives `T<=rho+1`. Hence this entire parameter-degree range is closed"). So my `m = 2,3,4` ladder entries are **calibration, not progress on the open case**, and I say so rather than letting `T = 4` at `m = 4` read as a measurement of the frontier.

4. **My D1 ladder search had a real bug and its first run published a false negative.** `d4_ladder.py` initially scanned only the *basis vectors* of the realization nullspace, and reported "no non-degenerate realization" at `m = 2,3,4`. Scanning random *combinations* found `T = 4` at every cell, two fields each. The superseded run is not in the results file (it was overwritten by the corrected run), but the bug was mine and the first conclusion I drew from it was wrong.

5. **The dimension ledger (D3) is a NAIVE COUNT and I can name a case where it is blind.** At `m = 1, T = 6` it reports `excess = -11 < 0` ("realizable") although `T*rho = 18 > N*e = 16` makes `T = 6` *impossible* by the hard incidence bound. The ledger silently assumes the hard bound already holds; it is a **secondary** filter inside `T*rho - O <= N*e`, never a standalone cap. This repo has a prior on exactly this failure mode (`background/nodes/pb_design_ceiling/proof.md:125`, "the naive count is false for that family"). I POSE, I do not claim.

6. **F1 was still not exercised, for the second round running.** Round 31 flagged `F1` (a realizable `T = rho+2` with `w* > 7m-1`) as live and untested. I have now supplied the missing *premise* — a realizable `T = rho+2` — but at `m = 1` the `w*` window is the single point `{2rho} = {6} = {7m-1}`, so the test is degenerate by construction. F1 remains unexercised, and `m = 1` has **zero power** over it.

7. **No exhaustive `m = 2` search was run**, although `m = 2` is exactly where my own ledger puts the boundary (`excess(2) = -1`). That is the single highest-value experiment this round identified and did not do. Enumerating it needs triples of `7`-subsets of a `32`-set (`C(32,7)^3 ~ 4e19`) and is not a brute-force job; the reduction in D3 turns it into a finite algebraic system, which is the handoff.

8. **Two of my greps scanned quarantined trees.** My exclusion filters (`grep -vE 'prize-codex-|pilots_20260811|CAMPAIGN_LEDGER'`) were applied to grep's **output**, not its search path, so the recursive scans did traverse `notes/pilots_20260811/` (sibling round-33 dirs), `notes/pilots_20260802/` and `prize-codex-` paths. **No line from any of them ever entered my context** — the filters removed them and in fact no matching line survived — but the scan touched the files, and the constraint says "never open". Disclosed rather than glossed. See COMPLIANCE.

9. **`s = 0` is asserted from the construction, not independently measured.** In every witness the locator sets are pairwise disjoint, so no domain point is a common root and `s = 0` follows; but I did not compute the primitive generator's fixed factors directly. It is a derivation, not an instrument reading.

10. **The `d_x <= e` step, which is the spine of my whole reduction, is BANKED, not mine** (`saturation_rigidity/statement.md:49-50`). See CATCH-24A.

---

## CATCH-24A — own-repo subtraction, run BEFORE every claim

| object | in-repo prior | verdict |
|---|---|---|
| `T` = "finite slopes carrying a domain-split degree-`r` locator" | `background/nodes/rate_half_ca_hankel_minimal_index_budget/statement.md:32-33` | banked (definition) |
| CA-bad slope set `=` supported slope set | `background/nodes/rate_half_ca_hankel_split_pencil_equivalence/statement.md:36-42` `(HS3)`, and `:45-47` "an exact supported-slope census" | **banked and PROVED.** My D1 reconciliation *uses* this; it does not establish it. |
| `d_x <= m` (`= e`) | `background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md:49-50` | **banked, and it is the spine of my reduction** |
| deficit identity `sum_x (m-d_x) = 1+O` | same, `:53` `(SAT4)` | banked |
| `T*rho - O = sum_x d_x` incidence identity | `notes/pilots_20260810/rh_type2_stratum/REPORT.md:96` (citing `saturation_rigidity/proof.md:38,48`) | banked |
| "fully domain-split members of a pencil" as the object to count | `background/nodes/rate_half_list_budget_three_residual_transversal_atlas/statement.md:76`, `claim_contract.md:6,22` | **PORT.** Same instrument, different lane (list-budget-three). New here is the consumer: the `ca_hankel` `A=3` stratum. |
| `T*rho <= N` disjointness fence, and "`w* = 2rho` is vacuous for `m >= 2`" | `notes/pilots_20260810/rh_type2_stratum/REPORT.md:30`, quoting `apolar_origin/REPORT.md:78` (R4) | **banked — and my `m=1` witness is its unique boundary case realized.** `(4m+1)(4m-1) <= 16m` holds only at `m=1`; I exhibit exactly that object. This CONFIRMS round 31, it does not extend it. |
| `T <= r+1` exhibited to FAIL | `background/nodes/xr_nondeep_tangent_supportwise_payment/refutation.md:29` ("eight bad slopes, exceeding `r+1=6`"); `notes/pilots_20260810/rh_farca_upper/REPORT.md` (measured `T = 8`, wide regime) | **banked in the WIDE regime `r > R/2`.** My witness is at `r = R/2-1` (narrow regime, where `minimal_index_budget`'s round-32 narrowed scope HOLDS, `statement.md:86-104`). Different regime; I claim only that. |
| `(ERC4)` `T <= 4e+1` | `background/nodes/rate_half_ca_hankel_exceptional_root_charge/statement.md:75-79` | banked; **my contribution is that it is ATTAINED at `e = m = 1`** |
| `(NEWCAP)`, `(OV)`, `(AO1)`, `(FR)`, `9/4` | `notes/pilots_20260810/rh_type2_stratum/REPORT.md:19,164,184-188` | banked, round 31 |
| LB1 | `notes/pilots_20260810/rh_overlap_cap/REPORT.md:19,79-85` | banked, round 31 |
| LB1 is a moving-kernel object with `T = r+1 > rho` | `notes/pilots_20260810/rh_farca_upper/REPORT.md:66`; petal structure `:152` | **banked — and it is the fact that settles CATCH-24C.** My step is only to notice it puts LB1 in the corank-0 branch. |
| naive dimension counts fail | `background/nodes/pb_design_ceiling/proof.md:125` | banked; quoted against my own D3 |
| **the reduction "supported slopes = totally-split members of the locator curve `Q_Z`, and `d_x <= e` makes the fibre structure the whole object"** | greps for `totally split`, `split member`, `fibre` over `background/`, `critical/`, `notes/pilots_20260810` returned the atlas node (other lane) and the `type2_fr` fibre-spend nodes (a different functional: fibre *mass*, not fibre *count*) — **no prior in this lane** | claimed as new **in this lane only**, low confidence that the idea is new anywhere |
| **an exhibited `(SAT1)–(SAT5)` model with `T = rho+2`** | greps for `realizab`, `SAT3.*realiz`, `rho+2 is realiz`, `vacuou` over `background/`, `critical/`, `notes/pilots_20260810`, `notes/pilots_20260802` returned **no prior**; the only adjacent text is `notes/pilots_20260810/rh_fr_algebraic/REPORT.md:223` declaring the census has **zero power** over `(SAT3)` | **claimed as new.** The campaign had no realizability datum, in either direction. |

---

## D1 — THE DEFINITIONAL RECONCILIATION (CATCH-24C), THEN THE LADDER

### D1.1 The two definitions, quoted side by side

**(SAT) lane** — `background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md:16`:

> "Let `Z` be the set of finite supported slopes and `T=|Z|`."

on the profile `:11-14` `(SAT1)` `m>=1, rho=4m-1, N=16m, A=3, e=m, s=0, delta=rho-3e=m-1`, with the strict target `T<=rho+1` and the unique failure size `T=4m+1=rho+2` `:36-40` `(SAT3)`.

**LB1 lane** — the counted object is `B_ca^far(a)`, the finite CA-bad slope set of a column-far pair, `notes/pilots_20260810/rh_overlap_cap/REPORT.md:19`:

> "**LB1 (unconditional lower bound).** For the razor row and every `a` in the open bracket, `B_ca^far(a) >= n-a+1 = r+1`."

**The bridge is PROVED**, `background/nodes/rate_half_ca_hankel_split_pencil_equivalence/statement.md:36-42`:

> "Consequently, if the pair is column-far, its finite CA-bad slope set is exactly `{gamma in F: ker(M_r(y_0)+gamma M_r(y_1)) intersects D_r(D)}`. `(HS3)`"

and `:45-47`: "The remaining bound `B_ca^far(n-r)<=r+1` is therefore an **exact supported-slope census**". The `minimal_index_budget` node uses the two names interchangeably in one sentence — `:32-33` "the number `T` of finite slopes carrying a domain-split degree-`r` locator" and `:61` "at most `r+1` **supported finite slopes**".

> **VERDICT (CATCH-24C): the lanes DO reconcile. `T_LB1` and `T_SAT` are the same functional, by a PROVED equivalence. There is no equivocation.**

### D1.2 …and it changes nothing, because the *configuration* does not transfer

On the strict row `r = R/2-1` (`minimal_index_budget/statement.md:82-84`: "only the final strict budget `2^39` (`r=R/2-1`, possible `A=3`)"), `A=3` forces `rho = (R-2)/2 = R/2-1 = r`, so **`r = rho` and `r+1 = rho+1` are the same integer**. My R2 registration read that coincidence as a transfer. It is not one:

- LB1's construction (`rh_overlap_cap/REPORT.md:79-85`) takes a core `E` with `|E| = a-1` and `T_set = D\E` with `|T_set| = r+1`; its locator sets are `S_{lam_j} = T_set \ {j}` — the `r+1` subsets of size `r` of an `(r+1)`-set. Verified independently in `rh_farca_upper/REPORT.md:152` ("the petal structure, verbatim").
- Hence every core point lies in `r` of the `r+1` locators: **`d_x = r = 4m-1`**. The `(SAT)` profile requires `d_x <= e = m` (`saturation_rigidity/statement.md:49-50`). `4m-1 > m` for every `m >= 1`.
- Equivalently: LB1's syndrome pencil has **full column rank `r+1` generically** (its rank drops to `r` exactly at the `r+1` bad slopes), so its generic kernel is `0`, there is no primitive generator `Q_Z`, and `e` and `s` are undefined. That is the branch `minimal_index_budget/statement.md:62` sets aside: "Indeed, the full-column-rank branch is already proved."

> **So LB1 attains `T = r+1` in the corank-0 branch; the `A = 3` branch `(SAT)` is about is `corank 1`, and LB1 says nothing about it.** Before this round the `A=3` rank-deficient branch had **no** constructed object with `T > 3` at any scale.

### D1.3 The reduction that makes construction possible

With generic corank 1, `ker M(gamma) = <Q_gamma>` and `Q_Z` has coefficient degree `e` in `Z`. Reading `Q_Z` as a bivariate `F(Z,x)` of bidegree `(e, rho)`:

- `gamma` is supported **iff** `F(gamma, ·)` is (a scalar times) a monic squarefree degree-`rho` polynomial split over `D` — i.e. the supported slopes are exactly the **totally-split members of the locator curve**;
- for each `x in D`, `F(·, x)` has `Z`-degree `<= e`, which is precisely the banked `d_x <= e` (`saturation_rigidity/statement.md:49-50`);
- so the whole configuration is the **fibre structure** of `F`, and `sum_x d_x = T*rho - O <= N*e` is the hard incidence bound.

At `e = 1` the curve is a **pencil**, `d_x <= 1` forces the locator sets to be **pairwise disjoint**, and the supported slopes are the totally-split fibres of the degree-`rho` rational map `psi = -Q_0/Q_1 : P^1 -> P^1`. Since `T >= 2` then forces two disjoint split `rho`-sets, **enumerating unordered pairs of disjoint `rho`-subsets of `D` enumerates every candidate pencil**: `C(16,3)*C(13,3)/2 = 80,080` at `m = 1`, independent of `q`. That is the exhaustive `m=1` search.

### D1.4 THE T-LADDER BY CONSTRUCTION (`d4_ladder_results.txt`)

Explicit family (**Kummer pencil**): for `q = 1 mod rho`, take `Q_Z(X) = X^rho + Z`. Then `q_rho == 1` (never degenerate), `q_0 = Z`, so `e = 1`, `s = 0`, and `Q_Z(x) = x^rho + Z` has the single root `Z = -x^rho`, giving `d_x <= 1`. The member at `gamma` is `X^rho + gamma`, split over `F_q` exactly when `-gamma` is a nonzero `rho`-th power, with root set a **coset of `mu_rho`** — pairwise disjoint by construction. Every cell below was solved for `(y_0,y_1)` and verified column-far at generic rank `rho`.

| `m` | `rho` | `N` | `rho+2` | `e=1` ceiling `floor(N/rho)` | **T measured, two fields** | fields |
|---|---|---|---|---|---|---|
| 1 | 3 | 16 | **5** | 5 | **5, 5** | 67, 73 |
| 2 | 7 | 32 | 9 | 4 | 4, 4 | 197, 211 |
| 3 | 11 | 48 | 13 | 4 | 4, 4 | 199, 331 |
| 4 | 15 | 64 | 17 | 4 | 4, 4 | 271, 331 |

**The ladder attains its own ceiling at every `m`, and the ceiling equals `rho+2` only at `m = 1`**: `sum_x d_x = T*rho <= N*e = N` gives `T <= floor(16m/(4m-1)) = 5, 4, 4, 4, …`. For `m >= 2` the `e = 1` route stalls at `4` against `rho+2 = 9, 13, 17`. **`(SAT1)`'s `e = m` is not decoration — it is the entire difficulty**, and `m = 1` is the unique `m` where the two coincide.

---

## D2 — THE (SAT) PROFILE OF THE LARGE-T CONFIGURATIONS

Measured on the exhaustive `m=1, q=17` set (`d2_realize_results.txt`) and re-measured on the designed-domain large-`q` witnesses (`d3_results.txt`). Every quantity below is an instrument reading, not a derivation.

| functional | required by (SAT) | **measured** |
|---|---|---|
| generic rank `rho` | `4m-1 = 3` | **3** (all cells) |
| `A = R+1-2rho` | `3` | **3** |
| `e` (parameter degree) | `m = 1` | **1** |
| `s` (fixed domain factors) | `0` | **0** (derived — MISS 9) |
| `T` | `rho+2 = 5` | **5** |
| `u_gamma` | `rho = 3` | **3,3,3,3,3** |
| `O = sum(rho-u_gamma)` | `<= delta = m-1 = 0` `(SAT2)` | **0** |
| rank-drop slopes `c_gamma` | `sum c_gamma <= delta = 0` | **0** |
| `max d_x` | `<= m = 1` | **1** |
| `sum_x (m-d_x)` | `= 1+O = 1` `(SAT4)` | **1** |
| parameter-saturated columns | `>= N-(1+O) = 15` `(SAT5)` | **15** |
| column-far | no common split locator `(HS2)` | **OK** |
| `w* = a*` | — | **6** |

**`a*` versus `7m-1` — F1 does NOT fire.** `a* = w* = 6`, and `7m-1 = 6`. `(NEWCAP)` is satisfied **with equality**. It is satisfied degenerately: at `m = 1`, `Lmin(0) = (N-1)C(m,2)+C(m-1,2) = 0`, so `(NEWCAP)` collapses to `w* <= 2rho = 6`, which is the trivial bound. So `m=1` **confirms nothing about `(NEWCAP)`'s content** — declared zero-power (Z3). What it does do is make F1's *premise* live for the first time.

**The whole counting chain is attained simultaneously.** From the measured locator sets: taking `W = S_0 u S_1` (`|W| = a* = 6`), exactly `2` slopes satisfy `S ⊆ W` and `3` do not, so

```text
T_1 = 2 = min(m+1, floor(a/(a-rho)), floor((am+O)/rho)) = min(2,2,2)
T_2 = 3 = CAP(m,a) = floor((N-a)e/(R+1-a)) = floor(10/3)
(AO1) = T_1 + T_2 = 5 = T                       EXACTLY ATTAINED
(MI2)  = rho - Ae + floor((N-s)e/(rho-s)) = 0 + floor(16/3) = 5   ATTAINED
(ERC2) = floor(((N-s)e + rho - Ae)/(rho-s))     = floor(16/3) = 5  ATTAINED
(ERC4) = 4e+1                                   = 5                ATTAINED
```

Four independent banked bounds, all equalities on one object. **That is the strongest available evidence that the `A=3` counting layer has no slack left to extract at the bottom of the range**, and it is why I read round 31's `9/4` as a route ceiling rather than as looseness.

**No `(SAT)` axiom is violated by large `T`, so no axiom becomes the T-cap candidate.** D2's "if no" branch is therefore closed: the T-cap, if it exists, is **not** an axiom violation but a *moduli* obstruction that turns on at `m >= 3`. That is D3.

---

## D3 — THE T-CAP ATTEMPT: POSED, NOT CLAIMED

Since `(SAT3)` is realized, the honest deliverable is (i) the calibration table above and (ii) an `m`-dependent cap **candidate**. Here it is, flagged as a heuristic with its own failure mode named.

> **(TCAP-DIM), POSED.** Fix the `(SAT1)` profile and ask for `T = rho+2`. The free data are: the curve `F(Z,x)` of bidegree `(e,rho) = (m, 4m-1)` (`(m+1)·4m - 1` projective coefficients), the slope set `G` (`T` of them), and the evaluation domain `D` (`N = 16m` points). The binding conditions are `(SAT4)`: all but `1+O` of the `16m` domain points must have **all `m` roots** of the degree-`m` polynomial `F(·,x)` inside `G`, i.e. `F(·,x) | H_G(Z)`. Counting these as `m` conditions per point less one free `x`:
>
> ```text
> params(m) = [(m+1)4m - 1] + (4m+1) + 16m = 4m^2 + 24m
> conds(m)  = T*rho - O                     = 16m^2 - 1 - O
> excess(m) = 12m^2 - 24m - 1 - O
> ```
>
> `excess < 0` **exactly** for `m in {1, 2}` (at `O = 0`: `-13`, `-1`), and `excess > 0` for **every** `m >= 3` (`+35, +95, +179, …`, and `2.27e23` at `m = 2^37`). A second, independent bookkeeping (conditions counted as divisibility at `16m-(1+O)` points; parameters = curve and `G` only) gives `excess2(m) = 12m^2 - 24m - 2` — the same sign change between `m = 2` and `m = 3`.
>
> **CONJECTURE.** `(SAT3)` is realizable exactly for `m <= 2` and unrealizable for `m >= 3`; hence `T <= rho+1` at the official `m = 2^37`, closing the strict endpoint.

**Positive controls (the ledger reproduces what I measured).** `e = 1` family at `T = floor(N/rho) = 4`, `m >= 2`: `params = 24m+3`, `conds = 16m-4`, `excess = -8m-7 < 0` — predicted realizable at every `m`, and it **is** (D1.4, two fields per cell). At `m = 1, T = 5`: `excess = -13`, predicted realizable, and it **is** (six fields).

**Falsifiers, pre-committed.**
- **G1 (kills it outright):** an `(SAT1)`-profile column-far Hankel pencil with `T = rho+2` at any `m >= 3`.
- **G2 (the decisive experiment, NOT RUN):** settle `m = 2`. The ledger puts it at `excess = -1`, i.e. *marginal*. D3's reduction makes this a finite algebraic system rather than a brute force: `F(Z,x) = c_2(x)Z^2 + c_1(x)Z + c_0(x)` with `deg c_i <= 7`; the requirement is a 9-vertex multigraph of 31 edges with degrees `7^8, 6` (**this design exists** — take `K_9` minus a 2-path and 3 disjoint edges), and for each edge `{a,b}` a point `x` with `c_1(x) = -(a+b)c_2(x)`, `c_0(x) = ab·c_2(x)`. That is `62` equations **linear in the 24 coefficients** once `G` (9 free) and the 31 points (31 free) are chosen — 40 parameters against 39 rank conditions. A realization exists iff that system has a rational point.
- **G3:** a proof that the `16m-(1+O)` divisibility conditions are not independent (the standard way naive counts die — `background/nodes/pb_design_ceiling/proof.md:125`).
- **G4 (and I supply the warning myself):** a *structured* family can beat a dimension count. My own Kummer family is exactly such a family at `e = 1` and exists at every `m`. If a Galois-cover analogue exists at `e = m`, (TCAP-DIM) dies. I have no evidence either way.

**What (TCAP-DIM) is NOT.** It is not a theorem, not a proof sketch of a theorem, and not usable as a fence. MISS 5 records a case where it returns the wrong answer. Its only current status is: *the one quantitative story consistent with every measurement this round produced*, including the two positive controls and the `m = 1` realization it correctly predicts.

---

## D4 — VERDICT ON THE CONDITIONAL STACK

> **CALIBRATED. Not vacuously closed. Still conditional — and now conditional on something known to have a model.**

- **Vacuously closed: REFUTED.** `(SAT3)` has a model at `m = 1` over six fields, with `(SAT1)–(SAT5)` all satisfied and the pencil verified column-far at generic rank `rho`. The "largest single result of the campaign" branch of my brief is **dead**.
- **Calibrated: YES, and sharply.** `(AO1)`, `(MI2)`, `(ERC2)`, `(ERC4)` are simultaneously attained; `(NEWCAP)` holds with equality (degenerately); round 31's R4 fence (`T*rho <= N` only at `m=1`) is confirmed **by exhibiting its unique boundary object**.
- **Still conditional-with-power: YES for `m >= 2`.** Nothing this round bears on `e = m >= 2`. `(NEWCAP)`, the `7/4` ledger, FR-canonical's ledger use and the one-integer residual (i) all remain exactly as round 31 left them, with the `9/4` intact.
- **The new constraint on the whole programme:** every future proof attempt must be `m`-dependent and must **fail at `m = 1`**. The witness above is the regression test. A proof that survives it is not thereby correct; a proof that does not survive it is thereby wrong.

**Handoff, in priority order.** (1) Settle `m = 2` via the G2 system — it is the ledger's boundary and the only cheap decisive experiment left. (2) Look for an `e = m` structured family (Kummer/Galois analogue) — that is G4, and it is the way (TCAP-DIM) dies. (3) Re-run round 31's `(FR)` programme with the knowledge that the counting layer is exactly tight at `m = 1`, so the missing factor of 2 must come from an instrument that is trivial there.

---

## PREDICTIONS vs OUTCOMES

| | registered | outcome |
|---|---|---|
| P(full reconciliation) `0.35` / cousins `0.45` / equivocation `0.20` | — | **the `0.35` branch RESOLVED YES** — same functional, PROVED equivalence `(HS3)` |
| P(`T=rho+2` realizable) `0.12` | — | **MISS — it is realizable**, exhaustively at `m=1,q=17` and at five more fields |
| P(T-cap theorem) `0.08` | — | **no theorem** (correctly priced) |
| P(T-cap candidate with named axiom + sketch) `0.55` | — | **PARTIAL** — a candidate, but *not* an axiom violation: no `(SAT)` axiom is violated by large `T`, so the mechanism I registered does not exist |
| P(F1 fires \| realizable) `0.10` | — | **did not fire** (`a* = 7m-1` exactly); but degenerately, zero power |
| **R2** LB1 realizes `rho+1`, failure one slope beyond, `P = 0.70` | — | **PARTIAL MISS (MISS 1)** — the number reconciles, the configuration does not; LB1 is corank-0 |
| R2b P(LB1 reaches `>= rho+2` on the (SAT) count) `0.15` | — | resolved NO |
| P1 transposition/duality involved, `0.50` | — | **NO** — no transposition; a PROVED equivalence, not a duality |
| P2 targeted constructions reach `T >= 4` at `m=1..4`, `0.60` | — | **HIT** — `T = 5,4,4,4`, two fields each |
| P2b `T >= 9` at some `m >= 2`, `0.15` | — | **not achieved** |
| P3 binding axiom is `(SAT4)`, `0.55` | — | **MISS as posed** — `(SAT4)` is *satisfied*, not violated. `(SAT4)` is nonetheless the operative constraint, entering as the moduli condition in (TCAP-DIM). Partial credit at best. |
| P4 no cheap counting contradiction, `0.85` | — | **HIT** — `16m^2-1-O <= 16m^2` is consistent at every `m`; the cap needs structure |
| P5 settle `m=1` this round, `0.65` | — | **HIT — settled affirmatively and exhaustively** |
| P6 failure would be a strictness/genericity side condition, `0.40` | — | **resolved NO** — no side condition fails; `A=3`, corank 1, column-far all verified |
| P7 `w* < 7m-1`, `0.85` | — | **HIT (boundary)** — `w* = 7m-1` exactly, so `<=` holds and F1 does not fire |
| P8 `>= 1` CATCH-24A subtraction lands, `0.90` | — | **HIT — five landed**, two of them (`d_x <= e`; the R4 `T*rho <= N` fence) load-bearing for my main result |

---

## ZERO-POWER DECLARATIONS

1. **`m = 1` has zero power over the official `m = 2^37` configuration.** It shows the axiom scheme is consistent; it does not show the official instance exists. `e = m` is `1` there and `2^37` officially.
2. **`m >= 2` was not touched.** Every `m >= 2` object I built has `e = 1`, a range `(ERC2)` already closes (`exceptional_root_charge/statement.md:70-73`). The ladder entries `T = 4` are **not** measurements of the `m >= 2` frontier.
3. **`m = 1` has zero power over `(NEWCAP)`.** `Lmin(0) = 0` there, so `(NEWCAP)` degenerates to the trivial `w* <= 2rho`; attaining it says nothing about the non-degenerate bound, and F1 remains unexercised.
4. **The exhaustive `q = 17` scan is exhaustive over PENCILS, i.e. over `e = 1`.** At `m = 1` that is the whole `(SAT1)` profile (`3e <= rho` forces `e <= 1`), so the scan is genuinely complete **there and only there**.
5. **The `q = 97, 113, 193, 241, 257` negatives in `d1_m1_results.txt` are about a FIXED domain `D = mu_16`, not about `q`.** With `D` designed, `q = 1009, 2003, 10007` all succeed on the first draw. Do not read the negatives as a `q`-decay.
6. **(TCAP-DIM) is a naive dimension count with a known blind spot** (MISS 5). It has no standing as a bound.
7. **`s = 0` is derived from disjointness, not measured** (MISS 9).
8. **The `m=2` "design exists" statement is combinatorial only** — the 9-vertex 31-edge multigraph exists; that is not evidence the algebraic system has a solution.

---

## MEASURED FUNCTIONALS (CATCH-19C)

`m, rho=4m-1, N=16m, R=8m, k=N-R, r` (`=rho` on the strict row), `A=R+1-2rho`, `e`, `s`, `delta=rho-Ae`; `T`; per slope `S_gamma`, `u_gamma=|S_gamma|`, `c_gamma=rho-rank M(gamma)`, `O=sum(rho-u_gamma)`; per point `d_x`; the deficit `sum_x(m-d_x)`; saturated-column count; `w*=a*=min_{g!=g'}|S_g u S_g'|`; `T_1`/`T_2` split against `W`; `CAP(m,a)=floor((N-a)e/(R+1-a))`, `T1cap`, `AO1`, `(MI2)`, `(ERC2)`, `(ERC4)`; column-farness (no common split locator, `(HS2)`); generic rank and the rank multiset over all finite slopes. **New here:** the fibre functionals of the locator curve — `F(Z,x)` of bidegree `(e,rho)`, the totally-split-member count, and the fibre multiset `{-Q_0(x)/Q_1(x) : x in D}` at `e = 1`. Registered but not measured: **none** — `s` is flagged as derived (MISS 9), and the `m = 2` system is declared not run (MISS 7).

---

## COMPLIANCE

**Registrations.** R0–R7 (notation, the four demanded blind priors plus three refinements, the load-bearing R2 arithmetic prediction, P1–P8 with numeric windows, five pre-committed zero-power declarations, fixed route order, four falsifiers, compliance plan) were appended to `PREREG.md` under "## Pilot registrations" with the Edit tool **after reading exactly the two named anchors and before any other read, any grep, and any interpreter invocation**. No post-registration addenda.

**Compute law.** **Five interpreter invocations**, every one of the form `tools/ramguard local -- python3 …` issued from the repo root with the literal `--` and an explicit `RAMGUARD_TIMEOUT=290` (`local` = 1G / 5 min; 290 s is *inside* the profile, not an extension). **Ramguard status: all five exited under the guard; zero guard failures, zero memory events.** No `tiny` runs were needed. **No bare `python3` at any point.** Stdlib only — no third-party imports, no Modal, no network, no git, no subagents. One logical (non-guard) defect is disclosed as MISS 4: `d4_ladder.py`'s first run scanned only nullspace basis vectors and produced a false negative at `m = 2,3,4`; the corrected run (random combinations) is the one in `d4_ladder_results.txt`.

**RAM discipline.** `dag.json` **never opened** — node shards and grep only. File-at-a-time reads throughout; the two large statements (`rate_half_ca_hankel_exceptional_root_charge`, `rate_half_band_crossing_location`) were read in bounded `sed` windows rather than whole, and `critical/nodes/rate_half_band_crossing_location/statement.md` was never read at all (only grepped). Each script holds `O(N^2 + q)` state and writes its own checkpointed results file.

**Quarantine — with a disclosed deviation (MISS 8).** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` was **never displayed, never read, and no line of it ever entered my context**. However, two recursive greps carried `notes/pilots_20260802` / the repo root in their **search path** while filtering `prize-codex-`, `pilots_20260811` and `CAMPAIGN_LEDGER` out of their **output**. The scans therefore traversed the quarantined trees — including the sibling round-33 directories under `notes/pilots_20260811/` — even though nothing from them was surfaced. No sibling round-33 directory was listed, opened, or read; no `ls` of `notes/pilots_20260811/` was run. I report this as a genuine deviation from "never open" rather than claiming clean compliance on a technicality. No path containing `prize-codex-` was opened.

**Write scope.** Every write is inside `notes/pilots_20260811/rh_sat3_realizability/`: `PREREG.md` (registrations appended), `d1_m1_exhaustive.py` + `d1_m1_results.txt`, `d2_hankel_realize.py` + `d2_realize_results.txt`, `d3_largeq_and_ledger.py` + `d3_results.txt`, `d4_ladder.py` + `d4_ladder_results.txt`. **`REPORT.md` itself was REFUSED by the harness** ("Subagents should return findings as text, not write report files"), so this report is returned verbatim as the final message per the brief's fallback clause; the directory therefore contains 9 files and no `REPORT.md`. **No** `dag/`, `nodes/`, `critical/`, `background/` or `tools/` edits; no git operations of any kind; the session scratchpad was not used. AUDIT-AND-DRAFT respected: nothing outside my directory was altered, and (TCAP-DIM) is posed for coordinator triage, not banked.

**Banked scripts.** **None were copied and none were executed.** All four scripts were written from scratch in my own directory against the nodes' own conventions (`M_r(y)=(y_{i+j})` with the `(R-r) x (r+1)` shape from `split_pencil_equivalence/statement.md:14-18`; `D_r(D)` = monic squarefree degree-`r` with roots in `D`, `:20-21`; `v_x = 1/prod_{y!=x}(x-y)`). The cost is that this round carries **no replay-identity evidence** — the same gap round 31 declared (its MISS 3). Independent cross-checks used instead: the `q=17` exhaustive family count (16) is reproduced by two different code paths (`d1` fibre-multiset count, `d2` full Hankel census); the Kummer family reproduces `T = 5` at `m=1` from a completely different construction than the pair-enumeration; and every witness satisfies the banked identity `sum_x d_x = T*rho - O` exactly.

**Method discipline.** CATCH-24A own-repo greps were run before every novelty claim and produced **five live subtractions**, two load-bearing (`d_x <= e`; the R4 `T*rho <= N` fence). CATCH-24C was executed as the round's first obligation with both definitions quoted side by side at `file:line`, and it **overturned my own registered R2**. Every quantifier claim above carries a `file:line`. Every max-quantified claim carries a zero-power declaration. Two-field confirmation for every structural claim (`m=1`: `q in {17,67,73,1009,2003,10007}`; `m=2,3,4`: two `q` each). MISSES FIRST, and the round's two self-corrections — the ladder bug (MISS 4) and the ledger's blind spot (MISS 5) — are reported as falsifications of my own work, not retrofitted.
