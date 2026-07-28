# Audit

Modal app `ap-42XirNxhFdMDLcgSyAoyqK` ran the two complete census engines on
eight 256 MB workers with 60-second timeouts. They used 45.217 aggregate dual
worker-seconds and wrote resumable checkpoints. The independent checker
validates source hashes, all eight rows, exact engine equality, profile and
conductor totals, every retained vector, and one hostile mutation.

Modal app `ap-qH9fzHkBAjTdTeWWEgJ7iN` ran the FLINT/PARI ledger in nine batches
per engine with 256 MB workers. The norm checker validates source/census
hashes, vector ordering, exact agreement, distinct count, maximum, threshold
count, maximizing indices, and one hostile mutation. Proper- and full-
conductor populations are disjoint and sum to the complete census.
