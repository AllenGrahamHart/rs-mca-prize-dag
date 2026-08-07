# Proof

If two nonzero polynomials differ by a scalar, their logarithmic derivatives
agree wherever both polynomials are nonzero. Evaluating at `W=0` proves
`(KBLD-1)` on the stated constant-nonzero chart. Direct differentiation of
`g=u^2-Wv^2` gives

```text
g(0)=u0^2,    g'(0)=2u0u1-v0^2,
```

and division by `u0^2` proves `(KBLD-2)`. For a linear factor `W-a`, the
same ratio is `-1/a`; summing with the printed multiplicities gives the
expected side.

The exact Sage replay constructs these six observed contributions and the
24 expected contributions in the source rational function field. It clears
denominators, removes only source named factors, descends symmetrically from
`c,d` to `s=c+d,p=cd`, and factors both numerator and denominator over
`Q`. The numerator factorization has one degree-67 factor. The only
nonnamed denominator factors have degrees `7,7,11,11`, all squared.

If one of those factors vanishes, the point belongs to its explicit
denominator branch. Otherwise all divisions are valid and the degree-67
numerator must vanish. These cases are exhaustive. QED.
