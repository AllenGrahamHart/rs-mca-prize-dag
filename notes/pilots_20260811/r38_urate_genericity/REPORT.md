All runs complete. Full report follows.

---

# REPORT — r38_urate_genericity (round 38)

## VERDICT

**R-GENERICITY'S RANK HALF IS PROVED. R-URATE IS REFUTED. The far-CA count moves a third time — but not at the razor.**

Three results, each with a proof and a machine confirmation at two or more fields:

1. **D1 IS DONE.** The engineering matrix is not a generic Vandermonde glue — it **decouples completely into a line-pencil concurrency problem**. Row `(i,x)` says the point `p_x := (e_0(x),e_1(x)) in F^2` lies on the line `X + gamma_i Y + lambda_i Z_{Y_i}(x) = 0`. Two lines with distinct `gamma` always meet, so a point of `W` covered `d(x)` times costs exactly `max(d(x)-2,0)` conditions **on `lambda` alone**. This yields an EXACT rank formula, `rank(M) = j(rho+1) - L + rank(Phi)` with `L = sum_x max(d(x)-2,0)` and `Phi` the explicit concurrency matrix — **confirmed with ZERO violations in ~500 designs across 16 (cell,field) rows, 8 cells, 2 domain types** (`g1_results.txt:17,33,50,67,85,103,118,133,148,163,180,197,211,225,240,255`, every row `R2b-1: N confirmed / 0 violated`). Its clean corollary — *every point of `W` in at most two `A_i` + distinct `gamma_i` => FULL RANK `j(rho+1)`, `lambda` completely free* — is D1's requested Vandermonde/exchange condition, and it is unconditional.

2. **TWO OF THE FOUR SIDE-CONDITIONS ARE NOW PROVED, NOT "60/60".** At the razor `j = 126` is *exactly* the one-common-point exact-double-cover design (`126 rho = 2r` on the nose), the kernel is exactly 2-dimensional, and `lambda_i = -(u+gamma_i v)/Z_{Y_i}(x^*)` in closed form. Hence **`lambda_i != 0` fails on EXACTLY `j` of the `q+1` projective kernel points** — a finite count, no genericity. **Measured EXACT at 4/4 rows** (`g3_results.txt:6,11,16,21`, every row `R2e VERDICT: EXACT HIT`). `gamma_i` off the fibre is proved by a union bound (`det M_x = c_a c_b (gamma_a-gamma_b)^2 != 0`), measured `48/63/80` bad points against the proved bound `j(r+1) = 72/90/110` (`g3:5,10,15,20`).

3. **R-URATE IS FALSE, AND I BROKE IT MYSELF.** The banked cap `T <= r+1 + (2(r+1)-1)/rho` is refuted at `C3 = (n=26,k=13,r=10,rho=3)` on the razor's own domain type: a **rank drop** in `Phi` (two points of `W` shared by all `j` sets with `Z_{P_i}` proportional there) buys `j = 9 > cap = 7`, and the **FULL `C(26,10) = 5,311,735` census returns `T = 19 > 18 = (r+1)+cap`, column-far, `T_fib = 10`, `T_eng = 9/9`, `T_other = 0`, at THREE fields** (`g4_results.txt:51-52`; `g5_results.txt:4-6,9-11`). The banked full-census value `T = 17` at exactly this cell and field (`crossing_location:4717-4718`) is **not the maximum**: I get 18 at `j = 7` (`g2_results.txt:41`) and 19 at `j = 9`.

```
B_ca^far(k+2^34) >= r+1 + 126 = 1,082,331,758,719      (construction; rank half + 2 of 4
                                                        side-conditions now PROVED)
cap: T <= r+1 + max_m [ -(m-1) + floor((2(r+1-m)+1)/(rho+1-m)) ]
     = r+1 + 126 at the razor (max at m=1)  -- but ONLY within a named normal form,
     and the m=1 form is exactly what the C3 counterexample escapes at small rho.
```

**At the razor the arithmetic saves the cap and I can say why:** the trade-off is *one fibre slope lost per unit of rank deficiency, `1/rho` slopes gained*, so deficiency is catastrophic when `rho = 2^34` and free when `rho = 3`. `T_max(m)-(r+1)` = `125, 126, 125, 124, 123, 117, -873, ...` at `m = 0,1,2,3,4,10,1000` (`g4_results.txt:14-19`). The break-even `m* = 17,178,409,629` sits a factor `17.17` above the pigeonhole ceiling `m_pig = 1,000,446,576` (`g4:10-12`). **That margin is the only thing holding the razor cap up, and it is a margin against pigeonhole, not against algebra (ZP-13, registered before any run).**

4. **R-USYM CLOSES.** `sigma^e` and `sigma^o` fuse the parity blocks iff they are linearly dependent iff `sigma = (X-x_0)p(X^2)` (odd degree) or `sigma = q(X^2)` (even degree); at ODD `r` the second is impossible by degree parity, so **the carrier family is EXHAUSTIVE**. Measured: `prop-but-NOT-carrier = 0` and `carrier-but-NOT-prop = 0`, sweeping 31,824 and 497,420 split locators, 2 shapes, 2 fields (`g3_results.txt:63-64,69-70,75-76`). Counts match the closed form `C(n/2,(r-1)/2)(n-r+1)` exactly: `1008 = 84*12`, `4620 = 330*14`.

`B_ca^far(k+2^34) < 2^128`: **NO.** I add no upper bound. `log2(r+1+126) = 39.977280 = log2(r+1)` to six decimals (`g4:31`); `(r+1+126)/2^39 = 1.968750000 = 2^0.977280` (`g4:32`).

---

## MISSES FIRST

1. **MY HEADLINE REFINEMENT WAS WRONG, AND MY OWN RUNS KILLED IT ON THE FIRST INVOCATION.** I registered (A-5, B-6, B-7, B-8) that the true maximum `j` is `floor(2r/rho)` — my exact-double-cover constraint — and NOT the anchor's `floor((2(r+1)-1)/rho)`, naming C3 and C11 as discriminators at P = 0.70/0.70/0.65. **REFUTED at both.** C3 reaches `j = 7` (my prediction: 6) at both `intZ` and `mu_26` (`g1_results.txt:117,132`); C11 reaches `j = 9` (my prediction: 8) at both (`g1:180,197`). My in-head derivation of the `m=1` constraint was `j rho <= 2r`; the correct constraint is `j rho <= 2r+1`, because one point outside `x^*` may carry multiplicity 3 and still leave `dim ker Phi >= 1`. **I registered a sharper cap than the anchor's and the machine handed it straight back.**

