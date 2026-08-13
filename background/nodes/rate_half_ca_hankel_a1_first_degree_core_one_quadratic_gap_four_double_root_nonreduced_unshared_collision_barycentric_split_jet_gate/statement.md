# `A=1` nonreduced collision barycentric split-jet gate

- **status:** PROVED
- **closure:** explicit classified-row formulas for the collision value and derivative jets
- **consumer:** `rate_half_band_crossing_location`

Retain an unshared nonreduced exact collision and the extremal paired
split-biform row set `X`. Write

```text
G(t,x)=lambda_x P_x(t)       (x in X),             (BSJ1)
```

where `P_x` is the monic polynomial on the distinct off-line supported
slopes incident with `x`. The actual biform determines the unique
projective full-support weld vector `lambda`.

The collision parameter `tau` is neither an assigned center nor an
off-line supported slope. In particular,

```text
P_x(tau)!=0       for every x in X.                (BSJ2)
```

Put

```text
L_X(Y)=product_(x in X)(Y-x),
b_x=L_X(x_*)/((x_*-x)L_X'(x)),
d_x=b_x[L_X'(x_*)/L_X(x_*)-1/(x_*-x)].            (BSJ3)
```

Then the complete outside value and derivative rows are

```text
R(t):=G(t,x_*)
     =sum_(x in X)b_x lambda_x P_x(t),

J(t):=G_X(t,x_*)
     =sum_(x in X)d_x lambda_x P_x(t).             (BSJ4)
```

Choose `z=t-tau` and let `P_x^[s](tau)` denote the `s`-th Hasse
coefficient. Define

```text
R_s=sum_x b_x lambda_x P_x^[s](tau),
J_s=sum_x d_x lambda_x P_x^[s](tau).               (BSJ5)
```

The collision imposes the exact value-row gate

```text
R_0=R_1=0,       R_2!=0.                           (BSJ6)
```

Its three regular Smith profiles are selected by the two derivative-row
tests

```text
J_0!=0:                    [4];
J_0=0, J_1!=0:             [1,3];
J_0=J_1=0:                 [2,2].                  (BSJ7)
```

## Scope

This is an exact finite linear-algebra gate on the realized row-root data
and weld vector. It does not prove that `(BSJ6)` or any line of `(BSJ7)`
is impossible.
