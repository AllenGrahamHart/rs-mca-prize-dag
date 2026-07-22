# Proof - L1 Mersenne-checkpoint embedded two-fiber family

Write `H=gamma K`, where `K` is cyclic of order `mN`. Its unique subgroup
`K_2` of order `2N` has index `m/2`, so the cosets of `K_2` partition `H`
as asserted.

Fix one coset `H_j`. Its order is

```text
2N=2p+2.                                               (1)
```

The exact `m=2` classification in
`l1_official_split_pencil_value_capacity` applies to any multiplicative
coset of this order. For each antipodal complement `{x,-x}`, it gives
`C,R,delta` as in `(EM2-1)--(EM2-2)` and the identity

```text
(R-delta)(R+delta)=Omega_(H_j)/C.                      (2)
```

The right side is squarefree and split in `H_j`; the two factors are coprime
and each has degree `p`, so both split completely there. Since `H_j` is a
subset of `H`, they are also complete split fibers in the full domain.
Their constant difference gives the first-checkpoint moment collision by the
split-pencil converse.

The involution `x -> -x` has no fixed point in odd characteristic and
partitions the `2N` points of `H_j` into `N` antipodal pairs. The exact
two-fiber theorem is injective in the complement, giving `N` unordered
fiber pairs in that coset. A fiber pair determines the unique coset
containing its union, so pairs from different `H_j` cannot coincide. This
proves `(EM2-3)`.

Finally, expansion of `R=Z(Z^2-b)^((p-1)/2)` has leading term `Z^p` and
nonzero next term of degree `p-2`. Thus the normalized perturbation has
degree exactly `p-2`. The first-checkpoint constraint

```text
deg Q<=2p-d-1                                          (3)
```

holds exactly for `d<=p+1`; intersecting with the checkpoint range `d>=p`
gives `(EM2-4)`.

The polynomial `C` is even and `(p-1)/2` is an integer, so `R` is odd. If
`R-beta` splits completely in `H`, negating its roots shows that `R+beta`
also splits completely. The value zero cannot be split: the distinct roots
of `R` are zero and the two roots of `C`, and zero is not in a multiplicative
coset, leaving only two possible domain roots, fewer than `p`. Therefore the
split values form nonzero sign pairs and their number `h` is even. The
maximal-value theorem excludes `h=m`; listing the remaining positive even
integers through `m-1` proves `(EM2-5)`.
