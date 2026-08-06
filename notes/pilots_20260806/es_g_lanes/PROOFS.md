# PROOFS — ES-G-LANES (round 17)

Derivations behind the four-lane re-check against (ES-G).  Every statement
relied on is quoted VERBATIM with `file:line`.  Machinery in `esg_lib.py`,
validation in `esg_selftest.py` (1413 checks, 0 failures), tables in
`esg_analysis.py` / `full_run.txt`.

---

## 0. The statement being applied, verbatim

`notes/pilots_20260806/es_boundary_adversary/FABLE_AUDIT.md:21-25`

> - **(ES-G)**: the terminal's statement of record is the GLOBAL-balance
>   form (2^n <= p^{|Z_w|} with the TRUE cyclotomic-closure size), with
>   balance imposed STRATUM-BY-STRATUM (C4-a: T a union of mu_{2^a}-
>   cosets sees only the surviving conditions of the n/2^a instance;
>   the binding stratum is not always a = 0).

The stratum clause's source, `notes/pilots_20260806/es_boundary_adversary/REPORT.md:84`

> Candidate lemma: *balance must be imposed stratum-by-stratum, a = 0 … log2(M)−1; the binding stratum is not always a = 0.*

and its mechanism, same file `:79`

> **(C4-a) THE STRATUM MECHANISM — the deep violations are a *mis-specified codimension*, not a conspiracy.** If T is a union of μ_{2^a}-cosets with 2^a < M, every odd-index window condition holds *for free*, and the surviving conditions reduce to a strictly smaller instance at n/2^a. The per-weight Lam then **over-counts** the constraint.

The residual this pilot was commissioned to close, `REPORT.md:90`

> **(C4-d) delta > 1 residual for the prize rows.** The banked Lambda uses `|Z_w| >= w-1 with equality iff delta = 1`. At delta ∈ {2,4} the prize-row balance status depends on the **actual** cyclotomic-closure size, not the bound

The per-weight form being retired, `notes/pilots_20260804/mun_anticoncentration/REPORT.md:40`

> **(ES) ENTROPIC SUPPRESSION OVER mu_n.** … If the row is **sub-balance**, `c·log2 q >= log2 C(n,r') + sigma`, then `R(V) = R^per(V)` — **no accidental members**.

So the two functionals are, with `c` conditions over a value field of size `V`:

```
PER-WEIGHT (retired):  c*log2 V  >=  log2 C(n,r')
GLOBAL     ((ES-G)):   c*log2 V  >=  n
```

`GLOBAL => PER-WEIGHT` since `C(n,r') <= 2^n`.  No third functional is used.

---

## 1. L1 — what `|Z_w|` IS, and its exact value at `n = 2^41`

### 1.1 The condition count is the p-closure size, and the base is p not q

`notes/pilots_20260804/mun_anticoncentration/PREREG.md:60`

>   mod `n`; `dim C = n - |Z_w|`, `w-1 <= |Z_w| <= delta (w-1)`.

`notes/pilots_20260804/crossing_w2_opening/REPORT.md:69` (THEOREM Q, PROVED)

> Fix `n,r',w`. For every `q` with `n | q−1`, `W_w` and its entire sig-profile depend on `q` only through `p = char F_q` — never through `e` in `q=p^e`.

Hence for the crossing (prefix/cyclic) instance the condition count is
`c = |Z_w| = |closure of {1,...,w-1} under multiplication by p in Z/n|`
and the value field is `F_p`, i.e. `V = p`.  **This is load-bearing: a
tower row `q = p^e` gets NO extra balance from `e`** — the count is the
same, only `p` pays.

### 1.2 The admissible characteristics

`notes/pilots_20260804/mun_anticoncentration/PREREG.md:41-43`

> **Characteristic arithmetic (proved, verify3_prizerow.py R3).** `n = 2^41`,
> `n | p^e - 1`, `p^e = q < 2^256` force `delta := ord_n(p) = 2^j` with
> `j <= 2`, so `delta in {1,2,4}` and `p >= 2^39 + 1`.

`notes/pilots_20260806/f2_tq_pin/PROOFS.md:114-115`

>     v_2(e) <= 2,      e <= 6,      log2 p >= 39,
>     ord_n(p) in {1,2,4}  =>  TOWER DEPTH <= 2 RUNGS.

Extension rows are admissible, not a hypothetical —
`critical/nodes/axis8_generating/proof.md:13-14`

