# Proof

Apply the zero-loop product-q weld to `(KBZ433O-1)`.  The two product
determinants are linear in `x`.  Removing target guards from their
compatibility gives `(KBZ433O-2)`.  If its coefficient and constant vanish,
then `Q^2-S^2=-16y(y-1)^2=0`, so the branch is guarded.

On the regular branch

```text
c=b(bS-Q)/(bQ-S).                                 (1)
```

Substitution in one product row gives `x=X_num/X_den`, with

```text
X_num=b^2y^4-3b^2y^3-5b^2y^2-b^2y
      -2by^4+6by^3-22by^2+2by+y^4-3y^3-5y^2-y,
X_den=b^2y^3+5b^2y^2+3b^2y-b^2
      -2by^3+22by^2-6by+2b+y^3+5y^2+3y-1.        (2)
```

After `(1)--(2)`, the q equations are affine-linear in `(t,r)`.  Preserve
the common scaling in Cramer's rule and impose `t^2=x,r^2=y`.  Their exact
gcd is `X_den(y^2-1)`.  Removing this regular-branch guard leaves residual
degrees 20 and 15.  The exact lex bases and binary Frobenius gcds are the
four rows of `(KBZ433O-3)`.

The first-row quadratic splits at

```text
b=1047557337, 1678774983.
```

Both specializations give `y=1605884903` and `X_den=0`; their `X_num`
values are respectively `1104448158` and `464033812`, so neither is a
product solution.  Original-equation replay finds no guarded packet.

For every sign row, the lost linear-`c` and product-solve ideals have exactly

```text
(b,y)=(0,-1),(1,0),(-1,1),                       (3)
```

all guarded.  Three singular-q rows have only `(3)`.  The `(+,+)` row adds
the two false points above and no others.  This exhausts all divisions.

The two target relabelings from the preceding four-cell theorem act on cell
`1` with orbit `[1,3,8,10]` and preserve the original product-q system.
The exclusion transports to the other three cells. QED.
