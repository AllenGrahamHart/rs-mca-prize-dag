# Proof

One antipodal edge orbit over a complete quotient fiber contributes the
same unordered target edge at both deck-related source points, hence target
edge weight two.  If the same antipodal type occurred over two quotient
fibers, that target edge would have weight at least four and defect at least
`binom(4,2)=6`.  The proved component defect budget is three.  Therefore no
antipodal type repeats, proving `(KBPQ-1)` without any product-injectivity
assumption.

At a positive common fiber `kappa=[u:v]`, the exact homogeneous sum equation
is

```text
u v B_1(kappa)+q_kappa A_2(kappa)=0,              (1)
```

with `A_2(kappa)!=0`.  At either ramified quotient value `uv=0`, star
transport fixes the source point and forces an antipodal target edge.  At a
nonramified loop, `q_kappa=0` and `uv!=0`, so `(1)` forces
`B_1(kappa)=0`.

Suppose `B_1=0`.  Equation `(1)` makes every nonramified common edge
antipodal, while the positive ramification rule makes either ramified common
edge antipodal as well.  Thus all five common fibers are loops.  There are
only three antipodal target types, so one repeats, contradicting
`(KBPQ-1)`.  Hence `B_1` is a nonzero homogeneous linear form.  It has one
projective root, proving that at most one loop is nonramified.  The stated
two- and three-loop ramification pins follow.

For target-pair degrees `d=(d_0,d_1,d_2)`, the five common edge orbits obey

```text
2l_i+sum_(j!=i)m_ij=d_i,       sum_i l_i+sum_(i<j)m_ij=5. (2)
```

Enumerate `l_i in {0,1}` and nonnegative `m_ij`, then quotient by the swap
of the two equal-degree pairs.  For `(4,4,2)`, `(2)` gives six labeled
solutions in five orbits; for `(4,3,3)` it gives seven labeled solutions in
five orbits.  Their representatives and orbit sizes are exactly
`(KBPQ-2)`.  The checker exhausts the finite integer ranges and replays every
degree equation. QED.
