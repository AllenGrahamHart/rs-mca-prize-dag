# Claim contract - L1 marked common-pencil quotient-boundary router

## Inputs

- a core partition into complete fibers of the same polynomial `P` used by
  the common constant-shift pencil;
- `l1_marked_common_pencil_crt_fiber_bound` for the numerator multiplicity;
- fixed bounds `p<=P_0` and `beta<=B_0` when polynomiality is invoked.

## Output

Every split defect locator is uniquely a partial-fiber boundary times a
quotient-core locator. In a fixed boundary box the codeword count is bounded
by a fixed polynomial factor times the corresponding full-fiber quotient-core
census.

## Consumer rule

Consumers may remove bounded boundary and numerator multiplicity from the
primitive locator budget. They must retain the quotient-core census, source-
chart first-match multiplicity, cores not partitioned by `P`, and arbitrary-
locator petals. No exact-periodic ownership follows from this node.

## Falsifier

Two decompositions of one split locator, a boundary containing a full fiber,
a fixed `(B,A_0)` producing two locators, or a fixed locator producing more
than the CRT numerator bound.

