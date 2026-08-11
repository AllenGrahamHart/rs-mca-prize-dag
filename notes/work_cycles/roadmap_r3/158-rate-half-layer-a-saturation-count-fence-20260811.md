# Cycle 158: rate-half Layer-A saturation-count fence (2026-08-11)

Canonical Round 35 proposed using the positive row surplus
`3m^2-5m` at saturated `W` as the mechanism behind sampled Layer-A full
rank. The bare promotion is false already at `m=2`.

Over any odd field containing `mu_32`, take thirteen points from `mu_16`,
nine slopes `mu_8 union {eta}`, and

```text
Q(Z,X)=Z^2-X^4.
```

Every point has exactly the two slopes `+/-x^2`. The resulting Layer-A
matrix has 26 rows and 24 columns, but

```text
ker E={A(X)Q(Z,X): deg A<=3},
rank E=20,       nullity E=4.
```

```text
result:                  FALSIFIED bare count-plus-saturation rank premise
DAG delta:               +1 PROVED route-fence leaf
critical status delta:   none
compute:                 exact F_97 replay only; no Modal spend
new assumptions:         none
```

This does not falsify the canonical endpoint statement because the example
does not realize `W=S_g union S_h` with both blocks of size seven or the full
split-biform/Hankel constraints. The corrected route must use those
hypotheses essentially; the incidence count by itself is retired.
