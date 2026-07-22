# XR prize flat-nullity first-core peeling owner

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_prize_flat_nullity_maxwell_trade_space_compiler`,
  `xr_uniform_maxwell_first_core_peeling_owner`,
  `xr_prize_flat_nullity_nonpersistent_root_cap`

Fix any normalized prize P-A flat-nullity cell after deleting its at-most-`v`
exceptional slopes. Order its blocks, coordinates, parity rows, and field
elements once. Repeat:

1. if the current family satisfies the Maxwell density inequality, choose
   its lexicographically first inclusion-minimal dense core;
2. choose the first nonzero trade in the canonical row-reduced left-kernel
   basis of that core;
3. attach the resulting pointed certificate to the first active block and
   delete that block.

Every deleted block receives exactly one certificate. The process terminates,
and the retained terminal family has size at most

```text
floor((2(R-v)-1)/h).                                  (PO1)
```

Including the initially deleted exceptional slopes, the total unowned
population is at most

```text
v+floor((2(R-v)-1)/h)<n                               (PO2)
```

on every prize row. It is therefore already inside the `8n^3` allocation.

Each pointed certificate contains its `(a,u,v)` cell, minimal core, excess
`e`, normalized trade, trade rank, and the first applicable rank-one or
rank-two owner from the proved routers. Thus one cell no longer incurs
duplication across overlapping Maxwell cores or multiple trades.

This theorem proves ownership and pays the terminal remainder. It does not
bound the number of nonterminal basis/flat/dual-plane certificates or sum
them across cells.
