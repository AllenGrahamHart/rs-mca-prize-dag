# Cycle 349: MCA rank-11 minimal-row split-pencil payment (2026-08-15)

Cycle 348 optimized owner petals independently and left the low interval
`10<=K'<=15528`. At the minimal row, exact correction-space rank and the
selected-support incidence geometry provide a second owner resource.

## Abstract weighted split-pencil theorem

Let owner petals have weights `s_p<=A-1` and total at most `S`. On each
distinct affine record line, let the chosen support induce masses
`x_(L,p)<=s_p` of exact total `A`, and charge

```text
Q_L=sum_p C(x_(L,p),2).
```

Split lines into three classes. Balanced selected partitions inject their
cross-petal coordinate pairs globally. A selected dominant line with only
one globally heavy owner consumes disjoint light mass through that owner;
the clean-line inequality has exact slack

```text
(d-1)(d+s)(s-1),       d=A-s.
```

Lines containing two globally heavy owners inject into heavy-owner pairs.
This proves

```text
sum_L Q_L
 <=floor((A-2)S^2/8)+C(S,2)+C(h,2)C(A-1,2),
h=floor(S/(floor(A/2)+1)).
```

The theorem uses each record's chosen support and does not assume absence of
accidental agreements outside it.

## Minimal-row application

At `K'=10`, saturation gives `V'=F[X]_<10`. Every eleven-set has evaluation
rank ten and every nine-set rank nine. Thus the complete component density
`990810934/10^9` enters rank-nine owner planes; no half-lane loss remains.
Moreover the nine-set kernel locator has exactly those nine domain roots, so
`J=B` and every marked extension uses two coordinates from one owner petal.

With

```text
A=67473,       S=1048577,       h=31,
```

the three capacity terms are

```text
9273161316835569,
    549756338176,
   1058433770040,
```

for total `9274769506943785`. Full-density weighted averaging gives demand
`11736940042024039`, exceeding capacity by `2462170535080254`. Rank nine is
therefore impossible at `K'=10`; dimension equality also excludes the
rank-eight and kernel alternatives there.

The primary and independent certificates pass. The abstract audit exhausts
281,827 weighted affine-plane instances over `F_3` and 1,260 deterministic
`F_5` instances while retaining every rich line.

```text
result:                PROVED rank-nine closure at K'=10
newly closed rows:     10
remaining rank nine:  11..15528
new premise:           none
compute:               constant-memory exact integers under RAMguard
next route action:     attack K'=11, where rank-eight and kernel charts
                       return; couple the one-dimensional correction
                       quotient to the selected-support split-pencil cap
```
