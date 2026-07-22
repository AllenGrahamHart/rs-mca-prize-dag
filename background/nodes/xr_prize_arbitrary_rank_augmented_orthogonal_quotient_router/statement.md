# XR prize arbitrary-rank augmented-orthogonal quotient router

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_prize_arbitrary_rank_dual_projective_support_router`,
  `xr_prize_arbitrary_w_rank_two_received_pair_router`

Use a support-minimal rank-`r` trade circuit from the arbitrary-rank
dual-projective router. Let

```text
P:L->F^2,       P(F)=(<F,b>,<F,q>),
K=ker P=L intersect (W+<b,q>|X)^perp,
s=rank P in {0,1,2}.                                 (OQ1)
```

Then `dim K=r-s`, and every active row satisfies

```text
P(lambda_i) dot (1,gamma_i)=0.                       (OQ2)
```

There are exactly three interaction classes.

1. **`s=0`.** The complete row space is augmented-orthogonal.
2. **`s=1`.** Exactly one active row lies outside `K`; its slope is the
   unique affine root of the nonzero image direction. Every other row is in
   `K`, and circuit independence sharpens the arity bound to

   ```text
   r+2<=t<=2r-1.                                     (OQ3)
   ```

3. **`s=2`.** After choosing quotient coordinates `L/K=F^2`, every row has

   ```text
   P(lambda_i)=tau_i(-gamma_i,1),                    (OQ4)
   ```

   where `tau_i=0` exactly for augmented-orthogonal rows. Thus the complete
   interacting quotient is slope-determined. Its coefficient-slope columns
   lie on the conic

   ```text
   tau_i(-gamma_i,1,-gamma_i^2,gamma_i),             (OQ5)
   ```

   whose span has dimension at most three.

Consequently arbitrary trade rank creates no higher-dimensional received
interaction: every packet is an augmented-orthogonal lift of a rank-zero,
rank-one, or slope-determined rank-two quotient. This theorem does not count
those lifts or prove the aggregate P-A bound.
