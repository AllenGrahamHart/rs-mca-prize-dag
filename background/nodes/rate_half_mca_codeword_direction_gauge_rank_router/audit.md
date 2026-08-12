# Audit

The primary verifier evaluates both terms of `(G3)` at every legal ambient
dimension for every printed rank, checks unimodality and each exact adjacent
wall, and rejects four contract mutations.

The independent verifier locates the minimum of the first term from its
successive-ratio sign, then uses binary search on the increasing branch and
cross-checks the printed boundary values.  It rejects three controls.

Both checks use bounded integer state under RAMguard.  No Modal compute is
used.
