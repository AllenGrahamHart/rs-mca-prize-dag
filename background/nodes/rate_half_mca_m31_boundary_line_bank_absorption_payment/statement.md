# Mersenne boundary-line-bank absorption payment

- **status:** PROVED
- **scope:** Mersenne-31 full-lift supports `101157<=e<=124805`

Retain the pair-noncontained full-lift notation.  Put

```text
s=floor((e-K)/3),  H=e-s-1,  U=min(H,m),  c=K-1,
```

and fix `h0=65272`.  Let `P_h0(e)` be the independently truncated
Johnson/mean-centered prefix.  For `h0<h<=U`, define

```text
A_h=2h-e,
J_h=floor(e(A_h-c)/(A_h^2-e*c)).
```

Suppose `2h>e`, `A_h>c`, and `A_h^2>e*c` throughout.  Set

```text
G_e = 1_{H<m} + sum_(h=h0+1)^U J_h,
C_e = P_h0(e) + sum_(h=h0+1)^U (1-J_h).
```

There are `G_e` affine explanation-line slots `L_i` such that

```text
|Z| <= C_e + sum_i |L_i|.                         (LB1)
```

Consequently, if the family is unsafe for budget `B`, one slot has size at
least

```text
lambda_e=ceil((B-C_e+1)/G_e).                     (LB2)
```

Total-core packing and the existing core-absorption theorem then give the
printed low-list contradiction whenever their denominators are positive.

Exact replay at the official Mersenne row proves every support

```text
101157<=e<=124805.
```

At the endpoint,

```text
(P,C,G,lambda)=(1636955,1604577,34560,440),
core=65220,  low list cap=126,
bound=16706559,  slack=70656.
```

At adjacent `e=124806`, the same legal compiler gives `16831491`, exceeding
the budget by `54276`.  This is a method wall, not an unsafe certificate.
