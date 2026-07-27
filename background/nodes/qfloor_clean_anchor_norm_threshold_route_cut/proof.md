# Proof

At a candidate predecessor `m=a_safe-1`, the canonical quotient radius has

```text
m = k + n/N'.
```

Thus `N'=n/(m-k)`. Substitution in the six candidate rows gives `N'=256`
at rates `1/4` and `1/8`, and `N'=512` at rate `1/16`, independently of
whether `n=1024` or `n=2^41`. The qfloor parameter is
`ell'=rho N'+1`, giving `65,33,33` respectively.

Exact integer exponentiation gives

```text
130^128 : 899 bits,
 66^128 : 774 bits,
 66^256 : 1548 bits.
```

In particular each integer is greater than `2^256`. If the ambient field has
order `q=p^e<2^256`, then its characteristic satisfies `p<=q<2^256` and
cannot exceed any displayed threshold. Hence the load-bearing norm premise of
`qfloor_exact` fails on all six rows, even before its prime-field and
degree-one-reduction requirements are considered.

The exact binomial comparisons in the verifier confirm why these rows look
like quotient witnesses: every `binom(N',ell')` is above its budget. But the
qfloor proof obtains distinct slopes only by reducing a nonzero cyclotomic
norm modulo `p`; when the size hypothesis fails, the raw locator classes may
collide. The binomial comparison alone therefore cannot supply a `Q` payload.
