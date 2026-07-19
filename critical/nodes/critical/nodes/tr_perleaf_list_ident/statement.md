# tr_perleaf_list_ident

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/gap1_terminal_reserve.md']

## Statement

Conditional reduction: the per-character TR set A_r is algebraically the
worst-word exact-list kernel at the same-rate quotient row, after the lifted
joint-stabilizer identity and the degenerate-tower correction column. Hence
the per-leaf bound is supplied by the corrected exact-list split
x4_exactlist_staircase_split transported to quotient rows; there is no separate
per-leaf counting theory.

## Attack surface

the only remaining attack is against the transported exact-list split itself;
a mismatch between a stable per-character agreement and a quotient-row
exact-list instance would falsify the dictionary

## Falsifier

a per-leaf count provably exceeding the quotient-row list count (would break the dictionary; toy-checkable)

## Ledger (migrated notes)

Codex red-node pass (2026-07-04): reclassified from TARGET to CONDITIONAL.
The quotient dictionary is algebraic; the open content is
x4_exactlist_staircase_split at quotient rows, with the QA.24 degenerate-tower
correction already carried by tr_joint_telescope. X-4: TR's arithmetic must
carry the transported quotient-row staircase term explicitly (exact binomials
at scale n'/Q) before the primitive per-leaf bound applies. | X-4b: the
quotient-row split gains the moment column verbatim.
