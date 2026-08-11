# Cycle 165: rate-half `A=1` separated correction is center-disjoint (2026-08-11)

The full three-center source identity sharpens Cycle 164. Every assigned
center error support is contained in

```text
supp(b_0,b_1)=U=S_alpha union S_beta,
```

while the fixed heavy point `x_*` is external to `U`. If any center were a
root of `S_B`, its specialized locator root `x_*` would therefore be padded,
putting the center in both `S_B` and `g_*`, contrary to separatedness. Hence

```text
gcd(S_B,Lambda)=1,
j=deg gcd(Lambda,g_*S_B^2)<=1.
```

```text
result:                  PROVED correction-center disjointness and j<=1
DAG delta:               +1 PROVED leaf, 7 req edges
critical status delta:   none
compute:                 tiny logical replay only; no Modal spend
new assumptions:         none beyond the separated extremal profile
```

Every correction root now has exact heavy-row order two. The remaining
overlap form is nonzero, correction-coprime, and constant or linear.
