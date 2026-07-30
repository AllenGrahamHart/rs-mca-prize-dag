# Proof

The coordinate source-facet theorem imports the preserving source lift

```text
(T,X) -> (tau(T),b(X)).                             (1)
```

Both projectivities are nontrivial involutions in odd characteristic, so
over the geometric closure they may be normalized independently to
`tau(T)=-T` and `b(X)=-X`. The quotient coordinate is then `W=X^2` after
a projective target change.

The lift `(1)` preserves the irreducible source component. Its defining
bihomogeneous form is therefore an eigenvector. Since the action has order
two and the characteristic is odd, the eigenvalue is `epsilon=+1` or
`epsilon=-1`, proving `(KBCO-1)`.

Every form of `X`-degree at most four has a unique decomposition

```text
H(T,X)=U(T,X^2)+X V(T,X^2),
deg U<=(2,2),       deg V<=(2,1).                   (2)
```

Substitute `(2)` into `(KBCO-1)` and compare the even and odd parts in
`X`. One obtains

```text
U(-T,W)=epsilon U(T,W),
V(-T,W)=-epsilon V(T,W).                            (3)
```

If `epsilon=+1`, the `T`-degree-at-most-two form `U` contains only its
constant and quadratic powers of `T`, while `V` contains only its linear
power. This is exactly `(KBCO-2)`. The two coefficients of `U` are
degree-at-most-two forms in `W`, contributing `3+3` parameters, and the
coefficient of `T` in `V` has degree at most one, contributing two. The
dimension is eight.

If `epsilon=-1`, `U` contains only its linear power of `T`, while `V`
contains its constant and quadratic powers. This gives `(KBCO-3)` with
dimension

```text
3+2+2=7.                                            (4)
```

The source deck sends `X` to `-X`, hence

```text
bH=U-XV.
```

It equals `H` projectively only when `V=0`: comparison of the even parts
fixes the scalar as one, after which the odd parts force `V=0`. The parent
source theorem says `H` and `bH` are distinct, giving the printed nonzero
conditions.

Finally the quadratic base-change factorization gives, after one endpoint
rescaling,

```text
G(T,W)=H(T,X)H(T,-X)=U(T,W)^2-WV(T,W)^2.            (5)
```

Equation `(3)` makes both squares in `(5)` even in `T`, for either sign.
This proves `(KBCO-4)`. The source-row compiler supplies uniqueness of a
reconstructed `H`, so failure of these identities is an exact packet
deletion rather than a coordinate-choice heuristic. QED.
