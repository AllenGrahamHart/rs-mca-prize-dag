# Proof

At `u=4`, the quadratic normal-form theorem gives

```text
O=0,       I_H=e-6.                                  (1)
```

The omission number is a sum of nonnegative terms
`d-ubar_gamma`. Thus `O=0` makes every residual specialized locator
squarefree and split on exactly `d=rho-1` residual domain points. Adding the
fixed simple core root `s_0` proves `(ICS2)` and `deg_Z(s_0)=T`.

For the scalar residual degree `a=2`, the cancelled heavy factor has degree

```text
h=d-3-a=rho-6.                                       (2)
```

The residual domain has `N-1` points, so the light set has size

```text
|L|=(N-1)-h=3rho+5.                                  (3)
```

Every light row is parameter-saturated and therefore occurs in exactly `e`
supported locators. In the double-root packet, the unique heavy residual
root `x_*` carries all `I_H=e-6` heavy incidences. Every other heavy row has
none. Removing `x_*` from the `h=rho-6` heavy rows leaves `rho-7` inactive
rows. This proves `(ICS3)--(ICS5)`. The handshake check is

```text
T+(3rho+5)e+(e-6)=T rho,                              (4)
```

using `rho=3e-1` and `T=rho+4`.

The rate-half code has dimension `N/2=2rho`, hence minimum distance

```text
d_min=N-2rho+1=2rho+1.                               (5)
```

Two codewords cannot both lie within distance `rho` of the same received
word, proving the uniqueness in `(ICS6)`. The split-locator equivalence
constructs an error supported inside `E_gamma`, so

```text
supp(f_gamma-c_gamma) subset E_gamma.                 (6)
```

The double-root normal form says more. Every excess root is simple and new
relative to the specialized minimal locator, and all `C_tot=e-6` excess
degree occurs at the `e-6` incidences of `x_*`. Thus each slope in `Z_*`
has rank loss exactly one, every other supported slope has rank loss zero,
and `x_*` is the one padded root outside the minimal locator at those
deficient slopes. A split moment sequence with at most `rho` sources has
middle-Hankel rank equal to the number of its nonzero sources. Hence the
unique errors have the exact weights in `(ICS8)`.

We next prove the line cap. Suppose an affine codeword line `(ICS9)` contains
the assigned centers at `h` distinct supported slopes, `r` of them in
`Z_*`. Subtract it from the received pencil and put

```text
b(t)=f_0-c_0+t(f_1-c_1),
U=supp(f_0-c_0,f_1-c_1).                              (7)
```

Column-farness of the received pair gives `|U|>=rho+1`; otherwise the
codeword pair `(c_0,c_1)` would be within `rho` columns. At every coordinate
of `U`, the nonzero affine scalar `b(t)(x)` vanishes at at most one of the
`h` slopes. Therefore

```text
sum wt(b(gamma)) >=(h-1)|U|.                          (8)
```

By `(ICS8)`, the total weight at the `h` assigned centers is at most
`h rho-r`. Combining with `(8)` gives

```text
(h-1)(rho+1)<=h rho-r,
h<=rho+1-r.                                          (9)
```

Finally fix distinct supported slopes `alpha,beta`. Their assigned centers
determine one affine codeword line. If a third slope `gamma` has

```text
|E_alpha union E_beta union E_gamma|<=2rho,           (10)
```

then compare `c_gamma` with the value at `gamma` of the affine line through
`c_alpha,c_beta`. Their difference is a codeword. Using `(6)`, that
difference is supported inside the union in `(10)`. By `(5)` it is zero, so
`c_gamma` lies on the same line.

If the fixed pair contains `r_0=|{alpha,beta} intersect Z_*|` deficient
centers, then the line through it contains at least `r_0` deficient centers.
By `(9)` it contains at most `rho+1-r_0` assigned centers, whereas there are
`T=rho+4` supported slopes. At least `3+r_0` centers lie off it, and every
such slope violates `(10)`. This proves `(ICS11)--(ICS12)`. QED.
