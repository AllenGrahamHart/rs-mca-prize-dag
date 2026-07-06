# e1_folded_certificate_soundness

- **status:** PROVED
- **closure:** proof

## Statement

For 2-power `N'`, the folded short-vector certificate is sound for E1: if the
complete folded search over

```text
w in {-2,-1,0,1,2}^{N'/2}
```

finds no nonzero vector with

```text
sum_x w_x zeta^x = 0 mod p,
```

then every E1 collision is cyclotomic/antipodal and there is no non-quotient
exceptional collision at that row.

## Falsifier

A row with a non-quotient E1 collision despite a complete folded search
reporting no nonzero folded kernel vector.
