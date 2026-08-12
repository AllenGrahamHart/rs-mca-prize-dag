# Audit

## Source

Upstream `#1160` contains the exact one-shift lattice/support census theorem.
Upstream `#1159`, as present on the `#1163` head, isolates the deployed
`K=k` versus `K=k+1` gap.  Exact source blobs are pinned in
`source_contract.json`.

## Shift convention

The proof writes both weighted degrees explicitly.  It does not substitute
`k+1` for the code dimension in the upstream theorem.  The lattice module is
unchanged; only its shift and one quotient coefficient differ.

## Exact support

The locator has exactly the complement roots and degree `n-m`.  This avoids
silently shrinking a larger source support.  The explanation, line, slope,
and support are retained rather than reconstructed from owner labels.

## Pair noncontainment

The noncontainment check is not a Boolean field.  It is the exact degree test
on the two unique degree-`<m` support interpolants.  This is decidable by
finite-field arithmetic and is equivalent to the source definition because
`m>k`.

## Verification

The primary verifier exhausts every value assignment on every four-point
support of a six-point `GF(7)` row, checking all `36,015` effective-envelope
support records and the exact `7^3` versus `7^4` dimensions.  It also checks
all shift-degree pairs in a bounded degree box and runs eight mutations.  The
independent audit derives the official-row coefficient gap and tests the
same-support pair criterion without importing the primary verifier.
