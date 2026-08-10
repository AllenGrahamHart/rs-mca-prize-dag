# Repeated-BC cell-3 outside-label quotient

- **status:** PROVED
- **scope:** the 105 missing-record/perfect-matching labels in a repeated-BC cell-3 outside system

Order the seven records as

```text
(BE, CF, DE+, DE-, DF+, DF-, EF).
```

The target involution `d -> -d` induces the record permutation

```text
(0,1,3,2,5,4,6).
```

Direct symbolic replay shows that this permutation preserves all seven
outside products and all seven squared sums. Transporting a missing record
and the perfect matching of the residual six records gives an involution of
the full `7*15=105` labels. Its orbit census is

```text
size 1:  9
size 2: 48
total:  57 orbits covering 105 labels.
```

The canonical orbit ledger has SHA256
`70c074ad010a7c8a03c84d6eaeb6206f14b941de455301180c9aa51a03f02b91`.

This does not exclude any orbit, close the route, K3, or either Prize result.

## Falsifier

A product or squared-sum mismatch under `d -> -d`, a non-involutive label
map, a missing or repeated label, or a different exact orbit census.
