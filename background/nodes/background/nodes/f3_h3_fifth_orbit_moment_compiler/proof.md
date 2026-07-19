# Proof

The swap involution on the `P(t)` ordered product representations has `D(t)`
fixed points. Therefore its orbit count is

```text
U(t)=(P(t)+D(t))/2.
```

Because `a^2=t` has at most two roots in the odd-characteristic official
fields, `0<=D(t)<=2`, and parity gives `D(t)=P(t) mod 2`. Hence

```text
U(t)>=ceil(P(t)/2).
```

For `P(t)<=18` there is nothing to prove. If `P(t)>=19`, put
`u=ceil(P(t)/2)>=10`. Then

```text
P(t)-18 <= 2(u-9).                                (1)
```

For every integer `u>=10`,

```text
binom(u,5) >= 231(u-9).                           (2)
```

At `u=10` this is `252>=231`, and at `u=11` it is equality
`462=231*2`. For `u>=11`, induction follows from

```text
(u+1)(u-9) - (u-4)(u-8) = 4u-41 > 0,
```

together with `binom(u+1,5)=binom(u,5)(u+1)/(u-4)`.
Combining `(1)` and `(2)`, and using monotonicity of the binomial coefficient,
gives

```text
(P(t)-18)_+ <= (2/231) binom(U(t),5).
```

Multiplication by `R(t)>=0` and summation over the only nonzero left-hand
terms, namely `t!=1` with `P(t)>=19`, proves `(O5)`. If
`M_5^rich<=(34650/17)n^2`, then

```text
17X_18 <= 17*(2/231)*(34650/17)n^2 = 300n^2.
```

The coefficient `2/231` is sharp for the integer compiler: at
`P=22,D=0,U=11`, both sides before multiplication by `R(t)` equal `4`.
