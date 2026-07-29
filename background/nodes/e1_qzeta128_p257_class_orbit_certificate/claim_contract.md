# Claim contract

## Object

The 64 degree-one prime ideals above 257 in
`K=Q(zeta_128)=Q[x]/(x^64+1)`.

## Conditional claim

Their ideal classes are pairwise distinct.

## Conditional dependency

`e1_qzeta128_p257_two_involution_nonprincipality_certificate`: the two
explicit ideals `q_1 q_63` and `q_1 q_65` are nonprincipal.

Its `q_1q_65` assertion is proved. Its sole open premise is the degree-32
fixed-field nonprincipality certificate for the prime of residue 66
transferring to `q_1q_63`.

## Proved and published inputs

- `e1_conductor256_full_unit_circular_basis` imports Miller's unconditional
  theorem `h(Q(zeta_256)^+)=1`.
- Weber's oddness theorem for 2-power cyclotomic class numbers, including the
  plus factor, is pinned in `source_evidence.md`.

## Proved implication

The open premise excludes the two non-complex involutions from the stabilizer
of `[q_1]`. Real class number one makes complex conjugation act by inversion,
and odd full class number then excludes the remaining involution. Every
nontrivial subgroup of `(Z/128Z)^x` contains an involution, so the stabilizer
is trivial and the orbit has 64 elements.

The former full class-group certificate remains an acceptable stronger
discharge of the premise, but is no longer required.

## Nonclaims

- The published slide is evidence, not the required replay.
- The proved `q_1q_65` product alone is insufficient; the remaining
  `q_1q_63` product is still required.
- GRH-conditional class-group output is insufficient for an unconditional
  prize proof.

## Consumer

`e1_profile018_qzeta128_class_descent_two_ideal_bound`.
