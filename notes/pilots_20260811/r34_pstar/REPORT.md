As expected, the harness refused the write. Full REPORT text follows verbatim.

---

# REPORT — r34_pstar (round 34)

## MISSES FIRST

1. **THE BRIEF'S "EQUIVALENTLY" IS FALSE, AND SO IS THE BANKED NODE TEXT
   THAT CARRIES IT.** The mandate reads "does ANY column-far pencil at
   razor-shaped parameters have `p* <= R/2` (equivalently: is FG nonempty
   among column-far pencils in the wide regime)". These are **not**
   equivalent. FG membership (`K_0 = P*·F[x]`, i.e. `h_r = p*`) forces
   `p* <= 2rho`, which at the razor is `p* <= R/32` — a factor **16**
   stronger than `p* <= R/2`. The same conflation is banked verbatim at
   `critical/nodes/rate_half_band_crossing_location/statement.md:3059-3061`.
   I registered this as R0-e at 0.85 and it is confirmed by exhibition
   (D1.3, four constructed column-far pencils with `2rho < p* <= floor(R/2)`
   that are provably **not** in FG, `e2_results.txt`). The verdict is
   unaffected only because I answer YES to the *stronger* question.
2. **I WAS WRONG THAT THE FG GENERATOR IS LITERALLY FIXED, AND MY OWN
   MEASUREMENT REFUTES ME.** On constructed FG pencils the modal low
   apolar generator covers only **8–12 of 11–13** slopes (and 14–17 of 17),
   with **1 to 4 distinct** generators over the slope line
   (`e2b_results.txt`, all four cells). "Fixed" is a *generic-slope*
   statement with exceptional slopes, exactly as round 33's FG5 words it
   ("at every generic slope") and not as I read it. The one construction
   with a literally constant generator at every one of the `q` slopes is
   witness A (`e2_results.txt`, `distinct = 1` at all four cells).
3. **R0-g is a hairline MISS at one cell of six.** I registered "modal
   `p* = ceil(2R/3)` in **>= 90%** of uniform random pencils". Measured:
   0.91500, 0.90017, 0.99100, 1.00000, 0.99650 — and **0.89933** at the
   LB1 cell (`e1_results.txt:37`). The true value there is `~1 - 1/q =
   0.909`, so I set the threshold essentially *at* the truth and lost to
   sampling noise. A badly-chosen window, not a surprising world.
4. **Witness A is dead as an R-FG instance at one cell.** At `S3_sep` the
   closed-form witness A has bad-slope count **`T = 0`**
   (`e2_results.txt`). It is a valid FG member and a valid column-far
   pencil, and a *useless* live instance of the budget question. The live
   instances come from construction C, where `T` ranges 1..13.
5. **NO BOUND. `B_ca^far(k+2^34) < 2^128` remains NO.** I add no upper
   bound of any kind. This round is an existence verdict plus coordinates;
   it moves a residual from "possibly empty, possibly closable negatively"
   to "nonempty, with witnesses", which is the opposite of the
   simplification the brief hoped for.
6. **Zero razor-regime measurement.** Every machine number here is at
   `q <= 17`, `R <= 16`, `rho <= 3`. Everything at razor scale is
   closed-form arithmetic and elementary proof. Pre-registered.
7. **THE DIMENSION COUNT IS A TRAP AND I ALMOST LET IT CARRY THE
   VERDICT.** `codim{p* <= 2rho} = 2R-3p = 2,095,944,040,448` out of an
   ambient `dim Gr(2,R) = 2,199,023,255,548` — a naive reader (and I, for
   one draft) sees 95.3% codimension and reads "empty". It is not: the
   locus still has dimension `3p-4 = 103,079,215,100`, i.e. `~q^{10^11}`
   points over any field. **Codimension bounds density, never
   emptiness** (pre-registered MISS-2-guard item 4). The verdict rests on
   witnesses, not on the count. Registered R0-d = 0.35 for "the count is
   decisive" — HIT, in the sense that it is not.
