# e22_dyadic_chain_mobius_accounting

- **status:** PROVED
- **closure:** proof

## Statement

Let the admissible dyadic quotient scales be a finite chain

```text
M_1 < M_2 < ... < M_r.
```

For each support class `R` with at least one admissible scale, let
`m(R)` be its unique minimal admissible scale, supplied by
`e22_minimal_scale_partition`.

Let:

- `A_j` be the raw number of classes counted by the scale-`M_j` staircase
  summand;
- `N_j` be the number of selected classes with `m(R)=M_j`;
- `O_{i,j}` for `i<j` be the number of classes with `m(R)=M_i` that are also
  counted by the raw scale-`M_j` summand, with the same declared multiplicity
  convention as `A_j`.

Then the accounting is triangular:

```text
A_j = N_j + sum_{i<j} O_{i,j}.
```

Consequently

```text
N_j = A_j - sum_{i<j} O_{i,j}.
```

Thus exact selected minimal-scale counts follow once the cross-scale overlap
counts `O_{i,j}` are known.

## Falsifier

A class counted at scale `M_j` whose minimal admissible scale is larger than
`M_j`, or a class whose minimal scale is not unique.
