# Audit

The verifier checks exact file custody, eight-by-eight shard structure, the
full 720-case formal product, norm witness equality, the `288/432` status
census, all `1,584` non-guard roots, all `126` distinct base values, manifest
equality, and all-pair replay exclusion.

The hostile audit mutates norm coverage, witness equality, manifest custody,
replay coverage, guard status, and all-pairs singularity.  Every mutation
must be rejected.

The proof boundary was audited explicitly: a coordinate-gcd certificate only
rules out a vertical component and is not used as pointwise exclusion.  The
pointwise theorem uses the nested norm and finite replay.
