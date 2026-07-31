# Proof

The full signed internal `DE/DF` records form one forced-record type for
each `tau_0` parity.  Choose `DE=d e=m`.  The unforced products are

```text
cm/d, cf, -m, df, -df, tau_0*mf/d.
```

Their factors give the rational residual sextic.  Multiplication by `d^2`
clears its two linear denominators and gives `(KB41S0I-1)`.  The scaling is
reversible on `d!=0` and commutes with the binary action.

For each parity, apply `E_0,E_1,E_2`.  Sparse cubic-field arithmetic gives
fourteen monomials per equation.  In each cubic component, exact grevlex
Buchberger reduction completes after 406 S-pairs.  The one-term monic basis
element at exponent `(0,1)` is `f`, so the ideal contradicts the required
guard `f!=0`.

The form depends on the common row only through `b,c,m` and the product
involution.  Their exact component data are row-independent, so both parity
deletions apply to all four rows.  The binary-sextic compiler proves that
the complete frontier consists of `6+10+4=20` forced-record cells per row.
The current and preceding nodes delete all six `S0`, all ten `S1`, and all
four `S2` cells in each of four rows.  Therefore the 80-cell product
frontier is empty.  QED.
