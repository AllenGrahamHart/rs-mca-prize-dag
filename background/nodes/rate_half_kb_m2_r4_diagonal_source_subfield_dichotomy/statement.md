# KoalaBear m2 r4 diagonal source-subfield dichotomy

- **status:** PROVED
- **scope:** actual `(m,r,delta)=(2,4,2)` component with stabilizer
  `S=<tau x tau>`
- **dependency:**
  `rate_half_kb_m2_r4_diagonal_fiber_resultant_interpolation_compiler`
- **consumer:** `rate_half_band_closure`

Let `E` be the function field of the normalization of the actual endpoint
component. The birational bidegree-`(2,4)` source model gives a tower

```text
F=K(W) subset K(X) subset E,
[K(X):F]=[E:K(X)]=2,       W=psi(X).               (KBDS-1)
```

Let `sigma` be the diagonal stabilizer automorphism, so
`sigma(T)=tau(T)` and `sigma(W)=tau(W)`, and put
`K_1=sigma(K(X))`. Exactly one of the following holds.

1. **Source-line lift.** If `K_1=K(X)`, then `sigma` restricts to a
   projective involution `s` of the source line with

   ```text
   psi(sX)=tau(psi(X)),       sb=bs,                (KBDS-2)
   ```

   where `b` is the deck involution of `psi`. The actual source equation
   is preserved by `(T,X)->(tau(T),s(X))`, and hence

   ```text
   star(sx)=tau(star(x)).                            (KBDS-3)
   ```

   Over the geometric closure there are compatible coordinates

   ```text
   b(X)=-X,       s(X)=1/X,       psi(X)=X^2,
   tau(Z)=1/Z.                                      (KBDS-4)
   ```

   A bidegree-`(2,4)` source equation then obeys

   ```text
   T^2 X^4 H(1/T,1/X)=epsilon H(T,X),
   epsilon in {+1,-1}.                              (KBDS-5)
   ```

   The two reciprocal coefficient spaces have dimensions eight and seven.

2. **Biquadratic source cover.** If `K_1!=K(X)`, then `E/F` is Galois
   with group `V4`. If `eta` fixes `K(X)` and
   `eta'=sigma eta sigma^(-1)`, the third deck involution is
   `mu=eta eta'`. If `g` is the source-normalization genus, then

   ```text
   g in {0,1},       #Fix(mu)=2-2g.                 (KBDS-6)
   ```

   The exact tame branch passports over the `W`-line are

   ```text
   g=0: eta, eta', mu;
   g=1: eta, eta, eta', eta'.                       (KBDS-7)
   ```

This dichotomy does not delete either branch or the diagonal orientation.
It does not identify this function-field `V4` with the already-deleted
full ambient stabilizer type. It proves no order-two type, trivial type,
owner, payment, row, or Prize result.

## Falsifier

An actual diagonal component for which `sigma(K(X))` is neither `K(X)`
nor a second quadratic intermediate field producing the printed `V4`
cover; failure of `(KBDS-2)--(KBDS-5)` in the first branch; or a
non-lifting source of genus at least two or with a passport outside
`(KBDS-7)`.
