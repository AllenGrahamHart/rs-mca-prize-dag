# f_descent_termination

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: CONJECTURE]
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s3b_iii_3_fibers_and_noanchor.md#1']

## Statement

Iterating the weight-w descents (each drops degree >= w, dimension <= w-1; E9 observed w <= 3 suffices at toy scale) produces a descent tree of TOTAL size poly(n), with the spread/moment base at each leaf. Grounded by E9's census multiplicities. With this, F_r assembles for r = O(log n), and high dimension merges into the fiber machinery.

## Attack surface

DECOMPOSED by consumer family: MDS-dual flats trivial (f_termination_mds); Hankel-kernel flats via the coset-pattern lattice bound (f_termination_hankel — the open piece); the escaping sunflower-fiber family is priced by the PMA machinery, NOT by descent (no double-counting). The support-lattice reformulation (f_support_lattice) is what defuses the naive 2^depth danger.

## Falsifier

a toy flat whose descent tree branches super-poly (searchable at n = 16..32)
