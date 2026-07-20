# Audit

1. `E_1` and `E_3` have negative signs; the recurrence uses the signed
   coefficients `E_j`.
2. The recurrence multiplier is `4n-3j`, not `4n-j`.
3. The doubled-order indices are `2H-2,2H-1,2H`, with
   `H=2^37+1`.
4. The two windows start at indices `0` and `2H`; shifting the second window
   by one changes the secondary gate.
5. The canonical leading coefficient is `alpha=4c`, not `c`.
6. `P` is the complementary-root product. The canonical lower polynomial is
   named `C` and is not a free variable after `(C2G6)`.
7. Equation `(C2G10)` is applied only after `alpha,beta,gamma` have been
   reconstructed from canonical span.
8. This exact interface can still be too expensive to evaluate naively and
   does not promote the contributor pre-request to runnable status.
9. Primary-only fourth-root rigidity is false: a bounded exact sweep found
   twelve non-pure primary survivors. Every one failed `(C2G6)`.
10. The stronger implication from `(C2G4)` and `(C2G6)` to a pure
    fourth-root denominator has survived bounded falsification but remains
    unproved and is not a dependency of this node.
