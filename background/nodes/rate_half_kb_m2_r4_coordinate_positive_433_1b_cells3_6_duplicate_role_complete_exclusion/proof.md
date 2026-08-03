# Proof

In cell 3 the common assignment is

```text
singleton AB; pairs (LA,AC), (BC+,BC-),
```

while cell 6 has

```text
singleton AC; pairs (LA,AB), (BC+,BC-).
```

Thus exchanging common roles `AB,AC` sends cell 3 to cell 6.

Write the cell-3 source roots at roles

```text
LA, AB, AC, BC+, BC-
```

as

```text
1, t, epsilon_1 iota, r, epsilon_2 iota r.
```

The common target products and source-weighted sums `q=z(a+b)` are

```text
LA:  (-1,0),
AB:  (b,t(1+b)),
AC:  (c,epsilon_1 iota(1+c)),
BC+: (bc,r(b+c)),
BC-: (-bc,epsilon_2 iota r(b-c)).                (1)
```

After `B'=C,C'=B`, cell 6 has the first source sign unchanged.  Its `BC-`
target sum is `C-B=-(B-C)`, so choosing the deck-conjugate source root flips
the second sign.  With `(epsilon_1',epsilon_2')=(epsilon_1,-epsilon_2)`, the
cell-6 rows are exactly `(1)` after the role permutation

```text
LA fixed, AB' <- AC, AC' <- AB, BC+ fixed, BC- fixed.
```

The quotient labels `1,t^2,-1,r^2,-r^2` undergo the same permutation.
Consequently both complete positive Vieta rows at every common role are
preserved, not only their product halves.

The canonical active edge signs are

```text
AB=AC=BF=DE=DF=1,       CF=sigma_c, EF=sigma_o.
```

After exchanging `B,C`, gauge the three outside vertices `D,E,F` by
`sigma_c`.  This returns every active sign to the same canonical value, so
both cycle invariants and the lane `(sigma_c,sigma_o)` are fixed.  In target
coordinates this is `(KBP1B36-T-1)`.  The outside product records become

```text
de,de,-de,df,sigma_o ef,sigma_c cf,bf,
```

and the signed squared sums undergo the same transposition of the last two
positions.  All other rows are fixed.  Permuting `b,c`, and multiplying
`d,e,f` by one unit preserves nonzero and pairwise-not-opposite target guards.

For any missing index, deleting its row before the transposition is the same
as deleting the transposed index afterwards.  The induced permutation of the
six compact positions sends a perfect matching to another canonical perfect
matching.  Exact enumeration gives a bijection of all `7*15=105`
missing-record/matching cases.  The source-sign flip and target-lane identity
are bijections, so all 1,680 principal cell-6 systems map to the full 1,680
principal cell-3 systems.  The latter are empty by
`(KBP1B3-COMPLETE-1)`.

Finally, the exact rank-drop common exception classifier lists cell 6 among
the cells whose guarded rank-drop ideal is the unit ideal in all four source
signs.  Thus the rank-drop and rank-five branches are both empty in cell 6.
Together with the parent theorem for cell 3, orbit `[3,6]` is empty. QED.
