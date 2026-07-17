# Rate-half cyclic simple-pole MCA floor

- **status:** see `dag.json` (single source of truth)
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **object:** support-wise CA and MCA at the official rate-half cap row

Let

```text
n = 2^41,                 k = 2^40,
c = 2^22,                 d = 2,048,
sigma_max = dc+c-1
          = 8,594,128,895,
C = RS[F,D,k],
q = |F| < 2^256,
```

where `D` is a multiplicative coset of order `n`. Put

```text
N = 524,288,   d = 2,048,   m = 264,192,
B = C(524287,264192),
L_q = ceil(B/(N q^2047)).
```

Choose the residual prefix in the cyclic-rotation construction to have its
largest allowed size `s=c-1`. At radius

```text
delta_0 = 1 - (k+sigma_max)/n,
```

the proved cyclic-rotation construction supplies at least `L_q` distinct
words of `RS[F,D,k+1]` in one closed ball. The quantitative simple-pole
conversion gives

```text
epsilon_ca(C,delta), epsilon_mca(C,delta)
  >= E(q,L_q)
   = L_q(q-n)/(q(q-n+kL_q))
   > 2^-83
   > 2^-128                                             (SP1)
```

for every

```text
delta_0 <= delta < 1-k/n.
```

Equivalently, both CA and MCA are prize-unsafe at every agreement

```text
k+sigma,       1 <= sigma <= sigma_max.                  (SP2)
```

This is an exact list-to-distinct-slope conversion. It does not identify the
ordinary-list threshold with the MCA threshold, and it does not require the
stronger sufficient condition `L_q>(q-n)/k`.

In particular

```text
sigma*=8,592,912,738 < sigma_max,
```

so the previously conjectured safe point at `k+sigma*+1` is unsafe. The
fixed-point formulation of `rate_half_band_closure` is therefore refuted;
the remaining rate-half task must locate a later, field-dependent adjacent
crossing.
