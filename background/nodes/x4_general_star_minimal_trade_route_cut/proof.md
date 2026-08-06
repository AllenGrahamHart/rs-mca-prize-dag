# Proof

Write `e_j` for the elementary symmetric polynomial over `F_17`.

For

```text
P={1,2,3},       Q={4,5,14},
```

direct expansion gives

```text
(e_1,e_2,e_3)(P)=(6,11,6),
(e_1,e_2,e_3)(Q)=(6,10,8).
```

Thus the pair is order 1 but not order 2, hence not minimal at width 3.
The three two-element sums from `P` are `{3,4,5}` and those from `Q` are
`{1,2,9}` modulo 17.  They are disjoint, so no two points on each side form
a width-2 minimal subrecord.  Equivalently, the locator polynomials are

```text
L_P=X^3+11X^2+11X+11,
L_Q=X^3+11X^2+10X+9,
L_P-L_Q=X+2,
```

rather than differing by a constant.  Their common first coefficient is
nonzero, so neither block is a literal order-1 null block.  Exhausting the
maps `x -> ax` and `x -> a/x` also shows that the two supports are not in one
dihedral orbit.

For the census, enumerate every `h`-subset of `F_17^*`, index it by its bit
mask, and group masks by `(e_1,...,e_d)`.  Within each group count unordered
pairs of disjoint masks.  Taking `(h,d)=(3,1)` gives `4576`.  Taking
`d=h-1` for `h=1,...,8` gives the displayed minimal-record vector and total
`963`.  This is exhaustive because every unordered disjoint pair appears in
exactly one prefix group and exactly once within that group.

The independent audit instead enumerates each `2h`-element union and its
complementary `h+h` partitions.  It obtains the same numbers without using
prefix buckets.  Since `4576>963`, the pigeonhole principle rules out a
multiplicity-one map from the full general population to the full minimal
population.  The explicit witness separately rules out the natural map that
peels a contained minimal subtrade.
