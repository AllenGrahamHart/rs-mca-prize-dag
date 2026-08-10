The harness refused the `REPORT.md` write (subagent policy), so per the brief I return the full report text verbatim below.

**Headline for relay:** the `5.04e22` residual-(ii) cap **shrinks to `1.236950581231e12`** — a `40,722,652,881x` (10.61 decimal orders) reduction — via one inequality the anchors had banked in the wrong direction; the residual is now a factor of exactly `9/4`. Neither budget closes. Deliverables (scripts + results) are in `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260810/rh_type2_stratum/`.

---

# REPORT — rh_type2_stratum (round 31)

## VERDICT (first)

**The stratum does NOT close. Both budgets `{2^39, 2^39+1}` stay open, status unchanged.** What did happen: the `5.04e22` **shrinks to `1.236950581231e12`** — a factor of **40,722,652,881x ≈ 10.61 decimal orders of the 11-order gap** — and the residual is reduced to a single **factor of exactly `9/4 = 2.25`**, with the missing inequality named to the constant.

The mechanism is one inequality that was sitting in the anchors in the wrong direction:

> **(OV)** For **every** pair of distinct supported slopes `gamma != gamma'`, `w* <= |S_gamma u S_gamma'|`. *(`(v_gamma, v_gamma')` is itself a `D`-representation of the syndrome pair up to a `GL_2` basis change, and joint support is `GL_2`-invariant: `x` is in the joint support iff `(c_{0,x}, c_{1,x}) != 0`, a condition invertible maps preserve.)*

Summing (OV) over all `C(T,2)` pairs and pairing it with the banked saturation layer through the incidence identity `sum_{gamma<gamma'} |S_gamma ^ S_gamma'| = sum_x C(d_x,2)` gives a **`W`-free ceiling on `w*` itself**:

> **(NEWCAP)** Under `(SAT1)-(SAT4)` with `T = rho+2`, `w* <= 2rho - (Lmin(O) + (T-1)O)/C(T,2)`, where `Lmin(O) = (N-1-O)C(m,2) + (1+O)C(m-1,2)` is the convexity minimum of `sum_x C(d_x,2)`. The bound is monotone in `O` (slope `3m+1 > 0`), so it is tightest at `O = 0`: `w* <= 8m-2 - (m-1)(8m^2-1)/(2m(4m+1))`, i.e. **`w* <= 7m-1`** for `m >= 1024` (exact integer values in `d2_transport_results.txt`).

Because `CAP(m,a) = floor((N-a)e/(R+1-a))` is monotone increasing in `a` (verified exhaustively for `m = 2,8,64` in `d1_anatomy_results.txt`), the banked residual cap may be re-evaluated at `a = 7m-1` instead of `a = 8m-2`:

| | `a` | `s = R+1-a` | residual-(ii) cap at `m = 2^37` |
|---|---|---|---|
| banked | `8m-2` | `3` | `50 371 909 150 701 174 915 072` |
| **sharpened** | `7m-1` | `m+2` | **`1 236 950 581 231`** |

and the whole `AO1` becomes `2 + 1236950581231 = 1236950581233` against `rho+1 = 2^39 = 549755813888` — **a residual factor of `2.2500`, down from `9.1626e10`.** The residual `w*` window also shrinks from `2/3` to `5/12` of the admissible range (measured `0.6667 -> 0.4167` at `m = 2^20, 2^37`).

**And `a = 8m-2` — the point at which the `5.04e22` was evaluated — is VACUOUS for every `m >= 2`.** `w* = 2rho` forces every pair of supported locator sets to be disjoint and of full size `rho`, which needs `T*rho <= N`, i.e. `(4m+1)(4m-1) <= 16m`: **true only at `m=1`**. That is the banked R4 fence (`notes/pilots_20260810/apolar_origin/REPORT.md:78`); what is new is that `w* = 2rho` *forces* the disjointness R4 refutes.

---

## MISSES FIRST

1. **P12 registered miss, HIT AS A MISS.** I registered `P(no close) = 0.90`. The stratum did not close; neither budget moved. The `9/4` survives.

2. **I FALSIFIED MY OWN PUBLISHED RESULT INSIDE THIS SESSION, and the superseded text is still in my results file.** `d1_anatomy_results.txt` section D1.6 prints an integer "counting feasibility certificate" at `a = 8m-2` for every `m` up to `2^37` and concludes *"the counting system at a=8m-2 with T=rho+2 is EXACTLY integer-feasible ... Therefore NO argument that uses only (SAT2)-(SAT5), d_x<=m, (C2) and (C3) can close the a=8m-2 face."* **That conclusion is WRONG.** The certificate omitted (OV). Adding it (`d2_transport_results.txt` D2.4) kills the certificate at every `m >= 2`: its own `|S_gamma ^ W| = rho - p_gamma` forces a pair union `<= 2rho - ceil((rho-p)/2) < a`. I am flagging the stale conclusion rather than editing the results file, per the round-29 precedent on mislabelled counters. **This self-falsification is what produced the session's main result** — the certificate's failure mode *is* (NEWCAP).

