# Audit

## Exact-head replay

The upstream primary checker was replayed from a shared temporary clone at
exact `pr1159@e603e0cedc5220ec2f29bd53836e732e3ec14934`, with this DAG supplied
for its external source pins.  It passed the certificate check and all `62`
semantic plus `3` parser mutations.  Replaying on the later `#1163` stack
correctly fails source drift because `#1160/#1163` modify a pinned manuscript;
the exact-head replay is the valid one.

## Independent checks

The local primary verifier independently proves primality, carrier order,
extension-modulus irreducibility, interval arithmetic, the pole root-count
noncontainment, guarded numerator cap, and both shifted minima.  It does not
load or execute the upstream checker.

The second verifier uses a separate irreducibility and shift-ledger path and
rechecks the actual/effective root margins.  Both reject owner promotion.

## Scope

This imports an actual witness theorem.  It does not repair the independently
frozen Q/BC predicates.  In particular, the strings `boundary` and
`first-interior` remain numerical profile descriptions, not owners.
