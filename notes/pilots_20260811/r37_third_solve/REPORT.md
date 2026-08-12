All deliverables executed; six ramguard runs, six clean exits. Here is the full REPORT text.

---

# REPORT — r37_third_solve (round 37)

## VERDICT (first)

**THERE IS NO THIRD EXACT SOLVE, AND I CAN NOW SAY EXACTLY WHY: THE (PAR) LADDER HAS EXACTLY TWO RUNGS BECAUSE THE PARAMETRIZATION IS A LENGTH-4 SEQUENCE.** Writing `(u_0,u_1,u_2,u_3) = (k,f,g,-h)`, round 36's `(PAR)` is the **2×2-minor (cross-product) vector of the 2×3 Hankel matrix `[[u_0,u_1,u_2],[u_1,u_2,u_3]]`**: `L·(Q_2,-Q_1,Q_0) = -(row_0 × row_1)` — verified `58/58` at `q=97` and `59/59` at `q=193` (`d1_results.txt:3,6`). Prescribing `Q_0` split consumes the slot `u_0=k`; prescribing `Q_2` split consumes `u_3=-h`; **`Q_1` is then the third minor of an already-determined sequence — there is no polynomial left to invert.** After Möbius re-basing to `{0,1,∞}` the third prescription becomes an **overdetermined type-(4,4) Cauchy (rational) interpolation problem**: `f/g` must take 14 prescribed values on `S_0 ∪ S_∞`, against `4+4+1 = 9` degrees of freedom and only `2` free scale ratios — **deficit 3, i.e. `q^{-3}` per subset-triple** (`d4_results.txt:56-62`). Not a proportionality, not a norm condition: a **lattice-minimum / rational-interpolation** condition, with an exact `O(1)` test but no solve.

Three things did land, and one of them is the round:

1. **THE `s ≠ 0` CRITERION IS EXACT AND PURELY COMBINATORIAL: `s = |S_0 ∩ S_2|`.** `251/251` agreement, zero disagreements, two fields (`d2_results.txt:19,25`), joint histogram perfectly diagonal `[(0,0):28,(1,1):75,(2,2):71,(3,3):18,(4,4):6]` at `q=97` (`:18`). Round 36's `42/46` mortality (`r36_sat3_on_l2/REPORT.md:38`) is entirely explained: the meet-in-the-middle enumerated all `C(32,7)` subsets including those meeting `S_0`. **Restricting `S_2 ⊆ mu_32 \ S_0` gives a 100% `s=0` yield and a 7.00× smaller search space** (`d4_results.txt:47-48`). Measured `s=0` fraction `0.1414` against the predicted `C(25,7)/C(32,7) = 0.1428` (`d2_results.txt:20`).
2. **`T = 4`, ON CERTIFIED `e = m = 2` OBJECTS, ON TWO FIELDS — over a BESPOKE domain.** `1` instance at `q=97` and `4` at `q=193` (`d3_results.txt:4,12`), both records fully certified from scratch against the original `36×32` system: `deg(7,7,7)`, seprank 3, `s=0`, nullity 1, `M(Z)Q_Z=0` entrywise true, generic rank 7, one reduced rank-drop point (rank 6, none at infinity), zero degree-`≤1` kernel vectors (`d5_results.txt:4-11,17-24`). `|union| = 23` and `24`, both `≤ 32`. This **beats round 36's bespoke record of 3**. The route is a new instrument: the **bespoke second exact solve** (both `Q_0` and `Q_2` prescribed split with free roots), which raises the `T≥3` rate from round 36's `1.39e-4` to `0.0140` — a **101× gain at `q=97`** (`d3_results.txt:3-4` vs `r36_sat3_on_l2/REPORT.md:146-149`).
3. **A GENUINE EXACT MECHANISM, NAMED: `(OV4)`.** For any three supported slopes `i,j,k`, `e(k,i) + e(k,j) ≤ 4`, because the roots that a third member shares with `S_i ∪ S_j` are exactly the roots of `f + z g`, a polynomial of degree `≤ 4`. Zero violations in `374` `T≥3` objects across two fields (`d3_results.txt:6,14`). It is the first **structural** (non-counting) constraint the lane has produced at `m=2`. **It does not close `(SAT3)`: the banked 9-vertex 31-edge design passes it with slack 2** (`d4_results.txt`, section E).

**What did NOT happen: no `T ≥ 3` over `mu_32` (my record there is `2`, a TIE with round 36), no third exact solve, no emptiness theorem, no `m ≥ 3`, no `q ~ 2^128`, and my `T=4` is NOT in a negative-exponent cell** (the bespoke ledger exponent is `18+T > 0`; the `mu_32` `T=4` cell is `+42.5` bits at `q=97`, `d4_results.txt:6`).

---

## MISSES FIRST

