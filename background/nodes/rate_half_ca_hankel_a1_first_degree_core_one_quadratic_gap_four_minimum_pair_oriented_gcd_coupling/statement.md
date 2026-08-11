# `A=1` quadratic minimum-pair oriented-gcd coupling

- **status:** PROVED
- **closure:** every `rho+3` pair has a linear-size center-owned row gcd
- **consumer:** `rate_half_band_crossing_location`

Retain pair union `rho+3` and the two oriented rank-two normal forms. If an
orientation starts at deficit `r_sigma`, its common gcd degree satisfies the
sharpened source-exclusion bound

```text
g>=max(1,ceil((r_sigma e-2)/(r_sigma+2))).           (OGC1)
```

Suppose both endpoint deficits vanish. Let `G_X,G_Y` be the common gcds for

```text
X=S_beta\S_alpha,       Y=S_alpha\S_beta.
```

Then they have the same degree `g` and there is a supported slope set `C`
of size `g-1` such that

```text
Z(G_X)=C union {beta},       Z(G_Y)=C union {alpha}. (OGC2)
```

After these gcds are removed, the three forward and three reverse row forms
have six pairwise-disjoint supported root sets. Hence

```text
g+1+6(e-g)<=3e+3,
g>=ceil((3e-2)/5).                                  (OGC3)
```

For the official `e=183251937963`, `(OGC3)` gives

```text
g>=109951162778.                                    (OGC4)
```

Combining `(OGC1)` and `(OGC3)`, every minimum pair in either quadratic arm
has an oriented center-owned common parameter divisor of linear degree:

```text
max(r_alpha,r_beta)=0:  g>=ceil((3e-2)/5),
max(r_alpha,r_beta)=1:  g>=ceil((e-2)/3),
max(r_alpha,r_beta)=2:  g>=ceil((e-1)/2).            (OGC5)
```

## Scope

The theorem does not exclude these large-gcd pencils. It does not identify
the gcd scheme beyond its supported simple roots or compare it with the
heavy-row cube factors.
