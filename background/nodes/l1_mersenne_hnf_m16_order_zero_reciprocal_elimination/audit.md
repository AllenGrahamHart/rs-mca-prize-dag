# Audit

## Exactness

Both eliminants are formed as polynomials over `F_8191`; no evaluation grid,
floating point, probabilistic factorization, or field-element sampling is
used. The raw degree bounds in the proof exceed the characteristic, which is
why ordinary base-field interpolation would not be a certificate here.

## Independent construction

The primary worker constructs `Q_s` by a polynomial resultant. The audit
constructs the same characteristic polynomial from a companion matrix,
matrix traces, and Newton identities. It does not call the primary
`Res(P_s,Z-W^16)` operation. Both workers use exact Singular polynomial
resultants for the final two-variable eliminants and reproduce all four
hashes. The small radical and field-polynomial divisibility are checked again
by a stdlib local verifier.

## Logical direction

The reciprocal equations are necessary only. That is sufficient for an
exclusion: a genuine survivor would be a common zero of `F_1,F_2,F_3` and
hence of both resultants. No reverse implication from an eliminant root to an
HNF survivor is claimed.

## Resources

The final primary and audit workers each used one CPU, peaked at `110 MB`,
and ran for `16.75` and `12.79` seconds. The exact bill was not queried; the
whole bounded campaign is conservatively recorded below `$0.05` and no
further run is needed.

## Nonclaims

Order one remains open. This theorem does not close the first-checkpoint
atlas, the arbitrary-word L1 target, or either grand challenge.
