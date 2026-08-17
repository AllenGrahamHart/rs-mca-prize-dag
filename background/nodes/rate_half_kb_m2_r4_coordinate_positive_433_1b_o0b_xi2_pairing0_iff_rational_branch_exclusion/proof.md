# Proof

The `q4` infinity equations are

```text
k5 - be k2 = 0,
k5 - cf k2 = 0.
```

Their difference gives `(be-cf)k2=0`.

If `k2=0`, either equation gives `k5=0`. The proved collapsed-common
exclusion says that no admissible common base point satisfies these two
equations, so this branch is empty.

Hence a survivor must have `k2 != 0`, `be=cf`, and
`k5=be k2 != 0`. Since `b,c,a2m` are also guarded nonzero, the infinity
equations, the record collision, and `q3` uniquely give

```text
e = k5/(b k2),
f = k5/(c k2),
d = a0m*b*k2/(k5*a2m).
```

Substitute these values into `q7` and clear the nonzero denominator
`b*k2*k5`. For the finite pairs `q5,q6`, scale each quadratic by its
nonzero record denominator and retain its exact quadratic resultant. These
three base-only equations are necessary for an `IFF` solution; allowing
their resultant roots at infinity only enlarges the locus.

Adjoining the cleared equations to the checked 21-element common basis gives
the following exact stages:

```text
q7: dimension 0, size 42
q5: dimension 0, size 44
q6: dimension 0, size 44
```

Sequential saturation by all 16 route guards becomes unit at guard index 5,
`b+1`. The denominator guards `k2,k5,a2m` and the final six-cofactor
rank saturation remain unit. Thus even the necessary superset is empty.
Both branches are empty, proving `IFF` empty. QED.
