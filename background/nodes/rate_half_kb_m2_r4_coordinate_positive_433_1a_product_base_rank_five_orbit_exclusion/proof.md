# Proof

Swapping the identical `AB+` roles identifies cells `4` with `7` and `5`
with `8`, so it suffices to treat cells `4,5`.

If the cell-4 product block had rank below five, `(KBPB5-2)` would be a
homogeneous linear system in the nonzero pair `(b,c^2)`.  Its determinant is
`B^2-A^2=(B-A)(B+A)`.  Direct expansion gives

```text
B-A=2(R-1)(T-1),       B+A=4(R+T).
```

The guards give `R!=1`, `T!=1`, and `R+T!=0`, while the deployed
characteristic is odd.  Thus the determinant is nonzero, contradiction.

For cell 5, assume both equations `(KBPB5-4)` vanish.  Multiply the first by
`cC+B` and twice `S` times the second, then subtract.  This gives the left
side of `(KBPB5-5)`.  The identity

```text
B-C=2S,       B^2+C^2-4S^2=2BC
```

expands it to `cBC(c+1)^2`.  Here `c`, `R+/-1`, `T+/-1`, and `c+1` are
all nonzero guards, so this too is impossible.  The prior theorem supplies
the other three role orbits, and independence of the loop row raises product
rank five to base rank six. QED.
