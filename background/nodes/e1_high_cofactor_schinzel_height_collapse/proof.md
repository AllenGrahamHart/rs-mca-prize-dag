# Proof

Let `n=64`. For a positive vector `z` with `sum z_i=n`, put

```text
D=-sum_i log z_i,       P=sum_(z_i>=1) log z_i.
```

The equality `sum(z_i-1)=0` gives

```text
sum_i |log z_i|=D+2P.                                 (1)
```

We first prove the finite entropy lemma

```text
D<6.845  =>  P<11.9.                                 (2)
```

Let `a` be the number of coordinates assigned to the side `z_i>=1`,
including any coordinates equal to one, and put `b=64-a`. Unless all
coordinates equal one, `1<=a,b<=63`. Write

```text
A=sum_(z_i>=1)(z_i-1)=sum_(z_i<1)(1-z_i).
```

Concavity of `log` on the positive side and convexity of `-log` on the
negative side give

```text
P <= a log(1+A/a),
D >= -a log(1+A/a)-b log(1-A/b).                     (3)
```

The second expression is strictly increasing in `A` on `0<A<b`. For each
of the 63 integer choices of `a`, the directed verifier does one of two
things:

1. it proves `a log(64/a)<11.9`, so `P>=11.9` is impossible; or
2. it brackets the solution of `a log(1+A/a)=11.9` from below and proves
   that the second expression in `(3)` is greater than `7.187` there.

Thus `P>=11.9` would imply `D>7.187>6.845`, proving `(2)`. Combining
`(1)--(2)` gives

```text
sum_i |log z_i|<6.845+2(11.9)=30.645.                (4)
```

Now take two fixed-row, fixed-root collisions `alpha,beta` in one common
cofactor `2^mu`, with `mu>=2`. The common-prime associate router supplies a
unit `u` with `beta=u alpha`. Since `p>2^255`, its product identity gives

```text
D=log(18^64/(2^mu p))
 <64log18-(255+mu)log2
 <=64log18-257log2
 <6.845.                                             (5)
```

Apply `(4)` to the two normalized conjugate-square vectors. Coordinatewise,

```text
lambda_a(u)=log z_a(beta)-log z_a(alpha),
```

so the triangle inequality gives

```text
||lambda(u)||_1<2(30.645)=61.29.                     (6)
```

The full-unit circular-basis theorem writes `u=zeta_256^j v`, where `v` is
a totally real algebraic unit and the torsion factor does not change any
absolute logarithm. If `u` is not torsion, then `v` is a nonzero totally real
algebraic integer different from `+-1`. Schinzel's height theorem, in the
short form of Hoehn and Skoruppa, states

```text
h(v)>=(1/2)log(phi),       phi=(1+sqrt(5))/2.          (7)
```

Reference: G. Hoehn and N.-P. Skoruppa, "Un resultat de Schinzel",
Journal de theorie des nombres de Bordeaux 5 (1993), 185,
doi:10.5802/jtnb.88. Their note proves Schinzel's original bound for every
totally real algebraic integer other than `0,+-1`.

If `d=[Q(v):Q]`, each real conjugate of `v` occurs `64/d` times among the
64 conjugate pairs of `Q(zeta_256)`. Because `v` is a unit,

```text
sum_(sigma:Q(v)->R)|log|sigma(v)||=2d h(v).
```

Therefore

```text
||lambda(u)||_1
 =(64/d) sum_sigma 2|log|sigma(v)||
 =256h(v)
 >=128log(phi)>61.595.                                (8)
```

This contradicts `(6)`. Hence `u` is torsion, and every nonempty fixed
cofactor family is one shift/sign orbit. Summing over `mu=2,3,4` gives at
most three such orbits. QED.
