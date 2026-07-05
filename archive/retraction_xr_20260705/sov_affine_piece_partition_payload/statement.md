# sov_affine_piece_partition_payload

- **status:** TARGET
- **closure:** proof

## Statement

For every official-shape row, every `h in (20,A]`, and every forced-root
higher-coefficient conditioning cell of anchored-core locators, provide a
partition into:

- affine pieces where `c(L)=[X^{h-1}]L` has nonzero linear part; and
- paid or norm-structured exceptional pieces whose total size is below the
  character-sum budget.

## Falsifier

A forced-root conditioning cell with no such partition, or with exceptional
mass above the character-sum budget.
