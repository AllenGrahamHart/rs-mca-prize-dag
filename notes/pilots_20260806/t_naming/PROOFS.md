# PROOFS — the t-NAMING COLLISION (round 17, pilot `t_naming`)

Opus 5, 2026-08-06. Replay:

```
tools/ramguard tiny -- python3 notes/pilots_20260806/t_naming/verify.py
```

→ **68 checks, 0 FAIL**, digest `T_NAMING_VERIFY_ALL_PASS` (log: `VERIFY_LOG.txt`).

Every load-bearing statement is quoted VERBATIM with `file:line`.
Pre-registrations U1–U9 were appended to `PREREG.md` before any script ran.
§1.5, §4.5 and §6 rest on evidence found by a repo-wide sweep that landed
**after** U1–U9 were locked; that provenance is flagged wherever it matters.

---

## 0. The source surfaces, verbatim

**(A) The XR side.** `background/nodes/xr_radius_arithmetic/proof.md:24-27`:

> - **FM scale (banked Lemma FM1, exact).** For a row `(n, k, q)` at exact
>   agreement `A`, with `t = A - k`, `j = n - A`, the aligned-support mean is
>   `E[X] = C(n, j)(1 - q^{-t}) q^{1-t} <= C(n, j) q^{1-t}`. Gate
>   `B* = floor(q / 2^128)`, so `log2 B* = L - 128` with `L := log2 q`.

`background/nodes/xr_radius_arithmetic/proof.md:41-43`:

> ```
> t* = min { t : E[X] <= B* }
>    = min { t : log2 C(n, n-k-t) + (1 - t)L <= L - 128 }
>    = min { t : t * L  >=  log2 C(n, n-k-t) + 128 }.                        (T*)
> ```

`background/nodes/xr_radius_arithmetic/proof.md:33-34`:

> - **Prize convention.** `L = log2 q = 255.9` (the "`2^{255.9}`" prize row of the
>   budget audit), `n = 2^41`, `k = rho n`.

`background/nodes/xr_radius_arithmetic/proof.md:54-58`:

> ```
> rate    t*              s* = t* - 1
> 1/2     8,592,912,739   8,592,912,738
> 1/4     7,014,660,390   7,014,660,389
> 1/8     4,722,556,392   4,722,556,391
> 1/16    2,943,177,800   2,943,177,799
> ```

**(B) The F2 side.** `notes/pilots_20260806/f2_tq_pin/PROOFS.md:158-160`:

> `t = |Lambda|`, the number of power-sum (Newton) conditions
> `p_l(S) = 0`, `l in Lambda`, imposed on a block `S ⊆ mu_n`. It is defined
> once, globally, not per rung

`notes/pilots_20260806/f2_tq_pin/PROOFS.md:170-176`:

> Each condition `p_l(S) = 0` is **one equation over the field in which the
> power sums live**, costing `log2 q` bits; the space of blocks carries `n`
> bits. The window of `t`-null blocks is empty iff `q^t > 2^n`, i.e.
>
> ```
>                         t · L  >=  n .                                (C)
> ```

`notes/pilots_20260804/f2_opening/PROOFS.md:19-20`:

> A **frequency** is `f(x) = sum_{l in Lambda} C_l x^l`, `C_l in F_{p^2}`,
> with character `chi_c(x) = Tr(f(x)) in F_p`. The census term is

`notes/pilots_20260804/f2_opening/PROOFS.md:27-29`:

> **Class K1** = the parity-pure class: `Lambda` consists of ODD exponents
> only (`f2_deployed_windows/REPORT.md:41`). *Not* the `k=1` of
> `critical/nodes/f2_k1_contraction_theorem` — a live naming collision.

**(C) The mca_floor side.** *(Path note: the brief cites
`critical/nodes/rate_half_cyclic_simple_pole_mca_floor/`; that directory does
not exist. The node lives in `background/nodes/`.)*
`background/nodes/rate_half_cyclic_simple_pole_mca_floor/statement.md:10-17`:

> ```text
> n = 2^41,                 k = 2^40,
> c = 2^22,                 d = 2,048,
> sigma_max = dc+c-1
>           = 8,594,128,895,
> C = RS[F,D,k],
> q = |F| < 2^256,
> ```

`.../statement.md:52-56`:

> Equivalently, both CA and MCA are prize-unsafe at every agreement
>
> ```text
> k+sigma,       1 <= sigma <= sigma_max.                  (SP2)
> ```

`.../statement.md:63-71`:

> In particular
>
> ```text
> sigma*=8,592,912,738 < sigma_max,
> ```
>
> so the previously conjectured safe point at `k+sigma*+1` is unsafe. The
> fixed-point formulation of `rate_half_band_closure` is therefore refuted;
> the remaining rate-half task must locate a later, field-dependent adjacent
> crossing.

---

## 1. (N1) The two definitions, formalized side by side

### 1.1 The table

