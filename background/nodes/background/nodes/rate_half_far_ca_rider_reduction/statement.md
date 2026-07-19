# Rate-half far-CA rider reduction

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`

Let `C` be a linear code of length `n`, let `a=n-r` with `r<n/2`, and fix a
received pair that is column-far at agreement `a`. Let `L_2(n-2r)` denote the
maximum number of codeword pairs agreeing with one received pair on at least
`n-2r` common coordinates. Then its CA-bad slope count is at most

```text
1+(r+1)L_2(n-2r).                                        (RR1)
```

Consequently

```text
B_ca^far(a)<=1+(r+1)L_2(n-2r).                           (RR2)
```

If there are at least two CA-bad slopes, both received components are within
`2r` coordinates of `C`; translating by a closest code pair reduces the CA
problem to a column-far pair whose two components are each `2r`-sparse.

At rate one half, `n=2k` and `a=k+tau`, so

```text
n-2r=2a-n=2tau.                                          (RR3)
```

Thus a sufficient far-CA safe condition at a proposed rate-half agreement is

```text
1+(r+1)L_2(2tau)<=floor(q/2^128).                        (RR4)
```

This is a lossless structural reduction followed by a possibly loose rider
count. It does not assert that `(RR4)` holds.
