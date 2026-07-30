# Proof

## 1. The quadratic intermediate field

Let `Gamma` be the normalization of the actual endpoint component and
write `E=K(Gamma)`. The diagonal fiber compiler supplies an actual
bidegree-`(2,4)` source component `H(T,X)=0` which maps birationally to
`Gamma` under

```text
(T,X) -> (T,psi(X)).                                (1)
```

Consequently `K(X)` is a subfield of `E`, and the two projection degrees
give `(KBDS-1)`. All quadratic extensions here are separable because the
challenge characteristic is odd.

The diagonal stabilizer lifts to an involution `sigma` of `E` satisfying

```text
sigma(T)=tau(T),       sigma(W)=tau(W).              (2)
```

Although `sigma` need not fix `F=K(W)` pointwise, it preserves `F` as a
field. Therefore

```text
K_1=sigma(K(X))
```

is another degree-two intermediate field between `F` and `E`.

## 2. The source-line branch

Suppose `K_1=K(X)`. An automorphism of the rational function field is
projective, so the restriction of `sigma` is some `s in PGL_2`. Equations
`(1)--(2)` give

```text
psi(sX)=tau(psi(X)).                                 (3)
```

Also `s^2=1`. Conjugation by `s` preserves the fixed field `F` of the deck
involution `b`. It must preserve the unique nontrivial automorphism of the
quadratic extension `K(X)/F`, so `sbs^(-1)=b`. The two involutions are
distinct, since `s=b` would make the left side of `(3)` equal to `psi(X)`.
This proves `(KBDS-2)`.

The automorphism `sigma` acts on the source model as

```text
(T,X) -> (tau(T),s(X)).                              (4)
```

It preserves the irreducible source component. Thus an irreducible
bihomogeneous equation is an eigenvector for `(4)`. Applying `(4)` to a
fiber proves `(KBDS-3)`; unlike the whole-fiber identity in the parent
compiler, this individual-star identity is asserted only after the
intermediate field has been proved invariant.

Over the geometric closure, normalize `b(X)=-X`. A distinct involution
commuting with `b` must exchange zero and infinity, so after scaling `X`
it is `s(X)=1/X`. Taking the quotient coordinate `W=X^2` makes the induced
involution `tau(W)=1/W`. The two endpoint coordinates use the same
projective line, so the same normalization gives `tau(T)=1/T`. This proves
`(KBDS-4)`.

For a bidegree-`(2,4)` form, pullback by reciprocal inversion is represented
in the affine chart by

```text
H(T,X) -> T^2 X^4 H(1/T,1/X).                       (5)
```

This linear operation squares to one. Hence its eigenvalue is `+1` or
`-1`, proving `(KBDS-5)`. On the fifteen coefficient positions
`(i,j)`, `0<=i<=2`, `0<=j<=4`, it sends

```text
(i,j) -> (2-i,4-j).
```

There are seven two-element orbits and the fixed center `(1,2)`, so the
two eigenspace dimensions are eight and seven.

## 3. The biquadratic branch

Suppose `K_1!=K(X)`. Two distinct separable quadratic extensions of `F`
inside the degree-four field `E` have compositum of degree four. Their
compositum is therefore all of `E`, and the compositum of two quadratic
Galois extensions is biquadratic. Thus

```text
Gal(E/F)=<eta,eta'>=V4,                              (6)
```

where `eta` fixes `K(X)` and
`eta'=sigma eta sigma^(-1)` fixes `K_1`. The conjugation formula is valid
even though `sigma` acts nontrivially on `F`: the conjugate still fixes
every element of `F`. The two involutions are distinct, and their product
`mu` is the third nontrivial deck transformation.

Let `g` be the genus of `Gamma`, and write `n_u` for the number of fixed
points of a nontrivial `u in V4`. Both quotients by `eta` and `eta'` are
rational, because their function fields are `K(X)` and its `sigma`-image.
Riemann--Hurwitz for either quadratic quotient gives

```text
n_eta=n_eta'=2g+2.                                  (7)
```

The full quotient has function field `F`, hence genus zero. Tameness makes
every point stabilizer cyclic, so the fixed sets of the three involutions
are disjoint. Riemann--Hurwitz for the degree-four quotient gives

```text
n_eta+n_eta'+n_mu=2g+6.                             (8)
```

Substituting `(7)` into `(8)` yields

```text
n_mu=2-2g.                                          (9)
```

Nonnegativity forces `g=0` or `g=1`, proving `(KBDS-6)`. If `g=0`, each
of the three involutions has two fixed points, one `V4` orbit, so the base
has one branch value of each inertia type. If `g=1`, `eta` and `eta'`
each have four fixed points, or two base orbits, while `mu` has none. This
is exactly `(KBDS-7)`. QED.
