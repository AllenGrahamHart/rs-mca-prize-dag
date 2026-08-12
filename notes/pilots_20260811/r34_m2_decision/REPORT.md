Greps done — the reduction I used is partly banked (`endpoint_rational_normal_kernel_curve`), and the Kummer route is already excluded at the official endpoint. Writing the report.

Here is the full REPORT text.

---

# REPORT — r34_m2_decision (round 34)

## VERDICT (first)

**(SAT3) IS NOT REALIZABLE ANYWHERE I COULD REACH AT m = 2 — and this is a FIELDS-SEARCHED NEGATIVE, NOT A THEOREM.** The decisive experiment ran; every layer of it failed in the same direction, and the failure has a *mechanism*, not just a rate:

1. **The combinatorial layer is free and is not the constraint.** The simple design is **unique up to isomorphism** (420 labelled, 1 iso class — `d1_results.txt`), exactly the brief's `K_9 - (P_3 + 3K_2)`; multigraph designs exist in the tens of thousands.
2. **The curve layer never opened.** The brief's 62×24 system had rank **24 (full) in 400 random and 200 structured `(G,X)` draws over two fields** — never the ≤ 23 needed for a curve to exist.
3. **The forward search decayed exactly at the random-polynomial rate, with zero structural enhancement.** 480,000 nets (240k per field) that *already carry three totally-split members by construction* reached **max n7 = 4** at `q=97` and **3** at `q=193`, against the **8** that the design provably forces. The measured cost of the 4th split member, `8.8e-6`, matches the naive "a random degree-7 polynomial splits over a 32-set" rate `q·C(32,7)/q^7 ≈ 4e-6` to within a factor 2. **The net structure buys nothing.**
4. **The symmetry escape hatch (round 33's G4) is classified and closed.** At `m = 1` the Kummer family works because `e = 1` forces the locator sets to be **pairwise disjoint** and group cosets are exactly that. At `m = 2` the design forces 31 of the 36 slope pairs to **share** a point, and orbits are equal or disjoint — so the coset mechanism is *structurally* unavailable (and dies precisely where round 31's banked R4 fence `T·rho <= N` dies: `63 > 32`). What remains — symmetries that *move* the members — is finite and I enumerate it: **only cyclic orders `k ∈ {2,3}` can host the design at all**, i.e. the maximum concentration factor is 3, so a symmetric witness still needs ≥ 3 independent splitting events at ~`10^-5` each.
5. **A NEW, SHARPER GATE THAN (SAT3) ITSELF.** The locator curve is only half the object; it must also be the kernel of a *real* syndrome Hankel pencil, which is the coefficient-chain system `M(Z)Q_Z = 0` — **`(m+2)(4m+1)` equations on `16m` unknowns, overdetermined by `4m^2-7m+2` = `-1, +4, +17, +38, ...`**. **`m = 1` is the only `m` at which it is underdetermined** — which is exactly why round 33's `m=1` search succeeded on *all sixteen* families. At `m = 2` I found **zero non-degenerate solutions in 2,800 structured and random curves over two fields**: every apparent hit was the same degenerate family (generic rank **1**, a fixed domain factor, `s ≠ 0`), whose rate I predicted and confirmed on two fields (`1.58%` vs `1.43%` at `q=97`; `0.79%` vs `0.71%` at `q=193`).

**So the deliverable is not "m=2 is negative". It is: `T = rho+2` at `m=2` now needs a `(SAT1)`-profile object with `e = m = 2`, and NOBODY HAS EVER EXHIBITED ONE — not round 33 (every `m>=2` object it built had `e=1`), not me.** That is a sharper, more tractable question than (SAT3), it is stated as an exact linear-algebra problem, and **proving it empty for `m >= 2` would close the strict endpoint outright.**

**(TCAP-DIM)'s boundary moves from 2 to 1** — but on a *corrected* ledger, not on my search: the posed count omits the automorphism group that acts on every solution. **Corrected excess at `m=2` is `+3` to `+5` (unrealizable-expected), while `m=1` stays `-9` to `-7` and the `e=1` ladder stays negative at every `m` — both of round 33's positive controls preserved, and only `m=2` flips.**

**F1 did NOT fire and could not: no witness, so no `a*` to measure. Zero power (pre-declared Z3).**

---

## MISSES FIRST

