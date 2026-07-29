# Attack

The `J_65` half is closed. Primary route for `J_63`:

1. construct the degree-32 fixed field
   `Q(zeta_128-zeta_128^(-1))` and `p_66=(257,beta-66)`;
2. certify `p_66` nonprincipal unconditionally;
3. retain the exact relation matrix, class-character data, or other
   proof-producing obstruction used for the test.

The full PARI route may use `bnfinit`, `bnfisprincipal`, and the default
`bnfcertify(B)`. A more focused cyclotomic route may instead certify a
nonzero 21121-primary image of `p_66`. `subcyclopclgp(128,21121)` rigorously
determines the relevant minus part but does not by itself locate this ideal.

The independent route must use a different CAS/algorithm or replay exported
exact relation and principal-witness data without invoking the primary
class-group routine.

The job must checkpoint, distinguish `PASS`, `FAIL`, and `INCOMPLETE`, and
obey the compute request's one-container pilot and spend limits. No local WSL
class-group computation is authorized.
