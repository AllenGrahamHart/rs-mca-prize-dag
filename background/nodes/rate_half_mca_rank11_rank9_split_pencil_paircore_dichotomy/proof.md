# Proof

Lift the fixed residual owner plane through the line-global common-core
cancellation adapter. The deleted coordinates and the residual cell `B`
belong to the set `J` where every lifted owner pair equals the original
received pair. In particular `j=|J|>=10`.

Let `C_p` be the complete pair core of owner point `p`, put `c_p=|C_p|`, and
write

```text
P_p=C_p minus J.
```

The owner-plane evaluation argument in the predecessor gives two facts:

1. `J subset C_p` for every `p`;
2. the petals `P_p` are pairwise disjoint across distinct owner points.

## Pair intersections enter owner cores

Suppose `t_p>=2`, and choose two distinct record slopes `gamma,delta` whose
record lines meet at `p`. The point `p=(A_p,B_p)` owns both fixed explanation
polynomials:

```text
h_gamma=A_p+gamma B_p,
h_delta=A_p+delta B_p.
```

Let their selected original supports be `S_gamma,S_delta`, each of size
`m=1116048`. Since the domain has size `n=2097152`,

```text
|S_gamma intersection S_delta|>=2m-n=134944.        (1)
```

At a coordinate in this intersection, the received slope line agrees with
both displayed explanations. The slopes are distinct, so subtracting the
two equalities recovers equality of both received columns with
`(A_p,B_p)`. Hence

```text
S_gamma intersection S_delta subset C_p,
c_p>=134944.                                        (2)
```

## Ordered record pairs are paid by petals

Put

```text
D=n-m=981104,
x=m-c_p,
y=t_p-1.
```

Support-wise pair noncontainment gives `c_p<m`, so `x>=1`. The fixed-owner
exception sets of its `t_p` slopes are disjoint outside `C_p`; therefore

```text
t_p(m-c_p)<=n-c_p=(m-c_p)+D,
yx<=D.                                               (3)
```

Assume the low-common-core branch `j<=134943=m-D-1`. Then

```text
m-j>=D+1.                                           (4)
```

Since `y>=1`, (3) also gives `y<=D`. Moreover

```text
D+1-x-y=(D-yx)+(y-1)(x-1)>=0,
```

so `D+1-x>=y`. Combining this with (4) yields

```text
c_p-j=(m-j)-x>=D+1-x>=y=t_p-1.
```

Also `D+1>=t_p`. Thus every point with `t_p>=2` satisfies

```text
t_p(t_p-1)<=(D+1)|P_p|.                             (5)
```

Double the exact owner-block identity and sum (5). Petal disjointness and
`j>=10` give

```text
g(g-1)
 =sum_p t_p(t_p-1)
 <=(D+1) sum_p |P_p|
 <=981105*(n-j)
 <=981105*(n-10)
 =2057516501910.                                    (6)
```

Exact integer square-root evaluation gives

```text
1434405*1434404 = 2057516269620 <= 2057516501910,
1434406*1434405 = 2057519138430 >  2057516501910.
```

Therefore `g<=1434405` in the low-common-core branch. If a plane exceeds
that cap, the low branch is impossible and `j>=134944`, proving the stated
dichotomy.

The proof neither selects among different planes nor charges records from
different planes to one common core.
