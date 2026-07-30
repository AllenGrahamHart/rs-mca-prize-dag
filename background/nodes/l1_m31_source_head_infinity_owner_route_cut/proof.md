# Proof

Let `W` be the linear direction space of the normalized-label affine class.
For polynomials of degree below `d`, homogenized evaluation at infinity is the
linear functional

```text
ell_infinity(f)=[X^(d-1)]f.
```

Hence fixing a source head is exactly intersecting the affine class with one
parallel hyperplane `ell_infinity=c`. This explains the rank loss within one
head fiber, but it does not count the collection of parallel fibers.

The full-projective-line deletion recurrence starts from a fixed received
table `u`. For a projective evaluation line it partitions coordinates by
their normalized labels and counts exact pairs

```text
(f,x),  f(x)=u(x).
```

After adjoining infinity there is one new coordinate and one fixed value
`u_infinity`. Its complete incidence contribution is precisely

```text
#{f:ell_infinity(f)=u_infinity}.
```

Members with any other head contribute zero incidences at that coordinate.
Changing `u_infinity` selects a different received table, so bounds obtained
from different choices are not cells of one first-match partition. Therefore
the recurrence pays at most one selected head fiber and cannot be summed over
the head spectrum without an additional ownership theorem.

For the second assertion, fix any integer `D`. Create `D` abstract neighbors,
give neighbor `j` its own head `gamma_j`, and give it `4980` cores unused by
all other neighbors. Every head fiber then has size one, every fixed core has
load one, and every colored `(core,gamma_j)` cell has load one. These satisfy
the three proved upper caps for every `D`, while the colored-core incidence
count and the number of private colored cells are both exactly `4980D`.
Consequently those local inequalities have no finite aggregate consequence.
At `D=215793` the model has `1,074,649,140` private cells, which in particular
exceeds the proved floor `ceil(215793*4980/15)=71,643,276`. QED.
