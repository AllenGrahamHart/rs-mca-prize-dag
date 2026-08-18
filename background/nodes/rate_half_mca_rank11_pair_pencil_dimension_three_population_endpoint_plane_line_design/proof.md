# Proof

Fix `q=3170`. The population theorem gives `4960<=K'<=4982` and

```text
F_218>=-13661092+2953K'                             (1)
```

residual coordinates whose owner fiber is an affine plane containing exactly
218 selected types.

## Distinct full planes

Fix one such 218-point plane `A`. Let `J_A` be its complete received-pair
core in the original row. The global common core `J` lies in `J_A`. The
plane-218 endpoint theorem gives

```text
K_A:=K-|J_A|>=2044.                                 (2)
```

Every residual coordinate whose owner plane is `A` lies in `J_A\J`.
Conversely, at every coordinate in `J_A\J`, all 218 types in `A` are owners;
the plane cap prevents any additional owner. Hence `A` occurs exactly

```text
|J_A\J|=K'-K_A<=K'-2044                            (3)
```

times. Therefore the full-owner coordinates require at least

```text
B=ceil(F_218/(K'-2044))                             (4)
```

distinct 218-point planes. Exact evaluation over `K'=4960..4982` gives
`339<=B<=358`.

## Saturated plane pairs

For each row choose exactly the minimum `B` planes from `(4)`. For a selected
scalar point `p`, let `r_p` be the number of chosen planes containing it.
Then

```text
sum_p r_p=218B,
sum_p C(r_p,2)=sum_(A<C)|A intersection C|.         (5)
```

Two distinct affine planes are parallel or meet in one affine line. The
selected affine-line cap is 15, so the right side of `(5)` is at most
`15C(B,2)`. Balancing the integer multiplicities `r_p` over the 3,170
selected points gives the lower bound

```text
sum_p C(r_p,2)>=a(218B)-C(a+1,2)3170,
a=floor(218B/3170).                                 (6)
```

Capacity minus `(6)` is at most 36,489 on all 23 rows, and is 34,539 at the
minimum row `B=339`. Every plane pair whose selected intersection has size
below 15 loses at least one unit from the full capacity `15C(B,2)`. Thus the
number of saturated plane pairs is at least

```text
C(B,2)-[15C(B,2)-lower_bound]>=22752.               (7)
```

## Distinct saturated lines

A saturated pair meets in one affine line containing exactly 15 selected
types. Fix such a line `L`. Distinct affine planes through `L` intersect
exactly in `L`, so their off-line selected sets, each of size `218-15=203`,
are disjoint. Therefore at most

```text
floor((3170-15)/203)=15                             (8)
```

chosen 218-point planes contain `L`. One saturated line accounts for at most
`C(15,2)=105` saturated plane pairs. Equation `(7)` consequently gives at
least

```text
ceil(22752/105)=217                                 (9)
```

distinct saturated selected lines.

Finally, the line-cap equality argument gives a common received-pair core of
size

```text
ceil((15*1116046-2097152)/14)=1045967=K-2609.       (10)
```

Since the global core `J` lies in every line core, each saturated line has at
least `K'-2609`, hence at least `4960-2609=2351`, residual common-core
coordinates. QED.
