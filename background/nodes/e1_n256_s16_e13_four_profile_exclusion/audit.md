# Audit

Modal app `ap-AhqC0lLGj9BYMLmRpKa1mj` ran the two complete census engines on
111 workers with 256 MB limits and 60-second timeouts. They used 613.766
aggregate dual worker-seconds. The independent checker validates source and
atlas hashes, every row, exact engine equality, profile and conductor totals,
all retained vectors, and one hostile mutation.

Modal app `ap-cXvEeUhd1ym0Ep1InsluxC` ran one FLINT and one PARI norm batch.
The checker validates hashes, vector ordering, exact agreement, profile
maxima, 112 whole-norm threshold hits, four odd-part threshold hits,
maximizing indices, valuations, and one hostile mutation.

Modal app `ap-a4p98JmkMEXvNaIRL7bXzV` ran independent PARI and FLINT primality
classifiers on the four exceptions. They agree on two distinct composite odd
parts and zero eligible primes. The checker reconstructs every exception,
threshold, valuation, residue, and one hostile mutation.
