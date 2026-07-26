# WCL `(4,11)` quintic-divisor descent

- **status:** PROVED
- **closure:** proof
- **consumer:** `dli_wcl_slot_4_11_emptiness`
- **dependencies:** `dli_wcl_ell4_weight9_quartic_divisor_descent` (the `w=9`
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

## Scope — what is and is NOT proved here

**Proved:** the normalisation `(QQD3)`, the normal form `(QQD5)` with `e_9` free,
the square locator `(QQD6)`, the divisibility `(QQD7)`, and the reconstruction
identity `(QQD8)` (verified: for random `(B, e_9)` over `F_10007`, every root `y` of
`G` yields `rho` with `rho^2 = y` and `F(rho) = 0`).

**NOT proved here, and owed before the cell can be attacked as a census:** the
*converse* bijection. `(4,9)` additionally establishes that every monic `A`
satisfying its divisibility reconstructs nine **distinct, non-antipodal** roots with
product one and vanishing odd power sums. The corresponding statement for `(QQD8)`
— distinctness, non-antipodality, and that `(QQD2)` is recovered — is not
established here, nor is the `Delta` certificate `(QQD11)` analogue (no
characteristic-zero point of the ideal `I = (R_0,...,R_10)`).

Closes no cell. `dli_wcl_slot_4_11_emptiness` stays TARGET.
