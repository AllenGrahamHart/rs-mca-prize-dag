# Proof

For a fixed signed cell there are seven choices of the forced singleton mate
and `(6-1)!!=15` perfect matchings of the remaining records, hence 105
templates.

Represent a template by its edge-sign tuple, forced record, and unordered
set of three unordered record pairs.  Apply a sign change of `D,E,F` both to
the singleton edge signs and to the names `XY+/-` of each full signed pair.
For `S0` and `S1`, also apply the unsigned skeleton automorphism exchanging
`E` and `F`:

```text
S0: CE<->CF, DE+/-<->DF+/-;
S1: CE<->CF, DE<->DF.
```

`S2` has no nontrivial unsigned pair-name automorphism because the colored
pair, loop pair, and remaining pair have distinct roles.

Exhaustive finite orbit closure gives `(KB41TO-1)`.  The orbit sizes are
exactly `(KB41TO-2)`, and their weighted sums are

```text
6*4+14*8+44*16=840,
18*8+96*16=1680,
1+6*2+9*4+7*8=105.
```

Therefore every raw template occurs exactly once and the canonical cap is
201 per common row. QED.
