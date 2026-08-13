# Proof

Choose a minimum lift of the direction syndrome

```text
q=r_1-b,       b in RS[F,D,s],       wt(q)=R-j,
```

and put `E=supp(q)`.  Every selected witness has size `d+s`, while the
zero set of `q` has size `s+j`.  Hence

```text
|S_gamma intersect E| >= d-j.                        (1)
```

For `x in E`, let `Z_x` be the slopes whose selected witness contains `x`.
All explanations in this subfamily agree with the received line at `x`.
Subtract the received values there, divide by `X-x`, and delete `x`.  The
common-core cancellation adapter maps `Z_x` injectively to a support-wise
MCA-bad family in `(R+s-1,s-1,d+s-1)` and preserves slopes and
same-support noncontainment.

Any child direction lift lifts to an original degree-`<s` codeword
constrained to agree with `r_1` at `x`.  Its residual has the same weight
after deleting `x`.  Global minimality of `q` therefore gives child defect
`j_x<=j`.

The child hypothesis and double counting now give

```text
|Z|(d-j) <= sum_(x in E)|Z_x|
           <= (R-j)M_(s-1)(j),
```

which proves `(RS1)`.

For the repaired official envelopes, initialize each defect `j` at `s=1`
with the proved direct direction-distance value, only when that value is
within budget.  Iterate `(RS1)`, taking the minimum with the direct bound
whenever its denominator is positive.  This uses no affine-span incidence
bound.  Exact integer iteration gives the pinned checkpoints.
