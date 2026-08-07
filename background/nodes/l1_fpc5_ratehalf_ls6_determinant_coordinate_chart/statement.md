# Rate-half FPC5 LS6 determinant coordinate chart

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t3_split_slice_payment`
- **upstream interface:** primitive shift-pair / split-pencil control

Fix one guarded LS6 atom and one candidate `(D_0,Q_0,V_0)`. Write

```text
M=L_2L_3,       j=2ell-a,       s=ell-a,
h=ell-2a,       D_0E=MQ_0+V_0,       gcd(D_0,Q_0)=1.
```

Let `A` be the complete monic unguarded LS6 slice: all monic degree-`j`
polynomials `D` for which

```text
DE=MQ+V,       deg V<=s.
```

Then

```text
Phi:A -> K[X]_{<=h},       Phi(D)=H_D=D_0Q-DQ_0                 (DC1)
```

is an affine bijection. If `I_0=Q_0^(-1) mod D_0`, its inverse is

```text
R_H=rem_(D_0)(-H I_0),       D_H=D_0+R_H,
Q_H=(H+D_HQ_0)/D_0,          V_H=(D_HV_0-MH)/D_0.              (DC2)
```

Both displayed divisions are exact, `D_H` is monic of degree `j`,
`deg Q_H=deg Q_0`, and `deg V_H<=s`.

For two coordinates `H,G`, their cross determinant is

```text
D_HQ_G-D_GQ_H=(D_HG-D_GH)/D_0,       deg<=h.                  (DC3)
```

Thus all formal three-or-more determinant and Plucker identities are already
satisfied by the entire unguarded affine slice. They impose no additional
maximum bound.

The guarded split atom has an exact root-local description in this chart.
Require `D_H|L_C`. For a root `x` of `D_H`, primitivity is equivalent to

```text
x notin Z(D_0):       H(x)!=0;
x in Z(D_0):          H'(x)+D_H'(x)Q_0(x)!=0.                 (DC4)
```

In particular, on the base root set,

```text
Z(D_H) intersect Z(D_0)=Z(H) intersect Z(D_0).                (DC5)
```

The live problem is therefore a split-root and owner-safe quotient/dihedral
census in the explicit `H` chart. Abstract collective determinant
compatibility is fenced.

## Scope

This theorem does not bound the number of `H` satisfying `(DC4)` and
`D_H|L_C`, prove prefix flatness, or pay any deployed LIST row.
