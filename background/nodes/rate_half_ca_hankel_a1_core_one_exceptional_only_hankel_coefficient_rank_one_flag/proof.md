# Proof

The bi-isotropic theorem proves `v` is not in `W_q`, so `(HRF2)` holds. The
kernel-plane theorem gives `v in ker M_0`; together with the total
`M_0`-isotropy of `W_q`, this proves the first identity in `(HRF4)`.

For `0<=i<e`, pair the coefficient recurrence

```text
M_0q_(i+1)+M_1q_i=0
```

with `v`. Since `v in ker M_0`, this gives `v^TM_1q_i=0`. The top relation
`M_1q_e=0` gives the same result for `i=e`. Hence `v` is `M_1`-orthogonal to
all of `W_q`. The plane itself is `M_1`-isotropic, while transversality gives
`v^TM_1v!=0`. This proves the remaining assertions in `(HRF4)`.

It remains to identify the orthogonal complements. For either `s=0,1`, the
radical of `M_s` meets `W_q` in exactly one dimension by the bi-isotropic
endpoint intersections. Therefore the map

```text
ambient coefficient space -> W_q^*,       x |-> (w |-> x^TM_sw)
```

has rank `dim W_q-1=e`. Its kernel
`W_q^(perp M_s)` has dimension `(2e+2)-e=e+2`. The preceding calculations
show that `H_q` lies in both kernels, and `(HRF2)` gives the same dimension.
Thus both kernels equal `H_q`, proving `(HRF3)`. QED.
