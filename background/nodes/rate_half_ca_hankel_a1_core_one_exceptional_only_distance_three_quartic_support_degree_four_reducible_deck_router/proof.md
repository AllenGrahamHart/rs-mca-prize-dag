# Proof

Let

```text
C(X,Y)=[S(X)R(Y)-S(Y)R(X)]/(X-Y)                    (1)
```

be the off-diagonal coincidence polynomial of the separable degree-four map
`psi=S/R`. Over the algebraic closure, reducibility of the degree-three
polynomial `(1)` in `Y` gives a linear factor. It is the graph of a
nonidentity automorphism of the extension

```text
k(X)/k(psi),                                         (2)
```

hence the graph of a Mobius deck transformation. If no graph component is
defined over the base field, all base-field points lie in intersections of
Frobenius-conjugate components; the total intersection charge is at most
18, far below the `2(e-148)` captured ordered points. We may therefore fix
a base-field deck graph `Gamma_tau`. Removing it leaves a base-field divisor
`D` of bidegree at most `(2,2)`.

We need one finite Newton-support lemma. Every absolutely irreducible
non-toral polynomial supported in the square `[0,2] x [0,2]` has a
two-dimensional Newton polygon. A unimodular monomial coordinate change and
a monomial translation put it under the published subgroup estimate with
bidegree at most `(2,3)`, nonzero constant term, and nonconstant restriction
on the zero boundary. The worst constant is

```text
16*2*3^2*(2+3)=1440.                                 (3)
```

This is a finite lattice lemma: the verifier exhausts all `2^9` supports,
discards the lower-dimensional ones, and prints a valid determinant-one
change for each of the remaining `458`. A lower-dimensional absolutely
irreducible support is a primitive binomial and is toral.

There are at most two positive-bidegree geometric components in `D`.
Consequently, if `Gamma_tau` is nonspecial and `D` has no toral component,
the published graph and residual bounds, including a conservative charge
for non-base-field component intersections, give

```text
#C(mu_N x mu_N)<=
  (32+2*1440)N^(2/3)+8
  =2912N^(2/3)+8.                                   (4)
```

Exact cubing verifies

```text
2912N^(2/3)+8<2(e-148),       N=2^41.               (5)
```

This contradicts the captured pair count. Hence either the deck graph is
special or `D` has a toral component carrying subgroup points.

If the special deck graph itself has no subgroup point, it contributes zero
to the captured count. The two non-toral residual components alone have at
most `2880N^(2/3)+8<2(e-148)` points, so in that case `D` must have a toral
component carrying a captured point. Thus some special component carrying a
subgroup point will be obtained in either branch.

In the second case, write a primitive toral component as

```text
X^aY^b=q.                                            (6)
```

Neither exponent is zero because the coincidence divisor is primitive in
both variables. On its normalization, the two coordinate projections have
degrees `|b|` and `|a|`. Equality of their compositions with the degree-four
map `psi` gives

```text
4|a|=4|b|.                                           (7)
```

Primitivity then forces `|a|=|b|=1`. Thus `(6)` is itself one of the
special Mobius graphs

```text
Y=qX,       XY=q.                                    (8)
```

We have proved in all cases that `psi` has a special deck automorphism
carrying a subgroup point. Its constant therefore lies in `mu_N`.

The cyclic deck map is `X |-> zeta X`. Its order divides the degree four of
`(2)`, so the nonidentity order is `h=2` or `4`; its invariant field is
`k(X^h)`, proving `(Q4D1)`. The other special map is the involution
`X |-> c/X`, whose invariant field is `k(X+c/X)`, proving `(Q4D2)`.
Degree multiplicativity gives the displayed outer degrees. QED.
