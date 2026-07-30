# Proof

## 1. Category census

Every source row `H(alpha_i,X)` has degree four, so the six labels in each
of `I,J` contribute 24 incidences.

Above the five labels in `K`, the common-five source-facet theorem says
that the whole outgoing horizontal root set is `J`. The five complete
degree-two source fibers contain ten points, and the component has two
horizontal roots at each point. They therefore contribute ten `J-J`
stars and 20 `J`-incidences.

Above the unique label `eta in L minus K`, the whole outgoing root set is
`I`. Its complete fiber contributes two `I-I` stars and four
`I`-incidences.

The remaining six source fibers contain twelve points. Corollary 9.27
gives a five-label common subset of `I` and one exchanged `J` label at
each point. Thus a component star there is `I-I` or `I-J`. If their
counts are `x,y`, then

```text
x+y=12,       2x+y=24-4=20,       y=24-20=4.
```

Hence `x=8,y=4`. Adding the two `eta` stars proves `(KBO2-2)`.
All counts include divisor multiplicity, so ramified complete fibers do
not alter the argument.

## 2. Involution and degree profiles

At most one label of `J` can be absent from the `K`-fiber stars: a missing
label would need all four of its row incidences among the four
`J`-incidences outside `K`. If `j in J` occurs over `K`, equation
`(KBO2-1)` places `bar(j)` in the paired star over the same complete
fiber, hence also in `J`. Thus at least five labels of `J` map back into
`J`.

The number of labels crossing between `I` and `J` under an involution has
the same parity as six. It is therefore even. Since at most one `J` label
could cross, none does. This proves `bar(J)=J` and `bar(I)=I`.

For `j in J`, let `c_j` be its number of incidences outside the `K`
fibers. The `K`-fiber edge multiset is `bar`-invariant, so
`c_j=c_bar(j)`. Also

```text
sum_(j in J) c_j=4.
```

On the three `bar`-pairs, the representative values therefore sum to two.
Up to pair permutation they are `(2,0,0)` or `(1,1,0)`. Subtracting from
the total row degree four gives exactly `(KBO2-3)`.

## 3. Exact abstract survivor

Take the allowed aligned subcase `L=I` and

```text
I={0,1,2,3,4,5},       J={6,7,8,9,10,11},
bar=(0 1)(2 3)(4 5)(6 7)(8 9)(10 11),
K={0,1,2,3,4},         eta=5.
```

Over the five `K` fibers use the following five `bar`-edge orbits:

```text
(6,8)|(7,9),    (6,10)|(7,11),   (6,11)|(7,10),
(8,10)|(9,11),  (8,11)|(9,10).
```

Over `eta` use `(0,2)|(1,3)`. For the six one-exchange fiber pairs use

```text
x=2: (0,4)|(1,5)       x=3: (0,5)|(1,4)
x=0: (2,4)|(3,5)       x=1: (2,5)|(3,4)
x=4: (0,6)|(1,7)       x=5: (2,8)|(3,9).
```

The exchanged `J`-neighbor pairs in the final two rows are `(6,7)` and
`(8,9)`. Complete the two-regular, diagonal-free pole graph on right
vertices `6,...,11` by

```text
6:(8,10),  7:(9,11),  8:(10,11),
9:(6,7),  10:(6,7),  11:(8,9).
```

The first four one-exchange component stars lie in the common
`I minus {x}` facet. The last two use the exchanged `J` root on each
side and color exactly four pole edges by this component. Direct counting
gives 24 distinct stars, degree four at every label, category census
`(10,10,4)`, and defect zero. Thus the exact source-facet, symmetry,
degree, color, and defect ledgers are jointly consistent.

This fixture is an abstract route cut, not an endpoint polynomial or
component. Any deletion must use additional component interpolation,
coefficient geometry, or a same-record owner. QED.
