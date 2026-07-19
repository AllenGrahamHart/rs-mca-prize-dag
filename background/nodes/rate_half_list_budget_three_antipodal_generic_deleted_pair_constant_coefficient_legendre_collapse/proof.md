# Proof

Use `z` for the half-degree reversal variable in this proof. In the original
fourth-root reduction the reverse variable is `Y^(-1)`, and the deleted-pair
divisor is even. Setting `z=Y^(-2)` there gives

```text
E(z)=(1-z)(1-tz),       F(z)=E(z)^(-1/4).             (1)
```

The generic direction has `U(Y)=YU_0(Y^2)` and degree `4M-1`. Therefore the
fourth-root truncation theorem becomes

```text
B(z):=z^mU_0(z^(-1))=sum_(j=0)^m [z^j]F(z) z^j,
m=2M-1.                                               (2)
```

Put `A=xU_0^2`, as in the constant-coefficient dependency. Since
`a=deg A=2m+1`, reversal gives

```text
A_rev=z^aA(z^(-1))=B(z)^2.                            (3)
```

The full degree-`N-2=2a` reversal of
`Q=(x^N-1)/((x-1)(x-t))` is

```text
Q_full_rev=(1-z^N)/E(z).                              (4)
```

The survivor degree gate has `deg S=s=2M-2`, so
`deg R=deg(AS)=a+s`. Reversing `R=Q-A^2` first at full degree `2a` and then
at its actual degree gives

```text
Q_full_rev-B^4=z^(a-s)R_rev=z^(2M+1)R_rev.            (5)
```

The constant-coefficient dependency says

```text
sigma=[z^s](R_rev/B^2).                               (6)
```

Because `s+(a-s)=a`, equations `(4)--(6)` give

```text
sigma=[z^a]((1-z^N)/(EB^2)-B^2).                     (7)
```

Here `a<N`, and `B(0)=1`, so the term containing `z^N` cannot contribute.
Using `E^(-1)=F^4`, equation `(7)` becomes

```text
sigma=[z^a]((F^4-B^4)/B^2).                          (8)
```

Write `C=F-B`. By `(2)`, `ord C>=m+1`. Expanding `(8)` gives

```text
(F^4-B^4)/B^2
 =4BC+6C^2+4C^3/B+C^4/B^2.                           (9)
```

Now `a=2m+1`. Every term in `(9)` after `4BC` has order at least
`2m+2`, so

```text
sigma=4[z^a]BC.                                       (10)
```

Likewise `deg B^2=2m<a` and `ord C^2>=2m+2>a`. Hence

```text
[z^a]F^2=[z^a](B+C)^2=2[z^a]BC.                      (11)
```

Since `F^2=E^(-1/2)`, equations `(10),(11)` prove `(LCC2)`.

The binomial expansions of `(1-z)^(-1/2)` and `(1-tz)^(-1/2)` give
`(LCC3)`. For the recurrence, set

```text
G(z)=E(z)^(-1/2)=sum_(n>=0)H_nz^n.
```

Differentiating `E G^2=1` gives `2EG'+E'G=0`. Comparing the coefficient of
`z^n` yields `(LCC4)`. All displayed divisions are valid under the standing
characteristic hypothesis `char F>16M`.

The Legendre generating function is

```text
(1-2Xu+u^2)^(-1/2)=sum_(n>=0)P_n(X)u^n.
```

Substitute `u=r^2z` and `X=(r^2+r^(-2))/2` to obtain `(LCC5)`.

Finally substitute `sigma=2H` into the three equations `(CCG3)` and divide
by four. This gives exactly `(LCC6)`. QED.
