# Attack

Start with the binding prize rate-`1/8` row (`N=256,ell=33,S<=66`). Do not
enumerate all class pairs.

1. Seek an explicit three-color invariant on classes. Candidate invariants
   must be checked against every feasible coefficient profile, not only
   `(3,4)` or `S=16`.
2. A uniform maximum low-mass collision degree of two is sufficient by greedy
   coloring. Bound neighbors of one fixed class through the folded kernel and
   norm-divisor structure.
3. Falsify first: seek a same-fiber `K_4`, then more general four-critical
   subgraphs, on cheap selected primes before attempting a universal proof.
4. Reuse the proved conductor and cofactor screens as edge filters, but keep
   class-pair multiplicity and row quantifiers explicit.
5. Only after the three-color row is resolved, lift the method to the five
   looser row-specific bounds.

Any computation is evidence unless its certificate covers the complete
printed row scope. Large searches belong in `notes/PRIZE_COMPUTE_REQUESTS.md`,
not on the local machine.