8. **First-moment heuristics are actively misleading at razor shape.** At
   `q = 2^41`, `mu_2 = C(n,r)/q^{2rho} = 2^{7.899e11} >> 1`, so the random
   model says a uniformly random pair is column-**close** and column-far
   pairs are exponentially rare. My witnesses A and B are column-far
   **unconditionally** at exactly those parameters. The random model has
   zero power at the razor and I flag it as the round's main interpretive
   hazard — it is the same lesson as banked BANK 2
   (`crossing_location:3042-3045`: "*random-embedding censuses have
   `q^{-Theta(m^2)}` power — construction or nothing*").

---

## VERDICT

**FG IS NONEMPTY AT RAZOR SHAPE. The fixed-generator branch does NOT close
negatively. R-KER does NOT become the sole far-CA residual. R-FG is live
and now has explicit witnesses at razor parameters.**

I answer the mandate's question in the affirmative twice over, by
construction and not by count:

- `p* <= R/2` **occurs** among column-far razor pencils. In fact
  `p* = 2rho = 2^35` occurs, which is `R/32`, sixteen times below the
  lemma bracket.
- FG (the *stronger* condition the brief conflated with it) is **also**
  nonempty at razor shape, with two explicit witnesses — one with `P*`
  non-squarefree, one with `P*` squarefree so that round 33's FG3/FG4
  scaled-Vandermonde normal form and key equation apply verbatim.

The anticipated "tension" between low `p*` and column-farness **does not
exist**. Low `p*` makes `K_0` principal, and column-farness on a principal
`K_0` is a condition on `P*` alone, satisfied by all but a `2^{-1.15e12}`
fraction of degree-`2rho` polynomials. The two conditions do not compete;
the first one hands you the second.

---

## D1 — THE `p*`-VS-COLUMN-FARNESS STRUCTURE

### D1.1 The exact three-line tension (and why it is not a tension)

Write `V = <y_0, y_1> ⊂ F_q^R`, `Ann(V)_i = ker[M_i(y_0); M_i(y_1)]`,
`p* = min{i : Ann(V)_i != 0}`, `K_0 = Ann(V)_r`, `h_r = r+1 - dim K_0`.
`P* ∈ Ann(V)_{p*}` annihilates both sequences over their full length `R`,
so `V ⊂ IS(P*)`, the `p*`-dimensional truncated inverse system.

```
(i)   P*·F[x]_{<=r-p*} ⊆ K_0        whenever p* <= r
(ii)  h_r <= min(p*, 2rho)           ALWAYS   (2rho rows; (i) gives <= p*)
(iii) K_0 = P*·F[x]_{<=r-p*}  <=>  h_r = p*  <=>  p* <= 2rho and full rank
(iv)  on (iii):  column-far  <=>  P* is not D-split-squarefree   [round 33 FG2]
```

(ii) is the whole story and is unconditional: **FG ⟹ `p* <= 2rho`.** The
converse holds generically. (iv) is round 33's FG2, which I re-derive and
confirm **in both directions** by controls: construction B (`P*` with an
irreducible factor) is column-far at 4/4 cells, construction B' (`P*`
fully `D`-split-squarefree, everything else identical) is column-**close**
at 4/4 cells (`e2_results.txt`, `q = 11, 13, 17`).

The consequence the brief did not anticipate: on the low-`p*` locus,
column-farness costs **nothing**. The `D`-split-squarefree `P*` of degree
`p` number `C(n,p)` out of `~q^p`; at razor with `p = 2rho`,
`log2(C(n,p)/q^p) = 2.553e11 - 1.409e12 = -1.153e12`
(`e3_results.txt`). Almost every `P*` is column-far-inducing.

### D1.2 The corrected trichotomy at razor shape

| stratum | condition | `h_r` | `K_0` | generic-slope generator | visible at any round-33 cell? |
|---|---|---|---|---|---|
| generic | `p* = ceil(2R/3)` | `2rho` | not principal | none (`p* > p_gen`) | yes |
| **intermediate (new)** | `2rho < p* <= R/2` | `2rho < p*` | **not** principal | `P*`, fixed generically | **no** |
| **FG** | `p* <= 2rho` | `p*` | `P*·F[x]` | `P*`, fixed generically | yes |

At the razor the intermediate band is `2^35 < p* <= 2^39` — sixteen
octaves wide. **It is empty at every round-33 cell**: those have
`2rho >= ceil(R/2)` ((11,3,5): `4 >= 4`; (10,2,4): `4 >= 4`;
(9,2,4): `4 >= 4`; (11,2,4) and (12,3,5): `4` vs `5`, one value). This is
the pre-registered zero-power declaration #2, and it is why round 33 could
not have seen the distinction. I built cells with `4rho < R` specifically
to separate them (`S1/S2/S3`, `e1_results.txt:5-7`).

### D1.3 The intermediate stratum exhibited (the brief's error made concrete)

`e2_results.txt`, construction E, four instances, two fields:

| cell | `R` | `rho` | `2rho` | `floor(R/2)` | `deg P*` | `p*` | `h_r` | `dim K_0` | `r+1-p*` | principal? | column-far? |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 (q=11) | 10 | 2 | 4 | 5 | 5 | 5 | 3 | 6 | 4 | **False** | **True** |
| S2 (q=13) | 12 | 2 | 4 | 6 | 5 | 5 | 4 | 7 | 6 | **False** | **True** |
| S2 (q=13) | 12 | 2 | 4 | 6 | 6 | 6 | 4 | 7 | 5 | **False** | **True** |
| S3 (q=17) | 16 | 3 | 6 | 8 | 7 | 7 | 6 | 8 | 7 | **False** | **True** |
| S3 (q=17) | 16 | 3 | 6 | 8 | 8 | 8 | 6 | 8 | 6 | **False** | **True** |

Every row satisfies the lemma bracket `p* <= floor(R/2)` and is column-far,
and **none is in FG**. So "`p* <= R/2` occurs" would not have implied "FG
nonempty" even if I had only proved the weaker statement.

### D1.4 An extension of round 33's FG3, off FG

