# list_planted_arithmetic

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s7_list_side.md']

## Statement

planted_count(delta) is an explicit combinatorial formula (core/petal choices x scalar factors). Under worst_word_planted + challenger pricing + imgfib + integrality, the list crossing is decided by integer arithmetic: windows [priced_count - margin, priced_count) in eps*|F|-space, with the census/dodge structure transferring verbatim from the MCA side and with NO zone-(b) analogue (no value sets mod p; counts are explicit).

Premise weakening recorded 2026-07-06: downstream use does not require a global claim that only the planted and E15-successor families exist.  It is enough to have, row by row, a certified upper envelope for every non-extremal/non-planted contribution and explicit lower witnesses for unsafe rows.  Exact two-column challenger pricing is one clean way to supply that envelope, but not the only possible way.

## Ledger (migrated notes)

unsafe witnesses are free (exhibit the plants); the safe certificate is imgfib at the candidates + the FM-style extras table | IN FLIGHT: #196 | Must now price the E15 challenger class alongside planted counts (see revised worst_word_planted). | STATUS CORRECTED 2026-07-04: this is a proved conditional arithmetic reduction, not an unconditional theorem, because worst-word extremality and image-fiber safety are predicate inputs.

## Stress Evidence 2026-07-06

The challenger/envelope premise has two exact local falsifier runs attached:
`e22_extended_local_census.py` checked 77 cyclic-layout cells and 1,920,836
agreement subsets, while `e22_random_layout_census.py` checked 219 shuffled
cells and 1,427,408 agreement subsets.  Both returned UNCLASSIFIED=0.  This
supports the two-column arithmetic premise but does not replace the missing
top-down pricing theorem.

## W3 scope disposition

This node is now evidence only for `list_adjacency_closing`. The live
clean-rate assembly consumes `list_unsafe` for the constructive lower side
and `list_safe` for the uniform upper side. Literal safe-side W3 remains open
but unnecessary; the exact fiber construction refutes only applying its upper
inequality at the unsafe spending cell. The explicit planted and qcore counts
remain valid arithmetic.
