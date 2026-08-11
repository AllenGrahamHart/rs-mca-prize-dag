All experiments complete. Here is the full report.

---

# REPORT — r35_fg_razor (round 35)

## VERDICT

**R-FG-RAZOR: WALLED WITH A NAMED GAP — AND DOWNGRADED. The brief's D2 question is malformed at far-CA razor shape, because the type-2 spend/list ledger is VACUOUS there by sign. FG does not break a banked cap, does not produce the strict-endpoint contradiction, and — the round's main finding — is not where the extremal bad-slope count lives.**

Three results, each two-field-or-better confirmed:

1. **The type-2 ledger does not transfer.** `(C2)`'s per-slope spend floor is `(R+1) − w*` with `w* = |W| ∈ [r, 2r]` the joint-support size (`notes/pilots_20260810/apolar_origin/PREREG.md:181-186`). It is positive for *every* admissible `W` iff `2r ≤ R`, i.e. `r ≤ R/2`, i.e. `a ≥ 3n/4` — **exactly the top of the open bracket** (`critical/nodes/rate_half_band_crossing_location/statement.md:982`). The open bracket `[k+2^34, 3n/4)` is entirely below it. At razor shape `2r = 2,164,663,517,184 ≤ n = 2,199,023,255,552` (slack exactly `2rho = 2^35`), so the adversary can take `w* = 2r` and the floor becomes `−1,065,151,889,407`. **Vacuous, not slack.**

2. **FG carries no structural bad-slope floor; LB1 does.** At six rate-half razor-faithful cells across two shapes, in the subcritical regime `mu_1 = C(n,r)/q^rho < 1` where every admissible official row lives: LB1's type-1 slope count is **exactly `r+1`**, field-size independent (9/9 ledger rows). Witness B's FG replica has `T_1 = 2` or `3` — its trivial floor — at 9/9 ledger rows, and total `T` that tracks `q·mu_1` and falls **below** `r+1` (e.g. `T = 1` at `n=22, q=65537`, against `r+1 = 10`).

3. **LB1 is not in FG, not in the intermediate stratum, and sits one integer above it.** Measured `p*(LB1) = floor((R+2)/2) = floor(R/2)+1` at 5/5 rate-half shapes (`R = 10,11,12,13,14`), with `h_r = rho+1` and `dim K_0 = r−rho` at 5/5. At the razor that is `p* = 2^39+1 = 16·(2rho)+1`, exactly one above `floor(R/2)`, the top of the intermediate band, and sixteen octaves above FG's `2rho`.

`B_ca^far(k+2^34) < 2^128`: **NO.** I add no upper bound. R0-a was registered at 0.12 and the "walled" branch at 0.55; the latter fired.

---

## MISSES FIRST

1. **MY FIRST CELL DESIGN WAS NOT RAZOR-FAITHFUL AND WOULD HAVE INVERTED THE ROUND'S HEADLINE.** `e1`'s cells (`k=1`) satisfy the registered separating condition `4rho < R` but have `a−1 = 2..3 < r`, while the razor has `a−1 = 1,116,691,496,959 > r`. That sign governs `p*(LB1)` entirely: at `k=1`, `p*(LB1) = rho+1 = 3,3,4,4,4` (`e1_results.txt`, summary table); at rate half, `p*(LB1) = 6,6,7,7,8`. **Had I stopped at `e1` I would have banked `p*(LB1) = rho+1 ≤ 2rho`, i.e. declared LB1 to be inside the FG bracket — the exact opposite of the truth.** Caught by re-deriving `p*` by hand and rebuilding every cell at rate half (`e2a`, `e2b`, `e4`).

2. **MY OWN PRINCIPALITY TEST WAS WRONG AND PRODUCED A FALSE "NOT PRINCIPAL".** `e1`/`e2` tested `K_0 == g·F[x]_{≤ r − deg g}`. The containment that `h_r = p*` actually yields is `K_0 = P·F[x]_{≤ r − p*}` with `P ∈ Ann(V)_{p*}` of degree `d* ≤ p*` — the *window index*, not the degree. At the three `k=1` LB1 cells the first test returns False and the second True (`e4_results.txt`). The FG verdict is unchanged only because round-33 FG additionally demands `deg P = p` and there `d* = 3 < p* = 4`. I re-ran (`e4`) rather than let the wrong diagnostic stand.

3. **MY PRE-COMMITTED E20 IS ARITHMETICALLY RIGHT AND INTERPRETATIVELY WRONG.** I committed `(R+1)−a = −17,179,869,183` under the reading `a = k+rho`, and hedged `P = 0.45` that the banked "(R+1)-a floor" uses that `a`. **It does not.** `(C2)`'s `a` is `|W|`, a joint-support size in `[r, 2r]` (`apolar_origin/PREREG.md:181`). The razor object is `(R+1) − w*`, and E20 is not it. The registered 0.55 alternative fired; my razor number for the floor had to be recomputed.

4. **MY FIRST PADÉ DERIVATION OF `p*(LB1)` WAS WRONG.** I derived `p* = ceil((R+2)/2)` from the shifted minimal indices, ignoring that the auxiliary polynomial `E = prod_{y ∈ D\T}(x−y)` has degree `a−1`, which is *small* at `k=1`. The corrected law `p*(LB1) = max(rho+1, floor((R+2)/2))`, `d* = min(a−1, ·)`, reproduces both regimes (5/5 rate-half, 3/3 `k=1`, `e4_results.txt`). The razor conclusion survives; the derivation did not, first time.

5. **THE `2^128` COINCIDENCE IS A COINCIDENCE AND I NEARLY READ IT AS STRUCTURE.** `theta_1 = n·H2(r/n)/rho = 128·H2(63/128) = 127.977457` agrees with the prize's `B*(q) = floor(q/2^128)` to `0.0225` bits. The `128` in `theta_1` is `n/rho = 2^41/2^34` at the razor row; the `128` in `B*` is `EPSILON_BITS`, the prize soundness parameter (`tools/prize_row_descriptor.py:16`). **Unrelated.** My registered `P = 0.50` for "within a factor 2" HIT, but the hit is numerological and I say so rather than bank a false link.

6. **NO BOUND.** `B_ca^far(k+2^34) < 2^128` remains **NO**. I add no upper bound of any kind. Registered at 0.05; the round is a re-prioritisation, not an addition.

7. **ZERO RAZOR-REGIME MEASUREMENT, AND A DISCLOSED WIDENING.** Every machine number is at `q ≤ 65537`, `R ≤ 14`, `rho ≤ 3`, `r ≤ 19`. ZP-1 registered `q ≤ 31`; I went to `q = 65537` because the exact `O(rho)` bad-slope test removed the field-size ceiling and the subcritical regime is unreachable at `q ≤ 31`. A deviation in the permissive direction, disclosed.

8. **`rho = 3` AT RATE HALF IS STRUCTURE-ONLY.** `4rho < R` plus rate half forces `n ≥ 26`, and `C(26,10) = 5,311,735` put the `rho = 3` rate-half bad-slope census out of reach in stdlib Python. The `rho = 3` `T` census exists only at the non-faithful `k=1` cells. Declared, not hidden.

9. **I KILLED A RUN AND IT COMPLETED ANYWAY.** My first `e2_budget.py` had an `O(T^2·L^2)` ledger (7.6e9 operations at `q=23`). I issued `pkill`; it returned 144 and the harness then reported exit 0. It wrote **no** results file (no `e2_results.txt` exists in my directory). It counts as one of my six interpreter invocations and produced nothing.

