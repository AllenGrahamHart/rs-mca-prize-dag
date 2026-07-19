# Proof

The degree table in the split-fiber atlas gives `(LGA1)` directly: all four
cycle chambers, the first `K_4-e` chamber, the `K_4` chamber, both path
chambers, and the triangle-plus-singleton chamber are constant/linear. The
three pendant chambers and the second `K_4-e` chamber contain a degree-two
edge. Thus the count is `4+1+1+2+1=9` versus four.

For one of the nine linear chambers, write

```text
B(X)=B_0+X B_1.
```

At least one edge is linear, so `B_1!=0`. Also `B_0!=0`: every listed linear
chamber has at least two tight linear factors with distinct selected edge
roots, and those factors cannot both have zero constant term. The two
bivectors are independent.
If a constant edge is present, proportionality would force `B_1=0` on a
nonzero coordinate of `B_0`; if every edge is linear, proportionality would
give all six factors one root.

The Plucker identity and odd characteristic now give

```text
B_0 wedge B_0=B_0 wedge B_1=B_1 wedge B_1=0.
```

As in the `K_4` Grassmann-line theorem, the two endpoint planes are distinct
and meet in one line. Hence there are independent `w,u,v` satisfying
`(LGA2)`. The Plucker gate puts `A(X)` in the represented moving plane, so
the fixed three-space `<w,u,v>` has a one-dimensional annihilator and gives
a constant relation among the `A_i`.

We use one degree-pattern criterion to determine its support. If the
annihilator coefficient `lambda_i` vanishes, then the three vectors
`(w_j,u_j,v_j)` for `j!=i` are linearly dependent. Writing their common
linear equation as

```text
a w_j+b u_j+c v_j=0
```

shows that the three induced edge factors `b_jk` are either all constant or
all linear with one common root. This is the calculation in the `K_4`
parent: for `c!=0`, every factor is a scalar multiple of
`1-(b/c)X`; for `c=0`, every nonzero factor has root zero.

Inspect the five type rows. In every complementary triangle of the cycle,
linear `K_4-e`, `K_4`, and triangle-plus-singleton types, the edge degrees
are mixed constant/linear, or the triangle contains at least two tight linear
factors with distinct selected edge roots. Thus the three factors can be
neither all constant nor linear with one common root. Therefore no
`lambda_i` vanishes, proving `(LGA3)`. The `K_4` case also follows from the
parent theorem. This argument does not assume that a slack quotient root is a
new domain point.

In the path type, the complementary `013` triangle has three tight constant
edges. Its triangle identity is exactly

```text
q_13 A_0-q_03 A_1+q_01 A_3=0,
```

with all three coefficients nonzero. Since the fixed annihilator is unique,
this is `(LGA4)` and its `A_2` coefficient is zero. More explicitly,
`A_0,A_1,A_3` span a two-dimensional polynomial space: the displayed
relation exists, while two of these pairwise-coprime nonconstant locators
cannot be proportional. The locator `A_2` has degree `d`, whereas the other
three have degree `d-1`, so it is independent of that space. Hence the four
coordinate polynomials have exactly one constant relation, which must be the
annihilator of the three-space containing `A(X)`.

For `d>=3`, every locator appearing in these relations has a nonempty root
block. A one-term subsum is nonzero. A two-term subsum would make two
pairwise-coprime split locators proportional. A three-term subsum of
`(LGA3)` would force the remaining nonzero term to vanish. Thus every printed
relation is nondegenerate on its support.

Finally the normal-form partition identity proves `(LGA5)`. The exact
exceptional degrees are the sums `n_1+n_2+n_4` from the five incidence rows:
`4,6,8,3,5`. QED.
