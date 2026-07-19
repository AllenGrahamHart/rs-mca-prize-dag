# Uniform shifted-product fiber bound

- **status:** `PROVED`
- **consumers:** `f3_h3_mobius_excess_half` (marginal evidence only) and
  `f3_h3_double_accident_derivative_ideal` (separator-exponent optimization)

Let

```text
n=2^s,                  13<=s<=41,
p=1 (mod n),            p>=n^2,
H<=F_p^*,               |H|=n,
A=(1-H)\{0}.
```

For `tau in F_p^*\{1}`, put

```text
P(tau)=#{(a,b) in A^2:ab=tau}.
```

Then

```text
P(tau)<33 n^(2/3).                                      (PF33)
```

Equivalently, `(PF33)` bounds the number of `(x,y) in H^2` satisfying
`(1-x)(1-y)=tau`. The proof makes every constant and every low-order floor
choice explicit in the auxiliary-polynomial argument of
Konyagin--Shparlinski--Vyugin, arXiv:2005.05315.

This is a genuine uniform theorem on the official prime-field corridor, but
it is marginal. It does not control the correlation of `P(tau)` with the
quotient multiplicity `R(tau)` and therefore does not prove the C36'
weighted cutoff-18 target.

It may nevertheless be consumed to replace the trivial cutoff-excess cap
`n-19` by `ceil(33n^(2/3))-19` inside a separately proved construction. That
use does not turn the marginal theorem into a C36' discharge.
