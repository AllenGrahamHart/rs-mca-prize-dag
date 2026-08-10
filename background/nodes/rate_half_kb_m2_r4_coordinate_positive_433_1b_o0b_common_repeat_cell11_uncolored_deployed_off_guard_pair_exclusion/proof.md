# Proof

Let `K=F_p(x)`, let `A/K` be the exact rank-four or rank-six source algebra,
and let `E/A` be the rank-four missing-endpoint algebra.  For one pair of the
three paired-product polynomials, form its Sylvester matrix over `E` and let
`R` be its division-free determinant.

The certificate computes

```text
N = Norm_(A/K)(Norm_(E/A)(R)) in F_p(x).
```

Both norms are exact small determinants: subset dynamic programming for the
quartic determinant and endpoint norm, followed by exact Gaussian
elimination over `F_p(x)` for the rank-four/rank-six source norm.  At the
generic witness `x=2`, the nested norm equals the determinant of the original
flattened `64`, `96`, or `144` dimensional Sylvester multiplication matrix.
This checks the compressed implementation against the parent certificate.

Away from registered guards every rational denominator is defined.  If the
numerator of `N` is nonzero at `x`, then `R` is a unit in the specialized
finite source/endpoint algebra, so the selected polynomial pair has no common
root.  Exact finite-field root extraction over all 720 cases gives:

```text
288 cases: no non-guard root
432 cases: 1,584 non-guard root occurrences
distinct deployed base values: 126
```

The hash-pinned manifest contains every occurrence without deduplication
across formal cases.  At each occurrence the certificate specializes all
three possible equation-pair Sylvester matrices.  At least one matrix has
nonzero determinant in all 1,584 cases.  Hence at least one pair is coprime,
so the three equations cannot have a common endpoint.  This covers every
deployed off-guard source value.  QED.
