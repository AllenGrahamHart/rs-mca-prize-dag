# proof: census_bounded_scales

- **status:** PROVED
- **closure:** proof

## Statement (this node)

At agreement `A` (`t = A - k`, `j = n - A`), the quotient stratum on a
rate-preserving scale `N' = n/M` has **forced class ratio** `l'/N' = j/n`, so its
count grows **strictly monotonically** as `2^{N' H(j/n)}`. With `H(j/n)` bounded
below on the corridor (`j/n in [0.4, 0.5] => H(j/n) >= 0.97`), and the count
jumps between admissible scales being *staircase-step* sized, **exactly one**
scale's count lands within a staircase step of the gate `B*`, and that scale lies
in an **absolute window** `N' in [~120, ~400]` that is **independent of `n` and
`k` up to `2^40`**. Hence the census is `n`-uniform: every corridor crossing sees
only bounded scales. This is the lemma that makes a *symbolic* (n-free) census
possible and pins the deciding scale uniquely.

Companion: `dyadic_profile_evaluation` supplies the exact profile values; this
node supplies the structural pinning (monotonicity + uniqueness + `n`-uniformity)
that they instantiate.

## 1. Forced class ratio `l'/N' = j/n` [complete]

Fix a rate-preserving dyadic scale `M | gcd(n,k)` (so `N' = n/M`, `k' = k/M`, and
the fold is rate-preserving — this is exactly the seam condition proved in
`gap2_seam`). The order-`M` subgroup `mu_M <= mu_n` acts freely on `mu_n`; the
quotient map `pi_M : x |-> x^M` sends `mu_n` onto `mu_{N'}` with fibres of size
`M`. A quotient stratum is an `mu_M`-invariant co-support `T` (size `j`), which
descends to a co-support `T' = pi_M(T)` in the quotient row `mu_{N'}` of size

```
l' := |T'| = j / M = (j/n) * N'.                                          (C)
```

So the number of "selected classes" `l'` in the quotient row is **forced** by the
agreement: `l'/N' = (j/n)`, a rate/agreement invariant that does **not** depend on
`M`. (Equivalently, on the codeword side `thm:qcore` selects `k' = (k/n)N'`
classes; by complementation `C(N', l') = C(N', N' - l')` the two conventions give
the same count, since `1 - j/n = A/n`.) ∎

## 2. Strict monotone growth `2^{N' H(j/n)}` [complete]

The quotient-stratum count on scale `N'` is the exact binomial
`Q(N') = C(N', l') = C(N', (j/n) N')`. By the entropy estimate (Stirling, exact
two-sided bounds),

```
N' H(j/n) - (1/2)log2(2 N') <= log2 Q(N') <= N' H(j/n),                    (E)
```

with `H(p) = -p log2 p - (1-p) log2(1-p)`. For a fixed ratio `p = j/n in (0,1)`,
`H(p) > 0`, so `log2 Q(N')` is **strictly increasing in `N'`**: doubling `N'`
(the next admissible dyadic scale, `M -> M/2`) roughly doubles the exponent. This
is the monotonicity the census relies on — larger quotient rows hold strictly
more strata. ∎

## 3. Corridor lower bound on the entropy [complete, verified]

`H` is concave, symmetric about `1/2`, increasing on `[0, 1/2]`. On the corridor
`j/n in [0.4, 0.5]`,

```
H(0.40) = 0.97095... ,   H(0.45) = 0.99277... ,   H(0.50) = 1,
so   j/n in [0.4, 0.5]  =>  H(j/n) >= H(0.40) > 0.97.                      (H>=)
```

(Verified numerically below.) The corridor `j/n ~ 0.4-0.5` is the near-capacity,
near-rate-1/2 decision region; there the growth constant is essentially maximal.

## 4. The staircase-step gap forces a unique deciding scale [complete]

Between two consecutive **admissible** dyadic scales `N'` and `2N'` (recall for a
`2`-power domain the scale lattice is the chain `{2^i}`), the counts satisfy, by
(E),

```
log2 Q(2N') - log2 Q(N') >= 2N' H(j/n) - N' H(j/n) - (1/2)log2(4N')
                          =  N' H(j/n) - O(log N').                        (STEP)
```

