# Proof

Write the collapsed coefficient polynomials as

```text
A2(X) = z0 + z1 X,
A0(X) = z3 + z4 X.
```

The pinned equation `q3` says

```text
A0(lambda) = de A2(lambda),  lambda = -t^2,
```

and admissibility includes `A2(lambda)=a2m != 0`.

Consider the first polynomial of a finite matching pair with record `Y`:

```text
P_Y(u) = (z3-Y z0) + (z4-Y z1)u.
```

If its linear coefficient vanished, the finite-root equation would force its
constant coefficient to vanish as well. Hence `A0=Y A2` coefficientwise.
Evaluation at `lambda`, followed by the pinned equation and
`A2(lambda) != 0`, would give `Y=de`.

For pairing 0 the relevant first records and their differences from `de`
are

```text
q4:  Y=be,   Y-de = e(b-d),
q5:  Y=-de,  Y-de = -2de,
q6:  Y=-df,  Y-de = -d(e+f).
```

The target nonzero and square-distinct guards make all three displayed
differences nonzero; the field characteristic is odd. The finite pairs are
`q4,q5` in `FFI` and `q4,q6` in `FIF`, proving the claim.

Finally, two linear polynomials with first slope nonzero have a finite common
root if and only if their coefficient determinant vanishes: the first
polynomial fixes the root, and the determinant is exactly the condition that
the second vanishes there. QED.