10. **ONE REPLICA ROW IS INVALID AND I REPORT IT RATHER THAN DROP IT.** At `n=20, q=23` the LB1 replica has 5 common `D`-split locators in `K_0` (`e2a_results.txt:14`), so that row is column-**close**, not a valid far-CA instance. Expected `C(20,8)/23^3 = 10.35`. It is column-far at every `q ≥ 101` (0 col-close locators, 10/10 rows).

11. **ONE FG INSTANCE IS DEAD AS A LIVE INSTANCE.** At `(n,k,r) = (19,1,15)`, `q=19`, the FG replica has `T = 0` — no bad slopes at all (`e2b_results.txt:28`). A valid FG member, a useless budget instance; the same failure mode as anchor 1's miss 4.

---

## CATCH-24A SUBTRACTIONS (own-repo greps before every novelty claim)

Every recursive grep used search-level `--exclude-dir` for `prize-codex-work`, `pilots_20260802`, and the three sibling `r35_*` directories, whose *names* (not contents) I obtained with `find -maxdepth 1 -type d -printf '%f\n'` — disclosed, and the reason the exclude list is certifiable this round.

| # | claim | grep | banked? | verdict |
|---|---|---|---|---|
| 1 | the FG stratum, the `rho x p` scaled Vandermonde, the key equation `C_gamma·sigma ≡ h mod P`, (MI1) restored / (MI2) blocked | `-riE "key[- ]?equation"` | **YES** — `crossing_location:3054-3065` (round 33), residual named at `:3396` | **SUBTRACTED — round 33's, not mine** |
| 2 | `p*`, `h_r`, `codim{p* ≤ p} = 2R−3p`, the factor-16 correction, the intermediate stratum `2rho < p* ≤ R/2`, witnesses A and B | `-riE "intermediate stratum\|intermediate band"`, `-rnE "h_r\|stacked rank"` | **YES** — `crossing_location:3066-3085` (round 34) | **SUBTRACTED — round 34's** |
| 3 | `q_crit ~ 2^64`, "below it the column-far locus is measure-zero and every random model in this lane is void" | `-riE "q_crit\|q crit\|2\^64"` | **YES** — `crossing_location:3084`; zero far-CA hits elsewhere | **SUBTRACTED — round 34's.** My additive part: `theta_1 = 2·theta_2 = 127.977457`, the exact evaluation on the official row, and the shape-dependence catch below |
| 4 | LB1's construction, `B_ca^far(a) ≥ n−a+1 = r+1`, LB1-C `n < (a−k−1) log2 q` with margin 670,014,898,009, "88.02 bits below the 2^128 budget" | `-rnE "LB1-C\|a-k-1"` | **YES** — `crossing_location:635-645, 654-656` | **SUBTRACTED.** I reproduce the constant exactly as an independent check |
| 5 | `d_x = r` at LB1, "corank-0, its petal structure forces `d_x = r > e`" | `-rnE "d_x = r"` via `:3010-3011` | **YES** — `crossing_location:3010-3011` | **SUBTRACTED.** I re-derive it and confirm at 3 cells, 3 fields |
| 6 | budget `2^39` dead at `a = 3n/4` by LB1; `B_ca^far(3n/4) ≥ 2^39+1` | `-rnE "3n/4"` | **YES** — `crossing_location:659-662, 1038` | **SUBTRACTED** |
| 7 | `r ≤ R/2 ⟺ a ≥ n−R/2 = 3n/4` (the unique-decoding radius) | `-rnE "r <= R/2\|r<=R/2"` | **YES** — `crossing_location:982`; and `minimal_index_budget/statement.md:58,102` scopes the deployed corollary to `r ≤ R/2−2` | **SUBTRACTED** |
| 8 | "counting void at the razor", "the common wall of ALL counting instruments" | `-riE "counting void\|all counting instruments"` | **YES** — `crossing_location:985-987` | **SUBTRACTED.** My additive part is the *mechanism* for `(C2)` specifically: the floor's **sign**, and the exact `w*` threshold |
| 9 | **any statement linking type-2 / `X_gamma` / the `(C2)` ledger to far-CA or razor shape** | `-rniE "type[- ]?2.*(far[- ]?CA\|razor)\|(far[- ]?CA\|razor).*type[- ]?2"` on `critical/nodes background/nodes` | **ZERO HITS** | **ADDITIVE** |
| 10 | `mu_1 = C(n,r)/q^rho`, `mu_2`, first-moment thresholds in the far-CA lane | `-rnE "first[- ]moment\|C\(n,r\)/q\|mu_1\|mu_2"` | hits only in `dli`, `petal_g1`, `xr`, `fm1` lanes — **no far-CA hit** | **ADDITIVE** |
| 11 | `p*`, `h_r`, `dim K_0` **of LB1** | `-rnE "LB1.*(p\*\|h_r\|K_0)\|(p\*\|h_r\|K_0).*LB1"` | one hit, `crossing_location:3080`: "LB1 is GENERIC (`p* = r+1 = ceil(2R/3)`, 3591/3591)" — round 34, and that is at **LB1's own `k=2` small cell**, not at razor shape | **ADDITIVE, and it CORRECTS a banked reading** (see flag 2) |

**Genuinely additive this round:** (a) the `(C2)` transfer analysis — the floor's sign, the threshold `w* ≤ R ⟺ |S_g ∩ S_h| ≥ 2r−R = 62r/63`, and the identification of the ledger's scope boundary with `a ≥ 3n/4`; (b) `p*(LB1) = max(rho+1, floor((R+2)/2))` with `d* = min(a−1, ·)`, and the consequence `p*(LB1 at razor) = floor(R/2)+1 = 16·(2rho)+1`; (c) `h_r(LB1) = rho+1`, `dim K_0(LB1) = r−rho`; (d) the measured presence/absence of a structural `T`-floor (LB1 yes, FG no) across the `mu_1 = 1` threshold; (e) the LB1-C ≡ `mu_1 < 1` identification with its exact residue `log2 q + n(1−H2(r/n))`; (f) `theta_1 = 2·theta_2` and the shape-dependence of `q_crit`; (g) the `h_r`-dictionary re-prioritisation of R-FG vs R-KER; (h) `h_r = p*` is necessary but **not sufficient** for round-33 FG.

---

## D1 — THE KEY EQUATION INSTANTIATED

### D1.1 The exact objects at witnesses A and B, razor parameters

Razor shape: `R = k = 2^40`, `rho = a−k = 2^34`, `r = n−a = R−rho`, `n = 2R = 2^41`, `D ⊆ F_q`, `|D| = n`. Dictionary derived from the anchors' `(n,k,a)` cell tables and confirmed by the banked-constant check in D2.4: **`R = n−k`, `r = n−a`, `rho = R−r = a−k`.**

At witness B (`P* = P_1 P_2`, `P_1` irreducible of degree `rho`, `P_2` squarefree of degree `rho`, coprime — `crossing_location:3074-3075`), the key equation `C_gamma·sigma ≡ h (mod P*)` has exactly these objects (`e3_results.txt`, all integers exact):

