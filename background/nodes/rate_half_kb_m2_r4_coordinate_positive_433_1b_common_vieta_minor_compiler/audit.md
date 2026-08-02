# Audit

1. The role-cell enumerator gives exactly 15 distinct cells.
2. Both source-root signs give exactly 60 rows.
3. Every row has the exact `10 x 8` matrix shape and six minors.
4. Every row has six distinct minor digests.
5. Raw and stripped modes each account for all 360 minors.
6. Guard stripping divides only by printed nonzero/distinctness factors.
7. File hashes pin compiler, launcher, and full result.
8. Mutation tests reject a lost case, minor, or changed histogram.