1. **My registered P8(b) ("the locator curve `C` cannot be rational", 0.55) rests on an argument I later found to be WRONG, and I am reporting the refutation of my own reasoning rather than the claim.** I had argued: if `C` were rational with parameter `t`, hyperelliptic involution `sigma`, and `Z = psi(t)` of degree 7, then each fibre `psi^{-1}(g)` would be `sigma`-invariant, forcing `A - gB` and `A(-t) - gB(-t)` proportional for ≥ 8 slopes, hence `psi` even, hence `deg psi` even — contradiction with 7. **The premise is false.** The design does *not* make each fibre invariant; it makes the **union** `S = psi^{-1}(G)` invariant (the two roots over a saturated `x` are `a` and `b`, two *different* slopes). The correct consequence is only a product identity `prod_g (A-gB) = c·prod_g (Ã-gB̃)`, which is far weaker and which I cannot close. **P8(b) is withdrawn, not resolved.**
2. **My headline "the naive count is refuted at the (L2) layer" was itself wrong, and I caught it only in the certification pass.** `d1_results.txt` shows a structured ansatz realizing at ~1.4%, versus the naive codim-5 (`~q^-5 ≈ 10^-10`) prediction — I briefly treated that as a live refutation of my own ledger. `d4_results.txt` then showed **all** of those solutions have generic rank **1**, not `rho = 7`: they are weight-one-error pencils arising when `Q_0, Q_1, Q_2` share a domain root, i.e. `s != 0`, which `(SAT1)` (`statement.md:13`) explicitly forbids. The naive count survives; my premature reading of the raw rate did not.
3. **The symmetry classification my SCRIPT PRINTED is cruder than the one I report, and the results file carries the crude version.** `d3_results.txt` prints "the only symmetry order that can host the design is k=2", derived from an orbit table that (i) omits the domain constraint `|U| ∈ {31,32}` and (ii) assumes fixed-slope members have `u ≡ 0 (mod k)`. The correct constraint is `u ≡ 0 or 1 (mod k)` (the fixed point of the `x`-action may itself be a root), and with the domain constraint added the answer is **`k ∈ {2,3}`**, not `{2}`. The hand-corrected classification is in D3 below; the file is superseded on this line and I flag it rather than silently quoting the better number.
4. **Two of my eight interpreter runs died under the guard.** The design enumeration allowed block-pair multiplicities up to 7 and exploded; the first run hit `MemoryError` inside ramguard's 1G ceiling, the second a `SystemError` from the same recursion. Fixed by capping multiplicity and the solution count. The guard did its job; the bug was mine, and it means my multigraph enumeration is **capped, not complete** (">60000 labelled" is a floor, and I do not report its iso-class count).
5. **The `k=8` monomial family produced `n7 = 0` in every one of ~1,800 nets, which is BELOW the random rate, and I do not know why.** Expected ≈ 4 hits per field on a naive splitting heuristic. Trinomial Galois structure is the obvious suspect; I did not test it. So my "symmetry concentrates split members" mechanism was demonstrated by the `k=4` family (`n7 = 8` at `q=193`, `d3_results.txt`) and *not* by the `k=8` family that motivated it.
6. **I never exhibited a single genuine `(SAT1)`-profile object at `m = 2`, so my `T` distribution at `m=2` is EMPTY, not small.** Every statement I make about "how large `T` gets at `m=2`" is about the *locator layer only* (`n7 <= 4` measured, `n7 = 8` for a symmetric net with no pencil). I have **no** measurement of `T` on a real `m=2` syndrome pencil with `e = 2`. That is the round's biggest hole and it is why D2's positive branch is unreachable rather than refuted.
7. **My search is a slice, and a thin one.** The locator layer has ~40 free parameters; I sampled two scalars over 480,000 draws with the three prescribed root sets random, plus ~9,000 symmetric nets, plus 2,800 realization tests. `C(32,7)^3 ≈ 4e19` configurations exist at fixed `D`, and `D` itself is free. **Nothing here exhausts anything** except the design enumeration (L0) and the exact witness detector's *logic*.
8. **The reduction I used is BANKED, not mine** (`background/nodes/rate_half_ca_hankel_endpoint_rational_normal_kernel_curve/statement.md:26-40`: the parameter forms `Q_0..Q_m` are independent and `nu_Q` is a degree-`m` rational normal curve with hyperplane sections `H_x`). My "net + conic + incidence graph" *is* that node at `m=2`. See CATCH-24A.
9. **The `(L2)` gate I am promoting is the campaign's own named next gate, not a discovery.** `endpoint_rational_normal_kernel_curve/claim_contract.md:22` and `endpoint_component_defect_localization/claim_contract.md:19` both say "Next exact gate: exploit the Hankel/apolar coefficient chain". What is new is the **count** and the `m=1`-vs-`m>=2` sign change, not the instrument.
10. **`P3` (F1 at 0.35) was unexercisable and I registered it knowing the premise might not arrive.** With no witness, F1 is untested for the **third** round running.

---

## CATCH-24A — own-repo subtraction, run BEFORE every claim

Greps run with search-level `--exclude-dir='r34_*' --exclude-dir='prize-codex-*' --exclude-dir='pilots_20260802'` over `background/`, `critical/`, `notes/pilots_20260810/`, `notes/pilots_20260811/`.

