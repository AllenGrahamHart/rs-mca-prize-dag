# f_sparse_rank_split

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/xr_syzygy_flat_transport.md']

## Statement

Split many-sparse flats by d_sp = dim span of their sparse dual words: (a) d_sp bounded => quotient by the sparse span reduces to the PROVED fixed-d lattice machinery + strip; (b) d_sp growing => abundance of independent sparse words, which splits by weight: abundant weight-2 => the inverse theorem f_weight2_inverse (conclusion FINITE by f_dih_subgroup_completeness); higher-weight accumulation => face-4 configuration machinery via the proved transport dictionary. Exhaustive by construction.

## Attack surface

leg (a) is a quotient argument over the proved fixed-d bound; leg (b) wiring is the two named children

## Falsifier

a growing-d_sp flat with neither weight-2 abundance nor higher-weight accumulation (definitionally excluded — the split is exhaustive; the falsifier tests the LEG proofs)
