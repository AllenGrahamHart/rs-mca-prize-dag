# Audit

Modal app `ap-xIQLyhRtHtlRxbQkOIS7Yp` ran the two complete census engines on
eight 256 MB workers with 60-second timeouts. They used 52.945 aggregate dual
worker-seconds and wrote a checkpoint after every return. The independent
checker validates source and atlas hashes, all eight rows, exact engine
equality, profile and conductor totals, every retained vector, and one hostile
mutation.

Modal app `ap-4c65PlujVH2D5kNI12Bcac` ran one FLINT and one PARI batch with
256 MB workers. The norm checker validates hashes, vector ordering, exact
agreement, profile maxima, 32 whole-norm threshold hits, zero odd-part
threshold hits, maximizing indices, valuations, and one hostile mutation.
