# proof: dli_et_peak_mass_reduction

Let `theta_y in R/Z` be the normalized odd-evaluation sequence, and write

```text
S_m = sum_y exp(2 pi i m theta_y).
```

The Erdos-Turan inequality gives, for every interval `I` and every cutoff
`H >= 1`,

```text
|#{y : theta_y in I}/Y - |I||
  <= C/(H+1) + C sum_{1 <= m <= H} |S_m|/(mY).
```

Thus finite-frequency Weyl-sum bounds imply interval discrepancy at every
scale `|I| >= 1/H`, with an explicit error term controlled by the harmonic
sum of the normalized Weyl sums.

The Dirichlet kernel has only finitely many peak centers in each DLI factor.
For a truncation height `T`, decompose the neighborhood of each peak into
dyadic annuli

```text
2^{-r-1} < dist(theta, peak) <= 2^{-r}
```

down to the reciprocal scale used by the truncation. Each annulus is a union
of at most two intervals. Applying the Erdos-Turan interval bound to all
annuli gives the empirical mass of every peak annulus as its circle mass plus
the stated discrepancy error.

The truncated logarithmic loss is a bounded linear combination of the
indicator functions of these dyadic superlevel sets, via the standard
layer-cake identity

```text
min(F,T) = int_0^T 1_{F >= u} du.
```

Therefore the same annular interval bounds control the empirical average of
the truncated logarithmic loss. The residual mass below the smallest annulus
is exactly the peak-mass tail term, also controlled by the same interval
discrepancy estimate at the reciprocal truncation scale.

Summing over DLI factors, the assumed harmonic-range Weyl-sum bounds give the
advertised total error `sum_j eps_j=o(t)`. Hence the truncated-log
discrepancy and peak-mass tail bounds required by
`dli_truncated_log_transfer` follow deterministically.
