# Proof - L1 Pade-remainder Jacobian and tangent dichotomy

## 1. Polynomiality and differential

Monic Euclidean division expresses the quotient and remainder coefficients as
polynomials in the coefficients of `L`, so the remainder map is an affine
polynomial map.  Vary `L` through `L+sD` and write the first-order quotient
and remainder variations as `dQ` and `dP`.  Differentiating

```text
U=LQ+P
```

at fixed `U` gives

```text
0=DQ+L dQ+dP.                                       (1)
```

Reducing modulo `L` and using `deg dP<a` yields

```text
dP=-(DQ mod L),
```

which is `(JT3)`.  Equivalently, if `DQ=LS+R` with `deg R<a`, then
`dQ=-S` and `dP=-R`; substitution in `(1)` verifies the lift before taking
the residue class.

## 2. Primitive full rank

The tangent space to monic degree-`a` polynomials consists of all `D` with
degree below `a`, naturally identified with `F[Z]/(L)`.  Under this
identification `(JT3)` is negative multiplication by the residue class of
`Q`.  This linear map is invertible exactly when `Q` is a unit modulo `L`,
equivalently when `gcd(L,Q)=1`.

Thus the full remainder differential has rank `a` on the coprime locus.  The
map in `(JT2)` is the composition with the coordinate projection from all
`a` remainder coefficients to the top `w`.  A coordinate projection after
an automorphism is surjective, so its rank is exactly `w`.  The Jacobian
criterion gives a smooth local complete intersection of codimension `w`.
Taking the contrapositive proves that every rank-deficient section point lies
on `(JT4)`.

## 3. Exact-shell dichotomy

Write `Omega=L M`.  The domain locator is squarefree, so `gcd(L,M)=1`.
Exactness is `gcd(Q,M)=1` by the all-cofactor Pade-section theorem.  If also
`gcd(Q,L)=1`, then `gcd(Q,Omega)=1`; this is the primitive transverse class.
Otherwise `D=gcd(Q,L)` is a canonical nonconstant factor, is coprime to `M`,
and all of its domain roots lie among the agreement roots of `L`.  These two
classes are disjoint and exhaustive, proving `(JT5)`.

## 4. Tangent sharpness

Let `H` be the eight roots of unity in `F_17`.  Choose four roots for `L` and
let `Q` be the product of the first two corresponding linear factors.  Then
`gcd(L,Q)=Q` has degree two and `Q` has no root in `H` outside `L`.  For any
constant `P`, `U=LQ+P` has this exact agreement set and `k=1`.

Because `L` is squarefree, evaluation on its four roots identifies
`F_17[Z]/(L)` with `F_17^4`.  Multiplication by `Q` is diagonal with two zero
and two nonzero entries, hence has rank two.  The high-remainder projection
has three rows, so its rank is at most two.  This proves that actual Jacobian
rank loss can occur on the tangent branch without refuting the exact-shell
statement.
