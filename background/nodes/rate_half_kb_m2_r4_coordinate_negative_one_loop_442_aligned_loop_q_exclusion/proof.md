# Proof

The complete-fiber Vieta compiler gives `(KB41Q-1)`, with `B_0,B_2`
linear, `A_1` quadratic, and `x_W B_2(W)` nonzero at every actual row.
The aligned common classifier gives five distinct labels, so the common
product rows determine `B_0/B_2` and three q rows then determine `A_1` up
to their shared scalar.

In family A substitute

```text
i^2=-1, r^2+r+1=0, b=ir, c=ir^2, t^2=c.
```

Direct reduction of all five product and q rows gives the first triple in
`(KB41Q-2)`.  In family B use

```text
i^2=-1, ib^2+b-i=0, c=i-b, r=-1-ib, t^2=-b;
```

the last two identities are the denominator-free forms of `c=-1/b` and
`r=-i/b`.  The same reduction gives the second triple.  The factors
`1-c`, `1-i`, and `1+b` in family A, and `1-i` in family B, are units by
the source and target guards and the two family polynomials.  The two roots
of each displayed `A_1` are distinct: `c!=i` in A, while `b!=-i` in B
because substitution would give `-3i=0` in the deployed characteristic.

The common loop has `q=0` at `W=t^2`, which is `c` in A and `-b` in B.
Both retained skeletons have exactly one outside loop.  A loop star
`{y,-y}` has sum zero, so its q record vanishes.  Since `B_2` is nonzero
at every actual row, its label is the other root `W=i`.  Evaluation of the
product ratio gives

```text
A: b/i=r,               B: bi=ib.
```

It remains to compare this with the product router.  Put
`s=alpha*beta*gamma*delta in {+1,-1}`.

In family A, `b^2c^2=1`.  An `S1` loop would give `-d^2=r`, hence
`d^4=r^2`, but the router gives `d^4=-s`.  Neither `r^2=1` nor `r^2=-1`
is compatible with `r^2+r+1=0`.  An `S2` loop has product `b^2=-r^2`;
equating it to `r` contradicts `r^2+r+1=0`.

In family B, `b^2c^2=1`.  An `S1` loop gives `-d^2=ib`, hence
`d^4=-b^2`, while the router gives `d^4=-s`.  Thus `b^2=s`.  The cases
`b^2=1` are target guards; if `b^2=-1`, the family equation gives
`b=2i`, whose square forces characteristic three.  Finally an `S2` loop
would require `b^2=ib`, hence `b=i`; direct substitution in the family
quadratic gives `-i`, not zero.  All retained branches are empty. QED.
