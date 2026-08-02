# Pilot report: F2A.5 b-resolved slice coefficients (Opus 5 subagent, 2026-08-02)

Coordinator note: this file is the subagent's final report, persisted
verbatim by Fable (HTML entities restored). Coordinator verification and
adopted posture: FABLE_AUDIT.md alongside.

---

# F2A.5 pilot — b-resolved slice coefficients of the carry-DFT mode product

**Directory:** `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/f2_slice_coefficients/`
**Headline:** the slice route **has a foothold, and it is not the one the lane expected.** The b-resolved object has an exact product representation governed by a single new invariant (the modified difference multiset `Delta_i` in Z/2p). That invariant immediately produces a **new exact fence that inverts the F2A.4 mode-contraction criterion**: the windows the full-window analysis rates *best* at mode k = p are exactly the windows where the slice cancellation is *pinned at 1/p for every n*. F1 not triggered, F2 not triggered in the blindness sense (but the precision half survives verbatim), **F3 triggered on a named, coordinate-selectable window class.**

## 1. What was built, and the exactness discipline

All algebra is exact in `Z[zeta_p]` (integer vectors of length p modulo `sum zeta^i = 0`); `omega = zeta_2p = -zeta_p^((p+1)/2)`, so the whole model — weights `2cos(pi s/p) = omega^s + omega^-s`, the carry DFT `hhat_p(k) = sum_r h_p(r) omega^-kr` (computed as a finite sum, so **no division is ever needed**) — lives in one integral ring. Zero-testing is exact. Decimals are 60-digit renderings of exactly known algebraic numbers, and the scaled tables are exact **integers**. Floats appear only in SVD/recurrence residuals, labelled.

`verify_slice.py` — **11/11 exact validations PASS** (`F2A5_VALIDATION_ALL_PASS`):

| id | statement |
|---|---|
| V1 | ring, `omega^p = -1`, `omega^2 = zeta`, `2cos` exact |
| V2 | the `(-1)^U` bookkeeping of f2model **cancels the cosine signs exactly** — `sigma.W = h_p(S).prod 2cos(pi s/p)` (192 rows) |
| V3 | brute force over 2^n orientations == graded carry DP (exact, 12 rows) |
| V4 | **the b-resolved mode-product identity**, exact: `2p.A_b = sum_{k odd} hhat_p(k).e_b(A(k);B(k))`; even modes vanish (12 rows) |
| V5 | `|A_i(k)| = a_i^+` for **every** mode -> the annealed slice mass `E_b` is mode-independent (372 rows) |
| V6 | **Krawtchouk identity exact**: `A_b = sum_j D_j K_j(n-b;n)` (20 rows) |
| V7 | `sum_b A_b` == the audited F2A.2 `validate.py` V9 alignment, rel err 1.7e-14 |
| V8 | slice-death criterion, both directions (84 modes, 4 dead) |
| V9 | synthetic witness: common nonzero phase -> **every slice ratio == 1 exactly while the full window contracts** (10.77 < 28.83) |
| V10 | slice x carry counting DP == brute force |
| V11 | `hhat_p(p) = 2` and `|e_b(p)| = E_b` on all-odd-Delta windows -> the k=p mode alone puts `E_b/p` into **every** slice |

`mode_and_coset.py verify` — 3/3 exact (`C1` phase identity, `C2` death dichotomy over 124 modes, `C3` coset containment).

## 2. The exact structure the slice coefficients have

Define `sigma_i^± = s_i^± + p.u_i^±  (mod 2p)`, `u = [2s > p]`, and `Delta_i = sigma_i^+ - sigma_i^-`. Then (all exact):

- **The U-sign is a carry shift.** `h_p(S).(-1)^U = h_p(sum_i sigma_i mod 2p)`. The whole signed alignment is a *pure carry statistic in sigma*; no separate parity bookkeeping exists. (V2)
- **Per-mode product form is exact:** `A_i(k) = omega^{(k+1)s^+} + omega^{(k-1)s^+}`, and the slice coefficient of mode k **is** the elementary symmetric polynomial `e_b(A(k);B(k))`. (V4)
- **The phase law:** for every *odd* k, `A_i(k).conj(B_i(k)) = omega^{k.Delta_i}.a_i^+ a_i^-`, i.e. `arg r_i(k) = pi.k.Delta_i/p`. The mode index acts on the phases by **multiplication by k on the Delta multiset**. (C1)
- **Death dichotomy.** With `G = <Delta_i>`, `D = <Delta_i - Delta_j>`:
  `slice-dead at k  <=>  {k Delta_i} constant  <=>  k in Ann(D)`
  `full-window-dead at k  <=>  {k Delta_i} == 0  <=>  k in Ann(G)`
  and `Ann(D) contains Ann(G)`, **strictly** whenever `D` is a proper subgroup of `G`. (C2, V8, V9)