| object | in-repo prior | verdict |
|---|---|---|
| the locator curve as a **degree-`m` rational normal curve** `nu_Q` with domain hyperplanes `H_x` | `background/nodes/rate_half_ca_hankel_endpoint_rational_normal_kernel_curve/statement.md:26-40` (PROVED) | **BANKED. My net/conic picture at `m=2` is this node specialized.** I add only the `m=2` incidence graph and the search. |
| pencil shape `(4m+1) x 4m`, generic rank `4m-1`, primitive generator of parameter degree `m`, unique right Kronecker block `L_m` | same node, `statement.md:15-17`; `claim_contract.md:3-6` | **banked**; my conventions match the campaign's exactly (verified against the round-33 code I replayed) |
| "exploit the **Hankel/apolar coefficient chain**" as the next exact gate | `rate_half_ca_hankel_endpoint_rational_normal_kernel_curve/claim_contract.md:22`; `rate_half_ca_hankel_endpoint_component_defect_localization/claim_contract.md:19`; `rate_half_ca_hankel_endpoint_separated_pullback_exclusion/claim_contract.md:18` | **banked as an INSTRUMENT and as the named gate.** New here: its exact size `(m+2)(4m+1)` vs `16m` and the sign change at `m=2`. |
| coefficient-chain technique itself | `rate_half_ca_hankel_a1_first_degree_core_one_marked_source_frame/claim_contract.md:6`; `..._quadratic_gap_four_minimum_pair_bidirectional_heavy_incidence_localization/proof.md:9` | banked (A=1 lane, different matrix size) |
| **Kummer / separated-variable models excluded** at the official endpoint | `background/nodes/rate_half_ca_hankel_endpoint_separated_pullback_exclusion/statement.md:52` (PROVED): "This includes polynomial separated-variable and Kummer pullback models" | **BANKED AND PROVED — at `m=2^37`.** My `m=2` coset-mechanism exclusion is a different (elementary, incidence-budget) argument at a different `m`; it does **not** extend that theorem, it agrees with it. |
| `d_x <= e = m` | `rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md:49-50` | banked; spine of the whole reduction |
| deficit identity `sum_x (m-d_x) = 1+O`, `(SAT4)`; `O <= delta`, `(SAT2)`; failure size `T=rho+2`, `(SAT3)` | same, `:53`, `:33`, `:40` | banked |
| `T*rho <= N` fence, vacuous for `m>=2` (R4) | `notes/pilots_20260810/rh_type2_stratum/REPORT.md:30`, quoted in `notes/pilots_20260811/rh_sat3_realizability/REPORT.md:78` | **banked — and it is the exact reason the coset mechanism dies at `m>=2`.** My contribution is only to notice that the two facts are the same fact. |
| `(SAT3)` realizable at `m=1`, exhaustive at `q=17`, 16 families | `notes/pilots_20260811/rh_sat3_realizability/REPORT.md:30`, `d1_m1_results.txt`, `d2_realize_results.txt` | **banked — and REPLAYED BIT-IDENTICALLY by me** (see COMPLIANCE) |
| (TCAP-DIM) and its `m<=2` conjecture, `excess = 12m^2-24m-1-O` | `notes/pilots_20260811/rh_sat3_realizability/REPORT.md:190-200` | banked (POSED); **my correction to it is the novel part** |
| **quotienting a moduli count by the automorphism group acting on solutions** | greps for `orbit dimension`, `modulo automorphism`, `quotient by the group`, `PGL_2 orbit`, `automorphism group … dimension count` over `background/`, `critical/`, `notes/` returned **NOTHING** | **claimed as new IN THIS REPO.** It is textbook moduli bookkeeping elsewhere; the claim is only that (TCAP-DIM) omitted it. |
| **the exact size of the realization layer, `(m+2)(4m+1)` vs `16m`, and `m=1` as the unique underdetermined case** | greps for `realization system`, `16m unknowns`, `overdetermin` in the `ca_hankel` lane returned only the A=1-lane left-kernel overdetermination (`xr_split_pencil_maxwell_core_extraction/statement.md:46`) — a different object | **claimed as new in this lane** |
| **the cyclic-symmetry orbit classification (`k ∈ {2,3}` only)** | greps for `equivariant`, `mu_k-orbit`, `coset of mu` returned only the separated-pullback node and unrelated lanes | claimed as new; **low confidence that it is new anywhere**, and it is elementary |
| naive dimension counts fail | `background/nodes/pb_design_ceiling/proof.md:125` | banked; quoted against **my own** ledger, and MISS 2 is a live instance |

---

## D1 — THE SEARCH, PROPERLY STRUCTURED

Round 33 posed this as "40 parameters vs 39 rank conditions". That framing is right but incomplete: a witness must clear **three** layers, and the brief's 62×24 system is only the middle one.

### D1.0 The layers, and the exact witness detector

For `m=2`: `rho=7, N=32, R=16, r=7, A=R+1-2rho=3, e=m=2, s=0, delta=m-1=1, T=rho+2=9`. The locator curve is the net `F(Z,x)=c_2(x)Z^2+c_1(x)Z+c_0(x)` (`deg c_i <= 7`, 24 coefficients), member at slope `g` is `P_g = c_2g^2+c_1g+c_0`.

- **(L0) combinatorial.** `sum_g u_gamma = T*rho - O = 63 - O` incidences on `N=32` points with `d_x <= e = 2` gives a 31-edge multigraph on 9 vertices with degrees `7^8,6`.
- **(L1) curve-from-design.** Each edge `{a,b}` at `x` gives `c_1(x) = -(a+b)c_2(x)`, `c_0(x) = ab·c_2(x)`: 62 equations, linear in the 24 coefficients. A curve exists **iff** rank ≤ 23.
- **(L2) pencil-from-curve.** `M(Z)Q_Z == 0` with `M(Z)=M_r(y_0)+ZM_r(y_1)`: `(m+2)` blocks of `(R-r)=(4m+1)` rows on `2R=16m` unknowns.

**THE EXACT WITNESS DETECTOR (this is what makes the search finite rather than heuristic).** A 9-set with 31 edges has 62 endpoints among 9 vertices of degree ≤ 7, so **at least 8 slopes must have degree exactly 7**. Therefore

> `n7(net) := #{ g in P^1 : P_g splits into rho=7 distinct roots in D }`, and **`n7 <= 7` is an EXACT certificate that a net cannot host the design** — no maximisation over 9-subsets is needed, and no heuristic enters.

`n7` is the *bottleneck functional*, and it is precisely round 33's "totally split members" instrument, ported from `e=1` pencils to `e=2` nets.

### D1.1 (L0) — the design layer is free (`d1_results.txt`)

