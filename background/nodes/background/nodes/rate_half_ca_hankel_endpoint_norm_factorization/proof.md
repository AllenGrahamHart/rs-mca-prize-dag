# Proof

All parameter forms are homogeneous in `(U,V)`.  Each
`Q(U,V;x)` is nonzero of parameter degree exactly `m`, by the core-free
conclusion used in the endpoint-saturation theorem.

## 1. The norm has only a small power defect

Fix a supported slope `gamma`.  For each of the `u_gamma` distinct domain
roots `x` of `Q_gamma`, the linear parameter form `L_gamma` divides
`Q(U,V;x)`.  It follows that

```text
L_gamma^u_gamma divides R.
```

The forms belonging to distinct slopes are coprime.  Hence

```text
R=(product_gamma L_gamma^u_gamma) S                  (1)
```

for a homogeneous form `S`.  Its degree is determined exactly.  The endpoint
incidence identity gives

```text
sum_gamma u_gamma=T*rho-O
 =(4m+1)(4m-1)-O
 =16m^2-1-O.
```

Since `deg R=Nm=16m^2`, equation `(1)` yields

```text
deg S=1+O<=m.                                        (2)
```

Multiplying `(1)` by

```text
J=product_gamma L_gamma^(rho-u_gamma)
```

gives `J R=H^rho S`.  Moreover `deg J=O<=m-1`, proving `(ENF2)`.

No squarefreeness of the nonsaturated column forms is used: any repeated
supported root, root outside `Z`, or root at parameter infinity is retained in
the residual form `S`.

## 2. Complementary interpolation on saturated columns

The exact endpoint deficit is

```text
sum_(x in D)(m-d_x)=1+O.                              (3)
```

It is positive, so at least one column is nonsaturated.  Every nonsaturated
column contributes at least one to `(3)`, whence

```text
1<=b<=1+O<=m.
```

For `x in D_sat`, the degree-`m` form `Q(U,V;x)` has `m` distinct roots and
all of them belong to `Z`.  It therefore divides the squarefree degree-`T`
form `H`.  Define

```text
V_x(U,V)=H(U,V)/Q(U,V;x),       deg V_x=T-m=3m+1.
```

Interpolate each homogeneous coefficient of `V_x` as a polynomial in `x`
over the `N-b` distinct points of `D_sat`.  This produces a biform `Vbar` with

```text
deg_(U,V)Vbar=3m+1,       deg_X Vbar<N-b,
Vbar(U,V;x)=V_x(U,V)      for every x in D_sat.       (4)
```

Consequently `Q Vbar-H` vanishes identically as a parameter form at every
root of `P_sat`.  The distinct linear factors of `P_sat` are coprime, so
`P_sat` divides `Q Vbar-H` in `F[U,V,X]`.  Choose the sign of the quotient to
write

```text
Q Vbar+P_sat W=H.                                    (5)
```

The parameter degree of `W` is at most
`m+(3m+1)=4m+1`.  In the binary variable,

```text
deg_X(Q Vbar)<=rho+(N-b-1).
```

After division by the degree-`N-b` polynomial `P_sat`, this gives

```text
deg_X W<=rho-1=4m-2.
```

Finally `N-b>=16m-m=15m`.  This proves `(ENF3)` and `(ENF4)`.

## 3. Many fibers are completely clean

There are at most `deg S=1+O` supported slopes whose linear form divides `S`.
The exceptional-root theorem gives

```text
sum_gamma c_gamma<=delta=m-1,
```

so at most `m-1` supported slopes have positive rank loss.  Its pointwise
bound `o_gamma<=c_gamma` means that every omitted-root slope is already in the
rank-drop set; it must not be charged a second time.  The union of the
rank-drop and residual-multiplicity sets has size at most

```text
(m-1)+(1+O)=m+O.
```

Its complement in the `T=4m+1` supported slopes consequently has size at
least

```text
T-(m+O)=3m+1-O>=2m+2.                                 (6)
```

At a slope in this complement, `c_gamma=0`, so its Hankel rank is generic and
`o_gamma=0`; hence `Q_gamma` has `rho` distinct roots in `D`.  It is a nonzero
degree-`rho` form and is therefore squarefree and completely `D`-split.  Also
`L_gamma` does not divide `S`.  Equation `(1)` then gives

```text
ord_(L_gamma)R=u_gamma=rho.
```

The `rho` distinct root columns already contribute one order each, so every
one contributes exactly one.  All root incidences at this slope are
parameter-transverse.  This proves `(ENF5)`.

## 4. Exact product-code excess

Let

```text
M_(x,gamma)=Q_gamma(x),       x in D, gamma in Z.
```

The degree bounds in the two variables put `M` in

```text
RS[D,rho+1] tensor RS[Z,m+1].
```

No row is zero because `Q(U,V;x)` is nonzero of degree `m<T`.  No supported
column is zero because `Q_gamma` is a nonzero degree-`rho<N` form.  The number
of zero entries is the incidence count

```text
I=T*rho-O.
```

Hence

```text
wt(M)=NT-I=T(N-rho)+O.                                 (7)
```

The column code is MDS with minimum distance `N-rho`; equation `(7)` says
that the sum of all column excesses is exactly `O`.  On the other hand, the
row code has minimum distance `T-m`, and the exact column-capacity deficit
gives

```text
wt(M)=N(T-m)+sum_(x in D)(m-d_x)
     =N(T-m)+(1+O).                                    (8)
```

Equations `(7)` and `(8)` prove `(ENF6)`.  They are component-wise
near-equality statements.  The global minimum distance of the tensor product
allows zero rows or columns and is a different classification problem.  QED.
