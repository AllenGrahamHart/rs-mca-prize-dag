# Proof

The parent atlas and common compiler enumerate exactly fifteen assignments
of the five roles to two opposite source pairs and a singleton, and four
root-sign rows per assignment.  This gives sixty rows.

The product block has five rows and six columns.  Therefore all six of its
`5 x 5` cofactors vanish if and only if its rank is at most four.  The full
common matrix has ten rows and eight columns, so its rank is at most seven
if and only if all 45 choices of eight rows have zero determinant.  These
two determinantal conditions remain valid on every rank stratum; no pivot
minor is divided out.

The product compiler forms and guard-strips all six cofactors in each cell.
Guard stripping preserves their common zero set after adjoining `zH-1`.
The exact common classifier reconstructs every root-sign matrix, asks
Singular for all 45 maximal minors, adjoins the six product cofactors and
the inverse guard, and computes a standard basis over the deployed field.

The generated certificate contains one complete row for every element of

```text
{0,...,14} x {-1,+1} x {-1,+1}.
```

Its twenty rows in cells `0,1,2,3,6` have dimension `-1`, basis size one,
and terminal basis `{1}`.  Each remaining row has dimension zero, with the
basis-size ledger in `(KBP1BRD-5)`.  These are algebraic-closure statements
because unit-ideal and Krull-dimension computations over the deployed
prime field already decide the corresponding base-changed affine schemes.
This proves the claim. QED.
