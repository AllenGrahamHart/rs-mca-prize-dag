# REPORT — l1_ell_sweep (persisted verbatim by the coordinator from the session transcript, task ad4f92852e755bdbd, 2026-08-07)

All compute is done and every artifact is confined to the draft directory. Final report:

---

# L1-N10-ELL — the decisive ell-sweep (round 22 pilot, `notes/pilots_20260807/l1_ell_sweep/`)

**Headline: F-w1 did not fire, and at four cells it now provably *cannot* fire for any received word in the chart family — including the deepest reachable proper-band cell, `n=32, ell=5` (t=3, Λ=10, BOX = 1,606,481,810), where the test is exhaustive over all 9,216 legal projective words.** The random-word law survives the sweep to `ell=6` with the shell-resolved ratio flat to ~1%. The sweep also turned up a **bug in the round-21 machinery** (harmless to every banked number) and a **methodological finding: F-w1's own normaliser gets weaker as `ell` grows**, which I fix with a sharper one.

No status flip, no closure claim. Census evidence is evidence, never proof.

## 0. What was registered, and when

Registrations were appended to `PREREG.md` at 2026-08-07T06:48:10Z (HEAD `5ac7a5a52`) **before any computation** — closed form, per-cell predictions P0–P9, the full word search space, layouts, and the epistemic-labelling contract. Amendments and post-hoc additions are recorded separately at the end of that file (section "AMENDMENTS AND SELF-CORRECTIONS"), each flagged as pre-registered or not.

Sources quoted verbatim:

- `critical/nodes/l1_mixed_petal_amplification/statement.md:1366-1368`:
  ```
  #core kept a &lt;= Lambda := 2*ell + b - 2,   #petal lost om &lt;= Lambda + 1 - sigma
  =&gt;  the bucket is EMPTY when sigma &gt; Lambda, and otherwise
      BOX = Theta(C(k-1,Lambda) * C(t*ell,Lambda)) = Theta(n^{2*Lambda}).
  ```
- `notes/pilots_20260807/l1_pma_diag/REPOSE_DRAFT.md:62-67` (F-w1): *"FALSIFIED IF an `ell`-sweep at a fixed row returns a retained count exceeding `10 * BOX(ell)/q`, i.e. a word whose mixed floor-band mass is an order of magnitude above its own box-over-field prediction."*
- `REPOSE_DRAFT.md:70-72` (F-w2): *"A mixed-petal floor-band contributor at `sigma &gt; 2*ell + b - 2` in any maximal source chart."*

## 1. Replication gate (P2) — ALL PASS, by three independent code paths

`gate.py` + `brute.py` (direct Vandermonde solve, no dual conditions, no barycentric identity). Every banked number of record reproduced **exactly, including both histograms**:

| cell | banked | engine | brute |
|---|---|---|---|
| `16,8,97` consec / geom5 (LAYOUT-B) | 43 / 33 | 43 / 33 | 43 / 33 |
| `32,16,97` consec / geom5 (LAYOUT-B) | 2,879 / 2,857 | ✓ | — |
| `64,32,193` consec (LAYOUT-B) | 109,391, `33:109329, 34:62`, `2:987, 3:108404` | **character-identical** | — |
| `64,32,193` geom5 | 108,600, `33:108547, 34:53`, `1:6, 2:1001, 3:107593` | **character-identical** | — |
| round-21 LAYOUT-A n=24 ell=2/3/4 | 475 / 8,135 / 20,942 | ✓ | 475 ✓ |
| candidate totals BOX | 5,096 / 386,640 / 27,152,032 | closed form = enumeration, all cells | ✓ |

Round-21's two headline n=32 adversarial numbers also reproduced independently: the minimal-degree word gives **RET = 3,273** (`REPORT.md:47`: *"best found = 3,273, the minimal-degree word"*), and the filter-extremal word collapses to **RET = 122** (`REPORT.md:50`: *"exactness collapses it to 122"*).

## 2. SELF-CORRECTION: a bug in `d3_ell_sweep.py` (does not affect any banked number)

`d3_ell_sweep.py:84-86`:
```python
                            m = a + nb - om
                            drop = list(K) + list(B)
                            R = set(drop[:m - 1])
```
Two defects, both found before I reported anything downstream:

1. **`b &gt;= 2`**: `drop[:m-1]` reduces the support to a **k**-point set, not `k+1`; requiring the divided difference to vanish there is *stronger* than membership, so the filter under-counts. All round-21 cells have `b&lt;=1`, so nothing banked is touched — but two of my n=32 cells (`ell=3,5`) have `b=2`, so I could not reuse that filter.
2. **`b = 0`**: the whole `r=1` shell has `m=0`, and Python's `drop[:-1]` then deletes all but the last core point. This is why `d3` prints **`n=16 ell=3 → retained 0`**. The true value is **100**, confirmed independently by the engine and by `brute.py` with identical histograms `a={2:16, 3:30, 4:54}`, `agr={9:100}`. That number is not quoted in the round-21 REPORT or the node addendum.

My engine instead uses the exact necessary-**and**-sufficient existence test for `|S| = k+r` (derived and registered in R1 before measuring):
`sum_{j in S} U_j x_j^{s+1} prod_{l in D\S}(x_j - x_l) = 0` for `s = 0..r-1`, using `prod_{l != j}(x_j-x_l) = n x_j^{-1}` on `mu_n`. It factorises into one float64 matmul per stratum (exact: entries &lt; 16·96² = 147,456), which is what made the big cells reachable.

## 3. (D1) THE SWEEP — exact retained counts [MEASURED, exhaustive enumeration]

`BOX_enum == BOX_closed_form` at **every** cell (P1 CONFIRMED, DERIVED+CHECKED). The registered closed form is
`N_{k+r} = Σ_{a&lt;=Λ} Σ_{nb&lt;=b} C(k-1,a) C(b,nb) [C(tℓ,om) − [ℓ|om]·C(t,om/ℓ)]`, `om = a+nb−b+1−r`.

| n | ell | L | t | b | Λ | BOX | RETPRED | consec | geom5 | mindeg | max over words | band |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 24 | 2 | A | 6 | 1 | 3 | 64,812 | 464 | 475 | 472 | 452 | 518 | proper |
| 24 | 3 | A | 4 | 1 | 5 | 1,518,792 | 8,138 | 8,135 | 8,127 | 8,067 | 8,270 | proper |
| 24 | 4 | A | 3 | 1 | 7 | 5,326,002 | 20,748 | 20,942 | 20,861 | 20,786 | 20,966 | proper |
| 24 | 5 | A | 2 | 3 | 11 | 7,007,285 | 23,091 | 22,865 | 22,905 | 22,979 | 23,061 | **VACUOUS** |
| 24 | 6 | A | 2 | 1 | 11 | 7,029,263 | 23,136 | 22,573 | 22,427 | 22,518 | 22,693 | **VACUOUS** |
| 32 | 2 | A | 8 | 1 | 3 | 386,640 | 2,825 | 2,802 | 2,808 | 2,882 | 2,922 | proper |
| 32 | 2 | B | 8 | 1 | 3 | 386,640 | 2,825 | 2,879 | 2,857 | **3,273** | 3,273 | proper |
| 32 | 3 | A | 5 | 2 | 6 | 141,743,379 | 745,054 | 745,964 | 745,352 | 744,270 | 746,024 | proper |
| 32 | 4 | A | 4 | 1 | 7 | 407,151,656 | 1,857,423 | 1,858,828 | 1,856,179 | 1,858,625 | 1,858,828 | proper |
| 32 | 4 | B | 4 | 1 | 7 | 407,151,656 | 1,857,423 | 1,853,322 | 1,853,649 | 1,861,102 | 1,861,102 | proper |
| 32 | 5 | A | 3 | 2 | 10 | 1,606,481,810 | 4,856,351 | 4,857,063 | 4,857,042 | 4,855,659 | 4,857,063 | proper |
| 64 | 2 | A | 16 | 1 | 3 | 27,152,032 | 108,961 | 109,158 | 108,609 | 108,587 | 109,744 | proper |
| 64 | 2 | B | 16 | 1 | 3 | 27,152,032 | 108,961 | 109,391 | 108,600 | **127,964** | 127,964 | proper |
| 64 | 3 | A | 11 | 0 | 4 | 1,503,785,448 | 5,791,976 | 5,800,082 | — | — | 5,800,082 | proper |

Everything the brief asked for was reached and then some: n=32 ell=2,3 **and** ell=4 **and** ell=5; n=24 out to ell=6; plus n=64 ell=2,3 (grid extension A5).

**P0 CONFIRMED, and it matters:** the brief's `n=24, ell=5,6` cells both give `t=2`, hence `Λ = 11 = k−1` — the floor band `d &gt;= ell(t−2)` is **vacuous** there. They are measured and reported, but they are not points on the floor-band curve. The genuine proper-band frontier reached is `n=32, ell=5` (t=3, Λ=10).

