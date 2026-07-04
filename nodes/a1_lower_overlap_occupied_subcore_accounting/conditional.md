# a1_lower_overlap_occupied_subcore_accounting conditional proof

## Predicate node

- `anchored_nontoral_pte_bound`

## Claim

The lower-overlap occupied-subcore accounting follows from the active anchored
non-toral PTE bound.

## Proof

Work after the unified paid strip. A lower-overlap occupied subcore is, by
definition, active only when at least one post-strip aligned partner passes
through it. The P1 reduction already converts such a post-strip rich-line
event through a fixed subcore into a primitive anchored same-top-`t` locator
trade; the strip removes the tangent, quotient-with-tails, and dihedral
families, so an uncharged event is non-toral.

Choose the canonical first post-strip witness for each active occupied subcore
under the fixed ordering of slopes and supports. This gives an injection from
active occupied subcores to the anchored non-toral PTE pairs counted by
`A_h^nt`, up to the bounded local multiplicity already included in the P1
subcore reduction.

The predicate `anchored_nontoral_pte_bound` gives `A_h^nt <= h n` in the
relevant range, and the local multiplicity is absolute for the fixed
subcore/rich-line normal form. Therefore the total number of active occupied
subcores is budget-bounded, and summing the proved per-subcore cap over them
gives the required lower-overlap accounting.
