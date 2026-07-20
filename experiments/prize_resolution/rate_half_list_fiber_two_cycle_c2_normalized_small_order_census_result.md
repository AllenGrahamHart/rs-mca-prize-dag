# Normalized c=2 small-order census

The exact normalized gap/span interface was exhaustively evaluated for

```text
p in {2017,12097}, H in {3,4,7,8,10},
plus (p,H) in {(97,7),(113,8),(257,9),(641,9)},
N=8H-8,
```

with `2N | p-1`. Consequently every order-`N` denominator root in the
census is a base-field square. Common scaling fixes one root to one, leaving
exactly `binom(N-1,3)` normalized quartets per `(p,H)`.

Across `325,534` quartets, nineteen passed the nondegenerate primary gap.
Twelve were non-pure counterexamples to primary-only fourth-root rigidity;
all twelve failed the secondary square gate. The other seven occurrences
were the same geometric root set in their respective characteristics:

```text
{1,iota,-1,-iota},       iota^2=-1,
E(z)=1-z^4.
```

Five pure occurrences passed the secondary square gate and failed the full
canonical-span identity. The remaining pure occurrences failed the secondary
gate. No quartet reached a split canonical outer quartic, so no selected
`c=2` pair reached the invariant coupling test.

This falsification pilot kills the tempting route "nondegenerate primary gap
implies a pure fourth-root denominator". It found no counterexample to the
repaired route "primary plus secondary implies a pure fourth-root
denominator", but does not prove it and does not represent an official-order
campaign. Broader raw enumeration should not be requested until that repaired
statement is proved, refuted, or reduced to a coverage-defined arithmetic
task.
