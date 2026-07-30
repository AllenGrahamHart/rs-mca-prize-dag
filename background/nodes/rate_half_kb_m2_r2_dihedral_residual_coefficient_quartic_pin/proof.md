# Proof

Let `u` and `v` be the deck involutions of the `Y` and `Z` projections on
the rational outer normalization `C`. Define

```text
Phi_K:C -> P1 x P1,       p -> (Y(p),Y(vp)).        (1)
```

Precomposition by `v` swaps the two coordinates, so the image `K` is
symmetric. If `(1)` were generically two-to-one, `Y(vp)` would be a
projective function of `Y(p)`. Then `v` would preserve the fibers of `Y`
and normalize `<u>`. Two involutions with this property generate at most
the commuting `D_2` case, contrary to `n=3` or `6`. Hence `(1)` is
birational. Its two projections have degree two, so `K` has bidegree
`(2,2)`.

Over the geometric closure, choose endpoint coordinates in which the
degree-two inner map is

```text
h(t)=t^2,       tau(t)=-t.                          (2)
```

A symmetric affine bidegree-`(2,2)` equation is a linear combination of

```text
y_0^2 y_1^2, y_0 y_1(y_0+y_1), y_0^2+y_1^2,
y_0 y_1, y_0+y_1, 1.
```

Putting `sigma=y_0+y_1` and `pi=y_0y_1` gives the polynomial `k` in the
statement.

Fix a generic source parameter `X`, and let `t,s` be the two roots of
`H(T,X)`. The map from the source component to the endpoint component fixes
the second endpoint coordinate. Since the branch is transverse, the two
images `h(t),h(s)` are the two distinct `Y` values above that common `Z`
value. They are therefore siblings:

```text
k(h(t)+h(s),h(t)h(s))=0.                           (3)
```

With `S=t+s` and `P=ts`, equation `(2)` gives

```text
h(t)+h(s)=t^2+s^2=S^2-2P,
h(t)h(s)=t^2s^2=P^2.
```

Substitution in `(3)` proves that the entire coefficient image lies on
`Q(S,P)=0`. Expanding gives exactly the printed polynomial, of total degree
at most four.

The residual source theorem says that the coefficient image is an
irreducible plane quartic and that the map from the source-parameter line
to it is birational. If `Q` had degree below four, it could not contain this
image. If a degree-four `Q` were reducible, none of its components could be
the irreducible degree-four image. Consequently actual existence forces
`Q` itself to be that irreducible rational quartic. QED.