- **Slicing traps the carry in a coset:** `R_b subset base + b.Delta_1 + D`. The F2A.2 Sharp Law A (full sumset = Z/2p) **does not survive b-resolution** — the b-resolved reachability is governed by the *difference* subgroup, not the sumset. (C3)

Verdicts on the three pre-registered candidates:

**(a) Krawtchouk — DENSE, no foothold.** The identity is exact, but the degree profile is dense and erratic: all n+1 coefficients nonzero and above 1e-3 of max at all five instances; participation ratio 3.76-5.00 out of 11-15; no monotone decay (e.g. p=13, n=12: `0.008 0.112 0.466 0.913 1.000 0.841 0.740 0.490 0.061 0.178 0.138 0.044 0.006`).

**(b) PRODUCT — EXACT, and this is the foothold.** Exact per mode by V4/V5. The k-sum does **not** collapse: the mode matrix `M[k][b] = e_b(k)` has full rank `min(p, n+1)` at 5/5 instances, `sv_2/sv_1 in [0.20, 0.97]` (no rank-1/2 approximation), `sv_min/sv_1 in [3.4e-2, 5.0e-6]` (truncation error far above any 2^-n/3 target). Consistent with the F2A.2 Myhill-Nerode 2p result: the exact object is a width-2p b-graded transfer recursion, and no narrower.

**(c) RECURSION in b — ABSENT at low order.** P-recursive ansatz `sum_l q_l(b) A_{b+l} = 0`, deg `q_l <= d`. Positive control `C(40,b)` at (L,d)=(1,1) gives smallest normalised singular value **1.7e-17**. The real slice sequences give **1.1e-2 ... 2.2e-4** at (L,d)=(2,2) — twelve-plus orders away. Even a *single* mode (pure elementary symmetric) gives 5.8e-4 at (1,1). No hypergeometric/three-term structure.

**=> F1 verdict: NOT TRIGGERED.** The slice coefficients are not unstructured — but the only structure is the exact per-mode product form plus the Delta-phase law. Every *cheap* structure (sparse Krawtchouk, low-order recursion, low-rank mode collapse) is absent.

## 3. The new fence (main finding): the Delta-parity inversion

Since `2p = 2.p` with p prime, and the `Delta_i` are not all congruent mod p (guaranteed for `c` outside F_p), `D contains 2Z/2p` and the only odd candidate for death is **k = p**, with a three-way split:

| class | k = p is... | slice floor |
|---|---|---|
| all `Delta_i` **even** (<=> `f(s^+)=f(s^-)` for all i; contains the whole trace-zero line) | full-window dead **and** slice dead | 1/p |
| all `Delta_i` **odd** (<=> `f(s^+)!=f(s^-)` for all i) | **slice dead but full-window maximally contracting** | 1/p |
| mixed | neither | none |

`hhat_p(p) = 2` exactly, so **the k=p term alone contributes ±E_b/p to A_b at every b** (V11). Census over *all* frequencies (p = 7...31, exhaustive in c): the all-even class is essentially the trace-zero line (p-1 frequencies, plus a handful of small-window accidents); the odd-Delta fraction over the full pair set is 0.490-0.499 at every generic c. **So the all-odd class is reachable at ANY frequency by selecting the ~half of coordinates with odd Delta.**

The inversion is the point: F2A.2/`resonance.py` established "the k=p mode contracts a pair iff `f(s+) != f(s-)`, measured frequency ~1/2" as a *health* criterion. **Those are exactly the pairs that are fatal at fixed b.** An F2A.4 mode-contraction compiler written from the full-window criterion ranks windows exactly backwards for the b-resolved theorem, and its exceptional-owner list must be `Ann(D)`, not `Ann(G)`.

Measured, exact integers, `V_b = sum_{|tau|=b} h_p(sum sigma_i)`:

| p | window | n | worst central slice -log2 rho | log2 p | full-window -log2 |
|---|---|---|---|---|---|
| 23 | odd-Delta | 96 | **4.5207** | 4.5236 | 36.28 |
| 41 | odd-Delta | 96 | **5.3550** | 5.3576 | 39.98 |
| 67 | odd-Delta | 96 | **6.0627** | 6.0661 | 38.16 |
| 101 | odd-Delta | 96 | **6.6473** | 6.6582 | 34.80 |

