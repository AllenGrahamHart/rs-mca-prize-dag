# Proof

Fix an order-`n` row, a primitive generator `g` of its subgroup, and the
degree-one prime

```text
mathfrak P=(p,zeta-g)
```

of `Z[zeta]`. Suppose `P(t)>=19`. Swapping the two product coordinates
partitions the ordered representations into unordered pairs, with fixed
points only on diagonal representations. Hence the fiber contains at least
`ceil(P(t)/2)>=10` distinct members of `U_n`.

The ten-pair packing lemma proved in
`f3_h3_rich_fiber_norm_cutoff` supplies two distinct members `E,F` among any
ten such representations with

```text
||v_E-v_F||_2^2<=6.                                 (1)
```

Both shifted products reduce to `t` at `mathfrak P`, so
`alpha=beta_E-beta_F` belongs to `mathfrak P`. The proved dyadic
shifted-product Sidon theorem makes `alpha` nonzero. Therefore

```text
p divides |Norm(alpha)|,
```

and `(1)` puts `p` in the finite set `(LDR1)`. This proves `(LDR2)`.

If `p notin C_n`, no target has `P(t)>=19`. Every summand in `X_18` and
`Y_18` then vanishes, and the proved cutoff-18 compiler gives C36'.

It remains to justify the orbit reduction. An odd residue `r mod n` sends
`beta_E-beta_F` to `beta_(rE)-beta_(rF)`. Absolute rational norm is Galois
invariant. The Parseval identity writes the squared vector distance as the
average squared absolute value over all odd conjugates; multiplication by
`r` merely permutes those conjugates. Hence the distance is invariant too.
The other listed exchanges only change the sign of the difference or the
presentation of an unordered pair. Thus one representative per orbit gives
exactly the same candidate-prime union. QED.

## Raw-orbit growth fence

Put `m=n/2` and `M=floor((m-1)/2)`. For every `1<=i<j<=M`, the exponents
`i,j,i+j` are distinct and lie below `m`, so

```text
v_{i,j}=e_(i+j)-e_i-e_j
```

has squared norm three. There are `N=binom(M,2)` such vectors. Fix one of
them, with support `S` of size three. A second support `{u,v,u+v}` can meet a
given `s in S` only through `u=s`, `v=s`, or `u+v=s`; each condition has at
most `M` solutions in the family. Thus at most `9M` second vectors meet `S`.
Every remaining support is disjoint, and the corresponding vector distance is
exactly `3+3=6`. After making the pair of vectors unordered, this gives at
least `(LDR3)` low-distance pair-pairs.

The odd Galois group has order `phi(n)=m`, so every dilation orbit has size at
most `m`. Exchanges have already been quotiented by using unordered root pairs
and unordered pair-pairs. Hence there are at least `ceil(L_n/m)` complete
Galois/exchange orbits. Substitution at `n=8192` gives

```text
m=4096, M=2047, N=2094081,
L_n=2173296943108,
ceil(L_n/m)=530590075.
```

This proves the route fence. It does not lower-bound the number of distinct
norm values, because additional algebraic coincidences may merge many orbits.
