# REPORT.md — collinearity_object (round 29) — persisted verbatim by the coordinator (Fable) from the pilot's final message, task a78c092697e9a02a9, 2026-08-10. Pilot: Opus. No edits.

All measurements complete. Final report:

---

# REPORT — collinearity_object (round 29)

## VERDICT (first)

**D1 — THE UNIFICATION: one object, one functional, two regimes. ssparse's excess-collinear configurations are a THIRD CLASS — neither apolar's structured families nor apolar's q-dying sporadics.** The two pilots measured the *same* point set (proved as an identity, verified 1024/1024 at two fields and two `N`, and confirmed numerically by reproducing ssparse's `F_COLL = 16/34/28` **exactly** from apolar's reciprocal side, collision counts and all). What separates their answers is a single integer:

```
RIG := a - 1 - 2s        a = |W| = ambient+1,  s = reciprocal index size
```

apolar's cell `(a,s) = (6,3)` sits at `RIG = -1`; ssparse's cell `(a,s) = (3,6)` sits at `RIG = -11`. ssparse's 28 is a **small-ambient (a ≤ 4) artifact**: at `a ≥ 5` the excess vanishes at every field tested (max `F_COLL = s+1` in **all 1152** sampled `(W,q)` configurations, six fields). The official ambient is `a = w* ≥ 2^39+2`.

**D3 — THE SPORADIC BOUND LANDED, UNCONDITIONALLY, AT FULL STRENGTH ON A BAND.** Not a `q`-decay estimate, not conditional on GRH or an incidence conjecture: **for `RIG ≥ 0` sporadic collinearities of `{P_S}` do not exist at all**, uniformly in `q`. Route (a) (determinantal/Bezout), two lines of algebra:

&gt; **T4.** If `2s ≤ a-1`, then for any line `ℓ` and any three `P_{S_i} ∈ ℓ`, `1/σ_{S_i} = α_i/σ_{S_1} + β_i/σ_{S_2}` on `W` gives, after multiplying by `σ_{S_1}σ_{S_2}σ_{S_i}`, two degree-`2s` polynomials agreeing at `a &gt; 2s` points — hence **a polynomial identity**, hence `σ_{S_i} | σ_{S_1}σ_{S_2}`, hence every `S_i ⊆ G := S_1∪S_2` and the complements `G\S_i` are **pairwise-disjoint fibres of a degree-`k` map** (`k = |G|-s`). Therefore `Mk ≤ |G| = s+k`, i.e. `M ≤ 1 + s/k ≤ s+1`, and every collinear family is a **pencil**.

With the banked counting layer `d_x ≤ e = m` (verified verbatim from primary text, `rate_half_ca_hankel_endpoint_saturation_rigidity` (SAT2–SAT4)): the fibres partition `G`, so `d_x = M-1` on `G` (or `d_x = M` on `∩S_i`), giving **`M ≤ e+1 = m+1`**. Hence on that band the weight-extremal type-2 count is `≤ m+1`, and with `T_1 ≤ e+1`, `T ≤ 2m+2 ≤ 4m = ρ+1` for every `m ≥ 1` — contradicting SAT3.

