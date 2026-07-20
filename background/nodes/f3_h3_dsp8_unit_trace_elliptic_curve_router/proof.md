# Proof

The unit-product normal form gives `ruv=1` and `r+u+v=sigma`. Eliminating
`v` gives `(EC1)`. Multiplication by `ru` and homogenization give `(EC2)`.

Write

```text
F=X^2Y+XY^2-sigma XYZ+Z^3.
```

Its partial derivatives are

```text
F_X=Y(2X+Y-sigma Z),
F_Y=X(X+2Y-sigma Z),
F_Z=-sigma XY+3Z^2.                                  (1)
```

On `Z=0`, the cubic has the three points
`[1:0:0]`, `[0:1:0]`, and `[1:-1:0]`. Substitution in `(1)` shows that none
is singular. In the affine chart `Z=1`, the equation has no point with
`X=0` or `Y=0`. At a singular point both coordinates are therefore nonzero,
and the first two equations in `(1)` give

```text
2X+Y=sigma,       X+2Y=sigma.
```

Since the characteristic is not `3`, this forces

```text
X=Y=sigma/3.                                         (2)
```

Substitution in `F=F_Z=0` is equivalent to `sigma^3=27`. Hence the curve is
smooth exactly when `sigma^3!=27`. A smooth plane cubic is geometrically
irreducible of genus one.

If `sigma=3c` with `c^3=1`, scale `X=c(1+xi)`, `Y=c(1+eta)`. The terms of
degree two at the point `(c,c)` are

```text
xi^2+xi eta+eta^2.                                   (3)
```

Its discriminant is `-3`, which is nonzero in the stated characteristics,
so `(2)` is an ordinary node. The preceding derivative calculation proves
that it is the only singularity. A plane cubic with one ordinary node has
geometric genus zero, proving the geometric assertions.

It remains to check the counting ledger. One decorated normalized triple
`{r,u,v}` with distinguished root `r` gives two points `(r,u)` and `(r,v)`
on `C_sigma`; these are distinct on the small-generic DSP8 locus. The second
decorated triple independently gives `(s,x)` or `(s,y)`. Thus every decorated
ordered primitive-SP/quotient record counted by `K_25^c` has exactly four raw
presentations `(EC3)`. Conversely, a raw tuple reconstructs both completed
triples, their distinguished roots, the forced scale `q=rs`, target `(EC4)`,
and quotient record, so forgetting the two internal choices recovers one
`K_25^c` record. This proves the first equality in `(EC5)`.

The primitive-SP adapter already proves `J_25^c=4K_25^c`, giving the second
equality. Substitution in the existing DSP8 inequality gives `(EC6)`. QED.
