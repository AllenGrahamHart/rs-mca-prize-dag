# Attack

First discharge
`e1_qzeta128_p257_two_involution_nonprincipality_certificate`. It asks only
whether two explicit norm-`257^2` ideals are nonprincipal.

Primary route:

1. construct the three exact primes with roots `9,57,248` modulo 257;
2. form `q_1 q_63` and `q_1 q_65`;
3. certify each product nonprincipal unconditionally;
4. emit proof-producing relation or class-character data for both tests.

Independent route:

- repeat the two tests in a different CAS/algorithm, or
- check an exported relation matrix plus exact principal-ideal witnesses and
  its Smith form without invoking the primary class-group routine.

A full certified class group with the published Galois action remains an
acceptable stronger route, but it is no longer the minimum packet.

The job must checkpoint before certification, preserve useful partial output,
and distinguish `PASS`, `FAIL`, and `INCOMPLETE`. No local WSL class-group
computation is authorized.
