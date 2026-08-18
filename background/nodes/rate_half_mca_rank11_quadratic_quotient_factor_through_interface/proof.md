# Proof

At least 4,370 distinct split fibers occur. Since their locators are pairwise
disjoint and nonempty, at least two are distinct. Equation `(SPI11)` says each
locator is a nonzero scalar multiple of `u+gamma v`. Hence `u,v` are linearly
independent and their span equals the two-dimensional locator pencil.

In the antipodal case, the quotient identification writes every locator as

```text
X^2-y.
```

Two distinct values of `y` span `<X^2,1>`, so

```text
span{u,v}=span{X^2,1}.                               (1)
```

The ordered basis `(u,v)` differs from `(X^2,1)` by an invertible base-field
matrix. Therefore `-u/v` is a base-field fractional linear transform of
`X^2`: there is `M in PGL_2(F)` with `f(X)=M(X^2)`.

In the constant-product case, every locator has the form

```text
X^2-sX+kappa=(X^2+kappa)-sX.
```

Distinct nonfixed orbits have distinct sums `s`, so two locators span

```text
span{u,v}=span{X^2+kappa,X}.                         (2)
```

Again the basis change is invertible. On the projective line,

```text
(X^2+kappa)/X=X+kappa/X,
```

so `f(X)=M(X+kappa/X)` for a base-field Mobius map `M`.

The two quotient maps are invariant under `X -> -X` and
`X -> kappa/X`, respectively. Conversely, their nonfixed fibers are exactly
the locator pairs identified by the parent node. Finally, roots of
`u+gamma v` are precisely points where the projective value of `f` is
`gamma`; the affine scalar in `(SPI11)` changes no root. Hence `(QF1)` is the
actual slope map of the rational certificate, not only an abstract
classification of root pairs. No owner count follows from factorization
alone. QED.
