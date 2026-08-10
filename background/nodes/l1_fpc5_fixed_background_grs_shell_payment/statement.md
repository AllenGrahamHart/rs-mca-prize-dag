# Fixed-background FPC5 GRS shell payment

- **status:** PROVED
- **consumer:** `l1_fpc5_large_source_payment`

Fix one FPC5 source, touched-petal set, and defect degree with

```text
u=d-(t-1)ell,       0<=u<=b.
```

For every `u`-set `R` of background points, let `F_R` be the contributors
whose numerator vanishes on `R`. Put

```text
D=d+ell-1,
J_fix=d^2-N(d-ell).                                  (FP1)
```

Then the complete contributor family `F` satisfies

```text
|F| <= binom(b,u)                                    (FP2)
```

when `D>=N`, and

```text
|F| <= binom(b,u) N ell/J_fix                        (FP3)
```

when `D<N` and `J_fix>0`.

Consequently, for every fixed absolute `C`, either branch is polynomial
whenever

```text
min(u,b-u)<=C.                                        (FP4)
```

More explicitly, `(FP2)` is at most `n^C`, and `(FP3)` is at most
`n^(C+2)`.

The fixed and joint-background Johnson denominators obey

```text
J_bg=b J_fix-Nu(b-u).                                 (FP5)
```

Thus this payment is not a restatement of the existing `J_bg>0` branch. It
can apply with `J_bg<=0`, but exactly exposes the binomial background-choice
cost that the joint theorem absorbs.

## Scope

This is one fixed source/touched/degree-cell payment. It does not pay the
middle-polarity regime where both `u` and `b-u` grow, the noninjective
`J_fix<=0` GRS shells, source-layout aggregation, or chronology. Raw use of
`(FP3)` without its binomial factor is invalid.
