# Proof

The forced loop product is `-d^2`, proving `(KB41FL-1)`.  Project the exact
mate `m` into each irreducible cubic component of the representative common
quotient.  Euler's criterion gives `(-m)^((p^3-1)/2)=-1` in both, so
`T^2+m` is irreducible and adjoining `theta` produces a field of degree six
over the deployed base field.

After removing the forced loop record, the remaining products are

```text
-ce, -cf, -theta*e, delta*theta*f, ef, -ef.
```

Their factors `X-uZ` give `(KB41FL-2)`.  Build `E_0,E_1,E_2` directly by
tower-field arithmetic.  Each equation has 17 terms with leading monomial
`e^4f^4`.

For each cubic base component and each `delta`, exact grevlex Buchberger
reduction reaches a nonzero constant.  The pair counts are 57 for
`delta=-1` and 55 for `delta=+1`; monic normalization gives `1`.  Hence all
four component/parity ideals are raw unit ideals and both cells are empty.
QED.
