# Proof

For a literal assignment with common internal vertex `a`, the negative
source candidate has

```text
V=(f+gW, m(1-W), -(g+fW)),
f=cd+w,  g=-1-wcd,  m=-(c+d)(1+w).
```

The incidence label `z` is obtained directly from `V(a,z)=0`. The two
source edges determine the three target coordinates at `z`. Together with
the two forced q-membership equations this gives the five-row, four-column
linear reconstruction system compiled in
`aligned_negative_literal_identity.sage`.

The generic selected minor omits row 2 and contains `c+d`; the complementary
minor omits row 3 and contains `cd+1`. The pinned output records the complete
determinant factorization for every cell. Comparing the factorization of the
unused consistency equation with the selected determinant removes only
factors already inverted on that chart. This leaves one fixed-moving or two
moving-moving survivor components.

For each component, the compiler divides both norm evaluations by their
forced square, forms the monic residual quartic, and verifies `(KBNL-2)` by
exact ideal reduction. On the generic chart it then substitutes `d=-1/c`
and verifies `(KBNL-3)` by a second exact component reduction. On the
sum-zero chart, exact reduction modulo the component and `c+d` proves
`(KBNL-2)`; its zero together with `cd!=1` gives `cd=-1`, hence `c^2=1`.

All 24 cells pass. Fixed-moving cells contribute 16 component checks and
moving-moving cells contribute 16, for 32 total. The two longest generic
moving cells are pinned separately because they exceeded the first
330-second orchestration guard; both completed under the extended
900-second bound without changing the compiler.
