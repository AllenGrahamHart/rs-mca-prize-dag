# REPORT — cw_shared_target (persisted verbatim by the coordinator from the session transcript, task ae0601e93866fed17, 2026-08-07)

# THE CONSTANT‑WEIGHT CELL PRICED AS ONE TARGET — VERDICT: **TWO SEPARATE TARGETS**, with the divergence point named, proved at toy scale, and consistent with every banked official‑row datum

**Opus 5, 2026‑08‑07, round 23.** Artifacts, all in `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260807/cw_shared_target/`: `PREREG.md` (§R0–R5 appended **before** any computation, plus an OUTCOMES appendix added after), `cw.py`→`CENSUS.txt`, `attack.py`→`ATTACK.txt`, `adv.py`→`ADV.txt`, `consist.py`→`CONSIST.txt`. **130 PASS / 29 FAIL; every FAIL is a registered‑prediction miss or a strictness‑threshold miss, itemised below — none is a verifier error.** No `REPORT.md`. Nothing outside the pilot dir written (`find -newermt '-2 hours'` outside it returns empty); no `dag.json`/`nodes/`/`tools/` edit; no git; no Modal; no status flip; no closure claim.

---

## 0. Sources, quoted verbatim

**M4's crux** — `critical/nodes/rate_half_list_adjacent_crossing/statement_addenda/14-round22-u2-accident-cap.md:40-49`:

&gt; **CRUX RELOCATED.** In `X_w(gamma) &lt;= S(v) + Acc_deep + Acc_shallow`, the first two terms are now supplied (S(v) exact via SM(2); Acc_deep via U2). The remaining crux is `Acc_shallow` + aperiodic `S` — via the banked LEMMA Y/MW equality `W_w = BCH_w` (`w &lt;= p`, true at every official razor row), this is a CONSTANT‑WEIGHT POPULATION CAP for `BCH_w` in a prescribed sig class. The sharp deep‑stratum route is gated by the ternary minimum‑l1‑weight instrument (`integer_code_distance_cert`) — the same missing instrument as mystery 5's GE‑WEAK and the F2 lane's non‑local obligation (round‑22 f2_rlocality): the four‑lane convergence point.

**M4's sharp deep‑stratum route** — `notes/pilots_20260807/bb_nu_transport/PROOFS.md:389-403`:

&gt; **THE NEXT DECISIVE TEST.** An upper bound on `Acc_deep` better than U2 requires an **upper** bound on the weight enumerator of the relation set `R = { eps ∈ {0,±1}^L : Σ_{j&lt;L} eps_j θ^j = 0 in F_Q }`, because `A_deep(gamma) ≤ Σ_{eps ∈ R\{0}} C(L−U(eps), (r'_a−U(eps))/2)` (BB‑6, direction‑free)… Measured exhaustively: `#R ≈ 3^L/Q` to within 0.3% at `L = 16` (e.g. `p = 97`: `#R = 443777` vs `3^16/97 = 443780.6`), and the minimum support `U_min` is 3–4.

**M2's obligation** — `notes/pilots_20260807/f2_rlocality/PROOFS.md:614-626`:

&gt; **THE REQUIRED STATEMENT (the weakest one that closes the gap).** For a single interval `A subset F_p` with `rho = |A|/p = rho(1-c*) = 0.3826` and some `delta &gt; 0`, `#{ u in F_p^R : #{ s &lt; S : f_u(zeta^s) in A } &gt;= (1-delta) S } &lt;= p^R * 2^{-c* S + o(S)}`. Equivalently: **no codeword of the GRS value code `C*` is unusually smooth**…

**M2's terminal of record (the functional)** — `background/nodes/f2_z1_mass_knife_edge/statement.md:17-18` and `:55-56`:

&gt; **THEOREM Z‑FLOOR (pointwise first‑moment floor).** For EVERY F_p‑subspace, `Z(L) = sum_{eps in L^perp cap T} 2^{-wt(eps)} &gt;= 2^m / p^{dim L}`.

