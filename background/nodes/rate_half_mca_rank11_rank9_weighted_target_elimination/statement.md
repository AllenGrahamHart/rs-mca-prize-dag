# Rank-nine weighted target elimination

- **status:** PROVED
- **scope:** the rank-nine affine-owner alternative of the fixed
  nine-subset component target

That alternative is empty for every residual dimension
`10<=K'<=1048576`.

For `K'<=67472`, the target's `2578110` records force a common plane core
of size at least `134944`, while pair noncontainment requires every owner
core, and hence the plane core, to have size below
`m'=67472+K'<=134944`.

For `K'>=67473`, the fixed-`B` weighted demand and cap satisfy

```text
W_B >=ceil((495405467/10^9) N_min
           *C(m',9)*C(m'-9,2)/C(n',9)),
W_B <=981105*(m'-10)*n'.
```

At the boundary `K'=67473`, these are

```text
6849288576200976639 > 147748596828055575.
```

The ratio of the unrounded lower bound to the upper bound increases with
`K'`, so the contradiction persists through the deployed endpoint.

## Consequence

The fixed component target now has two live branches: the fixed kernel chart
and the rank-eight owner flat. Rank eleven as a whole remains unpaid.
