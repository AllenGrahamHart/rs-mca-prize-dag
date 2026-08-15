# Proof

Put

```text
n'=1048576+K',       m'=67472+K',       D=n'-m'=981104.
```

Fix the rank-nine nine-set `B` and let `u` span the kernel of evaluation on
`B`. Owners agreeing with the received pair on `B` form one affine plane.
Let `J` be the coordinates where the complete plane agrees with the
received pair. Then `B subset J subset Z(u)`. The nonzero polynomial `u`
has degree below `K'`, hence

```text
9<=j:=|J|<=|Z(u)|<=K'-1.                            (1)
```

Off `Z(u)`, exactly one owner point can agree with the received pair. Thus
the complete pair core of an owner `p` has the disjoint form

```text
C_p=J disjoint_union P_p,
```

and the petals `P_p` are pairwise disjoint. Put `s_p=|P_p|`. Support-wise
pair noncontainment gives `j+s_p<m'`, so

```text
s_p<=m'-j-1.                                        (2)
```

## Exact extension charge

A marked rank-ten extension is `T=B union {x,y}`. Its owner agrees with the
received pair at both added coordinates. At least one of them lies outside
`Z(u)`, because two kernel zeros would leave evaluation rank nine. Hence at
least one added coordinate lies in `P_p`; the other lies in
`(J minus B) union P_p`. For one owner point the number of available
unordered extension pairs is therefore at most

```text
q_p=s_p(j-9)+C(s_p,2)
   =s_p*(j-9+(s_p-1)/2).                            (3)
```

One owner owns at most `D+1=981105` selected records. From (2)--(3),
owners with `s_p=0` contribute no marked extension; for every remaining
owner,

```text
q_p/s_p
 <=j-9+(m'-j-2)/2
  =(m'+j-20)/2.                                     (4)
```

Summing marked incidences by owner and using petal disjointness gives

```text
W_B
 <=981105*sum_p q_p
 <=981105*(m'+j-20)/2*sum_p s_p
 <=981105*(n'-j)*(m'+j-20)/2.                       (5)
```

Since `W_B` is integral, the floor of (5) is a valid cap.

## Optimize the residual common core

Ignoring the positive constant, the right side of (5) is

```text
F(j)=(n'-j)(m'+j-20).
```

Its forward difference is

```text
F(j+1)-F(j)=D-2j+19.                                (6)
```

For `j<=K'-1<=20616`, (6) is positive. Therefore (5) is largest at the
honest root ceiling `j=K'-1`, where

```text
U(K')=floor(981105*1048577*(67451+2K')/2).          (7)
```

The weighted selector demand is

```text
L(K')=(495405467/10^9) N_min
      *C(m',9)C(m'-9,2)/C(n',9),
N_min=274980728111260126.                           (8)
```

Exact arithmetic at the adjacent rows gives

```text
K'=15634: ceil(L)=50777401704768572,
           U       =50779283449126807;

K'=15635: ceil(L)=50783693985583057,
           U       =50780312213264392.              (9)
```

Before rounding, twice the cross-product `L-U` has numerator

```text
-18157619613263943707902051344298221552552276539946798639022884527164800
```

at the first row and

```text
32632198107169110848930789755311997983757628901001052346612176459768400
```

at the second. Thus `15635` is the honest first crossing.

Finally, the ratio of (8) to the unfloored expression in (7) is a positive
constant times the nine increasing factors `(m'-i)/(n'-i)`, `0<=i<=8`,
and

```text
(K'+67463)(K'+67462)/(2K'+67451).
```

After cancelling its positive common factor `K'+67463`, the last factor
has positive forward cross-difference `2(K'-11)` for `K'>11`. Hence the
ratio strictly increases from `K'=15635`, and the contradiction persists
through `20617`.
