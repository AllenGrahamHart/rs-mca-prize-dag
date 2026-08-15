# Audit

The primary verifier checks the exact formula, the factored clean-line
inequality for all relevant specialization values, exhaustive integer
partitions through `A=13`, and hostile contract mutations.

The independent audit exhausts weighted affine planes over `F_3` for
`A=3,4`. It retains every rich affine line, computes the exact best convex
selected partition on that line by dynamic programming, and checks `(SP1)`.
It also runs deterministic `F_5` stress cases. These are falsification
checks only; the proof is the injective accounting in `proof.md`.

All replay is constant-memory and belongs to the `tiny` RAMguard profile.
