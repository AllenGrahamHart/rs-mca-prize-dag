# Proof

At `a=7m-1`, the number of domain points outside `W` is

```text
N-a=16m-(7m-1)=9m+1.                                 (1)
```

Every such point belongs to at most `m` supported locator root sets. If
every type-2 slope spends at least `p` roots there, double counting gives

```text
T_2 p<=(9m+1)m,
T_2<=floor(((9m+1)m)/p).                              (2)
```

The type-1 term at this value of `a` is at most

```text
floor(a/(a-rho))
 =floor((7m-1)/(3m))=2.                               (3)
```

Combining `(2)` and `(3)` proves `(FRC1)`.

Put `C=(9m+1)m`. The inequality

```text
floor(C/p)<=4m-2                                      (4)
```

holds exactly when `C/p<4m-1`, equivalently `p>C/(4m-1)`. The least
integer with that property is

```text
floor(C/(4m-1))+1,
```

which proves `(FRC2)`. One less fails by the same equivalence, so the
threshold is sharp for this counting ledger.

If `m=4u`, then

```text
C=144u^2+4u,
(4m-1)(9u)=144u^2-9u,
0<13u<16u-1=4m-1.                                    (5)
```

Thus `floor(C/(4m-1))=9u=9m/4`, proving `(FRC3)`. For a clean locator,
`|S_gamma|=rho` and its outside spend is
`rho-|S_gamma intersect W|`; substituting `(FRC3)` gives `(FRC4)`.

Finally compare the old proposed spend. For `4|m`,

```text
p_req-(2m+2)=m/4-1,
```

which is positive for `m>=8`. Direct exact substitution at `m=2^37`
gives the two printed integers. Dividing the leading terms
`9m^2/(2m)` and `4m` gives the residual factor `9/8`. QED.
