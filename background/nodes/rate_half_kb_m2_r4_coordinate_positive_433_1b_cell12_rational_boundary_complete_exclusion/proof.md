# Proof

Fix one of the eight boundary points and one target lane.  Evaluate the
parent kernel as

```text
(A_0,A_1,A_2,B_0,B_1,B_2,beta_0,beta_1).
```

At the missing source label `x=-t^2`, all eight points have `A(x) != 0`.
Therefore the missing target product and squared sum are

```text
m = B(x)/A(x),
S = x (beta_0+beta_1 x)^2/A(x)^2.                 (KBP1B12-BD-1)
```

For missing roles `DE,DE,-DE,DF,sigma_o EF`, equations `(KBP1B12-BD-1)`
leave at most four ordered lifts of two target coordinates and one free
coordinate `y`.  For missing `BF` or `sigma_c CF`, eliminating `f` gives

```text
(u^2+m)^2-Su^2 = 0,  u=b or c.
```

This expression is nonzero at every boundary point, immediately excluding
all 30 endpoint labels.

For each remaining lift and residual matching, the compiler substitutes the
seven outside products

```text
DE, DE, -DE, DF, sigma_o EF, BF, sigma_c CF
```

into the three exact pair-resultant equations supplied by the kernel.  It
factors the first nonzero univariate equation, tests every deployed root in
the other two equations, and then tests all target guards.  Across all 32
point/lane shards and 3,360 labels, every shard is complete and there are no
witnesses or free branches.

The independent audit does not enumerate roots from a factorization.  It
reconstructs the missing lifts with an independent Tonelli-Shanks routine,
takes the gcd `G` of the three pair equations, computes

```text
R = gcd(G, y^p-y),
```

and divides from `R` every factor of the full target-guard product.  The
remaining degree is zero in every lift of every label.  It also replays the
missing product and squared-sum identities symbolically.  Hence no guarded
deployed target exists in any of the 3,360 systems. QED.
