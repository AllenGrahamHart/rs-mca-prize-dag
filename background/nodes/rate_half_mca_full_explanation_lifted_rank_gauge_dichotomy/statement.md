# Full-explanation lifted-rank gauge dichotomy

- **status:** PROVED
- **scope:** pair-noncontained MCA families whose selected explanations have
  full affine rank `K` in the shortened code

Fix an anchor slope and put

```text
U=span{c_gamma-c_0},
V=span{(gamma-gamma_0,c_gamma-c_0)} <= F direct_sum C.
```

Assume `dim U=K=dim C`.  Then exactly one of the following holds.

1. **Gauge-drop branch:** `dim V=K`.  There is a nonzero functional
   `ell:C->F` whose graph is `V`, and every `b in C` with `ell(b)=1`
   changes the selected explanations to affine rank exactly `K-1` under
   `c_gamma -> c_gamma-gamma b`.
2. **Full-lift branch:** `dim V=K+1`.  Then `V=F direct_sum C`, and every
   codeword gauge leaves explanation affine rank exactly `K`.

Pair noncontainment implies `r_1 notin C`.  Consequently the affine rank of
the selected error vectors `r_gamma-c_gamma` is exactly `dim V`: respectively
`K` or `K+1` in the two branches.

Combining the gauge-drop branch with the corrected occupancy compiler
improves the first top-rank high-support gates to

```text
KoalaBear:   e>=992852 in lifted rank 14;
Mersenne-31: e>=1037876 in lifted rank 6.
```

The full-lift branches retain the previous high-support gates.