3. **NO ESCAPE REPLAY WAS RUN.** D3 of the brief invited copying the banked round-29 census machinery into my directory. I wrote my own decoder instead (Berlekamp-Massey + Vandermonde over `F_q`), so this session has **zero replay-identity evidence**. The only reproduction check I have is that my independent evaluation of `(N-a)e/(R+1-a)` reproduces `50371909150701174915072` exactly — one number, not a byte-identical replay. This is a real gap in my evidence base and I do not dress it up.

4. **My registered binding obstruction was the RIGHT object for the WRONG reason.** R5 predicted the wall would be `S_gamma ^ W != {}` destroying the AO2 reciprocal-locator normal form. Measurement says the normal form **survives intact** — (GNF) below generalises it exactly, verified `280/280` at four scales and two fields with zero failures. What `j >= 1` destroys is *uniqueness* (the shortened code has dimension `j+1`, not `1`), and the operative wall turned out to be somewhere else entirely: the **per-slope spend floor** `|S_gamma \ W| >= R+1-a`. Partial miss.

5. **(EQ) is only HALF a theorem, and I registered it as an iff.** Proved: `wt(kappa) = a + p - n_0` with `n_0 >= n_gamma`, so equality in `(C2)` (`p = R+1-a+n_gamma`) **implies** `j = 0`. The converse needs `n_0 = n_gamma` (no cancellation `z_x = v_x` on `S_gamma ^ W`), which I did **not** prove. It held in 100% of measured slopes (`OK 121 / BAD 0` across all eight cells), but that is a **sampled** check, not a proof. P4 scored as a partial hit.

6. **P6 effectively UNEXERCISED.** I registered the fraction of collinear triples meeting `|u S_i| <= R` in `[0, 0.35]`. Measured: **1 triple out of 646** (`0.0015`), and every one of those 646 came from a `T = 3` configuration, so "triples" means one per pencil. The number is inside my window but the window had no discriminating power.

7. **MODE A (random pencils) is a COMPLETE NULL.** **765** random pencils across four scales, three `w*` values and six field choices produced `T = 2` in 764 of them and `T = 3` once — and **zero type-2 slopes**. That is not evidence that type-2 slopes are rare; it is evidence that uniform sampling of `(v_1, v_2)` cannot find them. Declared as zero-power, not reported as a rarity measurement.

8. **The number `7m-1` is NOT mine.** It is banked, twice, in the anchors and in primary text — see the CATCH-24A subtraction below. My contribution is the *direction of the inequality*, not the quantity.

9. **(GNF) is a tautology and a port.** See CATCH-24A. I verified it because my derivation of it could have been wrong, not because it is new.

10. **(NEWCAP) is CONDITIONAL on `(SAT3)` (`T = rho+2`).** It is not a theorem about arbitrary strict-`A=3` pencils. That is the right form for refuting the failure hypothesis, but it means the census — which never reached `T > 3` — **cannot test it at all**. Zero power; falsifier F1 is live and unexercised.

---

## CATCH-24A — own-repo subtraction, run BEFORE every claim