and the exact `(-1)^b` signature (p=13, n=32, `p.V_b/C(n,b)` for b=10...22):
`-0.977 +1.318 -0.955 +0.747 -1.090 +1.214 -0.862 +0.823 -1.180 +1.159 -0.743 +0.887 -1.340`

i.e. `V_b ~ (-1)^{b+1} C(n,b)/p`. **The model generates its own parity modulation, at relative scale 1/p rather than 2^-n/6, and the full window annihilates it by summing over b.**

## 4. Both fences run through the slice statistic

**Fence (ii), full-cube parity constant on slices — CONFIRMED, and now realised inside the model.** Separation between the full-window exponent and the worst central slice exponent, exact integers:

| p | window | n=48 | n=96 |
|---|---|---|---|
| 23 | mixed | 6.05 bits | 12.89 bits |
| 41 | mixed | 4.92 | 13.77 |
| 67 | mixed | 5.59 | 11.50 |
| 101 | mixed | 3.79 | 11.37 |
| 23 | odd-Delta | 17.68 | **31.76** |
| 67 | odd-Delta | 14.06 | **32.10** |
| 101 | odd-Delta | 9.20 | **28.15** |

A full-window theorem overstates the b-resolved exponent by 4-13 bits generically and by up to 32 bits on the odd-Delta class. **Confirmed on this implementation: a full-window mode theorem is worthless at fixed b.**

**Fence (i), hidden modulation — VISIBLE, but the precision problem survives verbatim.**

- *Uniqueness (new, exact):* brute force over all ±1 functions on {0,1}^n for n=2,3,4 finds **exactly two** with every below-full-degree Fourier coefficient zero, and they are `±(-1)^|x|` (Parseval: `|fhat(top)|=1` forces `f = ±chi_top`). **The extremal hidden modulation is forced to be the parity** — so fences (i) and (ii) are the same object seen from two sides.
- *Visibility:* for `w = 1 + 2^-{n/6}.eps`, every proper marginal is **exactly flat** (verified exhaustively at n <= 12), while the slice-mass profile deviates by **exactly ±2^-{n/6}**. Slicing therefore strictly increases resolution: it reduces a 2^n-dimensional joint-bias question to an (n+1)-dimensional profile question at the *same* precision.
- *Reversal, exact:* full-cube alignment/||w||_2 = 2^{n/3} (measured 2^1.839, 2^3.956, 2^5.989, 2^7.997, 2^9.999, 2^12.000, 2^20.000 at n = 6...60 vs targets 2^{n/3}); per-slice alignment/||w||_{2,b} = sqrt(C(n,b)) = **2^28.357 at n=60, b=30** — reproducing the dossier's own sqrt(C(60,30)) ~ 2^28 exactly.
- *Adversarial margin* `log2 FM_b = n/6 - (-log2 rho_b)` on real model data (generic windows): **-7.0 (p=23,n=24), -15.0 (n=48), -32.3 (n=96); -26.6 (p=41,n=96); -24.0 (p=67,n=96)**. Wherever the slice coefficient meets the target it is **2^24-2^32 times smaller** than a weight perturbation invisible to every proper marginal.

**=> F2 verdict: NOT TRIGGERED as stated** (the bias is visible in the slice statistic, at exactly the 2^-{n/6} scale, and the extremal modulation is uniquely the one slicing sees best) — **but the salvage architecture inherits the full precision requirement**: no theorem controlling the weights to relative accuracy coarser than the target itself can prove the slice bound. The black hole is a precision problem, not a blindness problem.

## 5. Cancellation table vs the 1/3 target

`eta = -log2(rho_b)/n`, bits of cancellation per coordinate; least-squares slopes fitted on n >= 32 (exact integer statistic):

| p | c | window | slice slope | slice intercept | full slope |
|---|---|---|---|---|---|
| 23 | (1,1) | mixed | 0.3444 | -0.61 | 0.4815 |
| 23 | (2,3) | mixed | 0.3038 | -1.06 | 0.4479 |
| 41 | (1,1) | mixed | 0.3176 | -2.17 | 0.4578 |
| 41 | (2,3) | mixed | 0.3620 | +2.06 | 0.5392 |
| 67 | (1,1) | mixed | 0.2765 | +1.19 | 0.3498 |
| 67 | (2,3) | mixed | 0.2620 | +0.78 | 0.3470 |
| 101 | (1,1) | mixed | 0.3226 | -5.32 | 0.4612 |
| 101 | (2,3) | mixed | 0.3399 | -4.91 | 0.4782 |
| 23-101 | both | **odd-Delta** | **0.003-0.024** | **~ log2 p** | 0.312-0.445 |

