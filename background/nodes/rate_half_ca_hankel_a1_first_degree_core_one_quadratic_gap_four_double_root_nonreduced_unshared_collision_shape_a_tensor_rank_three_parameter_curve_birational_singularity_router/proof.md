# Proof

Choose the minimal rank-three representation `(TBR1)`. Both coefficient
triples are linearly independent.

The `A_j` have no nonconstant common factor. Such a factor would divide
every row polynomial `G(t,x)`. Each official row has exact degree `m`
and all of its roots are distinct members of `Gamma`, so every root of
the common factor would lie in `Gamma`. At such a root all three `A_j`
vanish, making the complete parameter fiber zero, contrary to the
all-excess nonzero-fiber condition. Exact row degree excludes a common
basepoint at infinity. Thus `a` is basepoint-free and

```text
a^* O_(P^2)(1)=O_(P^1)(m).
```

If `d` is the degree onto the image curve and `c` is its degree, pullback
of a generic line gives

```text
m=dc.                                                (1)
```

For `delta in Gamma`, the all-excess fiber ledger gives

```text
|I_delta|=n-a_delta-r_delta,
sum_delta a_delta=e,
sum_delta r_delta=e-7.                              (2)
```

Hence the total column deficit is `2e-7`. An empty actual column costs
`n=(3e-7)/2`; two empty columns would cost

```text
2n=3e-7>2e-7.                                       (3)
```

There are therefore `3e-z` active slopes for one `z in {0,1}`.

Factor `a` through the normalization of `C_a`. If one active slope lies
over a normalization point `q`, choose an incident row. The corresponding
line section vanishes at every point of the degree-`d` fiber over `q`.
Its pullback is one official row polynomial, whose `m` roots are simple
and all lie in `Gamma`. Thus the fiber is reduced, has exactly `d`
distinct points, and all of them are active slopes. The active set is a
disjoint union of complete degree-`d` fibers, proving

```text
d | (3e-z).                                         (4)
```

Equation `(1)` also gives `d|m`. Since `e=m+2`,

```text
3e=3m+6,       3e-1=3m+5.                          (5)
```

Officially `m=183251937961` is coprime to both `6` and `5`. Therefore

```text
gcd(m,3e)=gcd(m,6)=1,
gcd(m,3e-1)=gcd(m,5)=1.                            (6)
```

Whether `z=0` or `z=1`, equations `(4)--(6)` force `d=1`. Hence
`c=m`, and the finite birational map from `P^1` is the normalization of
`C_a`.

Now take the four general-position coefficient rows from the predecessor
and let

```text
H_i={v in P^2:v dot b(x_i)=0}.
```

No three `H_i` are concurrent, so their six pair intersections `p_ij`
are distinct. A common root of rows `i,j` maps to `p_ij`. Conversely,
every normalization point above `p_ij` is a zero of both line pullbacks;
their complete simple root divisors lie in `Gamma`. Since `a` is the
normalization map, common roots are therefore in bijection with geometric
branches:

```text
|A_i intersect A_j|=r_ij.                           (7)
```

The frame theorem and `e-8=m-6` now give `(TBR6)--(TBR7)`.

For a reduced plane-curve singularity with `r` geometric branches,
pairwise branch intersection multiplicities give

```text
delta_p>=binom(r,2).                                (8)
```

Putting `s=30541989660`, equation `(8)` yields

```text
binom(s,2)=466406566180502462970.                   (9)
```

Finally `m-6=6s-5`. Convexity of `binom(r,2)` shows that the least total
over six nonnegative branch counts with this sum is attained by one count
`s` and five counts `s-1`. It equals

```text
binom(s,2)+5 binom(s-1,2)
 =2798439396930304829525.                           (10)
```

This proves all claims. QED.
