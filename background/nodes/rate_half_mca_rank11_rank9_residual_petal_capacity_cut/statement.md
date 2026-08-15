# Rank-nine residual-petal capacity cut

- **status:** PROVED
- **closed interval:** `15635<=K'<=20617`
- **first method crossing:** `K'=15635`

Fix the weighted rank-nine nine-coordinate chart in the residual component
target. Let `J` be the common residual core of its affine owner plane and
put `j=|J|`. Since `J` lies in the zero set of the nonzero degree-below-`K'`
kernel word,

```text
9<=j<=K'-1.
```

Writing each owner core as `J disjoint_union P_p`, exact petal-pair counting
gives the marked component cap

```text
W_B <=floor(981105*(n'-j)*(m'+j-20)/2).
```

On `10<=K'<=20617` this is largest at `j=K'-1`. Comparing that envelope
with the weighted selector demand first gives a contradiction at

```text
K'=15635:
demand =50783693985583057,
cap    =50780312213264392,
gap    =3381772318665.
```

At `K'=15634`, the cap still exceeds demand by `1881744358235`. The
unrounded demand/cap ratio strictly increases from the first crossing, so
rank nine is absent through `K'=20617`. Together with the separately proved
high-row weighted cut, rank nine is absent for every `K'>=15635`.

## Nonclaim

Rank nine remains open on `10<=K'<=15634`. The theorem does not pay rank
eight, assign chronology, move an active-v4 atom, or close rank eleven.

## Falsifier

A residual common core with `j>K'-1`; overlapping owner petals; a component
extension using no petal coordinate; marked load above the printed cap; or
failure of either adjacent-row comparison.