2. **CONSEQUENCE OF MISS 1: I RESOLVED THE ANCHOR'S MISS 3 AGAINST MY OWN PREDICTION.** The anchor could not say whether `j = 7` at C3 was cap-limited or search-limited and honestly said so (`r37_urand/REPORT.md:41`). It is **search-limited**: `j = 7` is reachable, at both domain types, and the resulting full census gives `T = 18` (`g2_results.txt:41`), not the banked 17.

3. **B-2 (additivity, P = 0.55) IS REFUTED, BY MY OWN CONSTRUCTION, AND IT IS THE ROUND'S HEADLINE.** I priced additivity at a coin-flip and hedged that it "holds within a normal form". It does not hold: rank drops are real, constructible, and they break the cap at C3 by 1 over three fields. I found the mechanism while writing the registrations (R2j) and priced the *consequence* (B-5) at only 0.20.

4. **B-11 (`m >= 2` designs FAIL at small cells, P = 0.75) IS HALF-REFUTED, AND THE REFUTED HALF IS THE ONE THAT MATTERED.** `m >= 3` fails exhaustively — over ALL `rho`-subsets, every projective class is a singleton at three cells (`g3_results.txt:26-27,33-34,40-41`, `LARGEST class = 1` six times). But `m = 2` **succeeds**: largest classes of size 8, 3, 15 (`g3:25,32,39`) and up to 40 at C9 (`g4:37`). I predicted the failure of the exact mechanism that then broke my own cap.

5. **THE `m >= 3` NEGATIVE HAS NO POWER AND I MUST SAY SO.** At C3 there are 455 `rho`-subsets and `q^2 ~ 4e10` classes, so "no collisions at `m = 3`" is what pure counting predicts. It is **not** evidence of an algebraic obstruction. The only *algebraic* obstruction I have is R2k (coset families force `m <= 2`), verified at 2 subgroup orders and every divisor (`g3_results.txt:49,58`). ZP-13 registered this in advance.

6. **THE CAP-BREAK IS ONE CELL.** Three fields (`q = 200201, 500111, 300301`), full census each, identical `T = 19` — but **one cell, one `rho`, one domain type**. C9 predicts the same break (`T_max(2) = 23 > T_max(1) = 22`, `g4_results.txt:36`) and I constructed the `j = 8` witness with the predicted single `chi` collision (`g4:38`), but `C(36,14) = 5.6e9` is out of reach, so **C9's break is UNCENSUSED**. Declared, not hidden.

7. **A-6 IS A SPLIT, AND THE SPLIT IS INSTRUCTIVE.** I registered `T = (r+1)+j` exactly. Measured: exact at 2/7 census rows (`g2:11` `T=17`; `g2:41` `T=18`) and `T = (r+1)+j+T_other` at the other five, with `T_other = 8,2,3,5,9` against nulls `q mu_1 = 0.63, 1.92, 2.49, 7.59, 9.81`. `T_other` is null-compatible background, not construction — but **my registered equality was an equality, and it is false as stated.** Only `T >= (r+1)+j` is used for any bound (MISS-2 clause 5).

8. **A-8 WAS NOT MEASURED.** I registered a prediction on the rank of the parity condition system (`ceil(rho/2)` on the carrier vs `rho` off it) and then tested the *classification* instead, which is the stronger and more decisive statement. The rank prediction is **unmeasured**, not confirmed. Registered-but-absent, declared here.

9. **TWO OF FOUR SIDE-CONDITIONS REMAIN OPEN, SO THE `+126` IS STILL NOT UNCONDITIONAL (B-3 MISS, correctly priced at 0.15).** `chi` injectivity survives for pairs in different block-pairs (union bound: `<= 2 (r+1)^2 ~ 1.2e24 << q+1 ~ 3.4e38`) but reduces, for pairs *inside* one block-pair, to injectivity of `Z_{P_b}/Z_{P_a}` — and multi-edges are FORCED (a `rho`-regular simple graph on 126 vertices needs `rho <= 125`, whereas `rho = 2^34`). Column-farness: Case `|S u W| <= R` is **proved** by MDS plus full support; Case `|S u W| >= R+1` is a first moment over `C(n,r)` supports and is declared ZERO POWER (ZP-4).

10. **NO RAZOR-SCALE MEASUREMENT, AS REGISTERED, AND NO WIDENING.** All machine numbers at `q <= 999983`, `R <= 18`, `rho <= 4`, `r <= 14`, exactly the envelope registered in ZP-1 before the first run.

11. **NO BOUND.** `B_ca^far(k+2^34) < 2^128` remains **NO** (B-15 registered at 0.02, HIT).

---

## CATCH-24A SUBTRACTIONS

Every recursive grep carried, at search level: `--exclude-dir=r38_side_door --exclude-dir=r38_cauchy_lattice --exclude-dir=r38_sporadic_det --exclude-dir=pilots_20260802 --exclude-dir=prize-codex-work --exclude-dir=.git --exclude-dir=__pycache__ --exclude=dag.json`. Sibling names taken from `CONSTRAINTS.md:36-38`, never from an `ls`. Hyphenated/infixed variants included.