| object | in-repo prior | verdict |
|---|---|---|
| the figure `5.04e22` | `critical/nodes/rate_half_band_crossing_location/statement.md:477` "not apply, and the counting cap there is 5.04e22 vs the 2^39"; derivation only in `notes/pilots_20260810/collinearity_object/d3_coverage.py:168-170` and its `d3_coverage_results.txt:94` | banked; I reconstruct, not discover |
| `(AO1)` | `notes/pilots_20260810/apolar_origin/PREREG.md:197-198` | banked |
| `(C2)` type-2 threshold `\|S_gamma \ W\| >= (R+1)-a+n_gamma` and `\|S_gamma ^ W\| <= a-n_gamma-(R-r+1)` | `notes/pilots_20260810/apolar_origin/PREREG.md:185-186` | banked |
| `r = rho` on this profile | `background/nodes/rate_half_ca_hankel_exceptional_root_charge/statement.md:128` "an exact `R=10,r=rho=4,e=1,delta=1` Hankel pencil" | banked |
| **(GNF)** `kappa_x = f(x)/sigma'_Z(x)`, `deg f <= \|Z\|-(R+1)` | `background/nodes/xr_two_slope_cost_theorem/proof.md:21-23`: *"Basis used by the verifier: `c^(t)_i = lam^S_i x_i^t`, `i in S`, `t = 0..\|S\|-k-1`, with `lam^S_i = prod_{j in S, j != i}(x_i-x_j)^{-1}` — the classical duality of generalized RS codes"*, and `statement.md:23` `(L1) dim C_S = \|S\|-k` | **PORT.** Same normal form, other lane. I claim the transport into the `ca_hankel` setting, nothing more. |
| **`w* <= \|S_i u S_j\|`** | `notes/pilots_20260810/apolar_origin/REPORT.md:57` "`w*` `<= \|S_i u S_j\| <= 2rho`" | **PORT.** The every-pair quantifier is the only thing I add. |
| **the number `7m-1`** | `notes/pilots_20260810/apolar_origin/REPORT.md:63` "`sum_x C(d_x,2)` forces mean `\|S_i n S_j\| ~ m-1`, i.e. mean `\|S_i u S_j\| ~ 7m-1 > 16m/3`"; replayed to primary text at `critical/nodes/rate_half_band_crossing_location/statement.md:207` "sits at large w* (~7m-1 > 16m/3)" | **PORT + RE-READING.** apolar computed exactly `7m-1` and read it as the LOCATION of the average configuration ("that is where the average configuration sits ... So this closure does not move either budget's status"). Because `w* <= min <= mean`, the identical number is an **upper bound on `w*`**. The contribution is the direction, not the arithmetic. |
| `T*rho <= N` disjointness fence | `notes/pilots_20260810/apolar_origin/REPORT.md:78` (R4) | **PORT.** New: `w* = 2rho` *forces* the disjointness R4 refutes. |
| `sum_x C(d_x,2)` as a counting instrument | `background/nodes/mca_quadratic_prize_rows/proof.md:46,52`; `background/nodes/upstream_gfv4_fixed_union_johnson/proof.md:76,82`; `notes/kernel_basis/WAVE6_AUDIT_FINDINGS.md:44` | standard in-repo technique |
| **(TR1')** "three supported slopes: either `\|u S\| >= R+1` or an exact linear relation" | greps for `S_1 u S_2 u S_3`, `union of the supports`, `three supports`, `minimum distance R+1` over `critical/`, `background/`, `notes/` returned **no prior** (only my own PREREG and collinearity_object's `\|S_1 u S_2 u S_3\| <= s+1` triple classifier at `PREREG.md:129`, a different statement) | claimed as new in this lane, low confidence that it is new anywhere |
| the "overlap-only theorems have a ceiling" warning | `background/nodes/l1_fpc5_ratehalf_m4_t2_distance_only_no_go/upstream_crosswalk.md:8-10`: *"A theorem whose only hypotheses are support weights and pairwise overlaps cannot close this consumer."* | **different consumer** (L1/FPC5 shift-pair lane), so not binding here — but it is an in-repo precedent that the `9/4` residual may be exactly the ceiling of the overlap-only route. Flagged, not asserted. |

---

## D1 — THE CAP'S ANATOMY

**It is the second summand of `(AO1)` evaluated at the top of the `w*` window, and nothing else.** `(AO1)` (`notes/pilots_20260810/apolar_origin/PREREG.md:197-198`) reads

```text
T <= min(m+1, floor(a/(a-rho)), floor((a m + O)/rho))
     + floor(((N-a) m)/((R+1)-a))
```

and the second term at `a = 8m-2` is `floor((8m+2)m/3)`. At `m = 2^37` this is **`2^38 (2^39+1)/3 = 50371909150701174915072`** — my independent evaluation matches the banked `notes/pilots_20260810/collinearity_object/d3_coverage_results.txt:94` digit for digit, and the division is **exact** (`(N-a)e mod s = 0`, so no floor loss). **P1 HIT, including the closed form registered blind.**

**The single count behind it.** Every type-2 slope spends at least `R+1-a` locator roots outside `W` (`(C2)`, `apolar_origin/PREREG.md:185`); each of the `N-a` outside points is spent by at most `e = m` slopes (`d_x <= m`, `saturation_rigidity/statement.md:49-50`). Hence `T_2 (R+1-a) <= sum_{x notin W} d_x <= (N-a)e`. That is the whole derivation.

**Where slack is given away — the four places, priced.**

- **(s1) the per-slope spend floor, and it is the ONLY one that matters.** `(C2)` supplies `p_gamma := |S_gamma \ W| >= R+1-a = 3` at `a = 8m-2`. Inverting the count for the floor that *would* close (D1.4): `p* = 2m+2 = 274877906946` exactly. The ratio of the two caps is the ratio of the two floors: `p*/3 = 91625968982` against `CAP/(rho+2) = 2^38/3 = 91625968981`. **The entire `5.04e22`-vs-`2^39` discrepancy is one inequality, off by a factor `~2m/3`.**
- **(s2) `d_x <= m` used flat** although `(SAT4)` (`saturation_rigidity/statement.md:53`) says `sum_x (m-d_x) = 1+O <= m`, i.e. `d_x = m` at all but `1+O` points. Pricing: this changes `sum_{x notin W} d_x` by at most `1+O <= m`, so it is worth a factor `1 + O(1/m)` — **negligible**, and I say so against my own registered guess.
- **(s3) the type-1 term is separately capped** and equals exactly `2` at `a = 8m-2` (`floor((8m-2)/(4m-1)) = 2`), so the type-2 term carries the whole budget. Worth `2` out of `4m`. Negligible.
- **(s4) no structure enters at all** — not apolarity, not MDS, not the Hankel pencil. This is the one that pays, and it pays through (s1).