| family | labelled solutions | iso classes |
|---|---|---|
| SIMPLE (blocks meet in ≤ 1 point) | **420** | **1** |
| multiplicity ≤ 2 | > 60000 (capped, MISS 4) | not counted |
| multiplicity ≤ 3 | > 60000 (capped) | not counted |

The unique simple class is the brief's `K_9 - (P_3 + 3K_2)`; degree check `[7,7,7,7,7,7,7,7,6]` printed. **P6 resolved YES on uniqueness and YES on multigraphs existing.** The combinatorial layer is not the binding constraint (P6c hit).

### D1.2 (L1) — the 62×24 system never dropped rank (`d1_results.txt`)

| field | draws | rank histogram | needed |
|---|---|---|---|
| `q=97` random `(G,X)` | 200 | `{24: 200}` | ≤ 23 |
| `q=193` random `(G,X)` | 200 | `{24: 200}` | ≤ 23 |
| `q=97` structured (`mu_9` slopes; AP slopes+points) | 50 | min rank 24 | ≤ 23 |
| `q=193` structured | 50 | min rank 24 | ≤ 23 |

**P2 HIT (0.93):** the layer is generically full rank. **P2b resolved NO** at this sample size: no structured `(G,X)` dropped it.

### D1.3 (L2) — the layer the brief did not count, and the sharpest fact in this report

```text
 m | rho | N  | R  | eqs=(m+2)(4m+1) | unknowns=16m | over = 4m^2-7m+2
 1 |   3 | 16 |  8 |              15 |           16 | -1
 2 |   7 | 32 | 16 |              36 |           32 | +4
 3 |  11 | 48 | 24 |              65 |           48 | +17
 4 |  15 | 64 | 32 |             102 |           64 | +38
 5 |  19 | 80 | 40 |             147 |           80 | +67
 6 |  23 | 96 | 48 |             200 |           96 | +104
```

**`m = 1` is the only `m` at which a realization is guaranteed.** Round 33's own docstring records this without drawing the consequence: "3(R-r) = 15 linear equations on 2R = 16 unknowns, so a nonzero solution ALWAYS exists at these parameters" (`rh_sat3_realizability/d2_hankel_realize.py:8-10`). That single inequality is why its exhaustive `m=1` scan found **all sixteen** locator families realizable. At `m>=2` the inequality reverses.

Measured (60 random curves per cell, two fields, `d1_results.txt`):

| field | `m` | nullity histogram |
|---|---|---|
| 97 | 1 | `{1: 58, 2: 2}` |
| 193 | 1 | `{1: 60}` |
| 97 | 2 | `{0: 60}` |
| 193 | 2 | `{0: 60}` |

**Analytic kill of the obvious `e=2` family** (checked by hand, confirmed by 440 scanned curves per field): for the Kummer-type `Q_Z(X) = X^7 + (alpha Z^2 + beta Z + gamma)` the leading `Z`-coefficient is the **constant** `alpha`, so `M_r(y_1)Q_2 = 0` forces `y_1[0..8] = 0`; block 3 then forces `y_0[0..7] = 0`; block 1 (`gamma y_0[i] + y_0[i+7] = 0`) then forces `y_0 = 0`. **The `e=1` Kummer family that carried round 33's ladder has no `e=2` analogue**: the leading parameter coefficient must itself be a degree-`rho` locator, not a constant.

---

## D2 — THE OUTCOME, CERTIFIED (the negative branch)

### D2.1 The forward search and its decay law (`d2_results.txt`)

