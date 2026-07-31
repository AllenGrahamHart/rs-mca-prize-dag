# KoalaBear m2 r4 coordinate negative loop-stratified q compiler

- **status:** PROVED
- **scope:** every negative-parity coordinate packet in one of the five
  common-`K` skeletons retained by `(KBNL-2)`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler` and
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate`
- **consumer:** `rate_half_band_closure`

Let `Lambda subset K` be the `ell=|Lambda| in {0,1,2}` fibers whose
`J` edge is antipodal, and put

```text
R_Lambda(W)=product_(lambda in Lambda)(W-lambda).
```

Then

```text
A_1(W)=R_Lambda(W) C(W),       deg C<=2-ell.       (KBNQ-1)
```

For every nonloop fiber `kappa in K minus Lambda`, define the row

```text
[R_Lambda(kappa), R_Lambda(kappa)kappa, ...,
 R_Lambda(kappa)kappa^(2-ell), q_kappa,q_kappa kappa]. (KBNQ-2)
```

The resulting square `(5-ell) x (5-ell)` matrix `Q_Lambda` satisfies

```text
det Q_Lambda=0.                                    (KBNQ-3)
```

Its kernel consists of the `3-ell` coefficients of `C` and the two
coefficients of `B_2`, with signs chosen so that

```text
R_Lambda(kappa)C(kappa)+q_kappa B_2(kappa)=0.
```

Thus the loop strata have exact determinant sizes

```text
ell=0: 5 x 5,       ell=1: 4 x 4,       ell=2: 3 x 3. (KBNQ-4)
```

A candidate also requires a kernel vector for which `B_2` is nonzero at
all five `K` labels.  These gates do not exclude a surviving skeleton,
positive parity, the coordinate orientation, an owner/payment, a row, or
either Prize result.

## Falsifier

An actual negative packet whose pinned loop factors do not divide `A_1`,
whose appropriate square determinant is nonzero, or whose reconstructed
kernel lacks the required leading support.
