# Audit

## Modal provenance

- count-only dual census: `ap-k55Y5gyShllfB8hQqHCwQ1`, 924.812 aggregate
  worker-seconds;
- full dual collector: `ap-YUhoRVWWVQcb1O5XcckRAp`, 943.198 aggregate
  worker-seconds;
- FLINT/PARI norm ledger: `ap-3hh9iFYztMHpgVSG9ydtd6`.

Every worker used 256 MB.  Census workers had a 60-second container timeout;
norm workers had 120 seconds.  Both census launchers wrote an incomplete
checkpoint before dispatch and rewrote it after each returned template.  The
norm launcher checkpointed after each engine.

## Independent checks

The folded-chord and direct-negacyclic engines agree per template.  The
collector reproduces every count and content checksum from the earlier
count-only run and stores exact agreement for every full-conductor vector.
The local collector checker independently recomputes all 6,834 profiles.

FLINT and PARI/GP agree on all 6,834 resultants.  The norm checker reconstructs
the source/collection hashes, vector ordering, distinct count, exact maximum,
threshold count, and maximizing indices.  Across the three checkers four
hostile mutations are rejected.

The two empty profiles are not conflated with norm exclusions.  The proper-
conductor and full-conductor populations are disjoint and sum exactly to the
complete actual-vector census.