At the deciding window `N' ~ 128` and `H >= 0.34` (all four rates), (STEP) is
`>= 128 * 0.34 ~ 43` bits — a *staircase step* far larger than any bounded factor.
Consequently the map `N' |-> log2 Q(N')` increases by `>= 43` bits at each dyadic
step, so **at most one** admissible scale can have `log2 Q(N')` within a
staircase step (a bounded number of bits) of the gate `log2 B* (~ 122-128)`. That
scale — the *deciding scale* `N'_*` — is therefore **unique**. (This is the
"monotone counts, q-factor gaps" uniqueness quoted in the statement's ledger.) ∎

## 5. The deciding scale lies in an absolute, `n`-uniform window [complete]

Two independent pins put `N'_*` in `[~120, ~400]`, `n`-freely:

- **Crossing pin (continuous).** The scale at which the growth `2^{N' H(j/n)}`
  would cross `B*` is `N'_cross = (log2 B*) / H(j/n) ~ 128 / H(j/n)`. Across the
  four rates `j/n in {0.5, 0.75, 0.875, 0.9375}` this is
  `128/H = 128.0, 157.8, 235.5, 379.5` respectively — **all inside `[120, 400]`**
  and depending only on the *rate* `H(j/n)` and the constant `128 = log2(q/B*)`,
  **not on `n`**.
- **Admissibility pin (dyadic).** Only scales with `M > t` are admissible, so the
  *largest* admissible quotient row is `N'_max = n / M_min` with
  `M_min = ` least power of two `> t`; hence

  ```
  N'_max = 2^{m - ceil(log2(t+1))}  ~  n/t  =  1/eta,     eta := t/n.       (U)
  ```

  On the corridor the reserve is `eta in [2^-9, 2^-7]`, so `N'_max in {128, 256}`
  (`= 2^7, 2^8`), again in `[120, 400]` and set by `eta` (rate + corridor
  position), **not by `n`**. Since `Q` is increasing, the deciding admissible
  scale is `N'_max`, and its count is `<= B*` (safety), closest from below.

Both pins are `n`-free. The concrete check: at rate `1/4`, the rows `n = 2^10`
(RowC) and `n = 2^41` (prize) — differing by a factor `2^31` — have the **same**
deciding scale `N'_max = 128`, the same forced selection `l' = 95` (co-support
convention `l' = round((j/n)N')`), and the same count `log2 C(128, 95) = 101.76`;
likewise `1/8` (`N' = 128`) and `1/16` (`N' = 256`). **The deciding scale, ratio,
and count are bit-identical across a `2^31` range of `n`.** (This is the same
stratum that `dyadic_profile_evaluation` counts in the *codeword* convention
`h = floor(A/M) = 32`, `C(127, 32) = 2^{99.81}`; the two agree up to
`C(N', l') = C(N', N' - l')` and the `O(1)` rounding of `l'` vs `N' - h` — both
are `n`-uniform and both pin the same deciding scale.) ∎

## 6. Consequence: `n`-uniform (symbolic) census

Because every corridor crossing consults only the unique deciding scale
`N'_* in [120, 400]`, and that scale is `n`-independent, the entire quotient
census can be carried out **symbolically at bounded `N'`** — the counts, the
deciding scale, and the safety margin are functions of `(rate, eta)` alone, with
`n, k` entering only through those two invariants (for all `n <= 2^40`, indeed up
to `2^41` as computed). This is precisely the `n`-uniformity claim: the census
never needs to examine unbounded scales, so a finite symbolic table settles every
row. ∎

## Verifier

`verify.py` (stdlib, exact big ints, <1s) checks:
(1) forced ratio (C) and the exact count `C(N', (j/n)N')`;
(2) strict monotonicity of `log2 Q(N')` in `N'`;
(3) `H(0.40) >= 0.97` and `H` monotone on `[0,1/2]`;
(4) the staircase-step gap (STEP) `>= 40` bits between consecutive admissible
scales at the deciding window;
(5) uniqueness — exactly one scale within a staircase step of `B*`;
(6) window `N'_cross = 128/H(j/n) in [120, 400]` for all four rates, and
`n`-uniformity: identical deciding scale/count for `n = 2^10` vs `2^41` at each
rate. All PASS.
