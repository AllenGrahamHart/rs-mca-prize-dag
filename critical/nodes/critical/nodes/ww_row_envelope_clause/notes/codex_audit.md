# Audit: W3 direct re-pose

## Finding: FIXED

The node packet had retired K_cell, but the authoritative DAG statement still
asserted count <= C*K_cell/q^sigma with no independent definition or
certificate semantics for K_cell. A secondary direct_repose_20260712 field
said that a different statement was binding. This violated the single-source
rule and left consumers dependent on which field a reader selected.

The DAG statement now matches the packet exactly: bound the actual challenger
count by the exact conservative residual integer budget. K_cell is retained
only as historical route vocabulary and cannot be consumed as a premise.

This repair does not prove the direct count.

## Finding: per-cell whole-residual form did not compose

The imported R1 wording compared every first-match cell count to the same row
residual `B_chal`. With more than one nonempty cell, these inequalities do not
imply that the total challenger count fits `B_chal`; no uniqueness theorem or
cell-budget partition was present in the packet or DAG.

The consumer needs a worst-case statement for each received word, not a mean
over words. The corrected form preserves that supremum and uses disjoint
first-match counts with explicit allocations `b_c` satisfying
`sum_c b_c<=B_chal(U)`. This is the standard sufficient ledger law and makes
the amber implication valid without assuming one active cell.

This repair also exposes the specification debt: the official cell descriptor
list and exact paid-column subtraction table must be emitted before W3 can be
closed by certificates.

## Finding: paid/residual ownership was ambiguous

The packet subtracted the quotient/staircase column in `P_paid` but defined
`N_chal^o` as all non-planted words in challenger cells. The repository also
claims that the E15 structured challenger is the quotient-coset staircase.
Without a binding ownership order, the same word could therefore be paid once
and then charged again to the residual.

W3 now orders the paid columns first and counts only the residual first-match
classes in `N_chal^o`. Closing data must print this ownership map and prove
coverage and disjointness. This correction neither proves the E15/staircase
identification nor supplies the missing residual envelope.