The descent that produces the scaled Vandermonde needs only `V ⊂ IS(P*)`
with `P*` squarefree — i.e. only `p* <= r`, **not** `p* <= 2rho`. Every
`M_r(y_gamma)` kills `P*·F[x]`, so the whole pencil descends to
`Lambda = F[x]/(P*)` of dimension `p*`, and in CRT coordinates
`M̄(gamma) = W·diag(c(gamma))` with `W` the `rho x p*` Vandermonde and
`c` linear in `gamma`. Measured (`e2b_results.txt`, part (b)): among
uniform random **column-far** pencils, `p* <= r` in
**393/393, 395/395, 398/398, 400/400** across four cells and three fields,
and `P*` is squarefree in 361/393, 354/395, 368/398, 380/400 (~92%).

So the normal form is **not** a thin-stratum curiosity: at the razor the
*generic* column-far pencil has `p* = ceil(2R/3) = 733,007,751,851 < r`,
and descends to a `2^34 x 7.33·10^11` scaled Vandermonde. What FG adds is
only that the descent is *exact* (`K_0` principal, `dim K_0 = r+1-p*`);
off FG the quotient `K_0 / P*·F[x]` has the measured dimension
`p* - 2rho` (spectrum `2:398`, `3:392`, `4:398`, `5:398` at the four cells,
matching `ceil(2R/3) - 2rho = 2,3,4,5` exactly — `e2b_results.txt`).

*Caveat quoted:* `dim Ann(V)_{p*} = 3p*+1-2R` generically, so `P*` is
**not** unique when `3p* > 2R+1`: measured `dim = 1` in 396/398 at S2
(where `3p*-2R = 0`) and in 3/395, 2/400, 26/393 at the cells where the
predicted dimension is 2, 2, 3. The descent is by a *choice* of `P*`.

---

## D2 — THE CENSUS

### D2.1 The `p*` spectrum (uniform random pencils, `e1_results.txt`)

| cell | `q` | `n,k,r` | `R` | `rho` | samples | `p*` spectrum | modal | `ceil(2R/3)` |
|---|---|---|---|---|---|---|---|---|
| W1 (round 33) | 13 | 11,3,6 | 8 | 2 | 6000 | 5:510, 6:5490 | 6 | 6 ✓ |
| W2 (round 33) | 11 | 10,2,6 | 8 | 2 | 6000 | 5:599, 6:5401 | 6 | 6 ✓ |
| S1 (separating) | 11 | 11,1,8 | 10 | 2 | 6000 | 6:54, 7:5946 | 7 | 7 ✓ |
| S2 (separating) | 13 | 13,1,10 | 12 | 2 | 6000 | 8:6000 | 8 | 8 ✓ |
| S3 (separating) | 17 | 17,1,13 | 16 | 3 | 2000 | 10:7, 11:1993 | 11 | 11 ✓ |
| L1 (LB1 cell) | 11 | 7,2,3 | 5 | 2 | 6000 | 2:1, 3:603, 4:5396 | 4 | 4 ✓ |

Restricted to **column-far** pencils the spectrum is unchanged
(`e1_results.txt` part B; column-far fraction 0.9725, 0.9875, 0.9950,
0.9950, 1.0000, 0.9975), and `dim K_0 = r+1-2rho` at **every** column-far
sample at every cell.

**Does `p* <= R/2` occur?** By *sampling*: **never** —
`#{p* <= floor(R/2)} = 0` at all five wide cells (the single L1 hit at
`p* = 2` is at a cell with `floor(R/2) = 2 < 2rho`). By *construction*:
**always available** — every FG and every intermediate-stratum instance in
D1.3 and D3.2 has `p* <= floor(R/2)` and is column-far. This split is
exactly registered prior R0-b (0.95 by construction, 0.10 by sampling):
**both HIT**, and it is the pre-registered MISS-2 guard doing its job — a
census that never sees an event says nothing about whether it exists.

### D2.2 The codimension, calibrated (`e1b_results.txt`)

Registered R0-c: `dim{p* <= p} = 3p-4` in `Gr(2,R)`, hence
`codim = 2R-3p`, hence frequency `~ q^{-(2R-3p)}`.

| cell | `R` | `q` | `p` | samples | hits | measured `-log_q(freq)` | predicted `2R-3p` | \|diff\| |
|---|---|---|---|---|---|---|---|---|
| W1 | 8 | 13 | 5 | 60,000 | 4956 | 0.972 | 1 | 0.028 |
| W1 | 8 | 13 | 4 | 300,000 | 12 | 3.948 | 4 | 0.052 |
| W2 | 8 | 11 | 5 | 60,000 | 5982 | 0.962 | 1 | 0.038 |
| W2 | 8 | 11 | 4 | 300,000 | 18 | 4.054 | 4 | 0.054 |
| S1 | 10 | 11 | 6 | 120,000 | 1105 | 1.955 | 2 | 0.045 |
| S1 | 10 | 11 | 5 | 400,000 | 2 | 5.090 | 5 | 0.090 |
| S2 | 12 | 13 | 7 | 300,000 | 127 | 3.028 | 3 | 0.028 |
| S3 | 16 | 17 | 10 | 120,000 | 450 | 1.972 | 2 | 0.028 |
| L1 | 5 | 11 | 3 | 60,000 | 5969 | 0.962 | 1 | 0.038 |
| L1 | 5 | 11 | 2 | 300,000 | 23 | 3.952 | 4 | 0.048 |

