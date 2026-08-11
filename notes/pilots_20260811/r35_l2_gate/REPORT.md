All deliverables executed. Here is the full REPORT text.

---

# REPORT — r35_l2_gate (round 35)

## VERDICT (first)

**R-L2 IS RESOLVED: THE `e = m = 2` STRATUM IS NONEMPTY. I CONSTRUCTED IT.**

A `(4m+1) x 4m = 9 x 8` syndrome Hankel pencil with **minimal index exactly `m = 2`, generic rank exactly `4m-1 = 7`, `s = 0`, and `Q_0,Q_1,Q_2` linearly independent** exists. **Twelve certified objects over FIVE fields** (`q = 97, 193, 257, 641, 769`; 3+3+2+2+2), each re-verified entrywise against the original `36 x 32` system `M(Z)Q_Z = 0` from scratch (`d2_results.txt`, `d3_results.txt`). This is **existence, and existence is witness-checkable — it is a theorem, not a fields-searched positive.** The campaign's first `m >= 2` object with `e = m`.

The route was the pre-registered inversion **D-F**: the `m=2` system is bilinear in `A = (Q_0,Q_1,Q_2)` (24 unknowns) and a syzygy datum `B = (f,g,h,k)` (20 unknowns), and for fixed `B` it is a **square `24 x 24`** homogeneous system in `A`. So a curve exists iff `det M(B) = 0` — **ONE condition, not five.** Measured hit rate `0.0179` at `q=97` and `0.0047` at `q=193` against the predicted `1/q = 0.0103 / 0.0052` (`d2_results.txt:5`). Blind curve search costs `q^-5 ~ 1e-10`; the inversion costs `q^-1`. **That factor of `q^4` is the whole round.**

Four consequences, in order of what they change:

1. **Round 34's `+4` does not mean what it was read to mean.** The equation-count excess `4m^2-7m+2` is not the existence count. The curve space has projective dimension `4m(m+1)-1` and the solvability locus has determinantal codimension `4m^2-7m+3`, so its **expected dimension is `11m - 4 > 0 at EVERY m >= 1`** (`d3_results.txt`). The sign change at `m=2` is a change in equation-count excess, **not** in the existence verdict. The `(L2)` layer was never the wall.
2. **The `+4` IS transverse, and I can say exactly where the excess lives.** At each witness `dim ker Phi = 1` and the recovered `(f,g)` is proportional to the `B` used, so `B |-> Q` has a zero-dimensional fibre and the good component has dimension **exactly `18 = 23 - 5`** (`d3_results.txt`, both fields). The excess is confined to the degenerate component: the common-root locus has dimension **21 > 18** and lies inside the solvability locus (`d1_results.txt`, nullity `2` on 40/40 planted curves per field).
3. **The difficulty moves, undiminished, to the domain layer.** The witnesses have **`T = 0`**, and the mechanism is sharp: **not one** of the `97` (resp. `193`) locators splits completely over `F_q` — the root-count histogram is `{0:31, 1:39, 2:17, 3:6, 4:1, 5:1}` at `q=97` (`d4_results.txt`), which is the Poisson(1) law of a *random* degree-7 polynomial to within noise. The `(L2)` layer is free and buys **nothing** at the splitting layer — the same "no structural enhancement" verdict round 34 measured on nets that had no pencil, now measured on nets that do.
4. **F1 is exercised for the first time in four rounds.** `a* = 14 - max shared roots = 13 = 7m-1` exactly, on both headline witnesses and on 5 of 6 (`d4_results.txt`, `d2_results.txt`) — **and one witness gives `a* = 12 < 13`**, which I report ahead of the five that agree.

