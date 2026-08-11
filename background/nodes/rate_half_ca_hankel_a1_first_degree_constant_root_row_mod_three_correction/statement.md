# `A=1` first-degree scalar root-row mod-three correction

- **status:** PROVED
- **closure:** row-summed cancelled-cube valuation
- **consumer:** `rate_half_band_crossing_location`

Retain either parameter-constant first-degree profile on the official row,
and write

```text
A_0=B R_a,       e=183251937963=0 mod 3.              (RMC1)
```

Let `x` be a heavy row at which `R_a` has positive multiplicity. Put
`d_x=e-c_x` for its number of distinct supported incidences. At each such
incidence, let `b_gamma` be one or zero according as `x` belongs to the
squarefree minimal recurrence locator, and let `r_gamma>=1` be its
multiplicity in the excess factor. Define

```text
t_x=#{gamma:b_gamma=0},
epsilon_x=sum_gamma(r_gamma-1).                       (RMC2)
```

Then the exact row congruence is

```text
c_x+epsilon_x-t_x=0 mod 3.                           (RMC3)
```

Equivalently, the extra excess degree on that row obeys

```text
epsilon_x>=least nonnegative integer congruent to t_x-c_x mod 3. (RMC4)
```

In particular, if every excess root on the row overlaps the minimal
locator (`t_x=0`), deficits congruent to `0,1,2 mod 3` require respectively
at least `0,2,1` extra excess copies beyond the incidence baseline.

If `E` is the set of heavy roots of `R_a`, the global regular-rank ledger
therefore sharpens to

```text
sum_gamma c_gamma
 >=I_E+2I_0+sum_(x in E) epsilon_x.                  (RMC5)
```

## Scope

The congruence is necessary, not sufficient. It does not assert full
omission, determine `t_x`, or exclude residual scalar degrees `3,4,5`.
