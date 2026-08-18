# Proof

Write `i=s+ra`, where `0<=s<r`, `0<=a<8`, and put

```text
eta=zeta^8,       omega=zeta^r,       iota=omega^2.
```

As in the complete-band Fourier localization, requiring every frequency
`f_0+8l`, `0<=l<r`, to vanish is equivalent to requiring, for each `s`,

```text
sum_(a=0)^7 X_(s+ra) omega^(f_0a)=0.                    (1)
```

For `f_0=2`, equation `(1)` is

```text
A+iota B=0,
A=X_0-X_2+X_4-X_6,       B=X_1-X_3+X_5-X_7,             (2)
```

with the local `s` suppressed. Both `A` and `B` are integers in `[-2,2]`.
If `(A,B)` is nonzero and `(2)` holds, then after squaring a nonzero-ratio
form one obtains `A^2+B^2=0` in the prime field. But
`0<A^2+B^2<=8`, contradicting characteristic greater than eight. Hence
`A=B=0`.

For `f_0=6`, the local equation is `A-iota B=0`, so it has the same solution
set. This proves `E_2=E_6`. Each of the two alternating four-bit sums has

```text
sum_(j=0)^2 binom(2,j)^2=6
```

zero assignments. The local event therefore has `36` assignments, and the
`r` quotient fibers tensor.

The antipodal shift is `i->i+4r`, or `a->a+4` in each local fiber. Under
this invariance, `(2)` reduces to

```text
2(X_0-X_2)=0,       2(X_1-X_3)=0.
```

There are four invariant local solutions. Thus the common event has `36^r`
words, its antipodal owner has `4^r`, and its primitive part has
`36^r-4^r`. Dividing by the binary sample-space and the two marginal
probabilities gives `(CA1)`.

For `r=1`, the ratio is `(64/9)(1-1/9)=512/81`, whose square exceeds `16`.
Exponential growth follows immediately. QED.
