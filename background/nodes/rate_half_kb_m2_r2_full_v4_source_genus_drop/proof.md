# Proof

## The source V4 cover

Let `L` be the function field of the normalization of the actual source
component `H_0`. Its bidegree `(2,4)` makes

```text
[L:K(X)]=2.
```

The characteristic is odd, so this extension is separable and has a unique
nontrivial involution `eta`. Its quotient is the source parameter line.

In the `(r,delta)=(2,4)` row, the component stabilizer is the full endpoint
V4. The preceding router proves that `a=tau x 1` lifts on `H_0` as

```text
(T,X)->(tau(T),b(X)),
```

where `b` is the deck involution of `psi`. Hence both `eta` and `a` fix
`W=psi(X)`. They commute because `a` preserves `K(X)` and must normalize
the unique nontrivial automorphism of `L/K(X)`. They are distinct, and

```text
[L:K(W)]=[L:K(X)][K(X):K(W)]=4.
```

Thus `<eta,a>` is the full V4 deck group of the degree-four map to the
`W`-line.

## The second endpoint involution

Let `c` be the lift of `1 x tau`. It fixes the function `T` and sends
`W` to `tau(W)`. It normalizes the deck group of the `W` map. Since the two
endpoint coordinate involutions commute, conjugation by `c` fixes `a`.
It must therefore send `eta` to `eta` or `eta*a`.

Suppose first that it fixes `eta`. Then `c` descends through
`Gamma/<eta>=P1_X` to a projective involution `j` satisfying

```text
psi(j(X))=tau(psi(X)).                              (KBMG-1)
```

The involution `j` is nontrivial. Since `c` fixes `T`, the unordered pair of
`T` roots of the binary quadratic defining `H_0` is the same at `X` and at
`j(X)`. Thus the coefficient map

```text
phi_H:P1_X -> P2
```

factors through `P1_X/<j>`. Its defining sections have degree four and no
common factor, so after a degree-two quotient its image has degree at most
two. This is precisely the line/conic coefficient-image branch already
excluded before the residual birational-quartic case. Therefore

```text
c eta c^(-1)=eta*a.                                (KBMG-2)
```

## Fixed-point count

Put `g=g(Gamma)` and write `n_s` for the number of fixed points of a
nontrivial deck involution `s` in `<eta,a>`. Tameness implies that a point
stabilizer is cyclic, so the fixed sets of the three nontrivial V4 elements
are disjoint. Riemann-Hurwitz for the V4 quotient to `P1_W` gives

```text
n_eta+n_a+n_(eta*a)=2g+6.                          (KBMG-3)
```

The degree-two quotient by `eta` is `P1_X`, so

```text
n_eta=2g+2.                                         (KBMG-4)
```

Equation `(KBMG-2)` makes `eta` and `eta*a` conjugate, hence
`n_(eta*a)=n_eta`. Substitution into `(KBMG-3)` yields

```text
n_a=2-2g.                                           (KBMG-5)
```

Since `n_a` is nonnegative, `g<=1`. The component is irreducible, so its
normalization has nonnegative genus. Therefore `g=0` or `1`, with fixed
counts two and zero respectively. QED.
