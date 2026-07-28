# Audit

Modal app `ap-wX3VHEQgXjopXqefRieIpQ` ran the two complete census engines on
up to 100 256 MB workers with 60-second timeouts. They used 959.740 aggregate
dual worker-seconds and wrote resumable checkpoints. The independent checker
validates source and atlas hashes, all 154 rows, exact engine equality, profile
and conductor totals, every retained vector, the two empty routed classes,
and one hostile mutation.

Modal app `ap-NKEaivIgiXPWHEwHeBgkkM` ran one FLINT and one PARI batch with
256 MB workers. The norm checker validates hashes, vector ordering, exact
agreement, profile maxima, ten whole-norm threshold hits, zero odd-part
threshold hits, maximizing indices, valuations, and one hostile mutation.
