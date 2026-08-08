# Proof

In cell 4 the common assignment is

```text
singleton AB; pairs (LA,BC+), (AC,BC-),
```

while cell 7 has

```text
singleton AC; pairs (LA,BC+), (AB,BC-).
```

Thus exchanging common roles `AB,AC` sends cell 4 to cell 7.

Write the cell-4 source roots at roles

```text
LA, AB, AC, BC+, BC-
```

as

```text
1, t, r, epsilon_1 iota, epsilon_2 iota r.
```

The common target products and source-weighted sums `q=z(a+b)` are

```text
LA:  (-1,0),
AB:  (b,t(1+b)),
AC:  (c,r(1+c)),
BC+: (bc,epsilon_1 iota(b+c)),
BC-: (-bc,epsilon_2 iota r(b-c)).                (1)
```

After `B'=C,C'=B`, cell 7 has the first source sign unchanged.  Its `BC-`
target sum is `C-B=-(B-C)`, so choosing the deck-conjugate source root flips
the second sign.  With `(epsilon_1',epsilon_2')=(epsilon_1,-epsilon_2)`, the
cell-7 rows are exactly `(1)` after the role permutation

```text
LA fixed, AB' <- AC, AC' <- AB, BC+ fixed, BC- fixed.
```

The quotient labels `1,t^2,r^2,-1,-r^2` undergo the same permutation.
Consequently both complete positive Vieta rows at every common role are
preserved, not only their product halves.

The canonical active edge signs are

```text
AB=AC=BF=DE=DF=1,       CF=sigma_c, EF=sigma_o.
```

After exchanging `B,C`, gauge the three outside vertices `D,E,F` by
`sigma_c`.  This returns every active sign to the same canonical value, so
both cycle invariants and the lane `(sigma_c,sigma_o)` are fixed.  In target
coordinates this is `(KBP1B47-T-1)`.  The outside product records become

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
are bijections, so all 1,680 principal cell-7 systems map to the full 1,680
principal cell-4 systems.  The latter are empty by
`(KBP1B4-COMPLETE-1)`.

Finally, the exact product-rank-drop complete theorem excludes the full
deployed rank-drop branch, including cell 7. Thus the rank-drop and rank-five
branches are both empty in cell 7.
Together with the parent theorem for cell 4, orbit `[4,7]` is empty. QED.
