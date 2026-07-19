# Audit - PMA sigma-one generic defect-four source obstruction

## Load-bearing checks

1. The field is valid: `q=65537^2` is a prime power and
   `65536 | q-1`.
2. The construction counts actual degree-`<k` codewords, not auxiliary
   supersets: `P=1+L_(C\D)W` has degree at most `k-1` and exact `D` is
   recoverable from `P`.
3. Exact six petal hits, exact defect four, and no background hit give exact
   total agreement `k+1`.
4. Pairwise-distinct rational values make every hit singleton; no full-petal
   payment applies in the constructed layout.
5. The first moment averages only over injective nonzero source labels, so
   every averaged word is a valid maximal source word.
6. The owner exclusions are support/source statements, not small-row
   heuristics: odd support size kills exact periodicity, balanced core geometry
   kills the dyadic owner, and the base-valued `{x,-x}` pair kills odd lift.
7. The proof uses the complete Top/Post total. It does not assume that the
   constructed layout is first or that a codeword remains diffuse in every
   other layout.

## Numerical evidence

The independent Modal census in
`experiments/prize_resolution/modal_pma_d4r0_census.py` enumerates exact
degree-four candidates at `n=16,24,32,36`. The `n=36` random layouts produced
about `346,000` exact-six codewords per seed; all were primitive and all were
outside the tested dyadic owner, with about `100,000` diffuse members. These
experiments motivated the proof but are not used by it.

## Nonclaims

The obstruction refutes the exact finite `n^6` PMA allocation. It does not
yet prove super-polynomial image-fiber growth, refute the full prize theorem,
or determine the correct replacement profile allocation.
