# Proof

Write `F` for the deployed field and let `D'` be any `1048587` coordinates
of the official smooth domain.  Choose `B subset D'`, `|B|=9`, and put

```text
u_0(X)=product_(b in B)(X-b),        u_1(X)=X u_0(X),
V'=span{1,X,...,X^7,u_0,u_1}.
```

The displayed polynomials are independent by degree, so `dim V'=10`.
Evaluation on `B` has rank eight and kernel

```text
U=span{u_0,u_1}.
```

For distinct `x,y` outside `B`, evaluation of this kernel on `{x,y}` has
determinant

```text
u_0(x)u_0(y)(y-x) !=0.                              (1)
```

Hence every `T=B union {x,y}` has evaluation rank ten on `V'`.

## Owner petals and received pair

Partition `D' minus B` into eight disjoint petals `P_e` and a remainder
`R`, where

```text
|P_e|=m'-1-|B|=67473,
|R|=1048587-9-8*67473=508794.
```

Choose distinct `t_0,...,t_7 in F` and define owner pairs

```text
p_e=(a_e,b_e)=(t_e u_0,1) in (V')^2.
```

Define the received pair coordinatewise by

```text
(r_0,r_1)=(0,1)       on B,
(r_0,r_1)=(a_e,1)     on P_e,
(r_0,r_1)=(s_x,0)     at x in R.                   (2)
```

The values `s_x` can be chosen so that all

```text
gamma_(e,x)=s_x-a_e(x),       0<=e<8, x in R,       (3)
```

are distinct and avoid any prescribed eighteen slopes.  Indeed, when the
`j`-th remainder coordinate is treated, collision with one of the `8j`
previous slopes forbids at most one `s_x` for each `e`; avoiding the
eighteen prescribed slopes does the same.  Thus at most

```text
64j+8*18 <=64(508794-1)+144=32562896
```

values are forbidden.  This is below the base prime `2130706433`, hence
below `|F|`.  The eight slopes created at one coordinate are internally
distinct because `u_0(x)!=0` and the `t_e` are distinct.

## Exact records and components

For each `(e,x)` use slope (3) and explanation

```text
h_(e,x)=a_e+gamma_(e,x).
```

Equation (2) shows agreement on `B`, on all of `P_e`, and at `x`.
On another remainder coordinate `y`, agreement would say
`gamma_(e,y)=gamma_(e,x)`, contrary to global slope distinctness.  On a
different petal `P_f`, it would say `(t_f-t_e)u_0=0` at a coordinate
outside `B`, which is impossible.  Therefore the exact support is

```text
S_(e,x)=B disjoint_union P_e disjoint_union {x},
|S_(e,x)|=9+67473+1=67483=m'.                       (4)
```

There are

```text
8*508794=4070352                                      (5)
```

distinct records.  For any two distinct `y,z in P_e`, equation (1) makes
`T=B union {y,z}` rank ten, while `p_e` agrees coefficientwise with the
received pair on `T` and owns the record because
`h_(e,x)=a_e+gamma_(e,x)b_e`.  Thus `T` lies on the corresponding
positive-dimensional affine-owner component.  Each record supplies
`C(67473,2)` such marked extensions.

The pair core of `p_e` is exactly `B union P_e`, of size `m'-1`.  More
strongly, no degree-below-eleven pair contains (4).  If a second component
polynomial `b` agreed with `r_1` on (4), then it would equal one on the
`m'-1=67482>K'-1` coordinates in `B union P_e`.  The RS root bound gives
`b=1`, contradicting `r_1(x)=0`.  This proves support-wise pair
noncontainment.

Finally the record error is

```text
e_(e,x)=r_0-a_e+gamma_(e,x)(r_1-1).
```

After anchoring one record, all differences lie in
`span{u_0,r_1-1}`.  The selected error family therefore has affine rank at
most two, stronger than the router's rank-three conclusion.

## Exact target comparisons

The distinct count (5) exceeds `2578110` by `1492242`.  Its marked weight is

```text
4070352*C(67473,2)=9265216597693056.                 (6)
```

At `K'=11`, the weighted concentrator demands

```text
ceil((55*495405467*274980728111260126*C(67483,11))
     /(10^9*C(1048587,9)))
 =5869376383979174.                                 (7)
```

The excess of (6) over (7) is `3395840213713882`.

## Reversible official-row lift

Choose `J` of size `K-11=1048565` in the complement of `D'` and let `L_J`
be its locator.  Set both received columns to zero on `J`; on `D'`, multiply
the residual received values, owners, explanations, and correction space by
`L_J`.  Locator multiplication is injective and sends `V'` into the
degree-below-`K` RS space.  Evaluation ranks on `B` and its extensions are
unchanged because `L_J` is nonzero there.  Every support gains `J`, becoming
size

```text
|J|+m'=1048565+67483=1116048=m,
```

and every displayed owner core becomes size `m-1`.  If an original-row
pair contained a lifted support, its second component would first factor by
`L_J` from its zeros on `J`, and the residual root-bound argument above
would again force a contradiction at `x`.  Thus all local properties and
counts survive the lift.

The family has only four million records and its normalized deviations do
not span the complete ten-space.  It therefore makes no claim to satisfy
the ancestor unsafe-line or dense-anchor hypotheses.
