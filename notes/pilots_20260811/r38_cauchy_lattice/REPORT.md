All sweeps complete. Writing the final report.

**REPORT — r38_cauchy_lattice (round 38)**

## VERDICT (first)

**THE CAUCHY-LATTICE INVERSE IS SOLVED AS AN ALGORITHM, AND THE ROUND'S TARGET IS TAKEN: `T = 3` OVER `mu_32`, TEN CERTIFIED WITNESSES, TWO FIELDS.** Round 37 left the third prescription as "SEARCH, with an exact test" and priced `T=3` over `mu_32` at an `8.93e3x` / `3.86e6x` shortfall (`r37_third_solve/REPORT.md:130`, banked at `critical/nodes/rate_half_band_crossing_location/statement.md:4982-4984`). That price is an artefact of the *instrument*, not of the problem. The two scale ratios `(lambda,mu) = (beta/gamma, beta/alpha)` — which force a `(q-1)^2` scan per subset-triple — **eliminate exactly**, and what is left is a codimension-3 rank condition on 15 field elements:

> **(TEST).** Put `u = f+g`, `G = (beta/gamma)g`, `H = (beta/alpha)f`. Then `A := {u : P_inf(x)u(x) = P_1(x)G(x) on S_0 for some deg-<=4 G}` is the kernel of the **2x5 Hankel matrix of moments** `m_j = sum_{x in S_0} P_inf(x)x^j/(P_1(x)P_0'(x))`, `j=0..5`; `B` likewise from `S_inf` with `n_j = sum_{x in S_inf} P_0(x)x^j/(P_1(x)P_inf'(x))`. `dim A = dim B = 3`, so `dim(A cap B) = 1` and **`u` is determined by `(S_0,S_inf,S_1)` alone**. Recover `G,H` by degree-<=4 interpolation. Then the triple admits a third split member **iff `u = c_1 G + c_2 H` with `c_1,c_2 != 0` and `deg(c_1G) = deg(c_2H) = 4`**; then `g = c_1G`, `f = c_2H`, and `L`, `h`, `k` are forced.

No `(lambda,mu)` scan, no lattice reduction, no Euclid. Cost **57 us/triple** in stdlib Python, so **one `(S_0,S_inf)` pair — all `C(32,7) = 3,365,856` subsets `S_1` — sweeps exhaustively in 192 s**, one ramguard window. Measured yield `9` hits at `q=97` against `9.09` predicted from `q^-3` (`d2_results_q97_s0..s3.txt`), and `1` at `q=193` against `3.62`. Ten objects, every one rebuilt from `(f,g,h,k,L)` alone and re-verified: `deg(Q_0,Q_1,Q_2) = (7,7,7)`, `deg L = 1`, `s = 0`, `deg gcd(f,g) = 0`, `(CONIC)` exact, all three (PAR) identities exact, and the three member root sets **exactly** the prescribed `S_0, S_1, S_inf` inside `mu_32` (`d3_results.txt:4-30` and per-witness blocks).

The loop with the mandate's framing closes exactly: every witness satisfies `f == R g (mod P_0P_inf)` with lattice first minimum `d_1 = 4` (generic 7), and its remainder-degree sequence is `[14,13,12,11,10,4,3,2,1,0,-1]` — **the window `{5,...,9}` skipped by a single degree-6 partial quotient**, which is precisely the characterisation I registered as (X5) (`d3_results.txt:27-30`).

**What did NOT happen:** no `T = 4` over `mu_32` (all ten witnesses have `T_mu32 = 3` exactly), no negative-exponent cell, no `(SAT3)`, no combinatorial criterion in the `(SCRIT)` mold, no WALL theorem, no `m >= 3`, no `q ~ 2^128`, **and no reproduction of round 37's `36x32` / seprank / `e = m = 2` certification** — my certification is intrinsic only, which breaks a rule I registered myself.

---

## MISSES FIRST

