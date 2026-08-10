# L1 FPC5 official-rate prefilter scale gap

- **status:** PROVED
- **consumer:** `l1_fpc5_large_source_payment`

Let an official row have

```text
n=2^s,       13<=s<=44,       k=n/R,
R in {4,8,16},       N=k-1.
```

For source scale `M`, write

```text
(R-1)k+1=M ell+b,       0<=b<ell.
```

Then the exact residual `(PF6)` of
`l1_fpc5_large_source_exact_prefilter` is empty throughout

```text
R=4:       5<=M<=12,
R=8:       7<=M<=28,
R=16:     15<=M<=56.                                  (SG1)
```

Consequently the unresolved large-source scales narrow from

```text
rate 1/2:   M>=5,       rate 1/4:   M>=5,
rate 1/8:   M>=7,       rate 1/16:  M>=15
```

to

```text
rate 1/2:   M>=5,       rate 1/4:   M>=13,
rate 1/8:   M>=29,      rate 1/16:  M>=57.             (SG2)
```

The three new endpoints are sharp for this arithmetic prefilter. At the
smallest official length `n=8192`, `(PF6)` has the following parameter
survivors:

```text
R   M   t   ell   b    d    r=2d-tell   u=d-(t-1)ell
4  13   3    472   9   911       406             -33
8  29   3    247   6   486       231              -8
16 57   3    134  43   278       154              10
```

These tuples are not asserted to be realized FPC5 contributors. They prove
only that `(SG1)` cannot be extended by one scale using `(PF6)` alone. The
rate-half range is unchanged for the same reason: `(PF6)` already has
parameter survivors at `M=5`.
