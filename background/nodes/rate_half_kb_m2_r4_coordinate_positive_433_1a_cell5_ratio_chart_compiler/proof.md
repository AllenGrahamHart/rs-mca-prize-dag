# Proof

The common-minor parent constructs the three `C1` equations exactly over the
deployed field.  The global product-base theorem supplies `rank B=6`, so the
pivot-chart reduction identifies their vanishing with the common rank-seven
condition on this chart.

Every atomic factor used in the compiler divides the declared guard product.
It is therefore a unit in the localized coordinate ring.  Exact polynomial
division removes only `t-r` from the first fast-stripped minor and no factor
from the other two, proving `(KBRAT-2)` without changing the localized ideal.

The guards include `b!=0` and `c!=0`.  Hence `x=c/b` is an invertible change
of variables, with inverse `c=bx`, and `b^2` is a unit.  Direct collection in
`b` gives degrees `1,2,2` and the coefficient ledger `(KBRAT-4)`.

Write `L0=a0+a1b`.  On `a1!=0`, `L0=0` is equivalent to
`b=-a0/a1`.  Substitution in `Lj=qj0+qj1b+qj2b^2` and multiplication by
`a1^2` gives exactly

```text
a1^2 Lj(-a0/a1)=qj0 a1^2-qj1 a0 a1+qj2 a0^2=Ej.
```

Thus `(KBRAT-5)` is necessary and sufficient on the generic branch.  If
`a1=0`, the equation `L0=0` is exactly `a0=0`; no division is permitted and
the compiler retains `L1=L2=0`.  These two branches exhaust the chart. QED.
