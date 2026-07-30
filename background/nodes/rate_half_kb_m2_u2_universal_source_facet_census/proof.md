# Proof

Every source row `H(alpha_i,X)` is a nonzero quartic, so the six labels in
each of `I` and `J` contribute 24 incidences among the 24 quadratic stars.

Above the five labels in `K`, the common-five source-facet theorem says that
the whole outgoing horizontal root set is `J`. The five complete quadratic
fibers contain ten divisor slots, and the component has two horizontal
roots in each slot. They contribute ten `J-J` stars and 20 `J` incidences.

Above `eta in L minus K`, the whole outgoing root set is `I`. Its complete
quadratic fiber contributes two `I-I` stars and four `I` incidences.

Each of the remaining twelve divisor slots lies in a one-exchange facet
with five `I` labels and one `J` label. A component star there therefore
has type `I-I` or `I-J`. If their counts are `x,y`, then

```text
x+y=12,       2x+y=24-4=20.
```

Thus `x=8,y=4`. Adding the two `eta` stars proves `(KBUS-1)`. The argument
uses no stabilizer or star equivariance.

Each `j in J` has total source degree four. The four `I-J` stars in
`(KBUS-1)` supply exactly four `J` incidences outside the `K` fibers. Put

```text
c_j=4-d_j.
```

Then `c_j` are nonnegative integers and

```text
sum_(j in J)c_j=4.                                  (1)
```

The partitions of four are

```text
4;       3+1;       2+2;       2+1+1;
1+1+1+1.                                            (2)
```

Pad each row of `(2)` by zeros to six parts, subtract from four, and sort.
This gives exactly the five rows in `(KBUS-3)`. Conversely every row there
has entries between zero and four and sum 20, so no integer profile is
missing. Two absent labels would contribute at least eight to `(1)`, hence
at most one label can be absent.

All counts are divisor counts. If a quadratic coordinate fiber ramifies,
its coincident point occupies both slots and the same arithmetic applies.
QED.
