# Proof

Put `R=N-k=8m`.  At the first strict endpoint,

```text
r=rho=4m-1.
```

The Hankel pencil therefore has

```text
R-r=4m+1 rows,       r+1=4m columns,
generic rank rho=4m-1.                                 (1)
```

Its generic right nullity is one and its generic left nullity is two.

## 1. The unique right singular block

The two-sided minimal-index theorem proves that every right and left
minimal index equals the parameter degree `e` of the primitive apolar
generator.  Here endpoint reduction has `e=m`.  Since the right nullity in
`(1)` is one, the Kronecker form of the pencil has exactly one right
singular block, namely `L_m`.  (There are also two left blocks and a regular
part, but they do not affect the right kernel.)

The homogeneous right kernel of the canonical block `L_m(U,V)` is generated,
up to harmless signs and reversal, by

```text
(U^m,U^(m-1)V,...,UV^(m-1),V^m)^T.                    (2)
```

Its `m+1` parameter coefficient vectors are the standard basis of the
`m+1` columns occupied by the block.  Kronecker strict equivalence acts on
the full column space by a constant invertible matrix over `F`.  Embedding
the vectors in `(2)` into the `4m` columns and applying that matrix therefore
leaves their `m+1` coefficient vectors linearly independent.

The primitive right-kernel generator is unique up to a nonzero scalar: the
rational right kernel is one-dimensional, and two primitive homogeneous
minimal generators of the same degree cannot differ by a nonconstant
rational function.  Its coefficient vector is the coefficient vector of
`Q(U,V;X)` in the degree-`r=rho` monomial basis in `X`.  Hence the vectors
just proved independent are precisely the coefficient vectors of

```text
Q_0(X),...,Q_m(X).                                     (3)
```

This proves `(RNC2)`.

## 2. Separation rank and the kernel curve

For a biform, separation rank across the `X | (U,V)` split is the rank of
either coefficient flattening.  Equation `(3)` makes that rank `m+1`; the
parameter degree gives the matching upper bound.  Thus the separation rank
is exactly `m+1`.

The monomials in `(2)` form the complete basis of
`H^0(P^1,O(m))`.  Replacing their target coefficient vectors by the
independent vectors `(3)` is a projective linear isomorphism onto
`P(span{Q_0,...,Q_m})`.  Hence `(RNC3)` is the degree-`m` Veronese embedding
followed by a projective linear isomorphism: it is a rational normal curve.
This argument uses monomials rather than binomially normalized sections and
is valid in every characteristic.

If a form of degree at most `rho` vanishes at every point of `D`, it has at
least `N>rho` roots and is zero.  Domain evaluation is therefore injective
on the coefficient span, proving the evaluation-space assertion.

## 3. Endpoint hyperplane sections

The endpoint has no fixed domain factor.  Thus evaluation at every `x in D`
is a nonzero linear functional on `span{Q_j}`, and `H_x` is a genuine
hyperplane.  Pulling it back along `nu_Q` gives

```text
Q(U,V;x)=0,                                             (4)
```

a homogeneous form of degree `m` in the parameter.

Component-defect localization proves that at least `3m+2` supported slope
fibers split all components completely and disjointly over `D`.  At each of
those parameters, `Q_gamma` is squarefree of degree `rho` and lies in the
`rho` distinct evaluation hyperplanes indexed by its roots.

The same theorem gives at least `15m` saturated domain fibers.  For each
such `x`, `(4)` has all `m` of its roots, distinctly, in the supported set;
these are exactly the points of the hyperplane section of the rational
normal curve.  Finally, its transverse-fiber count says that at least
`3m+1-O` of the split supported parameters are simple roots in each of their
domain sections.  These are the asserted incidence and transversality
statements.  QED.
