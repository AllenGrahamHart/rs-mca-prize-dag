# D5 — weakest-form re-pose DRAFT for `l1_mixed_petal_amplification`

Draft only. Not applied to the node. Round 21, 2026-08-07.
Every number below is reproduced by the four scripts in this directory.

## 0. Why a re-pose is needed

The statement of record (`critical/nodes/l1_mixed_petal_amplification/
statement.md:8-12`) quantifies over `sigma` and over received words `U`
but leaves the **petal size `ell` implicit**. The diagnosis shows `ell`
is the only parameter that controls the size of the object, via the
exact identity (verified at every tested cell, `d2_danger_map.py`,
`d3_ell_sweep.py`):

```text
maximal-source chart: |C| = k-1, t petals of size ell, |B| = b < ell,
                      t*ell + b = n-k+1        (rate 1/2: = k+1)
floor band:           d = |C \ S| >= ell(t-2)
agreement:            |S| >= k+sigma

  =>  #core points kept  a   <= A_max  = 2*ell + b - 2
      #petal points lost om  <= om_max = 2*ell + b - 1 - sigma
  =>  the bucket is EMPTY when sigma > 2*ell + b - 2 =: Lambda
      and otherwise  BOX = Theta( C(k-1, Lambda) * C(t*ell, Lambda) )
                         = Theta( n^{2*Lambda} ) = Theta( n^{4*ell+2b-4} ).
```

At `ell = 2, b = 1` (the ONLY cell the N10 census ever ran) this is
`Lambda = 3` and `BOX = Theta(n^6)` — so the registered super-polynomial
falsifier cannot fire there, for any received word, as a matter of
counting. The open content lives at `ell -> infinity`.

## 1. Proposed re-pose (weakest sufficient form)

> **(L1-MPA-w)** Let a row `(n, k, q)` and a received word `U` satisfy the
> corrected reserve `sigma log2 q_D >= (1+eps) log2 C(n, k+sigma)`, and let
> the quotient profile be budgeted. In every maximal-source chart of `U`
> with petal size `ell` and background `b < ell`, the mixed-petal /
> diffuse partial-petal contribution to `#ImgFib_U(k+sigma)` is at most
> `n^B` with `B` independent of `ell`.
>
> **Clause (a) — DISCHARGED BY COUNTING (this pilot, unconditional, every
> received word).** If `sigma > 2*ell + b - 2` the contribution is `0`.
> Otherwise it is at most `BOX(ell, b, sigma) <= C(k-1, Lambda) *
> 2^b * C(t*ell, Lambda)` with `Lambda = 2*ell + b - 2`; in particular at
> `ell = 2, b = 1` it is at most `(1+o(1)) n^6/2304`, which is `0.31`
> full-petal columns against an allowance of `floor(n^6/C(n+6,6)) = 720`
> (`critical/nodes/petal_growth/conditional.md:16`). No census is needed
> for this clause and no word family can violate it.
>
> **Clause (b) — THE ACTUAL TARGET.** For charts with `ell` growing with
> `n` — equivalently, by the listing inequality `|C| + ell = k-1+ell >=
> k+sigma`, for `ell >= sigma+1`, which at the official rows means
> `ell = Omega(n/log n)` — the contribution is `n^B` with `B` absolute.
> Here `BOX = n^{Theta(n/log n)}`, so the bound is NOT a counting fact and
> the whole content of the node sits in this clause.

## 2. Pre-registered falsifier for the re-pose

Two falsifiers, both reachable:

- **(F-w1) The ell-law falsifier.** The measured law on the banked object
  is `retained ~ sum_m N_{k+m}(ell) q^{-m}` (matched to 0.4-2% at n=32,64
  and to 44x across `ell = 2,3,4` at fixed `n = 24`). FALSIFIED IF an
  `ell`-sweep at a fixed row returns a retained count exceeding
  `10 * BOX(ell)/q`, i.e. a word whose mixed floor-band mass is an order
  of magnitude above its own box-over-field prediction. That is the
  signature of a genuine amplification mechanism and it is what a
  super-polynomial family must look like at small scale.
- **(F-w2) The clause-(a) falsifier.** A mixed-petal floor-band
  contributor at `sigma > 2*ell + b - 2` in any maximal-source chart.
  Clause (a) is a counting identity; a single such contributor kills it
  and re-opens `ell = 2`.

## 3. The decisive compute request (replaces `L1-N10-128`)

`L1-N10-128` (raise `n` to 128 at `ell = 2`, ~74 CPU-hours, ~$4.1;
`experiments/prize_resolution/l1_balanced_mixed_growth_census_result.md:78-86`)
buys a fourth point on a curve whose closed form is already known exactly
and which is provably capped at `n^6`. It should be **dropped**.

Proposed replacement, `L1-N10-ELL`: hold `n` fixed at 32 or 64 and sweep
`ell = 2,3,4,5,6` on both scalar schedules, measuring retained against
`BOX(ell)/q`. Cost at `n = 32` is comparable to the banked `n = 64`
run (`BOX(32, ell=3) = 1.4e8` vs the banked `2.7e7`); the `ell = 2,3,4`
row at `n = 24` is already done locally, in-session, at zero Modal cost
(`d3_ell_sweep.py`). This is the sweep that can actually fire the
falsifier, because it moves the parameter the object depends on.