|  | **`t_F2`** | **`t_XR`** |
|---|---|---|
| **Definition** | the **largest Newton index** in `Lambda`, under the `"odd l <= t"` convention — **not** `|Lambda|`; see §1.5 | `A - k`, the agreement excess of a received word over the RS dimension |
| **Index set** | **FREQUENCY space**: exponents `l` of `f(x) = sum_{l in Lambda} C_l x^l` | **COORDINATE space**: the `A` points of `D` where a codeword agrees |
| **Condition count** | `|Lambda| = ceil(t/2)` in class K1 (odd only) | `t` itself (the syndrome-space dimension, `fm1/statement.md:9`) |
| **Provenance** | `f2_opening/PROOFS.md:19,27-29`; `f2_sl1b/PROOFS.md:8-12` | `xr_radius_arithmetic/proof.md:24-25` |
| **Row** | F2 window row `(n, p, rung j)`; `m_j = 2^{22+j}` pairs | corridor row `(n, k, q)` at exact rate `rho = k/n` |
| **Governing formula** | (C) `(#conditions)·L >= n` | (T*) `t·L >= log2 C(n, n-k-t) + 128` |
| **Rate dependence** | **NONE** — no `k` appears in (C) | **STRONG** — `k = rho n` enters the binomial |
| **Consumers** | LEMMA 3 gloss, THEOREM A/B, the `|K1|` seam | corridor table, `s* = t*-1`, `averaged_xr`, `mca_floor` |

The two live on **different index sets** of sets of the same size `n`. Both are
integers in `[0, n]`, both get multiplied by `L`, and both are called `t`.

### 1.2 There is no repo-level naming ledger that covers them

`critical/nodes/noncontain_degeneracy/statement.md:9` already disambiguates a
`t`-collision — and `t_F2` is **not in it**:

> Disambiguation of the three t's: t_denom (denominator degree in def:residue, 1<=t<=r), T_slack (monomial exponent in x^{k+T} + z x^k), t_win (syndrome window t = A-k, the exact-agreement bucket) — t_win is a bucket parameter orthogonal to t_denom.

So the repo maintains a partial ledger of three `t`s, of which only `t_win`
(`= t_XR`) is one of ours. Counting `t_F2` and the `t*_eff` of §1.6, the repo
carries **at least six** distinct symbols in the `t` family.

### 1.5 CORRECTION TO THE BRIEF: `t_F2` is **not** `|Lambda|`

The brief and `f2_tq_pin` residual 1 both define `t_F2 := |Lambda|`, from
`f2_tq_pin/PROOFS.md:158`. **Five independent sources contradict it**, all
reading `t` as the max index with `Lambda = {odd l <= t}`:

`notes/pilots_20260806/f2_sl1b/PROOFS.md:8-12`:

> Notation is `f2_opening/PROOFS.md`'s. `F_q = F_{p^k}` is the ambient
> field, `k = [F_q : F_p]`; `R` = the number of exponents in a run of
> **consecutive odd** exponents contained in `Lambda`; under the
> `"odd l <= t"` reading `R = |Lambda| = ceil(t/2)`
> (`f2_sl1_powersums/PROOFS.md:8-10`).

`notes/pilots_20260804/f2_opening/PROOFS.md:327-329`:

> - Theorem A/B require `Lambda ⊇ {1,3,...,2m-1}`. At the official row
>   (`m_j = 2^{22+j}`, `t ~ 7e10`) that is **rungs 1..13**. Rungs 14-16 are
>   **NOT** discharged;

(`Lambda ⊇ {1,3,...,2m-1}` requires `t >= 2m-1` **only** if `t` is the max
index — which is exactly the test `f2_tq_pin` coded as `t >= 2 m_j - 1`.)

`notes/pilots_20260802/f2_deployed_windows/selection.py:43,50,54`:

> `T_CONDITIONS = 70_000_000_000             # t ~ 7e10 (F2_NEWTON_EMPTY_EXTREMES)`
> `    even_l = T_CONDITIONS // 2`
> `        codim = min(m_j, even_l)`

(the operational code halves `t` to get a count — `t` is a *range*.)

`SOL_TARGET_3_OFFICIAL_EXTRAS_FLOOR.md:19-23`:

> Call an index
> i P-FREE if p does not divide i, and let t* = #{p-free i <= t} (the
> EFFECTIVE conditions; char-divisible indices are redundant:
> p_{pi} = (p_i)^p). SUB-BALANCE HYPOTHESIS (required):
> |B0|^{t*} >= 2^N.

**The reductio (S18).** `t = |Lambda|` and `|Lambda| = ceil(t/2)` force
`t = ceil(t/2)`, whose only positive solution is `t = 1`. The two banked
readings are inconsistent for every `t >= 2`.

**Why `f2_tq_pin` was misled.** In the DLI lane the two readings genuinely
coincide, because there `Lambda` is *all* indices `<= t`, not the odd ones —
`background/nodes/dli_official_support_forcing/proof.md:27`:

> this is exactly the pinned `ell`, and `sum_j L_j = (2^33 - 1) + 1 = 2^33 = t`.

That degeneracy (`#{r <= t} = t`) makes `t = |Lambda|` *true in DLI* and
*false in K1*, where the parity restriction halves the count.

**Consequence for the balance (C).** (C) charges `L` bits per **condition**,
i.e. per element of `Lambda`. Under the K1 reading it therefore reads
`ceil(t/2)·L >= n`, giving

```
        t_F2  =  2n / L        (degree reading)                    (C')
   vs   t_F2  =   n / L        (count reading, f2_tq_pin's)        (C)
```

This factor 2 is **decisive** for three downstream verdicts (§2.7, §3.1, §6).

### 1.6 A third `t*`, unrelated to the corridor edge

`SOL_TARGET_3_OFFICIAL_EXTRAS_FLOOR.md:34-35`:

