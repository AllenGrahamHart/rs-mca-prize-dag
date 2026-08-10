# Haboeck quadratic Johnson-range MCA theorem

- **status:** PROVED
- **closure:** published theorem import with statement and proof audit
- **source:** IACR ePrint 2025/2110, Theorem 2

Let

```text
C={eval_D(p): deg(p)<=d},   |D|=n,   rho=d/n,
```

so `C` has dimension `d+1`. For an integer `m>=3`, put

```text
gamma_m=1-(1+1/(2m))*sqrt(rho),
ell_m=(m+1/2)/sqrt(rho).
```

For every received pair `f_0,f_1:D->F_q`, let `E_m(f_0,f_1)` be the set of
finite affine slopes `z in F_q` for which there is a support `A subseteq D`
with

```text
|A| >= (1-gamma_m)n,
(f_0+z f_1)|_A in C|_A,
but (f_0,f_1)|_A not in C^2|_A.
```

Haboeck's theorem gives

```text
|E_m(f_0,f_1)| <= (ell_m^7/3)*(rho*n)^2.              (HJ1)
```

For the repository convention `RS[F,D,K]={deg(p)<K}`, the exact reindexing
is

```text
d=K-1,   rho=(K-1)/n.                                  (HJ2)
```

Thus `(HJ1)` is an unconditional finite-affine MCA bad-slope bound at the
displayed discrete Johnson-approaching radii.

## Scope

This node imports only the proved quadratic-in-`n` bound in Haboeck's public
paper. It does not import the sharper linear-in-`n` formula printed in
BCHKS25, does not claim the asserted higher-degree sampler extension, and
does not cross the Johnson radius.
