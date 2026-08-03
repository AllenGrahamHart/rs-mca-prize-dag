# Proof

Use target variables

```text
a=de,  u=df,  v=ef,  f=f,             a f^2 = u v.       (1)
```

The parent quadratic-cover theorem supplies the guarded common curve

```text
F(r,b)=F_2(r)b^2+F_1(r)b+F_0(r)=0
```

and the normalized common kernel. At the missing label `xi=-t^2`, let
`A_xi,B_xi` be the two kernel evaluations. Because the missing record is one
of `de,de,-de`, its equation fixes

```text
a = B_xi/A_xi, B_xi/A_xi, or -B_xi/A_xi.                (2)
```

The established division-free boundary theorem for the preceding rank-one
node proves that the `A_xi=0` chart boundary has no guarded point. Target
guards give `a,u,v,f != 0`. Put `u=z` and use (1) as

```text
v = a f^2/z.                                             (3)
```

Thus only the torus variables `z,f` remain.

Reduce the three residual-pair Vieta determinants and the missing squared-sum
equation in `F_p(r)[b]/(F)`. Each equation is `C_i+bL_i`. The compiler first
builds these as ordinary polynomials in `u,v,f`, then applies (3) term by
term. For a monomial `u^i v^j f^k`, the exact map is

```text
u^i v^j f^k  ->  a^j z^(i-j) f^(k+2j).                  (4)
```

Powers of `a` are reduced in the same quadratic pair algebra. This avoids a
second symbolic rational-function expansion. A common coefficient
denominator and common `z` monomial are cleared per equation. Every
denominator root is recorded; clearing `z` is valid because `z!=0`.

Choose a nonzero cutter `C+bL`. Every solution annihilates

```text
C_i L-L_i C,                    for every other equation,              (5)
F_2 C^2-F_1 C L+F_0 L^2.                                             (6)
```

For each of the nine claimed matching indices, one normalized projection is
univariate in `z` or `f` and at least two are mixed. A resultant of two mixed
projections eliminates the inner target; its resultant with the univariate
projection eliminates the outer target and gives a nonzero `H(r)`.

FLINT computes and factors

```text
gcd(H(r), r^2130706433-r)
```

exactly. Across the 432 cases there are 9,456 parameter-root incidences.
Established route or inverse boundaries account for 5,248. At each of the
remaining 4,208 roots, the compiler specializes the original reduced
equations, enumerates every outer root, forms all common-`b` pair crosses and
curve norms in the inner variable, enumerates every inner root and every
`b` root, and enforces `a,z,f!=0`. All 8,736 direct fibers are empty. The 480
zeros encountered only on `a=0`, `z=0`, or `f=0` are recorded target-guard
boundaries, not discarded solutions. No live coefficient-clearing boundary
occurs.

The ledger stores every eliminant compressed and hash-pinned. An independently
written eight-shard FLINT replay reparses all 432 eliminants and reproduces
all 9,456 field-root sets. The aggregate checker verifies the full Cartesian
census, every root disposition, all direct fibers, and all custody hashes.
Therefore the 432 guarded systems are empty. QED.
