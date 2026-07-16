# Proof

Fix `r>=2` with `d_r>0`.  Starting from the chosen `m`-agreement sets,
repeatedly delete a member that belongs to fewer than `d_r` four-subset labels
whose current multiplicity is at least `r`.

At the moment of deletion, at least

```text
b-d_r+1=floor((r-1)T/(B+1))+1                    (1)
```

of its four-subsets have current multiplicity at most `r-1`.  Charge all
those labels to the deleted member.  Any fixed four-subset label is charged
at most `r-1` times: once its current multiplicity is at most `r-1`, only
that many members containing it remain, and multiplicity only decreases.
Consequently all deletions together can make at most `(r-1)T` charges.

If every member were deleted, `(1)` would imply

```text
|F| (floor((r-1)T/(B+1))+1) <= (r-1)T.
```

But `|F|>B` gives `|F|>=B+1`, while for every nonnegative integer `X`,

```text
(B+1)(floor(X/(B+1))+1)>X.
```

Taking `X=(r-1)T` is a contradiction.  Hence a nonempty subfamily remains,
and every member has the asserted `d_r` labels of multiplicity at least `r`.

By the proved reuse-core dictionary, each such label is a kernel basis whose
members lie on one exact size-`k` collision line.  Distinct labels through a
fixed selected member define distinct lines, so label multiplicity supplies
the required lower bound on line population within the retained subfamily.
Substitution in `(RH)` gives the table and the last positive thresholds.
