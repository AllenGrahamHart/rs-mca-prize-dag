# Proof

## 1. The transpose kernel curve

At half distance the Hankel pencil has

```text
R-r=4m rows,       r+1=4m+1 columns,
generic rank rho=4m-1.                                (1)
```

Its generic left nullity is one. The two-sided minimal-index theorem says
that every singular block has index `e`, so the unique left singular block is
the transpose of `L_e`. Its homogeneous left-kernel vector has `e+1`
independent parameter coefficient vectors. Kronecker strict equivalence is
constant and invertible, so their images remain independent.

The minimal-index theorem identifies the one-dimensional rational left
kernel directly with the degree-`rho` primitive apolar generator `Q`: in the
left apolar degree `R-r-1=rho`, no shift is present. Primitive generators of
the same one-dimensional rational kernel differ only by a nonzero constant.
Thus the coefficient forms `Q_0,...,Q_e` are independent.

The coefficient flattening of `Q` has rank `e+1`, its maximum possible rank.
The map `(HSL4)` is therefore the degree-`e` Veronese embedding followed by a
projective linear isomorphism. Since `N>rho`, domain evaluation is injective
on degree-at-most-`rho` forms.

## 2. Slope slack and saturation

At a supported slope of rank loss `c_gamma`, the exceptional-root theorem
provides a degree-`rho-c_gamma` apolar factor dividing both `Q_gamma` and the
squarefree supported locator. Hence

```text
rho-c_gamma<=u_gamma<=rho.
```

The regular Kronecker determinant gives

```text
sum_gamma c_gamma<=delta=rho-3e.
```

This proves the first part of `(HSL6)` and

```text
I=T*rho-O.                                             (2)
```

Core-freeness `s=0` makes every parameter form `Q(U,V;x)` nonzero, so it has
at most `e` distinct finite roots. Counting by domain point gives

```text
I=sum_x d_x<=Ne.                                       (3)
```

Thus `T*rho<=Ne+delta`. With `N=4rho+4`,

```text
Ne+delta=(4e+1)rho+e.
```

Since `e<rho`, integrality proves `T<=4e+1`.

A failure of the half-distance cap has `T>=rho+3`. Therefore `(HSL7)` is
nonnegative and

```text
h<=4e+1-(rho+3)=4(e-m)-1,
```

which proves `(HSL8)`. The capacity identity follows from `(2)`:

```text
C=Ne-I=Ne-(4e+1-h)rho+O
 =4e-rho+h*rho+O.                                     (4)
```

Using `O<=rho-3e` gives `C<=e+h*rho`. Every nonsaturated row contributes at
least one to `C`, proving `(HSL10)`.

At most `delta` supported slopes lose rank. On every remaining supported
slope, `Q_gamma` has `rho` distinct domain roots. The generic degree-`r`
kernel consists of the two linear shifts of `Q_gamma`; a squarefree split
supported locator is therefore `Q_gamma` times one further domain factor not
already dividing it. This proves the clean-column assertion.

The rows and columns of `W` lie in the printed RS codes and are nonzero. In a
failing profile `T>=rho+3>e`; evaluation on `Z` is injective through degree
`e`. Together with coefficient independence and injective domain evaluation,
this gives `rank W=e+1`. Counting nonzero entries as the complement of the
`I` root incidences proves `(HSL12)`.

## 3. Sharp-cap norm and complementary factors

Assume `h=0`. Each root incidence at `gamma` contributes a factor
`L_gamma` to the domain norm. Distinct slope forms are coprime, so

```text
R=(product_gamma L_gamma^u_gamma)S.
```

Its residual degree is `Ne-I=C=4e-rho+O<=e`. Multiplication by `J` proves
`(HSL13)`.

There are at most `C` nonsaturated rows. On a saturated row the degree-`e`
form `Q(U,V;x)` has `e` distinct roots in `Z`, hence divides the squarefree
degree-`T=4e+1` form `H`. Set `V_x=H/Q(U,V;x)` and interpolate its homogeneous
parameter coefficients over `D_sat`. This produces `Vbar` of parameter degree
`3e+1` and `X`-degree less than `N-b`. The biform `Q Vbar-H` vanishes at all
roots of `P_sat`, so division gives `(HSL15)`. Parameter and `X` degrees give
the printed bounds on `Wbar`.

Outside the at most `delta` rank-drop slopes and the at most `C` roots of
`S`, the norm order at a supported slope is exactly `rho`, supplied by its
`rho` distinct root columns. All those incidences are transverse. Their count
is at least

```text
T-delta-C=3e+1-O.
```

This proves `(HSL13)--(HSL15)`.

## 4. Component-degree chambers

Factor `Q` over the algebraic closure, with multiplicity. A parameter-degree-
zero component would be a fixed domain factor at a clean split slope,
contradicting `s=0`; an `X`-degree-zero component would contradict
primitivity. Thus `r_i,e_i>0`.

For each component, grid-line Bezout gives

```text
I_i<=T*r_i,       I_i<=N*e_i.
```

The resulting deficits are nonnegative. Accounting for component overlaps
by `E=sum_i I_i-I` and using `C=g+O` proves `(HSL17)`, and hence

```text
0<=D_i<=O-E<=delta=e-g,
0<=C_i<=g+O-E<=e.                                     (5)
```

For `a_i=4e_i-r_i`,

```text
C_i-D_i=N*e_i-T*r_i=T*a_i-4g*e_i.                    (6)
```

If `a_i<0`, then `(6)` gives `D_i-C_i>=T>e-g`, contrary to `(5)`.
Therefore `a_i>=0`, and summing gives `sum_i a_i=4e-rho=g`. Bounds `(5),(6)`
are exactly `(HSL18)`. Their interval has width `(2e-g)/T<1/2`, proving the
unique chamber assertion.

Finally set `e=m+1`. Equation `(HSL8)` gives `h<=3`; substituting its worst
value in `(HSL10)` gives

```text
N-(m+1)-3(4m-1)=3m+2.
```

Also `delta=m-4` and `T>=rho+3=4m+2`, so

```text
T-delta>=3m+6.
```

This proves `(HSL19)` and completes the proof. QED.
