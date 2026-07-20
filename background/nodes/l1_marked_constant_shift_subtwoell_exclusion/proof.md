# Proof - L1 marked constant-shift sub-two-ell exclusion

Since the polynomials `P-a_i` are pairwise coprime, the factors `V_i` are
pairwise coprime and `deg J=sum_i deg V_i`. Define

```text
F'=JF,       W'=JW.
```

For each `i`, write `J=V_iJ_i`. Equation `(MS1)` gives

```text
W'-c_iF'=J(W-c_iF)
          =(P-a_i)J_i A_i
```

for some `A_i`. Thus every full locator `P-a_i` divides `W'-c_iF'`. Also

```text
deg F'=d+v,       deg W'<=d+v,       gcd(F',W')=J.       (1)
```

The last equality uses `gcd(F,W)=1` and monicity of `J`.

By `(MS2)`, both enlarged polynomials have degree below `2ell`. Divide them
uniquely into two blocks modulo `P`:

```text
F'=F_0+PF_1,       W'=W_0+PW_1,
deg F_j,deg W_j<ell.
```

For every coefficient position `0<=r<ell`, the vector of coefficients in
`(F_0,F_1,W_0,W_1)` lies in the kernel of the matrix with rows

```text
R_i=(-c_i,-c_i a_i,1,a_i).                              (2)
```

Suppose this matrix had rank at least three. Its kernel cannot be zero,
because `F'` is nonzero, so it has dimension one. All coefficient vectors
are therefore scalar multiples of one vector `(A,B,C,D)`. For some nonzero
polynomial `H` of degree below `ell`,

```text
F'=H(A+BP),       W'=H(C+DP).                            (3)
```

Since `deg F'=d+v>ell`, one has `B!=0` and

```text
deg H=d+v-ell>v.                                         (4)
```

But `(3)` makes `H` a common divisor of `F'` and `W'`, contradicting `(1)`,
whose monic gcd has degree exactly `v`. Hence the row matrix has rank at most
two.

After permuting columns and changing signs, its rows are

```text
(1,a_i,c_i,a_i c_i).
```

For any three distinct labels, rank at most two makes the minors on columns
`(1,a,c)` and `(1,a,ac)` vanish. Hence `c_i=A+Ba_i` and
`a_ic_i=C+Da_i` on those three labels. The degree-at-most-two polynomial

```text
BZ^2+(A-D)Z-C
```

has three distinct roots, so it is zero. Thus `B=0` and those three `c_i`
are equal. Repeating with two fixed labels shows that every `c_i` is one
common scalar `c`.

The pairwise-coprime locators `P-a_i` now all divide `W'-cF'`. Their product
has degree `t ell>=3ell`, while

```text
deg(W'-cF')<=d+v<2ell.
```

Therefore `W'=cF'`. Its gcd with `F'` has degree `d+v>v`, again contradicting
`(1)`. This proves the exclusion.

For the L1 consequence, take any three dense petals in one constant-shift
pencil and let `V_i` be their missing-set locators. Their total degree is at
most the polarized charge `p`. The marked strict-strip hypothesis follows
from `d+p<2ell`, so the abstract exclusion applies.
