# Attack

First discharge
`e1_qzeta128_p257_two_involution_nonprincipality_certificate`. One of its two
norm-`257^2` ideals is proved nonprincipal. It now asks only whether the
degree-32 fixed-field prime of residue 66, equivalently `q_1q_63`, is
nonprincipal.

Primary route:

1. construct `E_63=Q(zeta_128-zeta_128^(-1))`;
2. form `p_66=(257,zeta_128-zeta_128^(-1)-66)`;
3. certify this prime nonprincipal unconditionally;
4. emit proof-producing relation or class-character data for the test.

Independent route:

- repeat the remaining test in a different CAS/algorithm, or
- check an exported relation matrix plus exact principal-ideal witnesses and
  its Smith form without invoking the primary class-group routine.

A full certified class group with the published Galois action remains an
acceptable stronger route, but it is no longer the minimum packet.

The job must checkpoint before certification, preserve useful partial output,
and distinguish `PASS`, `FAIL`, and `INCOMPLETE`. No local WSL class-group
computation is authorized.
