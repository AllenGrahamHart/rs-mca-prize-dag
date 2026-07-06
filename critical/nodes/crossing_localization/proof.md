# crossing_localization proof

Fix a row and let `B_C(a)` be the certified unsafe count at integer grid
index `a`. The count is finite and integer-valued. It is nonincreasing in
`a` because increasing the agreement index only removes admissible witnesses
from the counted set.

Assume the corridor arithmetic supplies integer endpoints `a_lo <= a_hi`
with

```text
B_C(a_lo - 1) > B*
B_C(a_hi) <= B*.
```

Define `a*` to be the first integer `a` in this interval with
`B_C(a) <= B*`. This first index is unique by definition, and monotonicity
gives

```text
B_C(a* - 1) > B* >= B_C(a*).
```

Thus the analytic crossing problem has been reduced to checking the finitely
many integer points in the corridor. If the real-valued corridor has width
`w`, it contains at most `ceil(w) + 1` integer grid points. In the recorded
corridor rows this is the advertised two-to-three point list.

No asymptotic estimate is used in this reduction; only monotonicity,
integrality, and the already-computed corridor bracket are required.
