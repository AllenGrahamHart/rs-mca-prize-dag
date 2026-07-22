# XR prize arbitrary-`W` trade-circuit Segre router

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_trade_circuit_arity_segre_atlas`,
  `xr_prize_flat_nullity_maxwell_trade_space_compiler`,
  `xr_prize_rank_one_trade_flat_basis_owner`

The row-scaling circuit bound does not require a uniform/MDS kernel. For any
trade of matrix rank `r`, every support-minimal row-scaling subtrade has
active arity `ell` satisfying

```text
r+2<=ell<=2r+1.                                       (AW1)
```

Every trade decomposes into such circuits of rank at most its own rank.
Consequently every rank-two trade in an arbitrary flat-nullity polynomial
space `W` decomposes into exactly these coefficient classes:

1. rank-one circuits on three blocks, routed to
   `xr_prize_rank_one_trade_flat_basis_owner`; and
2. rank-two circuits on four or five blocks.

For a rank-two circuit, choose a row-space basis `F,G`, write

```text
lambda_i=c_iF+d_iG,
z_i=(c_i,d_i,gamma_i c_i,gamma_i d_i) in F^4.         (AW2)
```

The `z_i` lie on the Segre quadric. A four-block circuit has column rank
three and is a nonconstant Mobius/Plucker graph between slope and row class.
A five-block circuit has column rank four and every four columns are
independent. These are exactly the same coefficient atlases as in the
uniform theorem; only their support realization now uses arbitrary `W`.

Thus arbitrary block arity is removed from the nonuniform rank-two frontier.
The theorem does not classify four/five-block support embeddings in `W`,
deduplicate them across cores, or pay their aggregate slopes.
