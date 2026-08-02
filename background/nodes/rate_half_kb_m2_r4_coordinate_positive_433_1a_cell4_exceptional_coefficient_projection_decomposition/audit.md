# Audit

The verifier pins six load-bearing result artifacts and both source archives,
checks all fifteen evaluation files, the rank and shape ledger, the complete
common-gcd factorization, every primitive quotient file, the degree sequence,
lex eliminant, deployed-root factorization, and all four zero quotient
remainders over `H`.  It checks every claimed linear root against the original
guard and verifies the DAG dependencies and nonclaim.

The mutation audit corrupts the interpolation rank, removes the `H^2` factor,
changes a residual root, and flips one exact quotient remainder.  Each mutation
must fail.