> At every row satisfying the hypotheses with official shape
> (N ~ 2^41, p ~ 2^31, |B0| = p^k, t* ~ 7e10 — and any scaled family

Here `t* ~ 7e10` is the **effective condition count** `#{p-free i <= t}`, not
the corridor edge `8.59e9`. `SOL_TARGET_3C_PRIMITIVE_CENSUS.md:15-16` renamed
it `t*_eff`; the `_3_` file did not. Same glyph `t*`, two objects, an order of
magnitude apart, and the `_3_` one carries the load-bearing sub-balance
hypothesis.

---

## 2. (N2) The identification is **REFUTED**. A common *schema* survives.

### 2.1 The coordinator's candidate, tested

The brief's candidate: *"both are forced to `n/L` at leading order by the SAME
counting balance … so the identification is an instance of one balance
identity."* **Half right; the decisive half wrong.** They are instances of one
*schema*, not of one *balance*: the schema has two free inputs and the two
`t`'s differ in both.

### 2.2 THEOREM (UFMB — the unified first-moment balance)

> Let `E` be an ensemble with `|E| = N`, let each object survive a prescribed
> set of `t` independent `F_q`-conditions with probability `q^{-t}`, and let
> `2^{-G}` be the target for the expected number of survivors. Then
> ```
>     E[# survivors] = N q^{-t} <= 2^{-G}   <=>   t·L >= log2 N + G .   (UFMB)
> ```
> `f(t) := tL - log2 N(t) - G` is strictly increasing on the admissible range,
> so the critical `t` is the unique integer crossing.

*Proof.* Linearity of expectation over `E`, then `log2`. Monotonicity: `tL`
rises by `L` per step while `log2 N(t)` is non-increasing (constant for
`N = 2^n`; for `N = C(n, n-k-t)` the argument moves below `n/2`, verbatim the
argument at `xr_radius_arithmetic/proof.md:47-49`). ∎

Both `t`'s are instances, with the instantiation forced by their own sources:

| | ensemble `E` | `log2 N` | gate `G` | critical `t` |
|---|---|---|---|---|
| `t_F2` | all blocks `S ⊆ mu_n` | `n` | `0` | `n/L` (or `2n/L`, §1.5) |
| `t_XR` | all `j`-supports, `j = n-k-t` | `log2 C(n, n-k-t)` | `128` | (T*) |

The `t_XR` row is a *rewriting*, not a modelling choice: from `proof.md:24-27`,
`E[X] <= C(n,j) q^{1-t} <= B* = q·2^{-128}` cancels one factor `q` per side,
leaving exactly `C(n,j) q^{-t} <= 2^{-128}`. Verified at **S6.b**.

### 2.3 COROLLARY (exact criterion)

```
    t_F2 = t_XR   <=>   Delta := n - log2 C(n, n-k-t) - 128 = 0 ,
    and in general      t_F2 - t_XR = Delta / L  (up to one rounding step).
```

Verified at all four rates (**S4**): predicted `Delta/L` matches measured
`n/L - t*` to within `0.03 / 0.71 / 0.51 / 0.67`, far under the one-step
tolerance `L = 255.9`.

### 2.4 The refutation: `Delta` is enormous away from rate 1/2

`Delta` is the entropy gap between the **full power set** `2^n` and the
**binomial shell** `C(n, n-k-t)`. With `tau = t/n`:

```
    log2 C(n, n-k-t) = n·H2(rho + tau) + O(log n) ,
    so   t_XR = (H2(rho+tau)·n + 128)/L ,   while   t_F2 ∝ n/L .
```

The identification demands `H2(rho + tau) = 1`, i.e. `rho + tau = 1/2`. Since
`tau ~ 0.0039 << 1`, that is **rate 1/2 and nothing else**. Measured (**S2/S3**):

| rate | `t_XR / (n/L)` | deviation |
|---|---|---|
| 1/2 | `0.999956` | **`-0.0044%`** |
| 1/4 | `0.816295` | **`-18.37%`** |
| 1/8 | `0.549563` | **`-45.04%`** |
| 1/16 | `0.310253` | **`-65.75%`** |

A quantity cannot be `18%`, `45%` and `66%` away from itself. **The
identification is REFUTED.** U1's falsifier did not trigger (**S3.F**).

### 2.5 The mechanism at rate 1/2: the central binomial

de Moivre–Laplace at `rho = 1/2`:

```
 log2 C(n, n/2 - t) = n - (1/2)log2(pi n/2) - 2t^2/(n ln2) - (4/3)t^4/(n^3 ln2) - ...
```

so the **exact error term** is

```
    Delta(1/2) = 2t*^2/(n ln2) + (1/2)log2(pi n/2) - 128 + (4/3)t*^4/(n^3 ln2) + ...
               = 9.688565e7 bits                                          (S4.2)
```

Quadratic-only closed form: `9.688466e7`, rel `1.02e-5` (**S5**).
Quadratic+quartic: rel `< 1e-7` (**S5.q**) — **the error term is closed;
nothing is unexplained.** Relative size, with `t* ~ n/L`:

```
    Delta/n  ~  2/(L^2 ln 2)  =  4.406198e-5  =  0.0044%          (S6)
```

**This closes a loop.** `f2_tq_pin` CATCH-4 measured the banked "within ~2% of
the counting threshold" as really `0.0044%`. That number is not empirical: it
is **exactly `2/(L^2 ln 2)`**, the second-order entropy deficit of the central
binomial — a Stirling correction, not evidence of an identity.

### 2.7 …and under the F2 lane's OWN reading, they differ by a **factor 2** even at rate 1/2

§1.5 shows the F2 lane reads `t` as the max index, so (C') gives
`t_F2 = 2n/L`. Then (**S17**):

```
    t_F2 = 2n/L = 1.71866e10  =  2.00009 x t*       ->  a 100.0% gap AT RATE 1/2
```

**So the celebrated `0.0044%` agreement is an artefact of the wrong
normalization.** Under the count reading (`f2_tq_pin`'s, which §1.5 refutes)
the two agree to `4.4e-5` at rate 1/2; under the reading the F2 lane's own
sources and code use, they are a clean factor of 2 apart. The identification
fails at **all four** prize rates, not three.

### 2.8 What is and is not proved

`t_F2` and `t_XR` are **genuinely distinct quantities**. Their apparent
rate-1/2 coincidence required *both* a wrong normalization *and* a
central-binomial accident; correct either one and it disappears.

**Honest scope (brief clause 3.1).** I needed no new modelling input — both
governing formulas were already banked. But I have *not* shown that no deeper
structural map `Lambda <-> agreement support` exists. What is proved: **the two
defining balances are different balances**, so the repo's adjudication of them
as one quantity is unsupported and numerically false at every prize rate under
the better-supported normalization.

---

## 3. (N3) The dependency repricing

Tags: **[F2]** consumes `t_F2`; **[XR]** consumes `t_XR`; **[SAFE]**
conclusion independent of which `t`; **[MIS]** consumed the wrong `t`.

| # | banked conclusion | file:line | correct | consumed | verdict |
|---|---|---|---|---|---|
| 1 | corridor table `t*`, `s*=t*-1` | `xr_radius_arithmetic/proof.md:54-58` | XR | XR | **[XR]** ok |
| 2 | `mca_floor` `sigma_max`, `sigma*` | `mca_floor/statement.md:14,65` | XR | XR | **[XR]** ok — §4 |
| 3 | LEMMA 3 *proper* | `f2_opening/PROOFS.md:222-227` | — | none | **[SAFE]** — it is `t`-free, §3.3 |
| 4 | LEMMA 3 official-row gloss | `f2_opening/PROOFS.md:232-233` | F2 | F2 | **[F2]** ok in type; rests on `dim L <= t`, §3.3 |
| 5 | "`t*` flips LEMMA 3 to 0.9687x" | `f2_sl1_powersums/REPORT.md:13` | F2 | **XR** | **[MIS]** |
| 6 | `f2_tq_pin` band rows at `t*` | `f2_tq_pin/PROOFS.md:337,340` | F2 | **XR** | **[MIS]** |
| 7 | `f2_tq_pin` band rows at `2^33` | `f2_tq_pin/PROOFS.md:338,341` | F2 | F2 (count) | **[F2]** ok, §3.1 |
| 8 | `f2_sl1b` `t*` row | `f2_sl1b/REPORT.md:54` | F2 | **XR** | **[MIS]** |
| 9 | `|K1| = 2^{n/2}` pricing identity | `f2_tq_pin/PROOFS.md:395-400` | F2 | **XR** | **[MIS]**, §3.2 |
| 10 | `7e10` exclusion | `f2_tq_pin/PROOFS.md:249-262` | F2 | F2 only | **[F2]** — but normalization-fragile, §6 |
| 11 | `t in (2^33, 5.364e10]` | `f2_tq_pin/PROOFS.md:202` | F2 | F2 (count) | **[MIS]** — wrong normalization, §1.5 |
| 12 | CATCH-2 sliver `[255.9113,256)` | `f2_tq_pin/PROOFS.md:443-446` | — | **mixed** | **[MIS]**, §5 |
| 13 | `b2b_near_tail_bound` caveat | `dag.json:7559` | ambiguous | both | **[MIS]?** — §3.4 |
| 14 | `official_scale.json` `t = 2^33` | `c2pp_nullity_structure/results/` | F2 (DLI) | F2 | **[F2]** ok by §1.5 degeneracy |
| 15 | `SOL_TARGET_3` `t* ~ 7e10` | `SOL_TARGET_3_OFFICIAL_EXTRAS_FLOOR.md:35` | `t*_eff` | `t*_eff` | **[MIS]** glyph clash, §1.6 |

### 3.1 The band survives the retyping (S14)

Rows 5/6/8 fed `t* = 8,592,912,739` — a coordinate-space agreement excess —
into LEMMA 3's gloss, which needs a frequency-space quantity. Category error,
and exactly the pre-registered defect catch. The *conclusion* survives because
`f2_tq_pin` independently ran `t = 2^33`, the infimum of the count-reading
`t_F2` interval:

```
  new-part : bands at t* : (15, 10)  ==  bands at 2^33 : (15, 10)   (S14.1)
  nested   : bands at t* : (14,  9)  ==  bands at 2^33 : (14,  9)   (S14.2)
```

**Citation defective, band intact** — *under the count reading*. Under the
degree reading the bands move to `(16, 11)` (**S15.3**), i.e. LEMMA 3 **holds**
at rung 16 with margin `1.9375x` instead of being violated at `0.9687x`
(**S15.2**). Controls reproduced first: `7.8915x`, `0.9687x`, `(16,13)`,
`(15,10)` (**S14.c1–c4**).

### 3.2 The `|K1| = 2^{n/2}` identity is exact only for `t_F2` (S16)

`f2_tq_pin/PROOFS.md:399-400` calls it *"structural, not numerical"*:

> The first identity is **structural, not numerical**: `dim K1 · L =
> (t*/2)·L = (t*·L)/2 = n/2` by the balance (F).

The step `(t*·L)/2 = n/2` **is** the (C) balance — a `t_F2` fact applied to a
`t_XR` number. Substituting honestly:

```
    (t_F2/2)·L = 1.099512e12 = n/2   EXACTLY        (S16.1)  -> structural
    (t*  /2)·L / (n/2) = 0.99995594  != 1           (S16.2)  -> approximate
    shortfall = Delta/2 = 4.8443e7 bits, the same 4.406e-5   (S16.3)
```

It is also **internally inconsistent**: `dim K1 = ceil(t/2) = |Lambda|`
together with `t = |Lambda|` forces `|Lambda| <= 1` (**S18**). The
`Θ(n)`-not-`o(n)` conclusion of (P6) is nonetheless **[SAFE]** — a `4.4e-5`
wobble cannot make a `2^{n/2}` factor `o(n)` — but "structural" must be
retyped, and if `t_F2` is only interval-pinned then `log2|K1|` is an interval
too, not the single value `n/2`.

### 3.3 LEMMA 3 itself is `t`-free

`f2_opening/PROOFS.md:222-227` contains **no `t`**:

> ```text
>     dim_{F_p} L  >=  m / log2 p  -  o(n)/log2 p.
> ```
>
> *Proof.* Drop every term but `c` in the kernel of the evaluation map;
> each contributes `T_W(0) = 4^m`, and the kernel has index `|L| = p^{dim L}`.
> QED

`t` enters only through the gloss at `:232-233` via the unstated step
`dim L <= t`. `f2_sl1b/results/VERIFY_LOG.txt:101` reports that step broken:

> `  [PASS] S8 under the tower the upper bound dim L <= k|Lambda| is VACUOUS at rungs 14-16 under every live t   -- dim L <= m is all that survives from above; every verdict that used 'dim L <= t' (= the k=2 case) needs re-derivation`

So **the lemma is safe; its consumption is not.** Every rung-14–16 verdict
built on `dim L <= t` needs re-derivation independently of this pilot.

### 3.4 One case I could not decide

`dag.json:7559` / `critical/nodes/b2b_near_tail_bound/node.json:8` substitutes
`t = 2^33+1` and `t* = 8592912739` interchangeably in one sentence while the
node sits in the `t`-null (F2) lane and its bound `N_{t+k} <= C(n,k)/C(t+k,k)`
is agreement-`t+k` counting (XR). Flagged as a **probable** wrong-`t`
consumption; I did not resolve it.

---

## 4. (N4) The near-collision: **not two objects — a real conflict**

### 4.1 `8,594,128,895` has an exact closed form, and it is the node's own

From `statement.md:12-14` (`c = 2^22`, `d = 2,048`, `sigma_max = dc+c-1`),
evaluating in exact integers (**S7**):

```
    sigma_max = 2048·2^22 + (2^22 - 1) = 8,594,128,895 = 2^33 + 2^22 - 1
```

It is a **construction ceiling** — the largest excess the cyclic-rotation
construction reaches at `c = 2^22, d = 2048` with maximal residual prefix
`s = c-1`. Not a threshold, not an optimum.

### 4.2 `8,592,912,739` in `mca_floor` **is** `t_XR` — same object, same number

`statement.md:65` reads `sigma*=8,592,912,738`. In exact integers (**S8**):

```
    sigma* = 8,592,912,738 = t* - 1 = s*                        EXACTLY
    the "safe point at k+sigma*+1" sits at excess sigma*+1 = t*  (S8.b)
```

`mca_floor` measures agreement as `k + sigma` (`(SP2)`), so its `sigma` **is**
`A - k` — verbatim `t_XR`'s definition. Two 10-digit integers matching exactly,
with matching semantics.

**Therefore `f2_tq_pin` residual 4's *"different object"* is WRONG, and so is
this brief's instruction to *"prove they are different objects"*.** Both are
excesses `A - k` at the same row: `sigma_max` a ceiling, `t*` an interior point
of the same axis. U3 predicted this and it is confirmed.

### 4.3 The difference — decomposed, and **already banked**

```
    sigma_max - t*  = 1,216,156                                     (S9.1)
    t* - 2^33       = 2,978,147                                     (S9.2)
    1,216,156 = (2^22 - 1) - (t* - 2^33) = 4,194,303 - 2,978,147    (S9.3)
```

**This is a re-derivation, not a discovery.** `notes/kernel_basis/WAVE9_AUDIT_FINDINGS.md:189-191`:

> - Independent constants (w9_checks.py, own code): log2 C(524287,264192)=524254.0796;
>   sigma*=2048*2^22+2,978,146=8,592,912,738; sigma_0=2048*2^22+2^22-1=8,594,128,895
>   (delta = 1,216,157); boundary (128+log2B-log2N)/2048 = 256.0366599729 > 256; list margin

and `critical/nodes/rate_half_band_closure/node.json:9` carries *"band width
2,978,146"*. The banked `delta = 1,216,157` is `sigma_max - sigma*`; the
brief's `1,216,156` is `sigma_max - t*`; they differ by exactly 1 because
`t* = sigma* + 1` (**S20**). So: the decomposition **is** closed in row
parameters, it was already in the repo, and the brief's number is the banked
one shifted by the `t*`/`sigma*` off-by-one. The difference itself has no
closed form, since `t*` is a transcendental crossing of (T*).

### 4.4 The conflict, surfaced

`mca_floor` is **PROVED** (`node.json:7`) and proves (`(SP1)`,`(SP2)`) that
`epsilon_ca, epsilon_mca > 2^-83 > 2^-128` at **every** excess
`1 <= sigma <= sigma_max`. And (**S10.1**): `1 <= t* <= sigma_max`.
**`t*` lies inside the proved prize-unsafe interval.** Non-vacuously: at
`q = 2^255` the cyclic list has `log2 L_q = 2250` (**S10.2**).

Not a formal contradiction — `xr_radius_arithmetic` proves a *first-moment
count* crossing, `mca_floor` a *correlated-agreement error* floor. But a
**substantive conflict of use**: the campaign consumes `t*` as *"the corridor
edge (smallest window with FM mean `<= B*`)"*, i.e. where a rate-1/2 row
closes, and `mca_floor` proves that at that excess the row is unsafe by 45 bits.

### 4.5 …and the conflict is **twice as bad** as the brief's framing (post-sweep)

`critical/nodes/rate_half_cyclic_rotated_prefix_floor/claim_contract.md:24-26`:

> > OPTIMIZED UPDATE (wave-10, 2026-07-18): `c=2^33,d=1,s=c-1`
> > supersedes the wave-9 endpoint. The proved unsafe band is
> > `1<=sigma<=2^34-1`; the earlier `8,594,128,895` endpoint is historical.

So `8,594,128,895` is **historical**. The current proved unsafe reach is
`2^34 - 1 = 17,179,869,183`, and (**S19.1**):

```
    t* / (2^34 - 1) = 0.50017
```

**`t*` is not `1.2e6` below the unsafe ceiling — it sits at essentially half of
it, deep in the interior.** The brief's "near-collision" is an artifact of
comparing against a superseded endpoint. The reconciliation is already
adjudicated by the repo (`statement.md:68-71`: *"the previously conjectured
safe point at `k+sigma*+1` is unsafe"*), and `xr_radius_arithmetic` still
carries no cross-reference to its own refutation.

**One coincidence to police, not to use (S19.2).** The degree-reading counting
floor `2n/256 = 2^34` equals the wave-10 band top plus one. Both are dyadic
multiples of `n/256`. Recorded **only** so that nobody reads it as evidence of
identity — it is exactly the genus of accident this pilot exists to expose.

---

## 5. (N5) The sliver seam: mis-typed, and **empty**

### 5.1 CATCH-2's "0.011 bits" is `Delta/t*`

CATCH-2 reports `L = 255.9` below `n/t* = 255.911275`. Reproduced (**S11.1**):
gap `= 0.011275` bits. And (**S11.2**) `Delta / t* = 0.011275` — **the same
number**. The "inconsistency" is the per-condition share of the entropy deficit:
a symptom of §2, not a mis-set convention.

### 5.2 The sliver was computed with `t*` frozen; `t*` is a function of `L`

`dt*/dL = -3.3576e7` per bit at the convention point (**S12.b**). Solving
`L >= n/t*` with `t*` held at its `L = 255.9` value does not solve the stated
condition.

### 5.3 Recomputed self-consistently, the sliver is EMPTY at every rate (S12)

Re-solving (T*) at each `L` over `(log2 n, 256)`:

```
  rate 1/2  : max_L [ t*(L)·L - n ] = -9.6811e7  < 0   at L = 255.999
  rate 1/4  : max_L [ t*(L)·L - n ] = -3.4772e11 < 0
  rate 1/8  : max_L [ t*(L)·L - n ] = -9.1995e11 < 0
  rate 1/16 : max_L [ t*(L)·L - n ] = -1.3825e12 < 0
```

**`{L : t*(L)·L >= n}` is empty.** U7(b)'s falsifier did not trigger
(**S12.F**). Forced by §2: `t*(L)·L - n = -Delta(L) < 0` for every `L < 256`.

**How far from reachable (S12.c).** `Delta = 0` first occurs at
`L = sqrt(2n/((128 - (1/2)log2(pi n/2)) ln 2)) = 2.4332e5` bits — a field of
size `~2^243316`. The `|F| < 2^256` cap would have to rise **~950x in bits**.
Not marginally unreachable: unreachable by three orders of magnitude.

### 5.4 The corrected convention (the recommendation)

`L = 255.9` is self-labelled a *"Prize convention"*
(`xr_radius_arithmetic/proof.md:33`); the rules say only `L < 256`.

1. **RETIRE the `[255.9113, 256)` sliver. FORCED.** It is a mixed-type object —
   the `t_F2` balance (C) applied to a `t_XR` value — and recomputed
   self-consistently it is empty for every admissible field. The implicit
   "move `L` up by 0.011 bits" repair provably does not work.
2. **Keep `L = 255.9`, re-label it. CHOICE (surfaced, not applied).** Replace
   *"Prize convention"* with *"representative evaluation point of an
   `L`-indexed family; the rules pin only `log2 n < L < 256`"*, and publish
   `dt*/dL = -3.36e7` per bit so consumers see the table is a slice, not a
   constant. Any admissible point would do; `255.9` has the merit that the
   banked table is already verified there.
3. **Never cross-audit the balances. FORCED.** Do not use (C) to audit `t_XR`
   or (T*) to audit `t_F2`: they are different balances (§2.2), and
   cross-auditing manufactures phantom inconsistencies of size `Delta` —
   which is precisely what CATCH-2 was.

---

## 6. The `7e10` exclusion — re-verified, and **partially overturned**

The brief requires verifying, not inheriting, `f2_tq_pin`'s claim.

### 6.1 The dependency audit confirms the narrow claim

The exclusion chain is: (C) `t·L >= n` [F2-side]; (R1) `n | q-1 => L > log2 n`
[rules]; the constant `n`. **Nothing else** — no `C(n,j)`, no gate `B*`, no
(T*), no `t*`, no `A`, no `k` (**S13.dep**). Recomputed independently:

```
  n = 2^41 : L = n/t = 31.415 < 41.0 = log2 n  -> EXCLUDED       (S13.2^41)
  n = 2^40 : L = n/t = 15.707 < 40.0           -> EXCLUDED       (S13.2^40)
  base-field reading : L = 31.415 < 39         -> EXCLUDED       (S13.p)
  origin reproduced  : n / log2 p_KB = 7.0962e10 ~ 7e10          (S13.orig)
```

**So the exclusion consumes no `t_XR`: it is independent of the collision as
the brief posed it.** `f2_tq_pin`'s claim is confirmed *on that axis*.

### 6.2 But it does **not** survive the count/degree axis (S21)

§1.5 shows the F2 lane's own reading gives (C') `t_F2 = 2n/L`. Then:

```
  COUNT  reading : t = 7e10 => L = n/t  = 31.415  < 41   -> EXCLUDED     (S21.1)
  DEGREE reading : t = 7e10 => L = 2n/t = 62.829,
                   and 41 < 62.829 < 256 -> RULES-ADMISSIBLE, NOT EXCLUDED (S21.2)
```

Under the degree reading the rules-forced interval is `(2^34, 1.0727e11]`, and
**`7e10` lies inside it** (**S21.4**).

### 6.3 The honest verdict

**The `7e10` exclusion is t-naming-independent only with respect to the
collision the brief named.** It is *not* robust: it holds under
`f2_tq_pin`'s count normalization and **fails** under the degree normalization,
which §1.5 shows is the better-supported one (five sources against one).
`f2_tq_pin` (P3)'s headline — *"`7e10` is EXCLUDED by the rules, under BOTH
field readings, at BOTH `n = 2^40` and `n = 2^41`"* — enumerated the field
readings but not the normalization, and the normalization is what decides it.

What survives unconditionally: the **origin** of `7e10` is still a unit error
(dividing the window-bits product by `log2 p ≈ 31`, a characteristic no
admissible row possesses, `f2_tq_pin` §1.3). A wrong derivation is not the same
as an excluded value, and only the first is established.

What does not survive: the positive identification `t = t*` (§2), exactly as
`f2_tq_pin` residual 1 anticipated — and now more sharply, since under the
degree reading the gap at rate 1/2 is a factor 2, not `4.4e-5`.

---

## 7. Catches

- **CATCH-A (maintainer-level, N4).** `f2_tq_pin` residual 4 and this brief
  both call `mca_floor`'s `8,592,912,739` a *"different object"* from `t*`.
  **It is the same object** (`sigma* = t*-1` exactly; `sigma = A-k` by `(SP2)`).
  Worse: `8,594,128,895` is **historical** — wave-10 supersedes it with
  `1 <= sigma <= 2^34-1`, so `t*` sits at `0.50017` of the current proved
  unsafe reach, deep inside it. `xr_radius_arithmetic` carries no
  cross-reference to its own refutation.
- **CATCH-B (N2).** The identification is **refuted**: `t_F2` is
  rate-independent, `t_XR` rate-dependent; gaps of `18/45/66%` at rates
  `1/4 / 1/8 / 1/16`, and a **factor 2 at rate 1/2** under the F2 lane's own
  normalization (§2.7).
- **CATCH-C (N2; closes `f2_tq_pin` CATCH-4).** The `0.0044%` tightness is not
  empirical: it is exactly `2/(L^2 ln 2)`, the second-order entropy deficit of
  the central binomial. A Stirling correction, not evidence of identity.
- **CATCH-D (N3).** `f2_sl1_powersums/REPORT.md:13`, `f2_sl1b/REPORT.md:54`,
  `f2_tq_pin/PROOFS.md:337,340` feed `t*` (coordinate-space excess) into
  LEMMA 3 (frequency-space). Type error; band survives under the count reading
  (S14), moves to `(16,11)` under the degree reading (S15.3).
- **CATCH-E (NEW, maintainer-level — `t_F2` is NOT `|Lambda|`).**
  `f2_tq_pin/PROOFS.md:158`'s *"`t = |Lambda|`"* is contradicted by five
  sources (`f2_sl1b/PROOFS.md:8-12`, `f2_sl1_powersums/PROOFS.md:7-10`,
  `f2_opening/PROOFS.md:327`, `f2_deployed_windows/selection.py:50,54`,
  `SOL_TARGET_3_OFFICIAL_EXTRAS_FLOOR.md:19-23`), all reading `t` as the max
  Newton index with `|Lambda| = ceil(t/2)`. The two cannot co-hold above
  `t = 1` (**S18**). It looked true because in the DLI lane `Lambda` is *all*
  `r <= t` (`dli_official_support_forcing/proof.md:27`), where count and index
  bound coincide. **This factor 2 decides three verdicts**: the rung-16
  LEMMA 3 margin (`0.9687x` VIOLATED vs `1.9375x` HOLDS), the `t_F2` interval
  (`(2^33, 5.36e10]` vs `(2^34, 1.07e11]`), and the `7e10` exclusion (§6).
- **CATCH-F (N5).** The sliver was computed with `t*` frozen while
  `dt*/dL = -3.36e7`. Recomputed self-consistently it is **EMPTY** at every
  rate; first reachable at `L = 2.43e5` bits (~950x the cap). CATCH-2's
  "0.011 bits" is `Delta/t*`, a symptom of CATCH-B.
- **CATCH-G (NEW).** A **third `t*`**:
  `SOL_TARGET_3_OFFICIAL_EXTRAS_FLOOR.md:20,35` uses `t*` for
  `#{p-free i <= t}` at `~7e10`, an order of magnitude from the corridor edge,
  and it carries the load-bearing sub-balance `|B0|^{t*} >= 2^N`.
  `SOL_TARGET_3C_PRIMITIVE_CENSUS.md:15-16` renamed it `t*_eff`; the `_3_` file
  did not.
- **CATCH-H (process).** The brief cites
  `critical/nodes/rate_half_cyclic_simple_pole_mca_floor/node.json:9`; that
  directory does not exist — the node is in `background/nodes/`.
  `f2_tq_pin/PROOFS.md:479` has the correct path, `REPORT.md:53` the wrong one.

---

## 8. Registrations: outcomes

| reg | outcome |
|---|---|
| U1 | **CONFIRMED** (S2, S3, S3.F, S6.b) |
| U2 | **CONFIRMED** (S4, S5, S5.q, S6) |
| U3 | **CONFIRMED, all four parts** (S7–S10) — though 4.3's decomposition was already banked (S20) |
| U4 | **CONFIRMED as literally registered** (S13) but its *conclusion* is **superseded**: a third naming axis I had not considered breaks the exclusion (§6.2, S21) |
| U5 | **CONFIRMED** (S14) |
| U6 | **CONFIRMED, and RESOLVED beyond registration.** I registered "I do NOT predict which reading is correct"; the sweep decided it 5-to-1 for the degree reading (§1.5) |
| U7 | **CONFIRMED** (S11, S12) |
| U8 | **CONFIRMED** (S16) |

**Weakness of my own pre-registration, stated plainly.** Eight for eight means I
registered after reading enough to be nearly certain — U1–U8 carry less
evidential weight than a blind pre-registration. The falsifiers were real and
tested in advance (S3.F, S12.F), but I took little risk. The genuinely
surprising results (§1.5, §4.5, §6.2) all came from evidence found **after**
the registrations, and none of them was predicted.

**Two self-corrections, both caught by the fail-closed harness:**

1. `S0.2` FAILED at `986.27` bits against my 1-bit tolerance. I had omitted the
   quartic de Moivre–Laplace term `(4/3)t^4/(n^3 ln2) = 986.3` bits. `lgamma`
   was never at fault; my formula was. Fixed in S0.2 and S5.q (now rel `<1e-7`).
2. `S21.3` FAILED because I wrote the divergence predicate as `A != B` when
   both branches are true; the correct predicate is `A and B`. Fixed.

---

## 9. Honest residuals

1. **I did not prove there is no deeper correspondence.** §2 proves the two
   *defining balances* differ and the values differ at all four rates under the
   supported normalization. It does not prove no structural map
   `Lambda <-> agreement support` exists. Minimal missing premise for the
   positive identification: a statement of the form *"the `t`-null block window
   is in bijection with the aligned `j`-support ensemble"*. Nothing supplies
   it, and the rate-dependence is strong evidence against it.
2. **CATCH-E's factor 2 is decided by weight of evidence (5-to-1), not by
   proof.** A maintainer should pin `Lambda`'s parity convention at the point
   where (C) is imposed. Until then the `t_F2` interval, the rung-16 verdict
   and the `7e10` exclusion all have two live values.
3. **`t_XR` remains conditional** on the open slot `xr_ledger_qpower`
   (`xr_radius_arithmetic/proof.md:31-32`), inherited unchanged.
4. **`t_F2` is less pinned than `f2_tq_pin` left it** — an interval, now with
   two candidate normalizations, and with `t*` removed as its pin.
5. **CATCH-A's conflict is of *use*, not of logic.** I did not check whether
   `mca_floor`'s and `xr_radius_arithmetic`'s predicates are formally
   compatible, only that the campaign consumes `t*` as a closure point and
   `mca_floor` refutes that consumption.
6. **Downstream cascades not priced.** `mca_floor` feeds `rate_half_band_closure`;
   CATCH-E reaches every LEMMA 3 / THEOREM A/B margin; `f2_sl1b`'s
   *"every verdict that used 'dim L <= t' needs re-derivation"* (§3.3) is a
   third cascade. I priced none of them.
7. **`m_16` and `log2 p = 30.99` are an inadmissible row** (`f2_tq_pin`
   CATCH-1: the tower breaks the field cap from rung 4). I reproduced that
   arithmetic to test the retyping, not to endorse it.
8. **Row 13 of §3 (`b2b_near_tail_bound`) is unresolved** — flagged as a
   probable wrong-`t` consumption, not established.
9. **Sweep provenance.** §1.5, §1.6, §3.3, §4.5, §6.2 and CATCH-E/G/H rest on a
   repo-wide sweep. I verified ten of its load-bearing quotes myself against
   the files; one line citation drifted (`even_l` is at `selection.py:50`, not
   `:49`) and is corrected here. Quotes I did not personally re-open are not
   used as load-bearing.
