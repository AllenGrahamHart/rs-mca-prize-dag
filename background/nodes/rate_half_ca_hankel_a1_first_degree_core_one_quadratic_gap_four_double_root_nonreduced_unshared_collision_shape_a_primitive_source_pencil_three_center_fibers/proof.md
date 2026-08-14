# Proof

The source numerator is

```text
B_src(t,X)=sum_(x in U_0)omega_x(t)L_U0(X)/(X-x). (1)
```

Every `omega_x` is parameter-linear, so `(PSP1)` holds. At a classified
point, interpolation gives

```text
B_src(t,x)=omega_x(t)L_U0'(x).                   (2)
```

The source partition has three distinct root classes. Thus the two
parameter coefficients of `B_src` cannot be proportional: otherwise all
nonzero forms in `(2)` would have the same parameter root. This proves
their independence.

Take the homogeneous gcd `H` and divide as in `(PSP2)`. The two remaining
domain forms are coprime homogeneous forms of common degree `D=R-1-h`.
They define the basepoint-free morphism `(PSP4)` of that degree.

Equation `(2)` is a nonzero parameter-linear form for every `x in U_0`.
Therefore no such point is a root of `H`, proving `gcd(H,L_U0)=1`. The
padded-center transversality theorem gives
`B_src(gamma_0,x_*)!=0`, so `H(x_*)!=0` as well.

At a center, the center Pade theorem gives

```text
B_src(gamma,X)=L_Mgamma(X)C_gamma(X).             (3)
```

Since `H` is coprime to `L_Mgamma`, equation `(3)` forces `H|C_gamma`.
Write `C_gamma=H Cbar_gamma`; division proves `(PSP6)`.

A nonzero fiber of a degree-`D` basepoint-free pencil has projective
degree exactly `D`. The class sizes are

```text
|M_alpha|=|M_beta|=n+2,
|M_(gamma_0)|=n+3.                               (4)
```

Subtract `(4)` from `D=R-1-h` and use

```text
R-1-(n+2)=d-1,       R-1-(n+3)=d-2              (5)
```

to obtain `(PSP7)`. Nonnegativity of the large residual degree gives
`h<=d-2`, completing `(PSP5)`.

For `x in M_gamma`, the source form `omega_x` vanishes at `gamma`, so
`(2)` gives `phi(x)=gamma`. For `x in M_delta`, `delta!=gamma`, its source
form is a nonzero multiple of the line cutting out `delta`, hence it is
nonzero at `gamma`. Thus no other classified point belongs to the
`gamma` fiber, proving `(PSP8)`. Equation `(PSP9)` is exactly the
nonvanishing `B_src(gamma_0,x_*)!=0` after removing the nonzero factor
`H(x_*)`.

Distinct fibers of a morphism are disjoint. Therefore the three
polynomials `B_prim(gamma,X)` are pairwise coprime. Equation `(PSP6)`
then makes the residuals `Cbar_gamma` pairwise coprime. Multiplying back
by the common factor `H` proves `(PSP10)`; no class-locator factor can
enter a pairwise gcd because `(PSP8)` excludes the other fiber there.

Finally, evaluation of `S_1(t)` at three distinct projective points has
rank two and a one-dimensional relation with every coefficient nonzero.
Apply that relation coefficientwise in `X` to the parameter-linear
polynomial `B_prim`. Substitution of `(PSP6)` gives `(PSP11)`. QED.