**What did NOT happen: no emptiness proof (D3's target is refuted by my own D2), no `(SAT2)-(SAT5)` object, no `m >= 3` decision, and no statement at `q ~ 2^128`.**

---

## MISSES FIRST

1. **My pre-registered derivation D-D is BANKED, twice, and I registered it as if it were mine.** `(A+s)e <= rho-s` is `(MI1)` at `background/nodes/rate_half_ca_hankel_minimal_index_budget/statement.md:29` (status PROVED, `:3`), which at `m=2, s=0` reads exactly my `3e <= 7`; and `delta = rho-3e = m-1` is literally displayed in `(SAT1)` at `background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md:13`. My "Kronecker ceiling `e <= (4m-1)/3`" and my "`e=2` forces `delta=1`" are **re-derivations of banked results**, not discoveries. What I add is only that I verified the *mechanism* on a real object (left kernel spanned by `Q_Z` and `X Q_Z`, left nullity 2, exactly one rank-drop parameter of rank 6, none at infinity — `d3_results.txt`, both fields). Reported first because I registered it in advance as a falsifiable derivation of mine.
2. **I found a PROVED node that appears to already close what the mandate says R-L2 would close, and I am flagging a possible mis-pricing of my own assignment.** `background/nodes/rate_half_ca_hankel_endpoint_residual_pole_interpolation_exclusion/statement.md:3` is **status PROVED**, `:7` retains "any strict `A=3`, `e=m` endpoint on an even row `m>=6`", and `node.json:8` concludes "**every e=m defect stratum is impossible, including the official m=2^37 row**". If that is what it says, then the brief's stake — "EMPTY for `m >= 2` => the strict endpoint closes outright" (PREREG.md mandate) and `critical/nodes/rate_half_band_crossing_location/statement.md:3302-3304` — is **already discharged at the official row**, and R-L2's real value is at small and odd `m`, not at the official endpoint. **I did not read that node's proof and I am not asserting a contradiction**; I am reporting a header-level tension for coordinator triage.
3. **D3's deliverable is dead, and it was killed by my own D2.** The brief asked whether the `+4` can be made a theorem at `m=2`. It cannot: I built witnesses. I registered `P3 = 0.08` for an emptiness proof and it resolves **NO by construction**. I report this as the refutation of the round's own second hypothesis, not as a side note.
4. **The brief's `(SAT1)-(SAT5)` table CANNOT be filled and I will not pretend otherwise.** My objects satisfy the pencil-intrinsic half of `(SAT1)` exactly — `A = R+1-2rho = 3`, `e = m = 2`, `s = 0`, `delta = m-1 = 1`, generic rank `rho = 7` (`saturation_rigidity/statement.md:13`). They satisfy **none** of the domain-facing conditions: `T = 0`, so `(SAT2)` (`O <= delta`), `(SAT3)` (`T = rho+2`), `(SAT4)` (the deficit identity) and `(SAT5)` are **vacuous, not verified**. The witness answers the mandate's stated linear-algebra question and **not** the endpoint question.
5. **My designed-domain instrument ran with zero input.** The greedy set-cover for a bespoke 32-subset returned `T = 0` **trivially**, because no locator splits completely over `F_q` at all — there was nothing to cover (`d4_results.txt`). So the "can you design `D`?" question is **untested**, not answered, and the greedy value is a lower bound on the best designable `T` in any case (MISS-2 guard (i)).
6. **My `a*` is not the endpoint's `a*`.** I minimised `|S_g u S_g'|` over **all** slope pairs; the endpoint minimises over **supported** pairs, of which my objects have none. Since a min over a subset is `>=` a min over the whole, my `13` is a *lower* bound on the endpoint functional, and **F1 is exercised only in this weak sense.** I registered `P8` expecting exactly this and it does not rescue the claim.
7. **One of the six headline witnesses has `a* = 12`, below `7m-1 = 13`** (`d2_results.txt`, `q=97` third witness, max shared roots 2). I report the disagreeing object before the five agreeing ones. It does not contradict the endpoint hypothesis `a = w* = a* = 7m-1` (miss 6 explains why) but it does show `a*` is **not** forced to `13` by the pencil alone.
8. **The inversion is `m=2`-specific and I did not decide `m=3`.** The `24 x 24` squareness is an accident: at `m=3` the analogous cleared system is `4` identities of 20 coefficients each = **80 equations on 48 curve unknowns** for fixed `B`, not square, so D-F does not port. **The `m >= 3` branch of R-L2 is exactly as open as it was this morning.**
9. **Five prime fields is not a theorem over `Z` or at `q ~ 2^128`.** The construction is a codimension-one condition (`det M(B) = 0`) on a rational parameter space defined over the prime field, which is why it works at every field I tried, but I did **not** lift a witness to `Z`, exhibit a geometrically irreducible good component, or run a Lang–Weil argument. **Z5 stands.**
10. **DEF-ID is answered from inside a quarantine.** I could not read the other `r35_*` pilots. My verdict rests on `(BIV-G)`'s statement and counts (`notes/pilots_20260811/rh_bivariate_system/REPORT.md:347-358, 363-366`) and on my own reduction, nothing else.
11. **An `ls` of `notes/pilots_20260811/` displayed the NAMES of the three sibling `r35_*` directories.** I opened, read and traversed none of them. Disclosed rather than left implicit.

---

## CATCH-24A — own-repo subtraction, run BEFORE every novelty claim

Every recursive grep carried `--exclude-dir='r35_*' --exclude-dir='prize-codex-*' --exclude-dir='pilots_20260802'` **at the search level**, over `background/`, `critical/`, `notes/`. Hyphenated and infixed variants were searched explicitly (`minimal-index` as well as `minimal index`; `BIV-G|BIV_G|(BIV|W-layer|W layer`; `11m-4|11m - 4`; `4m^2 - 7m|4m2-7m|4m^2-7m`).

| object | in-repo prior | verdict |
|---|---|---|
| **`e <= (4m-1)/3`; `e=2 => delta=1`** (my registered D-D) | `rate_half_ca_hankel_minimal_index_budget/statement.md:29` `(MI1)` PROVED (`:3`); `endpoint_saturation_rigidity/statement.md:13` displays `delta=rho-3e=m-1` | **BANKED TWICE. Not mine.** MISS 1. I add only its verification on a real object. |
| left and right kernels generated by the same `Q_Z`; left minimal index `= e` | `minimal_index_budget/statement.md:21-23`; `a1_core_one_middle_adjugate_factorization/proof.md:12-13` ("one right minimal index `e`, one left minimal index `e`, regular size `Delta=1`") | **banked**; my `d3` check reproduces it at `A=3, m=2` |
| `(4m+1) x 4m` pencil, generic rank `4m-1`, `Q_j` independent, `nu_Q` a degree-`m` RNC | anchor 2, `endpoint_rational_normal_kernel_curve/statement.md:14-17, 22-30` PROVED | **banked — it is my object's definition.** My `seprank = 3` check is that node's `(RNC2)` at `m=2`. |
| `(SAT1)`: `A=3, e=m, s=0, delta=m-1`; `s != 0` forbidden | `endpoint_saturation_rigidity/statement.md:13` | **banked**; my witnesses are certified against this exact line |
| the `(L2)` gate, its size `(m+2)(4m+1)` vs `16m`, deficit `4m^2-7m+2`, `m=1` uniquely underdetermined | `critical/nodes/rate_half_band_crossing_location/statement.md:3284-3308`; `r34_m2_decision/REPORT.md:17,107-114` | **banked — it is my mandate.** My contribution is that **this count does not govern existence**. |
| "nobody has ever exhibited a `(SAT1)`-profile pencil with `e=m` at any `m>=2`" | `critical/.../statement.md:3297-3299` | **banked as the campaign's own record.** My witnesses are the first counter-instance to that record. |
| **`e=m` endpoint strata excluded on even rows `m>=6`, incl. the official `m=2^37`** | `endpoint_residual_pole_interpolation_exclusion/statement.md:3,7`; `node.json:8` — **status PROVED** | **BANKED AND PROVED, and it re-prices my own mandate** (MISS 2). My `m=2` witness is outside its hypotheses (`m=2` is not `>= 6`) and is not an endpoint defect stratum (`T=0`), so **no contradiction**. |
| the degenerate rank-1 family (shared domain root, `s != 0`, weight-one error), rate `(49/32)/q` | `r34_m2_decision/REPORT.md:168`; `critical/.../statement.md:3290-3294` | **banked as a family and a RATE.** New here: it is a **dimension-21 excess component** of a locus of expected dimension 18 (`d1_results.txt`, nullity 2 on 40/40 per field). |
| the `e=2` Kummer analogue is analytically dead (leading `Z`-coefficient constant) | `r34_m2_decision/REPORT.md:127`; `critical/.../statement.md:3294-3296` | **banked and honoured**: my witnesses all have `deg Q_2 = 7` exactly, and my search **rejected** kernel curves with `deg Q_2 != 7` (1 rejection at `q=97`, `d2_results.txt:6`) |
| the INVERSION method ("choose the object first, pay only combinatorics") | round-34 bank 3, as described in my brief (PREREG.md, D2) | **banked as a METHOD.** The `24 x 24` square-determinant instrument at `m=2` is new. |
| naive dimension counts fail | `background/nodes/pb_design_ceiling/proof.md:125` | banked; quoted against **my own** ledger (Z2, MISS-2 guard (iv)) |
| the `(f,g)` congruence reduction `Q_2 f == Q_1 g (mod Q_0)`, `Q_1 f == Q_0 g (mod Q_2)`; the `14x10` `Phi` | greps for `determinantal`, `degeneracy locus`, `Porteous`, `Fulton`, `syzygy`, `Pade` in the `ca_hankel` lane returned only `l1_fpc5_tpetal_hankel_support_determinantal_system` and `spread_syzygy_circuit_bound` — **different lanes, different objects** | **claimed new in this lane; LOW confidence it is new anywhere** (it is an apolarity/Padé manoeuvre) |
| **expected dimension `11m-4` of the `(L2)` solvability locus** | greps for `11m-4`, `11m - 4`, `expected dimension` returned only `r34_m2_decision` orbit-dimension text and an unrelated `t_petal_lemma` line | **claimed new** |
| DEF-ID posed, unexplained | `critical/.../statement.md:3371-3379` | banked as POSED; my verdict below is the deliverable |

---

## D1 — THE STRATUM AS AN EXACT OBJECT

### D1.1 The four blocks, and where the `+4` actually sits

`m=2`: `rho=7, N=32, R=16, r=7, A=R+1-2rho=3, e=m=2, s=0, delta=m-1=1, T_target=rho+2=9`. `M(Z)=M_r(y_0)+Z M_r(y_1)` with `M_r(y)[a][b]=y[a+b]` of size `9x8`, `y_i in F^16`; `Q_Z=Q_0+ZQ_1+Z^2Q_2`, `deg Q_j <= 7`. `M(Z)Q_Z=0` is four 9-row blocks:

```text
B0: M_0 Q_0 = 0
B1: M_0 Q_1 + M_1 Q_0 = 0
B2: M_0 Q_2 + M_1 Q_1 = 0
B3: M_1 Q_2 = 0
```

**D-A verified (registered in advance): `B0` and `B3` each have rank exactly 9** — histogram `{9: 40}` on 40 random degree-7 `Q_0` per field, both fields (`d1_results.txt`). So each leaves a 7-dimensional space (the recurrence/locator space of `Q_0` resp. `Q_2`), and:

> **The entire overdetermination is in the two cross blocks: 18 equations on 14 unknowns.** At general `m` the same reduction gives `m(4m+1)` equations on `8m-2` unknowns, deficit `4m^2-7m+2` — the deficit is preserved exactly, verified as arithmetic for `m=1..7` (`d1_results.txt`).

**WHICH 4 conditions.** With `S_0 = roots(Q_0)`, `S_2 = roots(Q_2)`, `W = S_0 u S_2` (14 points generically), `y_0 = sum_{S_0} lambda_x v_x`, `y_1 = sum_{S_2} mu_x v_x`, the cross blocks read

```text
B1:  sum_{x in S_0} lambda_x Q_1(x) x^a  +  sum_{x in S_2} mu_x Q_0(x) x^a = 0,  a=0..8
B2:  sum_{x in S_0} lambda_x Q_2(x) x^a  +  sum_{x in S_2} mu_x Q_1(x) x^a = 0,  a=0..8
```

i.e. **two diagonal rescalings of `(lambda,mu)` must both land in the same `[14,5]` GRS code `C = ker(9x14 Vandermonde)`.** Two 5-dimensional subspaces of a 14-dimensional space: `5+5-14 = -4`. **That is the `+4`, localized exactly.**

### D1.2 The exact solvability criterion (D-B — verified, and it is the round's instrument)

Writing `C = {(u_x f(x))_x : deg f <= 4}`, the condition becomes a pair of congruences:

> **(D-B)** For `Q_0,Q_2` squarefree of degree 7, pairwise coprime with `Q_1`: `M(Z)Q_Z=0` has a nonzero solution **iff** there are `f,g` of degree `<= 4`, not both zero, with
> ```text
> Q_2 f == Q_1 g  (mod Q_0)        and        Q_1 f == Q_0 g  (mod Q_2)
> ```
> equivalently `rank Phi(Q) <= 9` for the `14 x 10` matrix `Phi:(f,g) |-> (Q_2f-Q_1g mod Q_0, Q_1f-Q_0g mod Q_2)`. Recovery: `lambda_x = u_x f(x)/Q_1(x)` on `S_0`, `mu_x = u_x f(x)/Q_0(x)` on `S_2`, `u_x = 1/prod_{y != x}(x-y)`.

**Verified `120/120` per field, both fields: `nullity(36x32) == 10 - rank(Phi)`, joint histogram `{(0,0): 120}`** (`d1_results.txt`). The falsifier did not fire. This replaces a `36x32` object by a `14x10` one and is what makes the rest of the round computable.

### D1.3 RECONCILING THE TWO COUNTS — the brief's central D1 question

**They answer different questions, and BOTH were misread. Here is the exact bookkeeping.**

- **The equation-count excess** `(m+2)(4m+1) - 16m = 4m^2-7m+2 = +4` is the difference of equations and unknowns for a **fixed** curve. It is **not** an existence codimension.
- **The determinantal codimension** — the honest naive existence count — is `deficit + 1 = 5`, since a nonzero solution needs `rank <= 31` of a `36x32` matrix, `(36-31)(32-31) = 5`, equivalently `rank <= 9` of the `14x10` `Phi`, `(14-9)(10-9) = 5`. Round 34 already used `q^-5` in its own MISS 2 (`r34_m2_decision/REPORT.md:30`) without drawing the consequence. **D-C verified**: `0` hits in `120` random curves per field, both fields, consistent with `q^-5` (`d1_results.txt`).
- **The incidence count** `23 + 32 - 36 = 19` is the dimension of the total incidence variety. **It is contaminated.** D-E verified: the common-root locus has dimension `3*7-1 + 1 = 21` in `P^23` and **lies inside the solvability locus** — nullity histogram `{2: 40}` on 40 planted curves per field, both fields (`d1_results.txt`), exactly the predicted `y_0 = lambda v_{x*}, y_1 = mu v_{x*}` two-parameter family. In the incidence variety that component has dimension `20+3 = 23 > 19`. **A count with an excess component carries no verdict** (`pb_design_ceiling/proof.md:125`; my MISS-2 guard (iv)).

**And the correct count, once stated properly, never said "empty" at all:**

```text
 m | proj dim curve space 4m(m+1)-1 | det codim 4m^2-7m+3 | EXPECTED DIM = 11m-4
 1 |                             7  |                  -1 |                   7
 2 |                            23  |                   5 |                  18
 3 |                            47  |                  18 |                  29
 4 |                            79  |                  39 |                  40
 5 |                           119  |                  68 |                  51
```

> **`4m(m+1)-1 - (4m^2-7m+3) = 11m-4 > 0` for every `m >= 1`. The `(L2)` layer is nonempty-expected at EVERY `m`.** Round 34's "`m=1` is the only underdetermined case, therefore `m>=2` is expected empty" is a **non sequitur**: the quantity that flips sign at `m=2` is the equation-count excess, and the quantity that governs existence is `11m-4`, which never flips. `d3_results.txt`.

**So: the TCAP ledger and the incidence count do not conflict, because neither is about this layer's existence.** TCAP-DIM prices the **full `(SAT3)` object** (curve + design + `T=rho+2` split members); the incidence count prices the **total** `(L2)` incidence variety including its excess component; and the `(L2)` layer's own existence count is `11m-4 >= 0`. The `m=2` cell of TCAP-DIM (`+3..+5`, `r34_m2_decision/REPORT.md:191-198`) is **untouched** by my result — my witnesses have `T=0` and are not `(SAT3)` objects.

### D1.4 Is the `+4` transverse? (registered P5) — YES, on the good component

At each witness, `dim ker Phi = 1`, and the recovered `(f,g)` is **proportional to the `B` the witness was built from** (both fields, `d3_results.txt`). So `h,k` are then determined and the fibre of `B` over `Q` is a single point up to scale. Hence

```text
dim(good component) = dim{B : det M(B) = 0} = 19 - 1 = 18 = 23 - 5.
```

**Exactly the expected dimension: the codimension-5 condition is transverse on the good component, and the excess (dimension 21) is confined to the degenerate common-root component.** Two-field confirmation.

---

## D2 — THE CONSTRUCTIVE ATTACK (the deliverable)

### D2.1 The inversion (D-F, registered in advance)

Clearing D-B's congruences with quotients `h,k` (degree `<= 4` automatically) gives two polynomial identities of degree `<= 11`:

```text
E1:  Q_2 f - Q_1 g - Q_0 h = 0        (12 coefficient equations)
E2:  Q_1 f - Q_0 g - Q_2 k = 0        (12 coefficient equations)
```

**Bilinear** in `A = (Q_0,Q_1,Q_2)` (24 unknowns) and `B = (f,g,h,k)` (20 unknowns). For fixed `B` this is a **square `24 x 24`** homogeneous system in `A`: a curve exists iff `det M(B) = 0`. **One condition on a 19-dimensional projective `B`-space.**

- **Not vacuous:** `det M(B) != 0` on `29/30` (`q=97`) and `30/30` (`q=193`) random `B` — the D-F falsifier did not fire (`d2_results.txt:4`).
- **Rate as predicted:** `4/223 = 0.0179` vs `1/97 = 0.0103`; `3/638 = 0.0047` vs `1/193 = 0.0052` (`d2_results.txt:5`).
- **Certification is against the ORIGINAL system**, never through the reduction: `deg Q_0 = deg Q_2 = 7`, `s = deg gcd(Q_0,Q_1,Q_2) = 0`, separation rank 3, `nullity(36x32) >= 1`, generic rank 7, **`M(Z)Q_Z=0` re-checked entrywise from scratch**, and **zero kernel vectors of parameter degree `<= 1`** (a `27x16` system) so `e = 2` exactly.
- **Rejections were exactly the two banked degeneracies:** `deg Q_2 != 7` (the Kummer death, 1 case) and `s != 0` (7 cases) at `q=97`; none at `q=193` (`d2_results.txt:6`).

### D2.2 The witness (reproducible, `q = 97`)

```text
f = [42,13,19,51,10]   g = [83,79,17,36,40]   h = [58,28,77,64,20]   k = [2,60,10,65,31]

Q_0 = [ 7, 10, 78, 31, 43, 62, 29, 22]
Q_1 = [80, 88, 69, 63, 34, 94, 70, 62]
Q_2 = [80,  4, 73, 12, 82, 59, 47,  1]
y_0 = [77,90,33,0,95,81,25,10,92,6,84,21,86,26,40,74]
y_1 = [ 1,20,62,91, 3,28,56,71,93,78,43,53,86,96,93, 1]
```

| certified property | required | measured |
|---|---|---|
| `deg(Q_0,Q_1,Q_2)` | `(7,7,7)` (leading param coefficient a genuine degree-`rho` locator) | `(7,7,7)` |
| separation rank of `Q` | `m+1 = 3` (`(RNC2)`) | **3** |
| `s = deg gcd(Q_0,Q_1,Q_2)` | `0` (`(SAT1)`) | **0** |
| `nullity(36x32)` | `>= 1` | **1** |
| generic rank of `M(Z)` | `rho = 4m-1 = 7` | **7** |
| `M(Z)Q_Z = 0` entrywise, from scratch | true | **true** |
| kernel vectors of parameter degree `<= 1` | `0` (else `e < m`) | **0** |
| **minimal index `e`** | **`m = 2`** | **2** |
| rank-drop divisor | `delta = rho-3e = 1` reduced point | **one point `z=10`, rank 6; no drop at infinity** |

Same table at `q=193` (`z=62`), and two more certified objects each at `q=257, 641, 769` (`d3_results.txt`). **Twelve objects, five fields.**

### D2.3 DEF-ID — REAL TRANSPORT OR COINCIDENCE?

**Verdict: a coincidence of counts, and — more decisively — a coincidence of a quantity that governs NEITHER layer.**

`(BIV-G)` (`rh_bivariate_system/REPORT.md:347-358`) has `G`-unknowns `(3m-2)m = 3m^2-2m` and `G`-conditions `6m(m-1)+(m-1)(m-2) = 7m^2-9m+2` (`:363-365`). `(L2)` has unknowns `16m` and conditions `(m+2)(4m+1)`. The identity is real and exact:

```text
(m+2)(4m+1) + m(3m-2)  ==  (m-1)(7m-2) + 16m  ==  7m^2+7m+2.
```

Three reasons it is not a transport:

1. **Incompatible shapes.** `(BIV-G)` is quadratic-vs-quadratic with ratio `-> 7/3` (`REPORT.md:366`); `(L2)` is **quadratic-vs-LINEAR** (`4m^2+9m+2` against `16m`), ratio `-> infinity`. At `m=2`: `12` on `8` versus `36` on `32`, and after my canonical reduction `18` on `14`, and after D-B `14` on `10`. **No two of these shapes agree** — only the difference does. A transport carrying witness technology would have to preserve solution spaces, hence shapes.
2. **The two deficits arise from structurally different expressions.** `(L2)`: `deficit = mT - 2rho` with `T=4m+1, rho=4m-1` (from the reduced shape `m(4m+1)` on `2(4m-1)`). `(BIV-G)`: `deficit = (m-1)(a-1) - m(3m-2)` with `a = 7m-1`. Same value, different provenance.
3. **DECISIVE: the shared quantity governs neither layer.** I have shown the `(L2)` deficit does **not** control `(L2)` existence — the controlling number is `11m-4`, positive at every `m` (D1.3), and the layer is **nonempty at `m=2` by construction**. A transport of a non-governing quantity transports nothing. Symmetrically, `(BIV-G)` is realizable at `m=3` (bank 3) despite deficit `+17`.

**P4 resolves NO.** And the operative sub-question — "would it carry bank 3's `m=3` witness technology into an `(L2)` construction?" — is **moot**: my `(L2)` construction needed no bank-3 technology, only the squareness accident at `m=2`. **Caveat (MISS 10): this verdict is from inside my quarantine.**

---

## D3 — THE EMPTINESS ATTACK

**Refuted at `m=2` by D2. Reported anyway, because the exact characterization survives and is the instrument for `m >= 3`.**

**The nullity-drop locus, exactly (not a rate).** For `Q_0,Q_2` squarefree of degree 7, pairwise coprime with `Q_1`, the locus is

```text
{ Q :  rank Phi(Q) <= 9 },     Phi the 14 x 10 matrix of D-B,
```

i.e. the simultaneous vanishing of all `C(14,10) = 1001` maximal minors — entries linear in the coefficients of `Q`. Its structure, both fields:

- an **excess component** of dimension **21**: `Q_0,Q_1,Q_2` share a root `x*`; there `nullity = 2` exactly (40/40 per field, `d1_results.txt`), generic rank 1, `s != 0` — forbidden by `(SAT1)` (`saturation_rigidity/statement.md:13`). This is round 34's degenerate family, now with a dimension.
- at least one **good component** of dimension exactly **18 = 23-5**, containing my witnesses, on which `s=0`, generic rank 7, `e=2`, `delta=1` (D1.4).

**Can the `+4` be a theorem at `m=2`? NO — the good component is nonempty and of expected dimension.** The only surviving emptiness question is at `m >= 3`, where the analogous count gives expected dimension `11m-4 = 29, 40, 51, ...` — **also positive**, so an `m>=3` emptiness proof would have to defeat a positive expected dimension, i.e. come from structure, not counting. **I did not attempt it and I claim nothing about it.**

**What replaces the emptiness route.** The binding constraint returns to the domain layer, and the witnesses measure it for the first time on a real object (`d4_results.txt`):

| field | locator root-count histogram over all finite parameters (roots in `F_q`) | parameters splitting completely | `T` over `mu_32` | max roots in `mu_32` |
|---|---|---|---|---|
| 97 | `{0:31, 1:39, 2:17, 3:6, 4:1, 5:1}` | **0** | **0** | 4 |
| 193 | `{0:74, 1:71, 2:34, 3:11}` | **0** | **0** | 1 |

The `q=97` histogram is the Poisson(1) law of a random degree-7 polynomial (`36.6/36.6/18.3/6.1/1.5/0.3` percent) to within noise. **Having a syndrome pencil buys nothing at the splitting layer** — the same "no structural enhancement" round 34 measured on nets without pencils (`r34_m2_decision/REPORT.md:146`), now measured on nets with them. **This is the sharpest statement the round supports about the strict endpoint: `(L2)` is free, and `(SAT3)` is where the entire difficulty was and remains.**

---

## D4 — VERDICT

> **R-L2 RESOLVED: NONEMPTY. A `(4m+1) x 4m` Hankel pencil with minimal index exactly `m=2`, generic rank exactly `4m-1=7`, `s=0`, `delta=m-1=1` and independent `Q_0,Q_1,Q_2` EXISTS — twelve certified objects over five fields, each re-verified entrywise against `M(Z)Q_Z=0`. The `(L2)` gate does not close the endpoint at `m=2`, and by the `11m-4` count it was never going to close it at any `m`. The difficulty is entirely at the domain/split layer: `T = 0`, and not one locator splits over `F_q`. THIS PART IS A THEOREM (existence is witness-checkable). Everything about `m >= 3`, about `(SAT2)-(SAT5)`, and about `q ~ 2^128` is NOT.**

**Which of D1's two counts survived contact:** *neither, as an existence verdict.* The incidence count `19` is contaminated by a dimension-21 excess component (verified). The TCAP ledger `+3..+5` prices a different object `(SAT3)` and is untouched. The count that survives is the one neither pilot wrote down: **expected dimension `11m-4`, positive at every `m`, and at `m=2` confirmed by construction** (dimension exactly 18).

**Handoff, priority order (recommendations only — AUDIT-AND-DRAFT).**
1. **Re-price R-L2 on the board**: the `e=m` stratum is nonempty at `m=2`; the emptiness route to the strict endpoint is dead at `m=2` and expected-dead at every `m` by the `11m-4` count. Round 34's "proving that stratum empty for `m>=2` closes the strict endpoint" should be re-posed as an `m>=3`-only question **and** cross-checked against MISS 2.
2. **Triage MISS 2 first.** `endpoint_residual_pole_interpolation_exclusion` is PROVED and claims every `e=m` defect stratum on even rows `m>=6` is impossible, including the official `m=2^37` row. If correct, R-L2 was never the decisive question for the official endpoint and the board's "decisive question" label needs moving.
3. **The real gate is `(SAT3)` on an `(L2)` object.** The joint question — an `(L2)` witness whose locators split over a multiplicative domain at `T = rho+2 = 9` parameters — is now stateable with both halves realizable in isolation. My inversion controls the `(L2)` half exactly and leaves `f,g,h,k` free; **designing `B` so that the resulting `Q_z` split over `mu_32` is the natural next instrument** and I did not attempt it.
4. **Do not spend compute on blind `(L2)` search at any `m`.** Blind is `q^-5`; the inversion is `q^-1` at `m=2`. At `m>=3` the squareness is lost (`80` equations on `48` for fixed `B`) and a new inversion is needed.
5. **F1/(NEWCAP):** exercised only weakly (`a* = 13 = 7m-1` over all slope pairs, one witness at `12`); a genuine test still needs supported slopes.

---

## PREDICTIONS vs OUTCOMES

| registered | outcome |
|---|---|
| **D-A** blocks 0,3 have rank exactly 9; the `+4` is entirely in the cross blocks | **VERIFIED**, `{9:40}` per field, both fields (`d1_results.txt`) |
| **D-B** `nullity(36x32) == 10 - rank(Phi)`, the `14x10` congruence criterion | **VERIFIED**, `120/120` per field, both fields; falsifier did not fire |
| **D-C** existence codim is `5`, not `4` | **VERIFIED** (determinantal, two independent derivations agree; `0/120` random hits per field) |
| **D-D** `e <= (4m-1)/3`; `e=2 => delta=1` (one reduced rank-drop point) | **VERIFIED on real objects** (one drop point, rank 6, none at infinity, both fields) — but **BANKED**, not mine (MISS 1) |
| **D-E** common-root locus has dim 21 and sits inside the solvability locus => excess | **VERIFIED**, nullity `{2:40}` per field, both fields; falsifier did not fire |
| **D-F** `det M(B)=0` is one condition; hit rate `~1/q` | **VERIFIED**, `0.0179` vs `0.0103`, `0.0047` vs `0.0052`; det not identically zero (`29/30`, `30/30`) |
| **P1** stratum nonempty over `F-bar` = 0.75 | **HIT — resolved YES**, constructively, over five fields |
| **P1b** nonempty over a small prime field = 0.85 | **HIT** — `q=97,193,257,641,769` |
| **P2** a fully certified witness lands this round = 0.60 | **HIT** — 12 objects |
| **P2b** D-F is the route = 0.80 | **HIT** — it was the only route run |
| **P3** an emptiness proof lands = 0.08 | **resolved NO — refuted by my own D2** (MISS 3) |
| **P4** DEF-ID is a real transport = 0.30 | **resolved NO** — coincidence of a quantity governing neither layer (D2.3); quarantine caveat (MISS 10) |
| **P4b** I can locate `(BIV-G)` = 0.55 | **HIT** — `rh_bivariate_system/REPORT.md:347-358` |
| **P5** the `+4` is transverse (no excess on the good component) = 0.55 | **HIT** — good component has dimension exactly `18 = 23-5`, fibre of `B` a point, both fields |
| **P5b** operative codim is 5 = 0.90 | **HIT** |
| **P5c** excess component of dimension 21 = 0.88 | **HIT** |
| **P6** D-B verifies with no correction = 0.70 | **HIT** |
| **P7** the `e <= (4m-1)/3` ceiling verifies = 0.80 | **HIT** — and it was already banked (MISS 1) |
| **P8** `T >= 1` over `mu_32` without designing the domain = 0.05 | **resolved NO** — `T=0`, and *no* locator splits over `F_q` at all |
| **P8'** `a*` measurable and in `{13,14}` = 0.80 | **partial HIT** — `a* = 13` on 5 of 6, **`12` on one** (MISS 7); and it is not the endpoint's `a*` (MISS 6) |
| **P9** the `(L2)` question is already answered in-repo = 0.10 | **resolved NO for `m=2`**, but see MISS 2: a PROVED node answers the *endpoint* `e=m` question for even `m>=6` |

---

## ZERO-POWER DECLARATIONS

1. **Z1 (pre-declared) is now moot on the positive side and stands on the negative side.** A negative search at these `q` would have had zero power (codim 5, `q^-5`); a **witness** has full power, and that asymmetry was registered in advance as MISS-2 guard (iii).
2. **Z2 honoured: I never used the Thom–Porteous/Fulton–Lazarsfeld nonemptiness argument**, precisely because D-E predicted (and I then verified) an excess component that would account for the class. The witness is constructive.
3. **Z3 partially discharged: F1 was exercised for the first time in four rounds, but weakly** — `a*` over all slope pairs, not over supported ones (MISS 6). **(NEWCAP) remains at zero power.**
4. **Z4 honoured: `T = 0` over `mu_32` is reported with zero power over `(SAT3)`.** The stronger fact — no locator splits over `F_q` at all — is a *measurement on 6 objects*, not a theorem about the good component.
5. **Z5 stands: five prime fields, no lift to `Z`, no `q ~ 2^128` statement.** The construction is a codimension-one condition on a parameter space defined over the prime field, which is the reason it worked at every field tried; that is an explanation, not a proof of uniformity.
6. **The `11m-4` ledger is a heuristic** with the `pb_design_ceiling/proof.md:125` blind spot. It has **zero power** as a bound; its only confirmed instance is `m=2`, where the witness makes it moot. MISS-2 guard (iv) honoured: I do not quote `19`, `18`, `+4` or `+5` as evidence for or against emptiness anywhere.
7. **The greedy designed-domain `T` is a lower bound on the best designable `T`, and in this round it had no input at all** (MISS 5).
8. **`max shared roots = 1` is a maximum over all `C(q,2)` pairs for six specific objects** — not a statement about the good component. Sample maxima never become bounds (MISS-2 guard (i)).
9. **Nothing here bears on `m >= 3`, on the `9/4`, the `7/4` ledger, FR-canonical, or Rout.**

---

## MEASURED FUNCTIONALS (CATCH-19C)

`m, rho=4m-1, N=16m, R=8m, r=rho, A=R+1-2rho=3, e, s, delta=rho-3e`; rank of block 0 / block 3 on `y_i`; `nullity(36x32)`; `rank Phi` for the `14x10` congruence matrix and `dim ker Phi`; `det M(B)` for the `24x24` inversion matrix and its vanishing rate; `deg Q_j`; `deg gcd(Q_0,Q_1,Q_2) = s`; separation rank of `Q` (`(RNC2)`); generic rank `max_z rank M_r(y_0+zy_1)`; the finite rank-drop set and the rank there (`delta`); rank at infinity; dimension of the degree-`<=1` kernel (the `e<=1` filter); left nullity of `M_r(y_0)` and the left-kernel generators `Q_Z, X Q_Z`; per-parameter locator root count in `F_q` and in `mu_32`; `T` over `mu_32`; `T` over a greedy designed 32-subset; `max_{g != g'} deg gcd(Q_g,Q_{g'})`; `a* = w* = min|S_g u S_{g'}|`; `d_x`, saturated-point count, `sum_x(m-d_x)` and `O` (all vacuous at `T=0`); expected dimension `11m-4`; the dimension of the excess component (21) and of the good component (18).

**Registered but NOT measured:** `T` on any object with supported slopes (none exists — MISS 4/5); the endpoint's `a*` over supported pairs (same reason — MISS 6); any `m >= 3` quantity (MISS 8); the iso-class structure of the good component; whether the good component is geometrically irreducible or defined over `Z` (MISS 9).

---

## COMPLIANCE

**Registrations.** R0 (route order), six falsifiable pre-committed derivations D-A…D-F **each with its own falsifier**, numeric priors P1–P9, the four-clause MISS-2 mean-vs-max guard, and six zero-power declarations were appended to `PREREG.md` under "## Pilot registrations" with the **Edit tool**, after reading **exactly** the two named anchors and **before any other read, any grep, any `ls`, and any interpreter invocation**. **No post-registration addenda.** The registered route order (verify structure → verify D-B → reconcile counts → inversion → certify → emptiness → verdict) was followed exactly; D3 was executed and reported even after D2 had already refuted its target.

**Compute law.** **Four interpreter invocations, every one of the form `tools/ramguard local -- python3 …` issued from the repo root with the literal `--`**, each with an explicit documented `RAMGUARD_TIMEOUT` (`280` for `d1_structure.py`; `290` for `d2_invert.py`, `d3_scale.py`, `d4_tmeasure.py` — inside the `local` profile's 5-minute ceiling, not an extension). **Zero bare `python3`, for any purpose** — no file patching, no probes, no empty heredocs. Stdlib only; no third-party imports, no Modal, no network, no git, no subagents. **Ramguard status: four clean exits, no memory or timeout event.**

**Write discipline (upgraded clause).** **No `sed -i`, no `awk -i`, no `perl -i`, no `tee`, no shell redirection onto any existing file, no in-place shell stream edit of any file.** Every file I authored was created with the **Write** tool; the single edit to `PREREG.md` used the **Edit** tool. The two bounded reads that used `head`/`sed -n` were **read-only stream reads with no `-i`**, used as RAM-discipline windows, not writes. Scripts created and overwrote only their own results files (`d1_results.txt`, `d2_results.txt`, `d3_results.txt`, `d4_results.txt`), as the constraint permits.

**RAM discipline.** `dag.json` **never opened**. Node shards and grep only. Every large statement was read in a bounded window (`endpoint_saturation_rigidity` in two windows of 16 lines; `residual_pole_interpolation_exclusion` head-20; `rate_half_band_crossing_location` — a 3399-line file — in a single 130-line window; `rh_bivariate_system/REPORT.md` in one 40-line window). Each script holds `O(q + N^2)` state and writes its own results file.

**Quarantine — clean, with search-level exclusion.** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` **never opened, never traversed**. **No sibling `r35_*` directory was opened, read or traversed**; one `ls` of the shared parent `notes/pilots_20260811/` displayed their names, which I disclose (MISS 11). **Every recursive grep carried `--exclude-dir='r35_*' --exclude-dir='prize-codex-*' --exclude-dir='pilots_20260802' at the SEARCH level**, never as output filtering; the one non-recursive grep targeted a single explicitly-permitted file. No path containing `prize-codex-` was touched. `r34_*` and `rh_*` dirs were read as explicitly permitted; **no banked script was run** (I wrote all four of mine from scratch, so the copy-before-running rule was not engaged).

**Write scope.** Every write is inside `notes/pilots_20260811/r35_l2_gate/`: `PREREG.md` (registrations appended), `_shared.py`, `d1_structure.py` + `d1_results.txt`, `d2_invert.py` + `d2_results.txt`, `d3_scale.py` + `d3_results.txt`, `d4_tmeasure.py` + `d4_results.txt`. **No `dag/`, `nodes/`, `background/`, `critical/` or `tools/` edits; no git; the session scratchpad was not used.** AUDIT-AND-DRAFT respected: nothing outside my directory was altered, every recommendation above is posed for coordinator triage, and **`REPORT.md` is not written** — per the brief's fallback clause this report is returned verbatim as my final message.

**Method discipline.** CATCH-24A greps ran **before** every novelty claim, including hyphenated/infixed variants of every key phrase, and produced **eight live subtractions, three of them load-bearing**: my registered D-D is banked twice (`(MI1)`, and `delta=rho-3e` inside `(SAT1)`); the whole `(L2)` framing is the coordinator's banked gate; and a **PROVED** node already excludes `e=m` endpoint strata on even rows `m>=6` including the official row, which re-prices my own mandate. Every quantifier claim carries a `file:line` or a results-file citation. Every max-quantified claim carries a zero-power declaration. **Two-field confirmation for every structural claim** (`q in {97,193}` throughout; `257, 641, 769` added for the construction). **MISSES FIRST**, and the round's own self-corrections — that my headline derivation was already banked, that D3's deliverable was killed by my own D2, that the `(SAT1)-(SAT5)` table cannot be filled, and that one witness disagrees with the other five on `a*` — are reported as falsifications of my own work, in that order, before any result.
