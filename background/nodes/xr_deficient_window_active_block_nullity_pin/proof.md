# Proof

The primitive Pade-pencil router proves

```text
c<=d-ell-g.                                         (1)
```

Every `D`-local target has at least two selected slopes. Their active-defect
blocks are disjoint, each has size `r`, and both lie in `D subset G_d`.
Therefore

```text
g>=|D|>=2r.                                         (2)
```

Combining `(1)` and `(2)` gives

```text
c<=d-ell-2(h-d)=3d-2h-ell,
```

which is `(ABN1)`.

At the boundary, substitute `d=h-2ell-1` to obtain

```text
c<=h-7ell-3.                                        (3)
```

For `h=2^33+1`, the remainder in `h-4=7ell_0+5` makes the right side of
`(3)` equal to `6`. For `h=2^32+1`, the remainder is one and the right side
is `2`. This proves `(ABN2)`. QED.