**Quantifier claims, quoted.** `(SAT1)` profile `saturation_rigidity/statement.md:11-14`; `(SAT2)` `:33`; `(SAT3)` `T=4m+1=rho+2` `:40`; `(SAT4)` `:53`; `(SAT5)` `:59`; the incidence identities `I = T*rho - O` and `I = sum_x d_x <= N*m` at `saturation_rigidity/proof.md:38` and `:48`.

**The brief's "~39-order gap" is imprecise (P2 HIT, registered at 0.75).** The honest figures: `CAP/(rho+1) = (2^39+1)/6` and `CAP/(rho+2) = 2^38/3`, both `= 91625968981`, i.e. **11 decimal orders / 36 binary orders**, not 39. (`CAP` has 23 digits / 76 bits; `2^39` has 12 digits / 40 bits.)

**`m = 1` is structurally empty of the mandate's stratum (P7/P8 HIT, and it is a proof, not a measurement).** At `a = 8m-2`, `p in [R+1-a, rho] = [3, 4m-1]`; at `m=1` that interval is the single point `p=3`, and `wt(kappa) = a+p-n_0 = 9-n_0 >= R+1 = 9` forces `n_0 = 0`, hence `j = 0` for **every** type-2 slope. So the only banked failure witness — the `q=17` fence — contains **none** of the stratum this pilot was sent after. The `w*` window also degenerates to `[6,6]` there.

---

## D2 — STRUCTURE TRANSPORT

**What transports, and how.**

**(GNF) — the generalised reciprocal-locator normal form. TRANSPORTS COMPLETELY.** The sub-code of `K` supported in a set `Z` is `{(f(x)/sigma'_Z(x))_{x in Z} : deg f <= |Z|-(R+1)}` (dimension `|Z|-R`, matching `(L1)`). Hence for every type-2 slope

```text
kappa_{gamma,x} = f_gamma(x) / sigma'_{Z_gamma}(x),   deg f_gamma <= j_gamma,
Z_gamma = supp(kappa_gamma),   j_gamma = wt(kappa_gamma) - (R+1).
```

`j = 0` recovers apolar's `(AO2)` `kappa_x = 1/sigma'_{W u S}(x)` exactly. **Measured: `OK 280, BAD 0`** across the eight cells (`m=1,2,3,4`; `q in {17,97,193,257}`), with `kappa` built by *nullspace* so the check is independent of the formula. **P5 HIT.** But see MISS 9: this is a dimension count, and the same basis is banked in the `xr` lane.

**So `j >= 1` does NOT break the normal form.** It breaks **uniqueness**: the shortened code has dimension `j+1`, so `kappa` is no longer determined by its support. That is the honest statement of why `T4` does not transport — `T4`'s divisibility step (`sigma_{S_i} | sigma_{S_1}sigma_{S_2}`) needs the `1`-dimensional case.

**(EQ) — the identification of the stratum. HALF-TRANSPORTS.** `wt(kappa) = a + p - n_0` with `n_0 = #{x in W : kappa_x = 0} >= n_gamma`. Therefore *equality in `(C2)` `=> j = 0`* is a theorem, and the converse needs `n_0 = n_gamma`. Measured both directions `OK 121 / BAD 0`; the converse is **sampled, not proved** (MISS 5). Consequence at `a = 8m-2` with `n_0 = 0`: **`j = p - 3` exactly**, confirmed by the `j`-histograms — `m=2`: `j in {0,1,2,3,4}`; `m=3`: `{0..8}`; `m=4`: `{0..12}`, each value hit exactly as often as its `p`.

