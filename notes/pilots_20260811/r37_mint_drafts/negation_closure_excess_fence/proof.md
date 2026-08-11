# Proof

## 1. The row collapse

Let `D = {+-1, ..., +-m}`, `n = 2m`, and `v_x = 1/prod_{y != x}(x-y)`.
Replacing `x` by `-x` permutes `D`, so

```text
v_{-x} = (-1)^{n-1} v_x.
```

Moreover `sum_{x in D} v_x g(x) = 0` whenever `deg g <= n-2` (the standard
Lagrange/residue identity: the sum is the coefficient extraction of a proper
rational function). Take `e_0 = 1` on `T` and `e_1 = x^2` on `T`, and let the
locator be **even**, `sigma(x) = Q(x^2)`, with root set `S = A u (-A)`.

For a Hankel row of index `i`, the functional applied to `sigma` is
`sum_{x} e(x) v_x x^i sigma(x)`. Since `sigma` and `e_1/e_0 = x^2` are both
even, the summand is `v_x x^i (even in x)`. Pairing `x` with `-x` therefore
makes the contributions of a full orbit cancel when `i` is **odd**, and the
only surviving terms come from orbits that the support `T` meets one-sidedly.
`T = {1,...,r+1}` meets orbits `1..r+1` one-sidedly and misses the remaining
`off = m - (r+1)` orbits entirely. If the locator's root set `S` **covers**
those missed orbits, `sigma` kills exactly the surviving terms, and the odd
rows vanish identically.

The verifier checks this directly rather than by re-deriving it: on all
`1158` covering even locators it scans, every odd-index entry of both `U` and
`W` is zero.

## 2. The residual count and the two regimes

What remains after the collapse are the rows of index `0 mod 2`, i.e.
`ceil(rho/2)` of them, and they constrain the single unknown `gamma` through
`U_i + gamma W_i = 0`. Therefore:

- `rho = 2`: one condition, one unknown — solvable for every covering even
  locator, so **each covering locator produces a bad slope**. The verifier
  confirms set equality (bad set = covering set) at H1 and H3, both fields.
- `rho >= 3`: at least two conditions on one unknown — generically
  inconsistent. The verifier confirms `0` bad locators at H4 despite `165`
  covering ones, and the same at H6/H7/H8 in the source bank.

The dichotomy is entirely a function of `ceil(rho/2)`; `q` does not appear.

## 3. The covering count

`A` must be an `r/2`-subset of the `m` orbits containing all `off` missed
orbits, so the free choice is `r/2 - off` orbits out of the remaining
`m - off`:

```text
#covering = C(m - off, r/2 - off),        off = m - (r+1).
```

At `off = 1` this is `C(m-1, r/2-1)`, the banked form — which is therefore a
special case, not the law. The verifier evaluates (CNT) against all six
banked cells and additionally asserts that `C(m-1, r/2-1)` does NOT match
when `off != 1`, so the scope restriction is itself under test.

## 4. The razor kill

`ceil(rho/M) <= 1` iff `M >= rho`. At razor `rho = 2^34`, so an invariant
carrier needs an automorphism of order at least `2^34`. Negation closure
gives `M = 2` and leaves `ceil(2^34/2) = 2^33` conditions on one unknown, an
over-determination of `2^33 - 1 = 8589934591`. Nothing in this count depends
on `q`.

## 5. Scope: why this is a fence and not a counterexample

The exhibits sit at `r > R/2`, outside the shape where
`B_ca^far(n-r) <= r+1` is proved. So they do not contradict that node; they
show it is false as a *universal*. The razor row at the crossing offset also
has `r > R/2` (`63*2^34` against `2^39`), which is why the cap there has to
come from the fibre pigeonhole rather than from the proved bound. The same
inequality `2r > R` is what makes the type-2 spend/list ledger vacuous by
sign on the whole open bracket.

The symmetric-T variant at `rho >= 3` is **unmeasured**; parity predicts
survival at `rho = 3` and death at `rho >= 4`. That gap is not closed here.
