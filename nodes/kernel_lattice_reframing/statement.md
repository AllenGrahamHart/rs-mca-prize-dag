# kernel_lattice_reframing

- **status:** PROVABLE
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

Since p = 1 mod N', zeta lives in F_p and e1 is an F_p-linear functional on class indicators: a collision is EXACTLY a ternary vector (entries -1/0/1, support <= 2l') in the kernel lattice K_p = {v : sum v_x zeta^x = 0 mod p}, beyond the known cyclotomic relations. The entire per-prime certification crux is a sparse-short-vector question about one explicit rank-N' lattice. Gaussian-heuristic arithmetic independently reproduces the typicality prediction (~2^-50 expected hits at N'=128).

## Ledger (migrated notes)

converts the crux from additive-combinatorics existence into lattice technology: search = LLL/BKZ; certification = cone-restricted dual/transference bounds (honestly harder than plain lambda_1)
