### 2026-08-10 general-t FPC5 fixed-background Hankel codimension

The new PROVED node
`l1_fpc5_tpetal_fixed_background_hankel_codimension` handles the `u>=0`
background threshold inside the Padé-Hankel chart. For a fixed required
`u`-set `R`, append `L_R` to the CRT modulus with label zero. Since

```text
u=d-(t-1)ell,
```

the augmented low-numerator Hankel block has exactly

```text
t ell+u-d-1=ell-1
```

full-rank rows. Its locator vector space has dimension `d-ell+2`, and its
monic split-divisor chart has affine codimension exactly `ell-1`, independent
of `t` and `u`.

The exact background incidence identity is

```text
sum_(|R|=u)|F_R|=sum_G binom(|R_G|,u).
```

A first-`R` rule partitions contributors but does not preserve the complete
linear chart. No critical status changes. The remaining obligations are a
base-field-normalized guarded split-divisor bound in each rational Hankel
cell and a chronology-valid weighted or first-`R` aggregation. Export to
`rs-mca` PR #1151 is pending.
