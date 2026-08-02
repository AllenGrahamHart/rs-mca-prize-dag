# Proof

Write

```text
A_2=d_0+d_1W+d_2W^2,
A_0=e_0+e_1W+e_2W^2,
B_1=beta_0+beta_1W.
```

Direct substitution into `X^4H(T,-1/X)` gives `(KBC58R-2)`.  In particular,
the map is an invertible involution, preserves the bidegree bound, and sends
nonzero `B_1` to nonzero `B_1'`.

Set `lambda'=lambda^(-1)`.  Coefficient reversal gives

```text
A_j'(lambda')=lambda'^2 A_j(lambda),
B_1'(lambda')=-lambda' B_1(lambda).
```

Since `z'=-1/z`, one has `q'=z's=-q/lambda=-q lambda'`.
Substitution proves both identities `(KBC58R-3)`.  Every actual complete
source record therefore transports to a record with the same target edge,
and conversely because the transformation is involutive.

All source lifts in the fixed-point-free deck support are nonzero.  For
nonzero labels `a,b`,

```text
a^(-1)-b^(-1)=-(a-b)/(ab),
a^(-1)+b^(-1)=(a+b)/(ab).
```

Hence distinctness and opposite-pair guards are preserved.  Inversion is a
projectivity commuting with the normalized deck `X -> -X`, so the complete
source-facet partition and outside matching incidences transport
bijectively.  Target representatives, products, sums, and target guards are
unchanged.

In the cell-5 root display, direct evaluation of `z -> -1/z` fixes the `AC`
relative sign, replaces `r` by `-1/r`, flips the relative sign on `AB-`, and
replaces `t` by `-1/t`.  The loop's two source lifts give the same antipodal
target record and `q=0`, so its canonical root remains `1`.  This proves
`(KBC58R-4)` without changing the matching cell.  Transposing the identical
`AB+` roles gives the same conclusion in cell `8`.

The parent exclusion proves the four rows with `epsilon_2=-1` empty.  If a
row with `epsilon_2=+1` existed, `(KBC58R-1)--(KBC58R-4)` would produce an
admissible parent-row packet, a contradiction.  Thus all eight rows in
`(KBC58R-5)` are empty. QED.
