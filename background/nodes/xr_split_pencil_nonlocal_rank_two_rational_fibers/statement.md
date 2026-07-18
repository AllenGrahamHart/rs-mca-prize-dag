# XR nonlocal rank-two rational-fiber dictionary

- **status:** see `dag.json` (single source of truth)
- **consumers:** `xr_highcore_collision_count`, `xr_lowcore_spread_heart`
- **dependencies:** `xr_split_pencil_trade_rank_two_support_atlas`,
  `xr_split_pencil_six_face_syzygy_quotient`

Let `Lambda` be a rank-two trade representing a nonzero class after the
six-face-syzygy quotient. Let `X` be its active coordinate set. Then there
are exactly four active rows with distinct slopes `gamma_1,...,gamma_4`, and
the zero sets `Z_i=X\supp(lambda_i)` form one of the two partitions

```text
|X|=7:  (|Z_1|,...,|Z_4|)=(1,2,2,2),
|X|=8:  (|Z_1|,...,|Z_4|)=(2,2,2,2).                  (RF1)
```

There is a rational function `phi in F(X)` such that

```text
phi(x)=gamma_i  iff  x in Z_i,       x in X,           (RF2)
deg phi <= |X|-5.                                      (RF3)
```

Consequently:

1. In the seven-coordinate profile, `deg phi=2`. In characteristic not two,
   its three two-point fibers are orbits of one nontrivial Mobius involution
   of the projective line. The singleton coordinate is either fixed by that
   involution or has its partner outside `X`.
2. In the eight-coordinate profile, `deg phi` is two or three. In the
   degree-two branch all four pairs are orbits of one Mobius involution. The
   degree-three branch is a genuine residual possibility.

Both quadratic profiles occur over `F_101`, and the cubic eight-coordinate
profile occurs over `F_103`. Thus generic dual-code or pair-cap arguments
cannot remove either side of the dichotomy. A payment must own the local
quadratic pullback charts and separately control the cubic profile. This
dictionary does not supply that payment or promote either consumer.
