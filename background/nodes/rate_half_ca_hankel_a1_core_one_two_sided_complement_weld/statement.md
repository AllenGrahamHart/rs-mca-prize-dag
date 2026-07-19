# `A=1` core-one two-sided complement weld

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_component_norm_localization`

Retain the official dominant component `Q_*=Q` from the core-one
componentwise norm theorem. Write its bidegree as

```text
(r,e_*)=(2e_*+1,e_*),       D_0=16m-1,       T=4e+1. (TSW1)
```

Let `D_* in {0,1}` be its total supported-slope root deficit and let `C_*` be
its residual-domain parameter deficit. Define:

```text
Z_cl = supported slopes where Q_gamma has all r roots in D\S,
P_cl = product_(gamma in Z_cl)L_gamma,
E_Z  = P/P_cl,                 deg E_Z=D_*;

D_sat = residual domain rows where Q(U,V;x) has all e_* roots in Z,
P_X   = product_(x in D_sat)(X-x),
B_X   = G_X/P_X,               G_X=product_(x in D\S)(X-x),
c=deg B_X<=C_*.                                      (TSW2)
```

There are biforms `V,W,A,B` with

```text
Q V+P_X W=P,                                          (TSW3)
Q A+P_cl B=G_X,                                       (TSW4)
```

and degree bounds

```text
deg_(U,V)V=T-e_*,       deg_X V<D_0-c,
deg_(U,V)W<=T,          deg_X W<=r-1,                 (TSW5)

deg_(U,V)A<T-D_*,       deg_X A=D_0-r,
deg_(U,V)B<=e_*-1,      deg_X B<=D_0.                 (TSW6)
```

The two complements are not independent. There is a biform `K` such that

```text
W B-B_X E_Z=Q K,                                      (TSW7)
V B+A E_Z=-P_X K,                                     (TSW8)
```

with

```text
deg_(U,V)K<=T-1,       deg_X K<=D_0-1.                (TSW9)
```

Thus the dominant component divides a difference of two products, one of
which is the separated low-defect form `B_X(X)E_Z(U,V)` with

```text
deg_X B_X<=e-5b-1+D_*,       deg_(U,V)E_Z<=1.          (TSW10)
```

Equations `(TSW7),(TSW8)` are the exact two-sided complement weld. They
reduce the remaining mixed-component problem to classifying this bounded
matrix factorization together with `adj M=lambda*q*q^T`. They do not by
themselves exclude the component or close the stratum.
