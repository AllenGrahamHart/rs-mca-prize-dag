# Proof

Fix `P` and write `C=L_P`.  For each incident `Q_i`, put `B_i=L_(Q_i)` and
`H_i=C-B_i`.  If `Q_i!=Q_j`, then `B_i!=B_j` and

```text
B_i-B_j=H_j-H_i
```

is a nonzero polynomial of degree at most one.  The locator of
`Q_i intersect Q_j` divides both `B_i` and `B_j`, hence divides their
difference.  Therefore

```text
|Q_i intersect Q_j|<=1.                                  (1)
```

Suppose there are `M` such removed sets in the `A`-point universe `S0`,
and let `r_x` be the number containing `x`.  Then

```text
sum_x r_x=Me,
sum_x binom(r_x,2)=sum_(i<j)|Q_i intersect Q_j|<=binom(M,2).
```

Cauchy-Schwarz gives `sum_x r_x^2>=M^2e^2/A`.  Substitution and division by
`M>0` give

```text
M(e^2/A-1)<=e-1.
```

When `e^2>A`, this is `(PC-2)`.  Fixing `Q` instead gives

```text
L_(P_i)-L_(P_j)=H_i-H_j,
```

so the same proof in the `(N-A)`-point complement proves `(PC-3)`.

It remains to check the official specialization.  Put `T=2^31`.  If
`0<=t<T`, then for every official rate

```text
s=min(N-K-t,K+t)
```

lies between `N/16` and `N/2`.  Binomial symmetry and unimodality, followed
by the elementary product bound, give

```text
binom(N,N-K-t)=binom(N,s)
 >=binom(N,N/16)
 >=(N/(N/16))^(N/16)
 =2^(N/4).                                               (2)
```

Since `log2(q)<256`, one also has

```text
t log2(q)<T*256=2^39=N/4.                               (3)
```

Equations `(2)--(3)` contradict the corridor inequality, even before its
extra `128` bits are added.  Hence `t>=2^31`.

The difference-degree partition gives `e>=t+d+1=t+2` at `d=1`.  Thus
`e>=2^31+2`, while both `A` and `N-A` are at most `N=2^41`; in particular
both are smaller than `e^2`.  The right sides of `(PC-2)--(PC-3)` increase
with the universe size, so each is at most

```text
floor(2^41(2^31+1)/((2^31+2)^2-2^41))=1024.             (4)
```

This proves the official codegree claim.  Summing the degree bound over the
vertices of either projection proves the final bounded-multiplicity
reduction. QED.