1. **MY REGISTERED (X8) IS REFUTED BY MY OWN ARITHMETIC, EXACTLY.** I registered that the doubly-prescribed sub-locus is thinner than the stratum average, so round 36's `+62.5` bits at `T=3` would be misleading. It is not. My sub-locus count `M·(q+1)q/6` with `M = C(32,7)^3(q-1)/q^3` reproduces the ledger's `E(3)` with **ratio `1.000000000000` at all five fields** (`d4_results.txt:17-21`). **The reachable sub-locus is exactly as rich as the stratum average.** P17 (0.65) resolves NO. Reported first because I registered it as load-bearing.
2. **MY REGISTERED (X2) WAS WRONG IN BOTH DIRECTIONS AND I HAD TO CORRECT IT TWICE.** I registered "after two prescriptions the residual `h` freedom is 1 dimension". The truth is **0** for `h` (prescribing `Q_2` determines `h` uniquely: `200/200` distinct `Q_2` from 200 `h`-draws, zero collisions, two fields, `d1_results.txt:9-10`) and **4** for the configuration `(ell,g,c)` (`18 − 7 − 7 = 4`, `d4_results.txt:14`). Neither number was the one I registered.
3. **MY `T`-RECORD OVER THE TRUE DOMAIN `mu_32` IS `2` — A TIE, NOT A GAIN.** All 28 certified `s=0` objects at `q=97` and all 4 at `q=193` have `T = 2` over `mu_32` (`d2_results.txt:21,27`), exactly round 36's headline. **My `T=4` is over a bespoke domain and both record objects have `T = 0` over `mu_32`** (`d5_results.txt:15`, and the `q=193` counterpart). The two columns are never merged. P5 (registered expected max `T` over `mu_32` = 2) **HIT exactly, which is the honest way of saying I did not advance the endpoint-relevant number.**
4. **`(SCRIT)` IS NOT A DISCOVERY ABOUT `s`; IT IS A CONSEQUENCE OF THE BANKED CROSS-PRODUCT, AND ONE LINE OF IT WAS ALREADY VISIBLE IN ROUND 36'S OWN DATA.** Round 36 reported `4/46` and `1/13` `s=0` survivors (`r36_sat3_on_l2/REPORT.md:21`); `C(25,7)/C(32,7) = 0.1428` predicts `6.6` and `1.86`. **The criterion was already implicit in the numbers they printed and they did not extract it** — but neither did I derive it from anything new: it follows from `Q_1(x) = (fg + hk)/L` with `k = f^2/g`, `h = -g^2/f` at a shared root, four lines. I claim the statement, not the machinery.
5. **`(OV4)` DOES NOT CLOSE ANYTHING, AND THE BANKED DESIGN PASSES IT WITH SLACK.** The `m=2` `(SAT3)` design banked at `rh_sat3_realizability/REPORT.md:206` (`K_9` minus a 2-path and 3 disjoint edges) is a **simple** graph, so its worst `e(k,i)+e(k,j)` is `2 ≤ 4` (`d4_results.txt`, section E). `(OV4)` excludes only *concentrated* designs. **I name a mechanism; I do not fire it.**
6. **MY REGISTERED (X7) IS WRONG.** I registered `s ≠ 0 ⟺ gcd(Q_2,f) ≠ 1`. False: `gcd(Q_2,f) ≠ 1` forces `f(x_*) = g(x_*) = 0` hence a common root of `Q_0` and `Q_2`, but `Q_1(x_*) = h(x_*)k(x_*)/L(x_*)` need not vanish. The correct criterion is `(SCRIT)`; `deg gcd(f,g) = 0` on **every** solution I built (`d2_results.txt:22,28`), so the branch (X7) named never even occurred. P9 (0.55) resolves NO.
7. **`(SCRIT)`'s UNRESTRICTED FORM HAS AN EXCEPTION AND MY OWN DATA CAUGHT IT.** On unconstrained `(PAR)` draws, `s = deg gcd(Q_0,Q_2)` held `57/58` and `58/59` — the two failures are `(s_{02},s) = (1,0)` (`d1_results.txt:4,7`), i.e. a shared root of `Q_0,Q_2` at which `f` and `g` both vanish. The clean statement needs the hypothesis `f(x)g(x) ≠ 0`; on prescribed-split objects that hypothesis is automatic (`251/251`, `d2_results.txt:19,25`). **Same species of exception as round 36's `f(ell)=g(ell)=0` refinement of (RES); I did not register it.**
8. **I SHIPPED A BUG AND IT COST A RUN.** My first `d2_scrit` invocation returned `0` solutions at both fields (`d2_results.txt:3,9`) because I truncated a degree-8 polynomial when reducing mod a degree-4 modulus. Found by inspection, fixed with Edit, re-run. **The failed run is preserved in the append-mode results file rather than overwritten** — that is what the round-36 losses rule is for, and it is why the miss is visible at all.
9. **MY `T=4` IS NOT THE "FIRST NEGATIVE-EXPONENT CELL" THE BRIEF ASKED FOR.** Over a bespoke set the ledger exponent is `18+T > 0` for every `T` (`r36_sat3_on_l2/REPORT.md:98`); the `mu_32` `T=4` cell sits at `+42.5` bits at `q=97` (`d4_results.txt:6`), still positive. **Nothing this round probes emptiness-mechanism territory.**
10. **BANKED `T = 4` RECORDS EXIST AND MINE IS NOT A CAMPAIGN RECORD IN THE RAW NUMBER.** `rh_sat3_realizability/REPORT.md:52` reports `T = 4` at `m = 2,3,4`. Those objects have `e = 1` (`:50`), a class `(ERC2)` closes, so my claim is only: **the first `T = 4` on objects certified `e = m = 2`, and over a relaxed domain at that.** Stated before the number, as round 36 had to.
11. **`(SAT2)/(SAT4)/(SAT5)` ARE STILL INAPPLICABLE.** At `T=4`, `sum_x d_x = 28` out of `2|union| = 46` (`d5_results.txt:14`); `(SAT3)` needs `63` out of `64`. I report the occupancy instead of a vacuous table, exactly as round 36 did.
12. **F1/(NEWCAP) IS STILL AT ZERO POWER.** Even at `T=4` the supported pairs are 6 with overlaps `[0,0,1,1,1,2]` and `[0,0,1,1,1,1]` (`d5_results.txt:13`, `q=193` counterpart) — `a*` over supported pairs is now a 6-sample minimum on two objects, not a minimum over a family, and the objects are bespoke-domain. **No F1 test.**
13. **THE `q=193` `s=0` FRACTION UNDERSHOOTS.** `4/53 = 0.0755` against the predicted `0.1428` (`d2_results.txt:26`). Expected `7.6`, observed `4` — Poisson-consistent (`p ≈ 0.12`) but I report the deficit rather than only the `q=97` agreement.

---

## CATCH-24A — own-repo subtraction, run BEFORE every novelty claim

