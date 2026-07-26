# Router doubling-test soundness for all k — the (2,7) k=5 obligation, discharged
# (2026-07-26)

The sizing ledger says the `(2,7)` census is live *"after the GMP-gcd swap +
**router-soundness for k=5**"*. This note discharges the router-soundness half, in
general `k`, so it covers `k=5` and every future slot rather than one cell.

Artifact: `../verify_router_doubling_soundness.py` (stdlib, exact, no floats;
15,016 polynomials certified; 4 mutation controls, all caught).

## The test in use

Every `(2,w)` router normalizes a selected sub-tuple and leaves a monic degree-`k`
factor `f` determined by the shape variables, whose roots must be tested for
membership in `mu_M`, `M = 2^t` (`t = 10` at `M = 1024`). The test in production is
the power-of-two doubling recurrence — *"ten recurrence doublings per candidate"* —
i.e. compute `X^M mod f` by `t` modular squarings and ask whether the result is `1`.

## Lemma (μ_M-membership router soundness)

Let `F` be a field with `char F = 0` or `char F > k`, let `M = 2^t` with
`char F != 2`, and let `f in F[X]` be monic of degree `k` with `f(0) != 0`. Then

**(i)** `X^M == 1 (mod f)` ⟺ `f | X^M - 1` ⟺ **`f` is squarefree and every root of
`f` lies in `mu_M`**.

**(ii)** Hence the doubling test has **no false positives**: if it passes, every
root of `f` is in `mu_M`.

**(iii)** It *does* have **false negatives**, exactly on the non-squarefree `f`
whose roots all lie in `mu_M`.

**(iv)** The correct test on an arbitrary `f` is `X^M == 1 (mod rad f)`, where
`rad f = f / gcd(f, f')`.

### Proof

`X^M - 1` is **separable** over `F`: its derivative is `M X^{M-1}`, and `M = 2^t`
is invertible since `char F != 2`, while `X` does not divide `X^M - 1`; so
`gcd(X^M - 1, M X^{M-1}) = 1`.

*(i)* `X^M == 1 (mod f)` ⟺ `f | X^M - 1` is the definition. If `f | X^M - 1`, then
`f` inherits squarefreeness from the separable `X^M - 1`, and each root of `f` is a
root of `X^M - 1`, i.e. lies in `mu_M`. Conversely if `f` is squarefree with all
roots in `mu_M`, then `f = prod (X - r_i)` with the `r_i` distinct elements of
`mu_M`, and `X^M - 1 = prod_{z in mu_M} (X - z)` has each `X - r_i` as a distinct
factor, so `f | X^M - 1`.

*(ii)* Immediate from (i).

*(iii)* If `f` is not squarefree it cannot divide the separable `X^M - 1`, so the
test fails — **even when every root lies in `mu_M`**. The condition `char F > k`
makes `gcd(f, f')` compute the radical correctly (no inseparability from a
`p`-th-power factor at degree `k`).

*(iv)* `rad f` is squarefree with the same roots as `f`, so (i) applies to it. ∎

## Why this is the soundness obligation, not a technicality

The slots are **zero-event obligations**: the census must *exclude every
candidate*. A false **positive** would be harmless here (it only keeps a candidate
alive for the norm stage). A false **negative** silently discards a candidate — and
a discarded candidate is exactly an un-excluded one. So:

> Applying the bare doubling test to a possibly-non-squarefree `f` makes the
> resulting emptiness claim **unsound**.

The remedy is either (a) test `rad f`, or (b) enumerate the non-squarefree stratum
separately. **The closed `(2,6)` certificate did (b)**: its `510` structural
double-zero cases — the antipodal-mirror family `c = 512+a+b` — are precisely this
stratum, handled by the power-of-two vanishing-sum lemma instead of by the
recurrence. That was not incidental bookkeeping; it was this obligation being paid.

Any `(2,7)` router at `k = 5` owes the same payment, and now has a general
statement to cite rather than re-deriving it per weight.

## Certification

`verify_router_doubling_soundness.py` certifies (i)–(iv) over
`(p, M) in {(17, 8), (17, 16), (97, 32)}` for `k = 2,3,4,5`, on 15,016 monic
polynomials — a deterministic spread sample plus a **forced non-squarefree
stratum** `(X - g^a)^2 * (in-mu_M rest)`, since a random sample would rarely hit
the very case the lemma is about. Results:

- **0 false positives** across all 15,016;
- every false negative observed is non-squarefree, as (iii) requires;
- the radical test (iv) agrees with true membership on every polynomial;
- the doubling count is exactly `t`.

Explicit false-negative witness: `f = X^2 + 2X + 1 = (X+1)^2` over `F_17`, `M = 8`.
Its only root `-1` has order `2 | 8`, so it *is* in `mu_8` — yet
`X^8 = 1 + 9(X+1) != 1 (mod f)`. The bare test discards it.

## Non-claims

- Closes no slot. `(2,7)` remains TARGET: this discharges the router-soundness
  half of its precondition; the GMP-gcd swap and the 33k CPU-h census remain.
- Says nothing about which candidates the `(2,7)` router enumerates, nor about its
  completeness as a reduction — only about the correctness of the membership test
  applied to whatever it produces.
- The `char F > k` hypothesis is harmless at official scale (`k <= 11`, `char` a
  prime `> 2^167`) but is stated because the lemma is false without it.