&gt; **THE OPEN TERMINAL (residual, not claimed):** prove `Z_1 &lt;= 2^{o(m)}` at `k = e`.

**The named bridge instrument** — `background/nodes/es_ternary_suppression_instruments/statement.md:92-97` (status `PROVED`; there is **no** dedicated CW‑FLOOR node — it lives as addendum item 3 on this node):

&gt; 3. THEOREM CW‑FLOOR (the constant‑weight Z‑FLOOR, r' even): `|X_r'| &gt;= C(L, r'/2)^2 / p^{delta_a}` — the round‑19 untested cell yields a real instrument; it upgrades the round‑18 heuristic tower‑row excess to a PROVED 2^205.71 (vs DSA's single‑fibre 2^104.27) and is vacuous at every prime row by 3.85 bits; unavailable at odd r' (proved).

**And its origin, which already banks the object identification** — `notes/pilots_20260806/crossing_gap/REPORT.md:83`:

&gt; The whole thing turns on one coincidence (registered as G2.1 and confirmed): **the constant‑weight collision multiplicity `C(L−U, W−U/2)` at `W+W' = r'` is identically LEMMA TC's fibre size `C(L−U,(r'−U)/2)`.** This is the exact constant‑weight analogue of THEOREM Z‑FLOOR, with the cube `2^L` replaced by the shell `C(L,r'/2)` and the difference‑multiplicity weight `2^{L−U}` replaced by LEMMA TC's binomial.

**Subtraction disclosed up front (hard law 5):** the shape of my H1 is that banked G2.1 sentence. I claim **no novelty** for it. What is new here is the *quantitative* ratio `GDEV`, the side‑by‑side pricing, the graded verdict, and the adversarial sweeps.

---

## 1. (D1) THE TWO CONTRACTS, EXACTLY

Named functionals (CATCH‑19C; all registered in `PREREG.md` §R0 before computing):
`TMASS(D) := Σ_{eps ∈ D ∩ {0,±1}^N} 2^{−wt(eps)}` (the ternary theta at ½ of an F_p‑subspace `D ⊆ F_p^N`; **this is exactly f2's `Z(L)` with `D = L^⊥`**); `SIGMA := N − κ·log2 p`; `HEUR := 1 + (2^N−1)/p^κ`; `CRATIO := TMASS/HEUR`; `EXCESS := (TMASS−1)·p^κ/(2^N−1)`; `GDEV(L,r',U) := [C(L−U,(r'−U)/2)/C(L,r'/2)]·2^U`.

| | **M2 (F2 terminal)** | **M4‑b (sharp deep stratum)** | **M4‑a (the LIVE crux)** |
|---|---|---|---|
| functional needed | `TMASS(L^⊥) = Z_1` | `TMASS(RSET)` | `X_w(γ)` / `|W_w|` on `BCH_w` |
| direction | **UPPER** | **UPPER** | **UPPER** |
| ternary length `N` | `m = S = 2.75e11` | `L = 2^{41−v} ≤ 128` | `n = 2^41` |
| codimension `κ` | `R = S/log2 p ≈ 2^32` | `δ_a = 1` (see SC‑1) | `w−1 = 2^35−1` |
| `SIGMA` | `+17.98` (exact‑balance) or `−46.02` | `+85.415` (v=34, witness) … `−38.585` (v=39) | not modelled (see §5) |
| quantifier | every admissible row; individual `u` | every shell `γ`; every row | every `γ`; every row |
| tolerance | **4.77 bits** (proved floor `2^17.98` → finite target `1+N^3 = 2^22.75`) | **54.45 bits** (`B* = 2^127.5098` minus banked proved floor `2^73.061`) | 54.45 bits |
| what is banked | Z‑FLOOR (LOWER), Z‑1 (`wt ≥ 2R+1 = 8,589,934,681`), Z‑2 (l1 moments to `2R`), Z‑NOGO | LEMMA TC **bijection**; U2 `= 2^117.0820`; U1 `= C(128,62) = 2^124.0820` | LEMMA Y/MW (`W_w = BCH_w`, `w ≤ p`); **nothing else** |
| bridge from the primal count to `TMASS` | **NONE — the terminal IS the functional** | **LEMMA TC, a bijection, 0 bits** | **collision/Cauchy–Schwarz only, ≥ 4.57e11 bits** |
| `ell` (odd‑power conditions feeding Z‑2) | `R = 2^32` ⇒ `wt ≥ 2R+1` | **`1`, PERMANENT** ⇒ `wt ≥ 3`, attained | `1`, PERMANENT |
| already sufficient? | **NO** (open terminal) | **YES at v ≥ 35** (`U1 &lt; B*`) | **NO** |

The `ell = 1` entry is banked, not mine — `critical/nodes/integer_code_distance_cert/statement.md:41-45`: *"the system supplies `ell = 1` odd‑power condition against the `ell = 65` the threshold needs, and `ell = 1` is PERMANENT: multi_multiplier_reduction (REFUTED) proves the k‑multiplier residue matrix is a rank‑1 outer product for every k. Z‑2 at `ell = 1` yields only "weight &gt;= 3", attained."*

---

## 2. (D2) THE SHARED‑FORM VERDICT — round‑19 gates, graded

### OBJECT — **PASS for {M2, M4‑b}. FAIL for {M2, M4‑a}.**

M4‑b's functional and M2's `Z_1` are the same functional up to an explicitly computed weight ratio. From LEMMA TC (`notes/pilots_20260806/crossing_low_w/PROOFS.md:169-178`) the deep‑stratum population is exactly

`Acc_deep_total = C(L,r'/2) · Σ_{eps ∈ RSET, eps≠0} GDEV(U)·2^{−U}`, `r' = L−2`,

so the two consumers weight the *same* ternary weight enumerator by `2^{−U}` (M2, exactly) and by `GDEV(U)·2^{−U}` (M4‑b). Measured `GDEV` (exact rationals, `CENSUS.txt` §1):

| L | 8 | 16 | 32 | 64 | 128 |
|---|---|---|---|---|---|
| `GDEV` at `U=2` | 1.0714 | 1.0500 | 1.0282 | **1.014881** | 1.0076 |
| `max_U GDEV` | 1.1429 | 1.4322 | 1.8980 | 2.5951 | 3.6073 |

Monotone increasing in `U` at every `L`; `max_U GDEV(L,L−2,U) = 2^{L−2}/C(L,L/2−1) = Θ(√L)`. The identity `Σ_{all eps} C(L−U,(r'−U)/2) = C(2L,r')` verified in exact integers at `L = 8, 16, 64`.

**But M4's LIVE crux is not this functional.** `Acc_shallow` + aperiodic `S` is the primal constant‑weight population on `BCH_w`, and it reaches `TMASS` only through a bridge (next gate).

### REGIME — **FAIL as posed; PARTIAL as a statement form.**

No parameter overlap: `N` differs by 9 orders (`2.75e11` vs `≤128`), `κ` by 9 orders (`2^32` vs `1`), `ell` by 9 orders (`2^32` vs `1`, permanently), and the tolerances by 11× (4.77 vs 54.45 bits). `SIGMA` straddles zero *within* M4 alone (`+85.415` at v=34 witness, `−38.585` at v=39). What **is** shared is the *statement form*, and both families obey it at toy scale — see §3.

### METHOD — **FAIL for M4‑a (fatally, by 10 orders of magnitude); PASS for M4‑b (but M4‑b is not on the critical path at v ≥ 35).**

This is the divergence point, and it is exact.

* **On the 2‑adically periodic strata**, LEMMA TC's fold `eps_j = [j ∈ S'] − [j+L ∈ S']` is a **bijection**. Verified independently: `FIB(fold) == NW(brute force over all C(2L,r') subsets)` at **20/20** toy cells, and `ACC = FIB − C(L,r'/2)` reproduces bb_nu_transport's banked `N_acc` at **12/12** cells exactly (416, 80, 16, 16, 0 at L=8; 4848608, 2432064, 1823616, 1332800, 1042272, 808256, 744128 at L=16). **Loss: 0 bits.**
* **Off them — i.e. exactly `Acc_shallow` + aperiodic `S`** — the only bridge is the collision bound `NW² ≤ Σ_{eps ∈ C∩T, balanced} C(n−U, r'−U/2)`. Measured loss `L2LOSS := ½log2(COLL) − log2(NW)` as a fraction of the total suppression `κ·log2 p`, at the eight `L=8`, `w=2` cells: **0.4993, 0.3932, 0.4966, 0.3961, 0.4054, 0.3963, 0.3563, 0.3120** — range `[0.3120, 0.4993]`, mean 0.4069, **never above ½**. This is PROPOSITION BR's break, banked at `crossing_gap/REPORT.md:85` (*"the floor loses exactly `log2 C(2L,r') − 2 log2 C(L,r'/2)` bits"*), measured here in the ceiling direction.
* **At the official row**: `κ = w−1 = 34,359,738,367`, `log2 p = 42.584963`, so `κ·log2 p = 1.46321e12` bits. At the **most favourable measured fraction (0.3120)** the collision bridge alone throws away **4.565e11 bits**. M4's *entire* tolerance is **54.45 bits**. Ratio **8.38e9**.

**Conclusion: no unification language.** OBJECT passes only on the sub‑need that M4 does not need; METHOD fails on the sub‑need M4 does need.

### The weakest common strengthening, and its toy‑scale test

**EXCESS‑CEILING(C)** (the exact upper companion of the proved THEOREM Z‑FLOOR): `TMASS(D) − 1 ≤ C·(2^N−1)/p^κ` for every admissible `D`.
**CRATIO‑CEILING(C)** (weaker): `TMASS(D) ≤ C·(1 + (2^N−1)/p^κ)`.

**Tested before proposing, adversarially, in both families on 2‑power grids** (`ATTACK.txt` §A, `ADV.txt` §ADV‑1/2):

| sweep | cells | max `EXCESS` | max `CRATIO` |
|---|---|---|---|
| M4 family, `L=4`, `p&lt;200000` | 4466 | 0.0000 (`RSET = {0}` at every `p &gt; 8`) | — |
| M4 family, `L=8`, `p&lt;30000` | 2229 | **0.9375** (p=17); last `p` with a relation **881** | — |
| M4 family, `L=16`, `p&lt;20000` | ~150 | **1.3343** (p=18401) | **1.2610** (p=18401) |
| M2 family `(S,R)=(8,2)`, `p&lt;30000` | 279 | 0.2833 | — |
| M2 family `(S,R)=(16,2)`, `p&lt;20000` | 32 | **2.3463** (p=3137) | ≤1.2610 |
| M2 family `(S,R)=(8,3)`, `(16,4)` | 311 | **0.0000** (ternary kernel `= {0}` at every swept `p`) | — |

&gt; **The registered adversarial search found a counterexample.** **EXCESS‑CEILING(C=2) is FALSIFIED** at `(S,R,p) = (16,2,3137)`: `EXCESS = 2.3463`, driven by 32 ternary kernel vectors of weight 11 against a heuristic mass of `2^{−7.23}`. The excess does not look bounded (2.13 at p=1409, 1.70 at 1889, 2.35 at 3137, tracking `SIGMA → −∞`). Reproduce: `tools/ramguard local -- python3 notes/pilots_20260807/cw_shared_target/adv.py`.

**What survives is the CRATIO form, with `C ≤ 1.2610` over every swept cell of both families (0 violations).** Z‑FLOOR held at 12/12 M4 cells and 6/6 M2 cells; Z‑1 (`min ternary weight ≥ 2R+1`) held at **622/622** swept M2‑family cells.

&gt; **Catch for the maintainer (a normalization distinction, not a contradiction).** `f2_z1_mass_knife_edge/statement.md:22-24` reads *"Tight within a factor 2 of the ensemble mean (no subspace beats random by more than 2x). 696 configurations, exact rationals, 0 violations."* That factor‑2 calibration licenses the **CRATIO** normalization (my max 1.2610, consistent). In the **EXCESS** normalization — which is the one a consumer at `SIGMA &lt; 0` actually needs — the factor exceeds 2 inside f2's own family. Worth pinning which normalization the banked calibration covers.

**Licensing controls, from a from‑scratch code path.** `ZTOY(17,8,2) = 1.250000` and `ZTOY(97,16,2) = 9.387207` — the banked G1 and G4 values of `tern_route_b/PROOFS.md:124-127`, reproduced exactly (cf. `f2_rlocality/REPORT.md:81`). CW‑FLOOR's banked `2^205.71` reproduced as `2·log2 C(128,63) − log2 p = 205.7132`.

---

## 3. (D3) THE FIRST ATTACK — what the surviving form buys each consumer

**Chain (an identity + one exact finite bound + the assumed ceiling; no inequality transferred without its own proof):**
`Acc_deep_total = C(L,r'/2)·Σ_{eps≠0} GDEV(U)2^{−U}` (LEMMA TC identity, 20/20 + 12/12 verified) `≤ C(L,r'/2)·GDEVmax(L)·C·(2^L−1)/p^{δ_a}`.

**M4** (`CONSIST.txt`; log2 throughout; `B* = 2^127.5098`):

| v | L | S(v) | U2 (banked) | SIGMA (witness) | CEIL C=2, witness | CEIL C=2, e=1 @2^129.585 |
|---|---|---|---|---|---|---|
| 34 | 128 | 117.1491 | **243.6279 (vacuous)** | +85.415 | **212.4150 (still vacuous)** | **125.4150 → BELOW B\*, +2.0947 bits** |
| 35 | 64 | 54.6242 | 117.0820 (+10.4278) | +21.415 | 84.4150 (**+43.0947**) | −2.5850 |
| 36–39 | 32…4 | — | already below `B*` | — | below | below |

* At **v ≥ 35 the ceiling changes no verdict** — `U1 = C(128,62) = 2^124.0820 &lt; B* = 2^127.5098` already, i.e. **the *trivial* ternary bound `TMASS ≤ 2^L` suffices** (registered H4, HELD). It buys a 32.67‑bit margin improvement at v=35, nothing more.
* At **v = 34** it de‑vacuums **only the `e = 1` prime rows**, margin **+2.0947 bits** — precisely the rows `13-wave47-theorem-bb.md:12-13` records as *"untouched and provably unreachable by the method."*
* **It must NOT de‑vacuum the tower rows, and it does not — by 84.9053 bits.**

**The consistency test against THEOREM BB (the sharpest check I ran).** `13-wave47-theorem-bb.md:3-9` proves at break‑region tower rows `max-shell X_{2^34} &gt;= 2^199.575 &gt; B*`. Composing it with the LEMMA TC identity gives a **banked official‑row lower bound on the shared functional**: `EXCESS ≥ 2^{−11.8400}`, i.e. the true ternary theta at the official object sits **11.84 bits below** its volume heuristic. **The only official‑row datum that exists about this functional is consistent with the proposed ceiling, and does not refute it.** That is real evidence, from the official row, not a toy.

**M2** (`ATTACK.txt` §C): under the exact‑balance reading (`SIGMA = +17.98`), CRATIO‑CEILING(C) gives `Z_1 ≤ C·(1+2^{17.98})`, meeting the finite target `2^{22.75}` iff `C &lt; 2^{4.77}` **strictly** (at `C = 2^{4.77}` the value is exactly 22.7500 — that is the single "FAIL" line in `ATTACK.txt` §C, a boundary equality, and I report it as such). At the toy‑measured `C ≤ 1.2610` it gives `Z_1 ≤ 2^{18.31}`, **4.44 bits of headroom**. Under the `R = ceil(t/2)` reading (`SIGMA = −46.02`) the target is met trivially — which is itself informative: the terminal is only *open* under the exact‑balance reading.

**Calibration clause honoured** (`f2_z1_mass_knife_edge/statement.md:97-98`, *"No toy is evidence about Z_1 at the official row"*): every toy number above is evidence about the **form** of the ceiling and about identities, never about `Z_1` at the official row. The M4 official‑row consequences are **conditional on an unproved ceiling** and are labelled as such throughout.

---

## 4. (D4) THE VERDICT FOR THE BOARD — **TWO SEPARATE TARGETS**

**The exact divergence point, in one sentence:** *the bridge from the primal constant‑weight population to the ternary theta is a bijection exactly on the 2‑adically periodic strata (LEMMA TC), and `Acc_shallow` + aperiodic `S` is by definition their complement; off them the only available bridge is the collision/Cauchy–Schwarz step, whose measured loss is 0.31–0.50 of `κ·log2 p` — at the official row ≥ 4.565e11 bits against a 54.45‑bit tolerance.*

Three further separations, each with a number: **direction** (the named bridge instruments — THEOREM CW‑FLOOR and THEOREM Z‑FLOOR — are both **LOWER** bounds; *both* consumers need the UPPER companion, which nothing in the bank supplies); **`ell`** (M2 gets `wt ≥ 2R+1 = 8,589,934,681` from Z‑2; M4 gets `wt ≥ 3`, attained, permanently); **tolerance** (4.77 vs 54.45 bits).

**What the round‑22 "FOURTH lane convergence" (`f2_z1_mass_knife_edge/statement.md:160-162`) actually is,** stated honestly: a genuine convergence on the **object** (one functional, `TMASS`, already banked as G2.1) and on the **missing direction** (both need the ceiling; only the floor is proved), but **not** a convergence on the bottleneck — M2 is closed by the shared form, M4 is not.

**Re‑pose draft for the surviving instrument** (offered as a candidate for the board; the *proposer* is the coordinator, I flag, do not flip):

&gt; **CONJECTURE Z‑CEILING (the upper companion of THEOREM Z‑FLOOR).** There is an absolute constant `C` such that for every admissible F_p‑subspace `L` on the 2‑power grid, `Z(L) = Σ_{eps ∈ L^⊥ ∩ T} 2^{−wt(eps)} ≤ C·(1 + 2^m/p^{dim L})`.
&gt; **Consumers:** M2's open terminal, completely, provided `C &lt; 2^{4.77}`. M4's deep stratum at `v = 34`, `e = 1` prime rows only (+2.0947 bits at `C = 2`); nothing at `v ≥ 35`; **nothing for `Acc_shallow`**.
&gt; **Registered falsifier:** any admissible `(N, κ, p)` on the 2‑power grid with `CRATIO &gt; C`. Current status: `C ≤ 1.2610` over 7,000+ exhaustively swept cells in both families, 0 violations; the **sharper EXCESS form is already FALSIFIED at `(S,R,p) = (16,2,3137)` with `EXCESS = 2.3463`, so it must not be stated in that form.**
&gt; **Hypothesis that is load‑bearing:** the 2‑power grid (CATCH‑Z6). At composite `2L` the p‑free cyclotomic relations drive `EXCESS` to **178.51** (L=6, p=19993) and it grows linearly in `p`.

---

## 5. Registered predictions vs outcomes, and self‑corrections stated plainly

| reg. | outcome |
|---|---|
| Q1 | **SPLIT.** Monotonicity HELD at all `L`; `GDEV(64,62,2) = 1.014881` HELD (registered `1.0149±0.001`). **Band `[1,1.6]` FALSIFIED** at `L = 32/64/128` (1.8980/2.5951/3.6073). Corrected law: `max_U GDEV = 2^{L−2}/C(L,L/2−1) = Θ(√L)`. |
| Q2 | **HELD, 12/12 exactly.** |
| Q3 | **HELD.** `CRATIO ≤ 1.2610` everywhere on the 2‑power grid, both families. |
| Q4 | **FALSIFIED as registered** (predicted `CRATIO &gt; 100` at composite `2L`; measured max 1.51). The mechanism was right, the normalization wrong: in the EXCESS form it reaches 178.51. |
| Q5 | **FALSIFIED, both clauses.** M4's `USTAR = 8 = L/2` (bulk), not `UMIN = 3`; M2's G1 `USTAR = 0`. **H5 is dead.** Corrected law, identical in both families: `USTAR` is governed by `SIGMA` — bulk `N/2` when `SIGMA ≫ 0`, `eps = 0` when `SIGMA &lt; 0`. This *strengthens* OBJECT and moves the divergence entirely onto METHOD. |
| Q6 | **SPLIT.** Fraction in `[0.3120, 0.4993]`, mean 0.4069; registered threshold 0.40 fails at 4/8 `L=8` cells, and all 12 `L=4` cells are degenerate (`RSET = {0}`, `NW` = structural fibre only) so the registered form does not apply there. §2's conclusion uses the **most favourable** measured fraction and is unaffected. |
| Q7 | **SPLIT**, and superseded by SC‑1. |
| Q8 | **HELD but MIS‑REGISTERED BY ME.** `3.85` reconstructs as `128 − log2 C(128,63) = 128 − 124.1491 = 3.8509` at **v = 34**, reference `log2 p = 128`; my PREREG guessed `v = 35` / the witness `p`. Not a correction against the node — a reconstruction, and it matches. |
| H1/H4 | **HELD.** H2 **SPLIT** (EXCESS form falsified; CRATIO form survives). H3 **HELD** with SC‑1's correction. |

**SC‑1 (my own defect; the biggest thing I got wrong).** `attack.py` §B used `κ = e` (the extension degree) for the deep‑stratum relation set. The correct codimension is `κ = δ_a = 1` on every break‑region row (`p ≡ 1 mod n_a`, so `θ ∈ F_p`) — bb_nu_transport's own *"the measured U2 loss factor tracks `Q = p`"* (`REPORT.md:63`). **I found it because the wrong value made the proposed ceiling assert `Acc_deep(v=34, witness) ≤ 2^126.0`, contradicting banked THEOREM BB's `≥ 2^199.575` by 73.575 bits.** The contradiction is what located the error. `consist.py` is the corrected section; with `κ = 1` the ceiling is consistent with BB (slack 11.8400 bits) and de‑vacuums v=34 only at the `e=1` prime rows. **Every `κ = e` number in `ATTACK.txt` §B is superseded by `CONSIST.txt`.**

**SC‑2.** My PREREG §R1 wrote *"`SIGMA = +46.02` (the knife‑edge constant Delta)"* for M2. Wrong sign and wrong reading: `46.02` is the margin by which Z‑FLOOR is **silent** (`SIGMA = −46.02`) under the banked `R = ceil(t/2)` reading; `SIGMA = +17.98` under the exact‑balance reading. Corrected throughout the report.

**SC‑3.** My `check()` helper mixes verifier assertions with registered predictions, so the raw "29 FAIL" overstates. Itemised: 3 = Q1 band, 1 = Q4, 20 = Q6 (12 degenerate `L=4` + 8 threshold), 1 = Q7 boundary (`SIGMA = 0.0000` exactly at my chosen reference `p = 2^128`; at the live‑window floor `2^129.5849625` it is `−1.585`), 3 = the H2/EXCESS falsification (the finding itself), 1 = the `C = 2^{4.77}` float boundary. **Zero verifier errors.**

**Not claimed:** any status flip; that Z‑CEILING is true (it is a conjecture, and its sharper form is already falsified); that any toy is evidence about `Z_1` or about `X_w` at an official row; that `Acc_shallow` is bounded; that mystery 2's terminal is closed; anything about the `t`‑reading.

**Rule compliance.** Every `python3` went through `tools/ramguard local -- python3 …` from the repo root, with the literal `--`; all files were authored with the harness Write/Edit tools (no shell, no python), so no bare‑`python3` patching. Stdlib only. 2‑power grids (CATCH‑Z6) with the composite grid used only as a declared invalid control; `Λ = {1,3,…,2R−1}` so exponent 0 never occurs (CATCH‑19B); every measured functional named in PREREG §R0 before computing (CATCH‑19C). **QUARANTINE honoured:** `CAMPAIGN_LEDGER.md` never opened; the three sibling round‑23 pilot dirs never read; the clause was passed **verbatim** to the single read‑only search subagent I dispatched, which confirmed compliance in its return.

**result:** The constant-weight cell is ONE OBJECT and TWO TARGETS — mystery 2's terminal `Z_1` and mystery 4's deep-stratum accident term are provably the same functional `TMASS(D) = Σ_{eps ∈ D∩{0,±1}^N} 2^{−wt}` up to the exactly-computed ratio `GDEV ∈ [1, 2^{L−2}/C(L,L/2−1)] = [1, Θ(√L)]` (`GDEV(64,62,2) = 1.014881`), verified by reproducing bb_nu_transport's `N_acc` at 12/12 cells and the LEMMA TC bijection at 20/20 cells; but the round-19 gates do NOT all pass, so no unification language: OBJECT passes only for the sub-need M4 does not have (the trivial bound `U1 = C(128,62) = 2^124.0820 &lt; B* = 2^127.5098` already suffices at `v ≥ 35`), and METHOD fails for the sub-need M4 does have, because `Acc_shallow` + aperiodic `S` lies exactly off the periodic strata where LEMMA TC's fold is a bijection, and the only remaining bridge — the collision step — was measured to lose 0.31–0.50 of `κ·log2 p`, i.e. ≥ 4.565e11 bits at the official row against M4's entire 54.45-bit tolerance (ratio 8.4e9), while mystery 2 pays no bridge at all since its terminal IS the functional; the weakest common strengthening (CONJECTURE Z-CEILING, the never-drawn upper companion of the proved THEOREM Z-FLOOR) was tested adversarially before being proposed and its sharp EXCESS form was FALSIFIED at toy scale at `(S,R,p) = (16,2,3137)` with `EXCESS = 2.3463 &gt; 2`, leaving only the ratio form which survives 7,000+ exhaustively swept cells of both families at `C ≤ 1.2610`, closes mystery 2's 4.77-bit finite target with 4.44 bits of headroom, and for mystery 4 de-vacuums `v = 34` at the `e = 1` prime rows only (+2.0947 bits) while correctly NOT de-vacuuming the tower rows (by 84.9053 bits) in agreement with THEOREM BB — whose `2^199.575` floor, composed with the LEMMA TC identity, supplies the first official-row datum on the shared functional and puts it 11.84 bits BELOW its volume heuristic, consistent with the conjecture rather than refuting it; four registered predictions were falsified (Q1's band, Q4's normalization, Q5/H5's dominating-weight hypothesis, and H2's sharp form) and one modelling defect of mine (`κ = e` instead of `κ = δ_a = 1`) was caught only because it made my own conclusion contradict a banked theorem.
