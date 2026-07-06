# corridor_ext_crossing

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/proof_sketch/s2_paid_ledger.md']

## Statement

The extension-pole contribution at the crossing points: exact arithmetic of the ext column at a_safe and a_safe - 1 per rate (consuming the proved ext_pole_floor/ext chain), yielding the grid-step fraction the ext side recovers. Provable-shaped: the components are proved; the crossing-point evaluation is arithmetic.

## Attack surface

evaluate the proved ext functions at the six crossing points

## Falsifier

an ext crossing value that widens a corridor

## Ledger (migrated notes)

COMPUTED (agent, verifier PASS): N(L) = 0 at all six crossing points on generating rows — the ext eater is a GUARD (0.000 grid steps), and the non-generating branch WIDENS. CONDITIONAL on the generating-rows reading = axis8_generating.