| object | value |
|---|---|
| modulus `P*`, `p = deg P* = 2rho` | `34,359,738,368` |
| `Lambda = F[x]/(P*)`, `dim_{F_q}` | `34,359,738,368` |
| `sigma`: `deg ≤ r`, unknowns | `r+1 = 1,082,331,758,593` |
| `h`: `deg h ≤ m_Q−1`, unknowns | `m_Q = p−rho = 17,179,869,184` |
| `C_gamma`: `deg ≤ p−1` | `34,359,738,367` |
| total unknowns `(r+1)+m_Q` | `= R+1 = 1,099,511,627,777` |
| constraints (the congruence mod `P*`) | `p = 34,359,738,368` |
| DOF surplus `(r+1)+m_Q−p = R+1−p` | `1,065,151,889,409 = deg Q' = m_P+m_Q = r+1−rho` |
| `U_gamma = C_gamma^{-1}Lambda_{<m_Q}`, `dim` | `m_Q = 17,179,869,184` |
| `codim U_gamma` in `Lambda` | `rho = 17,179,869,184` |
| `dim K_0 = m_P = r+1−p` | `1,047,972,020,225` |

The identity `(r+1)+m_Q = R+1` is **special to `p = 2rho`** (saturated FG) and is checked True in `e3_results.txt`. Witness A (`P* = x^{2rho}`, non-squarefree) is deliberately excluded from the key-equation analysis: FG3/FG4 assume `P*` squarefree (ZP-7).

### D1.2 The faithful replicas, and what "faithful" had to mean

A replica is razor-faithful only if it reproduces **four** signs, not two. The two the brief named (`4rho < R`, so the intermediate band is nonempty) I registered; the two I discovered are `a > R+1` and `a−1 > r`. `k=1` cells fail both (miss 1). All rate-half cells satisfy all four.

| shape | `q` | `n` | `k` | `R` | `rho` | `r` | `a` | `4rho<R` | `a>R+1` | `a−1>r` | band `(2rho, R/2]` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| H1 | 23,101,349,1009,10007,65537 | 20 | 10 | 10 | 2 | 8 | 12 | ✓ | ✓ | ✓ | `{5}` |
| H2 | 101, 65537 | 22 | 11 | 11 | 2 | 9 | 13 | ✓ | ✓ | ✓ | `{5}` |
| H3 | 101 | 24 | 12 | 12 | 2 | 10 | 14 | ✓ | ✓ | ✓ | `{5,6}` |
| H4 | 101 | 26 | 13 | 13 | 3 | 10 | 16 | ✓ | ✓ | ✓ | `{}` (`2rho=6=R/2`) |
| H5 | 101 | 28 | 14 | 14 | 3 | 11 | 17 | ✓ | ✓ | ✓ | `{7}` |
| S1–S3 (`k=1`, **non-faithful**) | 17,19,23 | 17,19,23 | 1 | 16,18,22 | 3 | 13,15,19 | 4 | ✓ | ✗ | ✗ | `{7,8},{7,8,9},{7..11}` |

**Witness-B faithfulness, 10/10 cells, `rho ∈ {2,3}`, ten fields `q ∈ {11,13,17,19,23,101,349,1009,10007,65537}`** (`e1_results.txt`, `e4_results.txt`): `p* = d* = deg P* = 2rho`; `h_r = 2rho`; `dim K_0 = r+1−2rho`; `K_0 = P·F[x]_{≤ r−p}` with `p = deg P` (the round-33 FG condition, `crossing_location:3059`) **True at 10/10**; column-far True at 10/10; `dim Ann(V)_{p*} = 1` at 10/10 (so `P*` is canonical here). The negative control B′ (`P_1` replaced by a `D`-split squarefree factor of the same degree, everything else identical) is column-**close** at 5/5 cells (`e1_results.txt`, summary table) — the two-directional confirmation of round 33's FG2.

### D1.3 Degrees of freedom vs constraints, measured on the replicas (D-1, D-2, FG5)

Measured at five cells, five fields (`e1_results.txt`, `key-eq` lines):

| cell | `q` | `rho` | `r+1−rho` | rank `M(gamma)` over all slopes | `dim ker M(gamma)` over all slopes | `codim U_gamma` | FG5 shift family |
|---|---|---|---|---|---|---|---|
| S0 | 11 | 2 | 7 | `{2}` | `{7}` | `{2}` | 11/11 |
| S1 | 13 | 2 | 9 | `{2}` | `{9}` | `{2}` | 13/13 |
| S2 | 17 | 3 | 11 | `{3}` | `{11}` | `{3}` | 17/17 |
| S3 | 19 | 3 | 13 | `{3}` | `{13}` | `{3}` | 19/19 |
| S4 | 23 | 3 | 17 | `{3}` | `{17}` | `{3}` | 23/23 |

- **D-1 HIT, and stronger than registered:** I registered `dim = (r+1)+m_Q−p` at `≥ 90%` of slopes; measured at **100%** of slopes at 5/5 cells, with `(r+1)+m_Q−p = r+1−rho` in every case. Reported as an exact set, not a mean (MISS-2 guard item 1).
- **D-2 HIT:** `codim U_gamma = rho` at 5/5 cells, every slope.
- **FG5 (round 33's restored (MI1)) confirmed 83/83** nontrivial slopes across five fields, searching over the whole space rather than an arbitrary basis vector (round 33's own miss 6).

**But D-2's registered significance was partly wrong, and I say so.** I registered "the constraint count is `rho` independent of `p`" as non-trivial. It is trivial: at any generic-rank slope `rank M(gamma) = rho`, so "`sigma ∈ ker M(gamma)`" is `rho` conditions whether or not the pencil is FG. The **non-trivial** content, which the measurement does establish, is the *factoring*: the slope-dependence depends on `sigma` only through its image in `F[x]_{≤r}/K_0`, of dimension `h_r ≤ 2rho = 2^35` — a compression of a `1.08e12`-dimensional object to a `3.4e10`-dimensional one. FG adds only that this quotient is a **ring** and `U_gamma` a **cyclic submodule**.

### D1.4 `h_r = p*` is necessary but NOT sufficient for FG (correction of a banked reading)

Anchor 1's D1.1(iii) — `K_0 = P*·F[x]_{≤ r−p*} ⟺ h_r = p*` — is **true** (verified 10/10 in `e4_results.txt`). But its D1.2 table then labels the row `h_r = p*` as "**FG**". That identification fails: round-33 FG requires `K_0 = P·F[x]_{≤ r − p}` with **`p = deg P`**, and `deg P = d*` can be strictly less than `p*`, because `Ann(V)_i` is defined by a *shrinking* condition set (`R−i+1` conditions), so a low-degree polynomial can first appear at a strictly larger window index.

**Exhibited at three cells, three fields** (`e4_results.txt`, `k=1` blocks): LB1 at `(17,1,13,q=17)`, `(19,1,15,q=19)`, `(23,1,19,q=23)` has `p* = 4 = h_r`, `d* = 3 = a−1 < p*`, `K_0 == P·F[x]_{≤ r−p*}` **True**, `K_0 == P·F[x]_{≤ r−deg P}` **False**, FG **False**. Three column-far pencils with `h_r = p* ≤ 2rho` that are **not** in FG.

---

## D2 — THE BUDGET ARITHMETIC AT RAZOR SCALE

### D2.1 The type-2 ledger, translated into far-CA symbols

`(C2)` (`notes/pilots_20260810/apolar_origin/PREREG.md:181-186`), `(C3)` (`:187-190`), `(C4)` (`:191-192`) are stated in the SAT lane's symbols, where the locator degree is `rho_SAT` and `N=16m, R=8m, rho_SAT=4m−1, e=m` (`notes/pilots_20260811/rh_sat3_realizability/REPORT.md:265`). Mapping by role — `|S_gamma| =` locator degree `= r` in far-CA symbols — the ledger reads:

