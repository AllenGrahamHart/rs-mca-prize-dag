# Direction-mismatch recursive shortening

- **status:** PROVED
- **closure:** field-general recurrence plus exact deployed envelopes
- **scope:** a support-wise MCA-bad family in a shortened row

## Recurrence

Let the row be `(N,K,m)=(R+s,s,d+s)`.  Let the received-line direction
have nonzero syndrome `y_1`, minimum lift weight `d_U(y_1)=R-j`, and
`0<=j<d`.  Suppose every support-wise MCA-bad family in the row with
dimension `s-1` and direction defect at most `j` has size at most
`M_(s-1)(j)`.  Then every such family in dimension `s` has size at most

```text
M_s(j) <= floor((R-j) M_(s-1)(j)/(d-j)).             (RS1)
```

This recurrence composes with the direct direction-distance bound by taking
the smaller bound at every dimension.  Starting from the all-defect
support-wise affine-span boundary gives the exact certified envelopes in
`source_contract.json`.

## Deployed effects

On KoalaBear, the recursive envelope pays defects `0<=j<=4330` at the first
large dimension `s=14`, pays that whole defect interval through `s=22`,
pays `j<=9` at `s=4982`, and pays the rank-regular branch `j=0` through
`s=4992`.

On Mersenne-31, it pays `j<=4334` at `s=6`, then the cutoff decreases as
recorded; the rank-regular branch remains paid through `s=4979`.

## Residual

The unproved branch is exactly the complement of the checkpointed recursive
envelope, together with every `j>=d`.  No payment is asserted there.

## Nonclaims

This does not close the low-direction cell, sum over unrelated global-core
families, supply an external first-match atlas, or close a row or prize.

## Falsifier

A child produced by cancellation whose direction defect exceeds its parent
defect, failure of the incidence floor `d-j`, a family violating `(RS1)`, or
an incorrect deployed checkpoint.
