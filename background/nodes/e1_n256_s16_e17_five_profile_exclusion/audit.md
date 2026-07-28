# Audit

Modal app `ap-nuzv6imnkUH0ElJlCLyKRy` ran the two complete census engines on
up to 100 256 MB workers with 60-second timeouts. They used 651.958 aggregate
dual worker-seconds and wrote resumable checkpoints. The independent checker
validates source and atlas hashes, all 111 rows, exact engine equality, profile
and conductor totals, every retained vector, and one hostile mutation.

Modal app `ap-YS86fN9k5a8svWi6zF2boU` ran one FLINT and one PARI batch with
256 MB workers. The norm checker validates hashes, vector ordering, exact
agreement, profile maxima, 16 whole-norm threshold hits, zero odd-part
threshold hits, maximizing indices, valuations, and one hostile mutation.