```
W a joint support of two bad locators,  w* = |W| in [r, min(2r, n)]
type-2 slope  =>  |S_gamma \ W| >= (R+1) - w* + n_gamma           (C2)
type-1 slope  =>  S_gamma subset W,  and  T_1 <= e+1               (C3)
d_x <= e for every x                                              (C4)
T_2 * ((R+1)-w*)  <=  sum_{x not in W} d_x  <=  (n-w*) e
CAP(w*) = floor( (n-w*) e / ((R+1)-w*) )
```

The SAT lane sits at `r = 4m−1`, `R = 8m`, so `2r = 8m−2 ≤ R` and the floor `(R+1)−w* ≥ 3 > 0` **always**. In far-CA symbols the SAT lane sits at `a = 12m+1 = 3n/4 + 1` — the **top** of the open bracket, i.e. the official candidate row's agreement. The razor sits at `a = k+2^34`, the **bottom**.

### D2.2 The floor's sign — the exact scope boundary

`(R+1) − w* > 0` for **every** admissible `W` iff `2r ≤ R`, i.e. `r ≤ R/2`, i.e. `a ≥ n − R/2 = 3n/4` at rate half — the unique-decoding radius, banked at `crossing_location:982`.

**At razor shape the floor is vacuous, by exact integers** (`e3_results.txt`):

```
w* range                     = [1,082,331,758,592 , 2,164,663,517,184]
n - 2r                       = 2rho = 34,359,738,368     (two DISJOINT locator
                                                          supports fit, with room)
worst case w* = 2r:  (R+1)-w* = -1,065,151,889,407        <-- VACUOUS
floor > 0  iff  w* <= R      iff  |S_g ^ S_h| >= 2r-R = 1,065,151,889,408
                                                = 62r/63 = 98.4127% of r
```

So the adversary controls the sign of the type-2 spend floor at razor shape, for free. **The entire open bracket `[k+2^34, 3n/4)` lies strictly below the ledger's scope.** This is the structural answer to the brief's D2: FG neither "stays inside" nor "dies on" the type-2 budget — the budget is not defined there.

### D2.3 What the two families actually do to the ledger, measured

Measured at every rate-half cell (`e2a_results.txt`, `e2b_results.txt`), locator lists capped at `LOCCAP = 24` per slope so `w*` is reported as an **upper** bound on the true `w*`:

| family | `w*` | `(R+1)−w*` | `T_1` | `T_2` | `e = max d_x` | CAP | `T_2 ≤ CAP` |
|---|---|---|---|---|---|---|---|
| LB1, all rate-half rows | `r+1` (9,9,10) | `rho = 2` | **exactly `r+1`**, 6/6 | accidental only | ≥ `r` | 49…649 | True, slack ≥ 1.5 orders |
| LB1, `k=1` rows | `r+1` (14,16,20) | `rho = 3` | **exactly `r+1`**, 3/3 | **0**, 3/3 | `r` = 13,15,19 | 13,15,19 | vacuously True |
| FG (witness B), all rows | `r+1`…`r+3` | 0…3 | **2 or 3**, 9/9 | rest | 4…100 | 4…600, or **None** | True, or **VACUOUS** |

Three things follow.

- **LB1's slopes are all type-1 and spend nothing.** `S_gamma = W \ {gamma} ⊂ W`, so `|S_gamma \ W| = 0` and the `(C2)` floor is never invoked. `T_2 = 0` at 3/3 `k=1` rows.
- **`(C3)` is TIGHT on LB1, at zero bits.** `d_x = r` for every `x ∈ W`, so `e = r` and `T_1 ≤ e+1 = r+1` is **attained**: measured `e = 13,15,19 = r` and `T_1 = 14,16,20 = r+1` at 3/3 cells. This independently re-derives `crossing_location:3010-3011` ("its petal structure forces `d_x = r > e`"). At razor scale `e = r = 1,082,331,758,592`, `e+1 = T_1 = 1,082,331,758,593`.
- **FG has no T1-line at all.** `T_1 ∈ {2,3}` at 9/9 ledger rows — its trivial floor, since the two slopes realising `w*` always qualify. And at `n=20, q=65537` the FG configuration produces `w* = 11 > R = 10`, making the floor `0`: **the razor's vacuity signature, exhibited at small scale.**

### D2.4 Which banked cap binds first, and by how many bits

At razor shape, ordered by slack (`e3_results.txt`):

| cap | source | razor value | FG's value | slack |
|---|---|---|---|---|
| `(C2)` spend floor `(R+1)−w*` | `apolar_origin/PREREG.md:185` | `≤ 0` at `w* = 2r` | n/a | **VACUOUS by sign** |
| `(C3)` `T_1 ≤ e+1` | `apolar_origin/PREREG.md:190` | `e+1 = r+1 = 1,082,331,758,593` | `T_1 = 2` (measured 9/9) | attained by **LB1** at **0 bits**; FG is `e−1` slopes under |
| `CAP(w*) = floor((n−w*)e/((R+1)−w*))` at LB1's `w* = r+1` | `rh_type2_stratum/REPORT.md:87` | `70,351,564,308,417 = 2^45.9996` | `T_2 = 0` | **46.00 bits — the whole cap** |
| `B*(q) = floor(q/2^128)` | `prize_row_descriptor.py:16,120` | `2^39` or `2^39+1` on the residual interval | heuristic `T = 2^{−6.70e11}` | ~`6.7e11` bits |

**No banked cap is broken by an FG pencil at razor shape.** The nearest cap, `(C3)`, is attained — by LB1, not by FG. The only cap actually exceeded anywhere in this lane is `B*(q)`, and LB1 exceeds it: `(r+1)/2^39 = 1.96876`, i.e. **0.977280 bits over the residual budget `2^39`** (banked at `crossing_location:1038`, `:659-662`; reproduced here independently).

**Banked-constant cross-check of the whole dictionary.** LB1-C is banked as `n < (a−k−1) log2 q` with "margin 670,014,898,009 at the bottom" (`crossing_location:640-641`). My independent evaluation at `log2 q = 167`: `(2^34−1)·167 − 2^41 = 670,014,898,009` — **exact match** (`e3_results.txt`). This is the two-field-style confirmation that `a = k+rho`, `n = 2^41`, `rho = 2^34` is the right reading.

### D2.5 The first moment is wrong by 6.70e11 bits, and LB1 proves it

The key equation's per-slope first moment is `mu_1 = |D_r(D)|·q^{-rho} = C(n,r)/q^rho` (density of `U_gamma` in `Lambda` is `q^{-rho}`, `codim U_gamma = rho`). Exact constants (`e3_results.txt`):

```
H2(63/128)      = 0.999823882599
log2 C(n,r)     = 2,198,635,969,291.21   (entropy)   /  ...969,270.39 (lgamma)
theta_2 = 64*H2  = 63.988728     (mu_2 = 1 threshold, the banked "q_crit ~ 2^64")
theta_1 = 128*H2 = 127.977457    (mu_1 = 1 threshold; theta_1 = 2*theta_2 EXACTLY)

log2 mu_1 :  q=2^41  +1.494261e+12 |  q=2^128 -3.872863e+08
             q=2^167 -6.704022e+11 |  q=2^256 -2.199411e+12
```

**Every admissible official row has `q > 2^128 > 2^theta_1`, so `mu_1 < 1` at every one of them.** At `q = 2^167` the first moment predicts `E[T] = 2^{-6.704022e11}`, while the **proved unconditional floor** is `B_ca^far(a) ≥ r+1 = 2^39.9773` (`crossing_location:635-637`). **The first moment is wrong by `6.704022e11` bits.** This is the sharpest available statement of "the random model has zero power in this lane" — sharper than the banked `q^{-Theta(m^2)}` remark (`crossing_location:3047`), because here the exhibit is unconditional and the error is quantified.

