# Audit

The assembly adds no algebraic assertion. Its only possible failure modes are
a missing matching, overlap, wrong multiplicity, or an unproved parent. The
independent verifier constructs sets of integer `(xi,pairing)` labels rather
than trusting cumulative prose counters, rejects overlap, requires exactly
45 labels, and checks all seven parents and requirement edges.