Every recursive grep carried, **at the search level**, `--exclude-dir=r37_urand --exclude-dir=r37_share3_gap --exclude-dir=r37_mint_drafts --exclude-dir=pilots_20260802 --exclude-dir='prize-codex-*' --exclude-dir=.git --exclude-dir=__pycache__ --exclude=dag.json`, over `background/`, `critical/`, `notes/`. Hyphenated/infixed variants searched explicitly: `third prescription`/`third-prescription`/`third member`/`third-member`; `shared root`/`shared-root`/`root sharing`/`root-sharing`; `norm condition`/`norm-condition`/`norm form`; `Cauchy interpolation`/`rational interpolation`/`Pade`/`Padé`/`lattice minim`/`extended Euclid`; `eigenvalue confinement`/`eigenvalue-confinement`; `deficit identity`/`deficit-identity`; `re-basing`/`rebasing`; `2x3 Hankel`/`2 x 3 Hankel`/`cross product`/`cross-product`/`minor vector`; `f^2-kg`/`f^2 - kg`/`g^2+hf`/`fg+hk`/`gcd(Q_2,f)`.

| object | in-repo prior | verdict |
|---|---|---|
| **(PAR), (RES), the `18` dimension, the `18-6T` exponent, `+62.5` at `T=3`, eigenvalue-confinement as the predicted wall** | `critical/nodes/rate_half_band_crossing_location/statement.md:4357-4366` ((PAR) verbatim), `:4363` ((RES)), `:4395-4396` (`+62.5`, `q`-independent), `:4399-4403` (eigenvalue confinement) | **BANKED AND COORDINATOR-AUDITED. All of it is my premise, none of it is mine.** |
| **the third exact solve as the missing instrument** | `r36_sat3_on_l2/REPORT.md:208`; `critical/.../statement.md:4407-4410` ("HANDOFF OF RECORD") | **banked as the open question — it is my mandate.** My answer (it does not exist, and why) is the deliverable. |
| **`d_x ≤ m`, `7T ≤ 2\|D\|`, `T ≤ 9`, the deficit identity** | `background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md:40,50` | **BANKED VERBATIM.** Used, never claimed. |
| **the unique-vote pencil argument** (each domain point roots a gcd-trivial linear pencil at exactly one parameter) | `background/nodes/f_dim1/statement.md:9` | **BANKED at `m=1`.** `(OV4)` is that argument transported *inside* the `m=2` problem via the `(PAR)` middle pair `(u_1,u_2)=(f,g)`: the votes now live on `f+zg`, not on the members. **Transport claimed, not the argument.** |
| **the `m=2` (SAT3) design as a 9-vertex 31-edge multigraph** | `rh_sat3_realizability/REPORT.md:206`, `:259` | **banked.** I test it against `(OV4)` and it passes. |
| `T = 4` at `m=2`; `max T over pencils = 3` | `rh_sat3_realizability/REPORT.md:52` (at `e=1`, `:50`); `rh_psi_degree/d3_m2_q97.txt:73` | **BANKED AND EQUAL-OR-HIGHER**, but out of class (`e=1` or `e` uncertified). MISS 10. |
| Padé / lattice-reduction / syzygy machinery as a **method** | `background/nodes/l1_exact_shell_balanced_shifted_lattice_reduction/statement.md:26`; `xr_joint_window_rank_syzygy_router/statement.md:25,34`; `..._distance_three_external_split_design_exclusion/statement.md:16` | **BANKED IN OTHER LANES (`l1`, `xr`, `A=1`).** My use of it in the `A=3, m=2` `(L2)` lane is new **as a location**, not as a technique. MEDIUM confidence. |
| "for any two supported slopes …" pairwise-slope laws | `rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_two_slope_coefficient_rank_spread/statement.md:57` `(QRS8)` | **banked in the `A=1` lane** — different lane, different object, different quantity (a lower bound on how many *other* slopes are constrained). No overlap with `(OV4)`. |
| **`L·(Q_2,-Q_1,Q_0) = -(row_0 × row_1)` for the 2×3 Hankel matrix of `(k,f,g,-h)`** | greps for `2x3 Hankel`, `cross product`, `minor vector`: only `l1_m4_h3_nu2_prime_field_belyi_normal_form/proof.md:44` (a numeric 3-vector cross product, different lane/object) | **claimed new in this lane.** Verified `58/58`, `59/59`, two fields (`d1_results.txt:3,6`). |
| **`(CONIC)`: `Q_0 g^2 − Q_1 fg + Q_2 f^2 = L Q_0 Q_2`, and its pointwise form `(SLOT)`** | greps for `Q_0 g^2`, `conic identity`: **zero hits** | **claimed new.** `58/58`, `59/59`, two fields. |
| **`(SCRIT)`: `s = \|S_0 ∩ S_2\|`** | greps for `s = \|S_0 cap S_2\|`, `shared root`, the `s!=0` criterion: banked only as an **open** miss (`r36_sat3_on_l2/REPORT.md:38`; `critical/.../statement.md:4417-4418` "no predictive criterion yet") | **claimed new; it is the brief's explicit D2 ask.** `251/251`. |
| **`(OV4)`: `e(k,i)+e(k,j) ≤ 4`** | greps for `overlap bound`, `pairwise overlap` in this lane: nearest are `l1_fpc5_ratehalf_m4_t3_split_slice_payment/statement.md:138` and `xr_split_pencil_rank_two_maxwell_properness/result.md:7`, both other lanes | **claimed new in this lane; MEDIUM-HIGH confidence.** 374 objects, zero violations. |

---

## D1 — THE THREE-MEMBER SYSTEM, STRUCTURED

### D1.1 The parametrization is a length-4 Hankel sequence (verified)

Set `u_0=k, u_1=f, u_2=g, u_3=-h`. Then `L Q_z = (u_1+zu_2)^2 − (u_0+zu_1)(u_2+zu_3)`, i.e. **`L Q_z = −det H(z)` for the 2×2 Hankel matrix of the `z`-shifted sequence**, and the three members are the three 2×2 minors of

```text
[[u_0, u_1, u_2],
 [u_1, u_2, u_3]] ,      L·(Q_2, −Q_1, Q_0) = −(row_0 × row_1).
```

Orthogonality of a cross product to its rows **is** round 35's `E1`, `E2`. Verified `58/58` (`q=97`) and `59/59` (`q=193`), together with `(CONIC)` and `(SLOT)` below (`d1_results.txt:3,6`).

### D1.2 The cost of a third split member — the exact answer