**On the official profile the hypothesis `2s ≤ a-1` (with `s = R+1-a = 8m+1-a`) reads `w* ≥ ⌈(16m+3)/3⌉ — the top TWO THIRDS of the admissible `w*` window, measured share 0.6667, exactly complementary to apolar's (AO1) band's 0.3333.** apolar's own audit named large-`w*` ("where the mass sits") as the round-29 starting point; that is the part now closed.

**NEITHER BUDGET CLOSES. Status unchanged.** Three named residuals, below.

**The `q=17` test case is explained to the unit.** `q=17` forces `m=1` (`N=16 | q-1=16`), hence `w*=6`, `s=3`, `2s = 6 = a &gt; a-1 = 5`: **the hypothesis fails by exactly one.** Measured on the fence's own `W`: `σ_{S_1}σ_{S_2} − σ_{S_3}(ασ_{S_2}+βσ_{S_1}) = 4·σ_W` — a nonzero multiple of `σ_W`, precisely the boundary term that `RIG ≥ 0` forbids. And why `q ≥ 97` does not supply it: at `RIG = -1` existence is a codimension condition whose rate decays — **0.0938 non-pencil families per random `W` at `q=17`, 0.0000 at `q ∈ {97,113,193,241,65537}`**, 64 random `W` each.

## MISSES FIRST

1. **P13 (registered miss-likely) HIT AS A MISS.** I registered that I did not expect to close either budget. I did not. Both `{2^39, 2^39+1}` stay open.
2. **P11 MISS.** Registered gap size `∈ {0,1,2}` with gap `= 0` for `m ≡ 0 mod 3`. Measured (from my own re-derivation of (AO1), which reproduces apolar's banked table **12/12**): gap `∈ {1,3}`, **never 0**, and not a function of `m mod 3` (`m=2`: {11}; `m=4`: {20,21,22}; `m=8`: {43}; `m=40`: {212,213,214}). The two bands tile the window up to 1 or 3 integers of `w*` — not zero.
3. **P7 MISS on cell C10.** I registered `F_COLL = 28` at `(N=32,a=3,s=2)` from "`N-a-s+1`". That formula is the **direct-side** family size (it needs `t`, not `s`); the reciprocal pencil size is `s+1 = 3`. Measured `F_COLL = 14` — and it is a **dihedral (inverse-pair) family of 14 disjoint pairs**, not a linear pencil. My arithmetic slip, caught by the measurement.
4. **P8 initially FAILED on a bug in my own test.** I extracted `(α,β)` from *normalised* projective representatives instead of the unnormalised `1/σ_{S_i}` basis, which rescales the coefficients and destroyed the leading-term bookkeeping (`α+β` came out `= 1`, forcing `deg D ≤ 5` and an apparent contradiction). Self-caught by the contradiction, fixed, and the corrected test hits exactly: `α+β = 14`, `D = (1-(α+β))σ_W = 4σ_W`, `c ≠ 0`.
5. **My registered threshold `RIG ≥ 0` is SUFFICIENT but NOT SHARP.** Measured `F_COLL = s+1` all the way down to `a ≥ 5` (i.e. `RIG` as low as `-6`) at both `N=16` and `N=32` and all six fields. The true boundary is strictly below my hypothesis and is **unproved** — this is exactly why the 1–3 value gap survives.
6. **A mislabelled counter in my own output, flagged not quietly reinterpreted.** `d2_sweep_results.txt` prints "TOTAL structure-theorem violations across the sweep: 107097". That counter sums the `d_x`-law check over **floppy** cells where I never claimed the law. Correct reading: **fibre-bound violations `M·k &gt; |G|`: zero in every cell of every sweep**; `d_x`-law violations: **zero in every `RIG ≥ 0` cell and in fact every `a ≥ 5` cell**; all 107097 sit at `a ∈ {3,4}`.
7. **CATCH-24A subtraction — my "new" family (F3) is not new.** `background/nodes/dihedral_quotient_stratum` already carries "products of inverse-pair quadratics `X^2-(a+a^{-1})X+1`", names it the **DIHEDRAL/CHEBYSHEV quotient `x ~ x^{-1}`**, and already flags convergence with Paper D v12's Chebyshev case (twin cosets, `K_c` kernels). My registered (F3) is that object in this setting. Claimed as a port, not an invention.
8. **P6's `q=17` window was never exercised.** I registered `F_COLL ∈ [s+1, 3(s+1)]` at `q=17` in boundary cells; measured exactly `s+1`.
9. **Registered functional `s_ℓ` NOT MEASURED.** The vanishing-slope spread was registered as a line invariant; the divisibility route made it unnecessary and I did not compute it. Declared, not dressed up.

## DELIVERABLES

All under `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260810/collinearity_object/`:

- `PREREG.md` — brief + my registrations (R0 functionals, R1 unification hypothesis, R2 regime law, R3 candidate family list, R4 route order, R5 cell grid, R6 predictions P1–P13 with numeric windows, R7 zero-power declarations, R8 compliance plan) appended with the **Edit tool before any interpreter run**.
- `d1_unify.py` + `d1_unify_results.txt` — the U1 identity test, the fence boundary test, the `|V|` ladder at `N=16`, the `N=32` cells, and the P4 cross-pilot reproduction.
- `d2_census.py` + `d2_sweep_results.txt`, `d2_n32_results.txt` — the `k`-graded census with `pdim`, counting-layer status, Galois typing of `k=2` fibres, and the RIG sweep.
- `d3_coverage.py` + `d3_coverage_results.txt` — the (AO1) re-derivation (12/12 vs banked), the tiling/gap table, the asymptotic 1/3–2/3 split, and the D4 payoff arithmetic.

**Escape replays (scratch copies, unmodified, md5-verified):** `d5_sporadic.py` — **IDENTICAL** (flat `840.00` at all five `q`; sporadic `0.167` at `q=17`, `0.000` at `q ≥ 97`; fence `W` sporadic `= 1`, triple `(4,6,16),(8,10,15),(9,12,13)`). `d2_sparse.py` — **IDENTICAL** (`F_COLL` `τ=2`: `16/34/28`; `τ=3`: `12/10/10`; `#pts` `256/1621/1706`).

