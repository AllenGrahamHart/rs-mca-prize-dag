# Proof

Let `K=Q(zeta_256)` and `K+=Q(zeta_256)^+`. Fix one prize row, one primitive
quotient root, and the cofactor `m=2`. For a collision, let `z_1,...,z_64` be
its normalized conjugate squares. Then

```text
sum z_i=64,
D=-sum_i log z_i=log(18^64/(2p))
 <64log18-256log2<7.539.                              (1)
```

For a positive vector of mean one put

```text
P=sum_(z_i>=1) log z_i.
```

The entropy argument of `e1_high_cofactor_schinzel_height_collapse`, now
with the cofactor-`2` constants, proves

```text
D<7.539  =>  P<12.2.                                 (2)
```

Indeed, if `a` coordinates are on the side `z_i>=1`, `b=64-a`, and
`A=sum_(z_i>=1)(z_i-1)`, Jensen's inequalities give

```text
P <= a log(1+A/a),
D >= -a log(1+A/a)-b log(1-A/b).                     (3)
```

For each `1<=a<=63`, the directed verifier either proves that the first
quantity can never reach `12.2`, or brackets the first point where it does
and proves that the second quantity exceeds `7.6806`. Thus `(2)` holds.
Since `sum(z_i-1)=0`,

```text
sum_i |log z_i|=D+2P<7.539+2(12.2)=31.939.           (4)
```

Take two collisions `alpha,beta` in the fixed branch. The common-prime
router gives `beta=u alpha` for an algebraic unit `u`. Coordinatewise
subtraction in `(4)` gives

```text
||lambda(u)||_1<2(31.939)=63.878.                    (5)
```

The full-unit theorem writes `u=zeta_256^j v`, where `v` is a totally real
unit in `K+`; the root of unity does not change `lambda`. Suppose that `u`
is not torsion. Then `v` is different from `+-1`.

For a totally real algebraic integer `x` of degree `d`, write

```text
Omega(x)=M(x)^(1/d)=exp(h(x)).
```

C. J. Smyth proved that the two smallest values of `Omega` are

```text
Omega(beta_1)=sqrt(phi),
Omega(beta_2),
```

where `phi=(1+sqrt(5))/2`, and `beta_2` has minimal polynomial

```text
P_2(X)=X^4-X^3-3X^2+X+1.
```

Reference: C. J. Smyth, "On the Measure of Totally Real Algebraic Integers.
II", Mathematics of Computation 37 (1981), 205--208,
doi:10.1090/S0025-5718-1981-0616373-7.

We first exclude the least value inside `K+`. Let `d=[Q(v):Q]`. Since `d`
divides `[K+:Q]=64` and `v` is not rational, `d` is even. If
`Omega(v)=sqrt(phi)`, then

```text
M(v)=Omega(v)^d=phi^(d/2).                            (6)
```

All conjugates of `v` lie in the Galois field `K+`, so the product defining
`M(v)` also lies in `K+`. For every positive integer `n`,

```text
phi^n=(L_n+F_n sqrt(5))/2,       F_n>0.
```

Equation `(6)` would therefore put `sqrt(5)` in `K+`. This is impossible:
`K+` is a subfield of the conductor-`256` cyclotomic field and is unramified
outside `2`, whereas `Q(sqrt(5))` has discriminant `5` and is ramified at
`5`. Hence Smyth's ordering gives

```text
Omega(v)>=Omega(beta_2).                             (7)
```

The polynomial signs

```text
P_2(2.09)<0<P_2(3),       P_2(-2)>0>P_2(-1.33)
```

put two roots outside the unit circle with absolute values greater than
`2.09` and `1.33`. Therefore

```text
M(beta_2)>2.09*1.33=2.7797>1.29^4,
Omega(beta_2)>1.29.                                  (8)
```

As in the high-cofactor node, restriction multiplicities and the squared
absolute logarithms give

```text
||lambda(u)||_1=256h(v)>256log(1.29)>65.188.          (9)
```

This contradicts `(5)`. Thus `u` is torsion, so every two collisions in the
fixed cofactor branch differ by a negacyclic shift/sign. The branch has at
most one such orbit. QED.

