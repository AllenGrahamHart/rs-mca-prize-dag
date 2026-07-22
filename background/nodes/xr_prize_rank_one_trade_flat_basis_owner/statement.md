# XR prize rank-one trade flat/basis owner

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_prize_flat_nullity_maxwell_trade_space_compiler`,
  `xr_prize_flat_nullity_rank_metric_trade_router`,
  `xr_rs_flat_nullity_basis_charge`, `xr_poststrip_affine_pencil_charge`

Let a rank-one trade in a normalized prize P-A cell have active block set
`J`, `ell=|J|>=3`, and common nonzero dual support `S`. Put

```text
j=rk_W(S).
```

Two active slopes imply the stronger local condition

```text
b|S in W|S,       q|S in W|S.                        (FO1)
```

There is an exact owner dichotomy.

1. **Spanning support (`j=a`).** Choose the lexicographically first `W` basis
   `T subset S`. Every point of `S\T` is persistent for both basis residuals

   ```text
   a_T=b-I_Tb,       d_T=q-I_Tq.
   ```

   All active blocks contain `T`, and the exact moving-zero charge gives

   ```text
   ell<=floor((R-v)/h).                               (FO2)
   ```

2. **Proper-flat support (`j<a`).** The canonical owner
   `F=cl_W(S)` is a proper rank-`j` flat satisfying

   ```text
   S subset F,       |F|<=j+u.                       (FO3)
   ```

   Since `S` is dependent, this branch requires `u>=1`.

The owner is canonical after fixing the ambient coordinate order: first
choose the support `S`, then its closure, and in the spanning branch its first
basis. When `u=0`, the proper-flat branch is empty, so every rank-one trade is
a persistent basis-pencil record.

This theorem does not sum owner fibers, count proper flats, or pay the
trade-rank-at-least-two stratum.