> The official family admits non-generating rows. Therefore the tower case is
> admissible and must be priced by the `ext_lift` / `f1_classification` chain.

and the rules cap, `critical/nodes/rules_freeze/statement.md:9`

> smooth domain = coset of a power-of-2-order subgroup; k <= 2^40; |F| < 2^256; rates EXACT in {1/2, 1/4, 1/8, 1/16}

**Structure lemma (proved here, verified).**  `ord_{2^m}(p) | 4` iff
`p ≡ ±1 (mod 2^{m-2})`.  Hence every admissible characteristic lies in one
of exactly EIGHT residue classes mod `2^41`:
`p ≡ ε(1 + j·2^39)`, `ε ∈ {±1}`, `j ∈ {0,1,2,3}`.

### 1.3 Exact closure sizes (the deliverable)

Write `W = w-1`, `n = 2^m`.  Every `g ∈ <p>` satisfies `g ≡ ε_g (mod 2^{m-2})`.
For `W < 2^{m-2}` and `s,s'' ∈ [1,W]`:

* `ε_g = +1`: `g·s ≡ s (mod 2^{m-2})`, and both lie in `[1,2^{m-2})`, so
  `g·s mod n ∈ [1,W]` **iff** `g·s ≡ s (mod n)` **iff** `j·(s mod 4) ≡ 0 (mod 4)`.
* `ε_g = −1`: `g·s ≡ −s (mod 2^{m-2})`; the only candidate `≤ W` is
  `2^{m-2} − s`, which needs `−j·(s mod 4) ≡ 1 (mod 4)` **and** `s ≥ 2^{m-2} − W`.

Therefore `|Z_w| = Σ_{s=1}^{W} delta / m(s)` with `m(s) = #{g ∈ <p> : g·s mod n ∈ [1,W]}`
depending only on `s mod 4` and on the threshold test.  This is
`closure_size_fast`; it is validated against `closure_size_brute` at
`m = 5..16` over ALL `p` of order 1, 2, 4 and 13 values of `W` each
(`esg_selftest.py` block (A), 0 failures), and it reproduces the round-16
witness table's own `|Z_w|` values at `n = 32` exactly (block (D)).

**Result at `w = 2^v`, `v = 34..37`** (before the orbit-merge effect):

| `p` class mod `2^41` | `delta` | exact `|Z_w|` | ratio to `w-1` |
|---|---|---|---|
| `1` | 1 | `w-1` | `1` |
| `2^40+1 = 1099511627777` | 2 | `3·2^{v-1} - 1` | `≈ 1.5` |
| `2^40-1`, `2^41-1` | 2 | `2(w-1)` | `2` |
| `2^39+1`, `3·2^39+1` (ε=+1) | 4 | `11·2^{v-2} - 1` | `≈ 2.75` |
| `2^39-1`, `3·2^39-1` (ε=−1) | 4 | `6·2^{v-1} - 2` | `≈ 3` |

