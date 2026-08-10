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
vanish.

The parent symmetric-tower theorem includes an independent exact
chart-coverage certificate: adjoining
`b*c*(b+c)*(bc-1)*(bc+1)=0` to each original common ideal localized by its
source/target guard gives the unit ideal.  Therefore no original guarded
source point lies over `x=1` or `x=-1`.  Since every possible base-field zero
of the selected cofactor would force one of those two norm roots, no guarded
base-field source point lies on the selected-cofactor fiber.
