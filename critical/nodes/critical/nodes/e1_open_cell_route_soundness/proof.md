# proof: e1_open_cell_route_soundness

By `official_row_primes_pinning`, the prize statement does not provide a
hidden finite list of official row primes. Therefore an E1 open-cell payload
must declare one of two legitimate forms:

- a theorem uniform over the admissible field/rate/domain family; or
- an exhibit-specific certificate naming the exact field being certified.

If the payload takes the uniform route and proves admissible-family typicality
for the explicit norm-divisor exceptional set in the cells `N' in {128,256}`,
then it is exactly the first disjunct in
`e1_official_typicality_or_certificate`.

If the payload takes the exhibit route, it names the fields and provides
complete folded kernel searches for the open cells with no nonzero
non-cyclotomic folded vector. By `e1_folded_certificate_soundness`, each such
complete no-vector certificate excludes all non-quotient E1 collisions in the
named row. This is exactly the second disjunct in
`e1_official_typicality_or_certificate`.

Thus either accepted route proves the E1 open-cell typicality-or-certificate
predicate.
