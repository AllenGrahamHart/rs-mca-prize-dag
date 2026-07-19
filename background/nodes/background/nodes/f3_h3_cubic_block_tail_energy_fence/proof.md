# Proof

Fix `n=2^s`, `s>=13`, and put

```text
M=(n-1)(n-2).
```

For every `m=2^j`, `3<=j<=s`, set

```text
q_m=floor(3n^2/m^3).
```

Let

```text
U=sum_(m>=8) q_m m(m-1),       R=M-U.
```

Since

```text
U < 3n^2 sum_(j>=3)2^(-j)=3n^2/4<M
```

on every official order, `R` is positive. Every term in `M` and `U` is even,
so `R` is even. Put `q_2=R/2`. This proves `(CT1)` exactly.

For `tau=2`, the number of blocks is

```text
q_2+sum_(m>=8)q_m
 =M/2-(1/2)sum_(m>=8)q_m(m(m-1)-2)
 <n^2/2=4n^2/2^3.
```

For `3<=tau<=n`, let `2^k` be the least power of two in the ladder
`8,16,...,n` that is at least `tau`. Then `k>=3` and

```text
#{B:m_B>=tau}
 <=3n^2 sum_(j>=k)2^(-3j)
 =(24/7)n^2/2^(3k)
 <4n^2/tau^3.
```

This proves `(CT2)` for every integer `tau>=2`; the real-`tau` form follows
by the same ceiling step. For `tau>n` the tail is empty.

The quotient-block dictionary gives `m` parameters of multiplicity `m-1`
for each block of size `m`. Including the identity parameter, the induced
energy is therefore

```text
E_prof=(n-1)^2+sum_m q_m m(m-1)^2.               (1)
```

Eliminating the size-two residual with `(CT1)` gives the exact finite formula

```text
E_prof=(n-1)^2+M
       +sum_(m>=8)q_m m(m-1)(m-2).               (2)
```

Substituting `n=2^s` and the printed floor formula into `(2)` is an exact
integer calculation. For each of the twenty exponents `22<=s<=41`, it gives

```text
4E_prof>145(n-1)^2.
```

The smallest violating order is `s=22`; there
`E_prof/n^2>37.875`, already above the target. At `s=41`, the ratio exceeds
`74.875`. The verifier replays every floor, the exact mass, all tail
breakpoints, and all twenty strict inequalities using integers only.

The construction is deliberately abstract. It proves that the displayed
marginal statements do not imply the energy endpoint; it says nothing about
whether such a block multiset is realized by a shifted subgroup.
