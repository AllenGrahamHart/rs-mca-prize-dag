# Cross-type degree-18 atom-weld compiler

- **status:** PROVED
- **scope:** any two distinct triple-owner heavy-ruling pair types that each
  own at least 29 records

Fix two such types `p,q`. There is a common recovery set containing `p,q`
and at most three further triple-owner types. Let `t in {1,2,3,4}` be the
number of secondary types relative to either anchor. One can form two
core-saturated order-32 packets, respectively 18-anchored at `p` and `q`,
with the following exact profile:

```text
t   counterpart records   other records   shared deck
1           14                   0              28
2           11                   3              25
3            8                   6              22
4            5                   9              19.              (AW1)
```

Both packets have common support intersection equal to the complete
triple-owner core, slope-interpolation degree in `18..31`, at least one
off-anchor explanation, and at least three records from every represented
type. Therefore each packet either emits

```text
chi>=2299571,                                             (AW2)
```

or has a nontrivial pole-simple scalar-locator rational certificate. If
neither packet emits `(AW2)`, their certificates are projectively identical.

Thus every pair of large types has a chronology-compatible pairwise atom
weld unless high complexity is already forced. This does not identify welds
made with different third types, create one canonical atom for the full
population, or pay the welded atom.

## Falsifier

Failure to extend `q-p` to a recovery set of at most four secondary types;
an incorrect row of `(AW1)`; loss of the full core intersection, degree-18
gate, off-line record, pure-locator exclusion, or pole-simplicity; or two
nonidentical rational certificates on one compiled shared deck.
