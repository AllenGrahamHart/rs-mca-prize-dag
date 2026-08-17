# Proof

Let `s=10`. A `q`-space `W` with at least `c` common zero columns is called
`h`-transverse when no proper subspace of `W^perp` contains more than `h`
of them. Greedy ordered-basis selection gives at least

```text
(c-h)^(s-q)
```

ordered labelled bases for `W^perp`; all such bases come from the anchor's
set of at most `m` labels. Hence the number of transverse `q`-spaces is at
most

```text
floor(m_fall_(s-q)/(c-h)^(s-q)).                    (1)
```

Every pair type assigned to one `q`-space lies in a two-fold common-support
interleaving of an affine `q`-dimensional RS subcode. The ordinary affine
list cap followed by the proved sub-square interleaving collapse gives the
printed `R_q` record charge. Multiplying by (1) gives the independent-bucket
charge `F_q(Delta)`, where `Delta=c-h`.

For the shared first rung, scan `1<=Delta<=c0`. The largest `h=c0-Delta`
for which

```text
F_1(Delta)+F_2(Delta)<=L_low
```

is `h=42452`, at `Delta=89398`; the slack is `2007222636724`. The adjacent
`Delta=89397` exceeds the budget by `17108854816460`.

For a serial second rung starting in dimension `q`, let its two gaps be
`Delta_q,Delta_(q+1)>=1`. The zero floor evolves as

```text
c_next=c-Delta_q+1,
```

so positivity requires `Delta_q+Delta_(q+1)<=c0+1`. Both charges are
nonincreasing in their gap, hence a minimum uses equality. Exhaustively
evaluate the `c0` integer pairs

```text
(d,c0+1-d),  1<=d<=c0.
```

For `q=1` the unique minimum has the value and gaps printed in the
statement; for `q=2` likewise. Both exceed the complete low-record budget,
even before charging the other initial rank branch. This proves the stated
method wall.
