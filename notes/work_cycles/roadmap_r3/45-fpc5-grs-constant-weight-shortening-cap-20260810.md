### 2026-08-10 FPC5 GRS constant-weight shortening cap

Every fixed FPC5 GRS syndrome shell now injects into a binary
constant-weight support code. If the shell endpoint is `H`, distinct locator
supports have distance at least `2(H-d)`. Complementing supports and fixing a
common `j`-subset gives an exact shortened Plotkin-Johnson cap

```text
floor { binom(N,j)/binom(w,j)
        floor((N-j)sigma/[x^2-(N-j)(x-sigma)]) },
```

where `w=min(d,N-d)`, `x=w-j`, and `sigma=H-d`; a residual weight below
`sigma` is singleton. The fixed-background incidence factor `binom(b,u)` is
retained.

This is a proved field-independent cap and a new route beyond the
adjacent-dimension Haboeck strip. It is not a uniform large-source payment:
the binomial ratio may remain exponential when the required shortening
depth grows.
