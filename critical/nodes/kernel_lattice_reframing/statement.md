# kernel_lattice_reframing

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

Since p = 1 mod N', zeta lives in F_p and e1 is an F_p-linear functional on class indicators: a collision is EXACTLY a ternary vector (entries -1/0/1, support <= 2l') in the kernel lattice K_p = {v : sum v_x zeta^x = 0 mod p}, beyond the known cyclotomic relations. The entire per-prime certification crux is a sparse-short-vector question about one explicit rank-N' lattice. Gaussian-heuristic arithmetic independently reproduces the typicality prediction (~2^-50 expected hits at N'=128).

## Ledger (migrated notes)

converts the crux from additive-combinatorics existence into lattice technology: search = LLL/BKZ; certification = cone-restricted dual/transference bounds (honestly harder than plain lambda_1) | PROVED 2026-07-04 by writing e1(B)-e1(B') as a sparse ternary kernel vector in F_p[zeta].

## Round-22 forced correction (2026-08-07, coordinator-applied, CATCH-1 of ge_floor_falsifier): the expected-hits figure is multiplicity-inflated by 54.3 bits

The banked "~2^-50 expected hits at N' = 128" (reproduced round-21
as 2^-47.1 = 3^128/2^250) counts the UNFOLDED ternary cube — the
multiplicity of one folded class counted as independent trials. The
number of distinct folded classes is 5^64 = 2^148.6, so the
EXISTENCE probability heuristic is 2^-101.4, not 2^-47.1. Same
defect class as round-21's collision catch (multiplicity as
distinctness), on the other side of the node: the correction makes
the emptiness claim SAFER. Exhaustive census at h = 8 shows even
the class heuristic OVER-predicts badness by 2-3 orders (measured
bad-prime density 0.069 vs heuristic 0.981 in the 2^16 window).
Source: notes/pilots_20260807/ge_floor_falsifier/ (stats.py,
d3_kernel.py; coordinator-replayed).