Central-slice values across p = 7...101, c = 4 frequencies, n = 16...64 (`slice_cancellation_counts.json`, 180 rows): generic windows give `eta_n in [0.33, 0.67]`, `eta_S = -log2 rho / log2 C(n,b) in [0.36, 0.78]` against the square-root barrier 0.5 — the mechanism is square-root cancellation in the slice, degraded by an `O(log p)` startup deficit.

**=> F3 verdict: TRIGGERED, conditionally and precisely.**
- Generic (mixed-parity) windows: slice slope **0.26-0.36**, straddling 1/3 (4 of 8 fits above, 4 below), with a negative intercept of up to 5 bits. The 1/3 budget is **marginal, not cleared uniformly**; the weaker 1/43 = 0.0233 calibration is cleared with ~13x margin.
- The slice exponent is systematically **~0.69x** the full-window exponent for the same coordinates — a constant-factor loss that must be paid by any b-resolved theorem.
- Odd-Delta windows: slice exponent **statistically zero**, floored at `log2 p`. Both targets fail once `n > 43.log2 p` (~1330 coordinates at official p ~ 2^31) and the 1/3 target fails at `n > 3.log2 p ~ 93`.

## 6. What this hands the lane

1. **The b-resolved reachability audit must be re-run on the difference subgroup** `<Delta_i - Delta_j>`, not the sumset. F2A.2's Sharp Law A is a full-window statement and does not transfer.
2. **The F2A.4 exceptional-owner list is `Ann(D)`, not `Ann(G)`** — strictly larger, and the sign of the k=p pair criterion is *inverted* relative to `resonance.py`.
3. **The correct slice dial is phase SPREAD, not phase location.** `e_b` acquires a global `e^{ib.theta}` under a common rotation, so any argument proving contraction by alignment against a fixed direction is worthless at fixed b (V9, exact witness).
4. **The theorem cannot be uniform over coordinate subsets.** Roughly half the coordinates at every frequency carry odd Delta; selecting them floors the slice at 1/p. The b-resolved slice-coefficient theorem must use the specific window, and needs a hypothesis excluding parity-homogeneous coordinate sets.

## 7. Files (all under `notes/pilots_20260802/f2_slice_coefficients/`)

`slicecore.py` (exact `Z[zeta_p]`, model, sigma/Delta, slice DPs, Krawtchouk) . `verify_slice.py` (V1-V11, ALL PASS) . `mode_and_coset.py` (stages `verify|census|fence|weighted`) . `cancellation.py` (stages `count|scale|weight`) . `structure.py` . `fences.py`
`results/`: `slice_cancellation_counts.json` (180 rows) . `slice_scaling.json` . `slice_cancellation_weighted.json` . `slice_coset_fence.json` . `slice_fence_weighted.json` . `delta_parity_census.json` . `slice_structure.json` . `fence_modulation.json` . `fence_adversarial.json` . `fence_reversal.json`
All runs under `tools/ramguard local`. Nothing written outside the directory (`sys.dont_write_bytecode` set before importing f2model; `git status` shows only the new untracked dir). No commit, no push, no DAG/critical/background/tools change, nothing m2-related touched.

## 8. Honest caveats

- **Scale.** The slopes come from the **balanced-weight integer proxy** (carry and cosine *signs* exact via sigma; only the magnitude variation `|2cos|` set to 1). The true-weight exact cyclotomic computation reaches only n <= 12, where the `O(log 2p)` transient dominates and the numbers are noisy (1-8 bits, no slope extractable). The **structural** results — coset confinement, `hhat_p(p)=2`, `|e_b(p)| = E_b`, the death dichotomy — are exact **with true weights** and weight-independent; only the claim that the remaining modes contract enough for the 1/p floor to be *attained* rests on the proxy.
- **Primes.** p <= 101 for scaling, p <= 23 for true weights; official p ~ 2^31 is a four-decade extrapolation on laws that are exactly constant over the measured range (the `log2 p` floor matches to 3-4 decimal places at every p tested).
- Single descent j=1, q = p^2 only; tower functoriality untested (inherited gap from F2A.2).
- The F2A.1 orientation-cube seam and PP5.0 remain unproven upstream; nothing here is mintable.
- The 1/3 vs 1/43 normalisation is taken from `verify_brief5_f2_myerson_program_arithmetic.py` (`tower_budget_checks`, `weak_margin_block_target`); both are reported since PP5.0 has not frozen the composition law.
- `eta_n <= H(b/n)` unconditionally by integrality, so slices with `b/n` outside ~[0.174, 0.826] can never reach 1/3 and `b in {0, n}` have `rho = 1` exactly — a structural reason the slice target must be normalised by `log2 C(n,b)`, not by n.
