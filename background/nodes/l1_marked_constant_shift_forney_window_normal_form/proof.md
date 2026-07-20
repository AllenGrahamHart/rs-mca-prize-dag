# Proof - L1 marked constant-shift Forney-window normal form

## 1. The interpolation module

Consider the `K[Z]`-linear evaluation map

```text
Phi:K[Z]^2 -> direct_sum_i K,
Phi(A,B)=(B(a_i)-c_iA(a_i))_i.                         (1)
```

It is surjective: take `A=0` and interpolate an arbitrary value vector by a
polynomial `B` of degree below `t`. Its kernel is `L`, so
`K[Z]^2/L` has `K`-dimension `t`. Since `K[Z]` is a PID, `L` is a free
rank-two module. For any module basis, its determinant generates the index
ideal and therefore has degree `t`. Both basis columns evaluate into the same
one-dimensional line at every `a_i`, so their determinant is divisible by
`Q`. Hence every basis determinant is `kappa Q`, `kappa!=0`.

Apply polynomial row reduction to a basis until its two leading coefficient
vectors are independent. The process terminates because every reduction
strictly lowers one maximum component degree. Write the resulting degrees as
`mu<=nu`. Independence of the leading vectors gives the predictable-degree
property

```text
deg(h_0q_0+h_1q_1)
 =max(deg h_0+mu,deg h_1+nu),                         (2)
```

with the usual convention for a zero term. It also makes the determinant
degree `mu+nu`. Since that determinant is `kappa Q`,

```text
mu+nu=t.                                               (3)
```

## 2. Saturation forces both basis directions into the strip

Multiplying by `J` restores the full congruences and gives

```text
gcd(F',W')=J,       deg gcd(F',W')=v.                  (4)
```

The `P`-adic coefficient pairs of `F',W'` have degree at most `m` in the
block variable `Z` and lie in `L`. By `(2)`, the complete truncated module is

```text
L_(<=m)
 ={h_0q_0+h_1q_1:
   deg h_0<=m-mu,       deg h_1<=m-nu},                (5)
```

with a summand absent when its bound is negative.

Suppose `nu>m`. Then every coefficient pair is a polynomial multiple of
`q_0`. Collecting those multipliers over the `X`-coefficient positions gives

```text
F'=A_0(P)H(X,P),       W'=B_0(P)H(X,P).                (6)
```

Here `A_0` is nonzero. Otherwise `B_0` would vanish at all `t` labels, while
`deg B_0<=mu<=t/2<t`, forcing `q_0=0`.

Because `t<=2m`, equations `(3)` and `nu>m` imply `mu<=m-1`. Since
`deg F'=d+v`, equation `(6)` forces

```text
deg H>=d+v-mu ell>d+v-(m-1)ell>v,                     (7)
```

contradicting `(4)`. Thus `nu<=m`, and consequently `mu<=nu<=m`.
Equations `(3)` and this upper bound give exactly `(FW5)`.

Both summands in `(5)` are now present. Its dimension is the left side of
`(FW6)`, which becomes `2m-t+2` by `(3)`. This truncated module is the kernel
of the displayed `t` by `2(m+1)` coefficient matrix, so its rank is exactly
`t`.

## 3. Coefficient reconstruction

For every coefficient position `0<=r<ell`, expand its block pair uniquely in
the reduced basis as

```text
h_(0,r)(Z)q_0+h_(1,r)(Z)q_1,
deg h_(0,r)<=m-mu,       deg h_(1,r)<=m-nu.
```

Set

```text
R_j(X,Z)=sum_(r=0)^(ell-1) X^r h_(j,r)(Z).
```

Reassembling the `P`-adic blocks proves `(FW7)--(FW8)` and uniqueness.

Neither evaluated multiplier can vanish. If, for example, `R_1(X,P)=0`,
then `R_0(X,P)` is a common factor of `F',W'`. Its degree is at least

```text
d+v-deg(A_0(P))>=d+v-m ell>v,
```

contradicting `(4)`; the other case is identical. Any common divisor of the
two evaluated multipliers divides both entries in `(FW8)`, hence divides the
exact gcd `J`. This proves `(FW9)`.

The endpoint specializations follow immediately from `(FW3)--(FW7)`.

## 4. Sharp families

For an admissible pair `mu,nu`, the proposed pairs `(1,U)` and `(V,0)`
satisfy all interpolation conditions if the labels in `U` receive value zero
and the labels in `V` receive value `U(a_i)`. Their determinant is `-UV=-Q`,
and their leading vectors are independent, so they are a reduced module
basis with degrees `mu,nu`.

In `(FW10)`, the product `R(P)V(P)` has degree `m ell`, so
`deg F=m ell+c`, while `deg W=mu ell`. On a root label of `U`, the polynomial
`W` vanishes. On a root label of `V`, one has `F=1` and `W=U(a_i)` modulo
`P-a_i`. Thus all congruences hold.

Finally, the resultant `Res_X(F,W)`, viewed as a polynomial in `lambda`, has
value `1` at `lambda=0`. It is nonzero over the rational function field, so
`gcd(F,W)=1`. This proves every sharpness claim.