| # | claim | grep | banked? | verdict |
|---|---|---|---|---|
| 1 | R-URATE, R-GENERICITY, the `j(rho+1) x (2(r+1)+j)` matrix, the four side-conditions, the `+126` | `-rniE "R-URATE\|R-GENERICITY"` | **YES** — `critical/nodes/rate_half_band_crossing_location/statement.md:4741-4746`; `r37_urand/REPORT.md` | **SUBTRACTED — the brief's own provenance.** Additive: the *answers* |
| 2 | the whole U-rand construction, `T = (r+1)+j`, the `rho` exchange rate, FENCE-1, minimal-spend rigidity, `chi_Y` | same | **YES** — `crossing_location:4697-4720` | **SUBTRACTED IN FULL — round 37's.** I import it and price its cap |
| 3 | **concurrency loci of a Vandermonde-type arrangement as the finite-field incidence reformulation** | `-rniE "concurren"` | **YES** — `background/nodes/f_concurrency_equiv/statement.md` (PROVED): "P cap D_j corresponds EXACTLY to points lying on >= j of the n evaluation hyperplanes" | **SUBTRACTED — the METHOD is banked in the F-lane.** Different object (there: hyperplanes `H_x = {P(x)=0}` in polynomial parameter space; here: lines in the `(e_0,e_1)`-plane indexed by *slopes*, one pencil per point of `W`). **ADDITIVE:** the far-CA instantiation, the exact rank formula `rank M = j(rho+1)-L+rank Phi`, and the `d(x)-2` cost |
| 4 | "pencil trade-off law" | `-rniE "trade-?off law"` | **YES** — `background/nodes/xr_band_key_lemma_pencil_mass/statement.md:113` ("no `poly(n)` pencil trade-off law is true", a proved *negative*) | **SUBTRACTED — the phrase and the xr object.** Different quantity (pencil mass minimum vs bad-slope count); my law is a *positive* exchange rate `1 fibre slope : 1/rho new slopes` |
| 5 | `Z_{cH}(X) = X^d - c^d` for a coset of a subgroup of `mu_n` | `-rniE "X\^(d\|rho\|m) *- *c\^\|coset vanishing"` | textbook; nearest banked uses are in the list/kb lanes (`rate_half_list_budget_three_split_pencil_normal_form`, `f2_ssparse_tower_extension`) | **SUBTRACTED as textbook.** **ADDITIVE:** the *consequence* — coset families force `m <= 2`, closing the natural razor-domain attack on the cap |
| 6 | "one support pays for at most one slope"; the minimum-distance spend; MDS `d = R+1` | round-37 greps #3/#4 | **YES** — `critical/nodes/counting_frame/statement.md:9`, `v8_ledger/statement.md:9`; `rate_half_type2_fr_two_type1_fibre_spend_calibration/statement.md:48` | **SUBTRACTED IN FULL — Paper D's and the FR lane's.** Used only as inputs |
| 7 | the carrier-exhaustiveness QUESTION at odd `r` | `-rniE "carrier[- ]exhaust"` | **YES, AS AN OPEN QUESTION** — `crossing_location:4734-4735` | **SUBTRACTED as the question. ADDITIVE: the ANSWER** (degree-parity completeness proof + excess-0 sweep) |
| 8 | **"rank deficiency in `Phi` costs a fibre slope"; the deficiency/collapse trade; `T_max(m)`; the pigeonhole ceiling `m_pig` and the `17.17x` margin** | `-rniE "fibre collapse\|rank deficiency.*(buy\|cost)\|deficiency.collapse"` | **ZERO HITS** outside my own directory | **ADDITIVE — the round's core law** |
| 9 | **`rank M = j(rho+1) - L + rank Phi`; the `lambda_i = -(u+gamma_i v)/Z_{Y_i}(x^*)` closed form; "exactly `j` bad projective kernel points"** | greps 1,3 | **ZERO HITS** | **ADDITIVE — R-GENERICITY's rank half + side-condition 1** |
| 10 | **a codeword-mediated configuration ABOVE the banked cap; `T = 19` at `mu_26`** | `-rniE "T *= *17\|5,?311,?735"` | banked value is `T = 17` (`crossing_location:4717-4718`) | **ADDITIVE — and it CORRECTS the banked census number** |

