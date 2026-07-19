# prize conditional proof

- **status:** CONDITIONAL
- **closure:** proof from predicate nodes

## Predicate nodes

- `mca_grand`
- `list_grand`
- `packaging`

## Claim

Conditional on the predicate nodes, the Proximity Prize is resolved.

## Proof

`mca_grand` is the assembly for the MCA grand challenge: it supplies the
determination of the MCA threshold under its predicate chain.

`list_grand` is the assembly for the list-decoding grand challenge: it supplies
the corresponding list threshold determination under its predicate chain.

`packaging` supplies the compiler, verifier, dossier, and bridge-ledger layer
needed to present those determinations under the rules and refusal discipline.

The prize root asks for exactly these three pieces: both grand challenges
resolved per the official statement, and packaged per the rules. Therefore the
root follows conditionally from the three predicate nodes.
