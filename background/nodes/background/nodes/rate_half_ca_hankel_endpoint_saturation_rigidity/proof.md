# Proof

All root counts below are distinct-root counts.  Since `s=0`, no evaluation-
domain factor divides the primitive generic generator `Q_Z` identically in
the parameter.  Hence, for every `x in D`, the specialization `Q_Z(x)` is a
nonzero homogeneous parameter polynomial of degree at most `e=m`.

## 1. Row omissions are charged to rank loss

Fix a supported slope `gamma`.  If its rank loss is `c_gamma`, the
exceptional-root theorem supplies a specialized minimal apolar generator
`G_gamma` of degree `rho-c_gamma`.  It divides both `Q_gamma` and the
squarefree domain-split locator.  Therefore `G_gamma` has
`rho-c_gamma` distinct roots in `D`, all of which are roots of `Q_gamma`.
Since `Q_gamma` is a nonzero form of degree `rho`,

```text
rho-c_gamma <= u_gamma <= rho.
```

Thus every row omission

```text
o_gamma=rho-u_gamma
```

satisfies `0<=o_gamma<=c_gamma`.  The local Smith-form charge from the same
theorem gives

```text
sum_(gamma in Z)c_gamma<=delta=m-1.
```

Summing proves `(SAT2)`.  In particular, if `I` denotes the number of
root-slope incidences, then

```text
I=sum_(gamma in Z)u_gamma=T*rho-O.                     (1)
```

## 2. There is only one possible failing row count

For a fixed domain point `x`, the nonzero polynomial `Q_Z(x)` has at most
`m` distinct finite parameter roots.  Counting `(gamma,x)` in the other
order therefore gives

```text
I=sum_(x in D)d_x<=N*m=16m^2.                         (2)
```

Combining `(1)`, `(2)`, and `O<=delta` yields

```text
T(4m-1)<=16m^2+m-1.                                  (3)
```

The two adjacent products are

```text
(4m+1)(4m-1)=16m^2-1,
(4m+2)(4m-1)=16m^2+4m-2.
```

The second exceeds the right side of `(3)` for every `m>=1`.  Hence
`T<=4m+1`.  A failure of the desired strict cap `T<=4m` must therefore have
exactly `T=4m+1`, proving `(SAT3)`.

## 3. Column saturation

Assume `(SAT3)`.  Equations `(1)` and `(2)` now give the exact capacity
deficit

```text
sum_(x in D)(m-d_x)
 =N*m-I
 =16m^2-((4m+1)(4m-1)-O)
 =1+O.                                                (4)
```

This is `(SAT4)`.  Each summand in `(4)` is a nonnegative integer, and every
nonsaturated domain point contributes at least one.  There are consequently
at most `1+O<=m` nonsaturated points, so at least

```text
16m-(1+O)>=15m
```

points have `d_x=m`.  This proves `(SAT5)`.

At a saturated point, a nonzero parameter polynomial of degree at most `m`
has `m` distinct finite roots.  Its degree is therefore exactly `m`; its root
set is a subset of `Z`; and it divides the squarefree product `H_Z`.  QED.
