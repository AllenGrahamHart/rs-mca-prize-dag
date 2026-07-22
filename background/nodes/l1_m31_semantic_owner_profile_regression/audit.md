# Audit

## Upstream replay

PR `#1047` was fetched at exact head
`0e735999acf24a7779b2271553deb26207396cda` and extracted to a fresh temporary
directory. With the pinned `leanprover/lean4:v4.31.0` toolchain, `lake build`
completed all `14` jobs successfully. The relevant source SHA256 values are:

```text
DeployedOwnerProfiles.lean  c8a2c5505b2f167e6fa7b299959bfc55b3e3f56bf6d0fae331b4fd36818041a4
SemanticLineRegression.lean 2dc478f468408248d9bf4595391f4d538a64c6cda62dc7668741dd567dbb95d5
threshold note               066ce8bf617dcf5261004d7bb13f8084813f3344aa3efd467168360e981ce3c3
```

The local Python verifier independently replays the theorem-relevant finite
field checks, rather than treating a successful upstream build as the proof.

## Quantifier audit

The deployed constructors begin with a certificate containing the slope list
and its source-theorem length bound. They prove a typed payment chain for that
supplied list. They do not construct a list from an arbitrary received word,
prove every explanation reaches one of the two branches, or sum profiles over
one line. The average ceiling `1993678` is likewise a calibration hypothesis,
not a binomial calculation performed by this packet.

The `F_241` half has stronger semantics but only finite scope. Its parity
certificates exclude a common explanation of the line direction, and its
owner predicate is fixed before the residual filter. This makes the two owner
deletions genuine in the fixture. It does not transport the result to the
deployed M31 row or to the support-level `T_64` profile in
`l1_m31_t64_quotient_prefix_intercept_fence`.

No relation to the KoalaBear MCA four-cell chronology is claimed: the object,
row, denominator, and owner unit are all different.
