# Audit

Modal app `ap-v5PL88R8Ux130XBREm4eA1` ran the two complete census engines on
eight 256 MB workers with 60-second timeouts.  They used 47.750 aggregate
worker-seconds and wrote resumable checkpoints.  The independent checker
validates source hashes, all eight rows, exact engine equality, profile and
conductor totals, every retained vector, and one hostile mutation.

Modal app `ap-4g3qQD2QBjTJtojanosSzw` ran the FLINT/PARI ledger in 31 batches
per engine with 256 MB workers.  The norm checker validates source/census
hashes, vector ordering, exact agreement, distinct count, maximum, threshold
count, maximizing indices, and one hostile mutation.  Proper- and full-
conductor populations are disjoint and sum to the complete census.
