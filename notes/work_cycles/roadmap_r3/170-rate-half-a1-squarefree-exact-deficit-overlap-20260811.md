# Cycle 170: rate-half `A=1` squarefree exact-deficit overlap (2026-08-11)

The unified squarefree theorem bounded the heavy-row center overlap by one.
The exact source partition removes that residual bookkeeping freedom:

```text
J=gcd(Lambda,g_*S_B^2)=gcd(Lambda,g_*),
j=deg J=d_A in {0,1}.
```

A correction center is already a padded-heavy center, and the center roots
of `g_*` are exactly the nonzero deficit indicators. Therefore the two
squarefree passing profiles are now

```text
d_A=0: R_lambda=c g_*S_B^2, c!=0;
d_A=1: R_lambda=(g_*S_B^2/ell_gamma)T_1,
       T_1!=0, deg T_1<=1, gcd(T_1,S_B)=1.
```

```text
result:                  PROVED exact overlap/deficit equality
DAG delta:               +1 PROVED leaf, 2 req edges
critical status delta:   none
compute:                 finite center-subset replay; no Modal spend
new assumptions:         none beyond squarefree unified setup
```

The next squarefree decision is no longer indexed by a free overlap degree;
it is exactly the pair of already classified endpoint-deficit profiles.