## 4. (D2) THE F-w1 TEST — silent everywhere, and *exhaustively* silent at four cells

### 4a. Direct test on the declared word space [MEASURED / SEARCHED / SAMPLED]

Across 14 cells and 71/51/23/14/6/3/1 words per cell (schedules + minimal-degree + random + RANSAC), the largest `RET/(BOX/q)` observed anywhere is **0.9096** (n=64 ell=2 LAYOUT-B, mindeg). F-w1 needs `&gt; 10`. **Largest observed `RET/(10·BOX/q)` = 0.09096 — an 11x headroom at the tightest cell, and 34x at n=32 ell=5.** No word came within an order of magnitude of firing.

*Honest scope*: RANSAC maximises FILT, and round-21 already showed FILT is **anti**-correlated with RET at the extreme. I reproduced that mechanism at every large `ell`: at n=24 ell=4 the filter-extremal word spikes FILT to 2,034,714 (88x mean) and `RET = 0`; at n=24 ell=6, FILT = 2,839,055 and `RET = 0`; at n=32 ell=3, FILT = 11,942,684 and RET = 375,674 (half the mean). So a search alone cannot bound the true max — which is why I built the next instrument.

### 4b. The word-uniform upper bound `UB` — NOT pre-registered (amendment A3)

For every candidate `S`, a degree-`&lt;k` interpolant exists only if `g^{(0)}(S)·c = 0`, and `g` does not depend on `c`. Hence one pass over the cell gives the histogram of `g` over `F_97^t`, and `RET(c) &lt;= FILT(c) &lt;= UB(c) := #{S : g(S)·c = 0}` for every word. When `t &lt;= 3` the legal word space is 96 or 9,216 projective points, so `max_c UB(c)` is **enumerated, not searched**.

| n | ell | L | t | words | kind | max UB | 10·BOX/q | maxUB/thr | # over |
|---|---|---|---|---|---|---|---|---|---|
| 24 | 2 | A | 6 | 4,003 | search | 778 | 6,682 | 0.116 | 0 |
| 24 | 3 | A | 4 | 2,003 | search | 18,992 | 156,576 | 0.121 | 0 |
| 24 | 4 | A | 3 | **9,216** | **EXHAUSTIVE** | 2,034,714 | 549,072 | 3.706 | **1** |
| 24 | 5 | A | 2 | **96** | **EXHAUSTIVE** | 446,532 | 722,401 | 0.618 | **0** |
| 24 | 6 | A | 2 | **96** | **EXHAUSTIVE** | 2,839,055 | 724,666 | 3.918 | **1** |
| 32 | 2 | A | 8 | 20,003 | search | 5,218 | 39,860 | 0.131 | 0 |
| 32 | 2 | B | 8 | 20,003 | search | 12,714 | 39,860 | 0.319 | 0 |
| 32 | 4 | A | 4 | 1,503 | search | 4,639,185 | 41,974,398 | 0.111 | 0 |
| 32 | 5 | A | 3 | **9,216** | **EXHAUSTIVE** | 263,632,666 | 165,616,681 | 1.592 | **1** |

At exactly **one** word per cell does the bound exceed the threshold, and it is the same word every time: the constant-scalar word `c = λ·(1,…,1)`. Each was adjudicated exactly:

- n=24 ell=4, `c=(1,1,1)`: **RET = 0** (measured, full engine).
- n=24 ell=6, `c=(1,1)`: **RET = 0** (measured, full engine).
- n=32 ell=5, `c=(1,1,1)`: **RET = 1,594,308** vs threshold 165,616,681 → ratio **0.0096**.

The n=32 ell=5 case exceeds the ramguard local wall (its FILT is ~2.6e8), so I derived its exact structure (`degen_word.py`, amendment A4, NOT pre-registered): for `c = λ·1`, `U` agrees with the **codeword** `λL_C` on all of `D\B`, so any other contributor `P'` has `P'−λL_C` nonzero of degree `&lt;k`, hence `|S ∩ (D\B)| &lt;= k−1`, hence `r &lt;= nb−1 &lt;= b−1`. **Corollary: `RET(λ·1) = 0` whenever `b &lt;= 1`** — which is exactly what was measured at both n=24 cells. For `b = 2` this forces `r=1`, `nb=b`, `a=om`, `V = μ·L_{S'}`, and one consistency equation `f(K)·h(O) = ρ`, countable by histogram. **CHECKED**: the formula returns 375,674 at n=32 ell=3 and the full engine returns **375,674** — exact agreement.

