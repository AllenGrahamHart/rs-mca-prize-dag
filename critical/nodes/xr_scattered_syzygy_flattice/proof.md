# xr_scattered_syzygy_flattice proof

## Predicate node

- `xr_syzygy_flat_transport`

## Claim

Diffuse far-spread stagnations are exactly transported to the Face-2
sparse-dual/closed-set lattice objects over the corresponding
intersection-pattern flats.

## Proof

In a diffuse stagnation, the `k+1` overlap budget is distributed over many
small overlaps, so no single overlap triggers the near-core forcing rungs. The
proved transport node `xr_syzygy_flat_transport` identifies the resulting
rank-stagnation witness as a constrained-support dual codeword. Its support is
not arbitrary: it is cut out by the same intersection pattern that records the
small overlaps among the aligned supports.

That intersection pattern is exactly the flat used by the Face-2 machinery.
Counting such stagnations therefore becomes counting constrained-support dual
codewords and their linear relations inside that flat, which is precisely the
sparse-dual/closed-set lattice object in the Face-2 formulation.

The node does not assert the final polynomial bound for the Face-2 residue; it
proves the dictionary identifying the diffuse Face-4 residue with that
Face-2 object. The counting theorem remains wherever the DAG wires the Face-2
residue.
