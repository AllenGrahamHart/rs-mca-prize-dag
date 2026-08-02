# KoalaBear positive 433-1a cell-5 signed-pair guard stable rank

- **status:** PROVED
- **scope:** deployed characteristic, generic `t`, cell 5, signs
  `(-1,-1)`, rational lift chart 2, squared `DE+/DE-` pair
- **consumer:** cell-5 signed-family component ledger

Let

```text
K = F_2130706433(t),
A = K[x1,x0,b]/<P,g3,h>,
g = d0*d1,
```

where `P(b,t)` is the proved reciprocal quartic, chart 2 supplies the
rational `r,c` lift, and

```text
g3 = n1*d0+n0*d1,
h  = q1^2*d0^2-q0^2*d1^2
     +4*Delta^2*n0*d0*d1^2.
```

Here `xj=zj^2`, and `dj,nj,qj` are the exact chart-substituted `D,N,Q`
evaluations from the signed-pair interface.  The hash-pinned exact
Groebner presentation gives

```text
dim_K A = 64.
```

If `M` denotes multiplication by `g` on `A`, then

```text
rank_K(M^2)=rank_K(M^3)=24.
```

Consequently every later rank is also 24 and

```text
dim_K A[g^-1] = 24.                              (KBGS-1)
```

This is a generic-function-field length theorem.  It does not assert that
the localized algebra is reduced or has 24 geometric components, classify
its residue fields, treat exceptional `t` fibers, lift `x0,x1` to guarded
source roots, impose source distinctness, append the colored `BE` edge,
cover the other three `c` charts or the `DF` family, delete cell 5 or
`433-1a -> O0b`, close K3, or prove either Prize result.

## Falsifier

An exact failure of the printed Groebner presentation, the matrix identity
for multiplication by `g^2`, the rank-24 factorization, the nonzero pivot
minor, or the localization/stable-image argument.
