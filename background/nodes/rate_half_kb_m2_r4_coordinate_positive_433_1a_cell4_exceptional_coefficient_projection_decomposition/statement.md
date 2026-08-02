# KoalaBear positive 433-1a cell-4 exceptional coefficient projection

- **status:** PROVED
- **scope:** the `L=M=0` coefficient chart left by the main cell-4 signed-pair
  reconstruction over `F_2130706433`; source symmetry transports the reduction
  to cell `7`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_cell4_signed_pair_projection_reconstruction`
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient`
- **consumer:** `rate_half_band_closure`

Let `P(b,t)` be the common plane, `F(w0,b,t)` the live signed-pair projection,
and `L,M` the two primitive reconstruction coefficients.  For independent
parameters `s,u`, set

```text
R_(s,u)(w0,t)=Res_b(P,L+sM+uF).                 (KBC4EC-1)
```

The fifteen integer points `(s,u)` with `s,u>=0` and `s+u<=4` form a rank-15
evaluation set for all total-degree-at-most-four polynomials.  Exact FLINT
evaluation of `(KBC4EC-1)` at these points therefore detects whether it is
identically zero in `(s,u)`.  The common gcd of the fifteen resultants is

```text
U(t) H(w0,t)^2,                                 (KBC4EC-2)
```

where `H` is irreducible of bidegree `(8,12)` with `97` terms.  Every
base-field root of the univariate factor `U` is `t=+/-1` or `t=+/-i`; its two
remaining factors are irreducible cubics.  Thus `U=0` is excluded by the
original `t(1-t^2)(1+t^2)` guard over the deployed field.

After division by `(KBC4EC-2)`, the ideal of all fifteen primitive resultants
is zero-dimensional of degree `470`.  Its lexicographic `t` eliminant has
degree `105` and factors as

```text
t^13 (t+i)^4 C(t)^5 (t-i)^11 (t+1)^18 (t-1)^44, (KBC4EC-3)
```

where `C` is an irreducible cubic.  Hence the residual algebra has no
admissible deployed-field point.  Every admissible deployed exceptional
projection must therefore lie on `H(w0,t)=0`.

Modulo `H`, an exact pseudo-Euclidean chain produces a primitive linear
polynomial

```text
A(w0,t)b+B(w0,t),                               (KBC4EC-4)
```

of degrees `(7,1,688)` in `(w0,b,t)`.  The remainders of `P,L,M,F` by
`(KBC4EC-4)` are all exactly zero after coefficientwise reduction modulo `H`.
Thus `b=-B/A` is the generic lift of the surviving curve.  Zeros of the
quotient-leading scales or `A` remain exceptional and are not deleted here.

This node does not prove that every `H` point is a guarded signed-pair point,
classify the exceptional lift of `(KBC4EC-4)`, impose the colored `BE`
equations, exclude cell 4 or 7, or close the positive route, K3, LIST, MCA, or
either Prize problem.

## Falsifier

A singular evaluation matrix, failed factor reconstruction, an additional
deployed linear root in `(KBC4EC-2)` or `(KBC4EC-3)`, a nonzero quotient
remainder in `(KBC4EC-4)`, or treating the necessary `H` projection as a
sufficient solution curve.
