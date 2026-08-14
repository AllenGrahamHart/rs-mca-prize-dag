# `A=1` shape-A Padé-parity quotient route fence

- **status:** PROVED
- **closure:** the common-kernel floor is the automatic locator-parity block
  plus one exact excess intersection
- **consumer:** `rate_half_band_crossing_location`

Retain Shape A. Write

```text
Qbar(z,X)=sum_(i=0)^e z^i Q_i(X),
U_Q=span{Q_0,...,Q_e} subset S_d,
d=R-n-2=2n+5.                                    (PPQ1)
```

In the source residue algebra `A=F[X]/(L_U0)`, retain

```text
B_src(z,X)=J(X)(z-varphi),
Lambda(z)=(z-alpha)(z-beta)(z-gamma_0),
E_3=W_X+varphi W_X+varphi^2W_X.                  (PPQ2)
```

Then the global Padé identity gives

```text
J Qbar(z,X)=q_varphi(z)G(z,X),
q_varphi(z)=Lambda(z)/(z-varphi) in A[z].         (PPQ3)
```

Consequently,

```text
dim U_Q=e+1,       J U_Q subset E_3.              (PPQ4)
```

For the nondegenerate residue pairing `tau(FH)`,

```text
S_n^perp=S_d.                                     (PPQ5)
```

The right radical of the common-kernel pairing

```text
(h,E) |-> tau(hE/J),       h in S_n, E in E_3,   (PPQ6)
```

is therefore exactly

```text
E_3 intersect J S_d.                              (PPQ7)
```

Define the nonnegative Padé-parity excess

```text
xi=dim(E_3 intersect J S_d)-(e+1)>=0.             (PPQ8)
```

Then the combined locator-interpolation map and its common kernel obey

```text
rank T=3r-(e+1)-xi=dim ker Phi-xi,
kappa=n+e+2-3r+xi.                                (PPQ9)
```

At the lower rank boundary `3r=n+5`, this specializes to

```text
rank T=r-xi,
kappa=e-3+xi>=e-3=183251937960.                   (PPQ10)
```

## Route ruling

The previously isolated `e-3` common-kernel floor is automatic Padé/RS
parity, not an owner-sensitive alignment to be ruled out by ambient
dimension. In particular, the normal form itself can never prove
`kappa<=e-4`. A boundary exclusion must import an independent Shape-A
condition that contradicts the Padé quotient, rather than continue with a
dimension-only common-kernel estimate. The excess `xi` measures additional
right-radical rows beyond the mandatory locator coefficient block; neither
`xi=0` nor `xi>0` alone excludes Shape A.
