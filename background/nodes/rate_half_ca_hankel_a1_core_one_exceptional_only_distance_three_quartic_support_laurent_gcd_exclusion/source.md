# Published input

P. Corvaja and U. Zannier, *Greatest common divisors of `u-1`, `v-1` in
positive characteristic and rational points on curves over finite fields*,
J. Eur. Math. Soc. 15 (2013), 1927--1942, Theorem 2.

For a smooth projective absolutely irreducible curve `X` in characteristic
`p`, let `u,v` be multiplicatively independent rational functions modulo
constants, with nonzero differentials. Let `S` be their zeros and poles and
`chi=|S|+2g-2`. Then

```text
sum_(z outside S) min{ord_z(1-u),ord_z(1-v)}
 <=max{
   3(2 deg(u)deg(v)chi)^(1/3),
   12 deg(u)deg(v)/p
 }.
```

Primary source: https://ems.press/journals/jems/articles/4076

The application here uses `u=x^N`, `v=y^N`, `deg x=deg y=3`, and
`chi<=18`. It does not use the weaker bidegree-dependent Stepanov constant
from the earlier subgroup-curve nodes.
