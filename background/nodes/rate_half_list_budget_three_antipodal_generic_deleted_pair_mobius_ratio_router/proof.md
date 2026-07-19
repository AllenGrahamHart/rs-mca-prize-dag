# Proof

The branch-collapse dependency places all deleted-root lifts, outer roots,
and Möbius data in `F_p`, with `4N` dividing `p-1`. In particular `iota` and
all order-`4N` roots lie in `F_p`.

Write the two deleted antipodal pairs as `{b,-b}` and `{c,-c}`. Within each
pair, order its square-root lifts so that the second is `iota` times the
first. Divide all four lifts by the first one and put `r=a_2/a_0`. This gives
the tuple in `(MRR2)`. Since the squared deleted-pair ratio is `t`,

```text
t=(c/b)^2=r^4.                                        (1)
```

The deleted pairs are distinct, so `t!=1`. Their lifts have order dividing
`4N`, proving the remaining assertions in `(MRR2)`.

The even-factorization dependency gives distinct nonzero `lambda,mu` and the
outer polynomial

```text
(W^2+lambda)(W^2+mu).                                 (2)
```

Choose `alpha^2=-lambda` and `beta^2=-mu`, which are in `F_p` by the branch
collapse. Scaling the target points by `alpha^(-1)` gives
`(1,-1,y,-y)`, where `y=beta/alpha` and `q=y^2=mu/lambda`. Distinctness in
`(2)` gives `q!=1`; exchanging the two pairs inverts `q`.

The ratio has a stronger torsion constraint. In the reverse coordinate, the
two factors of the even-factorization dependency are

```text
H_lambda=B_0^2+lambda w^(2M+1)C_0^2,
H_mu    =B_0^2+mu     w^(2M+1)C_0^2.                  (3)
```

They have degree `L=4M-1=N/2-1`, constant term one, and root sets contained
in `mu_N`. If `c` is the leading coefficient of `C_0`, the monic reversals
`w^L H_lambda(w^-1)` and `w^L H_mu(w^-1)` have constant terms
`lambda c^2` and `mu c^2`. Each constant term is, up to the sign
`(-1)^L`, the product of `N`th roots and therefore lies in `mu_N`. Their
ratio is `q=mu/lambda`, proving `(MRR3)` and `q^N=1`.

For four ordered points define

```text
cr(A,B;C,D)=((A-C)(B-D))/((A-D)(B-C)).                (4)
```

The target antipodal ordering has

```text
z_y=cr(1,-1;y,-y)=((1-y)/(1+y))^2.                   (5)
```

Changing either orientation replaces `z_y` by its inverse. Eliminating that
orientation gives the exact invariant equation

```text
(z-1)^2(1+q)^2=4q(z+1)^2.                            (6)
```

Indeed, substituting `(5)` proves `(6)`. Conversely, as a polynomial in `z`,
the left side minus the right side factors into two linear terms whose roots
are `z_y` and `z_y^(-1)`. This remains valid when `q=-1`, where both roots
are `-1`.

The target antipodal partition pulls back under a Möbius bijection to one of
the three perfect matchings of the source tuple `(1,iota,r,iota r)`. For the
ordered representatives

```text
(1,iota ; r,iota r),
(1,r ; iota,iota r),
(1,iota r ; iota,r),                                 (7)
```

direct use of `(3)` gives

```text
z_0=(r-1)^2/(r^2+1),
z_1=2r/(r^2+1),
z_2=-2r/(r-1)^2.                                     (8)
```

All displayed denominators are nonzero because `r^4!=1`. Substituting the
three values in `(6)` and cancelling their nonzero denominators gives,
respectively, `(MRR4)`, `(MRR5)`, and `(MRR6)`.

Cross-ratio equality, up to the orientation inversion already included in
`(5)`, is necessary and sufficient for a fractional-linear map between two
ordered quadruples of distinct points. Thus one of the three equations is
also sufficient for the Möbius matching, proving the claimed equivalence.

In each equation the leading and constant coefficients as a polynomial in
`q` are the same and nonzero. Its roots are therefore reciprocal, giving at
most one unordered ratio per source pairing. Finally substitute `q=-1` into
the three equations. Their right-side factors give exactly the three
harmonic alternatives stated after `(MRR6)`; the middle alternative
`r=-1` contradicts `r^4!=1`. QED.
