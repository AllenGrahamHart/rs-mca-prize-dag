# Proof

For `z in F_eta`, full outside gives `a(z)=-P(z)` and `b(z)=-Q(z)`.
Therefore

```text
P(z)+eta Q(z)=0.                                      (1)
```

The point is not a common root, so `H(z)!=0`. Cancelling `H` in `(1)` shows
that every distinct point of `F_eta` is a root of the nonzero polynomial
`Pbar+eta Qbar`. Its squarefree locator therefore divides that member. The
degree bound in `(MR4)` follows, and in particular

```text
x+delta_eta<=e.                                      (2)
```

The quantities `h` and `ell` are nonnegative because `L_C|H` and
`deg H+e<=k-1`; equation `(2)` makes `u>=delta_eta>=0`. Using
`c=A-x-s` and `t=A-k`,

```text
h+u+ell
=(deg H-c)+(e-x)+(k-1-deg H-e)
=k-1-c-x
=k-1-(A-x-s)-x
=s-t-1=r.                                            (3)
```

This proves `(MR6)`. In particular `r>=0`, so `s>=t+1`.

Suppose `s=t+1`. Equation `(3)` forces `h=u=ell=0`, and `(MR6)` forces
every `delta_eta=0`. Monicity and `L_C|H` give `H=L_C`; `(MR4)` becomes

```text
Pbar+eta Qbar=kappa_eta L_(F_eta).                    (4)
```

Choose two selected slopes. Their two coefficient rows `(1,eta)` are
independent, so `(Pbar,Qbar)` is an invertible coordinate transform of two
base-field locators. Multiplication by the base locator `H` and restriction
to the fixed source gives a base-field basis for the translated source pair.
The positive-rank case is therefore deleted by the C5 owner; the rank-zero
case has no noncontained witness. Thus the zero-slack boundary is empty after
first match.

The next integer source size is `67474`. The source-rational survivor bound
then gives

```text
e>=ceil(67474/2)=33737,
deg H<=k-1-e=1048575-33737=1014838,
```

which is `(MR7)`.

At `s=t+2`, equation `(3)` partitions one among three nonnegative integral
slacks, proving `(MR8)`. For `(0,0,1)`, `H=L_C`, `e=x`, and every deficit is
zero, so the preceding C5 argument applies. For `(1,0,0)`, the quotient
`H/L_C` is monic linear. If it is base-defined, the same two-member descent
applies, so only a nonbase twist can survive. For `(0,1,0)`, `(MR4)` gives

```text
deg A_eta<=1-delta_eta.
```

Hence `delta_eta` is zero or one. A deficit-one member is a scalar base
locator; two such members trigger C5. More generally two projectively base
members trigger the same argument. With `J>=21`, a surviving record has at
least twenty deficit-zero members, each with a possibly nonbase linear
cofactor. This proves all claims.
