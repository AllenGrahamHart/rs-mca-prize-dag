# Proof

Write `R=R_actual`. The ambient and record-support capacities give

```text
I_d/R <= min(A_d/R,P_d) <= min(A_d/N_min,P_d)=u_d,   (1)
```

because `R>=N_min`. Summing the per-record nine-shadow theorem over all
`R` residual records gives

```text
sum_d w_d I_d/R <= C(m',9),                          (2)
w_d=C(d+2,2)/C(K'-d-9,2).
```

For every nonempty stratum, `w_d` strictly increases with `d`: its
numerator increases and its denominator decreases. Therefore the linear
program maximizing `sum_d x_d` under (1), (2), and `x_d>=0` is the
fractional-knapsack problem obtained by filling `d=1,2,...,9` in order.
Call its exact optimum `Phi(K')`.

This comparison is uniform in the unknown `R`. Replacing `R` by a larger
value only decreases every ambient normalized cap `A_d/R`; the record and
shadow caps are unchanged. Hence the true normalized optimum is at most
the one evaluated at `N_min`.

The dominant kernel lane would require

```text
I_kernel/R >= (495405467/10^9) C(m',11).             (3)
```

The primary verifier evaluates the exact rational difference between (3)
and `Phi(K')` on all 15,436 rows from `K'=10` through `15445`. The
independent verifier reconstructs the same optimum from the dual linear
certificate

```text
Phi <= B/w_f + sum_(d<f) (1-w_d/w_f) u_d,
```

where `B=C(m',9)` and `f` is the first partially filled stratum.

At `K'=15445`, scaling by `N_min` gives

```text
demand =
4344088209787446708963641497455555028744633393303455877367677479,

capacity =
4343910165131984891897760705185029306760436489468113543077136890.
```

At `K'=15446`, the corresponding values are

```text
demand =
4344664578131587275065401301289634311619616096420518827596862523,

capacity =
4344788665170165692429952655282566408633189591744254718078149100.
```

The exact rational comparison has the same sign at both rows, so the
displayed integer gaps are not rounding artifacts.