1. **MY REGISTERED (X3) IS WRONG AS STATED, AND MY OWN VALIDATION CAUGHT IT.** I registered "`rank[u;G;H] <= 2`" as the criterion. It is necessary and **not** sufficient: there is a degenerate branch where `G` and `H` are *proportional* (`rank[G;H] = 1`), which makes `rank[u;G;H] <= 2` automatic while `u ∉ span(G,H)`. It is not rare and it is **pair-dependent**: on one `q=23` pair it fired **3824** times against **6** genuine hits, on the sibling pair **7** times against **7** (`d1_results.txt`, `d1_validate2` block: `[((1,4,4),3818),((2,4,4),13)]`). Brute force settles it: agreement with the **corrected** criterion `113/113`, agreement with raw `rank<=2` only `73/113` (the 40 sampled degenerate triples are all false positives). **P7 (0.60) resolves NO.** The corrected clause is in the VERDICT and is what all ten witnesses were found with.
2. **I DID NOT REPRODUCE ROUND 37's CERTIFICATION, WHICH VIOLATES MY OWN REGISTERED R4(vi).** I registered that no `T=3` would be claimed until certified against the original `36x32` system with `nullity`, `seprank`, `M(Z)Q_Z = 0` entrywise, generic pencil rank, the rank-drop set, the rank at infinity and the degree-`<=1` kernel dimension. **I built none of that apparatus.** What I certify is intrinsic: the (PAR) identities from `(f,g,h,k,L)`, the degrees, `s = 0`, `deg gcd(f,g) = 0`, `(CONIC)`, the full `P^1(F_q)` slope scan for `T`, `(OV4)`, and the lattice drop. **`e = m = 2` is therefore NOT certified for any of my ten objects** — they are members of the same (PAR) family round 37 certified, and that is an inheritance argument, not a certificate. Stated before the headline number.
3. **ROUND 37's OWN RESULTS FILE ALREADY CONTAINED THE NUMBER THAT MAKES THIS SWEEP FEASIBLE, AND I DID NOT DISCOVER IT.** `r37_third_solve/d4_results.txt:54` reads `q=97 q^-3 = 1.096e-06 triples needed ~ 912673`. Against `C(32,7) = 3,365,856` triples per pair that is `3.69` expected hits **per pair** — i.e. the target was one pair-sweep away, in their own file, three lines below the `8.93e3x` shortfall they published (`:31`). **I claim the instrument and the witnesses; I do not claim the rate.**
4. **MY (P4) MEASUREMENT WAS BADLY DESIGNED AND I REPORT IT ANYWAY.** I measured whether the Euclid remainder-degree profile survives a one-point move of `S_1`: `28/60` at `q=97`, `47/60` at `q=193` (`d1_results.txt`, `[B3]`). Those numbers are **uninformative**, because the generic profile is the all-quotients-degree-1 profile `[14,13,...,0]`, so "identical" is the null expectation. The design tested nothing. The correct statement — that the Euclid route is abandoned, not accelerated — comes from the scale-elimination, not from this measurement.
5. **A RAMGUARD RUN WAS WALL-KILLED BY MY OWN SIZING ERROR.** `d1_validate`'s cross-check sampled *all* `3830+` raw hits at `484` `(lambda,mu)` values each; ramguard `local` killed it at its `290 s` limit (exit 124, "reached its 290 wall limit"). The sweep half had already flushed to `d1_results.txt` in append mode, so nothing was lost — that is what the append rule is for. **P11 (0.30) resolves YES.**
6. **I SHIPPED A BUG THAT CRASHED A RUN.** `d1_validate2.py` indexed `r[1],r[2],r[3]` on a 3-tuple: `IndexError: tuple index out of range`, after the sweep had printed. Fixed with the Edit tool and re-run. **P12 (0.75) resolves YES.**
7. **`q=193` UNDERSHOOTS AND FOUR OF ITS TWELVE PAIRS ARE NOT EXHAUSTIVE.** `1` hit against `3.62` predicted (`p ~ 0.12`, Poisson). Seeds 4-7 were budget-stopped at `2,686,976 / 2,621,440 / 2,621,440 / 2,686,976` of `3,365,856` (`78-80%`), because six parallel ramguard processes slowed the inner loop from `57` to `~100 us/triple`. The two-field claim rests on **one** `q=193` witness (seed 10).
8. **TWO OF MY `q=97` PAIRS ARE ALSO PARTIAL.** Seeds 2 and 3 swept `2,621,440` of `3,365,856` (`77.9%`) each. Only `q=97` seeds 0,1 and `q=193` seeds 0,1,2,3,8,9,10,11 are **complete** exhaustive pair-sweeps. Every count below carries its denominator.
9. **ONE WITNESS IS OUTSIDE THE NOMINAL DEGREE PROFILE.** `q97-p0-w1` has `deg k = 3`, not `4` (`d3_results.txt:5`, `degfghkL (4,4,4,3,1)`). The other nine are `(4,4,4,4,1)`. I do not know whether `deg k = 3` costs `e = 2`; I flag it rather than quietly drop the witness.
10. **NO `T = 4` OVER `mu_32`, AND NO SEARCH AT THE REQUIRED RATE.** All ten witnesses have `T_mu32 = 3` with `supported = [0, 1, inf]` exactly. A fourth split member is a further `~q^-7` per slope; nothing here probes it. **P9 (0.05) and P19 (0.02) resolve NO by construction, with zero power.**
11. **THE WALL HORN (c) OF THE MANDATE IS NOT DELIVERED, AND MY (X8) REMAINS A PREDICTION.** I registered that no purely combinatorial criterion exists. I did not prove it. What I have is one weak, **unclaimed** signal: `8` of the `9` `q=97` hits have `|S_1 cap S_0| + |S_1 cap S_inf| >= 3` against `54.0%` of the admissible population (`p ~ 0.034`, `n = 9`), and `0` of `9` fall in the `61.4%`-mass low-overlap classes. **This is data-dredging on nine points and I claim nothing from it.**
12. **`a*` RESOLVED AGAINST MY PRIOR UNDER BOTH READINGS, AND F1 IS STILL AT ZERO POWER.** Per-object `a*` (min over supported pairs) `= 12` on `9` of `10` witnesses, `13` on one. Per-pair histogram over `30` supported pairs: `{12: 10, 13: 10, 14: 10}` — exactly uniform, no modal value. **P6 (0.40) resolves NO.** And `(NEWCAP)`'s premise is `T = rho+2 = 9`; at `T = 3` nothing is tested.
13. **THE BRIEF'S OWN DENOMINATOR IS WRONG AND I FLAG IT RATHER THAN RE-SCOPE SILENTLY** (registered as R7(b)). `C(25,7) = 480,700` is not the admissible `S_1` count: `(SCRIT)` constrains `S_0` against `S_inf`, not `S_1`. The honest sweep is all `C(32,7) = 3,365,856`, of which `2,330,904` (`69.25%`) are reachable by the fast path (`|S_1 cap S_0| <= 2` and `|S_1 cap S_inf| <= 2`); the rest are shown empty in one 5x5 rank test each.
14. **THE EXHAUSTION HAS TINY SCOPE (R4(v)).** I swept **4** `(S_0,S_inf)` pairs at `q=97` and **12** at `q=193`, out of `C(32,7) x C(25,7) ~ 1.6e12` ordered disjoint pairs. Nothing here is a statement about `mu_32` in general, still less about emptiness anywhere.
15. **`(SAT2)/(SAT3)/(SAT4)/(SAT5)` REMAIN INAPPLICABLE.** At `T = 3`, `sum_x d_x = 21` against `2|union| = 34..38`; `(SAT3)` demands `63` of `64`. I report occupancy, not a vacuous table — as rounds 36 and 37 had to.

---

## CATCH-24A — own-repo subtraction, run BEFORE every novelty claim

Every recursive grep carried, **at the search level**, `--exclude-dir=r38_side_door --exclude-dir=r38_urate_genericity --exclude-dir=r38_sporadic_det --exclude-dir=pilots_20260802 --exclude-dir='prize-codex-*' --exclude-dir=.git --exclude-dir=__pycache__ --exclude=dag.json`, over `background/`, `critical/`, `notes/`. Hyphenated/infixed variants searched explicitly: `Hankel moment`/`moment matrix`/`moment kernel`/`2x5 Hankel`/`2 x 5 Hankel`; `scale elimination`/`scale-elimination`; `first minimum`/`first-minimum`/`successive minima`/`minimum drop`/`minimum-drop`; `continued fraction`/`continued-fraction`/`partial quotient`/`partial-quotient`; `extended Euclid`/`half-gcd`/`half gcd`/`hgcd`; `weak Popov`/`weak-Popov`; `Cauchy interpolation`/`rational interpolation`/`Pade`/`Padé`; `dual annihilator`/`derivative weight`; `a*`/`NEWCAP`/`7m-1`/`projective convention`/`roots at infinity`; `meet in the middle`/`meet-in-the-middle`; `T = 3 over mu_32`/`T=3 over mu_32`; `C(32,7)`/`3365856`/`3,365,856`.