**(CONIC)** `Q_0 g^2 − Q_1 fg + Q_2 f^2 = L Q_0 Q_2` (three lines: multiply out `(f^2−kg)g^2 − (fg+hk)fg + (g^2+hf)f^2 = (f^2−kg)(g^2+hf)`). Its pointwise form is

**(SLOT)** `g(x)^2 · q_x(−f(x)/g(x)) = L(x) Q_0(x) Q_2(x)`, where `q_x(z) = Q_0(x)+zQ_1(x)+z^2Q_2(x)`.

Hence for `x ∈ S_0 ∪ S_∞` the *second* root of `q_x` is `−f(x)/g(x)` — **one formula for both**. Two consequences:

- **(OV4)** For any third slope `z`, `roots(Q_z) ∩ (S_0 ∪ S_∞) = roots(f+zg) ∩ (S_0 ∪ S_∞)`, of size `≤ deg(f+zg) ≤ 4`, unless `f+zg ≡ 0` (which forces `g | L·gcd(Q_0,Q_2)`, impossible at `s=0`, `deg g = 4`). Verified in form `26/26` and `17/17` on unconstrained draws (`d1_results.txt:5,8`), and as a bound with **zero violations in 374 `T≥3` objects** (`d3_results.txt:6,14`). By `PGL_2`-covariance of `(PAR)` this reads, for any three supported slopes, **`e(k,i) + e(k,j) ≤ 4`**.
- **The ladder is exhausted.** `Q_0` prescribed determines `u_0=k`; `Q_2` prescribed determines `u_3=−h` **uniquely** — `200/200` distinct `Q_2` from 200 `h`-draws, both fields (`d1_results.txt:9-10`). `Q_1 = (u_1u_2−u_0u_3)/L` is then forced.

### D1.3 The re-basing to `{0,1,∞}` — and what the third condition IS

At `{0,1,∞}` the three prescriptions are `Q_0 = αP_0`, `Q_2 = γP_∞`, `Q_0+Q_1+Q_2 = βP_1`, so **`Q_1 = βP_1 − αP_0 − γP_∞` is determined by the three split sets and two scale ratios.** Reducing `(CONIC)` mod `P_0` and mod `P_∞` gives exactly round 35's `(D-B)` congruences `Q_2 f ≡ Q_1 g (mod Q_0)`, `Q_0 g ≡ Q_1 f (mod Q_2)` — and evaluating them pointwise turns the third prescription into

> **(CAUCHY).** Find a type-`(4,4)` rational function `f/g` taking the 14 prescribed values `t(x) = Q_1(x)/Q_2(x)` on `S_0` and `t(x) = Q_0(x)/Q_1(x)` on `S_∞`. **14 conditions against `4+4+1 = 9` degrees of freedom: overdetermined by 5; with 2 free scale ratios the net deficit is 3, i.e. `q^{-3}` solutions per subset-triple** (`d4_results.txt:56-62`).

Equivalently `f ≡ R g (mod P_0P_∞)` with `deg P_0P_∞ = 14`: the **first minimum of an explicit rank-2 `F_q[x]`-lattice must drop from its generic 7 to `≤ 4`**. So the answer to the brief's trichotomy is: **not a ring proportionality, not a norm condition — a lattice-minimum / rational-interpolation condition.** It admits an exact `O(1)` **test** (one extended Euclid, or one `14×10` rank) but **no solve**, because there is no free polynomial left: the two solvable slots `u_0` and `u_3` were spent on the first two members. **Re-basing does not help** — the three-member problem at `{0,1,∞}` is symmetric in the three minors, so no choice of base creates a slot. That is the sense in which the third prescription is *structurally different*.

---

## D2 — THE PUSH

### D2.1 `(SCRIT)`: the `s ≠ 0` criterion, exactly (the brief's D2 sub-ask)

If `x ∈ S_0 ∩ S_2` with `f(x)g(x) ≠ 0`, then `k(x) = f(x)^2/g(x)`, `h(x) = −g(x)^2/f(x)`, so `L(x)Q_1(x) = f(x)g(x) + h(x)k(x) = 0` **automatically**. Hence

> **(SCRIT)** `s = deg gcd(Q_0,Q_1,Q_2) = deg gcd(Q_0,Q_2) = |S_0 ∩ S_2|`, and **`s = 0 ⟺ S_0 ∩ S_2 = ∅`** — a zero-cost combinatorial test applied *before* any algebra.

Measured over the full `C(32,7)` meet-in-the-middle: **`198/198` at `q=97`, `53/53` at `q=193`, zero disagreements**, joint histogram exactly diagonal (`d2_results.txt:18-19,24-25`). Solutions per configuration `3.30` vs predicted `C(32,7)/q^3 = 3.69`, and `0.44` vs `0.47` (`:17,23`). `s=0` fraction `0.1414` vs `C(25,7)/C(32,7) = 0.1428` (`:20`). **Operational consequence: restricting to `S_2 ⊆ mu_32 \ S_0` yields 100% `s=0` at 1/7.00 the search cost** (`d4_results.txt:47-48`), replacing round 36's empirical `4/46`.

### D2.2 The bespoke double solve, and `T = 4`

Prescribing `Q_2` split with **free** roots is also exact: `prod(x−b_i) ≡ γ''·L^{-1}g^2 (mod f)` is solved by fixing `b_1..b_5`, forcing one ring coordinate to vanish, and taking `b_6,b_7` from the resulting quadratic. Every object produced therefore has `T ≥ 2` **by construction**:

```text
 q     objects   T=2     T=3    T=4    T>=3 rate    round-36 T>=3 rate   gain
 97      9261    9130    130     1      0.01404        1.39e-4           101x
193      7338    7095    239     4      0.03312        5.32e-4            62x
```
(`d3_results.txt:3-4,11-12`; round 36's rates from `r36_sat3_on_l2/REPORT.md:146-149`.) **Both `T=4` records fully certified** (`d5_results.txt:4-15,17-28`): `deg(7,7,7)`, seprank `3`, `s=0`, nullity(36×32) `= 1`, `M(Z)Q_Z = 0` entrywise from scratch **true**, generic rank `7` with histogram `[(6,1),(7,96)]` / `[(6,1),(7,192)]`, single finite rank-drop at `z=1` / `z=41` with rank 6, **rank at infinity 7** (no drop), degree-`≤1` kernel dimension `0` ⇒ `e = 2` exactly. `|union| = 23` and `24`, so a bespoke 32-set exists in both cases. Reproducible `q=97` record:

```text
f=[74,17,86,23,58]  g=[9,77,35,14,1]  h=[96,79,72,12,72]  k=[56,36,57,93,65]  L=[63,1]
Q0=[82,2,91,96,61,35,50,1]  Q1=[22,39,54,52,92,55,41,82]  Q2=[54,49,0,15,26,20,62,6]
supported slopes {0, 23, 72, inf} ; S_0=[4,23,25,51,66,83,86] ; S_inf=[16,21,28,55,62,64,67]
```

### D2.3 `T` over `mu_32` — the honest distance

All 28 (`q=97`) and 4 (`q=193`) certified `s=0` exact objects have **`T = 2`** (`d2_results.txt:21,27`). The quantified gap to `T=3`:

```text
 q     4-dim family per (S_0,S_inf)   expected T>=3 in it   P(T>=3 | one T=2 object)   T=2 objects needed
 97    q^4 = 88,529,281                     354.0                  4.00e-6                 2.5e5
193    q^4 = 1,387,488,001                   89.9                  6.48e-8                 1.54e7
```
(`d4_results.txt:26-31`.) Against my 28 and 4, the shortfall is **8.93e3×** and **3.86e6×**. **`T=3` over `mu_32` was not sought at anything near the required rate, so its absence here is absence where none was sought** (R5.2, pre-registered).

---

## D3 — THE MECHANISM QUESTION

**A wall appeared, it is exact, and it is not eigenvalue-confinement.** `(OV4)` — `e(k,i)+e(k,j) ≤ 4` — is a statement about *supports*, derived from `deg(f+zg) ≤ 4`, i.e. from the **middle pair of the length-4 sequence**, not from the concentration functionals round 36 measured. Its consequences for the `(SAT3)` design at `m=2` (9 slopes, 63 slots, 31 doubled points, degrees `7^8,6`):

- `e(k,i) ≤ 4`, and `e(k,i)=4` forces `deg k = 4 < 6` ⇒ **`e(k,i) ≤ 3` always**;
- `e(k,i)=3` forces `e(k,j) ≤ 1` for every other `j`;
- all-multiplicity-`≤2` designs are unconstrained.

**HONEST VERDICT: the banked design passes with slack 2** (it is simple, so its worst pair-sum is 2; `d4_results.txt`, section E). `(OV4)` excludes *concentrated* designs only. It is the lane's first genuine structural constraint at `m=2` and it **does not close `(SAT3)`.**

On the brief's second horn: **through `T=4` the counting instruments are failing in the direction of EXISTENCE.** My sub-locus count reproduces the ledger exactly (ratio `1.000000000000`, five fields, `d4_results.txt:17-21`), the `T=3`-over-`mu_32` cell really is `+62.5` bits `q`-independently, and I built `T=4` over a relaxed domain with 9,261 objects. **Nothing I measured points at emptiness.** Per R4(iv) I convert none of this into a verdict in either direction: a positive first moment is not a witness, and my `T=4` is not `(SAT3)`.

---

## D4 — VERDICT

> **THE THIRD PRESCRIPTION IS NOT AN EXACT SOLVE AND CANNOT BE ONE IN `(PAR)` COORDINATES: the parametrization is a length-4 Hankel sequence whose two solvable slots are consumed by the first two members, and the third condition is an overdetermined type-`(4,4)` Cauchy interpolation (deficit 3, `q^{-3}` per triple) with an exact `O(1)` test and no inverse. What replaces it is (a) `(SCRIT)` `s = |S_0 ∩ S_2|`, which makes the second solve 100%-yield at 1/7 the cost, and (b) `(OV4)` `e(k,i)+e(k,j) ≤ 4`, the lane's first exact structural law — which the banked `(SAT3)` design satisfies. `T = 4` over a bespoke 32-set on certified `e=m=2` objects, two fields, fully certified; `T = 2` over `mu_32`, a TIE with round 36.**

**T-record with provenance.** `T_mu32 = 2` (28 objects at `q=97`, 4 at `q=193`, `d2_results.txt:21,27`); `T_bespoke = 4` (1 at `q=97`, 4 at `q=193`, over 9,261 + 7,338 exact double-prescribed objects, `d3_results.txt:4,12`, certified `d5_results.txt:4-28`); `T_mu32` of the bespoke records `= 0` (`d5_results.txt:15`).

**Solve-vs-search status of the third prescription: SEARCH, with an exact test.** Cost `q^5 ≈ 8.6e9` evaluations per `T=3` over `mu_32` at `q=97` by any of the three equivalent routes (4-dim fibre scan; `(λ,μ)`-scan per triple; lattice-minimum test) — all three reproduce the same `q^{-3}`.

**Handoff, priority order (recommendations only — AUDIT-AND-DRAFT, nothing applied outside my directory).**
1. **Bank `(SCRIT)` and retire the "no predictive criterion" line at `critical/nodes/rate_half_band_crossing_location/statement.md:4417-4418`.** `s = |S_0 ∩ S_2|`, four lines of proof, `251/251` two fields, and it converts round 36's `4/46` into `1/1`.
2. **Bank `(CONIC)`/`(SLOT)` and the 2×3-Hankel-minor form of `(PAR)`.** Three lines each, witness-checkable, and they are what make `(OV4)` and `(CAUCHY)` derivable.
3. **Bank `(OV4)` as a NECESSARY condition on any `(SAT3)` design, with the explicit note that the banked 9-vertex design passes.** It is the first structural constraint; it should be recorded as a filter, never as an exclusion.
4. **Re-pose the "third exact solve" handoff.** It should not be carried as an open instrument: in `(PAR)` coordinates it provably does not exist. The correct open item is *"an exact solve for a rank-deficient `14×10` Cauchy system"*, which is a different (and likely Padé-lattice) question — and the `l1`/`xr` lattice-reduction nodes are where its machinery already lives.
5. **The bespoke double solve should replace round 36's single prescription for all bespoke pushes** — 101× and 62× on the `T≥3` rate at equal compute.
6. **`m ≥ 3` remains untouched;** `(PAR)` is `m=2`-specific and every statement here inherits that.

**Cross-pilot flag (self-contained; I read no sibling `r37_*` directory).**

> At `m=2` the `e=m` Hankel-pencil stratum's parametrization is the **2×2-minor vector of a 2×3 Hankel matrix on a length-4 polynomial sequence** `(k,f,g,−h)`, so `L·(Q_2,−Q_1,Q_0) = −(row_0 × row_1)`. Three transportable consequences: (a) the identity `Q_0g^2 − Q_1fg + Q_2f^2 = L Q_0 Q_2`, whose pointwise form says the *second* root of the member-quadratic at any point of `S_0 ∪ S_∞` is `−f(x)/g(x)`; (b) **overlap law**: for any three supported slopes, `e(k,i)+e(k,j) ≤ 4 = deg(f+zg)` — the `m=1` unique-vote argument (`f_dim1/statement.md:9`) transported to the *middle pair* of the sequence rather than to the members; (c) prescribing three split members is an **overdetermined type-`(4,4)` rational interpolation** (14 values, 9 dof, 2 scales, deficit 3), so exactly two prescriptions are solvable and the third never is — any lane with a length-`(n+2)` sequence should expect exactly `n` free prescriptions. Also: for prescribed-split `Q_0, Q_2`, `deg gcd(Q_0,Q_1,Q_2) = |S_0 ∩ S_2|` exactly.

---

## PREDICTIONS vs OUTCOMES

| registered | outcome |
|---|---|
| **(X1)** `L Q_z = det(P+zR)` expands to the three `(PAR)` numerators | **VERIFIED**, `58/58`, `59/59`; upgraded to the 2×3-Hankel-minor/cross-product form |
| **(X2)** residual `h`-freedom after two prescriptions `= 1` | **RESOLVED WRONG both ways** — `h` is `0`-dimensional, the configuration is `4`-dimensional (MISS 2) |
| **(X3)** the third prescription is NOT another ring proportionality; norm-type at best | **HIT on the negative half, WRONG on the positive half** — it is neither a proportionality nor a norm: it is a **lattice-minimum / Cauchy-interpolation** condition |
| **(X4)** yield from a fixed `(S_0,S_2)` exact solution `≈ 4.9e-4` | **SUPERSEDED** — I had fixed `h`, which is 0-dimensional; the right object is the 4-dim configuration fibre, expected yield `354` over `q^4` points (`d4_results.txt:26`) |
| **(X5)** re-basing at `{0,1,∞}` makes the system three minors of one sequence with `S_3` symmetry | **HIT** — and it is exactly why re-basing cannot create a free slot |
| **(X6)** `s = deg gcd(numerators) − deg L` | **HIT but TAUTOLOGICAL** (`Q_j` *is* the numerator over `L`); the non-trivial form is `(SCRIT)` |
| **(X7)** `s ≠ 0 ⟺ gcd(Q_2,f) ≠ 1` | **RESOLVED WRONG** — `deg gcd(f,g)=0` on every solution built (MISS 6) |
| **(X8)** the reachable sub-locus is thinner than the stratum average, so `+62.5` is misleading | **REFUTED EXACTLY BY MY OWN ARITHMETIC** — ratio `1.000000000000`, five fields (MISS 1) |
| **(X9)** the replacement is a shared-root/(SAT4) deficit prescription | **PARTIAL** — sharing is capped at 4 by `(OV4)`, so it cannot replace a 7-point prescription; the actual replacement is `(CAUCHY)` |
| **P1** a third exact solve exists `= 0.15` | **resolved NO**, and now with a structural reason |
| **P2** `T ≥ 3` over `mu_32` `= 0.22` | **resolved NO** — shortfall `8.9e3×` (`d4_results.txt:32-33`) |
| **P3** `T ≥ 4` over `mu_32` `= 0.03` | **resolved NO** |
| **P4** a genuine mechanism is NAMED `= 0.25` | **HIT** — `(OV4)`, exact, two-field, zero violations in 374 objects; **but it fires on nothing** (MISS 5) |
| **P5** expected max `T` over `mu_32` `= 2` | **HIT EXACTLY.** **P5a** bespoke `= 3` → **BEATEN, `= 4`.** **P5b** re-based `mu_32` `= 2` → **HIT** |
| **P6** the `s ≠ 0` criterion is found `= 0.70` | **HIT** — `(SCRIT)`, `251/251` |
| **P7** (X1) verifies with no correction `= 0.80` | **HIT** |
| **P8** (X6) is the right criterion `= 0.60` | **partial** — true but tautological |
| **P9** (X7) is the right criterion `= 0.55` | **resolved NO** (MISS 6) |
| **P10** re-basing makes the third condition strictly cleaner `= 0.35` | **HIT** — it exposes `(CAUCHY)`; it does **not** make it solvable |
| **P11** a CATCH-24A subtraction fires load-bearing `= 0.75` | **HIT** — four, incl. `f_dim1`'s vote argument under `(OV4)` and the banked `T=4` |
| **P12** the `+62.5` ledger reproduces from my own arithmetic `= 0.90` | **HIT** — exactly, at five fields |
| **P13** `T = 3` over a bespoke 32-set `= 0.60` | **HIT** — 130 and 239 instances |
| **P14** the third condition is a NORM condition `= 0.30` | **resolved NO** — lattice/interpolation, not norm |
| **P15** at least one ramguard run fails `= 0.35` | **resolved NO** — six invocations, six clean exits (one returned **zero output rows** from a bug of mine, not a ramguard event — MISS 8) |
| **P16** round 36's `T=2` `mu_32` witness re-certifies `= 0.85` | **NOT TESTED** — I regenerated the construction rather than replaying their coefficient vectors; declared unmeasured |
| **P17** the `+62.5` reading is misleading `= 0.65` | **resolved NO** (MISS 1) |

---

## ZERO-POWER DECLARATIONS

1. **R5.1 honoured and load-bearing.** `T = 4` is over a **bespoke 32-set** and has **ZERO POWER** for `(SAT3)`, the strict endpoint, or the official row. Both record objects have `T = 0` over `mu_32` (`d5_results.txt:15`). The columns are never merged anywhere.
2. **R5.2 honoured.** My failure to reach `T=3` over `mu_32` has **zero power**: the required rate is `4.0e-6` per exact `T=2` object and I built 28 (MISS 3, `d4_results.txt:29`).
3. **Every `T` carries its full distribution** (R4(ii)): `{2:9130, 3:130, 4:1}` and `{2:7095, 3:239, 4:4}`; `T` over `mu_32` `= {2:28}` and `{2:4}`.
4. **R4(i) honoured**: `T=4` is a **sample maximum over the constructions I ran**, never a bound. So is `(OV4)`'s observed worst value (`4` at `q=97`, `3` at `q=193`) — the **bound** `≤ 4` is proved, the observed maximum is not evidence about tightness beyond my sample.
5. **R4(iv) honoured**: the exact ledger agreement is a **first-moment** statement. I convert `+62.5` bits into neither existence nor emptiness, and I flag that my own registered attempt to discount it (X8) failed.
6. **`(OV4)` is a NECESSARY condition only.** It passes on the banked design with slack 2; it excludes nothing that was believed to exist (MISS 5). Declaring this explicitly so no downstream reader treats it as an exclusion.
7. **`(SCRIT)` is verified on the class I can regenerate** — prescribed-split `(PAR)` objects with `f(x)g(x) ≠ 0` on `S_0 ∩ S_2` — with denominators `198` and `53`. On **unconstrained** draws it has the `f=g=0` exception, `1/58` and `1/59` (MISS 7). It is not a statement about the whole stratum.
8. **F1/(NEWCAP) remains at ZERO POWER** — 6 supported pairs on 2 bespoke-domain objects, not a minimum over a family (MISS 12).
9. **Two fields only** (`97, 193`) for everything structural; five fields for ledger arithmetic, declared as arithmetic. **No lift to `Z`, no geometric irreducibility, no statement at `q ~ 2^128`.**
10. **Nothing here bears on `m ≥ 3`** — `(PAR)` is `m=2`-specific (`r36_sat3_on_l2/REPORT.md:210`) — **nor on `Rout`, the `9/4` or `7/4` ledgers, FR-canonical, or layer A.**
11. **`(SAT2)/(SAT4)/(SAT5)` are not verified, they are inapplicable at `T=4`**: `sum_x d_x = 28` of `2|union| = 46` (`d5_results.txt:14`) against the `63` of `64` that `(SAT3)` demands.

---

## MEASURED FUNCTIONALS (CATCH-19C)

`m, rho=7, N=32, R=16, A=3, e, s, delta=rho-3e, T_target=9`; `deg Q_j`; `s = deg gcd(Q_0,Q_1,Q_2)`; separation rank `(RNC2)`; `nullity(36x32)` and its rank; entrywise `M(Z)Q_Z = 0` from scratch; generic rank `max_z rank M_r(y_0+zy_1)` with its full rank histogram; the finite rank-drop set with its rank; the rank at infinity; the degree-`≤1` kernel dimension. **New here:** the length-4 sequence `(u_0,u_1,u_2,u_3) = (k,f,g,-h)` and its 2×3 Hankel cross product; the `(CONIC)` residual `Q_0g^2−Q_1fg+Q_2f^2−LQ_0Q_2`; the `(SLOT)` residual at every `x` with `g(x)≠0`; the injectivity of `h ↦ Q_2` on the `ell`-conditioned family (collision count over 200 draws); the joint histogram of `(deg gcd(Q_0,Q_2), s)`; the joint histogram of `(|S_0 ∩ S_2|, s)` over the full `C(32,7)` meet-in-the-middle; exact `S_2` solutions per configuration against `C(32,7)/q^3`; the `s=0` fraction against `C(25,7)/C(32,7)`; `deg gcd(f,g)`; `max_z |roots(f+zg) ∩ (S_0∪S_2)|`; the bespoke double-solve object count and its full `T` distribution; `|union of supported root sets|` per `T≥3` object; the **pairwise overlap matrix `e(i,j)` and the worst `e(k,i)+e(k,j)` over all slope triples** (the `(OV4)` functional) with its histogram; `sum_x d_x` over supported slopes against `2|union|`; `T` over `mu_32` for every object built; the sub-locus/ledger ratio at five fields; the `T=2`-objects-needed-per-`T=3` figure. **Registered but NOT measured:** any `T ≥ 5`; `T ≥ 3` over `mu_32`; a replay of round 36's published `T=2` coefficient vectors (P16); `(SAT2)/(SAT4)/(SAT5)` (inapplicable); the endpoint's `a*` over supported pairs on a `mu_32` object; anything at `m ≥ 3`.

---

## COMPLIANCE

**Registrations.** `R0` (notation from the anchors alone), `R1` (execution order), nine falsifiable derivations `(X1)-(X9)` **each with its falsifier**, seventeen numeric priors `P1-P17` including the brief's six and the **expected-max-`T` number (`P5 = 2`, with `P5a = 3` bespoke and `P5b = 2` re-based)**, the four-clause MISS-2 mean-vs-max guard `R4` (whose clause (iv) explicitly pre-committed me not to convert `+62.5` bits into existence — the trap I then fell into from the other side via (X8)), eleven zero-power pre-declarations `R5`, the subtraction plan `R6` with hyphenated/infixed variants, and the expected misses `R7`, were appended to `PREREG.md` under `## Pilot registrations` with the **Edit tool in three calls** (harness size rule), after reading **exactly** the two named anchors and **before any other read, any grep, any `ls`, and any interpreter invocation**. **No post-registration addenda**; the four registration errors ((X2), (X7), (X8), and (X3)'s positive half) are reported as misses, not edited. Execution followed `R1` (D1 → D2 → D3 → D4) exactly. `R7(a)` (I would tie, not beat, on `mu_32`) and `R7(c)` (the mandate's premise needs re-posing) both fired.

**Compute law — NO BREACH.** **Six interpreter invocations, all six `tools/ramguard <profile> -- python3 …` issued from the repo root with the literal `--`**: five `local` (`RAMGUARD_TIMEOUT=290` each) for `d1_struct.py`, `d2_scrit.py` (twice — the second after the Edit-tool bug fix), `d3_push.py`, `d5_certify.py`; one `tiny` (`RAMGUARD_TIMEOUT=55`) for `d4_ledger.py`. **Zero bare `python3` for any purpose** — no file patching, no string replacement, no probes, no heredocs, no no-op invocations. Stdlib only (`random`, `time`, `math`, `itertools`); no third-party imports, no Modal, no network, no git, **no subagents**. **Ramguard status: six clean exits, no memory event, no wall kill** (P15 resolved NO). `d3_push.py` self-budgeted at 125 s/field with `time.time()` caps; it exceeded the 120 s foreground tool window and was completed as a background ramguard process, exit code 0.

**Write discipline.** No `sed -i`, `awk -i`, `perl -i`, `tee`, or shell redirection onto any file; no in-place shell stream edit anywhere. The three `PREREG.md` registration appends and the three `d2_scrit.py` bug fixes used the **Edit** tool; all five scripts were created with the **Write** tool.

**Results-file rules (the new round-36 clause) — HONOURED, AND IT PAID.** Every results file is opened in **append** mode (`"a"`) with a timestamped `=== RUN … ===` header per invocation; **no blind `"w"` anywhere**, so the failed first `d2_scrit` run is still on disk at `d2_results.txt:2-14` and is cited as MISS 8 rather than lost. **No results-producing run was piped through `head`** — every run's stdout was taken through `tail` or read from the background task file after the script had written its own file, never a SIGPIPE-capable prefix filter on a live producer.

**Imported-script rule — NOT ENGAGED, and stated rather than assumed.** I imported and executed **no** banked script. All five scripts are mine, written from scratch; the polynomial/linear-algebra helpers are **duplicated into each file** rather than imported, exactly so that no import can write at import time. No banked script's output paths needed auditing because none was copied. Banked material was read **only** as data, via `grep -n` and two bounded `Read` windows.

**RAM discipline.** `dag.json` **never opened**; every recursive grep carried `--exclude=dag.json`. `critical/nodes/rate_half_band_crossing_location/statement.md` (>4600 lines) was read in **two bounded windows** (60 and 40 lines) plus grep output lines, never as a file. `rate_half_ca_hankel_..._two_slope_coefficient_rank_spread/statement.md` was read in one 12-line window. Largest object materialised: the `36×32` and `27×16` eliminations and the two `26,333`-element meet-in-the-middle tables; every driver writes its own results file.

**Quarantine — clean.** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` **never opened and never appeared in any tool output**. **No sibling round-37 directory (`r37_urand`, `r37_share3_gap`, `r37_mint_drafts`) was opened, read, listed or traversed**, and **`notes/pilots_20260811/` was never `ls`-ed** — every path I named was explicit. Every recursive grep carried `--exclude-dir=r37_urand --exclude-dir=r37_share3_gap --exclude-dir=r37_mint_drafts --exclude-dir=pilots_20260802 --exclude-dir='prize-codex-*' --exclude-dir=.git --exclude-dir=__pycache__ --exclude=dag.json` **at the search level**, never as output filtering. No path containing `prize-codex-` was touched. The `r36_*`, `r35_*` and `rh_*` directories were read as explicitly permitted (`r36_sat3_on_l2/FABLE_AUDIT.md` appeared as a grep hit line and was **not** opened).

**Write scope.** Every write is inside `notes/pilots_20260811/r37_third_solve/`: `PREREG.md` (registrations appended), `d1_struct.py` + `d1_results.txt`, `d2_scrit.py` + `d2_results.txt`, `d3_push.py` + `d3_results.txt`, `d4_ledger.py` + `d4_results.txt`, `d5_certify.py` + `d5_results.txt`. **No `dag/`, `nodes/`, `critical/`, `background/`, `experiments/` or `tools/` edits; no git; the session scratchpad was not used for any project file; nothing went to `/tmp`** (the background task's stdout capture is harness-owned, not a file I wrote). **AUDIT-AND-DRAFT respected:** every board and node recommendation in D4 is posed for coordinator triage and **nothing outside my directory was altered**. `REPORT.md` is not written — per the brief's fallback clause this report is returned verbatim as my final message.

**Method discipline.** CATCH-24A greps ran **before** every novelty claim, including hyphenated and infixed variants, and produced **eight live subtractions, four of them load-bearing**: `(PAR)`, `(RES)`, dimension 18 and the eigenvalue-confinement prediction are all already coordinator-audited into `critical/nodes/rate_half_band_crossing_location/statement.md:4347-4418`, i.e. my entire premise; `(OV4)`'s engine is the banked `m=1` unique-vote argument at `f_dim1/statement.md:9`; a banked `T = 4` at `m=2` already exists (out of class); and the Padé/lattice machinery my `(CAUCHY)` reformulation needs is banked in the `l1` and `xr` lanes. Every quantifier claim carries a `file:line` or a results-file citation with its denominator. Every max-quantified claim carries a zero-power declaration. **Two-field confirmation (`F_97`/`F_193`) for every structural claim** — the cross-product form, `(CONIC)`, `(SLOT)`, the ladder-exhaustion injectivity, `(SCRIT)`, `(OV4)`, the bespoke double solve, and both `T=4` certifications — with the five-field ledger arithmetic declared as arithmetic. **MISSES FIRST**, and the round's own self-corrections — that my registered `(X8)` is refuted by my own arithmetic, that `(X2)` was wrong in both directions, that my `mu_32` record only ties, that `(SCRIT)` was already latent in round 36's printed numbers, that `(OV4)` fires on nothing, that `(X7)` is false, and that I shipped a truncation bug — are reported as falsifications of my own work, in that order, before any result.
