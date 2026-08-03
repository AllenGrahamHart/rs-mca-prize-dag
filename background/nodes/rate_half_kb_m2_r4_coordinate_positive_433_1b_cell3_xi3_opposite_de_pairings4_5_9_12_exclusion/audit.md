# Audit

- The census has four pairing-4 rows covering four lanes each and eight
  pairing-5 rows covering two lanes each: 12 rows and 32 computed raw cases.
- Every row has degree profile `(P,J,M,R,Bezout)=(4,8,4,3,4x4)` and uses the
  quadratic-over-cubic tower norm.
- Candidate parameters are the union of every norm and exceptional-guard
  root; all 296 source points are explicitly listed and unique within rows.
- Direct replay enumerates 928 missing-`f` rows, 184 common-`q` roots, and 480
  final colored-pair lane evaluations.
- All 480 final colored-pair evaluations are nonzero.
- Witness, target-boundary, free-gcd, and unresolved ledgers are empty.
- Formal matching enumeration maps 4 to 9 and 5 to 12 under exchange of the
  two equal positive `de` records; paired symmetry preserves orientation.
- The 12 computed rows pay 32 raw cases, and exact transport pays 32 more.
- Primary and independent verifiers pin the compiler and census hashes.
