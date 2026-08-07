# Proof

Replace the parameter `b` in the canonical `F00` system by `b'=b^-1`. Its
endpoint registry is

```text
v0'=2, v1'=1/2, v2'=b^-1, v3'=b.
```

The source pair used by `F00(b')` is

```text
{E01',E02'} = {{2,1/2},{2,b^-1}},
```

which is exactly `F01(b)`. The unordered endpoint carrier is

```text
{2,1/2,b',b'^-1}={2,1/2,b,b^-1}=J_0(b).           (1)
```

The source reconstruction is determined by the selected pair, `q`, and `w`.
Thus the reconstructed source form for the left side of `(KBFI-1)` is the
same form as the right side, with coefficients related by literal
substitution. No endpoint coordinate transformation is being asserted.

The three targets `R02`, `R11`, and `R20` depend only on the two roots
`c,d` of `q`; they do not depend on the name assigned to the reciprocal pair
`{b,b^-1}`. The colored quotient identities use the quotient locators on the
underlying label sets and their complement. Equation `(1)` leaves those sets
and locators unchanged. Every label-distinctness and reconstruction localizer
is likewise carried to the corresponding factor under `b -> b^-1`; the map
is involutive and introduces no omitted chart on `b != 0`.

Consequently `(KBFI-1)` is an identity of the complete named-open systems,
including both quotient equations rather than only the four q-slice
equations. The map `b -> b^-1` is a bijection of
`F_(2130706433^6)^*`. A point of `F01(b)-Rxx` would therefore give a point of
`F00(b^-1)-Rxx`. The three canonical fixed-moving leaves exclude those
points for `R02`, `R11`, and `R20`, proving `(KBFI-2)`. QED.