**Ten calibration points, codimensions 1 through 5, three fields, maximum
deviation 0.090** against a registered tolerance of 0.5. R0-c HIT. The
parameter count is `p` for `P*` (projective) plus `2(p-2)` for
`Gr(2,p) ⊂ IS(P*)`.

### D2.3 The bad-slope budget on FG (`e2b_results.txt` part (c))

| cell | `q` | `rho` | `p` | `r+1` | `T` distribution (column-far FG pencils) | max `T` | mean `T` |
|---|---|---|---|---|---|---|---|
| W1 | 13 | 2 | 4 | 7 | 8:2 9:5 10:13 11:29 12:35 13:22 | **13** | 11.47 |
| S1 | 11 | 2 | 4 | 9 | 3:7 4:26 5:38 6:21 7:3 8:5 9:4 | **9** | 5.17 |
| S2 | 13 | 2 | 4 | 11 | 4:2 5:13 6:31 7:31 8:16 9:6 10:6 11:2 12:1 13:1 | **13** | 7.02 |
| S3 | 17 | 3 | 6 | 14 | 1:6 2:15 3:24 4:37 5:16 6:14 7:1 9:1 | **9** | 3.82 |

`T <= rho` and `T <= p` are refuted at all four cells; `T <= r+1` is
refuted at W1 (13 > 7) and S2 (13 > 11) and survives at S1 (9 = 9, tight)
and S3 (9 < 14). W1 reproduces round 33's FG7 row for the same cell
(their `9:2 10:1 11:7 12:17 13:12`, max 13 — mine `max 13`, same shape),
an independent re-implementation cross-check.

**The banked "on FG the measured `T = q`" is cell-dependent, not
universal.** It tracks the ordering statistic `mu_1 = C(n,r)/q^rho`:

```
mu_1 :  W1 2.73  >  S2 1.69  >  S1 1.36  >  S3 0.48
T/q  :  W1 0.882 >  S2 0.540 >  S1 0.470 >  S3 0.225      (monotone, 4/4)
```

*Reported as max-over-sample for every falsification and as a distribution
otherwise, per the pre-registered MISS-2 guard item 3.*

---

## D3 — THE RAZOR VERDICT, EXACT ARITHMETIC

Razor shape (round 33 PR-5): `R = k = 2^40`, `rho = 2^34`, `r = R-rho`,
`r/R = 63/64`, rate-half so `n = 2R = 2^41`, `D ⊂ F_q`, `q >= n`. All
integers below from `e3_results.txt`.

### D3.1 The count, stated as a count

```
dim Gr(2,R)          = 2R-4              = 2,199,023,255,548
dim{p* <= p}         = 3p-4              (p projective params for P*, 2(p-2) for Gr(2,p))
codim{p* <= p}       = 2R-3p

  p = 2rho  = 34,359,738,368   : dim =   103,079,215,100 , codim = 2,095,944,040,448 = 61·2^35
  p = R/2   = 549,755,813,888  : dim = 1,649,267,441,660 , codim =   549,755,813,888 = 2^39
  p = ceil(2R/3) = 733,007,751,851 : codim = -1  (everything: the generic value)
```

