# KoalaBear m2 r4 positive coordinate three-loop common-placement atlas

- **status:** PROVED
- **scope:** every loop placement and common-edge sign orbit in the positive
  three-loop profiles `(4,4,2)` and `(4,3,3)`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_three_loop_common_kernel_compiler`
  and
  `rate_half_kb_m2_r4_coordinate_positive_three_loop_complete_edge_skeleton_classifier`
- **consumer:** `rate_half_band_closure`

Put the quotient branch loops at `W=0,infinity` and the `B_1`-root loop at
`W=1`.  In each profile there are exactly two loop-placement orbits: the
root loop carries a high-degree target pair or a low-degree target pair.
Thus the two profiles have exactly four common placement orbits.

Normalize the target representatives at the three loop slots to `1,b,c`.
Let `x,y` be the two nonloop source lifts.  The common-kernel determinant in
each orbit is a product of the explicit source/target collision guards and
one residual:

```text
R_442,L = (y-x)(b^2-c^2)+bxy(x+y)(c^2-1),

R_442,H = (y-x)(b^2-c^2)
          +xy[x(c-1)(b^2+c)+y(c+1)(b^2-c)],

R_433,L = (y-x)(b^2-c^2)
          +(c-1)xy[b(c+1)x-(b^2+c)y],

R_433,H = (b-c)[(b+c)y-(bc+1)x]
          +xy(c-1)[(b^2+c)x-b(c+1)y].             (KBP3A-1)
```

Here `L/H` records the degree class carried by the root loop.  The 442
nonloop pair uses both opposite signed types; in 433 the common graph is a
tree, so its two edge signs are absorbed into the signed target
representatives.  Every residual has total degree six.

This atlas does not assert that a residual solution has an admissible
kernel, delete any orbit, impose an outside edge, close positive parity, or
prove either Prize result.

## Falsifier

A fifth loop-placement/sign orbit, an actual common packet outside these
four matrices, or failure of any guarded determinant factorization in
`(KBP3A-1)`.
