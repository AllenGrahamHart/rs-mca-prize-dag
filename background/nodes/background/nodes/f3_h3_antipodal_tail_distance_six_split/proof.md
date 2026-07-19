# Proof

Fix a selected target and put `e=P(t)-18>=15`. Let `m` be the number of its
squared-norm-at-most-three unordered representations. The degree ladder and
centroid estimate give

```text
m>=7+ceil(e/2),
2N_4(t)+N_6(t)>=ceil(m(m-4)/2).                         (1)
```

Suppose first that the fiber is antipodal-free. The distance-four degree cap
then gives

```text
N_4(t)<=m.                                              (2)
```

At `m=15`, equations `(1),(2)` imply

```text
N_6(t)>=83-2*15=53.
```

The degree ladder permits only `e<=16` at `m=15`, proving `(A6S2)` there.
For `m>=16`, discard favorable rounding to obtain

```text
N_6(t)>=(m^2-8m)/2.                                     (3)
```

Also `e<=2(m-7)`. The required comparison follows from

```text
(m^2-8m)/2 >=53(m-7)/8,
```

which is equivalent to

```text
4m^2-85m+371>=0.
```

The left side is positive at `m=16` and increasing thereafter. Hence
`N_6(t)>=53e/16`, proving `(A6S2)`.

On an antipodal target, the parent distance-six reduction gives
`e<=(8/21)N_6(t)`. Multiply the two pointwise estimates by `R(t)` and sum
over their disjoint target classes:

```text
17X_18^>14
 <=(272/53)M_6,33^0+(136/21)M_6,33^A
 =(136/1113)(42M_6,33^0+53M_6,33^A).                  (4)
```

Equation `(A6S3)` pays the exact residual budget `B_n`; the proved
excess-budget tradeoff then gives C36'. Replacing `B_n` by the smaller
`62n^2` gives `(A6S4)` because `53*62/272=1643/136`.

For the lower-cutoff alternatives, the same two fiberwise floors are

```text
F_0(m)=ceil(m(m-4)/2)-2m,
F_A(m)=ceil(m(m-2)/2)-4(m-1).                       (5)
```

At cutoff `E=6`, one has `e>=7` and `m>=11`. At the boundary `m=11`,
`e<=8`, `F_0=17`, and `F_A=10`, giving the ratios `8/17` and `4/5`.
For `m>=12`, the required comparisons reduce after discarding favorable
rounding to

```text
2m^2-33m+119>=0,       m^2-15m+43>=0.
```

They have values `11,7` at `m=12` and are increasing thereafter. Thus

```text
e<=(8/17)N_6(t)  on the antipodal-free P>=25 lane,
e<=(4/5)N_6(t)   on the antipodal P>=25 lane.       (6)
```

Multiplying by `17R(t)` and summing gives

```text
17X_18^>6 <=8M_6,25^0+(68/5)M_6,25^A
            =(4/5)(10M_6,25^0+17M_6,25^A).
```

This proves `(A6S8)`; replacing `B_(n,6)` by `198n^2` gives `(A6S10)`.

At cutoff `E=10`, one has `e>=11` and `m>=13`. At `m=13`, `e<=12`,
`F_0=33`, and `F_A=24`, giving ratios `4/11` and `1/2`. For `m>=14`,
the corresponding comparisons are

```text
m^2-19m+77>=0,        m^2-18m+64>=0.
```

They have values `7,8` at `m=14` and are increasing thereafter. Hence

```text
17X_18^>10 <=(68/11)M_6,29^0+(17/2)M_6,29^A
             =(17/22)(8M_6,29^0+11M_6,29^A).
```

This proves `(A6S9)`; replacing `B_(n,10)` by `130n^2` gives `(A6S11)`.

It remains to prove the incidence router. The distance-four cap proves that
an eligible fiber has at most one antipodal representation. Choose its
canonical sign `x`; its target is

```text
t=(1-x)(1+x)=1-x^2.                                     (7)
```

Take one edge counted by `N_6(t)`, with canonically oriented endpoints
`{u,v}<{a,b}`, and one ordered quotient representation `(z,w)`. Solving the
two common-product equations and the quotient equation using `(7)` gives
exactly `(A6S6)`. This sends the record to one quadruple in `J_6^A`.

Conversely, a quadruple satisfying the printed membership and orientation
conditions reconstructs the unique antipodal target, both oriented edge
endpoints, and the ordered quotient representation. The maps are inverse;
canonical sign, pair, and edge choices prevent duplication. Therefore
`|J_6^A|=sum N_6(t)R(t)` over the antipodal target class, which is `(A6S7)`.
QED.
