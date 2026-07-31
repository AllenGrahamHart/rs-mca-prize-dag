# Proof

Use the normalization in `(KBMMOS-1)`. Exact reconstruction and removal of
the incidence square give the primitive cores

```text
c product (6,8,6) 416 4ab53941752202b3
c sum     (5,12,8) 684 23b328b6dea34346
d product (4,6,8) 284 72568ee71be7f479
d sum     (4,10,9) 532 48c4bf1306aae34b.             (1)
```

The `c` product factors into the two cubic branches
`f2dbb3bdc114d07d` and `fd2b0e09a3a2312a`; the `c` sum is irreducible.
Their branch resultants have digests `02901bcd7b5e39cc` and
`0a2b29ced926a43d`. Complete factor multiplicities bind every factor to a
standard forbidden equation except the common `(4,3)` component
`0d44f8f7254e1a65` and the `(18,14)` component `13fb3d79b89daf53` on the
first branch.

Both `d` cores are reciprocal. Their exact trace digests are
`f0bba9bf4f23b8d2` and `2414ff4e8cdee299`; the parent digest is
`43a8347e92f7f81d`. After forbidden-factor binding, its three components are

```text
9622b8845f94fd73 (1,2),
c7aea723bf6f84a1 (3,2),
dbac8f34560fc4e3 (4,4).                            (2)
```

The six pair projections have digests

```text
45717df443835160 f17eb57458420432 fdc13f78c0f27fd7
1db833f7ec218a23 7b6dd06d29601e4b 0b010d8c5566cd18. (3)
```

Their characteristic-zero factor multiplicities and complete modular
factorizations are pinned in both checkers. Removing standard support and
irreducible degrees not dividing six leaves exactly

```text
d-53820732,
d^2-193204367d-98068426,
d+261596606, d+982346495,
d-1020436165, d-901544254,
d+583634928, d-583634934.                          (4)
```

For each factor in `(4)`, adjoin all four equations `(1)` over
`F_2130706433` and saturate by

```text
bcd; b,c,d in {2,1/2,1,-1};
(b-c)(bc-1)(b-d)(bd-1)(c-d)(cd-1);
5cd-4c-4d+5; 4c^2d-2c^2-3cd+3c+2d-4.             (5)
```

Every saturated basis is `[1]`. Since an irreducible polynomial over
`F_p` has a root in `F_(p^6)` only when its degree divides six, `(3)`--`(5)`
exhaust every deployed-field point.

The primary uses direct inversion and resultants. The no-import audit proves
the source identities with `DomainMatrix.solve_den`, reverse-lifts the
reciprocal `d` traces, and uses terminal subresultants for the cubic parents
and all six pair projections. Both validate the sparse checkpoints and all
eight saturations. Therefore the chart is empty. QED.
