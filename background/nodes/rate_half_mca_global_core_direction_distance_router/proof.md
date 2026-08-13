# Proof

Choose for each selected slope `gamma` a shortened explanation and an exact
pair-noncontained agreement support of size `m=d+s`.  Its error has weight at
most `t=R-d` and syndrome `y_0+gamma y_1`.

If `y_1=0`, then the shortened direction is a codeword.  Subtracting its
multiple from any slope explanation would simultaneously explain the base
and direction on the same support, contradicting pair noncontainment.  Thus
`y_1!=0`.

The proved directional Johnson-ray theorem applies on the complete shortened
domain of size `N=R+s`.  Any `R` parity-check columns span syndrome space, so
`d_U(y_1)<=R` and `j>=0`.  Its denominator becomes

```text
(N-t)^2-N(N-d_U(y_1))
 = (d+s)^2-(R+s)(s+j)
 = d^2-(R-2d)s-(R+s)j.
```

Its numerator is `(R+s)(d-j)`, proving the displayed bound whenever the
denominator is positive.

For integer budget `B`, positivity is equivalent to

```text
j <= floor((D_s(0)-1)/(R+s)),
```

and the floored rational bound is at most `B` exactly when

```text
(R+s)(d-j) < (B+1)(D_s(0)-(R+s)j).
```

Solving this strict integer inequality and imposing `j<=d-1` gives the
contract formula.  Exact scans through the first nonpositive dimension give
the official endpoints and maxima.  No affine-incidence theorem is used.
