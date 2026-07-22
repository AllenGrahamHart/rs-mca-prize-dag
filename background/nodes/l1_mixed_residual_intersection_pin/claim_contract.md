# Claim contract - L1 mixed-residual intersection pin

## Inputs

- `l1_polarized_petal_entropy_ledger`: polynomial payment for fixed `p+e`,
  strictly extending the former fixed-`u+e` payment;
- `pma_b11_first_match_router`: polynomial payment for the fixed B11 anchor
  gates at bounded `d-ell`;
- `petal_reserve_rich_fiber_reduction`: the source-coupled rich-fiber
  necessity.
- `l1_polarized_b11_box_closure`: complete payment of every fixed
  `(p,d-ell)` box.
- `l1_general_first_layout_domination`: one fixed source plus `M` anchors;
- `l1_fixed_source_quotient_partition_anchor_census`: polynomial supply of
  whole-petal-anchored quotient partitions;
- `l1_fixed_source_anchored_triple_polarity_closure`: complete payment of
  every fixed layout/core-defect/petal-polarity anchored common-pencil box,
  including partial cores and numerator fibers.

## Output

For every fixed threshold box, the unpaid mixed/partial residual is the exact
intersection `(I3)`, satisfies the two-parameter escape `(I4)`, and every
member also has the reserve rich fiber. In the fixed first source, the
anchored common-pencil residual has growing triple polarity; an unanchored or
smaller-fiber quotient map; or arbitrary petal locators.

## Consumer Rule

Use this node to restrict an attack or aggregate to `(I3)`. Do not treat the
restriction as a count of `(I3)`, a natural-scale owner, or a proof of L1.
Do not reintroduce a fixed-polarity Forney-key multiplier in the anchored
branch.

## Falsifier

A word outside `(I3)` that is in neither proved paid class, a missing B11
first-match case under the printed inequalities, or a failure of the rich
fiber hypotheses in the shared maximal-sunflower setting.
