# Proof

The symmetric tower gives a finite algebra

```text
A = F_p(x)[r,y]/(P(y,x), Q(r,y,x))
```

of dimension six for BC- and four for BC+ on its registered chart.  Substitute
`b`, `c`, `r`, and `t=(epsilon_1 epsilon_2)r^2` into the exact selected
product-rank cofactor.  If that element vanishes at a specialized point of
the finite algebra, its multiplication norm to `F_p(x)` vanishes at the
corresponding `x`.

Exact `python-flint` arithmetic factors each norm numerator over
`F_2130706433`.  For BC- the factor degrees/multiplicities are `(2,2)` and
`(1,10)`; the linear factor gives only `x=1`.  For BC+ they are `(3,2)`,
`(2,4)`, and `(1,4)`; the linear factor gives only `x=-1`.  At `x=1`, six of
the nine BC- tower guards vanish.  At `x=-1`, four of the six BC+ guards
vanish.  Thus no norm root lies on the deployed tower chart, and consequently
the selected cofactor is nonzero at every deployed base-field point.