&gt; **Verdict (D2): F-w1 does NOT fire at any cell. At n=24 ell=4, n=24 ell=5, n=24 ell=6 and n=32 ell=5, F-w1 *cannot* fire — for every received word of the chart family, not merely for the words searched.** This is an exhaustive statement over a fully enumerated word space, not a search maximum. At the remaining cells (t &gt;= 4) the statement is a search over 1,503–20,003 words plus the schedules/mindeg, and is a **lower bound on the true max**.

## 5. F-w2 and the scope of clause (a)

**F-w2 did not fire.** I said in advance (P4) that the in-family version is *tautological*: mixed ⟹ `om &gt;= 1`, and floor band ⟹ `a &lt;= Λ`, so `|S| &lt;= Λ + b + tℓ − 1 = k + Λ`. A census cannot falsify a definition, and I will not present it as if it could.

The non-tautological test I registered instead — **drop the floor band entirely** and see how far `sigma` actually reaches:

| cell | BOX (band off) | RET | agreement histogram | core histogram |
|---|---|---|---|---|
| n=16 ell=2, Λ=3 | 24,608 | 109 / 110 | `9:105, 10:4` / `9:109, 10:1` | up to a=6 |
| n=16 ell=3, Λ=4 | 25,884 | 123 / 91 | `9:123` / `9:91` | up to a=6 |
| n=24 ell=2, Λ=3 | 6,922,520 | 23,094 / 22,806 | `13:22897, 14:197` / `13:22633, 14:170, 15:3` | up to a=10 |

With the band gone the formal agreement ceiling at n=24 ell=2 is `k+11 = 23`; the **measured** maximum is `15 = k+3 = k+Λ`. So the exact-agreement semantics enforce `sigma &lt;= Λ` on their own at these cells — clause (a)'s conclusion is not carried by the band definition alone. Separately, the band is a real restriction: dropping it multiplies the mixed mass by **48.6x** at n=24 ell=2 (23,094 vs 475) and 107x in candidate count.

## 6. (D3) THE LAW IN ELL — it holds, to ~0.1% at the large cells

Registered law: `RETPRED = Σ_r N_{k+r}(ell) q^{-r} (1−1/q)^{n−k−r}`. Measured `EXC = RET/RETPRED` on the schedule words:

- n=24: 1.0241/1.0176, 0.9996/0.9986, 1.0093/1.0054, 0.9902/0.9919, 0.9757/0.9694
- n=32: 0.9920/0.9941, 1.0193/1.0115, 1.0012/1.0004, 1.0008/0.9993, 0.9978/0.9980, **1.0001/1.0001** (ell=5)
- n=64: 1.0018/0.9968 (A), 1.0039/0.9967 (B), 1.0014 (ell=3)

**Worst deviation on any schedule word, at any cell: 3.1%.** At the three largest cells (BOX 1.4e8, 4.1e8, 1.6e9) the law is accurate to **0.1%**. **P6 CONFIRMED. No amplification signal emerged at any `ell` up to 6.**

## 7. (D4) THE CLAUSE-(b) SHAPE — and a fix to the falsifier's normaliser

`RATIOBOX = RET/(BOX/q)` (the F-w1 normaliser) **shrinks monotonically in `ell`** — P5 CONFIRMED, and predicted quantitatively before measurement:

- n=24 LAYOUT-A: 0.7109 → 0.5196 → 0.3814 → 0.3165 → 0.3115 (closed-form prediction 0.6942/0.5198/0.3779/0.3196/0.3193 — agree to ~2%)
- n=32 LAYOUT-A: 0.7030 → 0.5105 → 0.4428 → 0.2933
- n=64 LAYOUT-A: 0.7759 (ell=2) → 0.7444 (ell=3)

**The cause is a defect in the falsifier, not a property of the object.** `BOX` sums *all* shells `Σ_r N_{k+r}`, but the mass lives at `r=1`; as `ell` grows the deep shells swell (`N_{k+2}/N_{k+1} ≈ Λ/(tℓ−Λ+1)`, and `N_{k+1}/BOX` falls 0.826 → 0.593 → 0.514 → 0.340 at n=32). So **F-w1's threshold `10·BOX/q` becomes progressively more generous as `ell` grows — up to 2.9x more generous at n=32 ell=5 — exactly in the regime the re-pose says carries the content.**

The shell-resolved normaliser I registered, `RATIOSHELL = RET/(N_{k+1}/q)`, is **flat**:

