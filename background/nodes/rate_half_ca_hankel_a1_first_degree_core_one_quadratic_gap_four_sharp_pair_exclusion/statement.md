# `A=1` quadratic gap-four sharp-pair exclusion

- **status:** PROVED
- **closure:** excludes pair union `rho+2` in both quadratic arms
- **consumer:** `rate_half_band_crossing_location`

Retain either core-one scalar quadratic packet at `u=4`, with exact actual
error supports `S_gamma`, deficits `r_gamma`, and

```text
rho=3e-1,       T=rho+4,       |S_gamma|=rho-r_gamma.
```

Then every two distinct supported slopes satisfy

```text
|S_alpha union S_beta|>=rho+3.                      (QSX1)
```

Consequently, if one projective codeword pencil contains the assigned
centers at a supported slope set `A` of size `h>=2`, then

```text
3h<=rho+3-sum_(gamma in A)r_gamma.                  (QSX2)
```

For every pair `alpha,beta`, at least

```text
ceil((2rho+9+r_alpha+r_beta)/3)                     (QSX3)
```

other supported slopes `gamma` satisfy

```text
|E_alpha union E_beta union E_gamma|>=2rho+1,       (QSX4)
```

where `E_gamma` is the full padded degree-`rho` locator root set. In
particular, `(QSX3)` is at least `2e+3`.

At the new minimum boundary `|S_alpha union S_beta|=rho+3`, the complete
coefficient-chain theorem gives residual row-form rank at most two on each
one-sided support difference. No rank-two fibre classification or packet
exclusion is claimed here.
