# Proof

Let `G_z(X)` be the monic external locator at slope `z`. The saturated design
gives

```text
product_(z external)G_z(X)=C(X)^e.                  (1)
```

The quotient descent pairs the roots of `G_z` under `tau`. A nonfixed orbit
contained in `C` contributes multiplicity two to the product of the descended
polynomials for each block containing both rows, and one for a block
containing exactly one. Across all blocks, each of its two rows occurs `e`
times, so its total quotient multiplicity is `2e`. An orbit meeting `C` in
one row contributes total multiplicity `e`. At a fixed point, ramification of
the quotient changes the square in the source coordinate into one linear
factor in `U`, so the same singleton count applies. Monic normalization and
`(1)` prove `(QEP3)`. Degree comparison proves `(QEP2)`.

Every `G_z` is squarefree. Therefore a nonfixed quotient root is double
exactly when both members of its orbit lie in the block, and otherwise is
simple. A fixed active root and a crossing orbit contribute a simple root.
This proves `(QEP4)` and the exact count

```text
sum_z s_z=e h+2 sum_O(e-d_O).                       (2)
```

It remains to bound the codegrees `d_O`. Write the orbit polynomial from the
norm descent as `E(U)` and its interpolation polynomial as `J(z;U)`. For an
outside orbit, `J(z;u)` is a nonzero polynomial of degree at most `e-1`:
its coefficients in the Lagrange basis are nonzero because all support
classes are disjoint and every `lambda_i` is nonzero.

On the antipodal branch,

```text
Q(z;x)-Q(z;-x)
 =z[B(x)-B(-x)]J(z;x^2),                            (3)
B(x)-B(-x)=2x(x^2+sigma_2).                         (4)
```

The two row polynomials agree identically only at the one possible quotient
coordinate `u=-sigma_2`. Otherwise a common external root would force
`J(z;u)=0` through `(3)`. But then either row value is
`Phi(z)E(u)!=0`, because an external slope is neither internal nor zero and
an outside orbit is disjoint from the roots of `A`. Thus nonidentical rows
have no common external root.

On the constant-product branch, put `u=x+c/x`. Division by the nonzero
values `A(x)` and `A(c/x)` gives

```text
Q(z;x)/A(x)-Q(z;c/x)/A(c/x)
 =z J(z;u)/E(u) [B(x)/x-B(c/x)/(c/x)],              (5)

B(x)/x-B(c/x)/(c/x)
 =(x-c/x)(u-sigma_1+sigma_3/c).                    (6)
```

Thus the only possible identical-row coordinate is
`u=sigma_1-sigma_3/c`. Away from it, a common external root in `(5)` would
again force `J(z;u)=0`, after which both normalized rows equal the nonzero
value `Phi(z)`. This is impossible. Hence every nonidentical orbit has
`d_O=0`. At the exceptional coordinate the normalized row polynomials are
identical and have the same `e` external roots, so `d_O=e`. This proves
`(QEP5)--(QEP6)`.

Let `epsilon` record whether that orbit lies in `C_2`. Substitution in `(2)`
and `2p+h=6e+3` gives

```text
sum_z s_z=e h+2e(p-epsilon)
             =e(6e+3-2epsilon).                    (7)
```

Each common block for the exceptional row pair contributes the unique double
root, so `sum_z d_z=epsilon e`; no other double root exists. This proves
`(QEP7)` and the factorwise classification. QED.