| n | measured RATIOSHELL across ell | `(1−1/q)^{n−k−1}` |
|---|---|---|
| 24 | 0.9161, 0.8965, 0.9073, 0.8908, 0.8777 | **0.8923** |
| 32 | 0.8508, 0.8612, 0.8618, 0.8634 | **0.8560** |
| 64 | 0.8532, 0.8550, 0.8489, 0.8530 | **0.8513** |

i.e. `RET = (1−1/q)^{n−k−1} · N_{k+1}/q` to ~1%, with no `ell` dependence at all. **Recommendation to the coordinator: re-state F-w1 against `N_{k+1}/q`, not `BOX/q`.** Under that normaliser the observed headroom is a uniform ~11x rather than a drifting 11–34x, and the test stays sharp at large `ell`.

**Extrapolation to `ell = Ω(n/log n)` [EXTRAPOLATED from the measured law — NOT measured, NOT proved]:**

Two honest caveats first. (i) The controlling parameter of the asymptotic regime is `t = (k+1)/ell`, not `ell`: at official rows `ell = Θ(n/log n)` gives `t = Θ(log n)`, which *grows*. My fixed-`n` sweep moves `t` **down** (16→8→5→4→3→2), so it probes the small-`t` end — the end where the band is closest to vacuous, i.e. the conservative direction. (ii) The law is a random-word law; adversarial words are bounded only by §4.

With that, extrapolating `MASS(σ) = Σ_{r&gt;=σ} N_{k+r} q^{-r}(1−1/q)^{n−k−r}` (`d4_extrap.py`):

| n | log2 q | t | ell | Λ | log2 MASS(σ=1) | log2 MASS(σ=ell−1) |
|---|---|---|---|---|---|---|
| 2^13 | 31 | 13 | 315 | 630 | +5,032 | **−5,598** |
| 2^20 | 31 | 20 | 26,214 | 52,435 | +491,775 | **−416,513** |
| 2^41 | 31 | 41 | 26,817,356,775 | 53,634,713,550 | +618,351,697,603 | **−340,273,263,757** |
| 2^41 | 128 | 41 | 26,817,356,775 | 53,634,713,550 | +618,351,697,506 | **−2,941,556,870,835** |

The census threshold `σ=1` sits astronomically **above** 1; the consumer threshold `σ = ell−1` (the listing bound `ell &gt;= σ+1`) sits astronomically **below** 1. This is round-21's D1-1 finding made quantitative in `ell`: the two regimes are separated by ~10^12 in log2 mass at official rows, and the separation is driven entirely by the `q^{-σ}` factor. Under the measured law, clause (b) would hold with enormous margin — but this says nothing at all about an adversarial word family, which is precisely the open content.

## 8. Registered predictions vs outcomes

| | prediction | outcome |
|---|---|---|
| **P0** | n=24 ell=5,6 have t=2, band vacuous | **CONFIRMED** ((2,3) and (2,1); Λ=11=k−1) |
| **P1** | closed form = enumerated BOX everywhere; = 5,096 / 386,640 | **CONFIRMED** at all 14 cells, incl. 27,152,032 at n=64 |
| **P2** | replication gate exact | **PASSED** after one adjudicated target correction (§2) |
| **P3** | F-w1 does not fire | **CONFIRMED**; max `RET/(10·BOX/q)` = 0.09096 |
| **P4** | no contributor at σ&gt;Λ | **CONFIRMED**; in-family tautological (stated in advance); off-family test in §5 |
| **P5** | RATIOBOX strictly decreasing in ell | **CONFIRMED**, and matched quantitatively to ~2% |
| **P6** | \|EXC−1\| &lt;= 0.10 on schedule words | **CONFIRMED**; worst 3.1% |
| **P7** | EXC(mindeg) &lt;= 1.30, not monotone in ell | **CONFIRMED**; max 1.1744 (n=64 LAYOUT-B). Sharper finding below. |
| **P8** | MAXEXC &lt;= 3.0 at n=32 | **CONFIRMED**; max 1.159 (SEARCHED — lower bound on the true max) |
| **P9** | trend bounded on extrapolation | **CONFIRMED** with the caveats in §7 |

**Sharper finding on P7.** Round-21's "~16% structural excess of the minimal-degree word" is **a coset-layout, `ell=2` phenomenon, not a degree phenomenon**: at LAYOUT-B it is 15.87% (n=32, deg U = 17 = k+1) and 17.44% (n=64, deg U = 33 = k+1), but at LAYOUT-B `ell=4` it is **0.20%** (deg U = 19), and at LAYOUT-A it is ≤2% at every cell (n=64 LAYOUT-A mindeg has deg U = 48 and EXC = 0.9966). The excess is carried by the `mu_2` antipodal symmetry of the petals, which dies once petals are `mu_4` cosets. That is the only structural excess this pilot found anywhere, and it does not grow with `ell`.

