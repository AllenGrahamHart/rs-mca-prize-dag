# Proof

Use the four-basis algebra and global coefficient kernel supplied by
`(KBP1B4-TOWER-1)`. Write the kernel as

```text
(A_0,A_1,A_2,B_0,B_1,B_2,beta_0,beta_1).
```

The missing mate of the singleton source label has quotient label `-t^2`.
On the guarded common locus `A(-t^2)` is invertible, and its source-forced
target product is

```text
m=B(-t^2)/A(-t^2).                              (KBP1B4-X2P0-2)
```

For target products `u,v`, eliminating a source pair at opposite quotient
labels gives

```text
P(u,v)=(p_2 q_0-p_0 q_2)^2
       -(p_2 q_1-p_1 q_2)(p_1 q_0-p_0 q_1),    (KBP1B4-X2P0-3)
```

where `p_i=B_i-uA_i` and
`(q_0,q_1,q_2)=(B_0-vA_0,-B_1+vA_1,B_2-vA_2)`.
At `xi=2`, the omitted record is `-DE=m`, hence `DE=-m`. Matching `0`
pairs the two surviving positive `DE` records and imposes `P(-m,-m)=0`.

The compiler reduces every multiplication first in the quadratic `t` basis
and then in the quadratic `b` basis; it recovers `c` from the proved linear
relation. It records every determinant inverted in this process. If the
target-free element vanishes at a common point, its four-dimensional
multiplication determinant vanishes in `F_p(r)`. This implication is valid
even if either quadratic algebra is reducible.

Exact FLINT arithmetic finds eight roots of the degree-`308` determinant
numerator in every source-sign row. Adding roots from all recorded inverse
numerators and denominators gives ten candidate `r` values. Direct lifting
through the original three tower relations gives the exhaustive per-sign
ledger printed in the statement. Five candidates hit `r=0` or `r^4=1`.
Two lifted branches hit a `t` route guard. Six further `(r,t)` branches have
a quadratic `b` relation with nonsquare discriminant, hence no
`F_p`-valued `b`. The remaining four guarded common points satisfy every
tower relation and route guard, but direct evaluation gives
`P(-m,-m) != 0`.

The primary verifier independently evaluates the common equations, missing
record, negative-`DE` sign, paired-product cut, and all route guards at the
four finite points, and checks the six no-`b` terminals by Euler's criterion.
The audit verifier separately recomputes the `F_p` root part of every stored
norm and inverse polynomial using its own coefficient-list arithmetic. Thus
no candidate or clearing boundary is omitted.

The target-free equation contains neither target sign. Each of the four
source-sign exclusions therefore applies to all four target lanes, excluding
all sixteen cases. QED.
