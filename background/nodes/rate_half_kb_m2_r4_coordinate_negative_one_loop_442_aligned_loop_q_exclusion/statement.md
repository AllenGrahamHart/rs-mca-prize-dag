# KoalaBear m2 r4 coordinate negative one-loop 442 aligned loop-q exclusion

- **status:** PROVED
- **scope:** both aligned common families and all product-level `S1-DE`,
  `S1-DF`, and `S2` survivors
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`,
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_aligned_pair_classifier`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_aligned_outside_product_router`
- **consumer:** `rate_half_band_closure`

Write the negative complete-fiber equations as

```text
B_0(W)-p_W B_2(W)=0,       A_1(W)+q_W B_2(W)=0.   (KB41Q-1)
```

The five common records determine the following scaled triples:

```text
A: B_0=b(1-c)(1-i), B_2=(1-c)(1-i)W,
   A_1=-(1+b)(W-c)(W-i),              F(W)=b/W;

B: B_0=b(1-i)W, B_2=1-i,
   A_1=-(W+b)(W-i),                   F(W)=bW.     (KB41Q-2)
```

All printed scale factors are units.  The common loop occupies the first
root `W=c` in family A and `W=-b` in family B.  Every retained outside
skeleton has exactly one further loop.  Its edge sum and hence `q_W` are
zero, while `B_2(W)` is nonzero, so `(KB41Q-1)` forces that loop to the
second root `W=i`.  Its product must therefore be

```text
A: F(i)=r,              B: F(i)=ib.               (KB41Q-3)
```

For `S1`, combining `(KB41Q-3)` with the routed loop product `-d^2` and
`d^4=-alpha*beta*gamma*delta*b^2c^2` forces `r^2` or `b^2` to be
`+1` or `-1`, contrary to the family equations.  For `S2`, its routed
loop product `b^2` cannot equal `r` in family A or `ib` in family B.
Thus every aligned product survivor is empty before the six nonloop
outside q rows or full interpolation are needed.

This theorem does not by itself compose the other five common matching
orbits, close another negative skeleton, close the coordinate orientation,
close a Prize row, or prove either Prize result.

## Falsifier

An admissible retained aligned packet whose common Vieta triple is not a
scalar multiple of `(KB41Q-2)`, a protected factor that vanishes, an
outside loop away from `W=i`, or a routed `S1/S2` branch compatible with
the product in `(KB41Q-3)`.
