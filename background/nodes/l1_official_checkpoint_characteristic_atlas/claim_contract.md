# Claim contract - L1 official checkpoint characteristic atlas

## Inputs

- official orders `2^13<=n<=2^44`;
- the generated-field divisibility and strict 256-bit cap;
- the proved characteristic floor `p>=3583`;
- the split-value capacity and complement-square compiler.

## Output

Exactly 59 characteristic/domain pairs can have `p<n`. Of them, 33 have no
minimum-width split pair, 10 reduce to the `m=2` complement-square census,
and 16 retain `m>=3`.
Exactly four of the `m=2` rows have two-point complements and exactly `n/2`
minimum-width pairs. The other six `m=2` rows are empty at `t=p`.

## Falsifier

An official-admissible pair `(n,p)` with `p<n` absent from the atlas; an atlas
row violating generated-field admissibility; or an incorrect `m` histogram.
An incorrect identification of the four two-point-complement rows is also a
falsifier.

## Nonclaims

No classification of perturbations on the 16 `m>=3` rows, no assertion that
every atlas pair appears in a submitted code, no control of `t>p`, and no L1
status change.