**And LB1-C *is* that subcriticality condition.** Exactly:

```
margin(mu_1 < 1)  -  margin(LB1-C)  =  log2 q + n(1 - H2(r/n))
   q=2^167 : 670,402,184,436.79 - 670,014,898,009 = 387,286,427.79  = predicted
   q=2^168 : 687,582,053,620.79 - 687,194,767,192 = 387,286,428.79  = predicted
```

i.e. `n < (a−k−1) log2 q` and `n·H2(r/n) < (a−k) log2 q` differ by `0.058%` of their margin. **LB1 lives precisely in the regime where the first moment forbids it.** That is not a coincidence — LB1's own column-farness needs `C(n,r)/q^{rho+1} < 1`, the same inequality shifted by one — and it is the reason no first-moment argument will ever price the far-CA residual.

---

## D3 — R-FG vs R-KER STRUCTURE, AND q_crit

### D3.1 They nest; they do not exchange; and the priority is inverted

R-KER as banked (`crossing_location:1004-1006`): "the `≥ r+1−2rho ~ 2^40`-dim common kernel with no `D`-split member; count slopes where a `≤ 2^34`-dim increment acquires one."

The exact dictionary, unconditional at every generic-rank slope:

```
dim ker M(gamma) = r+1-rho        (rank M(gamma) = rho)
dim K_0          = r+1-h_r        (h_r = stacked rank, rho <= h_r <= 2rho)
increment dim    = h_r - rho      in [0, rho]
V_r := F[x]_{<=r}/K_0             dim h_r <= 2rho = 2^35
```

- **R-KER** = count slopes at which the image of `D_r(D)` in the `h_r`-dimensional quotient `V_r` meets the `(h_r−rho)`-dimensional subspace `U_gamma`.
- **R-FG** = the same count, restricted to the sub-stratum where `V_r` carries a **ring** structure (`V_r ≅ Lambda = F[x]/(P*)`, `h_r = p = deg P*`) and `U_gamma` is a **cyclic** submodule `C_gamma^{-1}Lambda_{<m_Q}` (FG5, verified 83/83).

**They NEST: R-FG ⊂ R-KER. Closing R-KER closes R-FG; closing R-FG leaves R-KER open. They do not exchange.** Registered at 0.30 (nesting) — HIT.

**The `h_r` dictionary orders the strata, and the extremal count sits at the SMALL end — the surprise of the round.**

| stratum | `h_r` | increment | `dim K_0` | `p*` | structural `T` floor |
|---|---|---|---|---|---|
| **LB1** | `rho+1` (min nonzero) | **1** | `r−rho` | `floor(R/2)+1` | **`T_1 = r+1` exactly, 9/9 rows** |
| FG (witness B) | `2rho` (max) | `rho` | `r+1−2rho` | `2rho` | **none, 9/9 rows (`T_1 = 2` or `3`)** |
| generic | `2rho` | `rho` | `r+1−2rho` | `ceil(2R/3)` | not measured (ZP-4) |

Measured at 5 rate-half shapes (`R = 10..14`, `rho ∈ {2,3}`) and, for the `T` census, six fields spanning `mu_1 ∈ [2.9e-5, 238]`:

| `q` | `mu_1` | FG `T/q` | LB1 `T/q` | LB1 `T_1` | `r+1` | envelope `1−e^{−mu_1}` |
|---|---|---|---|---|---|---|
| 23 | 238.13 | 0.9565 | 1.0000 | — (col-close row) | 9 | 1.000000 |
| 101 | 12.349 | 0.9901 | 1.0000 | 9 | 9 | 0.999996 |
| 349 | 1.0342 | 0.5989 | 0.6447 | 9 | 9 | 0.644499 |
| 1009 | 0.12373 | 0.1100 | 0.1080 | 9 | 9 | 0.116384 |
| 10007 | 0.0012579 | 0.001299 | 0.001999 | 9 | 9 | 0.001257 |
| 65537 | 2.9329e-05 | **0.000061 (`T=4`)** | 0.000153 (`T=10`) | 9 | 9 | 0.000029 |
| 101 (H2) | 48.762 | 0.9901 | 1.0000 | 10 | 10 | 1.000000 |
| 65537 (H2) | 0.00011581 | **0.000015 (`T=1`)** | 0.000366 (`T=24`) | 10 | 10 | 0.000116 |

**`T(FG)` falls below `r+1` as soon as `mu_1 << 1`; `T_1(LB1)` never does.** At `n=22, q=65537` FG has `T = 1` against `r+1 = 10`. Since every admissible official row is deeply subcritical (`log2 mu_1 ≤ −3.87e8` at `q=2^128`), **the FG stratum is not where `B_ca^far`'s extremal count can live** — unless it beats its own first moment the way LB1 does, and nothing in FG's structure supplies the mechanism that does so for LB1 (a fixed `(r+1)`-point set `T` and `r+1` locators `T\{t\}`).

**Consequence for the board: closing R-FG would not move `B_ca^far`.** The load-bearing case is small `h_r`.

### D3.2 `p*(LB1)`, exactly

Derivation (confirmed 5/5 rate-half, 3/3 `k=1`): with `T ⊂ D`, `|T| = r+1`, `tau_T = prod_{t∈T}(x−t)`, `E = prod_{y ∈ D\T}(x−y)` of degree `a−1`, and `w_x/v_x = E(x)` on `T`,

```
Ann(V)_i = { sigma : deg sigma <= i, sigma = E g (mod tau_T), deg g <= i-rho-1 }
p*(LB1)  = min over nonzero (g,sigma) of max(deg sigma, deg g + rho + 1)
         = max( rho+1 , floor((R+2)/2) )      [shifted minimal indices sum to R+2]
d*(LB1)  = min(a-1, that index)
```

| `R` | 10 | 11 | 12 | 13 | 14 | 16 (`k=1`) | 18 (`k=1`) | 22 (`k=1`) |
|---|---|---|---|---|---|---|---|---|
| predicted `p*` | 6 | 6 | 7 | 7 | 8 | 4 | 4 | 4 |
| **measured `p*`** | **6** | **6** | **7** | **7** | **8** | **4** | **4** | **4** |
| `floor(R/2)` | 5 | 5 | 6 | 6 | 7 | 8 | 9 | 11 |
| `p* − floor(R/2)` | **1** | **1** | **1** | **1** | **1** | — | — | — |
| `d*` measured | 6 | 6 | 7 | 7 | 8 | 3 | 3 | 3 |
| `h_r` measured (`= rho+1`) | 3 | 3 | 3 | 4 | 4 | 4 | 4 | 4 |
| `dim K_0` measured (`= r−rho`) | 6 | 7 | 8 | 7 | 8 | 10 | 12 | 16 |

**At razor shape:** `p*(LB1) = R/2 + 1 = 549,755,813,889 = 16·(2rho) + 1` — one integer above `floor(R/2) = 549,755,813,888`, the top of the intermediate band, and `16 + 2^{-35}` times FG's `2rho`. So the extremal far-CA object is outside FG, outside the intermediate stratum `(2rho, R/2]`, and **just barely** outside it. The intermediate band did not carry load as a stratum (R0-c registered 0.20) but its **top edge is the sharp coordinate for LB1**, which I did not anticipate.

### D3.3 SECONDARY — q_crit on the official candidate row