**Genuinely additive:** (a) the line-pencil decoupling and the exact rank formula; (b) the multiplicity-`<=2` sufficient condition (D1's requested clean criterion); (c) the razor `m=1` exact-double-cover design and its closed-form kernel; (d) the *proof* of side-conditions 1 and 3 and the reduction of 2 and 4; (e) the deficiency/collapse trade-off law and `T_max(m)`; (f) the refutation of R-URATE with a three-field exhaustive census; (g) the coset obstruction `m <= 2`; (h) the carrier-completeness theorem closing R-USYM.

---

## D1 — THE MATRIX, STRUCTURED

Order the unknowns `(e_0|_W, e_1|_W, lambda_1..lambda_j)`. The row for `(i, x in A_i)` is `[delta_x | gamma_i delta_x | 0..Z_{Y_i}(x)..0]`, so the system reads

> **`p_x := (e_0(x),e_1(x))` lies on the `d(x)` lines `L_{i,x} : X + gamma_i Y + lambda_i Z_{Y_i}(x) = 0`, `i in I(x)`, and blocks interact ONLY through `p_x`.**

`Z_{Y_i}(x) != 0` for every `x in W` because `Y_i n W = empty` (the nonvanishing pattern). Distinct `gamma_i` => no two lines are parallel.

**Theorem D1 (rank).** With `gamma_i` pairwise distinct and `Y_i n W = empty`, put `d(x) = |I(x)|`, `n_c = #{x : d(x)=c}`, `L = sum_x max(d(x)-2,0)`, and let `Phi` (`L x j`) collect the concurrency conditions — the row at `x` for the `s`-th excess line being `det[[1,gamma_a,lambda_a Z_a(x)],[1,gamma_b,lambda_b Z_b(x)],[1,gamma_s,lambda_s Z_s(x)]] = 0`, i.e. coefficients `Z_a(x)(gamma_s-gamma_b)`, `-Z_b(x)(gamma_s-gamma_a)`, `Z_s(x)(gamma_b-gamma_a)`, **all nonzero**. Then

```
rank(M)     = j(rho+1) - L + rank(Phi)
dim ker(M)  = (j - rank Phi) + 2 n_0 + n_1
FULL ROW RANK j(rho+1)  <=>  rank(Phi) = L   (requires L <= j)
```

**Machine: 0 violations of either identity in ~500 designs, 8 cells x 2 domain types x 3 design families** (`g1_results.txt:17,33,50,67,85,103,118,133,148,163,180,197,211,225,240,255`).

**Corollary D1' (the clean sufficient condition the brief asked for).** *If the `gamma_i` are pairwise distinct and **every point of `W` lies in at most two of the `A_i`**, then `L = 0`, `M` has full row rank `j(rho+1)`, `lambda` is **completely free**, and `dim ker M = 2(r+1) - j rho`.* Proof: the per-point left-null system is the `2 x d(x)` Vandermonde with nodes `gamma_i`, of rank `min(2,d(x))`; so `d(x) <= 2` forces the left-null coefficients to vanish. Explicit witness: `j` consecutive arcs of length `rho+1` around a cyclic order of `W`, wrapping at most twice; feasible iff `j(rho+1) <= 2(r+1)`, i.e. `j <= 125` at the razor (`g4:6`). **This is a Vandermonde/exchange argument and it is unconditional — R-GENERICITY's rank half.**

**The razor design (`m = 1`).** One point `x^*` in all `j` sets, every other point in exactly two. Then `j rho = 2(|W|-1) = 2r`, and **`126 rho = 2r` EXACTLY at the razor** (`g4:5`, `2r/rho = 126`, `exact int? True`). The concurrency at `x^*` solves in closed form: for any `(u,v) = p_{x^*}`,

```
lambda_i = -(u + gamma_i v)/Z_{Y_i}(x^*),     ker Phi = 2-dim,  rank Phi = j-2 = L,
=> M has FULL ROW RANK,   dim ker M = 2  exactly.
```

That is precisely the anchor's measured "kernel dimension exactly 2 at `j = 126`". The `A_i\{x^*}` form a `rho`-regular multigraph on `j` vertices with `63 rho` edges; two partitions of `W\{x^*}` into 63 blocks of size `rho` realise it. Machine: `dim ker = 2` at every exact-double-cover row (`g2_results.txt:4,10,16,22,28,34`).

---

## D2 — R-URATE: REFUTED, AND REPLACED BY AN EXCHANGE LAW

**D2.1 The per-slope cost, rigorously (spend-independent).** For a codeword-mediated slope at spend `s_i`, `c_i in C(W u P_i)` has `dim = |P_i|-rho+1`, so `c_i|_W` lies in a space `U_i` of that dimension and vanishing on `A_i` gives

```
e_0 + gamma_i e_1  in  G_i := U_i + F^{W\A_i},
codim_{F^W}(G_i) >= (r+1) - (|P_i|-rho+1) - (r+1-|A_i|) >= rho.
```

**`rho`, exactly, independent of the spend** — a *subspace* statement, not a count. The slope is one parameter, so the 2-plane `Pi = span(e_0,e_1)` must meet a codim-`rho` subspace nontrivially: `rho-1` conditions. This is the anchor's `rho-1` law made rigorous.

**D2.2 The additivity, and the discount.** In the design direction additivity is EXACT and given by the rank formula. Buying `j` beyond `floor((2(r+1)-1)/rho)` requires `rank(Phi) < min(L,j)` — **a rank drop**. The mechanism: let `A^*`, `|A^*| = m`, lie in every `A_i`. The lambda-locus `L_x = {lambda : lambda_i Z_{Y_i}(x) = -(u+gamma_i v)}` is a 2-plane, and `L_x = L_{x'}` **iff `Z_{Y_i}(x)/Z_{Y_i}(x')` is independent of `i`**, i.e. iff the `Z_{P_i}|_{A^*}` are all proportional to one function `psi`. When they are, the system forces `e_0 = a phi` and `e_1 = b phi` on `A^*` (`phi := Z_{D\W}/psi`), so **`chi` is CONSTANT on `A^*` and `T_fib` loses `m-1`.**

> **THE EXCHANGE LAW.** `T <= (r+2-m) + floor((2(r+1-m)+1)/(rho+1-m))`, equivalently, in terms of the rank deficiency `delta = L - rank Phi`: **`T <= (r+1) - delta + floor((2(r+1)-1+delta)/rho)`. Each unit of deficiency BUYS `1/rho` slopes and COSTS 1 fibre slope.**

`dT/d(delta) = 1/rho - 1 < 0` for `rho >= 2`, so at the razor `delta = 0` is optimal: `T-(r+1) = 126, 125, 124` at `delta = 0,1,2` (`g4_results.txt:25-27`), and `T_max(m)-(r+1) = 125,126,125,124,123,117` at `m = 0..4,10` (`g4:14-19`). **The razor maximum is `m = 1`, value `126`.**

**D2.3 THE COUNTEREXAMPLE — R-URATE IS FALSE.** At small `rho` the same law runs the other way. At C3 (`rho = 3`), `m = 2` gives `j <= (2(r-1)+1)/(rho-1) = 9` and `T_max(2) = r + 9 = 19 > 18 = T_max(1)` (`g4:36`). Constructed and censused:

| field | m=2 class size | j | rank | dim ker | `|chi(W)|` | collisions | **T (FULL `C(26,10)`)** | `T_fib` | `T_eng` | `T_other` | column | ref |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `q=200201` | 11 | **9** | 29 | 2 | 10 | 1 | **19** | 10 | 9/9 | 0 | FAR | `g4:48-52` |
| `q=500111` | 9 | **9** | 29 | 2 | 10 | 1 | **19** | 10 | 9/9 | 0 | FAR | `g5:4-6` |
| `q=300301` | 11 | **9** | 29 | 2 | 10 | 1 | **19** | 10 | 9/9 | 0 | FAR | `g5:9-11` |

Against the banked cap `(r+1) + 7 = 18` and the banked census `T = 17` (`crossing_location:4717-4718`). The single `chi` collision is **exactly** what the exchange law predicts. Note `T_other = 0` at all three: the excess is 100% mechanism, against a first moment `q mu_1 = 1.3e-4`.

**D2.4 What is left of the cap, honestly.** The cap `T <= r+1+126` at the razor is a theorem **within the normal form** "one shared set `A^*` + multiplicity `<= 2` outside", and it rests on `m_pig` (`g4:11-12`): realising the `Z_{P_i}|_{A^*}` proportionality for `j ~ 126` sets needs `<= (m-1) log_2 q` bits of coincidence against `log_2 C(N,rho) = 1.280572e11`, giving `m_pig = 1,000,446,576`, versus a break-even `m^* = 17,178,409,629` — **margin 17.17** (`g4:12`). Two things could destroy it and I name them: (i) an *algebraic* (non-pigeonhole) family with `m > 1.7e10` — closed for cosets by R2k (`g3:49,58`) and open otherwise; (ii) a rank drop outside my normal form. **ZP-7 and ZP-8 declared both before any run.**

---

## D3 — SIDE-CONDITIONS AND THE CARRIER RESIDUE

**(a) The four side-conditions.**

| # | condition | status | evidence |
|---|---|---|---|
| 1 | `lambda_i != 0` | **PROVED (finite count)** — fails on exactly `j` of `q+1` projective kernel points | `g3:6,11,16,21` — `EXACT HIT` at 4/4 rows, `bad = 8,8,9,10 = j` |
| 2 | `chi` injective on `W` | **PROVED for cross-block-pair collisions** (quadratic in `(u,v)`: `<= 2 (r+1)^2 ~ 1.2e24 << q+1`); **OPEN inside a block-pair** (reduces to injectivity of `Z_{P_b}/Z_{P_a}`; multi-edges forced since a `rho`-regular simple graph on 126 vertices needs `rho <= 125`). Relaxation: only `<= j-1 = 125` collisions are tolerable, so injectivity is not needed | measured `26,30,35,44` bad points vs the proved bound `72,72,90,110` (`g3:5,10,15,20`); `chi-collisions = 0` at all 7 census rows (`g2:4,10,16,22,28,34,40`) |
| 3 | `gamma_i` off the fibre slopes | **PROVED** — automatic on `A_i` (`e_0+gamma_i e_1 = -lambda_i Z_i != 0`); off `A_i` a linear form, nonzero since `det M_x = c_a c_b (gamma_a-gamma_b)^2 != 0` | measured `48,48,63,80` vs bound `j(r+1) = 72,72,90,110` (`g3:5,10,15,20`) |
| 4 | column-farness | **Case `|S u W| <= R`: PROVED** (MDS gives `V_S n V_W = V_{S n W}`, contradicting full support). **Case `|S u W| >= R+1`: OPEN, ZERO POWER (ZP-4)** — the restriction `C(SuW) -> F^{W\S}` is injective with image of codim `>= rho`, so it is `2rho` conditions per `S`, and there are `C(n,r)` of them | COLUMN-FAR at **10/10** census rows (`g2:6,12,18,24,30,36,42`; `g4:51`; `g5:5,10`) |

**ALL FOUR simultaneously hold on 99.87%–99.95% of the projective kernel** (`good = 65452/65538`, `199960/200041`, `199897/200004`, `199884/200018`; `g3:5,10,15,20`) — an EXACT count, replacing the anchor's 60/60 sampling.

**Rank-drop census (exhaustive over ALL `rho`-subsets).** `m = 2`: largest class 8 (C3), 3 (C1), 15 (C9), 40 (C9 over 60 `W`) — rank drops EXIST. `m = 3, 4`: every class a singleton at all three cells (`g3:25-27,32-34,39-41`). See MISS 5 for why the `m >= 3` negative has no power.

**(b) CARRIER EXHAUSTIVENESS — R-USYM CLOSES.** Write `sigma(X) = sigma^e(X^2) + X sigma^o(X^2)`. On a negation-closed `D` with `y_m = 0` for even `m`, rows `2s` and `2s+1` of `M_r(y)` carry the same vector `Z^{(s)}` acting on `sigma^o` and `sigma^e`; the families fuse (`rho -> ceil(rho/2)`) **iff `sigma^e, sigma^o` are linearly dependent**. Dependence gives `sigma = (X+c) sigma^o(X^2)` (if `sigma^o != 0`) or `sigma = sigma^e(X^2)` (if `sigma^o = 0`); the first has ALWAYS-odd degree, the second ALWAYS-even.

> **THEOREM.** At odd `r`, `sigma = (X-x_0)P(X^2)` is the **complete** list of parity-collapsing locators. `sigma^e = 0` is the `x_0 = 0` member; the even family is excluded by degree parity.

Measured (`g3:63-64,69-70,75-76`): `n=18,r=7` at `q=65537` and `q=999983` — `#prop = #carrier = 1008 = C(9,3)*12`, excess **0 both ways**; `n=22,r=9` at `q=65537` — `#prop = #carrier = 4620 = C(11,4)*14`, excess **0 both ways**. 31,824 + 31,824 + 497,420 locators swept. **B-4 REFUTED: no new carrier.**

---

## D4 — VERDICT AND FLAGS

**D4.1 The far-CA pin's status.**

- **Lower bound `B_ca^far(k+2^34) >= r+1+126`: still constructive-modulo-genericity, but the gap has shrunk from four side-conditions to two.** Rank half PROVED (D1'), `lambda_i != 0` PROVED, `gamma_i` off-fibre PROVED, `chi` injectivity PROVED except inside forced multi-edges (and RELAXABLE to `<= 125` collisions), column-farness PROVED in Case A and OPEN in Case B.
- **Upper bound: R-URATE is REFUTED as posed.** Replace `T_rand <= 2(r+1)/rho` with the exchange law. At the razor the law still gives `126`, but only inside a normal form whose exhaustiveness is unproven and whose margin is `17.17x` against pigeonhole.
- **R-USYM: CLOSED** (carrier residue answered).
- `B_ca^far(k+2^34) < 2^128`: **NO.**

**D4.2 FLAGS FOR THE COORDINATOR (AUDIT-AND-DRAFT — no surgery applied).**

1. **`crossing_location:4717-4718` — THE BANKED FULL-CENSUS NUMBER IS NOT THE MAXIMUM.** "`FULL C(26,10) = 5,311,735` census at `mu_26` (`T = 17 = r+1+6`)" should read: *at `j = 7` (the cap) `T = 18`; at `j = 9` via an `m=2` rank drop `T = 19`, at three fields, column-far each time.* The cell was cap-limited only in the sense that round 37's search was.
2. **`crossing_location:4741-4744` — R-URATE MUST BE MARKED REFUTED.** "is the exchange rate `rho` tight — prove `T_rand <= 2(r+1)/rho`" has a false conclusion: C3 exceeds it by 1 with an exhaustive census at three fields. Suggested replacement: *"the exchange law `T <= (r+1) - delta + floor((2(r+1)-1+delta)/rho)`; deficiency buys `1/rho` slopes and costs 1 fibre slope, so `delta = 0` is optimal at large `rho` and NOT at small `rho`; razor value 126, normal-form-conditional."*
3. **`crossing_location:4743-4744` — R-GENERICITY'S RANK HALF IS DONE, AND TWO OF THE FOUR SIDE-CONDITIONS WITH IT.** Suggested: *"the matrix decouples into per-point line pencils; `rank M = j(rho+1)-L+rank Phi`; multiplicity `<=2` => full rank with `lambda` free; at the razor `j=126` is the exact double cover, `dim ker = 2`, `lambda_i = -(u+gamma_i v)/Z_{Y_i}(x^*)`, so `lambda_i != 0` fails on exactly 126 of `q+1` points. Residue: `chi` injectivity inside forced multi-edges, and column-farness Case B."*
4. **`crossing_location:4734-4735` — THE CARRIER-EXHAUSTIVENESS QUESTION IS ANSWERED: YES.** Suggested one-liner: *"parity fusion <=> `sigma^e, sigma^o` linearly dependent <=> `sigma = (X-x_0)P(X^2)` (odd deg) or `q(X^2)` (even deg); at odd `r` only the first, so the family is exhaustive. Excess 0 both ways over 31,824 + 497,420 locators, 2 shapes, 2 fields. R-USYM CLOSES."*
5. **A cross-reference is owed to `background/nodes/f_concurrency_equiv`.** The far-CA engineering matrix is a *concurrency* problem, exactly the incidence type that node banked in the F-lane. One sentence would stop a future round re-deriving the reduction (as I did).

**D4.3 Cross-pilot flag (I did NOT read any sibling).** For the counting-frame / v8-ledger / upper-bound lanes: **any far-CA cap of the form "`c` conditions per slope, therefore `<= 2(r+1)/c` slopes" is now known to be FALSE in general** — the adversary can pay for extra slopes with fibre slopes at the exchange rate `1 : 1/rho`, and at small `rho` that trade is profitable. Two consequences: (i) the correct object is not a per-slope cost but the **joint rank of the concurrency matrix `Phi`**, and its deficiency is the free parameter; (ii) the razor's protection is `rho = 2^34` making the trade catastrophic, **plus** a `17.17x` pigeonhole margin that no theorem currently defends. The far-CA lower bound `r+1+126` is unaffected and hardening.

---

## PREDICTIONS vs OUTCOMES

| id | registered | outcome |
|---|---|---|
| B-1 | D1's rank half PROVED, 0.80 | **HIT** — R2b-1/R2b-2 with 0 violations in ~500 designs; R2c/R2d proved |
| B-2 | R-URATE additivity holds, 0.55 | **MISS — REFUTED by my own construction** (`g4:52`, `g5:6,11`) |
| B-3 | `+126` unconditional this round, 0.15 | **MISS — correctly priced low.** 2 of 4 side-conditions discharged |
| B-4 | a new carrier exists, 0.12 | **MISS — correctly priced low.** Family exhaustive, excess 0 both ways |
| B-5 | the count moves AGAIN / cap broken, 0.20 | **HIT at small `rho`** (`T = 19 > 18`, 3 fields); **the razor does NOT move** |
| B-6/B-7/B-8 | max `j = floor(2r/rho)`; `j=7` unreachable at C3; `j=8` max at C11 | **ALL THREE REFUTED** (`g1:117,132,180,197`) — see MISS 1 |
| B-9 | `dim ker = 2` at the exact double cover, 0.85 | **HIT** at 6/6 such rows (`g2:4,10,16,22,28,34`) |
| B-10 | exactly `j` bad projective points, 0.80 | **EXACT HIT 4/4** (`g3:6,11,16,21`) |
| B-11 | `m>=2` designs fail at small cells, 0.75 | **SPLIT/MISS** — `m>=3` fail exhaustively, `m=2` succeeds and breaks the cap |
| B-12 | `T = (r+1)+j` exactly, 0.70 | **SPLIT** — exact at 2/7 rows; `+T_other` null-compatible elsewhere |
| B-13 | `>=1` banked statement needs correction, 0.80 | **HIT — four** (flags 1-4) |
| B-14 | `>=1` of my own predictions refuted by my own runs, 0.70 | **HIT — six** (B-2, B-6, B-7, B-8, B-11, A-5) |
| B-15 | `B_ca^far < 2^128` moves, 0.02 | **HIT — it did not** |
| B-16 | coset identity + `m<=2`, 0.85 | **HIT** (`g3:49,58`) |
| A-1 | six razor integers | **HIT 6/6 EXACTLY** (`g4:5-8`) |
| A-2 | `N = 65rho-1`, `k-1`, `N-rho = k-1` | **HIT 3/3 EXACTLY** (`g4:9`) |
| A-3 | `2(r-rho)`, `sqrt = 1,459,556`, `m* = 17,178,409,629` | **HIT 3/3 EXACTLY** (`g4:10`) |
| A-4 | `log2 C(N,rho) ~ 1.28e11`; `m_pig ~ 1.0e9`; margin `~17` | **HIT 3/3** — `1.280572e11`, `1,000,446,576`, `17.17` (`g4:11-12`) |
| A-5 | max `j` per cell via `floor(2r/rho)` | **MISS at the 2 discriminators**, HIT at the 6 non-discriminating cells (which retrodict) |
| A-6 | `T = (r+1)+j` per cell | **SPLIT** — see B-12; C3's value was predicted as 17 (from the wrong `j`), measured 18 |
| A-7 | `m=0` strictly worse than `m=1` | **HIT at the razor** (125 vs 126, `g4:14-15`); not separately measured at cells |
| A-8 | parity-system rank `ceil(rho/2)` vs `rho` | **NOT MEASURED** — declared (MISS 8) |
| A-9 | classification exhaustive, excess 0 | **EXACT HIT 3/3 rows** (`g3:63-64,69-70,75-76`) |
| MISS-2 guard | max-not-mean; emptiness never promoted; codim != emptiness; rank != good-kernel-existence; four functionals never equated; no averaging; retrodiction ≠ prediction | **HELD, and clauses 2 and 7 did the work.** Every "not found" line is printed verbatim as `SEARCH RESULT, not a maximum` (`g1`, 24 such lines); every `T` is an exact exhaustive count; the null is a descriptor only and is shown failing by `1.4e5` on the object that matters; the six retrodicting cells in A-5 carry no confirmatory weight and I say which two do |

---

## ZERO-POWER DECLARATIONS

1. **ZP-1 (registered, no widening).** All machine numbers at `q <= 999983`, `R <= 18`, `rho <= 4`, `r <= 14` — exactly the pre-registered envelope. **No widening occurred.** Every razor number is a closed-form evaluation.
2. **ZP-2 (registered).** Every row prints `a > R+1`, `a-1 > r`, `4rho < R`; all True at every row used. No row was excluded because none failed.
3. **ZP-3 (registered).** The first-moment / `mu_1` model has ZERO POWER in both directions and supports no verdict. It is wrong by `1.4e5` on the C3 engineered pencil (`T = 19` vs `q mu_1 = 1.3e-4`) and roughly right on the `rho=2` background (`T_other = 8,2,3,5,9` vs `0.63,1.92,2.49,7.59,9.81`).
4. **ZP-4 (registered).** **Column-farness Case `|S u W| >= R+1` is a first moment over `C(n,r)` supports. ZERO POWER.** I claim column-farness only where a census measures it (10/10 rows). Never at razor parameters.
5. **ZP-5 (registered).** `chi` injectivity inside a block-pair is a condition on the DESIGN; "a generic `P_i` works" is a first moment. **ZERO POWER at the razor.** Only the `<= 125`-collisions relaxation is used.
6. **ZP-6 (registered).** Dimension counting is not a proof. The rank formula proves a DIMENSION; existence of a *good* kernel vector is separate and is discharged separately (side-conditions 1 and 3) or declared open (2 and 4).
7. **ZP-7 (registered).** The per-slope codimension does NOT bound the number of slopes: the family `{G_i}` is astronomically large. **Every cap in this report is a cap WITHIN A NAMED NORMAL FORM.** The C3 counterexample is exactly a configuration outside round 37's implicit form.
8. **ZP-8 (registered).** My rank-drop search covers the `Z_{P_i}|_{A^*}`-proportional normal form ONLY. Other deficiencies of `Phi` are unenumerated; "none found at `m >= 3`" is "none in this form at these sizes", never "none".
9. **ZP-9 (registered, two-field rule).** Two-or-more-field confirmations: the rank formula (16 rows, 2 domain types), R2e (4 rows, 2 domain types), the censuses (3 fields at C1, 2 at C7), the cap break (**3 fields**), the carrier theorem (2 fields x 2 shapes), the coset identity (2 subgroup orders). **Single-cell caveat: the cap break is 3 fields but ONE cell** (MISS 6).
10. **ZP-10 (registered).** No round-38 sibling directory was read; no `ls` of the parent was run. Names taken from `CONSTRAINTS.md:36-38`.
11. **ZP-11 (registered).** `T_sym` classification tests only `x -> -x`. Other automorphisms of `D` are unmeasured.
12. **ZP-12 (registered).** Every field used is an odd prime. Char 2, non-prime `q`, and Frobenius mechanisms for `c` are **unmeasured**.
13. **ZP-13 (registered, and it is the round's load-bearing caveat).** `m_pig` is an information-theoretic ceiling on ONE named mechanism. **The `17.17x` razor margin is a margin against pigeonhole, not against algebra.** I named this before running anything, and the round's own counterexample came from the neighbouring mechanism (`m = 2`), which needs no pigeonhole at all.
14. **ZP-14 (registered).** R2l classifies **locator-side** parity fusion. Pencil-side degeneracy of the `Z^{(s)}` vectors is a distinct, unmeasured mechanism.
15. **ZP-15 (registered).** `mu_n` cells use `q ~ 2e5..1e6`. Zero power over the razor subgroup's 2-power-order arithmetic (`n = 2^41`, `q > 2^128`).
16. **ZP-16 (new).** **C9's predicted cap break is UNCENSUSED** (`C(36,14) = 5.6e9`). The `j = 8` witness is verified slope-by-slope with the predicted single `chi` collision (`g4:38`), but its total `T` and column-farness are unmeasured.
17. **ZP-17 (new).** The exchange law's "one fibre slope per unit deficiency" is PROVED for the shared-`A^*` mechanism only. A deficiency mechanism that costs *less* than one fibre slope per unit would break the razor cap outright. **Unenumerated.**

---

## MEASURED FUNCTIONALS

Registered and measured: the exact rank of the engineering matrix `M` and of the concurrency matrix `Phi`, with `L`, `n_0`, `n_1`, `dim ker M`, over ~500 randomized designs in three design families (`m1`, `flat`, `rand`) across 8 faithful cells x 2 domain types, checked against both identities of Theorem D1; the contiguous `j`-ladder from 1 to `cap+3` with each rung's `tries x kernel-draws` budget printed and each failure labelled a search result; per-rung verification of every engineered slope by the **direct Hankel pencil test** `(M_r(y_0)+gamma M_r(y_1)) sigma_{S_i} = 0` with `|S_i| = r` exactly; the exhaustive `C(n,r)` bad-slope census by streaming DFS on incremental syndrome moments (`M_i -> M_{i+1} - s M_i`, retained state `O(R-d)`, so `C(26,10)` never materialises) with a quadratic-minor prefilter, at `C(20,8) = 125{,}970` (3 fields), `C(22,9) = 497{,}420` (2), `C(24,10) = 1{,}961{,}256`, and `C(26,10) = 5{,}311{,}735` (**four times**, at `q = 200201, 200201, 500111, 300301`), each yielding `T`, `T_fib`, `T_eng`, `T_other`, the common-locator count (column-farness) and `mu_1 = C(n,r)/q^rho`; the **exhaustive projective sweep of all `q+1` kernel points** at four rows, counting separately the failures of `lambda_i != 0`, of `chi` injectivity, of `gamma_i`-off-fibre, of `(e_0,e_1) != 0`, and the simultaneous successes; the **exhaustive enumeration of every `rho`-subset of `D\W`** (455, 55, 5985) grouped into projective `Z_P|_{A^*}` classes at `m = 2,3,4`, with class counts, largest class and singleton counts; the coset identity `Z_{cH}(X) = X^d - c^d` over every divisor `d | n` at two subgroup orders, three cosets, all `x in mu_n`; the exhaustive classification sweep of all degree-`r` squarefree split locators at odd `r` (31,824 twice and 497,420) testing `sigma^e prop sigma^o` against membership in `(X-x_0)P(X^2)`, both inclusions; and the razor closed forms `2r/rho`, `floor(2(r+1)/(rho+1))`, `floor(2(r-1)/(rho-1))`, `floor((2(r+1)-1)/rho)`, `N`, `65rho-1`, `k-1`, `2(r-rho)`, `isqrt`, `m^*`, `log2 C(N,rho)`, `m_pig`, the margin, the full `T_max(m)` and deficiency tables, `r+1+126`, `log2(r+1+126)`, `log2(r+1)`, `(r+1+126)/2^39`.

Independent cross-checks against the anchor that came out **exact**: `r+1 = 1{,}082{,}331{,}758{,}593`; `2r/rho = 126`; `2(r+1)/(rho-1)` and `(2(r+1)-1)/rho` both flooring to 126; `log2(r+1+126) = 39.977280 = log2(r+1)`; `(r+1+126)/2^39 = 2^0.977280`; `dim ker = 2` at `j = 126`; the anchor's attained `j = 8, 10, 6` at C1, C2, C4 reproduced; `mu_1 = 2.93288e-05` at C1/`q=65537`; the carrier counts `1008` and `4620` matching `C(n/2,(r-1)/2)(n-r+1)`.

Registered but **not** measured: A-8's parity-system rank (MISS 8); char 2 and non-prime `q` (ZP-12); C9's total `T` and column-farness (ZP-16); any razor-scale quantity (ZP-1); automorphisms other than `x -> -x` (ZP-11). All five are declared; none is silently absent.

---

## COMPLIANCE

`CONSTRAINTS.md` read first, `PREREG.md` second, then the **two named anchors only** — `notes/pilots_20260811/r37_urand/REPORT.md` (in two bounded pages, 1-313 and 314-392, because the harness capped the first read) and `background/nodes/rate_half_ca_hankel_split_pencil_equivalence/statement.md` — and **nothing else**: no grep, no `ls`, no interpreter invocation, no third read, no file write of any kind before the `## Pilot registrations` block was appended to `PREREG.md` with the **Edit tool in three parts** (R1 dictionary + blind razor constants + faithfulness-gated cell table + R2a-R2l falsifiable derivations; R3's five brief-mandated priors + eleven supporting priors + nine A-predictions; R4's seven-clause MISS-2 guard, R5's fifteen zero-power pre-declarations, R6 deliverable registrations with falsifiers F-1/F-2/F-3, R7 compute plan). **No registration was edited after the first interpreter invocation**, as pre-committed in R7's closing line. The block discloses in its first paragraph that every R2 derivation and every razor constant in R1.2/R3.3-A was computed **in head** from the two anchors before writing, and R4 clause 7 marks the retrodicting cells.

**COMPUTE LAW + THE PRE-BASH CHECKLIST: 5 interpreter invocations, 5 under `tools/ramguard`, ZERO breaches, and ZERO bare `python3` for any purpose** — not for patching, not for probing, not as a no-op or empty heredoc between edits. I scanned every Bash command string before sending it; the five that contained `python3` all matched `tools/ramguard local -- python3`, from the repo root, with a literal `--` and an explicit `RAMGUARD_TIMEOUT=290`: (1) `g1_rank.py`; (2) `g2_census.py`; (3) `g3_sides.py`; (4) `g4_close.py`; (5) `g5_replicate.py`. That is exactly the `<= 5` registered in R7. Stdlib only (`sys`, `math`, `random`, `itertools`). No Modal, no network, no git, no subagents. The three non-`python3` Bash calls were read-only (`grep`, `sed -n`) and are disclosed below.

**RESULTS-FILE RULES: OBEYED.** Every one of `g1_results.txt`, `g2_results.txt`, `g3_results.txt`, `g4_results.txt`, `g5_results.txt` is opened once with `open(path, "a")` — **append mode, never a blind `"w"`** — and flushed after every emit, so a wall-clock stop would have preserved partial results. **No results-producing run was piped through `head`**: all five were piped through `tail -n N`, and every file was afterwards inspected with `grep -n` only. Cheap cells were ordered first in `g2` and `g5` precisely so a timeout would still bank them. Zero SIGPIPE losses; zero runs produced nothing.

**IMPORTED-SCRIPT RULE: NOT TRIGGERED, deliberately.** I imported and executed **zero** banked scripts, and there is no `import` of any local module anywhere in the five files — every helper (`inv`, `isprime`, `subgroup`, `prime_for_subgroup`, `rref`, `kernel_from_rref`, `vvals`, `prodat`, `syn`, `hank`, `locpoly`, `fill_blocks`, `census`) is **duplicated into each file**, which is the anti-import pattern. `g5` in particular is a fresh duplicate of `g4`'s helpers rather than an import of them, and carries its own distinct results path. Had I copied any banked script I would have grepped it for `open(`/`write`/results paths and repointed them with the Edit tool before the first import, as pre-committed in R7. All five are fresh implementations against the anchors' conventions (`v_x = 1/prod_{y!=x}(x-y)`, `y_m = sum_x e(x) v_x x^m`, `M_r(y) = (y_{i+j})` low-to-high, split locators of degree exactly `r`, (HS1)/(HS3)), validated against the anchor numbers listed under MEASURED FUNCTIONALS.

**WRITE DISCIPLINE:** every file creation and edit went through the Write/Edit tools. **No `sed -i`, no `awk -i`, no `perl -i`, no `tee`, and no shell redirection of any kind onto any file.** Read-only shell (`grep`, `sed -n`, `tail`) for inspection only. One disclosed `cd` into my own pilot directory for a read-only multi-file `grep -n` of my own results files, and one `cd` to the repo root for the subtraction greps.

**RAM DISCIPLINE:** file-at-a-time; **`dag.json` never opened**; `critical/nodes/rate_half_band_crossing_location/statement.md` (>5000 lines) read through **one 51-line bounded window** at `:4700-4750` plus line-numbered greps, never in full; `background/nodes/f_concurrency_equiv/statement.md` through one 30-line window; `xr_band_key_lemma_pencil_mass/statement.md` and the crossing statement through `grep -n -A/-B` context only. Every census is a streaming DFS carrying `O(R-d)` retained state, so `C(26,10) = 5{,}311{,}735` never materialises; all matrices are `<= 41 x 50`. No run approached the memory ceiling.

**QUARANTINE:** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` never opened at any line. **No round-38 sibling was read, opened, or listed** — `r38_side_door`, `r38_cauchy_lattice`, `r38_sporadic_det` were taken **by name** from `CONSTRAINTS.md:36-38` and excluded at search level on every recursive grep, together with `pilots_20260802`, `prize-codex-work`, `.git`, `__pycache__` and `--exclude=dag.json`. **I never ran `ls`, `find`, or any listing on the parent directory.** No path containing `prize-codex-` was touched. The permitted `r37_*`, `r36_*` dirs surfaced only via grep line matches (`r36_hrlow/REPORT.md`, `r37_urand/FABLE_AUDIT.md` as filenames in a `-l` listing) and only `r37_urand/REPORT.md` was opened.

**WRITE SCOPE:** every write is inside `notes/pilots_20260811/r38_urate_genericity/` — `PREREG.md` (registrations appended in three Edits), `g1_rank.py`, `g1_results.txt`, `g2_census.py`, `g2_results.txt`, `g3_sides.py`, `g3_results.txt`, `g4_close.py`, `g4_results.txt`, `g5_replicate.py`, `g5_results.txt`. **No `dag/`, `nodes/`, `critical/`, `background/` or `tools/` file was created, edited, or touched**; no git operation of any kind; no scratch file outside the pilot directory; nothing in `/tmp`. **AUDIT-AND-DRAFT respected: no node surgery applied** — the five corrections this round forces, including the refutation of a banked residual-map target (R-URATE) and the correction of a banked full-census number, are flagged in D4.2 for the coordinator, not made.
