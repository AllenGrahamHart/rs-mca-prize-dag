# KoalaBear m2 r4 coordinate negative one-loop 442 S1 forced-DE F41 product witness

- **status:** PROVED
- **scope:** a route-cut fixture over `F_41` for the canonical `S1`
  forced-`DE` outside product cell
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_cubic_root_gate`,
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_explicit_involution_compiler`,
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_complete_edge_skeleton_classifier`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_binary_sextic_eigenvalue_compiler`
- **consumer:** `rate_half_band_closure`

On the proved common witness over `F_41`, take

```text
i=9, (epsilon_1,epsilon_2)=(1,1),
b=10, c=5, r=12, t=30,
(Gamma,Alpha,Beta)=(7,16,16), Delta=-1, m=18.
```

In skeleton `S1`, choose singleton signs
`(alpha,beta,gamma,delta)=(1,-1,-1,1)` and

```text
(d,e,f)=(15,7,18).                                (KB41FW-1)
```

Then the forced record is `gamma*d*e=-d*e=18=m`.  The five common and seven
outside products are respectively

```text
(23,10,31,5,36),
(35,33,18,24,21,3,38),                            (KB41FW-2)
```

and all twelve are distinct.  The six residual outside products form the
three involution pairs

```text
(35,24), (33,38), (21,3).                         (KB41FW-3)
```

The six signed representative squares of `(1,b,c,d,e,f)` are also distinct.
After scaling the residual binary sextic by `d`, its coefficient vector is

```text
(15,27,7,12,23,1,17),                            (KB41FW-4)
```

and all seven equations `H(M)=Delta^3 H` vanish.  Exhausting all `40^2`
nonzero pairs in the coordinates `e=-m/d`, `f=sd` finds `(d,s)=(15,34)` as
the unique guarded invariant pair.

Thus the canonical `S1` forced-`DE` cell is not excluded by
characteristic-independent product geometry.  This witness is not in the
deployed characteristic and does not satisfy or test the seven outside
`q` rows, full interpolation, or either Prize result.

## Falsifier

Failure of any arithmetic identity in `(KB41FW-1)--(KB41FW-4)`, a collision
among the printed guards, or a second guarded invariant pair in the complete
`F_41` scan.
