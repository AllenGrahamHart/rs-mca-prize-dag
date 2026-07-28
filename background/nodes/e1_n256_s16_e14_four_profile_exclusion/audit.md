# Audit

Modal app `ap-rQOuJb9DVQwka46OLEj4Er` ran the two complete census engines on
1,321 workers with 256 MB limits and 60-second timeouts. They used
7,636.622 aggregate dual worker-seconds and wrote a checkpoint after every
return. The independent checker validates source and atlas hashes, every row,
exact engine equality, profile and conductor totals, all retained vectors,
and one hostile mutation. An earlier app `ap-C2U6Lugoj5XbrqQWnS2rLs` failed
at remote path initialization before any census engine ran and contributes no
evidence.

Modal app `ap-A7rhyHWVrOpGoAZM9bOuSs` ran four FLINT and four PARI batches with
256 MB limits. The norm checker validates hashes, vector ordering, exact
agreement, profile maxima, 152 whole-norm threshold hits, six odd-part
threshold hits, maximizing indices, valuations, and one hostile mutation.
This check explicitly pins failure of the inherited below-threshold shortcut.

Modal app `ap-JtCD7equumzMV4qV44ziGe` ran independent PARI and FLINT primality
classifiers on the six exceptions. They agree on three distinct composite
odd parts and zero eligible primes. The checker reconstructs every exception,
threshold, valuation, residue, and one hostile mutation.