**(TR1') — the MDS transport dichotomy. TRANSPORTS, needs no minimum-weight hypothesis.** Any three supported slopes admit a nonzero relation `c_1 v_1 + c_2 v_2 + c_3 v_3 in K` (their syndromes span only a `2`-space), supported in `S_1 u S_2 u S_3`. Hence

> either `|S_1 u S_2 u S_3| >= R+1`, or the relation vanishes identically, in which case `v_3 = alpha v_1 + beta v_2` and `S_3 subseteq S_1 u S_2`.

**Measured: `646` triples, `645` in the first alternative, `1` in the second, `0` violations**, four scales, two fields each. Useful but **not binding**: averaged over all triples it leaves `~13m^4` of slack against the saturation layer (arithmetic done in-session; not reported as a bound).

**(OV) — the one that pays.** Stated in the VERDICT. It is a corollary of `apolar_origin/REPORT.md:57` with the quantifier made explicit. It is what `T4` and `(AO1)` both left on the table: `T4` bounds collinear families of `{P_S}`, `(AO1)` bounds `T` *given* `a`; **neither bounds `a`.**

**What does NOT transport, posed exactly.** `T4`'s pencil census needs the reciprocal-locator points to live in a **common** coordinate space `W`. For a non-minimum-weight type-2 slope, `kappa_gamma|_W = z_gamma|_W - v_gamma|_W` and the deviation `v_gamma|_W` is supported on `S_gamma ^ W != {}` — different slopes deviate in different coordinates, so there is no single point set whose collinearity can be tested. **That obstruction is real and I did not remove it.** The route that worked went around it (counting on `w*`), not through it.

---

## D3 — THE SCALED CENSUS

Machinery (`d3_census.py`, written from scratch, stdlib only): `D = mu_N`, syndromes `sigma_i = A_i + gamma B_i`, Berlekamp-Massey with an early abort at linear complexity `> rho` (legal: `2rho = 8m-2 < R = 8m`, so the shortest LFSR is unique), root split over `D`, then a Vandermonde solve for `v_gamma`. Supported `<=>` `L <= rho` **and** `Lambda` splits into `L` distinct roots in `D`.

Two modes. **MODE A**: random `(v_1,v_2)` with prescribed `|S_1 ^ S_2| = 2rho-a` at `a in {4m+2, 6m, 8m-2}`. **MODE B (targeted)**: `W = S_1 u S_2` disjoint; choose `P` outside `W` with `|P| = p`; build `kappa in K` supported on `Z = W u P` by nullspace; set `v_1 := kappa` off `S_3` (free on `S_1 ^ S_3`), same for `v_2`; then `v_3 = v_1+v_2-kappa` is automatically supported in `S_3`. This realises the stratum on demand at every admissible `p`.

Scales and fields: `m in {1,2,3,4}`, `q in {17,97}`, `{97,193}`, `{97,193}`, `{193,257}` — `16m | q-1` in all eight cells. Two-field agreement on every structural number. 1410 pencils analysed in total.

| `m` | `q` | pencils | mode-B `T` hist | type-2 | `j=0` | `j>=1` | max `T_2^{>}` | `CAP(m,8m-2)` |
|---|---|---|---|---|---|---|---|---|
| 1 | 17 | 80 | `{3:20}` | 20 | 20 | **0** | 0 | 3 |
| 1 | 97 | 80 | `{3:20}` | 20 | 20 | **0** | 0 | 3 |
| 2 | 97 | 305 | `{3:125}` | 125 | 25 | 100 | 1 | 12 |
| 2 | 193 | 220 | `{3:100}` | 100 | 20 | 80 | 1 | 12 |
| 3 | 97 | 228 | `{3:108}` | 108 | 12 | 96 | 1 | 26 |
| 3 | 193 | 180 | `{3:90}` | 90 | 10 | 80 | 1 | 26 |
| 4 | 193 | 179 | `{3:104}` | 104 | 8 | 96 | 1 | 45 |
| 4 | 257 | 138 | `{3:78}` | 78 | 6 | 72 | 1 | 45 |

**`m=1` gives `T_2^{>} = 0` at both fields — matching the proof in D1.5, not merely consistent with it.**

**Pre-registered extrapolation (P10), run as registered.** `L(m) = CAP(m,8m-2)/max(1,TRUE(m))` with `TRUE` the measured per-pencil max: `L = 3, 12, 26, 45` at `m = 1,2,3,4`; least-squares exponent over `m in {2,3,4}` is **`p = 1.907`**, inside my registered `[1.0, 2.0]` and inside the narrow `[1.6, 2.0]`. **P10 HIT** — and immediately declared worthless as an extrapolation (R6.4): `TRUE` is a max over a sample of `T = 3` configurations, and `CAP ~ (8/3)m^2` is doing all the work.

**The census's own headline finding is a NEGATIVE about the census.** The `w*`-minimality counter fired **906 times in total** (pairs: `0/0/157/130/167/139/181/132`) in MODE B: **planting a third slope at `a = 2rho` makes the true `w*` drop below `2rho`.** I registered no prediction about this; it is the empirical shadow of (OV), and it is what sent me back to re-derive D1.6. At `m=1` the counter is **0** at both fields — the fence really does sit at `w* = 2rho = 6`.

---

## D4 — VERDICT + RESIDUALS

**The sharpened cap (exact, with proof sketch and falsifier).**

> **Theorem (conditional on `(SAT1)-(SAT4)` and `T = rho+2`).** `w* <= 2rho - Lmin(0)/C(T,2)` where `Lmin(0) = (N-1)C(m,2) + C(m-1,2)`; asymptotically `w* <= 7m-1`. Consequently the non-minimum-weight type-2 count obeys `T_2 <= CAP(m, 7m-1) = floor((9m+1)m/(m+2)) = 9m - 17`, and `T <= 9m - 15`.
>
> *Proof sketch.* (a) `(OV)`: for distinct supported `gamma, gamma'`, `(v_gamma, v_gamma')` is a `D`-representation of the syndrome pair up to `GL_2`, and joint support is `GL_2`-invariant, so `w* <= |S_gamma u S_gamma'|`, i.e. `|S_gamma ^ S_gamma'| <= (rho-o_gamma)+(rho-o_gamma') - w*`. (b) Sum over all `C(T,2)` pairs; the left side is `sum_x C(d_x,2)` by double counting. (c) `(SAT4)` gives `sum_x (m-d_x) = 1+O` with `d_x <= m`, so by convexity `sum_x C(d_x,2) >= Lmin(O)`. (d) Solve for `w*`; the bound is monotone in `O` with slope `(T-1) - (C(m,2)-C(m-1,2)) = 3m+1 > 0`, so `O = 0` is tightest. (e) `CAP(m,a)` increases in `a`. **QED (sketch).**
>
> *Falsifiers.* **F1 (live):** a realizable strict-`A=3` configuration with `T = rho+2` and `w* > 7m-1`. **F2:** distinct supported slopes with `|S_gamma u S_gamma'| < w*`. **F3:** any measured configuration with `sum_{gamma<gamma'}|S_gamma ^ S_gamma'| != sum_x C(d_x,2)`. **F4:** a configuration with `sum_x(m-d_x) = 1+O` but `sum_x C(d_x,2) < Lmin(O)`. F3/F4 are identity checks and were exercised with 0 violations in every census cell; **F1 was NOT exercised — the census never reached `T > 3`.**

**Exact ledger at `m = 2^37`** (`d4_verdict_results.txt`):

```text
budget rho+1                = 549 755 813 888            = 2^39
banked residual-(ii) cap    = 50 371 909 150 701 174 915 072
sharpened  a_max            = 962 072 674 303            = 7m-1
sharpened  cap              = 1 236 950 581 231
sharpened  AO1              = 1 236 950 581 233
shrink                      = 40 722 652 881 x           = 10.61 decimal orders
remaining gap               = 2.2500 x     (was 9.1626e10 x)
```

**Small-`m` ledger:** `a_max` `13/20/27/55` at `m = 2/3/4/8` (vs `14/22/30/62`), caps `9/16/24/58` (vs `12/26/45/176`), ratios to `rho+1` climbing `1.37 -> 1.50 -> 1.62 -> 1.87 -> 2.19 -> 2.24` and converging to `9/4`. The `a_max+1` check fails at every `m` tested — the ceiling is tight to the integer.

**THE HONEST FRONTIER, named to the constant.** The `(AO1)`/counting route closes `a` iff every type-2 slope satisfies `|S_gamma \ W| >= (N-a)e/(rho+1-T_1)`. At `a = a_max` that is `p* = 2m+2 + o(m)`; `(OV)` now supplies `R+1-a_max = m+2`. **The exact missing ingredient is a factor of 2 in the per-slope spend floor:**

> **(FR)** For a non-minimum-weight type-2 slope of a strict-`A=3` pencil at `T = rho+2`, `|S_gamma ^ W| <= ~2m` — i.e. a type-2 locator may share at most half of its roots with the **minimum** joint support.

`(OV)` gives exactly this statement pairwise, against one other locator set at a time (`|S_gamma ^ S_gamma'| <= 2rho - w* ~ m`). What is missing is the same statement **against all of `W` at once**. Note that the mean is already right — the saturation layer forces mean `|S_gamma ^ W| ~ 2m-2` — so (FR) is a *max-vs-mean* upgrade, precisely the kind of step that `background/nodes/l1_fpc5_ratehalf_m4_t2_distance_only_no_go/upstream_crosswalk.md:8-10` warns cannot come from support weights and pairwise overlaps alone in the sibling lane. **If that no-go transports, `9/4` is the ceiling of this route and the next instrument must be algebraic (the `(GNF)` polynomials `f_gamma`, or the Hankel pencil), not combinatorial.**

**Residual (ii) after this round, restated for the ledger.** Not closed. Reduced from *"cap `5.04e22`, `w*` window share `2/3`"* to *"cap `1.237e12`, `w*` window share `5/12`, residual factor `9/4`, one named missing inequality (FR)"*. Residuals (i) (the 1-or-3 `w*` tiling gap) and (iii) (`m=1`) are untouched by this round, and `m=1` is now known to be **structurally disjoint** from residual (ii).

---

## PREDICTIONS vs OUTCOMES

| | registered | outcome |
|---|---|---|
| P1 | `5.04e22 = floor((8m+2)m/3) = 2^38(2^39+1)/3 = 50371909150701174915072` | **HIT exact**, including the closed form and the no-floor-loss check |
| P2 | brief's "~39-order" wrong; true gap `2^38/3 ~ 9.16e10`, 11 decimal / 36.4 binary | **HIT** — 11 decimal, 36 binary, `CAP/(rho+2) = 2^38/3` exactly |
| P3 | `CAP` monotone in `a`; `CAP(m,4m+2)/m in [2.9,3.0]`; crossing `[5.30,5.34]` | **HIT** — monotone at `m=2,8,64`; `CAP(m,4m+2) = 3m` exactly at `m >= 2^10`; crossing `16/3` |
| P4 | `(EQ)` iff, 100% | **PARTIAL** — forward direction proved, converse only measured (`121/121`) |
| P5 | `(GNF)` exact, 100% | **HIT `280/280`** — but tautological and a port (MISS 9) |
| P6 | `TR1'` 100%; fraction with `\|u S\| <= R` in `[0,0.35]` | **HIT (0 violations); fraction `1/646 = 0.0015`, window unexercised** |
| P7 | fence `T_2^{>} = 0` | **HIT — and upgraded to a proof for all `m=1` configurations** |
| P8 | `m=1` has zero power to separate the strata | **HIT (proved: `p in [3,3]`)** |
| P9 | `TRUE(m) <= 2` for `m <= 4`, `TRUE(1) = 0` | **HIT (`0,1,1,1`) but ZERO POWER — max over `T=3` samples** |
| P10 | fit `p in [1.0,2.0]`, likely `[1.6,2.0]` | **HIT — `p = 1.907`** |
| P11 | mean `\|S\W\|/m in [1.8,2.2]` at official params | **HIT — `p* = 2m+2`, mean `~2m+1.5`** |
| P12 | no close | **HIT as a registered miss** |
| P13 | `>= 1` CATCH-24A subtraction lands | **HIT — four landed: `(GNF)`, `w* <= \|S_i u S_j\|`, `7m-1`, R4** |
| R5 | `P(cap crude by >= 10 orders)` = 0.20 (non-circular reading) | **the 0.20 branch RESOLVED YES** — 10.61 decimal orders, non-circular, derived |
| R5 | `P(closes under 2^39)` = 0.10 | **did not close** |
| R5 | binding obstruction = `S ^ W != {}` breaking the normal form | **PARTIAL MISS** — normal form survives (GNF); the wall is the spend floor (MISS 4) |

---

## ZERO-POWER DECLARATIONS

1. **The census has zero power over the failure configuration.** Every pencil analysed had `T <= 3`; `(SAT3)` requires `T = rho+2` (`9` at `m=2`, `2^39+1` officially). Nothing measured this round bears on the extremal configuration, and **falsifier F1 for my own main theorem was not exercised.**
2. **`TRUE(m)` is a max over a sample**, never exhaustive over `W` (`C(32,14) = 4.7e8` already at `m=2`). It is a **lower** bound on the true max: it can falsify, never bound.
3. **MODE A's null result (0 type-2 in 765 random pencils) is not a rarity measurement.** It measures the sampler.
4. **The `p = 1.907` looseness exponent has zero power as an extrapolation** to `m = 2^37`; it is descriptive over four points at `m <= 4`. The non-circular official-scale statement is the *derived* shrink `40722652881x`, which uses no small-scale data at all.
5. **`m=1`/`q=17` numbers are controls.** The `w*` window degenerates to `{6}` there and the stratum is provably empty.
6. **No claim decays in `q`,** so nothing here needs the `q >= 2^167` regime — but equally, nothing here rules out a bad configuration at large `q`; (NEWCAP) is uniform in `q` and that is its whole content.
7. **(EQ)'s converse and the `n_0 = n_gamma` condition are sampled, not proved** (121 slopes, four scales, two fields).
8. **The `9/4` is a ceiling on THIS route, not on the problem.** I have no evidence that `(FR)` is false, and none that it is true.

---

## MEASURED FUNCTIONALS (CATCH-19C)

`rho, N, R, R1 = R+1, e = m, delta = m-1, A = 3, T = rho+2` (SAT1/SAT3); `W`, `a = w*` = **minimum** joint support; `S_gamma`, `u_gamma = |S_gamma|`, `o_gamma = rho-u_gamma`, `O = sum o_gamma`; `d_x`; `n_gamma`; `kappa_gamma = z_gamma - v_gamma`; **new here:** `Z_gamma = supp(kappa_gamma)`, `p_gamma = |S_gamma \ W|`, `n_0 = #{x in W : kappa_x = 0}`, `j_gamma = wt(kappa_gamma) - (R+1)` (the **weight excess**, the stratum index), `T_2^{=} = #{j=0}`, `T_2^{>} = #{j>=1}`; `CAP(m,a) = floor((N-a)e/(R+1-a))`; `T1cap(m,a,O)`; `AO1 = T1cap + CAP`; `Lmin(O) = (N-1-O)C(m,2)+(1+O)C(m-1,2)`; `a_max(m)` from (NEWCAP); `p*` = the spend floor that would close; `L(m)` = looseness ratio. Registered but **not measured**: nothing — every registered functional was either measured or explicitly declared (R6).

---

## COMPLIANCE

**Registrations.** R0-R8 (notation, the D1 anatomy hypothesis, (GNF), (TR1'), predictions P1-P13 with numeric windows, the three blind priors the brief demanded, seven zero-power declarations, route order, compliance plan) were appended to `PREREG.md` with the **Edit tool after reading exactly the two named anchors and before any other read, any grep, and any interpreter invocation**. No post-registration addenda were used.

**Compute law.** **Twelve interpreter invocations**, every one of the form `tools/ramguard tiny|local -- python3 ...` from the repo root with the literal `--` and an explicit `RAMGUARD_TIMEOUT`: `tiny` x4 (`RAMGUARD_TIMEOUT` = 60, 60, 90, 60) plus one `tiny` smoke test at 120, and `local` x7 (`RAMGUARD_TIMEOUT=290` each, for seven of the eight census cells; the `m=1, q=17` cell was the `tiny` smoke test). **Ramguard status: all twelve exited under the guard; one FAILED and is reported** — invocation 1 (`d1_anatomy.py`, `tiny`) died with a `MemoryError` materialising a length-`4m-1` list at `m = 2^37`; I rewrote the certificate in closed form rather than raising the profile, and re-ran under `tiny`. **Disclosed deviation:** two `tiny` runs carried `RAMGUARD_TIMEOUT` above the profile's nominal 60 s (120 and 90); both in fact completed in a few seconds, and the env var is a documented ramguard feature (`tools/ramguard` usage text), but the brief characterises `tiny` as 60 s and I am flagging it rather than leaving it implicit. No bare `python3` at any point. Stdlib only — no third-party imports, no Modal, no network, no git.

**RAM discipline.** `dag.json` **never opened** (node shards + grep only); file-at-a-time reads throughout; one grep produced a 3.3 MB persisted output and was immediately narrowed rather than re-run broadly; the census was written to hold `O(N + R^2)` state with an early Berlekamp-Massey abort, and the eight cells were run as separate checkpointed invocations each writing its own results file.

**Quarantine.** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` was **never opened at any line**. The three sibling round-31 directories (`rh_overlap_cap`, `rh_transport_dictionary`, `rh_e_axis_audit`) were **never read and never listed** — they are excluded by an explicit `grep -vE` filter on every recursive grep in this session, and no `ls` of `notes/pilots_20260810/` was run. No path containing `prize-codex-` was touched (also filtered on every grep). **No subagents were spawned**, so the propagation clause was not needed.

**Write scope.** Every write is inside `notes/pilots_20260810/rh_type2_stratum/`: `PREREG.md` (registrations appended), `d1_anatomy.py` + `d1_anatomy_results.txt`, `d2_transport.py` + `d2_transport_results.txt`, `d3_census.py` + eight `d3_m{m}_q{q}.txt` results files, `d4_verdict.py` + `d4_verdict_results.txt`. **`REPORT.md` itself was REFUSED by the harness** ("Subagents should return findings as text, not write report files"), so this report is returned verbatim as the final message per the brief's fallback clause; the directory therefore contains 14 files and no `REPORT.md`. **No** `dag/`, `nodes/`, `critical/`, `background/` or `tools/` edits; no git operations of any kind; the session scratchpad was not used.

**Banked scripts.** **None were executed.** I read `collinearity_object/d3_coverage.py` (lines 150-173) and `apolar_origin/d6_stratum.py` by `Read`/`grep` only, and wrote my own decoder from scratch. The "scratch copies only" rule is therefore satisfied vacuously — and the cost is MISS 3: this round carries **no replay-identity evidence**.

**Method discipline.** Own-repo greps (CATCH-24A) were run before every novelty claim and produced **four live subtractions**, two of which (`7m-1`; `w* <= |S_i u S_j|`) are load-bearing for the main result and are reported as ports with the direction-of-use as the only contribution. Two-field confirmation (`q` pairs `{17,97}`, `{97,193}`, `{97,193}`, `{193,257}`) for every structural claim; every quantifier claim above carries a `file:line`; every max-quantified claim carries a zero-power declaration; and the session's central self-falsification (MISS 2) is reported as a falsification of my own published conclusion, not retro-fitted.
