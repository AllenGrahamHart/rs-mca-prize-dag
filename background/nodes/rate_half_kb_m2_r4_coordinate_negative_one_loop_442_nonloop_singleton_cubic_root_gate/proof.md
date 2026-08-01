# Proof

Put `x=r^2`, `A=x^2-6x+1`, and `B=(x+1)^2`.  The product minor using the
loop, both `AB` records, and the nonsingleton `AC` record is

```text
b^2 A+bB-c(bB+A)=0.                              (1)
```

If its coefficient of `c` and its constant part both vanish, then

```text
bB+A=0,       bA+B=0.
```

Their `b`-resultant is `A^2-B^2=-16x(x-1)^2`.  The first factor contradicts
`r!=0`, and the second collides the labels `r^2,-r^2` with `1,-1`.
Consequently `bB+A` is nonzero on the guarded locus and `(1)` gives
`(KB41C-4)`.

Substitute `(KB41C-4)` into the q weld involving the nonsingleton `AC`
record.  After removing the guarded factor
`b^2 r(b-1)^2(b+1)^2`, the four rows factor as

```text
(e1,e2)   extra unit   label factors             residual
(+1,+1)   1+i          (r-1)(r-i)(r+i)           P_(+1,+1)(r)
(+1,-1)   1-i          (r+1)(r-i)(r+i)           P_(+1,-1)(r)
(-1,+1)   1+i          (r+1)(r-i)(r+i)           P_(-1,+1)(r)
(-1,-1)   1-i          (r-1)(r-i)(r+i)           P_(-1,-1)(r). (2)
```

The linear factors set `r^2` to `1` or `-1`, causing a collision in
`(KB41C-2)`.  The extra factors are nonzero in odd deployed
characteristic.  Therefore only the cubic residual remains, proving
`(KB41C-3)`.

The gate is sharp at the common-`K` level.  Over `F_41`, take

```text
i=9, epsilon_1=epsilon_2=1,
(b,c,r,t)=(10,5,12,30).
```

The labels are `(1,40,21,39,20)` and the products are
`(23,10,31,5,36)`.  They obey every distinctness guard, both product
minors, both q welds, and `P_(+1,+1)(12)=0`.  Finally, changing signs of
`B` and `C` generates the other cell representatives while the four
explicit epsilon rows retain every relative root-sign class. QED.
