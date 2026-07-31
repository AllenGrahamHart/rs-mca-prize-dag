# Proof

At a common-`K` fiber the negative Vieta equation is

```text
A_1(kappa)+q_kappa B_2(kappa)=0.                  (1)
```

The loop-budget theorem proves that an antipodal edge is exactly a zero of
`q_kappa` and forces `A_1(kappa)=0`.  The loop labels are distinct and
`ell<=2`, so their product `R_Lambda` divides the degree-at-most-two form
`A_1`.  This gives `(KBNQ-1)`.

Substitute `(KBNQ-1)` in `(1)` at the `5-ell` nonloop labels.  Expanding
`C` in the monomial basis of degree at most `2-ell` and `B_2` in the basis
`1,W` gives exactly the row `(KBNQ-2)`.  There are

```text
(3-ell)+2=5-ell
```

unknown coefficients and the same number of nonloop rows.  The actual
nonzero coefficient vector is in the kernel, so the square determinant
vanishes.  Conversely a kernel with `B_2(kappa)!=0` at every common fiber
reconstructs the sum half of the five negative Vieta records.  This proves
`(KBNQ-3)--(KBNQ-4)` and the support guard. QED.
