# c1_scalable_certificate conditional proof

## Predicate nodes

- `c1a_lowh_direct_certificates`
- `c1b_descent_injection`
- `midlarge_h_certification`

## Claim

Conditional on the predicate nodes, the scalable `D(n,h)` certificate required
by the (A) closure exists for `n = 1024`, all official row primes, and all
`h` in the official window.

## Proof

The h-window is partitioned by the coverage map recorded in the DAG.

First, `c1a_lowh_direct_certificates` supplies direct per-row certificates at
the bottom of the window, in particular the `h = 4` range and any low-h cases
covered by the direct MITM certificate path.

Second, `c1b_descent_injection` is proved. It supplies the dyadic
descent-injection certificate: trades at level `n = 1024` inject into bounded
bottom band-pair data with compatible lifts, while the diagonal/antipodal
branch is paid. This covers the descent-certified small-h range beyond the
direct bottom cases.

Third, the window audit shows `H_max = A`, so the remaining uncovered part is
the widened mid/large range. This is exactly the predicate
`midlarge_h_certification`, whose subnodes certify the range not covered by
C1a and C1b.

These three predicates cover the whole official h-window. Therefore, once they
hold, every required `D(1024,h)` cell has either a direct certificate, a
descent-injection certificate, or a mid/large-h certificate. That is precisely
the scalable certificate required by the (A) closure.
