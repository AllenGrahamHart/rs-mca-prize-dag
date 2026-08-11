# Clean-endpoint marked-row split-Veronese dependency

- **status:** PROVED
- **closure:** exact marked-row elimination and source combination
- **consumer:** `rate_half_band_crossing_location`

Retain the four-Hankel frame and the marked domain point `x_0`. For
`x in D`, put

```text
v_x=(Q_0(x),...,Q_m(x))^T.                              (MSV1)
```

For each source `s in {0,1}`, subtract `x_0` times the unshifted frame from
the shifted frame. The marked term vanishes and gives

```text
sum_(x!=x_0) (x-x_0)omega_x^(s) v_x v_x^T=0.           (MSV2)
```

Let

```text
U={x in D\{x_0}:(omega_x^(0),omega_x^(1))!=(0,0)}.     (MSV3)
```

Column-farness of the source pair implies

```text
4m+1<=|U|<=16m-1.                                      (MSV4)
```

After scalar extension to the algebraic closure, there is a linear
combination of the two relations `(MSV2)` whose coefficient is nonzero at
every `x in U`. Hence there are `lambda_x!=0` such that

```text
sum_(x in U) lambda_x v_x v_x^T=0.                     (MSV5)
```

Equivalently, as a biform in two parameter variables,

```text
sum_(x in U) lambda_x Q(z;x)Q(w;x)=0.                  (MSV6)
```

Every `x in U` is saturated, so each `Q(z;x)` is a nonzero scalar multiple
of a squarefree degree-`m` locator whose roots are supported slopes. Thus
`(MSV5)` is a full-support dependence among the quadratic Veronese images of
at least `4m+1` fully split supported locators; neither the residual factor
`S` nor the deficient row remains in it.

## Scope

This is an exact reduction, not an independence theorem. The live clean
gate is to exclude `(MSV5)` using the supported-locator incidence, the
degree-`rho` interpolation of the vectors `v_x`, or both. Arbitrary split
degree-`m` polynomials are not claimed to have independent quadratic
Veronese images.
