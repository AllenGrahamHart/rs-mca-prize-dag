# Exact MCA full-agreement endpoint

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`

Let `C` be a proper linear code in `F^D`, with `q=|F|` and `n=|D|`. Under the
finite-slope support-wise MCA convention, the exact bad-slope numerator at
full agreement is

```text
B_mca(n)=1.                                                (FA1)
```

Moreover `B_mca(a)>=1` at every agreement `1<=a<=n`. Consequently:

```text
q<2^128  =>  epsilon_mca(C,delta)>2^-128 at every radius,
q>=2^128 =>  epsilon_mca(C,0)=1/q<=2^-128.                (FA2)
```

Thus the grand threshold is zero below the field cutoff, while full agreement
is a certified safe endpoint at and above it.

For the official rate-half row in the nondegenerate field range, combining
`(FA1)` with the cyclic simple-pole lower bracket gives

```text
k+8,594,128,896 <= a_RH(q) <= n.                          (FA3)
```
