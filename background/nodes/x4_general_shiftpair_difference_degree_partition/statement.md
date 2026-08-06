# General shift pairs partition by difference degree

- **status:** PROVED
- **closure:** proof

Let `D` be a finite evaluation set in a field, let `A>t>=0`, and let
`R` be any support-wise residual family of `A`-subsets of `D`.  Fix
`S0,S in R`, `S!=S0`, with the same first `t` sub-leading coefficients of
their monic locators.  Write

```text
C=S intersect S0,  P=S\C,  Q=S0\C,  e=|P|=|Q|,
H=L_P-L_Q,         d=deg H.
```

Then `H` is nonzero and

```text
0<=d<=e-t-1,       hence e>=t+d+1.                 (DD-1)
```

Moreover,

```text
d=0  iff  e_j(P)=e_j(Q) for every 1<=j<=e-1.       (DD-2)
```

Thus `d=0` is exactly the F-4 minimal, constant-shift stratum.  Every
nonminimal general order-`t` record has `d>=1` and `e>=t+2`; the top side
width `e=t+1` is necessarily minimal.

For any fixed first-owner residual graph, the local degree at `S0` therefore
has the disjoint exact partition

```text
deg_R(S0)=D_0(S0)+sum_(d>=1) D_d(S0),               (DD-3)
```

where `D_d(S0)` counts its incident records of locator-difference degree
`d`.  Restricting to primitive records, or deleting any support-wise paid
classes before forming `R`, preserves the same partition.