**NAIVE-COUNT CAVEAT, quoted as pre-registered (R0-d, zero-power #3,
round 33's own zero-power #4 precedent).** These are parameter counts. They
can fail three ways: a positive-dimensional locus over `F̄` can have no
`F_q`-points; the intersection with column-farness can be non-transverse;
the parameterisation `(P*, V) ↦ V` can be non-injective or the locus
reducible. The count therefore **cannot** carry an emptiness verdict, and
95.3% codimension at `p = 2rho` is fully compatible with
`~q^{103,079,215,100}` witnesses. I answer by witness instead, which is
immune to all three failure modes.

### D3.2 WITNESS A — closed form, non-squarefree `P* = x^{2rho}`

```
y_0(m) = 1 if m = 2rho-1 = 34,359,738,367 , else 0
y_1(m) = 1 if m =  rho-1 = 17,179,869,183 , else 0        (0 <= m < R)
```

*Verification, four lines, no genericity, any `F_q`, any `D`.*
`M_r(y_0)` has rows `s = 0..rho-1` equal to the standard basis vectors
`e_{2rho-1-s}` (positions `rho .. 2rho-1`); `M_r(y_1)` gives
`e_{rho-1-s}` (positions `0 .. rho-1`). Hence the stacked matrix has rank
exactly `h_r = 2rho`, and `K_0 = {sigma : sigma_j = 0, j < 2rho} =
x^{2rho}·F[x]_{<=r-2rho}`, `dim K_0 = r+1-2rho = 1,047,972,020,225`. The
same computation in every degree `i < 2rho` forces `sigma = 0`, so
**`p* = 2rho = 34,359,738,368` exactly**. Every element of `K_0` is
divisible by `x^{2rho}`, hence has a repeated root, hence is **not** in
`D_r(D)`: the pencil is **column-far unconditionally**. Realisable as a
received pair because the syndrome matrix `(v_x x^m)_{m<R, x∈D}` has rank
`R` (any `R` columns are a scaled Vandermonde), so the syndrome map is
**surjective** onto `F_q^R`.

Checked at four cells, `q = 11,13,17`: `p* = 2rho`, `h_r = 2rho`,
`dim K_0 = r+1-2rho`, column-far, and the low generator **literally
constant across all `q` slopes** (`distinct = 1`), 4/4
(`e2_results.txt`).

### D3.3 WITNESS B — squarefree `P*`, so FG3/FG4 apply verbatim

Let `P_1` be **irreducible of degree `rho = 2^34`** over `F_q` (they exist:
`#irred = (q^d - O(q^{d/2}))/d > 0`), `P_2` any squarefree degree-`rho`
polynomial coprime to `P_1`; let `y_0`, `y_1` be their impulse responses
(`0,...,0,1` then the recurrence), truncated to length `R`.

*Verification, no genericity.* The leading `rho x rho` Hankel block of an
impulse response is the anti-identity, so `rank M_i(y_j) = rho` for
`rho <= i <= R-rho = r`, giving `Ann(y_j)_i = P_j·F[x]_{<=i-rho}` exactly
(containment plus equal dimension `i+1-rho`). `P_1, P_2` coprime, so
`Ann(V)_i = P_1P_2·F[x]_{<=i-2rho}`: **`p* = 2rho`** and
`K_0 = P*·F[x]_{<=r-2rho}` with `P* = P_1P_2` **squarefree** of degree
`2rho`, `dim K_0 = 1,047,972,020,225`. Every element of `K_0` is divisible
by the irreducible `P_1` of degree `2^34 >= 2`, which has **no root in
`D ⊆ F_q`**, so no element is a product of distinct linear factors over
`D`: **column-far unconditionally**.

This is an FG pencil in round 33's exact sense, so its FG3 normal form
`M̄(gamma) = W·diag(c(gamma))` (a `2^34 x 2^35` scaled Vandermonde) and its
FG4 key equation `C_gamma·sigma ≡ h (mod P*)`, `deg h <= m_Q-1`, hold
verbatim, with

```
m_P = r+1-p = 1,047,972,020,225 ,  m_Q = p-rho = 17,179,869,184 = rho (saturated)
deg Q' = R+1-p = 1,065,151,889,409 ,  m_P+m_Q = r+1-rho = 1,065,151,889,409
```

Checked at four cells, `q = 11,13,17`: `p* = 2rho`, `K_0` principal with
`deg gcd(K_0) = 2rho`, column-far, 4/4; and the negative control B'
(`P_1` replaced by a `D`-split-squarefree factor, everything else
identical) is column-**close**, 4/4 (`e2_results.txt`).

### D3.4 Why the intersection with column-farness is free, in numbers

```
log2 C(n, 2rho)              =  2.553398e+11      [float, n·H2(2rho/n)]
log2 q^{2rho}   at q = 2^41  =  1.408749e+12
log2 (fraction of degree-2rho P* that are D-split-squarefree) = -1.153410e+12
```

So on the low-`p*` locus, column-farness excludes a `2^{-1.15e12}`
fraction of the `P*` choices and nothing else. There is no transversality
question to get wrong, which is the second reason the naive count's
weakness does not bite here.

### D3.5 The first-moment parameters, and why they are useless here

```
log2 C(n,r) = n·H2(63/128) = 2.198636e+12          [float; r/n = 63/128 exactly]
q = 2^41 :  log2 mu_1 = log2 C(n,r)/q^{rho}  = 1.494261e+12
            log2 mu_2 = log2 C(n,r)/q^{2rho} = 7.898867e+11
column-farness first-moment threshold:  log2 q = n·H2(r/n)/(2rho) = 63.9887
```

At `q = 2^41` both are astronomically `> 1`: the random model says every
slope is bad *and* that column-far pairs are exponentially rare. The second
prediction is exhibited false by A and B. The threshold is a clean closed
form — `q_crit ≈ 2^{64}` independent of `R`, because
`n·H2(r/n)/(2rho) = 64·H2(63/128)` at this shape — so the razor question
changes character at `q ≈ 2^64` and every heuristic quoted at `q = 2^41`
must be re-derived above it. **Flagged as heuristic; zero power claimed.**

---

## D4 — VERDICT, LB1 CROSS-CHECK, RESIDUALS

### D4.1 Verdict

**FG NONEMPTY at razor shape (witnesses A and B, D3.2/D3.3).** Therefore:

- The brief's IF-NO branch does not fire. **The fixed-generator branch
  does not close negatively and R-KER is not the sole far-CA residual.**
- **R-FG becomes a real budget question** with live razor-scale
  coordinates: bound `#{gamma : C_gamma·sigma ≡ h (mod P*) for some
  sigma ∈ D_r(D), deg h <= 2^34 - 1}` for a line `{C_0+gamma C_1}` in
  `F[x]/(P*)`, `deg P* = 2^35`, `P*` with an irreducible factor of degree
  `2^34`. Witness B supplies `P*`; the free parameters are the `c_i`.
- `B_ca^far(k+2^34) < 2^128`: **NO.** No stratum is added to the covered
  set and no bound is proved.

### D4.2 LB1 consistency — predicted, then measured

Predicted (R0-f) before measurement: `dim K_0 = 0 ⟺ Ann(V)_r = 0 ⟺
p* > r`, a tautology, so LB1 pencils sit at the **top** of the `p*`
spectrum, opposite FG; sharper, `p* = r+1` in `>= 90%` of them at LB1's
own cell `RS[F_11,{0..6},2]`, `r=3`, `R=5`, `rho=2`
(`background/nodes/rate_half_ca_hankel_minimal_index_budget/statement.md:91`).

Measured (`e1_results.txt`, part D, 4000 pencils): `dim K_0 = 0` in
**3591**, of which column-far **3591/3591**; `p* = 4 = r+1` in
**3591/3591 (100%)**; `p* | dim K_0 > 0` is `2:1, 3:408`; and the
tautology check `dim K_0 = 0 ⟺ p* > r` has **0 violations in 4000**.
**R0-f HIT.** LB1 is *generic*, not special: `r+1 = 4 = ceil(2R/3)`.

The falsifier could bite only if I claimed a bound below `T = r+1`
somewhere LB1 lives. I claim no bound, so it cannot fire; I record that
honestly rather than as a pass.

### D4.3 Residuals handed forward

- **R-PSTAR: RESOLVED, POSITIVELY.** Column-far razor pencils with
  `p* <= R/2` exist; so do FG ones (`p* = 2rho = R/32`). Two explicit
  witnesses, one with `P*` squarefree. The residual should be retired and
  replaced by R-FG-RAZOR below.
- **R-FG-RAZOR (sharpened).** R-FG, now with a named instance family:
  `P* = P_1P_2` (`P_1` irreducible of degree `2^34`), `V ⊂ IS(P*)`
  2-dimensional with stacked rank `2^35`. Measured `T` at reachable cells
  is `1..q` and tracks `mu_1 = C(n,r)/q^rho`; at the razor
  `log2 mu_1 = 1.49e12`, so every heuristic says `T = q` and none of them
  has any power. **Unknown at the razor.**
- **R-PSTAR-INTERMEDIATE (new).** The band `2rho < p* <= R/2` — at the
  razor `2^35 < p* <= 2^39`, sixteen octaves — carries a generically fixed
  generator with a **non-principal** `K_0`. The FG3 descent still applies
  (D1.4) but the FG2 column-farness equivalence does **not**: column-farness
  there is a genuine extra condition on `K_0 / P*·F[x]`, measured to hold
  anyway at 5/5 constructed instances. Nobody has looked at this band; it
  is invisible at every round-33 cell.
- **R-KER, R-DEEP, R-LINEDEGREE** unchanged.
- **New open question, cheap:** is `mu_2 > 1` (i.e. `q < 2^{63.99}`) at the
  official candidate? If yes, the razor's column-far locus is a
  measure-zero object that only construction can reach, and every random
  model in the far-CA lane is void there.

---

## FLAGS FOR THE COORDINATOR (AUDIT-AND-DRAFT — no surgery applied)

1. **`critical/nodes/rate_half_band_crossing_location/statement.md:3059-3061`
   carries the false equivalence.** It banks R-PSTAR as "*does ANY
   column-far razor pencil have `p* <= R/2`? If no, FG is empty at the
   razor and R-KER is the SOLE far-CA residual*". The parenthetical
   inference is invalid: FG requires `p* <= 2rho = R/32`, strictly stronger
   than `p* <= R/2` (D1.1(ii), unconditional; D1.3, five exhibited
   counterexamples). Suggested repair: state R-PSTAR with the `2rho`
   bracket, and record that it is now **answered YES** by witnesses A and
   B. **I flag; I do not apply.**
2. **Same node, same block (`:3057`): "on FG the measured `T = q` kills
   `T <= rho`, `T <= p`, `T <= r+1`" should be narrowed.** `T <= rho` and
   `T <= p` are dead everywhere I measured; `T <= r+1` survives at 2 of my
   4 cells (S1 tight at 9 = 9, S3 at 9 < 14). The killing tracks
   `mu_1 = C(n,r)/q^rho`, not FG membership. The *conclusion* (all three
   are dead as universal bounds) stands; the *reason* as banked does not.
3. **Round 33's FG3/FG4 are stated on FG and are true more widely** — they
   need only `p* <= r` with `P*` squarefree, which held in 1586/1586
   column-far random pencils across four cells (D1.4). If the coordinator
   wants the strongest form banked, this is a free widening; note the
   `dim Ann(V)_{p*} = 3p*+1-2R` non-uniqueness caveat.
4. **`p*` is now repository prose** (`crossing_location:3047-3064`) but not
   a node object; the codimension law `codim{p* <= p} = 2R-3p` and the
   equivalence `dim K_0 = 0 ⟺ p* > r` are additive and calibrated
   (D2.2, D4.2) and would slot into a node cheaply.

---

## PREDICTIONS vs OUTCOMES

| | registered | outcome |
|---|---|---|
| R0-a | P(FG nonempty at razor) gut 0.55 / post-count 0.93 | **HIT — nonempty, two explicit witnesses** |
| R0-b | `p* <= R/2` at a wide cell: 0.95 by construction / 0.10 by sampling | **BOTH HIT** — construction 5/5 instances; sampling 0 of 26,000 |
| R0-c | `codim{p* <= p} = 2R-3p`, tolerance ±0.5 at codim 1–2 | **HIT — 10 points, codim 1–5, max deviation 0.090** |
| R0-d | P(dimension count decisive) 0.35 | **HIT as registered** — verdict is by witness; the count would have misled (miss 7) |
| R0-e | P(the brief's "equivalently" is wrong) 0.85 | **HIT — it is wrong, factor 16 at the razor; the banked node repeats it** |
| R0-f | `dim K_0 = 0 ⟺ p* > r`; `p* = r+1` in `>= 90%` at LB1 | **HIT — 3591/3591 (100%), 0 tautology violations in 4000** |
| R0-g | modal `p* = ceil(2R/3)` in `>= 90%` at every wide cell | **5/6 HIT, 1 hairline MISS** (L1: 0.89933) |
| R0-h | at least one constructed column-far FG pencil with `T > 0` | **HIT** — construction C gives `T` in 1..13; but witness A has `T = 0` at S3 (miss 4) |
| R0-i | seven exact razor integers | **7/7 HIT**, all reproduced exactly in `e3_results.txt` |
| MISS-2 guard | never infer emptiness from a census; label mean vs max | **HELD** — the census saw `p* <= R/2` zero times and I concluded nothing from it; every `T` used against a bound is a max |
| ZP-1..5 | five zero-power declarations | **ALL HELD**; ZP-2 (round-33 cells cannot separate FG from `p* <= R/2`) **verified**: all have `2rho >= ceil(R/2)` |

---

## CATCH-24A SUBTRACTIONS (own-repo greps before every novelty claim)

1. `grep -rn "common apolar" critical/nodes background/nodes` → one hit,
   `background/nodes/rate_half_ca_hankel_exceptional_root_charge/claim_contract.md:11`,
   unrelated (it cites the minimal-index theorem's common apolar form).
   **`p*` as an invariant is banked as round-33 prose** at
   `critical/nodes/rate_half_band_crossing_location/statement.md:3047-3064`
   and in the FALSE-marker at `:1004`. I subtract: the invariant, its
   generic value, `p* + p_gen <= R`, the FG stratum, FG2, the scaled
   Vandermonde, the key equation, `(MI1)` restored / `(MI2)` blocked are
   **all round 33's, not mine.**
2. `grep -rlnE "2R *- *3p|2R-3p|3p *- *4|codim.*apolar"` over
   `critical/nodes background/nodes notes` (with `--exclude-dir` guards)
   → **zero hits**. The codimension law `dim{p* <= p} = 3p-4`,
   `codim = 2R-3p`, and its ten-point calibration are additive.
3. `grep -rlnE "scaled.Vandermonde|scaled Vandermonde"` → `crossing_location`
   (round 33's bank) and
   `background/nodes/rate_half_bivariate_top_vandermonde_schur_reduction/`
   (a *different* object: a `4m+1`-rank diagonally scaled Vandermonde in
   the bivariate lane, statement.md:29). No collision.
4. `grep -rlnE "dim K_0 = 0|dim K_0 == 0"` → **zero hits**; the equivalence
   `dim K_0 = 0 ⟺ p* > r` is additive.
5. `grep -rn "explicit column-far"` → two hits: LB1's small-scale pencil
   (`minimal_index_budget/statement.md:91`, `RS[F_11,{0..6},2]`, `r=3`)
   and `crossing_location:637`. **No razor-scale explicit column-far
   witness exists in the repo**, and neither banked witness is low-`p*`.
6. `grep -rlnE "covering radius|first moment.*column"` → **zero hits**; the
   first-moment threshold `q_crit = 2^{n·H2(r/n)/(2rho)} ≈ 2^{63.99}` and
   the observation that the random model forbids what witnesses A and B
   exhibit are additive.
7. **Genuinely additive this round:** the unconditional inequality
   `h_r <= min(p*, 2rho)` and the consequent **FG ⟹ `p* <= 2rho`**; the
   refutation of the brief's/node's equivalence; the intermediate stratum
   `2rho < p* <= R/2` with five exhibited instances; the codimension law
   and its calibration; witnesses A and B at razor shape with elementary
   proofs; the observation that column-farness is *free* on the low-`p*`
   locus (with the `2^{-1.15e12}` fraction); the extension of FG3's descent
   to all `p* <= r`; `dim K_0 = 0 ⟺ p* > r` with the LB1 measurement; the
   `mu_1` ordering law for `T` and the `q_crit ≈ 2^{64}` threshold.

---

## ZERO-POWER DECLARATIONS

1. **No razor-scale computation exists here.** `q <= 17`, `R <= 16`,
   `rho <= 3`. Every razor statement is closed-form arithmetic
   (`e3_results.txt`) plus the elementary verifications in D3.2/D3.3, which
   are scale-free by construction. Pre-registered.
2. **The census has zero power on existence.** `p* <= R/2` was seen zero
   times in 26,000 uniform samples at wide cells and I conclude **nothing**
   from that; the codimension law (D2.2) explains why it must be zero at
   reachable `q`. Pre-registered MISS-2 guard, item 1.
3. **Codimension bounds density, never emptiness.** `codim = 2.096e12` at
   `p = 2rho` coexists with a locus of dimension `1.03e11`. Item 4 of the
   guard.
4. **The dimension count is naive.** Stated as a count, never as a verdict
   (D3.1); the verdict is by witness.
5. **`T` numbers are saturation artefacts** at every cell I can reach
   (`mu_1 ∈ [0.48, 2.73]`), refute candidate bounds and support none. The
   `mu_1` ordering law is a heuristic with 4 data points, offered as an
   ordering only, not a fit.
6. **`p_gen` inherits round 33's low bias** (its miss 8): I take a per-slope
   minimum, so exceptional slopes drag it down. This is why "distinct
   generators" is 1–4 on FG rather than 1, and I report the *modal-generator
   coverage* alongside it rather than a bare "fixed / not fixed".
7. **Two-field (in fact three-field: `q = 11, 13, 17`) confirmation** for
   every structural claim; every construction verified at 4 cells; the
   B/B' pair gives the two-directional confirmation for FG2.
8. **No claim about `char F`**, about `q` at razor scale beyond `q >= n`, or
   about `P*` non-squarefree inside FG3/FG4 — witness A is deliberately kept
   separate from the squarefree witness B for exactly that reason.
9. **`P*` is not unique** when `3p* > 2R+1` (`dim Ann(V)_{p*} = 3p*+1-2R`);
   the FG3 descent is by a *choice* of `P*` and I do not claim canonicity.

---

## COMPLIANCE

Brief read first, `CONSTRAINTS.md` second, then the **two named anchors
only** (`notes/pilots_20260811/rh_moving_kernel/REPORT.md`,
`background/nodes/rate_half_ca_hankel_split_pencil_equivalence/statement.md`),
and **nothing else** before the `## Pilot registrations` block — R0-a..i
with numeric windows, the MISS-2 mean-vs-max guard, five zero-power
declarations and the compute plan — was appended to `PREREG.md` with the
Edit tool, before any grep, any `ls` beyond my own directory, and any
interpreter invocation. No registration was edited afterwards. The
registration block discloses honestly that an in-head parameter count
preceded it, and records both a `gut` and a `post-count` number wherever
they differ, so the scoring lands on the right one.

**COMPUTE LAW: 6 interpreter invocations, 6 under `tools/ramguard`, ZERO
breaches, zero bare `python3` for any purpose.** From the repo root, with a
literal `--` and an explicit `RAMGUARD_TIMEOUT`: (1) `e1_census.py`
*local*, `RAMGUARD_TIMEOUT=280` — crashed in part B on an empty-polynomial
gcd edge case (disclosed, not silently re-run); (2) `e1_census.py` *local*,
280s, complete after the one-line Edit fix; (3) `e1b_codim.py` *local*,
290s; (4) `e2_construct.py` *local*, 290s; (5) `e2b_extend.py` *local*,
290s; (6) `e3_razor.py` *tiny*, 55s. Stdlib only (`sys`, `random`, `math`,
`fractions`, `itertools`). **All file edits went through Edit/Write**; no
interpreter was used to patch, probe, or no-op. No Modal, no network, no
git, no subagents.

**RAM DISCIPLINE:** file-at-a-time; **`dag.json` never opened**; the two
long node files read only through bounded windows (90 and 22 lines) plus
line-numbered greps; results checkpointed to `e1_results.txt`,
`e1b_results.txt`, `e2_results.txt`, `e2b_results.txt`, `e3_results.txt`
after every emit; no run exceeded ~90s or approached the memory ceiling.

**QUARANTINE:** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` never opened at
any line; **no `r34_*` sibling directory was read, listed, or opened**; no
path containing `prize-codex-` was touched. All greps but one were scoped
to `critical/nodes` and `background/nodes`. **Disclosed deviation:** one
grep (the codimension-novelty search) included `notes` in its search path
with search-level `--exclude-dir` guards on `prize-codex-work`,
`pilots_20260802` and four *guessed* `r34_*` names; it returned **zero
hits**, so no sibling content was surfaced, but because I never listed
`notes/pilots_20260811` I cannot certify the guessed exclude list covered
every sibling name. Every other recursive grep used search-level
`--exclude-dir` or was confined to the two node trees.

**WRITE SCOPE:** every write is inside `notes/pilots_20260811/r34_pstar/`
— `PREREG.md` (registrations appended), `e1_census.py`, `e1_results.txt`,
`e1b_codim.py`, `e1b_results.txt`, `e2_construct.py`, `e2_results.txt`,
`e2b_extend.py`, `e2b_results.txt`, `e3_razor.py`, `e3_results.txt` (and
this `REPORT.md`, which the harness refused — returned as text instead).
**No `dag/`, `critical/`, `background/`, `nodes/` or `tools/` file was
edited**; no git operation of any kind; no scratch file outside the pilot
directory; no banked script was copied or run (all four experiment scripts
are fresh implementations against the conventions in the split-pencil node,
cross-checked against round 33's published numbers at the shared cell).
AUDIT-AND-DRAFT respected: **no node surgery applied**; the two corrections
this round forces at
`critical/nodes/rate_half_band_crossing_location/statement.md:3057-3061`
are flagged for the coordinator, not made.
