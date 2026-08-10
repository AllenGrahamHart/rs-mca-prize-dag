# Proof

Evaluate `A(lambda_missing)` in each exact degree-six/degree-four symmetric
tower algebra and take the determinant of its multiplication map to
`F_2130706433(x)`.  Exact factorization and root extraction give no BC- root
inside the tower chart.  For BC+ the only chart-level roots are

```text
x = 153731577, 583634934, 1547071505.
```

Specialize both tower relations at each value and extract every base-field
`y` and `r` root.  The first value has no base-field `r` lift.  Each of the
other two values has two lifts in each epsilon row, giving 16 points in all.
Direct substitution verifies the six original common equations at every
point.  It also gives `b=c` and zero original common guard at every point.
Therefore none is a guarded source point.

The norm criterion is necessary for any zero of `A(lambda_missing)`, the
tower root extraction is exhaustive over the base field, and the parent
tower covers every original guarded source.  Hence no guarded base-field
source lies on the reconstruction-denominator boundary.
