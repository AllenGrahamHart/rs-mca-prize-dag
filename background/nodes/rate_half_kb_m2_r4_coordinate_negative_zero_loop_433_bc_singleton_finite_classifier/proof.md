# Proof

For cell `12`, parity reduction with `x=t^2,y=r^2` gives `(KBZ433B-1)`.
On its two branches the second product row gives respectively

```text
x=by,                         x=y/b.                (1)
```

After `(1)`, the first q row is linear in `r` and the second is linear in
`t`.  Substitution of those two rational values into `r^2=y,t^2=x` gives a
zero-dimensional ideal in `(y,b)`.  Lex elimination has degree `16` in the
same-sign rows and degree `12` in the opposite-sign rows.  Its base-field
root gcd has degree `6` and `5`, respectively.  Exact specialization in
`y`, rational reconstruction, and original-equation replay leave two
guarded packets per branch in every row.

The lost `x` ideal is the unit ideal after guard factors are removed.  Every
lost `r` point has `y=+/-1`.  Every remaining lost-`t` projection either has
`b in {0,+/-1}` or `y in {0,+/-1}`, or has zero coefficient and nonzero
constant on the prior `r` row.  Thus the cell-12 census is exhaustive.

For cells `13,14`, factor the first product row as `(KBZ433B-2)`.  The second
product row is linear in `x`; after its substitution the first q row is
linear in `b`.  In a same-sign row this determines `b` as a Mobius function
of `r`; the last q row determines `t`, and `t^2=x` leaves a split quadratic
in `r`.  Both roots reconstruct guarded packets on each branch.  In an
opposite-sign row, the first q row instead reduces to `r-i` or `r+i`, so
`r^2=-1` and the label guard fails.

The only cell-13/14 lost-`x` projection has `b=0,r=+/-1`; the later same-sign
linear solves have no base-field lost point.  Hence all branches are
exhausted.  Summing gives `(KBZ433B-3)`.  Original-equation replay proves
every admitted packet.  Adding the earlier exact orbit censuses gives the
64-packet full common atlas. QED.
