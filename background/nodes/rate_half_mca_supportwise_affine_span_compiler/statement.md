# Support-wise affine-span MCA compiler

- **status:** PROVED
- **closure:** strengthened affine-span incidence theorem
- **scope:** every Reed-Solomon row and every affine explanation subspace,
  with exact same-support pair noncontainment

## Statement

Let `C=RS[F,D,K]` have length `n`, let
`r_gamma=r_0+gamma r_1`, and write `m=K+w` with `w>=1`. Let
`A=c_0+C'` be an affine subspace of the code with `dim C'=s>=1`.
Suppose that for every distinct slope `gamma in Z` there are

1. an explanation `c_gamma in A`, and
2. an exact size-`m` support `S_gamma` on which `r_gamma=c_gamma`,

such that the received pair is not simultaneously explained by two
degree-`<K` codewords on that same support. Then

```text
|Z| <= floor(max(
  n^(falling s+1) / (m * w^(rising s)),
  (n-K+s)^(falling s+1) / w^(rising s+1)
)).
```

No global direction-separation hypothesis is required.

When `A=C` and `K=s`, the two terms coincide and the bound is

```text
J_s=floor(product_(i=0..s) (n-s+i)/(m-s+i)).
```

For the whole-line global-core router, this pays every shortened selected
slope family through `s=13` on KoalaBear and through `s=5` on Mersenne-31,
whether or not the shortened direction lies in the agreement ball.

## Consequence

The former `DIRECTION_LIST_SHORTENED_S` residual is unnecessary in the
support-wise MCA application. The first global-core residuals are now
`s>=14` on KoalaBear and `s>=6` on Mersenne-31.

## Nonclaims

This does not improve the numerical bound once `J_s>B*`, supply global-core
first-match coverage, define Q/BC, or close either deployed or prize row.

## Falsifier

An exact pair-noncontained support whose incident normal matrix has rank
below `s+1`, or a support-wise family exceeding the displayed incidence
bound.
