# midlarge_partner_cap_reduction proof

## Claim

For each fixed `h`, the mid/large-`h` trade bound reduces to bounding the
number of active anchored cores at that `h`.

## Proof

Use the proved node `value_set_partner_cap`. For any anchored core `P`, every
partner `Q` in the relevant `h`-window satisfies

```text
L_Q = L_P - c
```

for a value `c` in the value set `{L_P(x) : x in mu_n}`. Distinct partners
consume disjoint `h`-blocks of roots inside the `n`-point domain, so the value
set indexing gives at most `floor(n / h)` partners through a fixed active core.

Let `A_h` be the number of active anchored cores at this `h`. Summing the
per-core cap over active cores gives

```text
partners(h) <= A_h floor(n / h).
```

Thus every mid/large-`h` budget inequality follows once `A_h` is bounded by the
corresponding per-`h` active-core budget. In the recorded row arithmetic that
budget is about `3.3e3` active cores per `h`.

This is only a reduction. The downstream node `midlarge_h_certification` still
requires the separate active-core bounds in the scannable band `h in (6,20]`
and the asymptotic band `h in (20,A]`.