## 9. Costs, and what I did not run (no Modal launched)

Measured local throughput: **1.98e7 candidates/s/word** (n=32 ell=5: BOX 1,606,481,810 in 81 s/word, `ramguard local`, 1 GiB).

Reachable but skipped for session time (amendment A6): n=32 ell=6 and ell=8 (BOX ≈ 1.85e9, ~93 s/word — both `t=2` vacuous-band, already covered by the n=24 `t=2` cells); n=48 ell=3 (BOX 2.44e9, ~123 s/word).

Genuinely out of local reach — **Modal request lines for the coordinator** (I launched none):

```
L1-N10-ELL-64-4 : n=64, q=193, LAYOUT-A, ell=4 (t=8, b=1, Lambda=7),
                  BOX = 15,968,151,894,992, ~224 CPU-h per word,
                  4 words (consec, geom5, mindeg, 1 random) ~ 895 CPU-h, 1 GiB
L1-N10-ELL-48-4 : n=48, q=97,  LAYOUT-A, ell=4 (t=6, b=1, Lambda=7),
                  BOX = 205,253,983,244, ~2.87 CPU-h per word,
                  8 words ~ 23 CPU-h, 1 GiB     &lt;-- best value of the three
L1-N10-ELL-64-5 : n=64, q=193, LAYOUT-A, ell=5 (t=6, b=3, Lambda=11),
                  BOX = 37,169,887,044,546,200, ~520,593 CPU-h per word
                  -- DO NOT LAUNCH; report as out of scope.
```
Also worth a line: the exact evaluation of `c = λ·1` at n=32 ell=5 (FILT ≈ 2.6e8) needs ~15 CPU-min; `degen_word.py` already gives it in closed form (1,594,308), verified against the full engine at n=32 ell=3, so it need not be bought.

## 10. Artifacts (all in `notes/pilots_20260807/l1_ell_sweep/`, nothing else touched)

`PREREG.md` (registrations + amendments) · `cf_cells.py` (closed form + cost map) · `sweep_engine.py` (exact engine) · `brute.py` (independent Vandermonde path) · `gate.py` (replication gate) · `sweep_run.py` (driver, JSONL checkpoints) · `ub_scan.py` (word-uniform upper bound) · `degen_word.py` (constant-scalar word, closed form) · `aggregate.py` · `d4_extrap.py` · `results.jsonl` (142 KB, every word) · `ub_results.jsonl`.

`git status` confirms only `PREREG.md` modified plus new files, all inside the draft directory. No `dag.json`, no `nodes/`, no `tools/`, no git writes, no Modal. Every `python3` invocation went through `tools/ramguard tiny|local -- python3` from the repo root, including all file patching. Quarantine honoured: `CAMPAIGN_LEDGER.md` was never opened, nor were the other three round-22 pilot directories. No subagents were dispatched.

## 11. Bottom line for the coordinator

1. **F-w1 is silent, and at four cells — including the deepest proper-band cell reachable — it is *exhaustively* silent over every received word of the chart family.** That is a stronger outcome than the brief asked for, and it closes the "the search might have missed the max" objection at those cells.
2. **The re-pose should be amended in one place**: F-w1's normaliser `10·BOX(ell)/q` degrades as `ell` grows (2.9x looser at n=32 ell=5). Use `10·N_{k+1}(ell)/q`. `N_{k+1}` has the same registered closed form and is already computed.
3. **`d3_ell_sweep.py` has a `b&lt;=1`-only filter with two failure modes**; it should not be re-run at any `b=0` or `b&gt;=2` cell. Its `n=16 ell=3` output of 0 is wrong (true 100). No banked number is affected.
4. **The n=24 `ell=5,6` cells the brief named are `t=2`, band vacuous** — they measure a different (larger) object and should not be plotted on the floor-band curve. The proper-band frontier is `n=32 ell=5`.
5. **No amplification mechanism appeared at any `ell` up to 6, at any `n` up to 64.** The object is the random-word law to 0.1% at the three largest cells. Clause (b) remains entirely open: the sweep confirms that at reachable scale the census regime and the consumer regime are separated by the `q^{-σ}` factor, and no census at these scales can probe the latter.
