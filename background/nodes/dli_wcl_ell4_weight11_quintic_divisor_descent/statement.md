# WCL `(4,11)` quintic-divisor descent

- **status:** PROVED
- **closure:** proof
- **consumer:** `dli_wcl_slot_4_11_emptiness`
- **dependencies:** `dli_wcl_extended_six_slot_sparse_divisor_endpoints`,
  `dli_wcl_ell4_weight9_quartic_divisor_descent` (the `w=9` specialized
  template), `dli_wcl_newton_short_window_exclusion`

Let `K` have characteristic zero or characteristic greater than `11`, containing
`omega` of exact order `2048`. For a reduced signed weight-eleven relation put

```text
rho_i = s_i omega^(e_i),   0 <= e_i < 1024,   s_i in {+1,-1},
p_j   = sum_i rho_i^j.                                       (QQD1)
```

Assume the `ell = 4` window conditions

```text
p_1 = p_3 = p_5 = p_7 = 0.                                   (QQD2)
```

## Normalisation (the parity dichotomy applies, and `w = 11` is on the good side)

`gcd(11, 2048) = 1` with `11^(-1) = 931 mod 2048`, so with `a_11 = prod_i rho_i`
there is a **unique** common dilation

```text
lambda = a_11^(-931) in mu_2048                              (QQD3)
```

for which the normalised roots `lambda rho_i` have product one. Dilation preserves
reducedness and `(QQD2)`. (Contrast `(4,10)`: `11` is odd but `10` is not, and by
`verify_descent_parity_dichotomy.py` no global dilation exists there.)

## Normal form — a monic QUINTIC plus one free parameter

By Newton's identities, `(QQD2)` gives `p_k = k e_k` for `k = 1,3,5,7` once the
lower odd ones vanish, hence

```text
e_1 = e_3 = e_5 = e_7 = 0,     e_11 = 1 (product one).       (QQD4)
```

**This is where `(4,11)` departs from `(4,9)`.** The odd indices at most `9` are
exactly `{1,3,5,7,9}`, so at `w = 9` every odd elementary symmetric function is
pinned and the locator collapses to `X A(X^2) - 1`. At `w = 11` the odd indices are
`{1,3,5,7,9,11}`: `(QQD4)` pins five of them but leaves **`e_9` free**. Therefore

```text
F(X) = product_i (X - lambda rho_i) = X B(X^2) - (e_9 X^2 + 1),   (QQD5)
B(Y) = Y^5 + b_4 Y^4 + b_3 Y^3 + b_2 Y^2 + b_1 Y + b_0  monic quintic.
```

So the descent carries **six** parameters `(b_0,...,b_4, e_9)`, against four for
`(4,9)`.

## Square locator and divisibility

At a root `rho` of `F`, writing `y = rho^2`, `(QQD5)` gives
`rho B(y) = e_9 y + 1`, and squaring:

```text
G(Y) = Y B(Y)^2 - (e_9 Y + 1)^2 = product_i (Y - (lambda rho_i)^2),   (QQD6)
```

monic of degree `11`. Each `rho_i^2 = omega^(2 e_i)` lies in `mu_1024`, and
`lambda^2 in mu_1024`, so every root of `G` is a `1024`-th root of unity; the
relation being reduced makes the `rho_i` pairwise non-antipodal, so the squares are
distinct. Hence

```text
G(Y) divides Y^1024 - 1.                                     (QQD7)
```

The reconstruction map, when `B(y) != 0`, is

```text
rho = (e_9 y + 1) / B(y),        rho^2 = y,   F(rho) = 0.    (QQD8)
```

## Elimination endpoint

Dividing `Y^1024 - 1` by the monic degree-eleven `G` gives

```text
(Y^1024 - 1) mod G = sum_(j=0)^(10) R_j(b_0,...,b_4,e_9) Y^j, (QQD9)
```

with `R_j in Z[b_0,...,b_4,e_9]`: **eleven relations in six unknowns**, against nine
in four at `(4,9)`. This is the fixed characteristic-only endpoint for the cell.

## Converse — the bijection is COMPLETE (2026-07-26)

Let `B` be monic quintic, `e_9` a scalar with

```text
gcd(B(Y), e_9 Y + 1) = 1        (vacuous when e_9 = 0)          (QQD10)
```

and suppose `G(Y) = Y B(Y)^2 - (e_9 Y + 1)^2` divides `Y^1024 - 1`. Then `(B, e_9)`
reconstructs a normalised reduced weight-eleven relation satisfying `(QQD2)`:

1. **`G` is squarefree with 11 distinct roots** — it divides `Y^1024 - 1`, which is
   separable since `char` is odd.
2. **`B(y) != 0` at every root `y` of `G`.** If `B(y) = 0` then `G(y) = 0` forces
   `(e_9 y + 1)^2 = 0`, hence `e_9 y + 1 = 0`, contradicting `(QQD10)`.
3. **`rho(y) = (e_9 y + 1)/B(y)` satisfies `rho^2 = y` and `F(rho) = 0`** — the
   first directly from `G(y) = 0`, the second by substitution.
4. **The eleven `rho(y)` are distinct and are exactly the roots of `F`.**
   `rho(y_i) = rho(y_j)` implies `y_i = rho(y_i)^2 = rho(y_j)^2 = y_j`; and `F` is
   monic of degree 11 with these 11 distinct roots.
