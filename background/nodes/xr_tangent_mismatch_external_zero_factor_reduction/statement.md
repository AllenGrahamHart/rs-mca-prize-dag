# Tangent-mismatch external-zero factor reduction

- **status:** PROVED
- **consumer:** `xr_tangent_support_mismatch_bridge`

Let `C=RS[F,D,K]`, let `A=K+h` with `h>=1`, and write

```text
u=c_0+e_0,       v=c_1+e_1,
T=supp(e_0,e_1).
```

Suppose slope `z` has an exact-`A` witness `(p_z,S)` and put

```text
q_z=p_z-(c_0+z c_1) != 0,
W=S\T,       d=|W|,       P_W(X)=product_(x in W)(X-x).
```

Then `d<=K-1`, `P_W` divides `q_z`, and `g_z=q_z/P_W` has degree below
`K-d`. On the punctured domain `T`, define

```text
b_i(x)=e_i(x)/P_W(x),       i=0,1.
```

The word `b_0+z b_1` agrees with `g_z` on `S intersect T`, a set of size
`A-d`. Hence every nonzero support mismatch enters a punctured GRS chart with

```text
dimension K-d,
agreement A-d,
excess (A-d)-(K-d)=h.
```

If `R=|T|-(K-d)`, the chart error radius is at most `R-h`. This is a
per-witness, fixed-chart reduction. It does not sum over `W` or prove a
first-match aggregate.
