# Proof

## Full line supply

At `e=130237`, cutoff 65521, every selected low-core line has inside core at
least 807 and actual total core at most 64796.  After 7,582 removed lines,
the capped convex charge is

```text
charge=881897, target=15895318, next threshold=2.
```

Consequently an unsafe family forces a 7,583rd distinct line.  After that
line the threshold becomes one; no later line is used here.

## Pairs captured by the full factor

Work over the algebraic closure of `F(X)`.  Let `P` be the full gcd of all
nonzero members of the weight-264 interpolation kernel, represented by a
primitive polynomial after clearing denominators, and put
`d=deg_(Y,Z)P`.  The preceding router gives `1<=d<=52`.

Divide every kernel member by `P`.  The resulting cofactor family has gcd
one and total `(Y,Z)` degree at most `52-d`.  Two generic cofactors are
coprime.  Affine Bezout therefore permits at most

```text
(52-d)^2                                             (FM1)
```

common polynomial-pair zeros outside `P=0`.  Every one of the 7,583 selected
pairs is a common zero of the original kernel.  Hence at least

```text
t_d=7583-(52-d)^2                                   (FM2)
```

lie on `P`.  This is increasing for `1<=d<=52`, so `t_d>=4982`.

## Received-point concentration

For each captured pair `(a_i,b_i)`, let `U_i` be its inside common core.
Then `|U_i|>=u=807`, and `P(X,a_i(X),b_i(X))=0` identically.  On every
`x in U_i`, the received pair equals `(a_i(x),b_i(x))`; hence

```text
U_i subseteq S_P:={x in E:P(x,r_0(x),r_1(x))=0}.
```

Distinct selected line pairs are distinct pairs of degree-at-most-five
polynomials, so `|U_i intersect U_j|<=5`.  If `m_x` is the multiplicity of
`x` among the captured cores and `I=sum_x m_x`, then

```text
I>=t u,
sum_x C(m_x,2)<=5 C(t,2).
```

Therefore

```text
sum_x m_x^2 <= I+5t(t-1).
```

Cauchy and monotonicity in `I` give

```text
|S_P| >= ceil(t*u^2/(u+5(t-1))).                   (FM3)
```

The right side is increasing in `t`.  Substitution of the uniform minimum
`t=4982` gives

```text
ceil(4982*807^2/(807+4981*5))=126188.
```

Since `|E|=130237`, at most 4049 inside coordinates lie outside the factor.