The official candidate row (`tools/prize_row_descriptor.py:16-18,65-84,120`: `q < 2^256`, `k ≤ 2^40`, `n = 2^{subgroup_log2}`, rate `1/2`, `B*(q) = floor(q/2^128)`; `background/nodes/rate_half_ca_hankel_split_pencil_equivalence/statement.md:44-46`: "at the first unresolved official rate-half candidate, `R = k = 2^40` and `r = B*(q)−1 ≤ R/2`"; `crossing_location:62-64`: residual budget interval `[2^167, 2^167+2^129)`, budgets `{2^39, 2^39+1}`).

**One exact evaluation, at `q = 2^167`** (`e3_results.txt`):

```
(A) razor-shape thresholds applied at the official row's q:
      theta_2 = 63.988728    log2 q = 167   q > q_crit^(2) : YES, margin 103.011272 bits
                => log2 mu_2 = -3.539440e+12  <<1   the column-far random model is NOT void
      theta_1 = 127.977457                   q > q_crit^(1) : YES, margin  39.022543 bits
                => log2 mu_1 = -6.704022e+11 <<1   the KEY EQUATION is subcritical too

(B) the official row's OWN shape (r = B*-1 = 549,755,813,887, rho = 549,755,813,889,
    a = n-r = 1,649,267,441,665 = 3n/4 + 1):
      H2(r/n) = 0.811278124 ;  theta_2^own = 1.622556 ;  theta_1^own = 3.245112
      log2 mu_1^own at q=2^167 = -9.002520e+13 ;  log2 mu_2^own = -1.818344e+14

(C) two-row sanity, top of the interval and the widened top q < 2^256:
      log2 q = 167 : razor-shape mu_2 = 2^-3.539440e+12 ; own-shape mu_2 = 2^-1.818344e+14
      log2 q = 255 : razor-shape mu_2 = 2^-6.563097e+12 ; own-shape mu_2 = 2^-2.785914e+14
```

**q_crit PASSES**, by `≥ 64.0113` bits on the razor-shape threshold and `≥ 126.3774` bits on the row's own threshold, at every admissible official row. R0-d HIT.

**Precision catch (CATCH-24C class), flagged to the coordinator.** `q_crit ~ 2^64` is a **razor-shape constant**: `theta_2 = n·H2(r/n)/(2rho)` and at `r/n = 63/128, n/(2rho) = 64` it equals `64·H2(63/128)`. At the official candidate row's **own** shape (`r/n ≈ 1/4`) the same formula gives `theta_2^own = 1.6226`. The banked sentence "`q_crit ~ 2^64`: below it the column-far locus is measure-zero and every random model in this lane is void" (`crossing_location:3084`) is correct **only if read at the razor row `a = k+2^34`**; it must not be read as a row-level constant.

---

## D4 — VERDICT AND RESIDUALS

### D4.1 Verdict

**R-FG-RAZOR: walled with a named gap, and downgraded in priority.** Not resolved as a bound in either direction. What *is* resolved:

- **The brief's D2 dichotomy does not apply.** The type-2 spend/list ledger is vacuous by sign on the whole open bracket `[k+2^34, 3n/4)`. FG neither stays inside it nor dies on it (D2.2).
- **No banked cap is broken by an FG configuration at razor shape.** The nearest, `(C3) T_1 ≤ e+1`, is attained at 0 bits — by LB1, not FG. `CAP` is slack by its whole `2^45.9996`. `B*(q)` is exceeded only by LB1, by `0.977280` bits (banked).
- **FG is not the extremal stratum.** No structural `T`-floor at 9/9 rate-half ledger rows across six fields spanning `mu_1 ∈ [2.9e-5, 238]`; LB1 has one, exactly `r+1`, at 9/9.
- **The gap, named:** *does any FG pencil at razor shape beat its own first moment?* LB1 does, by `6.704022e11` bits. Nothing in FG's structure supplies the mechanism, and nothing here rules it out. That is the whole of R-FG-RAZOR now.

`B_ca^far(k+2^34) < 2^128`: **NO.**

### D4.2 The far-CA residual set after this round — RESTRUCTURED

Not `{R-KER}` alone, not `{R-FG, R-KER}` as banked (`crossing_location:3335-3338`), but **one `h_r`-indexed family with the priority inverted**:

- **R-HRLOW (new, and now the load-bearing one).** Bound `T` for column-far razor pencils with `h_r` near `rho` — increment dimension `1..O(1)`. **LB1 is the `h_r = rho+1` extremal**, `p* = R/2+1`, `dim K_0 = r−rho`, `T_1 = r+1`, and it **saturates `(C3)`**. Any upper bound in this lane must clear `T = r+1` at `h_r = rho+1` or explain why that configuration is excluded.
- **R-KER (unchanged in statement, sharpened in coordinates).** `rho ≤ h_r ≤ 2rho`; count slopes where the `(h_r−rho)`-dimensional increment over `K_0` acquires a `D_r(D)` member; the count factors through the `h_r`-dimensional quotient `V_r`. R-HRLOW and R-FG are its two ends.
- **R-FG-RAZOR (retained, DOWNGRADED).** The `h_r = p* = deg P*` sub-stratum where `V_r` is a ring and `U_gamma` cyclic. Nests inside R-KER; **closing it would not move `B_ca^far`** (D3.1). Recommend demoting it below R-HRLOW on the round-36 anchor list.
- **R-PSTAR-INTERMEDIATE (anchor 1's).** Did not carry load as a stratum, but its **top edge `floor(R/2)` is the sharp coordinate for LB1**, which sits exactly one integer above it at 5/5 shapes.
- **R-DEEP, R-LINEDEGREE** unchanged.

### D4.3 FLAGS FOR THE COORDINATOR (AUDIT-AND-DRAFT — no surgery applied)

1. **`critical/nodes/rate_half_band_crossing_location:3084` — narrow the `q_crit` sentence to the razor row.** `theta = n·H2(r/n)/(2rho)` is shape-dependent; at the official candidate row's own shape it is `1.6226`, not `~64`. Suggested repair: "`q_crit ~ 2^64` **at the razor row `a = k+2^34`**". Also additive and free: `theta_1 = 2·theta_2 = 127.977457` is the *key-equation* threshold, and every admissible official row (`q > 2^128`) is subcritical for **both**. **I flag; I do not apply.**
2. **`crossing_location:3080-3081` — "LB1 is GENERIC (`p* = r+1 = ceil(2R/3)`, 3591/3591)" is a statement about LB1's own small `k=2` cell and does not transfer to razor shape.** At razor-faithful shape `p*(LB1) = floor(R/2)+1` (5/5 shapes, `R=10..14`), `h_r = rho+1`, `dim K_0 = r−rho`. At the razor: `p* = 2^39+1`, one integer above the intermediate band's top. Suggested repair: scope the banked sentence to LB1's cell and add the razor-shape law.
3. **Anchor 1's D1.2 table labels the row `h_r = p*` as "FG". It is not.** Round-33 FG needs `K_0 = P·F[x]_{≤ r−p}` with `p = deg P`; `h_r = p*` only gives `K_0 = P·F[x]_{≤ r−p*}` with `deg P = d* ≤ p*`. Three exhibited counterexamples, three fields (`e4_results.txt`). If the FG bracket is ever used as a *criterion* rather than a definition, this bites.
4. **Nothing in the repository connects the type-2 ledger to far-CA or razor shape** (grep 9, zero hits) — and now there is a reason: `(C2)`'s floor is vacuous by sign on the whole open bracket. Worth banking as a scope fence, so no future round spends effort importing `(C2)`/`(C3)`/`(C4)`/`X_gamma`/layer-A into the bracket interior.
5. **Recommend re-ordering the round-36 anchors:** R-FG-RAZOR (currently anchor 4, `crossing_location:3396`) should sit below a new R-HRLOW. The evidence is D3.1's table.

### D4.4 Cross-pilot flag (I did NOT read any sibling)

For whoever holds the realizability / layer-A lanes: **`(C2)`, `(C3)`, `(C4)` and every instrument built on them are scoped to `r ≤ R/2 ⟺ a ≥ 3n/4`** (`crossing_location:982`), which is the *top* of the far-CA open bracket, not its interior. `(C3)` is **attained at 0 bits** by LB1 at `a = k+2^34` with `e = d_x = r`, so no `T_1` bound below `e+1` can be true there. Any transport of a W-layer or layer-A object into `[k+2^34, 3n/4)` is vacuous by sign before it is vacuous by counting.

---

## PREDICTIONS vs OUTCOMES

| | registered | outcome |
|---|---|---|
| R0-a | P(FG breaks a banked cap → contradiction) = 0.12; P(walled with named gap) = 0.55; P(clean negative) = 0.33 | **HIT — the 0.55 branch.** No cap broken; the question is malformed (ledger vacuous) |
| R0-b | reduces 0.25 / independent 0.20 / exchange 0.25 / **nest 0.30** | **HIT — they nest**, R-KER ⟹ R-FG, not conversely |
| R0-b1 | constraint count `= rho` independent of `p`, P = 0.80 | **HIT, but for a trivial reason** (it is the corank). The non-trivial fact is the factoring through the `h_r`-dim quotient. Partial hit, disclosed |
| R0-c | intermediate stratum carries load, P = 0.20 | **HIT as registered** — it carries no load as a stratum; **but its top edge is the sharp `p*(LB1)` coordinate**, 5/5, which I did not anticipate |
| R0-d | q_crit "passes" (`q > 2^63.9887`), P = 0.72; `≥128`-bit field 0.55; exactly `2^128` 0.40; `q<2^64` 0.28 | **PASSES by 103.011272 bits.** `≥128`-bit **HIT** (`q ∈ [2^167, 2^167+2^129)`); "exactly `2^128`" **MISS**; `q<2^64` correctly priced low |
| R0-d′ | banked coverage threshold within a factor 2 of `2^127.977457`, P = 0.50 | **HIT numerically (0.0225 bits) — but numerological.** The two 128s are `n/rho` and `EPSILON_BITS`. Reported as miss 5, not as structure |
| R0-e | E1–E22 exact | **22/22 EXACT** (`e3_results.txt`) |
| R0-e | F1–F7 within tolerance | **7/7.** Largest deviation F2: registered `2.198635975e12`, true `2.198635969291e12`, `|diff| = 5,709` vs tolerance `2e6` |
| R0-e | P(banked "(R+1)-a floor" uses `a = k+rho`) = 0.45 | **MISS — the 0.55 alternative fired.** `(C2)`'s `a` is `\|W\|` (miss 3) |
| D-1 | `dim = (r+1)+m_Q−p` at ≥ 90% of slopes, P = 0.85 | **HIT, stronger: 100% of slopes at 5/5 cells, 5 fields** |
| D-2 | `codim U_gamma = rho`, P = 0.85 | **HIT — 5/5 cells, every slope** |
| D-3 | R-FG and R-KER nest, neither reduces the other, P = 0.55 | **HIT** |
| D-4 | Poisson envelope `T/q ≤ 1−e^{−mu_1}+0.10`, P = 0.75 | **HIT — 20/20 measured (q, family) rows** |
| D-4 | `T/q` monotone in `mu_1` across cells, P = 0.70 | **MISS — 2 inversions** (FG: 0.9565 at `mu_1=238` vs 0.9901 at `mu_1=12.3`; and `T=0` at `mu_1=0.565` between `T=4` at 0.484 and `T=4` at 0.728) |
| D-5 | `theta_1 = 2·theta_2` identically, P = 0.95 | **HIT — exact** |
| D-6 | witness-B faithfulness, all six properties, ≥ 2 fields, P = 0.85 | **HIT — 10/10 cells, `rho ∈ {2,3}`, ten fields.** Caveat: the *LB1* row at `q=23` is column-close (miss 10) |
| misc | P(find a banked statement needing correction) = 0.80 | **HIT — three (flags 1–3)** |
| misc | P(anchor-1 flags 1–4 still unrepaired) = 0.70 | **MISS — they were banked inline** at `crossing_location:3066-3085` |
| misc | P(`B_ca^far < 2^128` moves) = 0.05 | **HIT — it did not** |
| misc | residual set: still `{R-FG,R-KER}` 0.55 / `{R-KER}` 0.10 / **restructured 0.35** | **The 0.35 branch fired** |
| misc | P(≥1 of E1–E22 wrong) = 0.10; P(≥1 of F1–F7 out of tolerance) = 0.15 | **Both HIT — none wrong, none out** |
| MISS-2 guard | max-not-mean; no emptiness from a census; codim ≠ emptiness; first moment has zero power both ways | **HELD** — every `T` used against a cap is an exact count or a max; means labelled as descriptors only; and I exhibit the first moment being wrong by `6.7e11` bits rather than trusting it |

---

## ZERO-POWER DECLARATIONS

1. **ZP-1 (pre-registered, with a disclosed widening).** No razor-scale computation exists here. All machine numbers at `q ≤ 65537`, `R ≤ 14`, `rho ≤ 3`, `r ≤ 19`. I registered `q ≤ 31` and went to `65537`; the widening is disclosed and was necessary because the subcritical regime `mu_1 < 1` is unreachable at `q ≤ 31`.
2. **ZP-2 (pre-registered, and it bit twice).** Cells without `4rho < R` cannot separate FG from the intermediate stratum. **Added this round:** cells without `a > R+1` and `a−1 > r` cannot see `p*(LB1)` correctly, and my own `k=1` cells failed exactly there (miss 1). I claim **zero power** from any `k=1` row for any `p*(LB1)` statement.
3. **ZP-3 (pre-registered).** The first-moment model has **zero power at the razor, in both directions.** `mu_1 = 2^{-6.70e11}` at `q=2^167` coexists with a proved floor of `2^39.977`. Every `E[T]` in this report is labelled heuristic and supports no verdict. In particular I do **not** conclude that FG has few bad slopes at the razor — only that FG exhibits no *structural* floor at any cell I can reach, in contrast to LB1 which does.
4. **ZP-4 (pre-registered).** I did not measure the density of FG among column-far pencils. FG is reached by construction only.
5. **ZP-5 (pre-registered).** `q_crit` is a first-moment threshold, not a proved phase transition. Zero power beyond the single official row evaluated; no claim about the behaviour of the true count near the threshold, nor about other rates.
6. **ZP-6 (pre-registered).** Every statement about the type-2 ledger is limited to `apolar_origin/PREREG.md:181-192` and the SAT-lane symbol table at `rh_sat3_realizability/REPORT.md:265`. I claim **zero power over ledger variants I did not read**, and `X_gamma` in the `(OUT-m)` sense (`crossing_location:3210-3231`) is an `m`-parameterised near-lane object I located but did not transport.
7. **ZP-7 (pre-registered).** No claim about `char F_q`, about non-squarefree `P*` inside FG3/FG4 (witness A is kept out of the key-equation analysis), or about canonicity of `P*` in general — though `dim Ann(V)_{p*} = 1` was measured at 10/10 FG cells and at 8/10 LB1 cells (`= 2` at `R = 12, 14`).
8. **ZP-8 (pre-registered).** Ten fields, five shapes; every structural claim is confirmed at ≥ 2 fields **and** ≥ 2 shapes. Single-field claims: none.
9. **New — `w*` is an upper bound.** The ledger retains at most `LOCCAP = 24` locators per slope, so every reported `w*` is `≥` the true `w*` and every reported floor `(R+1)−w*` is `≤` the true floor. The direction is against my own conclusion of vacuity at the FG cell where `(R+1)−w* = 0`, so that cell's vacuity is a *lower* bound on vacuity, not an artefact.
10. **New — `rho = 3` at rate half is structure-only.** No `T` census exists there (miss 8). The `rho = 3` bad-slope numbers come from `k=1` cells, which are non-faithful.

---

## MEASURED FUNCTIONALS

Registered and measured: `p*`; `d* = min{deg P : 0 ≠ P ∈ Ann(V)_{p*}}`; `dim Ann(V)_{p*}`; `h_r` (stacked rank); `dim K_0`; `deg gcd(K_0)`; the two principality tests `K_0 == P·F[x]_{≤r−p*}` and `K_0 == P·F[x]_{≤r−deg P}`; FG membership; column-farness (`K_0 ∩ D_r(D)`, exhaustive); `rank M(gamma)` and `dim ker M(gamma)` at every slope; `codim U_gamma` in `Lambda`; the FG5 shift-family property (searched over the whole space); `T` (exact bad-slope count, all slopes, via `A·sigma + gamma·B·sigma = 0`); per-slope list sizes (min/median/max/sum); `mu_1`, `mu_2`, `1−e^{−mu_1}`; `w*`, `(R+1)−w*`, `T_1`, `T_2`, per-slope spends `|S_gamma \ W|`, `d_x`, `e = max d_x`, `CAP(w*)`; the razor integers E1–E22 and reals F1–F7; `theta_1`, `theta_2`; the LB1-C margin and the `mu_1` margin and their exact difference; `B*(q)` vs `r+1` at four `q`.

Registered but **not** measured: nothing. Two functionals were declared *in advance* as unreachable and are reported as such — the `rho = 3` rate-half `T` census (ZP-10) and any razor-scale quantity (ZP-1).

---

## COMPLIANCE

`CONSTRAINTS.md` read first, `PREREG.md` second, then the **two named anchors only** (`notes/pilots_20260811/r34_pstar/REPORT.md`, `notes/pilots_20260811/rh_moving_kernel/REPORT.md`), and **nothing else** — no grep, no `ls` outside my own directory, no interpreter invocation — before the `## Pilot registrations` block (R0-a..e, D-1..D-6, the MISS-2 guard, eight zero-power declarations, the compute plan and the miscellaneous priors) was appended to `PREREG.md` with the **Edit tool**. **No registration was edited afterwards.** The block discloses honestly that the razor integers, the DOF count and the two entropy exponents were computed in-head from the anchors before writing, and marks D-4's Poisson envelope **semi-blind** because it is calibrated against anchor 1's four published `T` rows.

**COMPUTE LAW: 6 interpreter invocations, 6 under `tools/ramguard`, ZERO breaches, zero bare `python3` for any purpose.** From the repo root, with a literal `--` and an explicit `RAMGUARD_TIMEOUT`: (1) `e1_replica.py` *local*, `RAMGUARD_TIMEOUT=290`; (2) `e2_budget.py` *local*, 290 — the `O(T^2·L^2)` ledger, killed, completed with exit 0, **wrote no results file** (miss 9); (3) `e3_razor.py` *tiny*, `RAMGUARD_TIMEOUT=55`; (4) `e2a_budget.py` *local*, 290; (5) `e2b_shape2.py` *local*, 290; (6) `e4_classify.py` *local*, 290. This is exactly the ≤ 6 I registered. Stdlib only (`sys`, `itertools`, `math`). **All file edits went through the Edit/Write tools**; no `sed -i`, no `awk -i`, no `perl -i`, no `tee`, no shell redirection onto an existing file; the one redirection I used (`> notes/.../e2a_stdout.log`) created a **new** file that did not previously exist, and every `*_results.txt` is written by its own script. No interpreter was used to patch, probe or no-op. No Modal, no network, no git, no subagents.

**RAM DISCIPLINE:** file-at-a-time; **`dag.json` never opened**; `critical/nodes/rate_half_band_crossing_location/statement.md` (3,398 lines) read only through six bounded windows (68, 60, 55, 45, 40, 40 lines) plus line-numbered greps; `apolar_origin/PREREG.md` through one 19-line window; `tools/prize_row_descriptor.py` through a 120-line prefix; the locator enumeration is a streaming `combinations` loop with `O(1)` retained state per configuration (integer coefficients computed once per subset and reduced per field, so `C(22,9) = 497,420` never materialises); results checkpointed to `e1_results.txt`, `e2a_results.txt`, `e2b_results.txt`, `e3_results.txt`, `e4_results.txt` after every emit; no run approached the memory ceiling.

**QUARANTINE:** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` never opened at any line. **No `r35_*` sibling directory was read or opened.** One disclosed deviation, deliberately chosen to make the exclude list *certifiable* rather than guessed (round 34's gap): I ran `find notes/pilots_20260811 -maxdepth 1 -mindepth 1 -type d -printf '%f\n'` to obtain sibling directory **names only** — no file inside any sibling was listed, opened or read — and then excluded `r35_bivcurve_m4`, `r35_l2_gate`, `r35_rout_layer_a` (plus `prize-codex-work` and `pilots_20260802`) at **search level** on every recursive grep. The `r34_*` and `rh_*` directories are readable under CONSTRAINTS and I read exactly two of them (the named anchors) plus, for the `(C2)`/`(C3)`/`(C4)` definitions and the SAT symbol table, `notes/pilots_20260810/apolar_origin/PREREG.md` and grep output from `notes/pilots_20260810/rh_type2_stratum/REPORT.md` and `notes/pilots_20260811/rh_sat3_realizability/REPORT.md` — all earlier-or-permitted dirs. No path containing `prize-codex-` was touched.

**WRITE SCOPE:** every write is inside `notes/pilots_20260811/r35_fg_razor/` — `PREREG.md` (registrations appended), `e1_replica.py`, `e1_results.txt`, `e2_budget.py` (superseded, produced nothing), `e2a_budget.py`, `e2a_results.txt`, `e2a_stdout.log`, `e2b_shape2.py`, `e2b_results.txt`, `e3_razor.py`, `e3_results.txt`, `e4_classify.py`, `e4_results.txt`. **No `dag/`, `critical/`, `background/`, `nodes/` or `tools/` file was edited**; no git operation of any kind; no scratch file outside the pilot directory; **no banked script was copied or run** — all five experiment scripts are fresh implementations against the conventions in `rate_half_ca_hankel_split_pencil_equivalence/statement.md:7-33` (`v_x = 1/prod_{y≠x}(x−y)`, `y_m = sum_x e(x) v_x x^m`, `M_r(y) = (y_{i+j})`, low-to-high coefficient order, `(HS2)`/`(HS3)` column-farness), cross-checked against round 33's and round 34's published numbers where the cells overlap and against the banked LB1-C constant `670,014,898,009` (exact match). AUDIT-AND-DRAFT respected: **no node surgery applied**; the five corrections this round forces are flagged in D4.3 for the coordinator, not made.
