# Proof

## Joint charge

Write the `i`th peeled parameterized explanation line as

```text
c_gamma=a_i+gamma*b_i.
```

Its total common core `G_i` consists of coordinates where
`(r_0,r_1)=(a_i,b_i)`.  Pair noncontainment gives `g_i=|G_i|<=m-1`.
Let `I_i` be the part in the `e`-coordinate gauged direction support.
The line direction `b_i` is a nonzero degree-`<K` codeword, so
`|G_i-I_i|<=c`.

The removed parameterized lines are distinct.  At least one of
`a_i-a_j` and `b_i-b_j` is a nonzero degree-`<K` codeword, whence
`|I_i intersect I_j|<=c`.  Inclusion-exclusion gives

```text
sum_i |I_i| <= e+C(r,2)c,
sum_i g_i   <= e+C(r+1,2)c.                       (JC1)
```

Also `sum_i g_i<=r(m-1)`.  Put

```text
S_r=min(r(m-1),e+C(r+1,2)c),
q_r=floor(S_r/(m-1)),
z_r=S_r-q_r(m-1).
```

For one explanation line, off-core agreement sets are disjoint, so its
size is at most

```text
f(g)=(N-g)/(m-g)=1+(N-m)/(m-g).                   (JC2)
```

The increasing function `f` is convex.  Moving core mass from the smaller
of two interior arguments to the larger cannot decrease their sum.
Iterating this exchange concentrates every maximizer at `0`, `m-1`,
and at most one remainder.  Therefore the integer total number of removed
slopes is at most

```text
L_r =
  rQ,                                             if q_r=r,
  floor(q_r Q + f(z_r)+(r-q_r-1)f(0)),            otherwise,            (JC3)
```

where `Q=N-m+1`.  This proves the joint charge without assuming the
forced lower bounds are the actual cores.

## Peeling

After `r` lines have been removed, unsafety of the original family forces
the residual to have more than

```text
T_r=B-L_r
```

slopes.  Apply the parent exact-layer affine-line bank to that residual.
If its base and slot counts are `C_r,G_r`, another slot has size at least

```text
lambda_r=ceil((T_r-C_r+1)/G_r).
```

For `lambda_r>=2`, total-core packing gives the same forced inside-core
lower bound

```text
u_r=max(ceil((lambda_r*m-N)/(lambda_r-1))-c,0).
```

Remove the whole parameterized line and repeat.  For the positive
`u_i`, pairwise inside-core intersection at most `c` gives the
contradiction criterion

```text
sum_i u_i-C(s,2)c>e,                              (JC4)
```

where `s` is the number of positive lower bounds.  Zero lower bounds are
omitted from `(JC4)`.

## Official interval

Use the same guarded moving cutoff as the parent recursion.  Exact replay
checks every prefix and line-bank guard.  All 21 supports
`130199<=e<=130219` terminate at `(JC4)`, using between four and
thirteen lines.

At `e=130220`, cutoff `65515` gives

```text
P_b=11904256, G=260559, C=11645636.
```

The first forced threshold is `20`, followed by 42 thresholds `16`.
Their positive inside-core bounds give only

```text
15811+42*2041-C(43,2)*5=97018<=130220.
```

For `r=43`, `S_r=134950=2(m-1)+44`, the exact joint charge is
`1962895`, and the residual target is `14814320`.  The next forced
threshold is `13`, whose core lower bound is zero.  Joint charges are
nondecreasing, so later thresholds cannot increase; neither `(JC4)` nor
the weighted prefix can then terminate this route.  No unsafe conclusion
is drawn.
