# Proof

## Symmetric target-fiber lemma

Let `G=Z/128Z`, let `h=64`, and let

```text
A=-A subset G \ {0,h},       |A|=m.
```

For `z in A`, put

```text
r_A(z)=#{(x,y) in A^2:x+y=z}=|A intersect (A+z)|.
```

Both `0 in (A+z)\A` and `z in A\(A+z)`, so `r_A(z)<=m-1`. Suppose equality
held. Equal cardinalities would force

```text
A+z=(A\{z}) union {0}.                                  (1)
```

Thus `a+z in A` for every `a in A\{-z}`. Starting at `z in A` and iterating
addition by `z`, relation (1) forces every nonzero element of the cyclic
subgroup `<z>` into `A`. Since `z` is neither zero nor the involution, its
order is at least four and is a power of two. The unique involution of
`<z>` is therefore `h=64`, contradicting `h notin A`. Hence

```text
r_A(z)<=m-2.                                             (2)
```

Summing (2) over `z in A` gives

```text
R(A,A,A):=#{(x,y,z) in A^3:x+y+z=0}<=m(m-2).            (3)
```

## The profile moment

For profile `(0,6,1)`, let `A` be the fourteen signed non-diameter classes
with nonzero autocorrelation and let `T={t,-t}` be the unique magnitude-three
pair. Then the absolute autocorrelation is exactly

```text
b=2 1_A+1_T.
```

The signed third moment is bounded by the zero-fiber cubic of `b`. Expanding
that nonnegative majorant gives

```text
|M_3| <= (b*b*b)_0
       =8 R(A,A,A)+12 R(A,A,T)+6 R(A,T,T)+R(T,T,T).     (4)
```

By (2),

```text
R(A,A,A)<=14*12=168,
R(A,A,T)=r_A(t)+r_A(-t)<=24.
```

The group has no element of order three, so `R(T,T,T)=0`. The four ordered
pairs in `T^2` have sums `2t,0,0,-2t`; since zero is absent from `A`,

```text
R(A,T,T)=2 1_A(2t)<=2.
```

Substitution in (4) yields

```text
|M_3|<=8*168+12*24+6*2=1644.                            (5)
```

This abstract bound is sharp: take the order-16 subgroup of `G`, delete zero
and 64, and choose `t` with `2t` still present. Sharpness is not an
autocorrelation existence claim.

The proved V=66 reduction certifies that the rational cubic-Hermite majorant
puts every full-conductor collision with `M_3<=1732` below norm `2^250`.
Since `1644<1732`, the collision-norm criterion contradicts pair feasibility.
The proper-conductor branch is already excluded. QED.
