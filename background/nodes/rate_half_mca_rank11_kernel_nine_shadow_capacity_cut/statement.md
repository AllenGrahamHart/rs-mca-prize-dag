# Kernel nine-shadow capacity cut

- **status:** PROVED
- **scope:** the dominant rank-deficient lane for `10<=K'<=15445`
- **units:** `(record, eleven-subset)` incidences

Let `R_actual>=N_min=274980728111260126` be the residual-record count. For
each corank `d`, retain the hybrid individual cap

```text
I_d/R_actual <= u_d(K')
  := min(A_d(K')/N_min, P_d(K')).
```

The nine-shadow theorem additionally gives

```text
sum_d w_d(K') I_d/R_actual <= C(m',9),
w_d(K')=C(d+2,2)/C(K'-d-9,2).                       (S)
```

Let `Phi(K')` be the maximum of `sum_d x_d` subject to (S),
`0<=x_d<=u_d(K')`. The weights increase with `d`, so the exact optimizer
fills the corank strata in order. Exact replay proves

```text
Phi(K') < (495405467/10^9) C(m',11)
```

for every `10<=K'<=15445`. At the endpoint, the demand exceeds the scaled
capacity by

```text
178044655461817065880792270525721984196903835342334290540589.
```

At `K'=15446`, the scaled capacity exceeds demand by

```text
124087038578417364551353992932097013573495323735890481286577,
```

so this one-shadow method stops there. At both boundary rows the optimizer
uses all of corank 1, `0.776...` of the corank-2 cap, and none of the higher
coranks.

## Falsifier

A violation of the nine-shadow inequality, nonmonotonicity in the unknown
record count, a lower-weight higher corank, any failed row in the closed
interval, or a claim beyond `K'=15445`.
