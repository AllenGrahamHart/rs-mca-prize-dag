# PMA sigma-one B11 threshold collapse and finite-payment route cut

- **status:** PROVED
- **consumer:** `pma_wide_residual`
- **source:** `pma_b11_first_match_router`

## Statement

On the official dyadic grid

```text
n=2^s, 13<=s<=44, rho in {1/2,1/4,1/8,1/16}, k=rho*n,
sigma=1,
```

a maximal sunflower has

```text
ell=2, M=(n-k)/2, b=1.
```

Use the B11 first-match thresholds

```text
(E,V_2,V_R)=(0,2,0).
```

Then, after the exact-periodic owner, the B11 partition collapses to

```text
d<=2: J or A2;
d>=3: GROW;
AR=RES=empty.
```

Indeed every touched-petal deficit is zero or one, so `G_2<=2`. The exact
B11 certificate for the paid part is

```text
J(n,k) + 11 binom(M,2) q^4,                         (S1)

J(n,k)=n(n-k+1)/Delta,
Delta=(floor(sqrt(n(k-1)))+1)^2-n(k-1).
```

Here `q` is the generated-field size. Formula `(S1)` is an upper certificate,
not a lower bound on the realized class.

Let `q_fit(n,k)` be the largest integer `q` for which `(S1)<=n^6`. It is
given exactly by

```text
q_fit=floor_root_4(
  floor((Delta*n^6-n(n-k+1))/(11*Delta*binom(M,2)))
).
```

At rates `1/8` and `1/16`, on every official row,

```text
q_fit<n+1.
```

Any field containing a cyclic evaluation domain of order `n` has
`n | (q-1)`, hence `q>=n+1`. Consequently this B11 certificate cannot fit
even the entire `n^6` primitive allocation at those two rates. It therefore
cannot supply a field-uniform finite PMA payment, still less an unspecified
post-full-petal remainder.

## Scope

The theorem closes the finite `sigma=1` threshold choice and proves that
`RES` is absent on that track. It does not show that the actual `d<=2` class
exceeds `n^6`, does not refute `imgfib`, and does not address the
asymptotic-reserve track where `ell` grows and fixed `V_2` no longer exhausts
all petal deficits. The live finite obstruction is the looseness and
field-dependence of the B11 cofactor census, not a missing threshold.
