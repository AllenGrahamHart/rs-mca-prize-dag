# Upstream crosswalk - boundary affine Q cell

## Off-by-one alignment

Paper D's active BC census starts at `d_1=w+2`; the profile `d_1=w+1` is
delegated to Q.  This node proves that assignment for L1 exact shells rather
than adopting it as a convention.

## Cell dictionary

The boundary projective pencil has one point at infinity, costing at most
one complete codeword, and an affine family `g_2+A g_1`.  When `W_1=1`, the
family is exactly the prescribed-top-`(w+1)` locator-Q fiber.  Otherwise it
is a quotient/residue affine Q cell of the type that upstream's active
priority map must coalesce.

## Remaining input

Q flatness and quotient-pullback coalescing remain open on the boundary.  At
`d_1>=w+2`, L1 needs the guard-pruned exact BC residual after
`l1_interior_bc_floor_higher_shell_q_routing`; Paper D's raw base-field floor
routes to higher-shell Q.  The surviving Q and exact-BC terms must be summed
with separate numerators in any finite certificate.
