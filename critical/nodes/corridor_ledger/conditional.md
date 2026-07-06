# corridor_ledger conditional proof

## Predicate node

- `fourth_mechanism_rate8`

## Claim

The corridor ledger closes exactly if the explicit rate-1/8 fourth-mechanism
wedge is supplied.

## Proof

The three original eaters are now numeric:

- `acl_second_order` supplies the evaluated ACL contribution.
- `corridor_window_cleanup` supplies the finite window cleanup column.
- `corridor_ext_crossing` supplies the extension-crossing arithmetic, which is
  zero at the checked generating-row crossing points.

The evaluated three-eater ledger delivers less than `W(rate) - 1` at all three
clean rates. Therefore the original three-eater route is a proved negative
result: it gives bracket-grade determinations only.

The remaining deficit is sharpest at rate `1/8`, where the missing amount is
`0.00707` grid steps, about `0.9` bits. The predicate
`fourth_mechanism_rate8` is defined to supply that missing amount by any of
the three listed routes: cap-end sharpening, tau-star reserve tightening, or
knife-edge census pinning.

If `fourth_mechanism_rate8` holds, adding its contribution to the completed
three-eater ledger reaches `W(rate) - 1` in the only live deficit case, and the
other clean rates are no worse. Hence the corridor ledger follows. Without
that predicate, the ledger remains bracket-grade by the completed arithmetic.
