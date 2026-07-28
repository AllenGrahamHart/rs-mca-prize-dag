# Audit

Date: 2026-07-28.

The proof is computation-light and exact. The logarithmic majorant is reduced
to a factored derivative and a rational Taylor certificate at the only
nontrivial endpoint. Every cofactor threshold is checked with a positive
Taylor truncation; a geometric Taylor-remainder upper bound independently
checks that the preceding `V=2 mod 8` chamber does not already meet the same
norm inequality.

The `V=2` exclusion is not a floating-point norm estimate. The verifier builds
the integer Lucas recurrence, replays the four resultant norms, checks the
three composite-cofactor remainders, and compares the pure-power quotients
against the exact upper endpoint of the prize interval.

No vector census, factorization, primality test, local search, or Modal run is
load-bearing. The result does not count the remaining vectors and therefore
does not promote either TARGET consumer.
