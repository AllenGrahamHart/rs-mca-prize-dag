# Attack

Primary route:

1. construct `K=Q[x]/(x^64+1)` and the three transcript-pinned primes;
2. form `J_63` and `J_65` by exact ideal multiplication;
3. certify both ideals nonprincipal unconditionally;
4. retain the exact relation matrix, class-character data, or other
   proof-producing obstruction used for each test.

The full PARI route may use `bnfinit`, `bnfisprincipal`, and the default
`bnfcertify(B)`. A more focused cyclotomic route may instead certify a
nonzero 21121-primary image of `J_63` and a nonzero 17-primary image of
`J_65`; the published class coordinates predict precisely those two
obstructions. `subcyclopclgp(128,p)` rigorously determines the minus
`p`-part but does not by itself locate either ideal in that part.

The independent route must use a different CAS/algorithm or replay exported
exact relation and principal-witness data without invoking the primary
class-group routine.

The job must checkpoint, distinguish `PASS`, `FAIL`, and `INCOMPLETE`, and
obey the compute request's one-container pilot and spend limits. No local WSL
class-group computation is authorized.