5. **Non-antipodal.** `rho_i = -rho_j` implies `y_i = y_j`, so `i = j` and
   `rho_i = 0` — impossible, since `F(0) = -1`.
6. **Product one.** `prod_i rho_i = (-1)^11 F(0) = -(-1) = 1`, because `F(0) = -1`
   identically. *(This is where the `-1` in the normal form earns its place.)*
7. **Window conditions recovered.** `F(X) = X B(X^2) - (e_9 X^2 + 1)` has no
   `X^10, X^8, X^6, X^4` term, so `e_1 = e_3 = e_5 = e_7 = 0`, and Newton (`char > 7`)
   gives `p_1 = p_3 = p_5 = p_7 = 0`.
8. **Signed form.** `rho^2 = y in mu_1024` gives `rho^2048 = 1`, so `rho in mu_2048`;
   since `omega^1024 = -1`, every such `rho` is `s omega^e` with `s in {+1,-1}` and
   `0 <= e < 1024`.

So **common-dilation orbits of `(4,11)` relations are in bijection with the pairs
`(B, e_9)` satisfying `(QQD10)` and the divisibility `(QQD7)`** — the exact analogue
of the `(4,9)` quartic bijection, with the side condition `(QQD10)` as the only new
ingredient (it is what keeps `0` out of the root set, and it is automatic at
`e_9 = 0`).

Machine-checked on 272 instances over `F_10007` from a fixed seed, including one
genuinely degenerate `(B, e_9)` where `B(-1/e_9) = 0`; the side condition tracked
the degeneracy exactly.

## What remains



**Proved:** normalisation `(QQD3)`; normal form `(QQD5)` with `e_9` free; square
locator `(QQD6)`; divisibility `(QQD7)`; reconstruction `(QQD8)`; and the **full
converse bijection** above under `(QQD10)`.

**Owed:** an explicit replayable `Delta` certificate and compatible-prime
exclusion. Characteristic-zero emptiness and existence of a nonzero integer
certificate are already proved by
`dli_wcl_extended_six_slot_sparse_divisor_endpoints`. The remaining task is to
extract and check such an identity, not to prove the ideal properness claim again.
The direct remainder shape is harder than `(4,9)`'s: **eleven** relations in
**six** unknowns, against nine in four.

Closes no cell. `dli_wcl_slot_4_11_emptiness` stays TARGET.

## The Delta route is NOT the cheap one — a reformulation, and a re-ordering (2026-07-26)

**First, a planning fact that changes the order of work.** The `(4,9)` node states
in terms: *"This theorem does not compute `Delta` or prove the slot empty."* So no
`Delta` exists for `(4,9)` either — and `(4,9)` is strictly the smaller problem
(**9 relations in 4 unknowns** against 11 in 6). **Any `Delta` attempt should be
made at `(4,9)` first;** if it is infeasible there it is certainly infeasible here.

**Why the direct expanded route is not selected.** `(Y^1024 - 1) mod G` with symbolic `G`
requires ten repeated squarings of a degree-10 polynomial whose coefficients live in
`Z[b_0..b_4, e_9]`. Coefficient degrees roughly double per squaring, so the `R_j`
carry degree on the order of `2^10` in six variables. The banked alternative is
the scheme-equivalent pruned straight-line lift: `142` variables, `147` equations,
and maximum total degree three. This does not make certificate extraction cheap,
but it avoids the claimed coefficient blow-up and is the correct computational
interface for any future certificate attempt.

**A cleaner equivalent form.** Write `P(Y) = prod_i (Y - y_i)` for the distinct
roots in `mu_1024`. Then the defining identities rearrange to

```text
(4,9)    P(Y) + 1              = Y * A(Y)^2      A monic quartic
(4,11)   P(Y) + (e_9 Y + 1)^2  = Y * B(Y)^2      B monic quintic
```

So each cell asks: **is there a squarefree product of 1024-th roots of unity which,
after adding `1` (resp. a squared linear form), becomes `Y` times a perfect
square?** Equivalently, `P + 1` must have `0` as a simple root and `deg A` double
roots. Setting `Y = 0` in the `(4,9)` form recovers `prod y_i = 1` immediately,
matching product-one.

This is a **polynomial Pell-type identity** `Y A(Y)^2 - P(Y) = 1`, with the extra
arithmetic constraint that `P` splits over `mu_1024`. It is a far better target than
the `R_j` elimination: no coefficient blow-up, and it exposes the double-root
structure that the eliminant hides.

**Route note (checked, negative).** Mason–Stothers does not bite here. With
`a = P`, `b = 1`, `c = Y A^2` (pairwise coprime, since `P(0) = -1` and a common root
of `P` and `A` would force `P = -1` there), `rad(abc) <= 9 + 1 + 4 = 14` against
`deg = 9`, so the abc bound reads `9 <= 13` — satisfied, no contradiction. The
squarefree parts are too large for abc to constrain, which is the same reason it
failed on the bridge pencil.

**Recommended next step for this lane:** attack `(4,9)` first because both its
four-parameter Pell form and its `114`-variable/`119`-equation cubic lift are
strictly smaller. A future certificate attempt must state which interface it uses;
failure of direct expanded remainders is not a fence against the sparse lift.