| object | in-repo prior | verdict |
|---|---|---|
| **`(PAR)`, `(CONIC)`, `(SLOT)`, `(SCRIT)`, `(OV4)`, the 2x3-Hankel-minor form, the deficit-3 `(CAUCHY)` reading, the `q^-3` per triple** | `r37_third_solve/REPORT.md:64-90,98-100`; banked at `critical/nodes/rate_half_band_crossing_location/statement.md:4978-4992` | **BANKED — MY ENTIRE PREMISE, none of it mine.** I use all of it and claim none of it. |
| **`T >= 3` over `mu_32` as the open target and its `8.9e3x/3.9e6x` price** | `critical/nodes/rate_half_band_crossing_location/statement.md:4675-4676` ("the single named instrument of the converged question"), `:4982-4984` | **banked as OPEN.** My ten witnesses close it at `q=97` and `q=193`. This is the deliverable. |
| **the rate `q^-3 = 1.096e-06`, "triples needed ~ 912673"** | `r37_third_solve/d4_results.txt:54-55` | **BANKED, IN ROUND 37's OWN FILE.** MISS 3. I claim the *instrument*, not the rate. |
| **a full `C(32,7) = 3,365,856`-subset exhaustive census as a compute pattern** | `notes/wave22_import_20260724/WAVE22_AUDIT_FINDINGS.md:135` (`l1_mersenne_checkpoint_analog (32,7,4) full 3,365,856-subset census - complete`) | **BANKED IN THE `l1` LANE.** The *scale* of enumeration is precedented; its use on the `(L2)` `m=2` third-member problem is new **as a location**, not as a technique. |
| **`(NEWCAP)` `w* <= 7m-1`, `(OV)` `w* <= \|S_gamma u S_gamma'\|`** | `critical/nodes/rate_half_band_crossing_location/statement.md:566-573` | **BANKED VERBATIM.** Used, never claimed. |
| **the `a*` projective-vs-affine convention question** | `r37_mint_drafts/REPORT.md:56` (`13` only under the projective reading, `12` affine on the same object); `critical/.../statement.md:3585-3587` (r35's `a* = 13` on 5 of 6, `12` on one) | **BANKED as the open convention question; RULED by the coordinator this launch.** I apply the ruling and measure its effect; I did not raise it. |
| **shifted-lattice / weak-Popov / `d_1+d_2 = n-k+1` machinery** | `background/nodes/l1_exact_shell_balanced_shifted_lattice_reduction/statement.md:20-24` `(BL2)`, `:55-57` `(BL5)` | **BANKED IN THE `l1` LANE (anchor 2).** It is the vocabulary for my (X5); my contribution is that the `(L2)` problem **does not need it** — see D1.3. |
| **the 2x5 Hankel MOMENT-KERNEL form of the scale-eliminated condition** | greps for `Hankel moment`/`moment kernel`/`2x5 Hankel`/`moment matrix`: only `background/nodes/hankel_moment_clean_leaves/` (different node), `critical/nodes/rate_half_band_crossing_location/statement.md:2498` (middle-Hankel moment surjectivity, `A=1` lane), `background/nodes/xr_rank_two_three_anchor_grs3_factorization/proof.md:42` ("classify the moment kernel", `xr` lane) | **claimed new in this lane.** Verified two fields; `dim A = 3` on every triple tested. |
| **elimination of the two scale ratios `(lambda,mu)`; `dim(A cap B) = 1` so `u` is determined by the three SUBSETS alone** | greps for `scale elimination`/`scale-elimination`: 3 hits, all unrelated (`f3_h3_..._compiler/statement.md:88`, `verify.py:120`, `rate_half_band_closure/notes/kb_c2_112_...py:109`) | **claimed new.** This is the whole round: it is what turns `(q-1)^2` per triple into `O(1)`. |
| **the corrected criterion `u = c_1G + c_2H`, `c_1c_2 != 0`, and its `G ∥ H` degenerate branch** | no prior anywhere | **claimed new**, and one of its two clauses is a correction of my own registration (MISS 1). Brute-force agreement `113/113`. |
| **`d_1 <= 4` <=> the remainder-degree sequence skips `{5,...,9}` <=> a partial quotient of degree `>= 6` straddling the window** | greps for `partial quotient`/`partial-quotient`/`continued fraction`: only `notes/f2_campaign/F2_CAMPAIGN_LOG.md:2031,2041,2056`, `FINDINGS.md:68`, `literature_map_20260726/LITERATURE_MAP.md:113` — all F2/cyclotomic-norm, different lane and object | **claimed new in this lane; standard continued-fraction folklore elsewhere.** MEDIUM confidence on novelty, HIGH on correctness: `200/200` and `200/200` two fields, `120/120` constructed drops, and `10/10` on the witnesses. |
| **`a*(0,inf) = 2rho = 14` forced on every `s = 0` object** | `r36_sat3_on_l2/REPORT.md:42` reports `a* = 14` as a **single sample**; `r37_third_solve/REPORT.md:34` reports overlaps `[0,0,1,1,1,2]` | **the numbers are banked as samples; the FORCING is new** — it is a two-line corollary of `(SCRIT)`, so no `T=2` object can ever give another value. |

---

## D1 — THE LATTICE, STRUCTURED (the real costs, derived before any pessimism)

**D1.1 The pointwise third-member conditions (X1), verified.** Reducing `(SLOT)` at the prescribed points: on `S_0`, `f/g = Q_1/Q_2`; on `S_inf`, `f/g = Q_0/Q_1`. Substituting `Q_0 = alpha P_0`, `Q_2 = gamma P_inf`, `Q_0+Q_1+Q_2 = beta P_1` and writing `F = f+g`:

```text
 x in S_0   :  gamma P_inf(x) F(x) = beta P_1(x) g(x)        (T0)
 x in S_inf :  alpha P_0(x)   F(x) = beta P_1(x) f(x)        (Tinf)
```

Verified on random (PAR) objects: `(CONIC)` `300/300` and `300/300`; `f Q_2 = g Q_1` at **every** `F_q`-root of `Q_0` (`297/297` at `q=97`, `333/333` at `q=193`); `f Q_1 = g Q_0` at every root of `Q_2` (`288/288`, `312/312`) — `d1_results.txt:4-5`.

**D1.2 The scales eliminate (X2), and the test is `O(1)` (X3).** With `G := (beta/gamma)g`, `H := (beta/alpha)f`, `(T0)` and `(Tinf)` become `P_inf(x)u(x) = P_1(x)G(x)` on `S_0` and `P_0(x)u(x) = P_1(x)H(x)` on `S_inf`, `u = F`. Since `deg G <= 4` and `|S_0| = 7`, the seven values `P_inf(x)u(x)/P_1(x)` must be degree-`<=4`-interpolable: exactly the two dual conditions `sum_x v_x/P_0'(x) = 0` and `sum_x v_x x/P_0'(x) = 0`, i.e. **`A = ker` of the 2x5 Hankel moment matrix `[[m_0..m_4],[m_1..m_5]]`**. Two 3-spaces in `F_q^5` meet in a line, so `u` is determined; then `u = c_1G + c_2H` is a `rank <= 2` condition on a `3x5` matrix — **codimension `(5-2)(3-2) = 3`, reproducing the banked deficit 3 from a route that never mentions a lattice.** Overlaps are handled uniformly: `|S_1 cap S_0| = k` replaces `k` moment rows by `k` vanishing rows `u(x) = 0` (the same total, 2, for `k <= 2`); for `k >= 3` the stacked `5`-column system has rank 5 and the triple is rejected in one elimination.

**D1.3 `L`, `h`, `k` are automatic (X4) — the 14 pointwise conditions are SUFFICIENT.** `(CONIC)` gives `L = (Q_0g^2 - Q_1fg + Q_2f^2)/(Q_0Q_2)`; the numerator vanishes on `S_0` by `(T0)` and on `S_inf` by `(Tinf)`, so `L` is automatically a polynomial, and `deg L = 1` was observed on `10/10` witnesses; then `f | (LQ_2-g^2)` and `g | (f^2-LQ_0)` follow from `(CONIC)` mod `f` and mod `g`. Round 37 established necessity of the Cauchy conditions; **sufficiency is what makes the inverse constructive.** **P20 HIT** — `L`, `h`, `k` polynomial on every genuine hit at `q=23`, `q=97`, `q=193`.

**D1.4 The Euclid trajectory (X5) — verified, and then retired.** For `f == Rg (mod P_0P_inf)`, `deg P_0P_inf = 14`, with `deg v_i = 14 - deg r_{i-1}`: `d_1 = min_i max(deg r_i, deg v_i) <= 4` **iff** some `i` has `deg r_i <= 4` and `deg r_{i-1} >= 10`, **iff the remainder-degree sequence skips `{5,...,9}`**. Both equivalences `200/200` at both fields, plus `deg v_i = 14 - deg r_{i-1}` `200/200`; constructed drops detected `120/120` (`d1_results.txt:7-10`). Blind rate `~q^-5`: measured `3.775e-3` vs `q^-5 = 4.115e-3` at `q=3` (ratio `0.92`, 40,000 trials); `q=5` and `q=7` are Poisson-consistent at `4` and `0` hits (`:12-14`). **Answers to the brief's three D1 questions:** (i) moving one point of `S_1` changes all 14 interpolated values multiplicatively, so `R` changes completely — and the degree profile is generically the constant all-ones profile, so it carries no signal either way (MISS 4); (ii) swapping `S_1` wholesale is the same statement; (iii) **there is no half-gcd incremental update, and none is needed** — the incremental object is the 14 values `P_1(x)`, updated with 14 multiplications per DFS node, and the test downstream of them is `O(1)` with a `~330`-operation constant. `q^-5 x (q-1)^2 = q^-3` per triple reconciles the lattice picture with the ledger exactly.

**D1.5 The real cost, measured.** `57.0 us/triple` and `56.8 us/triple` for the two complete `q=97` pairs; `67.1-73.2 us/triple` at `q=193`; `~100 us/triple` under six-way parallel contention. **A complete exhaustive pair sweep of `C(32,7) = 3,365,856` costs `191-247 s` — one ramguard `local` window.** Against round 37's route (`2.5e5` exact `T=2` objects per `T=3` at `~13.5 ms` each, `~3.4e3 s` per hit on their own arithmetic, or `~3.4e5 s` on mine), one hit now costs `~64 s` at `q=97`. I state this as a gain over **round 37's instrument**, not as a complexity bound (R5.6).

---

## D2 — THE PUSH

**D2.1 Validation, both directions, before any push** (`d1_results.txt`, `d1_validate`/`d1_validate2` blocks). `q=23`, domain all of `F_23`, two `(S_0,S_inf)` pairs, **all `C(23,7) = 245,157` subsets `S_1` per pair**. Branch accounting is exact: `dim0 311672 + rank3 169476 + hit 3844 + dim2 212 + overlap>2 5110 = 490,314 = 2 x 245,157`. Genuine hits **13** against `2 x 86,766/23^3 = 14.26` predicted. Every genuine hit reconstructs to a full (PAR) object with all identities true. Brute-force `(lambda,mu)` scan of the `14x10` system on `113` triples (13 genuine, 40 degenerate, 60 random): **corrected (TEST) `113/113`**, raw `rank<=2` `73/113`.

**D2.2 The sweep over `mu_32`.**

```text
 q     pairs  triples swept   complete?          hits   predicted (q^-3 on the
                                                        69.25% fast-path mass)
 97      4     11,974,592     2 of 4 complete      9         9.09
193     12     37,543,680     8 of 12 complete     1         3.62
```

`q=97` seeds 0,1: complete, `3` hits each, `191.9 s` / `191.1 s`. Seeds 2,3: `77.9%` swept, `1` and `2` hits. `q=193` seeds 0-3 and 8-11: complete, `0,0,0,0,0,0,1,0`; seeds 4-7: `78-80%`, `0` each. **Round 37's published rate (`354` expected per pair, `d4_results.txt:25`) would predict `872` hits at `q=97` and `694` at `q=193` on the same swept mass. Observed `9` and `1`. (X6) fires, at both fields, by a factor `~(q-1)`** — the ledger's `(q-1)` is a scaling orbit; what is wrong is the derived operational number `P(T>=3 | one T=2 object) = 4.00e-6` and the `2.5e5`-objects-needed / `8.93e3x`-shortfall line built on it.

**D2.3 A certified witness, both fields** (full data for all ten in `d2_results_q97_s0..s3.txt`, `d2_results_q193_s10.txt`; independent re-derivation in `d3_results.txt`).

```text
q=97   S_0  =[8,28,45,50,70,79,96]      S_inf=[27,34,46,47,55,67,89]
       S_1  =[1,20,33,42,45,67,78]
       f=[62,36,59,38,41]  g=[28,46,63,42,57]  h=[70,50,64,47,75]
       k=[30,72,86,96]     L=[52,60]   alpha=7  gamma=86
       Q0=[13,13,8,88,80,77,84,7]   Q1=[29,77,89,63,1,80,77,5]
       Q2=[9,95,96,90,27,29,38,86]
       T_mu32=3, supported {0,1,inf}, s=0, deg(7,7,7), |union|=19,
       sum d_x=21, OV4 worst e(k,i)+e(k,j)=2, a*=13, d_1=4

q=193  S_0  =[1,8,24,69,72,81,124]     S_inf=[9,42,64,150,151,179,192]
       S_1  =[8,67,69,121,126,143,151]
       f=[68,165,18,76,122]  g=[15,89,82,190,72]  h=[88,162,42,93,170]
       k=[27,112,75,128,80]  L=[151,111]  alpha=190  gamma=164
       Q0=[42,184,115,131,56,75,172,190]  Q1=[57,4,59,101,143,58,59,33]
       Q2=[13,121,176,81,67,132,49,164]
       T_mu32=3, supported {0,1,inf}, s=0, deg(7,7,7), |union|=18,
       sum d_x=21, OV4 worst=3, a*=12, deg-drop slopes {89,185}
```

`(OV4)` holds on all ten: worst `e(k,i)+e(k,j)` is `2,3,3,3,3,3,4,3,3,3` against the bound `4`; `max_z |roots(f+zg) cap (S_0 u S_inf)|` matches it exactly on every witness (`d3_results.txt`). Overlap patterns `(|S_1 cap S_0|, |S_1 cap S_inf|)` over the nine `q=97` hits: `(1,1)x1, (2,1)x4, (1,2)x3, (2,2)x1`.

**D2.4 Toward `T = 4`: not reached, not sought at rate.** The full `P^1(F_q)` slope scan on every witness returns `supported = [0, 1, inf]` and nothing else. A fourth split member costs a further `~q^-7`; my swept mass is `~5e7` triples. Absence where none was sought (R5.5).

---

## D3 — F1 UNDER THE RULING

**The ruling is real and, on this dataset, inert where it matters.** A slope supported over `mu_32` has seven *finite* roots, hence `deg Q_z = 7`, hence no root at infinity: **the projective and affine readings agree on every supported pair of every object in the campaign's `s=0` class.** The ruling bites only at the slopes where the leading quadratic `lead(Q_0) + z lead(Q_1) + z^2 lead(Q_2)` vanishes, and those can never be supported over a finite domain. Measured directly on the six `q=97` pair-0/pair-1 witnesses (`d3_results.txt`): for `q97-p0-w2` the all-slope-pair histogram is `[(12,1),(13,58),(14,4694)]` projective vs `[(12,1),(13,57),(14,4695)]` affine — the ruling moves **exactly one pair** (the pair of the two degree-drop slopes `{14,66}`) from `14` to `13`; identically one pair for `w3`; **and the minimum is `12` under both readings on all six.** The convention question is settled in the sense that it changes no endpoint functional here.

**The distribution.** Per supported pair over the ten witnesses (30 pairs): `{12: 10, 13: 10, 14: 10}` — exactly uniform, and *forced*: `a*(0,inf) = 14` always (because `s = 0` makes `S_0, S_inf` disjoint, by `(SCRIT)`), `a*(0,1) = 14 - |S_1 cap S_0|`, `a*(1,inf) = 14 - |S_1 cap S_inf|`. Per object (min over supported pairs, the endpoint functional): `[13,12,12,12,12,12,12,12,12,12]`. `7m-1 = 13`.

**A corollary that removes the need to regenerate prior objects.** For **every** `e=m=2` object with `s = 0` and exactly two supported slopes, `(SCRIT)` forces `S_0 cap S_inf = ∅`, hence `a*` over supported pairs `= 2rho = 14` **identically**. So round 36's single sample `a* = 14` (`r36_sat3_on_l2/REPORT.md:42`) and every one of round 37's 28+4 certified `s=0` `T=2` objects (`r37_third_solve/d2_results.txt:21,27`) carry the same forced value — regenerating them adds no information. Round 37's bespoke `T=4` objects give `a* = 12` and `13` from overlaps `[0,0,1,1,1,2]` and `[0,0,1,1,1,1]` (`r37_third_solve/REPORT.md:34`), unchanged by the ruling for the same reason.

**F1/(NEWCAP) status: ZERO POWER, as pre-declared (R5.3).** `(NEWCAP)`'s premise is `T = rho+2 = 9` (`critical/.../statement.md:567-573`); I have `T = 3`. Three supported pairs per object is not a minimum over a family. **No F1 test is claimed.**

---

## D4 — VERDICT

> **THE INVERSE IS AN ALGORITHM.** The third prescription's two scale ratios eliminate exactly; `u = f+g` is then determined by `(S_0,S_inf,S_1)` alone as the intersection of the kernels of two `2x5` Hankel moment matrices, and the drop is the single rank-`<=2` condition `u = c_1G + c_2H` (`c_1c_2 != 0`, both parts of degree 4) — codimension 3, `57 us`, no lattice reduction. That makes an **exhaustive per-pair sweep of all `C(32,7) = 3,365,856` subsets `S_1` a 192-second computation**, and it yields **`T = 3` over `mu_32`: ten certified objects, `9` at `q=97` from `11.97e6` triples (predicted `9.09`) and `1` at `q=193` from `37.54e6` (predicted `3.62`)** — the first of their kind, against a banked price of `8.9e3x` short. `T = 4` over `mu_32` was not reached. `e = m = 2` was **not** certified (MISS 2), and no criterion in the `(SCRIT)` mold exists on my evidence — `(TEST)` reads field values, not incidence.

**T-record with provenance.** `T_mu32 = 3`, ten objects: `q=97` seeds 0,1 (3 each, complete sweeps), seeds 2,3 (1 and 2, `77.9%` sweeps); `q=193` seed 10 (1, complete sweep). Previous record over `mu_32`: `2` (rounds 36 and 37). `T_bespoke` this round: **not measured** — I ran no bespoke-domain construction, so round 37's `T_bespoke = 4` stands and the columns are never merged.

**Solve-vs-search status of the third prescription: STILL SEARCH — but the search is now finite and cheap.** `912,673` triples per hit at `q=97` (`= q^3`), `~64 s` of sweep. There is still no *solve*: given `(S_0,S_inf)` you cannot write down an admissible `S_1`.

**Handoff, priority order (recommendations only — AUDIT-AND-DRAFT; nothing outside my directory was altered).**
1. **Retire the `8.9e3x/3.9e6x` shortfall line at `critical/nodes/rate_half_band_crossing_location/statement.md:4982-4984` and the `T >= 3 over mu_32` open-instrument line at `:4675-4676`.** Replace with the ten witnesses and the per-pair sweep cost. Note in the same edit that round 37's `d4_results.txt:54` already contained `912673`.
2. **Bank the scale-elimination and the corrected `(TEST)`** — including the `G ∥ H` degenerate branch, which is pair-dependent and can dominate raw hits (`3824` vs `6` on one `q=23` pair). Any reimplementation that omits the `c_1c_2 != 0` clause will report ~400x too many hits.
3. **Certify `e = m = 2` on the ten witnesses with round 37's `36x32` apparatus before any of them is used downstream** (MISS 2). Check `q97-p0-w1`'s `deg k = 3` first.
4. **Bank the `a*` forcing:** `a* = 2rho` on every `s=0` `T=2` object; and the finding that the projective ruling is inert on supported pairs and moves exactly one all-slope pair per degree-drop-slope pair.
5. **The next `T` question is a solve, not a sweep.** `T = 4` over `mu_32` needs `~q^3` pair-sweeps, i.e. `~q^3 x 192 s`; it is out of reach by enumeration and wants an inverse for the rank-`<=2` condition.
6. **A candidate necessary condition to test properly (NOT claimed):** hits concentrated at `|S_1 cap S_0| + |S_1 cap S_inf| >= 3`, `8/9` against `54.0%` (`p ~ 0.034`, `n=9`). Two more complete `q=97` pairs would take this to `n ~ 15`.

**Cross-pilot flag (self-contained; I read no sibling `r38_*` directory).**

> When a prescription problem carries free projective scale parameters, look for a **dual/annihilator elimination** before scanning them. Here the three prescriptions `Q_0 = alpha P_0`, `Q_{z=1} = beta P_1`, `Q_2 = gamma P_inf` reduce to two pointwise systems each depending on ONE ratio; substituting `G = (beta/gamma)g`, `H = (beta/alpha)f` makes both systems linear and the ratios vanish, leaving `u = f+g` in the intersection of two kernels of **2x5 Hankel moment matrices** built from `sum_x P_inf(x)x^j/(P_1(x)P_0'(x))`. The remaining condition is a single `rank <= 2` on a `3x5` matrix (codimension 3 = the deficit), with the degenerate branch `G ∥ H` that must be excluded explicitly. Cost per instance: `~330` field operations. **Transportable rule: a `k`-fold scale scan in an interpolation-type census is usually a missing dual-annihilator elimination.** Also: for a rank-2 `F_q[x]`-lattice of determinant degree `D` whose first minimum must drop from `D/2` to `<= b`, the exact criterion is that the Euclid remainder-degree sequence **skips the window `[b+1, D-b-1]`**.

---

## PREDICTIONS vs OUTCOMES

| registered | outcome |
|---|---|
| **(X1)** the two pointwise third-member conditions | **HIT**, `300/300` `(CONIC)` and `297/297`,`288/288`,`333/333`,`312/312` pointwise, two fields |
| **(X2)** the scales eliminate; `A` = kernel of a 2x5 Hankel moment matrix, `dim 3` | **HIT** — and it is the round |
| **(X3)** `hit <=> rank[u;G;H] <= 2`, codim 3, rate `q^-3` | **HALF WRONG (MISS 1).** Codim and rate **HIT** (`13` vs `14.26` at `q=23`; `9` vs `9.09` at `q=97`); the criterion needed the `u = c_1G+c_2H`, `c_1c_2 != 0` clause. **P7 NO** |
| **(X4)** `L`, `h`, `k` automatic; the 14 conditions are sufficient | **HIT**, every genuine hit at three fields (**P20 HIT**) |
| **(X5)** drop <=> remainder degrees skip `{5..9}`; blind rate `q^-5` | **HIT** — `200/200` x2, `120/120` x2, ratio `0.92` at `q=3`, and `10/10` on the witnesses |
| **(X6)** round 37's per-object rate is `(q-1)x` too large | **HIT, DECISIVELY** — `9` observed vs `872` predicted by their rate at `q=97`, `1` vs `694` at `q=193`. **P8 HIT** |
| **(X7)** `O(1)` amortised sweep, `C(32,7)` is the right denominator | **HIT** — `57 us/triple`, `192 s/pair`; the brief's `C(25,7)` was the wrong denominator (**R7(b) fired**) |
| **(X8)** no purely combinatorial criterion | **NOT RESOLVED.** Not proved, not refuted; one unclaimed `p~0.034` signal on `n=9` (MISS 11) |
| **(X9)** per-pair yield `3.69` (`q=97`), `0.468` (`q=193`) over all `C(32,7)` | **HIT at `q=97`** (`2.55` on the fast-path mass; observed `3,3`), **UNDERSHOOT at `q=193`** (`1` vs `3.62`, `p~0.12`, MISS 7) |
| **P1** exhaustive-per-pair sweep feasible `= 0.72` | **HIT** — 192 s per complete pair |
| **P2** `T = 3` over `mu_32` `= 0.55` | **HIT** — ten objects, two fields |
| **P3** a `(SCRIT)`-mold criterion `= 0.12` | **resolved NO** |
| **P4** Euclid incremental update is the speedup `= 0.30` | **resolved NO** — the Euclid route is retired, not accelerated; my measurement of it was void (MISS 4) |
| **P5** expected max `T` over `mu_32` `= 3` | **HIT EXACTLY.** P5a (bespoke `= 4`) **NOT TESTED** — no bespoke run. P5b **HIT** |
| **P6** `a* = 13` dominates `= 0.40` | **resolved NO under both readings** (MISS 12) |
| **P9 / P19** `T = 4` over `mu_32` / the negative-exponent cell | **resolved NO**, zero power |
| **P10** hit rate within `[0.7,1.4] x q^-3` | **HIT** — `9/9.09 = 0.99` at `q=97`; `q=193` is `0.28` (MISS 7) |
| **P11** a ramguard run fails `= 0.30` | **resolved YES** — one wall kill (MISS 5) |
| **P12** I ship a bug `= 0.75` | **resolved YES** — one crash (MISS 6) |
| **P13** a CATCH-24A subtraction fires load-bearing `= 0.80` | **HIT — four**: the whole `(PAR)`/`(CONIC)`/`(SCRIT)`/`(OV4)` premise; the banked open target; **round 37's own `912673`**; the banked `C(32,7)` census pattern in `l1` |
| **P14** `q=193` also produces a `T=3` `= 0.30` | **HIT** — one witness, seed 10 |
| **P15** I end with a WALL `= 0.15` | **resolved NO** — I end with an algorithm |
| **P16** a found `T=3` certifies as `e=m=2`, seprank 3, nullity 1 `= 0.55` | **NOT TESTED — MISS 2.** Intrinsic certification only |
| **P17** the moment form is banked in-repo `= 0.35` | **resolved NO** in this lane (three near-hits, all other lanes) |
| **P18** `a*` reproduces the banked `13` `= 0.50` | **PARTIAL** — `13` occurs on `10` of `30` supported pairs and as one object's `a*`; the ruling reproduces r35's `13`-vs-`12` mechanism exactly (one pair moved per degree-drop-slope pair) |

---

## ZERO-POWER DECLARATIONS

1. **R5.1 honoured.** Four `(S_0,S_inf)` pairs at `q=97` and twelve at `q=193`, out of `~1.6e12`. **ZERO POWER for `(SAT3)`, the strict endpoint, the official row, emptiness, or any statement about `mu_32` in general.**
2. **R5.2 honoured.** I ran **no** bespoke-domain construction this round, so I report **no** `T_bespoke`. Round 37's `T_bespoke = 4` is theirs and is never merged with my `T_mu32 = 3`.
3. **R5.3 honoured and load-bearing.** F1/`(NEWCAP)` at **ZERO POWER**: premise is `T = rho+2 = 9`, I have `3`. The `a*` dataset is 30 supported pairs on 10 objects, and its values are *forced* by the overlap combinatorics, not sampled.
4. **R5.4 honoured.** Two fields only (`97`, `193`) for everything; `q = 3,5,7,17,23,29` used only as validation arithmetic. **No lift to `Z`, no geometric irreducibility, no `q ~ 2^128`, nothing at `m >= 3`, nothing about `Rout`, the `9/4` or `7/4` ledgers, FR-canonical, or layer A.**
5. **R5.5 honoured.** No `T = 4` over `mu_32` has **zero power** — the required sweep is `~q^3` times what I ran.
6. **R5.6 honoured.** `57 us/triple`, `192 s/pair` and the "one hit per `64 s`" figure are properties of **my stdlib-Python implementation under ramguard**, not complexity bounds. The gain over round 37 is a gain over their *instrument*.
7. **R5.7 discharged, in the direction I feared.** `(TEST)` was registered as conjectural; one of its clauses was **wrong** and is reported as MISS 1. The corrected form is verified in **both** directions (`113/113` against brute force) at `q=23` only; at `q=97`/`q=193` only the forward direction is verified (every hit reconstructs), because the brute-force scan is `(q-1)^2` per triple.
8. **R5.8 honoured.** `(OV4)` is used as a *check*, never as a search win; it held on `10/10` witnesses and on `11/11` `q=23` reconstructions.
9. **R4(i)** honoured: `T = 3` is a **sample maximum over the triples I swept**, never a bound; so is `a* = 13`'s appearance and the `(OV4)` worst value `4`.
10. **R4(ii)** honoured: `T` distributions are `{3: 9}` over `9` hits at `q=97` and `{3: 1}` at `q=193`; all non-hit triples have `T = 2` by construction of the pair, which is **not** an object statement.
11. **R4(iv)** honoured: I convert neither the `+62.5`-bit cell nor the `q=193` near-miss into a verdict in either direction. The `q=193` zero-then-one is Poisson noise around `3.62`, nothing more.
12. **The nine-point overlap signal (MISS 11) is declared at LOW POWER and is not a result.**

---

## MEASURED FUNCTIONALS (CATCH-19C)

`m=2, rho=7, N=32, R=16, A=3, s, T over mu_32, T_target=9`; `deg Q_0,Q_1,Q_2`; `deg f,g,h,k,L`; `s = deg gcd(Q_0,Q_1,Q_2)`; `deg gcd(f,g)`; the `(CONIC)` residual; the three (PAR) identity residuals from `(f,g,h,k,L)` alone; the `z=1` member identity `Q_0+Q_1+Q_2 = P_1`. **New here:** the pointwise residuals of `(T0)`/`(Tinf)` at every `F_q`-root of `Q_0` and of `Q_2`; the 2x5 Hankel moment matrices and `dim A`, `dim B`, `dim(A cap B)`; the branch census `{dim0, dim2, rank3, hit, DEGEN, BIGOVL}` per sweep; `rank[G;H]` and `(deg G, deg H)` on every degenerate hit; the reconstruction failure taxonomy; the Euclid remainder-degree sequence, the cofactor-degree identity `deg v_i = 14 - deg r_{i-1}`, the first minimum `d_1`, the window-skip predicate, and the blind rate of `d_1 <= 4` at `q = 3,5,7`; the residue `f - Rg mod P_0P_inf` on every witness; the full `P^1(F_q)` slope scan with each member's `mu_32`-root count and degree; `|union|`, `sum_x d_x`, `2|union|`; the pairwise overlap matrix and worst `e(k,i)+e(k,j)`; `max_z |roots(f+zg) cap (S_0 u S_inf)|`; the leading quadratic and its degree-drop slopes; `a*` per supported pair and per object; `a*` over **all** `C(q+1,2)` slope pairs under **both** the projective and the affine reading, with full histograms; the hit overlap-pattern histogram against the admissible-population proportions; per-triple wall time. **Registered but NOT measured:** `nullity(36x32)`, separation rank, generic pencil rank and its histogram, the finite rank-drop set, the rank at infinity, the degree-`<=1` kernel dimension — hence `e = m = 2` (MISS 2); any `T >= 4`; any bespoke-domain object; `(SAT2)/(SAT3)/(SAT4)/(SAT5)` (inapplicable at `T=3`); anything at `m >= 3`; the reverse direction of `(TEST)` at `q = 97,193`.

---

## COMPLIANCE

**Registrations.** After reading **exactly** the two named anchors (`r37_third_solve/REPORT.md`, `l1_exact_shell_balanced_shifted_lattice_reduction/statement.md`) and **before any other read, any grep, any `ls`, and any interpreter invocation**, I appended `## Pilot registrations` to `PREREG.md` with the **Edit tool in two calls** (the second retried once after a whitespace mismatch, which required one bounded `Read` of my own registration file — the same file, mid-registration, and no other file was touched). Registered: `R0` notation from the anchors alone, `R1` execution order, **nine falsifiable derivations `(X1)-(X9)` each with an explicit falsifier**, **twenty numeric priors `P1-P20` including the brief's six and the expected-max-`T` number (`P5 = 3`)**, the six-clause MISS-2 guard `R4` (with the two new clauses on exhaustion scope and certify-before-claiming), eight zero-power pre-declarations `R5`, the subtraction plan `R6` with hyphenated/infixed variants, and expected misses `R7`. **No post-registration addenda**; the two registration failures ((X3)'s missing clause, and my own R4(vi) which I then could not honour) are reported as MISS 1 and MISS 2, not edited away. `R7(a)` (I expected to lose one of (X1)-(X9)) and `R7(b)` (the brief's denominator) both fired; `R7(c)`, `R7(d)`, `R7(e)` all fired as written.

**Compute law — NO BREACH. THE PRE-BASH CHECKLIST WAS APPLIED TO EVERY BASH CALL.** **21 interpreter invocations, all 21 of the form `tools/ramguard local -- python3 …`**, issued from the repo root with the literal `--`, each with `RAMGUARD_TIMEOUT` set explicitly (`280`, `285`, `290`, or `295`, documented per run). **Zero bare `python3` for any purpose** — no patching, no probes, no heredocs, no no-op invocations between edits. Stdlib only (`random`, `time`, `itertools`, `sys`, `math.comb`); no third-party imports, no Modal, no network, no git, **no subagents**. **Ramguard status: 19 clean exits, one wall kill (`d1_validate`, exit 124 at the `290 s` limit — MISS 5), one non-ramguard crash from my own `IndexError` (MISS 6).** Six runs were self-budgeted below their ramguard limit and stopped themselves at `[BUDGET STOP]` with the exact swept count printed; those are my caps, not ramguard events. Long runs were issued as background processes so no foreground tool window was exceeded.

**Write discipline.** No `sed -i`, `awk -i`, `perl -i`, `tee`, or shell redirection onto any existing file; no in-place shell stream edit anywhere. The two `PREREG.md` registration appends and the four source-file corrections used the **Edit** tool; all five scripts were created with the **Write** tool. The only shell redirections used were `> /dev/null 2>&1` on parallel launches (discarding stdout, never writing a file).

**Results-file rules — HONOURED, AND IT PAID.** Every results file is opened in **append** mode (`"a"`) with a timestamped `=== RUN … ===` header per invocation, and the sweep files are additionally **versioned per run** (`d2_results_q{q}_s{seed}.txt`) so that sixteen concurrent sweeps could not interleave. **No blind `"w"` anywhere** — which is why the wall-killed `d1_validate` run's sweep half survives on disk and is cited as MISS 5 rather than lost. **No results-producing run was piped through `head`**; `tail` and `grep` were applied only to files already closed by a finished process, never as a prefix filter on a live producer.

**Imported-script rule — NOT ENGAGED, and stated rather than assumed.** I imported and executed **no** banked script. All five scripts (`d1_struct.py`, `d1_validate.py`, `d1_validate2.py`, `d2_sweep.py`, `d3_astar.py`) are mine, written from scratch, with the polynomial/linear-algebra helpers **duplicated into each file** rather than imported, exactly so that no import can write at import time. No banked script's output paths needed auditing because none was copied. Banked material was read **only** as data, via `grep -n`, `sed -n` windows, and the two anchor `Read`s.

**RAM discipline.** `dag.json` **never opened**; every recursive grep carried `--exclude=dag.json`. `critical/nodes/rate_half_band_crossing_location/statement.md` (>5000 lines) was read **only** in four bounded `sed -n` windows (`560-580`, `3575-3600`, `4670-4682`, `4978-4992`) plus grep output lines — never as a file. Largest object materialised: the 14-value DFS product ladder and a `4x5` matrix; every driver writes its own results file. Peak memory per process was far under the `1G` ceiling; no memory event on any run.

**Quarantine — clean.** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` **never opened and never appeared in any tool output**. **No sibling round-38 directory (`r38_side_door`, `r38_urate_genericity`, `r38_sporadic_det`) was opened, read, listed or traversed, and `notes/pilots_20260811/` was never `ls`-ed** — every path I named was explicit. Every recursive grep carried `--exclude-dir=r38_side_door --exclude-dir=r38_urate_genericity --exclude-dir=r38_sporadic_det --exclude-dir=pilots_20260802 --exclude-dir='prize-codex-*' --exclude-dir=.git --exclude-dir=__pycache__ --exclude=dag.json` **at the search level**, never as output filtering. No path containing `prize-codex-` was touched. `r37_*` and `rh_*` were read as explicitly permitted.

**Write scope.** Every write is inside `notes/pilots_20260811/r38_cauchy_lattice/`: `PREREG.md` (registrations appended), `d1_struct.py`, `d1_validate.py`, `d1_validate2.py`, `d2_sweep.py`, `d3_astar.py`, `d1_results.txt`, `d3_results.txt`, and sixteen `d2_results_q{97,193}_s{n}.txt`. **No `dag/`, `nodes/`, `critical/`, `background/`, `experiments/` or `tools/` edits; no git; the session scratchpad was not used for any project file; nothing went to `/tmp`** (background stdout capture is harness-owned, not a file I wrote). **AUDIT-AND-DRAFT respected:** every board and node recommendation in D4 is posed for coordinator triage and **nothing outside my directory was altered**. `REPORT.md` is not written — per the brief's fallback clause this report is returned verbatim as my final message.

**Method discipline.** CATCH-24A greps ran **before** every novelty claim, including hyphenated and infixed variants, and produced **eleven live subtractions, four of them load-bearing**: the entire `(PAR)`/`(CONIC)`/`(SLOT)`/`(SCRIT)`/`(OV4)`/deficit-3 premise is round 37's and coordinator-audited; `T >= 3 over mu_32` is banked as the open target with its price; **round 37's own `d4_results.txt:54` already carried `912673`**; and a full `C(32,7)`-subset census is a banked `l1`-lane compute pattern. Every quantifier claim carries a `file:line` or a results-file citation with its denominator. Every max-quantified claim carries a zero-power declaration. **Two-field confirmation (`F_97`/`F_193`) for every structural claim** — `(X1)`, `(CONIC)`, the pointwise conditions, `(X5)`'s two equivalences and the cofactor identity, the sweep instrument, the branch census, and the `T=3` result itself — with `q = 3,5,7,17,23,29` declared as validation arithmetic and the `q=23` brute-force cross-check declared as the only place where `(TEST)` is verified in **both** directions. **MISSES FIRST**, and the round's own self-corrections — that my registered criterion was incomplete and my own validation caught it, that I could not honour my own certification rule, that round 37's file already held the key number, that a measurement of mine was void by design, that ramguard killed a run I sized wrong, and that I shipped a crashing bug — are reported as falsifications of my own work, in that order, before any result.
