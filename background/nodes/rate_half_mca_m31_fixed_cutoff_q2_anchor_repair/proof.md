# Proof

Write `A` for the top union.  Every member of `A union D1 union D2` owns at
most one slope.

## At least two top anchors

Two top anchors and any member of `D1 union D2` have at least

```text
e-s-s-(s+2)=K+q-2=K
```

common inside agreement coordinates.  Restriction injectivity therefore
puts `A union D1 union D2` on one affine codeword line.  Removing the two
coarse boundary charges from `F` leaves

```text
G=16895280-284224-258385=16352671.
```

If the support were unsafe, the line would have at least

```text
L=16777215-G+1=424545
```

members.  Total-core packing forces common core `67452=m-2`, of which at
least `67447` coordinates lie inside the gauged direction support.  The
core-absorption theorem synchronizes every assigned pair of deficit at
least `33715` onto the line.  The remaining punctured ordinary list has
agreement `33740` and cap `28`.  Hence

```text
|Z|<=101156*28+981129=3813497,
```

contradicting unsafety.

## Exactly one top anchor

If `|D1|>=2`, the top anchor and any two first-boundary members meet in

```text
e-s-2(s+1)=K+q-2=K
```

coordinates, so `D1` is one affine codeword line.  Its outside agreement is
`m-H=15`, and outside-core packing gives `|D1|<=Q_H=94742`.  Replacing its
coarse charge and adding the top anchor gives

```text
F-284224+94742+1=16705799.
```

If `|D1|<=1`, direct charging gives

```text
F-284224+2=16611058.
```

## No top anchor

If two size-`s+1` missed sets in `D1` intersect, they and any third member
have at least

```text
e-(3(s+1)-1)=K+q-2=K
```

common inside coordinates.  The fixed pair synchronizes all of `D1`, giving

```text
F-284224+94742=16705798.
```

Otherwise the missed sets are pairwise disjoint and

```text
|D1|<=floor(e/(s+1))=3,
```

giving `F-284224+3=16611059`.  The five cases are exhaustive and prove
`(Q2R)`.
