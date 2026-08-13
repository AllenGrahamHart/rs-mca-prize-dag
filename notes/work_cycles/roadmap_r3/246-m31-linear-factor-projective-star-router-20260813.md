# Cycle 246: M31 linear-factor projective-star router (2026-08-13)

In the degree-one common-factor branch, write the primitive factor as

```text
P=A(X)Y+B(X)Z+C(X).
```

Two captured degree-five sections remove `gcd(A,B)` and force
`deg A,deg B<=5`.  All captured sections then parameterize as

```text
(a_i,b_i)=(a_0+B*t_i,b_0-A*t_i),
deg t_i<=s=5-max(deg A,deg B).
```

Each `t_i` agrees with one induced received word on at least 807 of 130,237
points.  Exact ordinary Johnson caps for `s=0..4` are

```text
161, 201, 268, 401, 802.
```

Since at least 4,982 sections are captured, any nonconstant `A` or `B` is
impossible.  Thus `A,B` are constants.  Two `F`-rational captured pairs make
the center itself `F`-rational: all affine explanation lines pass through
one common finite slope-codeword point when `A!=0`, or have one common
direction codeword at projective slope infinity when `A=0`.

This is an exact bridge from the first Mersenne size-two wall to the shape of
the critical primitive-star problem, but not yet a proof of that consumer's
population bound.  The complementary algebraic residual has factor degree
at least two.

```text
start:                   69a98c3a7
canonical prize:         fdfb20a42
upstream frontier:       #1163-#1166; #1165 @ 2bddbd27
result:                  NARROWED; linear-factor router PROVED
DAG delta:               +1 PROVED node, +4 edges
critical status delta:   none; primitive-star target remains TARGET
Mersenne residual:       130237<=e<=1044241
first-support residual:  F-rational projective star or factor degree >=2
delta-star movement:     none
compute:                 exact arithmetic under RAMguard; no Modal
next route action:       pay the star or classify higher-degree factors
export target:           extend przchojecki/rs-mca PR #1165 after review
```
