# Proof

For each stated route, let `N(x,s,p,w)` be the assignment-specific descended
degree-67 numerator and let `w=-U/V` be exact reconstruction on the named
`V!=0` chart. Since `deg_w N=15`, evaluate

```text
H(x,s,p) = V^15 N(x,s,p,-U/V)
```

by homogeneous Horner reduction modulo the route Groebner basis. This is
equivalent to `N=0` on `V!=0` and introduces no denominator chart.

The `F05-R02` and `F07-R02` remainders have total degree 39 and respectively
1885 and 1890 terms. The `F06-R20` remainder has degree 41 and 1945 terms.
After adjoining each exact remainder, the resulting ideal remains
dimension one and nonunit. Sequential reduction of the complete square-free
transported named localizer reaches zero at factor 15 in all three cases.
Therefore no point of any field extension can lie in the route ideal while
all named factors are nonzero. QED.
