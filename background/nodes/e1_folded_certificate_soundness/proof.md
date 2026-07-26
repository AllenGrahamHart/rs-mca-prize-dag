# proof: e1_folded_certificate_soundness

By `kernel_lattice_reframing`, an E1 collision at a row with `p = 1 mod N'`
is exactly a ternary vector

```text
v in {-1,0,1}^{N'}
```

with

```text
sum_x v_x zeta^x = 0 mod p,
```

modulo the already-known cyclotomic relations.

For 2-power `N'`, `zeta^{N'/2} = -1`. Pair opposite coordinates and define

```text
w_x = v_x - v_{x+N'/2},        0 <= x < N'/2.
```

Then

```text
sum_{x<N'/2} w_x zeta^x
  = sum_{x<N'} v_x zeta^x.
```

Each `w_x` lies in `{-2,-1,0,1,2}`. The folded vector is zero exactly for the
antipodal/cyclotomic relation `v_x = v_{x+N'/2}` at every opposite pair.

Therefore any non-cyclotomic E1 collision produces a nonzero folded vector
`w` in `{-2,...,2}^{N'/2}` with folded sum zero. A complete folded search that
finds no such nonzero `w` excludes every non-quotient E1 collision at that
row. This proves the soundness of the folded certificate.
