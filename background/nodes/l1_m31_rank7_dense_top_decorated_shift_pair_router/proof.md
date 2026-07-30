# Proof

## 1. Pair-deficit count

For each combined-domain point `x`, let `r_x` be the number of agreement
supports containing it. Put

```text
I_ij=|S_i intersect S_j|,
delta_ij=t-I_ij.
```

The predecessor proves `delta_ij>=0`. Double counting and Cauchy-Schwarz
give

```text
sum_(i<j) I_ij
 =sum_x binomial(r_x,2)
 >=(M^2 m^2/N-Mm)/2.
```

Therefore the total integral deficit obeys

```text
D=sum_(i<j) delta_ij
 <=(M^2(Nt-m^2)/N+M(m-t))/2.                         (1)
```

Here `Nt-m^2=898676`. At `M=M0`, exact cross multiplication gives

```text
10(M0*898676+N(m-t)) < 9N(M0-1).                    (2)
```

The left-to-right ratio in (2) decreases with `M`, so (1) is strictly less
than nine tenths of `binomial(M,2)` for every `M>=M0`.

Every non-top pair has integral deficit at least one. Hence their number is
at most `D`, and more than one tenth of all pairs are top pairs. Their average
graph degree is strictly larger than

```text
(M-1)/10 >= 215792.8.
```

One vertex therefore has integer degree at least `215793`, proving
(DS1)--(DS2).

## 2. Decorated shift-pair normal form

Let `Omega` be the combined domain and let `U` be its interpolation
polynomial. Exact agreement gives

```text
U-a_i=L_i C_i,
```

where `deg L_i=m`, `Z(L_i)=S_i`, and `C_i` is nonzero at every root of
`L_i` in `Omega`.

For a top pair, the squarefree domain locators satisfy

```text
J=gcd(L_i,L_j),       deg J=|S_i intersect S_j|=t.
```

Write `L_i=JA` and `L_j=JB`. Their residual root sets are disjoint, so
`gcd(A,B)=1`, and

```text
deg A=deg B=m-t=w+1=67448.
```

Subtract the two interpolation identities:

```text
J(A C_i-B C_j)=a_j-a_i.
```

The right side is a nonzero polynomial of degree below `k=t+1` and is
divisible by the degree-`t` monic polynomial `J`. The quotient is therefore
a nonzero constant `c`, proving (DS3).

If a nonconstant polynomial divided both `C_i` and `C_j`, it would divide
both terms on the left of (DS3) and hence divide `c`. This is impossible.
Thus `gcd(C_i,C_j)=1`, and every counted edge is primitive in the decorated
cofactor sense.

## 3. Fixed-support projective compression

Fix the anchor supplied by Section 1. Every top neighbor satisfies

```text
a_j-a_i=c_j J_j,
```

where `J_j` is the monic locator of the `t` common agreements. Suppose
several neighbors have the same projective direction, so after monic
normalization they have the same `J`. Together with the anchor, they lie on
the affine line `a_i+cJ`.

All line members agree with the received table at the `t` roots of `J`.
Outside those roots, two distinct scalar labels cannot agree at the same
coordinate: their difference there is a nonzero scalar times `J(x)`. Each
line member has exactly `m-t=67448` agreements outside `J`, and these sets
are disjoint inside the remaining `N-t=1048577` coordinates. Therefore

```text
# line members <= floor((N-t)/(m-t))=15.
```

At most `14` top neighbors use one projective direction. The `215793`
neighbors from Section 1 consequently use at least
`ceil(215793/14)=15414` directions. Each direction is represented by its
monic `J`, a degree-`4980` divisor of the fixed anchor locator lying in the
six-dimensional direction space. This proves (DS4). QED.
