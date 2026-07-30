# Proof

## 1. Fiber resultants

Let `Gamma` be the bidegree-`(4,4)` endpoint component and `G(T,W)` an
irreducible defining form. The quadratic base change `W=psi(X)` has two
distinct components `H` and `bH`, each birational to `Gamma`. Comparing
bidegrees gives, up to a nonzero scalar,

```text
G(T,psi(X))=H(T,X) H(T,b(X)).                       (1)
```

Restricting (1) to the degree-two fiber divisor over `alpha_p` proves that
the right side of `(KBDI-1)` is projectively `G(T,alpha_p)`. At a
ramification point the two factors coincide, with multiplicity two. It is
nonzero because
`Gamma` has no vertical fiber. Each factor is a quadratic whose divisor is
the component star at that coordinate pole, so `R_p` is split and its two
factors obey the exact horizontal facets.

The diagonal stabilizer acts on `Gamma`. Irreducibility therefore gives a
constant eigenvalue `lambda` with

```text
G(tau(T),tau(W))=lambda G(T,W).                     (2)
```

In homogeneous coordinates, substitute `W=alpha_p` and use
`tau(alpha_p)=alpha_bar(p)`. Since `tau` is an involution, (2) gives
`(KBDI-2)` after projectivizing. Writing this as `tau^*R_p` retains the
homogenizing factor of the Möbius transformation.

This argument uses the product in (1). The induced automorphism of the
normalization of `H` need not preserve the subfield `K(X)`, so its two
points over one `X` value can map to different `X` values over the paired
`psi` fiber. No individual-star equivariance follows.

## 2. Facets and the global divisor

Corollary 9.27 gives root set `J` over every point above `K`, root set
`I` over both points above `eta in L minus K`, and the two printed
one-exchange facets over each label of `L^c`. Since `H` divides the
outgoing union, its quadratic stars lie in those sets. This proves the
three support bullets.

For each source label `alpha_i`, the row `H(alpha_i,X)` has degree four.
Consequently `alpha_i` occurs four times, counted with divisor
multiplicity, among all 24 quadratic stars. Multiplying (KBDI-1) over the
twelve quotient fibers therefore gives a degree-48 split divisor in which
every root of `A(T)` has multiplicity four. This is `(KBDI-3)`. The
argument includes ramified `psi` fibers because it is a divisor identity.

## 3. Exact interpolation equivalence

Choose the affine basis `1,T,...,T^4`. A biform of bidegree at most
`(4,4)` has a unique expression

```text
G(T,W)=sum_(a=0)^4 T^a g_a(W),       deg(g_a)<=4.   (3)
```

Suppose first that `G(T,alpha_p)=c_pR_p(T)` with every `c_p` nonzero.
For each `a`, the twelve-vector

```text
(c_p r_(p,a))_p
```

is the evaluation vector of `g_a`. It is therefore killed by `P`.
Stacking the five coefficient conditions is exactly `Mc=0`.

Conversely, let `c` be a full-support kernel vector of `M`. For each
`a`, the parity checks say that `(c_pr_(p,a))_p` belongs to the
degree-at-most-four evaluation code. Hence there is a unique polynomial
`g_a` of degree at most four taking those twelve values. Equation (3)
then satisfies

```text
G(T,alpha_p)=c_pR_p(T)
```

for every `p`. Uniqueness follows because twelve distinct evaluation
points determine every degree-at-most-four coefficient polynomial.

Thus a full-support kernel is equivalent to the claimed biform
interpolant. An actual diagonal component supplies one through (1), but a
passing interpolant must still satisfy irreducibility and the outer
self-correspondence factor identity. QED.