## WHAT LANDED

**(1) D1 — the unification identity (U1), proved and verified.** Because `D` is a multiplicative subgroup (`σ_D = X^N-1`, `σ'_D(x) = N/x`), for `x ∈ W`

```
1/σ'_{W∪S}(x) = x·σ_{D\(W∪S)}(x)/N     ⟹     P_S = diag(x/N) · L_T ,  T = (D\W)\S.
```

A diagonal map is projective-linear, so the reciprocal-locator set (apolar) and the direct-locator set (ssparse) are the **same point set up to a fixed collineation** — identical collinearity structure. **1024/1024 exact** at `q ∈ {97, 65537}`, `N ∈ {16,32}`. Both pilots' flagship cells are `N=16, t=7`; only the ambient differs (`a=3` vs `a=6`).

**(2) D1's classification answer.** Computing both functionals on the same cells: ssparse's maximal family at `(3,6)`, `q=65537` has `M=27`, `pdim = 3 &gt; 2`, `|G| = 13` (all of `D\V`), fibre sizes `{2,…,7}` — **no pencil structure at all**, so not apolar's structured class; and it does **not** die with `q` (33 at `q=97`, 27 at `q=65537`), so not apolar's sporadic class either. It is a floppy-regime family, possible only because at `a=3` a degree-`6` locator is not determined by its values on 3 points — the index map is not even injective there (1716 `S`'s → 1655/1706 points; 256 at `q=17`, the torus `(q-1)^2`).

**(3) D2 — the complete structured census, in the rigid regime.** Every collinear family is a pencil `{α f + β g}` of degree-`s` locators with fixed part `h = gcd(f,g)` and moving degree `k`; totally-`D\W`-split members are disjoint fibres of a degree-`k` map, so `M ≤ 1 + s/k`. Measured, both fields, `N=16` and `N=32`:

| k | family | max `M` | measured | field-independent? | counting-layer status |
|---|---|---|---|---|---|
| 1 | linear/pencil (apolar's `[A-uB]`) | `s+1` | `Mmax = s+1` in **every** rigid cell | yes | `d_x = M-1` ⟹ `M ≤ e+1` |
| 2 | `COSET(μ_2)` `{u,-u}` | `1+s/2` | `Mmax = 3` at `s=4` (`=1+s/2` exactly) | yes | `d_x ∈ {M-1,M}` ⟹ `M ≤ e+1` |
| 2 | `DIHEDRAL(uv=ζ)` `{u,ζ/u}` | `1+s/2` | present at every field, many `ζ` | yes (in-repo: dihedral_quotient_stratum) | same |
| 2 | non-Galois | `1+s/2` | 91→40→14→6→4→2 as `a` grows; decays in `q` | no | same |
| `h∣N` | coset/cyclotomic (apolar's R3) | `1+s/h` | realized | yes | same |
| `k` | general degree-`k` | `1+s/k` | realized up to `k=10` | no | same |

**The key safety question is answered NO.** In every rigid cell, every family satisfies `d_x ∈ {M-1, M}` (zero violations), so the banked layer `d_x ≤ e` caps *every* structured family at `M ≤ e+1 = m+1`, and `m+1 ≤ 4m = ρ+1` for all `m ≥ 1`. **No structured family — of any moving degree, at any field — threatens the residual budgets.** apolar verified this for the `k=1` family; it now holds for the whole census.

**(4) D3 — T4 and its band.** Stated above. `2s ≤ a-1` with `s = R+1-a` gives `w* ≥ ⌈(16m+3)/3⌉`; measured window share `0.6667` at `m = 2^10, 2^20, 2^30, 2^37` (apolar's `(AO1)` band: `0.3333`). The two closures are asymptotically **exactly complementary**: `1/3 + 2/3`, gap `1` or `3` integers.

**(5) The `q`-decay explained without character sums.** At `RIG = -1, -2` the identity fails only by the single term `c·σ_W`, `c = 1-(α+β)`; existence is then a codimension condition. Measured non-pencil families per random `W`: `(6,3)` `RIG=-1`: `0.0938 → 0` at `q ≥ 97`; `(5,3)` `RIG=-2`: `35.17 → 0.203 → 0.109 → 0 → 0.047 → 0` for `q = 17,97,113,193,241,65537`. Route (b) (character sums) was registered third and **is not needed**: it would only re-derive a mean statement that R7 already declares zero-power over a max.

**(6) A safety number with teeth.** Even where sporadics exist, they never beat the pencil family: **max `F_COLL = s+1` in all 1152 sampled `(W,q)` configurations at `a ≥ 5`**, plus every deterministic-`V` cell in the sweep. The `7–9×`-random collinearity ssparse flagged is confined to `a ∈ {3,4}`.

**(7) D4 — the payoff map, re-derived from primary text.** Profile from `..._saturation_rigidity` and `..._half_distance_a3_slope_slack_ledger`: `ρ=4m-1, N=16m, R=8m, A=R+1-2ρ=3, e=m`; `d_x ≤ m` and `Σ_x(m-d_x)=1+O ≤ m` under the failure `T = ρ+2` (SAT3/SAT4). Official `n = 2^41 = N ⟹ m = 2^37`, so **the budgets are exactly `{ρ+1, ρ+2} = {2^39, 2^39+1}`** and SAT3's "failure size is exactly `ρ+2`" *is* the one-slope deficit. `B*(q) = ⌊q/2^128⌋`, budget `b` met for `q ≥ 2^128 b`:

- budget `2^39` → `q ≥ 2^167`; budget `2^39+1` → `q ≥ 2^167 + 2^128` (**fourth independent derivation** of the round-28 precision fix);
- old bracket top `2^169 = 2^128·2^41 = 2^128 n` ✓;
- extension factor `2^41/(2^39+1) = 4 − 4/(2^39+1) = 4 − 7.275958e−12` → `4.000000` to six decimals, **not exactly 4**;
- the sliver `(2^167, 2^167+2^128)` has `⌊q/2^128⌋ = 2^39` exactly; relative width `2^-39`; "all `q &gt; 2^167`" needs the budget **pair**;
- low end `ρ ≤ R-r = 2^34`.

**What T4 would close if the residuals fell:** the weight-extremal type-2 stratum on the top 2/3 of `w*`. **What it does not close, named exactly:** (i) the gap of 1 or 3 `w*` values per `m`; (ii) type-2 slopes whose difference codeword is **not** of minimum weight `R+1` — the reciprocal-locator normal form does not apply to them, and the counting cap there is `(N-a)e/s`, which at `a = 8m-2` is `5.04e22` against a target of `2^39`; (iii) `m=1`. Any one of the three keeps both budgets open, and all three are open.

## PREDICTIONS vs OUTCOMES

| | registered | outcome |
|---|---|---|
| P1 | `d5_sporadic.py` scratch replay exact | **HIT** — identical |
| P2 | `d2_sparse.py` scratch replay `16/34/28`, `12/10/10` | **HIT** — identical |
| P3 | (U1) 100% of ≥256 samples, two fields, two `N` | **HIT — 1024/1024** |
| P4 | reciprocal side reproduces ssparse's `F_COLL` exactly | **HIT — 16 / 34 / 28**, and `#pts` `256/1621/1706` |
| P5 | `F_COLL = s+1` exactly in every rigid cell | **HIT** — C5–C8 at `N=16`, `(5,2),(6,2),(7,3),(8,3),(11,3)` at `N=32`, both fields, zero exceptions |
| P6 | boundary cells `= s+1` at `q≥97`; `[s+1,3(s+1)]` at `q=17` | **HIT (`=s+1`)**; the `q=17` window unexercised |
| P7 | C1 `28@65537`,`34@97`; C2 `[7,60]`; C3 `[5,40]`; C10 `=28` | **HIT / HIT (10) / HIT (5) / MISS (14, and it is dihedral)** |
| P8 | fence: `D = cσ_W`, `c ≠ 0` | **HIT after a self-caught bug** — `D = 4σ_W` |
| P9 | maximal family is `k=1` in every rigid cell | **HIT 100%** |
| P10 | `d_x ∈ {M-1, M}` for every family | **HIT in every rigid cell (zero violations); fails only at `a∈{3,4}`, outside the claim** |
| P11 | gap `∈{0,1,2}`, `=0` for `m≡0 mod 3` | **MISS — gap ∈ {1,3}, never 0** |
| P12 | payoff arithmetic incl. `4 − 7.28e−12` | **HIT exact** |
| P13 | no budget closes | **HIT as a registered miss** |
| — | (AO1) re-derivation vs apolar's banked table | **12/12 AGREE** (unregistered check) |

## SELF-CORRECTIONS

1. **The P8 test bug** (normalised vs unnormalised coefficient basis) — caught by my own contradiction (a degree-5 nonzero polynomial with 6 roots), disclosed, fixed, retested.
2. **The P7/C10 arithmetic slip** — I used the direct-side family formula on a reciprocal-side cell. The measurement corrected me and produced the dihedral family as the real answer.
3. **The mislabelled violation counter** in my own results file — reported as a mislabel rather than silently reinterpreted.
4. **My threshold is not sharp** and I say so: `RIG ≥ 0` is a proof hypothesis, `a ≥ 5` is the empirical boundary, and the difference is exactly the residual gap. I did not present the empirical boundary as a theorem.
5. **CATCH-24A**: the dihedral/inverse-pair family is already in-repo; I claim a port, not a discovery. I also grepped for the divisibility identity (`σ_{S_i} | σ_{S_1}σ_{S_2}` for collinear reciprocal locators) and found it **only** in my own PREREG — no in-repo prior.
6. **Scope discipline on T4**: it bounds the *weight-extremal* type-2 stratum (the object the brief names). I did not let it masquerade as a bound on all type-2 slopes, and I priced the untouched stratum explicitly (`5.04e22` vs `2^39`).

## MEASURED FUNCTIONALS (CATCH-19C)

`L_T = [σ_T(x)]_{x∈V}`; `P_S = [1/(σ'_V(x)σ_S(x))]_{x∈V}`; `Λ(V,t)`, `Λ*(V,s)`; `F_COLL` = max points of `Λ*` on a projective line; `STRUCT3/SPOR3` = apolar's collinear-triple census by `|∪S_i| ≤ s+1`; `PEN = s+1`; `G = ∪S_i`; `I = S_1∩S_2`; `k = |G|-s` (moving degree); `pdim = dim span{σ_{G\S_i}}` (`=2` ⟺ pencil, my new invariant); `d_x` = number of family members whose locator vanishes at `x` (the banked SAT counting functional); `RIG = a-1-2s`; `(AO1)` and `a_max(m)` re-derived from apolar's printed formula; `B*(q) = ⌊q/2^128⌋`. Registered but **not measured**: `s_ℓ` (vanishing-slope spread).

## ZERO-POWER DECLARATIONS

- `F_COLL` at `a ∈ {3,4}` (ssparse's cells) has **zero power** over the official residual: the official ambient is `w* ≥ 2^39+2`, and the excess vanishes at `a ≥ 5` in every one of 1152 sampled configurations. This is a declaration against my own headline: if the `a ≥ 5` collapse is an `N ≤ 32` artifact, the transport argument falls with it.
- Every `q=17` number is a small-field control (`D = F_q^*`, `m=1` forced); no structural claim rests on it. Two-field confirmation `{97, 65537}` for every structural claim; `N ∈ {16,32}`.
- The sporadic `q`-decay is a **mean over `W`** and has zero power over the existence of a single bad `W`. T4 does not use it; route (b) was registered third and not executed for that reason.
- `F_COLL` is a max: it is exhaustive over lines within each cell, but **sampled over `W`** (64 random `W` per cell in the decay runs, 3 rotation classes at ssparse's cell, one deterministic `V` in the sweep). The claim "`F_COLL = s+1` for `a ≥ 5`" is therefore *measured-exhaustive per cell, sampled over cells*.

## COMPLIANCE

Registrations (R0–R8, including the cell grid, the candidate structured-family list, the D3 route order (a)→(c)→(b), predictions P1–P13 with numeric windows, and the zero-power declarations) were appended to `PREREG.md` with the **Edit tool before any interpreter invocation**; no post-registration addenda were needed. **QUARANTINE held totally**: `notes/pilots_20260802/CAMPAIGN_LEDGER.md` was never opened at any line, and the three round-29 sibling directories (`list_profile_bound`, `k_extremal`, `slack_recursion`) were never read or listed; **no subagents were spawned**, so the clause needed no propagation. **COMPUTE LAW**: every one of the 12 interpreter invocations ran as `tools/ramguard tiny|local -- python3 …` from the repo root with `RAMGUARD_TIMEOUT` set explicitly (120, 180, 200, 280, 290, 560) — **no exceptions, including the one-liners and the sanity tables**; all authoring used Write/Edit; all other work was grep/ls/sed/md5sum. **BANKED SCRIPTS**: `d5_sporadic.py`, `d2_sparse.py`+`ffield.py`, and `d2_scan.py` were copied to the session scratchpad and md5-verified against the originals before running; both escape replays reproduced identically and the originals were never executed in place or modified. **RAM DISCIPLINE**: file-at-a-time reads, `dag.json` never opened, no bulk loads, the line census written to hold `O(M)` memory rather than a global line dictionary, four long runs backgrounded to results files, one wall-hit re-scoped (the `N=32` `(9,4)` cell dropped rather than extended, disclosed). **DRAFT-ONLY**: every write is inside `notes/pilots_20260810/collinearity_object/` (3 scripts + 4 results files + PREREG) plus the session scratchpad; no `dag/`, `critical/`, `background/`, `nodes/` or `tools/` edits; no git; no Modal; stdlib only. Own-repo grep (CATCH-24A) was run before every novelty claim and produced one live subtraction (the dihedral family). Two-field confirmation used for every structural claim; 2-power grids (`N ∈ {16,32}`, `q = 65537 = 2^16+1`, 64 random `W`) where the grid was mine.
