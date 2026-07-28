# Audit

Modal app `ap-87cpQMjvYyW2nYdoZpL6Uz` ran the two complete census engines on
up to 100 256 MB workers with 60-second timeouts. They used 7,712.034
aggregate dual worker-seconds and wrote resumable checkpoints. The independent
checker validates source and atlas hashes, all 1,321 rows, exact engine
equality, profile and conductor totals, every retained vector, and one hostile
mutation.

Modal app `ap-k5DWA74ZUKZK3N03ngNeEP` ran the final FLINT/PARI ledger in three
batches per engine with 256 MB workers. The norm checker validates hashes,
vector ordering, exact agreement, profile maxima, six whole-norm threshold
hits, zero odd-part threshold hits, maximizing indices, valuations, and one
hostile mutation. The earlier app `ap-u5Kj4NOzDFQPwSB1TLUNdT` produced the
same whole norms but did not print the decisive odd-part ledger and is
superseded.
