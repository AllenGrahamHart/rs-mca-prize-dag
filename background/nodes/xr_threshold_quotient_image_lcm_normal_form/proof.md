# Proof

Write `C|_S` for the image of the restriction map `C -> F^S`. A slope `z`
is explained on `S` exactly when

```text
(u+zv)|_S in C|_S,
```

or equivalently

```text
a_S+z b_S=0 in Q_S.                                  (1)
```

The pair `(u,v)` is simultaneously explained on `S` exactly when
`a_S=b_S=0`. This is the contained branch and contributes no support-wise
bad slope, which explains the first clause of `(QIL1)`.

Suppose now that `(a_S,b_S)!=(0,0)`. Choose a basis of `Q_S`. Equation (1)
holds exactly when every coordinate form

```text
L_(S,i)(z)=a_(S,i)+z b_(S,i)
```

vanishes. At least one coordinate form is nonzero. Their common roots are
therefore exactly the roots of their monic gcd `g_S`. Since one nonzero form
has degree at most one, `deg g_S<=1`.

This definition is basis-independent. A basis change applies an invertible
linear combination to the coordinate forms, so it preserves their generated
ideal in `F[Z]` and hence its monic generator. Equivalently, it preserves
equation (1) and its empty or singleton root set. This proves `(QIL1)`.

Now let `S` be any finite support family. By the fixed-support result, its
distinct noncontained slope image is

```text
union_(S in S) roots_F(g_S).
```

The root set of a least common multiple is the union of the factor root sets;
taking the radical removes repeated factors without changing that union.
Thus the image is exactly `roots_F(R_S)`. Every nonconstant `g_S` is a monic
linear polynomial over `F`, so `R_S` is a squarefree product of distinct
`F`-linear factors. Its number of roots is therefore its degree, proving
`(QIL2)` and `(QIL3)`.

The quotient-remainder threshold family is finite because the domain, scale
set, and support-size interval are finite. Applying the preceding identity to
that family gives the asserted threshold-union polynomial. The proof is an
exact image identity only; it supplies no degree estimate. QED.