Normalisation: three members are **prescribed split** at slopes `0, 1, infinity` (free by `PGL_2` on the slope line), so every net searched starts at `n7 >= 3`; the remaining freedom is two scalars and the three root sets (chosen with the design's pairwise intersections). For each domain point, `P_g(x)=0` is a **quadratic in `g`**, so a net's entire incidence structure costs `O(N)`.

**Positive control first (same machinery, `m=1`, `q=17`, `D=mu_16`):** 32,256 pencils, `n_split` histogram `{2: 15632, 3: 14560, 4: 2032, 5: 32}`, **MAX = 5 = rho+2 — REPRODUCED**, independently of round 33's code path.

**Main search, `m=2`:**

| field | nets | `n7` histogram | MAX `n7` | needed |
|---|---|---|---|---|
| `q=97` | 240,000 | `{2: 12196, 3: 227802, 4: 2}` | **4** | 8 |
| `q=193` | 240,000 | `{2: 6220, 3: 233780}` | **3** | 8 |

**The decay law, and why it is the whole story.** Cost of the 4th split member at `q=97`: `2/227802 = 8.8e-6`. The *naive* rate for an unstructured degree-7 polynomial to split over a 32-point domain is `q·C(32,7)/q^7 ≈ 4e-6`. **They agree to a factor of 2: the net structure provides no enhancement at all.** Contrast `m=1`, where the same step costs `2032/14560 = 14%` — a factor of `10^4` — because there the members are the **fibres of a rational map** and the domain points partition coherently. At `m=2` they are cliques in an essentially random pairing. **P7 HIT** (max ≤ 15 predicted at 0.75; observed 4), and the `q^-Theta(1)`-per-member law is confirmed on two fields (**P7b HIT**).

### D2.2 The symmetry families — round 33's G4, executed (`d3_results.txt`)

The only known way a structured family beats a dimension count here is a symmetry `F(zeta^s Z, zeta x) = zeta^t F(Z,x)`, which gives `S_{tau(g)} = zeta·S_g`: **one splitting event buys a whole orbit.**

| family | nets scanned | MAX `n7` | (L2) nullity of the best |
|---|---|---|---|
| `k=8` monomial (`q=97,193,257`) | 576 / 576 / 676 | **0** (MISS 5) | — |
| `k=4` (2-dim eigenspaces; not forced monomial), `q=97` | 3000 | 4 | 0 |
| `k=4`, `q=193` | 3000 | **8** | **0** |
| `k=4`, `q=257` | 3000 | 4 | 0 |

**The `k=4` family reached `n7 = 8` at `q=193` — exactly `rho+1`, the strict target, attained at the locator layer, via two orbits of 4 as the orbit arithmetic predicts. And it has NO syndrome pencil: (L2) nullity 0.** That is the mechanism in one line: symmetry concentrates split members and simultaneously sparsifies the parameter coefficients, and (L2) charges for sparsity.

### D2.3 The certification pass — the apparent (L2) hits are all degenerate (`d4_results.txt`)

| field | split-endpoint nets tried | nonzero realization | of those, `y_0=0` or `y_1=0` | generic-rank histogram of the rest (need `rho=7`) | **genuine `e=2, A=3` objects** |
|---|---|---|---|---|---|
| 97 | 700 | 10 (**1.43%**) | 21 | `{1: 39}` | **0** |
| 193 | 700 | 5 (**0.71%**) | 10 | `{1: 20}` | **0** |

**The degenerate family, identified and predicted on two fields.** A hit occurs precisely when `Q_0, Q_1, Q_2` share a domain root `x*` — then the weight-one error at `x*` has a rank-1 Hankel matrix whose 7-dimensional kernel swallows the whole net. Predicted rate `E[|S_0 ∩ S_2|]/q = (49/32)/q`: **1.58% vs 1.43% measured at `q=97`; 0.79% vs 0.71% at `q=193`.** These objects have a fixed domain factor, i.e. `s != 0`, which `(SAT1)` forbids (`saturation_rigidity/statement.md:13`), and generic rank 1, not `rho = 7`, i.e. not `A = 3`.

> **Consequence, and it is the round's most important sentence: I could not exhibit a single `(SAT1)`-profile object with `e = m = 2` at `m = 2` — not one, in 2,800 curves over two fields. Round 33 could not either (every `m>=2` object it built had `e=1`, `rh_sat3_realizability/REPORT.md:50`, a range `(ERC2)` already closes, `exceptional_root_charge/statement.md:70-73`). The nonemptiness of the strict `e=m` branch at any `m >= 2` is now an OPEN, EXACTLY-STATED, LINEAR-ALGEBRA question.**

I do **not** claim it is empty: the incidence count `23 + 32 - 36 = 19 >= 0` says the stratum should be nonempty and of codimension ~13 in `y`-space, which is exactly why sampling cannot reach it (`q^-13 ≈ 10^-26`).

### D2.4 What is exhausted vs what is sampled (demanded by the brief)

**EXHAUSTED:** (i) the simple-design iso classification (1 class, complete); (ii) the *logic* of the witness detector — `n7 <= 7` is an exact certificate, not a heuristic score; (iii) the admissible cyclic-symmetry orders (D3.2, a finite arithmetic classification); (iv) the analytic death of the `e=2` Kummer family.
**SAMPLED:** everything numerical — 480,000 nets, 2,800 realization tests, 400 curve-layer draws, ~9,000 symmetric nets, at `q ∈ {97,193}` (plus `257` for symmetry). **A fields-searched negative is not a theorem, and I say so in the verdict line itself** (MISS-2 guard clause (iii), honoured).

### D2.5 F1

**Not exercised.** F1 needs a realizable `T = rho+2` object to measure `a*` against `7m-1 = 13`; there is none. At `m=2` the window `[?, 2rho=14]` really is non-degenerate — the test is *available* for the first time — but the premise never arrived. **Zero power (Z3).** Third round running.

---

## D3 — THE TCAP BOUNDARY

### D3.1 The corrected ledger (`d1_results.txt`)

(TCAP-DIM) counts `params = 23(curve) + (4m+1)(slopes) + 16m(domain)` against `conds = T*rho - O`, and **does not quotient by the group that acts on every solution**: `x -> ax+b` on the domain and `gamma -> alpha*gamma+beta` on the slope line (dim 4), and generically the full `PGL_2 x PGL_2` (dim 6). The action has **finite stabilisers** — a positive-dimensional subgroup would have to fix 9 slopes and 32 points, hence be trivial — so every nonempty solution set has dimension **≥ 4 (≥ 6 generically)**, and an expected dimension below that is self-inconsistent.

| `m` | (TCAP-DIM) excess | corrected (+4) | corrected (+6) | verdict (+6) |
|---|---|---|---|---|
| 1 | −13 | −9 | **−7** | realizable-expected |
| 2 | **−1** | **+3** | **+5** | **UNREALIZABLE-expected** |
| 3 | +35 | +39 | +41 | unrealizable-expected |
| 4 | +95 | +99 | +101 | unrealizable-expected |

**Both of round 33's positive controls survive the correction:** `m=1` (PROVED realizable, exhaustively) stays negative; the `e=1` ladder (`excess = -8m-7`, realizable and measured at two fields per cell for `m=1..4`) stays negative at every `m` (`-8m-1`). **Only `m=2` flips.** An independent bookkeeping of the *same* correction, on the locator layer alone — unknowns `32 points + 9 lambda + 9 slopes = 50`, conditions `6 slopes x 8 coords = 48`, symmetries `1+3+3 = 7` — gives **excess `-5` at `m=2`** and **`+7` at `m=1`**, agreeing in sign with the table. **P5 HIT** (predicted `+3..+5`; got exactly `+3`/`+5`), and **P5b resolved NO** — no in-repo prior for the correction.

**Status of (TCAP-DIM): the conjecture "realizable iff `m <= 2`" should be re-posed as "realizable iff `m = 1`", and the `m=2` cell moves from *marginal* (`-1`) to *expected-empty* (`+3..+5`).** It remains a **heuristic with the `pb_design_ceiling/proof.md:125` blind spot** (Z2), and MISS 2 is a fresh instance of that blind spot biting inside this very report.

### D3.2 The symmetry classification (corrected by hand; supersedes the printed line in `d3_results.txt`, MISS 3)

Let a cyclic group of order `k` act on the `x`-line with the net invariant. Its induced action `tau` on the slope line is a Möbius map of the same order, so the 9 supported slopes split into `tau`-orbits of size `k` plus at most **2** fixed slopes. A fixed slope's member satisfies `f(zeta x) = nu f(x)`, hence `f = x^j h(x^k)`: its nonzero roots come in full `mu_k`-orbits, so `u_gamma ≡ 0 or 1 (mod k)`. The union `U = ∪_g S_g` is invariant with `|U| ∈ {31,32}`, so `|U| ≡ f (mod k)` with `f <= 2` fixed points of the `x`-action inside `U`.

| `k` | slope side `9 = A·k + F, F<=2` | fixed-slope `u ∈ {7,6}`, `u ≡ 0,1 (mod k)` | domain `|U| ∈ {31,32}` | verdict |
|---|---|---|---|---|
| 2 | `4·2+1` ✓ | `7≡1` ✓, `6≡0` ✓ | 31 (f=1) / 32 (f=0,2) ✓ | **ADMISSIBLE** |
| 3 | `3·3+0` ✓ | not needed | `31≡1`, `32≡2` ✓ | **ADMISSIBLE** |
| 4 | `2·4+1` ✓ | `7≡3` ✗, `6≡2` ✗ | — | dead |
| 5,6 | `F>=3` ✗ | — | — | dead |
| 7 | `1·7+2` ✓ | `7≡0` ✓ | `31≡3`, `32≡4` ✗ | dead |
| 8 | `8+1` ✓ | `7≡7` ✗, `6≡6` ✗ | — | dead |
| 9 | `9+0` ✓ | not needed | `31≡4`, `32≡5` ✗ | dead |
| ≥10 | `F=9>2` ✗ | — | — | dead |

> **Only `k ∈ {2,3}`. The maximum concentration factor is 3, so a symmetric witness still needs ≥ 3 independent splitting events at the measured ~`10^-5` each.**

**And the `m=1` mechanism is excluded outright at every `m>=2`.** Round 33's Kummer family works because `tau = id` (every slope fixed) and each `S_g` is a single `mu_rho`-coset. Distinct cosets are **disjoint**, and equal cosets force the members proportional, hence the net 2-dimensional, hence every shared point a fixed point of the pencil, i.e. `s != 0`. So `tau = id` forces `d_x <= 1`, i.e. `sum_x d_x <= N`, i.e. `T*rho <= N` — **which is exactly round 31's banked R4 fence, true only at `m=1`** (`rh_type2_stratum/REPORT.md:30`). `63 > 32` kills it at `m=2`. This agrees with, and does not extend, the PROVED separated-pullback exclusion at the official endpoint (`endpoint_separated_pullback_exclusion/statement.md:52`).

### D3.3 `m = 3` (calibration only, Z4)

`rho=11, N=48, T=13, e=3, delta=2`; incidences `143 - O` against a budget `3·48 = 144` — tight in the same way. Corrected ledger `+39/+41`. Realization layer overdetermined by `4·9-21+2 = +17` (vs `+4` at `m=2`). The brief asked for an `m=3` attempt only if `m=2` came out positive; it did not, so I report the arithmetic and stop. **Expected infeasible, and the structure that makes it infeasible is the same one, four times stronger.**

---

## D4 — VERDICT

> **THE `m`-BOUNDARY OF RECORD: `(SAT3)` is realizable at `m = 1` (PROVED, round 33, replayed bit-identically here) and NOT realizable at `m = 2` anywhere I could reach — a FIELDS-SEARCHED NEGATIVE at `q ∈ {97,193,257}` with an exact certificate at the design layer, a mechanism at the symmetry layer, and a corrected ledger that now expects emptiness. (TCAP-DIM)'s boundary moves from `m<=2` to `m<=1`. THIS IS NOT A THEOREM.**

Ranked by what it changes:

1. **The real gate is now `(L2)`, not `(SAT3)`.** `(m+2)(4m+1)` vs `16m`, overdetermined by `4m^2-7m+2`, negative only at `m=1`. **Nobody has ever exhibited a `(SAT1)`-profile pencil with `e=m` at any `m>=2`.** Proving that stratum empty for `m>=2` would close the strict endpoint — and it is a finite, exactly-stated linear-algebra question about Hankel pencils with prescribed Kronecker minimal index, which is precisely the "coefficient chain" gate three endpoint nodes already name as next.
2. **`m=1` is not a small case, it is a different mechanism.** Disjoint locator sets (`e=1`) are group cosets; overlapping locator sets (`e>=2`) cannot be. Every structured family that ever worked in this campaign used the coset mechanism, and the coset mechanism is dead for `m>=2` by an incidence budget that is already banked (R4).
3. **The regression-test principle sharpens.** Round 33: a proof of the strict target must fail at `m=1`. Round 34 adds: **it must also explain why the failure at `m=1` is the disjointness of `e=1` locator sets** — any argument that does not turn on `d_x <= e` overlap is fighting the wrong object.
4. **F1 stays unexercised, and `(NEWCAP)`, the `9/4`, the `7/4` ledger and FR-canonical are untouched.** Nothing in this round bears on them.

**Handoff, in priority order.** (1) **Settle `(L2)` nonemptiness at `m=2`**: does a `(4m+1) x 4m` Hankel pencil with minimal index exactly `m`, generic rank `4m-1`, and `s=0` exist? Construct one or prove none exists; either answer is worth more than another `(SAT3)` search. (2) If one exists, feed it to my `d2_forward.py` machinery and measure its `T` — that is the first real `m>=2` measurement the campaign would have. (3) Re-pose (TCAP-DIM) with the automorphism quotient and re-price the `m=2` cell as expected-empty. (4) Do **not** spend more compute on unstructured `(SAT3)` search at `m=2`: the decay law is measured and it is the random-polynomial rate.

---

## PREDICTIONS vs OUTCOMES

| registered | outcome |
|---|---|
| **P1** P((SAT3) realizable at `m=2`) = 0.10; found this round = 0.05 | **no witness; consistent with the prior, and the prior is now lower** — but a negative search does not confirm P1 (Z1) |
| **P2** linear layer full rank for random `(G,X)` = 0.93 | **HIT** — `{24: 200}` on both fields |
| **P2b** structured `(G,X)` drops rank = 0.25 | **resolved NO** at 100 structured draws |
| **P2c** rank ≤ 23 *with a realizing kernel* = 0.05 | **resolved NO** |
| **P3** F1 fires given realizable = 0.35 | **UNEXERCISED** — no premise; zero power |
| **P4** `m=3` realizable = 0.02 | untested by construction (calibration only) |
| **P5** corrected excess `+3..+5` at `m=2`, both controls preserved = 0.80 | **HIT, exactly** — `+3` (affine) / `+5` (projective); `m=1` and the `e=1` ladder both stay negative |
| **P5b** the correction is already in-repo = 0.30 | **resolved NO** (greps in CATCH-24A) |
| **P6** simple design unique up to iso = 0.90 | **HIT** — 420 labelled, **1** class |
| **P6b** genuine multigraph designs exist = 0.60 | **HIT** — thousands (capped enumeration, MISS 4) |
| **P6c** combinatorial layer not binding = 0.92 | **HIT** |
| **P7** max score ≤ 15 = 0.75 | **HIT** — max `n7 = 4` |
| **P7b** `q^-Theta(1)` decay per extra member = 0.85 | **HIT** — and quantified: the decay equals the *unstructured* rate |
| **P8a** irreducibility of `F` over `F_q(x)` = 0.75 | **HIT (proved).** If `F = c_2(Z-u)(Z-v)` with `deg u = d_1, deg v = d_2`, the four constraints `deg c_i <= 7` force `d_1+d_2 <= 7`, so saturated points `<= 9·min(d_1,d_2) <= 27 < 31`. Both `d_i >= 1` (a constant root would make one member identically zero). |
| **P8b** `C` cannot be rational = 0.55 | **WITHDRAWN — my argument was wrong** (MISS 1) |
| **P8c** class condition `9K ~ 31h + p_0`, codim `genus-1` = 0.45 | **survives as POSED, unverified.** Set-level `iota`-invariance of `psi*(G)` gives `9K ~ 31h + p_0`; the codimension reading is heuristic and I ran no computation on it. |

---

## ZERO-POWER DECLARATIONS

1. **`q ∈ {97,193,257}` has zero power over `q ~ 2^128`-scale fields and zero power over the *existence* question at `m=2`.** Negative searches at these sizes cannot exclude a codimension-5 (let alone codimension-13) stratum.
2. **Every dimension ledger here — mine and (TCAP-DIM)'s — is a heuristic** with the `pb_design_ceiling/proof.md:125` blind spot, and MISS 2 is a documented instance of that blind spot inside this report. No ledger has standing as a bound.
3. **F1 and `(NEWCAP)`: zero power.** No `T = rho+2` object at `m=2` was produced, so `a*` was never measured against `7m-1 = 13`.
4. **`m=3` work is calibration only.**
5. **The "0 genuine `e=2` objects" result has zero power to prove emptiness.** The stratum's expected codimension in `y`-space is ~13; 2,800 samples is `10^-23` of what would be needed.
6. **`n7 <= 4` is a max over a sample of 480,000 nets in a ~40-parameter space, not a bound on `n7`.** MISS-2 guard clause (i) honoured: I do not convert it into any statement about the true maximum.
7. **The multigraph design count is capped, not complete** (MISS 4).

---

## MEASURED FUNCTIONALS (CATCH-19C)

`m, rho=4m-1, N=16m, R=8m, r=rho, A=R+1-2rho, e, s, delta=m-1`; per slope `u_gamma` and the incidence degree; `O = sum(rho-u_gamma)`; per point `d_x`; deficit `sum_x(m-d_x)`; saturated-point count; `T` (finite supported slopes, from the kernel of `M_r(y_0+g y_1)` at every `g ∈ F_q`); generic rank `max_g rank M(g)`; existence of a degree-`<=1` kernel (the `e<=1` filter); `w* = a* = min_{g!=g'}|S_g ∪ S_{g'}|`; rank of the 62×24 curve layer; nullity of the `(m+2)(4m+1) x 16m` realization layer; **`n7` = totally-split members of a net (new here as the exact witness detector)**; the `mu_k`-coset pattern of a split root set; the `n7` decay rate per extra member. **Registered but not measured: `T` on any genuine `m=2, e=2` object (none exists — MISS 6); `a*` at `m=2` (same reason); the iso-class count of multigraph designs (capped — MISS 4).**

---

## COMPLIANCE

**Registrations.** R0, P1–P8 (with numeric windows), the MISS-2 mean-vs-max guard, four pre-committed zero-power declarations, a fixed route order and three falsifiers were appended to `PREREG.md` under "## Pilot registrations" with the Edit tool **after reading exactly the two named anchors and before any other read, any grep, and any interpreter invocation**. No post-registration addenda. The route order registered (design → L1 rank → forward search → structured families → ledger → verdict) was followed exactly; I did not reorder to chase a positive.

**Compute law.** **Eight interpreter invocations, every one of the form `tools/ramguard local -- python3 …` issued from the repo root with the literal `--`.** Six carried an explicit `RAMGUARD_TIMEOUT=290` (inside the `local` profile's 5-minute ceiling, not an extension); the two banked replays used the profile default. **No bare `python3` at any point, for any purpose** — no file patching, no probes, no empty heredocs; all file edits used Edit/Write, and the two `sed` call-site patches were shell text edits, not interpreter runs. Stdlib only; no third-party imports, no Modal, no network, no git, no subagents. **Ramguard status: six clean exits; two runs (the first two attempts at `d1_layers.py`) died INSIDE the guard on its 1G memory ceiling from my own unbounded design enumeration (MISS 4) — the guard contained them, and no host memory event occurred.**

**RAM discipline.** `dag.json` **never opened**. Node shards and grep only; the one large statement I needed beyond the anchors (`endpoint_separated_pullback_exclusion`) was read in a bounded `sed` window, and `endpoint_rational_normal_kernel_curve` in a `head`/`tail`/contract window. Each script holds `O(N^2 + q)` state and writes its own results file (`d1_results.txt`, `d2_results.txt`, `d3_results.txt`, `d4_results.txt`, plus the two replay files).

**Quarantine — clean, with search-level exclusion.** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` never opened, never traversed. **Every recursive grep carried `--exclude-dir='r34_*' --exclude-dir='prize-codex-*' --exclude-dir='pilots_20260802' at the SEARCH level`, not as output filtering** — the round-33 deviation (its MISS 8) is not repeated. No sibling `r34_*` directory was listed, opened, traversed, or read. No path containing `prize-codex-` was touched. The round-33 directory `notes/pilots_20260811/rh_sat3_realizability/` was read as explicitly permitted (`PREREG.md`, `REPORT.md`, `FABLE_AUDIT.md`, two scripts).

**Write scope.** Every write is inside `notes/pilots_20260811/r34_m2_decision/`: `PREREG.md` (registrations appended), `banked_d1_m1_exhaustive.py` + `banked_d2_hankel_realize.py` (copies of round-33 scripts, per the constraint to copy before running), `replay_d1_m1_results.txt`, `replay_d2_realize_results.txt`, `d1_layers.py` + `d1_results.txt`, `d2_forward.py` + `d2_results.txt`, `d3_structured.py` + `d3_results.txt`, `d4_certify.py` + `d4_results.txt`. **No `dag/`, `nodes/`, `critical/`, `background/` or `tools/` edits; no git operations; the session scratchpad was not used.** AUDIT-AND-DRAFT respected: nothing outside my directory was altered, and every claim above is posed for coordinator triage, not banked. **`REPORT.md` is not written** — the harness refuses subagent report files (confirmed by round 33, whose directory contains no `REPORT.md`), so per the brief's fallback clause this report is returned verbatim as my final message rather than written twice.

**Banked scripts and REPLAY IDENTITY (the gap round 33 declared).** I copied round 33's `d1_m1_exhaustive.py` and `d2_hankel_realize.py` into my directory and ran both under ramguard **before writing any code of my own**. Both outputs are **byte-identical** to the banked `d1_m1_results.txt` and `d2_realize_results.txt` (`diff` clean, both files). Round 33's `m=1` result therefore now carries independent replay evidence, and my conventions (`M_r(y)` shape, `D_r(D)`, `v_x`) are verified against the campaign's own code rather than re-derived. My `m=1` positive control in `d2_forward.py` reproduces `T = rho+2 = 5` from a **completely different code path** (quadratic-in-`g` incidence rather than pair enumeration).

**Method discipline.** CATCH-24A greps ran before every novelty claim and produced **five live subtractions, three of them load-bearing** (the rational-normal-curve reduction is BANKED and is my whole D1 picture; the coefficient chain is the campaign's own named gate; the Kummer/separated-pullback exclusion is PROVED at the official endpoint). Every quantifier claim carries a `file:line` or a results-file citation. Every max-quantified claim carries a zero-power declaration. Two-field confirmation for every structural claim (`q ∈ {97,193}` throughout, `257` added for the symmetry families). **MISSES FIRST**, and the round's three self-corrections — my withdrawn P8(b) argument, my premature "the naive count is refuted", and my own script's over-strong symmetry conclusion — are reported as falsifications of my own work, in that order, before any result.
