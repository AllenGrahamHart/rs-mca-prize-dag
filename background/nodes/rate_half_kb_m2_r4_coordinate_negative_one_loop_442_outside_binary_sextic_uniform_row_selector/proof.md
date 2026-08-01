# Proof

Use the six-dimensional quotient basis `(1,b,b^2,r,br,t)` in each root-sign
row.  Reconstruct `c` through its proved unit denominator and form the
multiplication matrices of

```text
Alpha=-b(c+b^2),
Beta=b^2(c-b^2-2bc),
Gamma=c+2b-b^2.
```

Expand the degree-six coefficient action `(KB41EV-2)` using multiplication
matrices, subtract `Delta^3` on the diagonal, and take rows and columns
`0,1,2`.  The determinant is an element of the rank-six quotient.  Taking
the determinant of its multiplication matrix gives `1133299039` modulo
`2130706433` in each of the four sign rows.  This proves `(KB41US-1)` and
shows that the three selected rows are independent.

The eigenvalue compiler proves that the full seven-row operator has rank
three.  Therefore the selected independent rows span its row space, proving
the equivalence `(KB41US-2)`. QED.