**CATCH-B (against round-15's bracket).**  `w-1 <= |Z_w| <= delta(w-1)`
(`mun PREREG.md:60`) is correct but **its top end is never attained at
delta = 4**: the maximum is `3(w-1)`, i.e. `0.75·delta(w-1)`.  Anyone
pricing a `delta = 4` row at the bracket top over-credits it by 33%.

**CATCH-C (orbit merge at the top of the bracket).**  At `w = 2^38, 2^39`
the two `ε = −1, delta = 4` classes lose orbits to the collision
`s ↦ 2^39 − s` and drop from `≈3(w-1)` to **exactly** `2(w-1)`.  The ratio
is NOT `w`-uniform across the crossing bracket; a single measured ratio
must not be transported.

**P1 verdict: REFUTED AS STATED, and I record it as such.**  I registered
the ratio SET as exactly `{1, 3/2, 2, 11/4, 3}`.  The true set at `w=2^34`
is `{1, (3·2^33−1)/(2^34−1), 2, (11·2^32−1)/(2^34−1), (6·2^33−2)/(2^34−1)}`
— my closed forms for `|Z_w|` were right, the ratio claim was wrong by the
`−1` offsets, and (per CATCH-C) it is not even `w`-uniform.

---

## 2. L2 — global balance at the crossing row

Global balance is `|Z_w|·log2 p >= n = 2^41`, i.e. `log2 p >= n/|Z_w|`.

Admissible `(delta, e)` pairs: `delta | e`, `e <= 6`, `v_2(e) <= 2`, giving
19 `(p-class, e)` combinations; `p ∈ [p_min(class), floor((2^256−1)^{1/e})]`.

**Threshold table at `w = 2^34`** (`thr = n/|Z_w|`):

| class | `delta` | `thr log2 p` | max admissible `log2 p` |
|---|---|---|---|
| `1` | 1 | `128.0000000` | `< 256/e` |
| `2^40±1`, `2^41−1` | 2 | `85.333` / `64.000` | `< 128` |
| `2^39±1`, `3·2^39±1` | 4 | `46.545` / `42.667` | `< 64` |

Verdicts over the whole structural bracket (`esg_analysis.py` L2 block):

```
w=2^34: ALWAYS sub-balance  0, FLIPS  8, NEVER 11   (of 19 (class,e) pairs)
w=2^35: ALWAYS sub-balance 10, FLIPS  5, NEVER  4
w=2^36..2^39: ALWAYS sub-balance 19, FLIPS 0, NEVER 0
```

**The C4-d sign flip is confirmed and localised**: it is exactly the
`w = 2^34, 2^35` end of the bracket, and it is driven by `e`, not by
`delta` — because THEOREM Q makes `e` free for the count but `e` divides
the available `log2 p`.

Reproduction of the banked numbers (`esg_selftest.py` block (C)):
`Lambda(2^34) = −2.20e12` at `log2 q_char = 256`, `+1.4943e12` at `2^41`,
crossover at `log2 q_char = 127.977` — all reproduced, which is what
licenses the machinery.

### 2.1 An explicit admissible counterexample row (P2)

```
p = 6597069766657 = 3·2^41 + 1   (prime; p ≡ 1 mod 2^41, so delta = 1)
e = 6,  q = p^6,  log2 q = 255.509775 < 256,  2^41 | q−1,  k = 2^40
B* = floor(q/2^128) = 242251802232021244567343686397347233808 (log2 B* = 127.510)
|Z_{2^34}| = 2^34 − 1,   |Z_w|·log2 p − n = −1.467419e12   ->  ABOVE BALANCE
```

This row satisfies every rules-freeze constraint.  `log2 B* = 127.51` is
well above the structural count `log2 S(2^34) = 117.149`, so `w = 2^34` is
inside the lane's live range at this row.  **(ES-G) is false at it.**

---

## 3. L3 — the stratum decomposition, and the binding stratum

### 3.1 The reduction, made exact

Let `T` be a union of `μ_{2^a}`-cosets, `T = ⋃_{y∈Y} y·μ_{2^a}`.  Then

```
p_s(T) = Σ_y Σ_{ζ∈μ_{2^a}} (yζ)^s = (Σ_y y^s)·(2^a if 2^a | s else 0),
```

so the conditions `p_s(T)=0`, `s = 1..w−1`, collapse to those with `2^a | s`
(the rest hold for free — C4-a), and with `s = 2^a s'` and `Y ⊆ μ_{n_a}`,

```
n_a = 2^{41-a},   W_a = floor((w-1)/2^a) = 2^{v-a} − 1,   r'_a = r'/2^a,
|Z^{(a)}| = |closure of {1..W_a} under *p in Z/n_a|.
```

`2^a ≠ 0` in `F_p` (p odd), so nothing is lost.  Stratum-`a` global balance
is `|Z^{(a)}|·log2 p >= n_a`, for `a = 0 .. log2(M) − 1 = v − 1`.

**Non-vacuity (checked):** `r' = 2^40 − 2^v` is divisible by `2^a` for every
`a <= v−1` and every `v = 34..39`, so every stratum has candidate members.
The strata are real obligations, not empty ones.

### 3.2 The binding stratum is the DEEPEST one, uniformly

At stratum `a`, `|Z^{(a)}| ≈ (w−1)/2^a · c_a` and `n_a = n/2^a`, so the
`2^{-a}` cancels — **except** that `c_a` (the closure factor) collapses as
`a` grows, because `ord_{2^{41-a}}(p)` drops to 1 once `p ≡ 1 mod 2^{41-a}`,
and because the `−1` in `W_a = 2^{v-a} − 1` bites hardest when `W_a` is
small.  Computed over all 8 classes and all `v ∈ {34,35,36,39}`: the binding
stratum is `a = v − 1` in **every** case.

At `a = v−1`: `n_a = 2^{42−v}`, exactly ONE condition survives
(`s = 2^{v-1}`, since `2·2^{v-1} = 2^v > w−1`), so `|Z^{(a)}| ∈ {1,2}`
(2 iff `p ≡ −1 mod 2^{42−v}`, i.e. iff `ε = −1`).  Required:

```
log2 p >= 2^{42-v} / |Z^{(a)}|.
```

| `w` | required `log2 p` (ε=+1 / ε=−1) | admissible? |
|---|---|---|
| `2^34` | `256` / `128` | **NO for all 19 (class,e) pairs** |
| `2^35` | `128` / `64`  | only 3 of 19 |
| `2^36` | `64` / `32`   | only 12 of 19 |
| `2^37..2^39` | `<= 32` | all 19 |

**At `w = 2^34` the requirement `log2 p >= 256` (ε=+1) or `>= 128` (ε=−1)
is unreachable at EVERY admissible row**, because `|F| < 2^256` forces
`log2 p < 256/e`, and the `ε=−1` classes all have `delta ∈ {2,4}`, hence
`e >= 2`, hence `log2 p < 128`.  Exact integer form: `p^e = q <= 2^256 − 1`,
so `e·log2 p < 256`; for `ε=+1, delta=1, e=1` the requirement is
`p >= 2^256 > q`.  No case survives.

**CATCH-A (against my own first script, self-caught).**  My first summary
column decided this with a float compare and reported 5/8 rather than 19/19,
because `log2(2^128 − 1)` rounds to exactly `128.0` in float64 and silently
flipped every boundary case.  All verdicts are now taken from the certified
Decimal comparator (`balance()`, 140-digit context with an explicit
`10^-110` pad and a `10^-40` UNDECIDED gate).  My own PREREG §7 forbade the
float compare; the clause caught it.

---

## 4. L2/L3/L4 — the band rows

### 4.1 The band window admits NO stratum decomposition

`notes/pilots_20260804/mun_anticoncentration/REPORT.md:30`

> **Scope split first (measured, `verify_bandlinear.py`).** The mandate asked for the cyclic-code form. That form is **exact for the crossing consumer and only a relaxation for the band consumer**

and its row table `:49` records the band window as

> | band 1/4 | `F_q`, `q >= 2^209` | `2^41`, `k=2^39` | `2d` generic forms, `d in [2^32+1, 2^33-1]` | not cyclic, not a slice |

The C4-a free-vanishing mechanism needs the conditions to be indexed by
cyclotomic exponents (`p_s`, `s` in a prefix): only then does `2^a ∤ s`
force `p_s(T) = 0` automatically.  `2d` **generic** `F_q`-linear forms on
locator-coefficient space have no such index, so no condition vanishes for
free on a coset union.  **There is no stratum decomposition of the band
window system; the only instance is `a = 0`.**  Likewise there is no
cyclotomic closure: `c = 2d` exactly, and the base is `q` (the forms have
`F_q` coefficients), so the balance bits are `2d·log2 q`.

### 4.2 Band-proper depth, verbatim

`notes/pilots_20260803/mint3_prep/WIRING.md:59`

> BAND PROPER here means the PILOT's upper window d in [ceil(h/2), h-2] (PREREG.md:26), NOT definitions item 2's [1, h-2] -- the distinction is carried everywhere.

`critical/nodes/xr_band_maximal_window_divisor_count/statement.md:5`

> - **scope:** the three prize rows and high band-proper depths

so the lowest depth `d = ceil(h/2)` IS in scope.

### 4.3 Verdicts

Global balance needs `log2 q >= n/(2d)`, and `log2 q < 256`, so it needs
`d > n/512 = 2^32`.

| rate | band-proper `d` | `d > 2^32`? | verdict |
|---|---|---|---|
| 1/4 | `[2^32+1, 2^33−1]` | yes, barely | FLIPS: sub-balance only for `d >= n/(2 log2 q)` |
| 1/8 | `[2^32+1, 2^33−1]` | yes, barely | same |
| **1/16** | `[2^31+1, 2^32−1]` | **NO** | **NEVER — above balance at every admissible `(q,d)`** |

Rate 1/16 in exact integers: `2d <= 2^33 − 2` and `log2 q < 256` give

```
2d·log2 q  <  (2^33 − 2)·256  =  2^41 − 512  <  2^41 = n.
```

The deficit is at least **512 bits even in the limit `q → 2^256`**, and it
grows to `2^41 − (2^32+2)·256 ≈ 2^41/2` at the bottom of the depth range
(required `log2 q = 511.99999976` there).

For rates 1/4 and 1/8 the above-balance zone is the low-depth end:

```
required log2 q at d = 2^32+1  :  255.999999940   (window to the 256 cap: 6e-8 bits)
above-balance zone at log2 q=209 :  d in [2^32+1, 5260821185]  (22.5% of band-proper)
above-balance zone at log2 q=250 :  d in [2^32+1, 4398046511]  ( 2.4% of band-proper)
```

### 4.4 CATCH-D — the `q >= 2^209` pin is a PER-WEIGHT threshold

`notes/pilots_20260803/sl2_unstructured/descent.py:211-213` computes

```
log2_q_critical = (lbinom(n, n - k - dlo) - b) / (2.0 * dlo)
```

i.e. `(log2 C(n,r') − log2 budget)/(2d)` — the REFUTED per-weight functional
(minus the budget).  `esg_selftest.py` reproduces
`208.47593052630532` to `< 1e-6` and confirms the `9.48e-9` offset from the
mun reading is exactly `log2(0.68 n^2)/(2d)`.  The corresponding **(ES-G)**
threshold at the same depth is `n/(2d) = 255.999999940` — **47.5 bits
higher**.  The band lane's field pin therefore does not deliver (ES-G) at
the depth it was computed for; it delivers the retired functional.

### 4.5 The syzygy lane's rank bracket

`critical/nodes/xr_band_forced_commonroot_syzygy_count/statement.md:105`

> dim K_d<=d-ell-|G_d|<=3d-2h-ell.                   (SL2-ABN)

The effective condition count is `rank J_d = 2d − dim K_d`, so
`rank J_d ∈ [2h − d + ell, 2d]`.  Both ends reported (PREREG §7):

| rate | depth | `c = 2d` | `c = rank_min` (`ell=0`) | verdict(2d) | verdict(rank_min) |
|---|---|---|---|---|---|
| 1/4, 1/8 | `d_lo = 5726623063` | `11453246126` | `11453246123` | ALWAYS | ALWAYS |
| 1/4, 1/8 | `d_hi = 8589934591` | `17179869182` | `8589934595`  | ALWAYS | **FLIPS** |
| 1/16 | both | — | — | **NEVER** | **NEVER** |

---

## 5. L5 — the u2c pin

`background/nodes/u2c_giant_tnull_dichotomy/node.json:10`

> "falsifier": "Pre-registered: sub-balance (q^t >= 2^n) scaled rows with non-coset-union extras exceeding the transported n^3 budget, sustained across >= 3 scales. Above-balance window accidents do NOT count."

and the statement it guards, `node.json:8`

> REPAIRED CLAIM: at rows with q^t >= 2^n (sub-balance everywhere; all official prize-max rows qualify by ~2%): every t-null block is a union of mu_M-cosets (M >= t) with zero-sum value patterns at multiples of M <= t.

**This is the GLOBAL form verbatim.**  The five round-16 witnesses, checked
by exact integer comparison `p^{|Z_w|}` vs `2^32`:

| `r'` | `w` | `p` | `delta` | `|Z_w|` | `Lam` (per-weight) | `log2 p^{|Z_w|}` | vs `n=32` |
|---|---|---|---|---|---|---|---|
| 6 | 4 | 7   | 4 | 10 | −8.284 | 28.074 | ABOVE |
| 6 | 3 | 47  | 2 | 4  | −2.429 | 22.218 | ABOVE |
| 6 | 4 | 17  | 2 | 5  | −0.648 | 20.437 | ABOVE |
| 5 | 2 | 23  | 4 | 4  | −0.475 | 18.094 | ABOVE |
| 5 | 2 | 463 | 2 | 2  | −0.090 | 17.710 | ABOVE |

All five are above the global boundary — round 16's claim
(`es REPORT.md:46`: "**0 of my 5 witnesses are below the global boundary.**")
**CONFIRMED independently**, and my machinery recomputes the report's own
`|Z_w|` column and `Lam` values (`esg_selftest.py` block (D), `esg_analysis.py`
L5 block asserts `|Lam_recomputed − Lam_banked| < 5e-3`).

Note the falsifier is strictly STRONGER than sub-balance: it also demands
extras beyond the `n^3` budget "sustained across >= 3 scales".  The five
witnesses fail it on all three counts.

### 5.1 CATCH-E — drift between the pinned wording and (ES-G)

Three drifts, all inside the same node:

1. **`q` vs the generated field.**  `node.json:8` CATCH #11 says the frozen
   `q`-wording is untenable:
   > the sub-balance window must be read at the GENERATED field B0 = F_p(D), i.e. |B0|^t >= 2^n, NOT at the ambient q. … The frozen q-scale wording is therefore untenable at such rows
   The falsifier at `node.json:10` still says `q^t >= 2^n`.  (ES-G) says
   `p^{|Z_w|}`.  **Three different bases in one node**; for the crossing
   instance THEOREM Q settles it in favour of the smallest one (`p`), which
   is also the least favourable.
2. **The "~2%" prose.**  `node.json:8` claims "all official prize-max rows
   qualify by ~2%".  The node's own 3C annotation contradicts it:
   > I3 — the '~2% sub-balance' prose is wrong in both directions: the exact admissible prize-max sliver is log2 Q in [255.9113, 256), width 0.089 bits
   So u2c's sub-balance is not a 2% margin but a 0.089-bit sliver at the very
   top of the field range.
3. **Consequence for the shared terminal.**  u2c's sliver requires
   `log2 Q >= 255.9113`; the band lanes' (ES-G) thresholds require
   `log2 q >= 255.99999994` (1/4, 1/8 at low depth) or `>= 256` (1/16); the
   dli RES lane requires the OPPOSITE inequality (§6).  These cannot all be
   satisfied at one row.

---

## 6. The dli RES lane — CATCH-F, the decisive one

`critical/nodes/dli_prime_weighted_large_block_support/DLI_CLOSE_PINNED.md:162-166`

> ## ROUND-4 SCOPED TARGET (the production row class, finally pinned)
> Row class R*: X = c * (full half-section of mu_{n'}), N = n'/2, with
>     2^N >= q^L    (balanced-volume / matched-alpha; automatic at production:
>                    N = 256L and q < 2^256).

`critical/nodes/dli_c1r3_gated_envelope_bound/statement.md:12`

> (H2)  2^N >= q^L,  N >= 16L,

`critical/nodes/dli_prime_weighted_large_block_support/notes/m4_report.md:107-108`

> - **A2** balance: `r_L = q^L / 2^{256L} < 1` for every admissible
>   `q < 2^256` — exact integer inequality at L = 1, 2, 34.

`2^N >= q^L` with `N = 256L` is **exactly the negation of global balance**
(`q^L >= 2^N`), and it is PROVED as a strict inequality for every admissible
`q < 2^256`, at every one of the 34 levels.  The dli RES production rows are
therefore **STRICTLY ABOVE global balance, by proof, everywhere** — and the
condition is not incidental, it is a scoping HYPOTHESIS of the lane (H2):
the round-4 refutation witness was diagnosed as *outside* R* precisely
because it violated it (`DLI_CLOSE_PINNED.md:160`: "q=97 violates 2^N >= q^L
(4096 < 9409). THE WINDOW LAW, FIFTH INSTANCE.").

The dli lane's object is a FLATNESS statement (`E_U[rho_j] <= 4` per level,
`rho_j = q^{L_j}|Z_j|/U_j`), which is only meaningful when the mean is `>= 1`,
i.e. above balance.  (ES-G) is a ZERO-COUNT statement conditioned on
sub-balance.  **They are the same shape in opposite regimes.**

This falsifies the round-15 discharge claim at `mun REPORT.md:53`:

> **(ES) discharges all four consumers.** … **dli RES**: same file, *"the SAME hard shape as the dli RES count."*

"Same hard shape" was read as "discharged by".  It is not: the shape is
shared, the regime is disjoint.

Also relevant, the dli lane's own analogue of CATCH #11 —
`critical/nodes/dli_prime_weighted_large_block_support/notes/f1_beta_check.md`
(catch #13) proves the "L_j genuinely independent `F_q`-conditions" clause
false at base-domain extension rows, with mis-pricing `(q/p)^{L_j}`.  That is
the same defect this pilot finds at the crossing row via THEOREM Q: the
value field is the generated one, not the ambient `q`.
