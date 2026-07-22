# XR prize arbitrary-`W` rank-two received-pair router

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_prize_arbitrary_w_rank_two_dual_plane_support_router`,
  `xr_rank_two_received_pair_alternating_router`

Let `L=<F,G> subset (W|X)^perp` be a four/five-block arbitrary-`W` dual-plane
packet. With the ordinary pairing on `X`, put

```text
theta=(<F,b>,<G,b>,<F,q>,<G,q>).                     (IR1)
```

For every circuit row with coefficient direction `[c_i:d_i]` and slope
`gamma_i`, selected-block realization forces

```text
theta dot (c_i,d_i,gamma_i c_i,gamma_i d_i)=0.       (IR2)
```

Hence:

1. **Five blocks.** The Segre columns span `F^4`, so

   ```text
   <F,b>=<G,b>=<F,q>=<G,q>=0.                        (IR3)
   ```

   Equivalently, `L` lies in the dual of the augmented received space
   `W+<b,q>` on `X`.

2. **Four blocks.** If

   ```text
   A c+B d+C gamma c+D gamma d=0                     (IR4)
   ```

   is the canonical Mobius hyperplane of the Segre circuit, then

   ```text
   theta=eta(A,B,C,D)                                (IR5)
   ```

   for one scalar `eta`. At `eta=0` the plane again annihilates both received
   directions. At `eta!=0`, the interaction matrix

   ```text
   ((<F,b>,<F,q>),(<G,b>,<G,q>))                     (IR6)
   ```

   is invertible, because nonconstancy of the Mobius graph is exactly
   `AD-BC!=0`. This is the perfect-pairing branch.

Conversely, `(IR3)` or `(IR5)` certifies every selected trade-row pairing
against `b+gamma_i q`. It does not certify the full agreement blocks.

Thus every arbitrary-`W` rank-two dual plane is either augmented-orthogonal
or a four-block perfect interaction plane. The theorem does not count either
class or prove the aggregate P-A bound.
