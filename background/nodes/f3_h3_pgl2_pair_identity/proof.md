# Proof

Write `A=(1-H)\{0}`. A product representation of `t` has

```text
a=1-x, b=1-y, x,y in H\{1},
(1-x)(1-y)=t.
```

Since `t` is nonzero, `x=1` cannot occur. Solving for `y` gives

```text
y = 1 - t/(1-x) = 1 + t/(x-1).
```

Thus choosing `x in H` whose image under the displayed inversion lies in `H`
is bijective with choosing `(a,b) in A^2` with `ab=t`. Hence
`P(t)=I_inv(t)`.

Similarly, a quotient representation has

```text
c=1-z, d=1-w, z,w in H\{1},
(1-w)/(1-z)=t.
```

Solving for `w` gives

```text
w = 1 - t(1-z) = 1 + t(z-1).
```

The affine intersection `I_aff(t)` also contains `(z,w)=(1,1)`. For `t!=0`,
if either coordinate equals `1`, the equation forces both to equal `1`.
Therefore this is the unique intersection point not corresponding to a valid
pair in `A^2`, proving `R(t)=I_aff(t)-1`.

For the polynomial form, `D_n` has root set `H`. Since `p>=n^2`, one has
`p>n`, so its roots are simple. The affine polynomial `A_t` is obtained from
`D_n` by an invertible linear change because `t!=0`; it is also squarefree,
and its roots are exactly

```text
{z:1-t+tz in H}.                                  (1a)
```

Their intersection with `H` is the affine fiber, proving the second identity
in `(PGL2)`.

The leading degree-`n` terms in `C_n` cancel, while its degree-`n-1`
coefficient is `n!=0`. The fractional-linear involution

```text
J(x)=x/(x-1)
```

maps `H\{1}` bijectively onto the roots of `C_n`: indeed

```text
C_n(J(x))=(x^n-1)/(x-1)^n.                        (1b)
```

Hence `C_n` has exactly `n-1` distinct roots and is squarefree. For
`z=J(x)`,

```text
1-t+tz=(x-1+t)/(x-1)=1+t/(x-1).                  (1c)
```

Therefore a common root of `A_t,C_n` is exactly one inversion-fiber point,
and `J` is bijective on the indexing roots. This proves the first identity in
`(PGL2)`; `(PGL3)` follows by addition.

Finally, if `R(t)>=1`, then `I_aff(t)>=2`. Under the proposed simultaneous
bound,

```text
P(t)=I_inv(t) <= 39-2 I_aff(t) <= 35.
```

This proves the reduction to the paired PGL2 intersection bound. No claim that
the constant 39 estimate itself has been proved is made here.

For the exact critical rectangle, suppose `P(t)=I_inv(t)>=19` and
`I_aff(t)<=18`. Equivalently, `R(t)<=17`. The stronger hypothesis `(PAIR56)`
also implies this, because

```text
2I_aff(t)<=56-I_inv(t)<=37,
I_aff(t)<=18,
R(t)=I_aff(t)-1<=17.                               (4)
```

The product fibers partition all ordered pairs from `A`, so

```text
sum_t P(t)=|A|^2=(n-1)^2.                          (5)
```

Only targets with `P(t)>=19` contribute to `X_18`. Applying `(4)`, then
enlarging the sum and using `(5)`, gives

```text
X_18<=17 sum_(t!=1,P(t)>=19)(P(t)-18)
    <=17 sum_t P(t)
    =17(n-1)^2<17n^2.                              (6)
```

Multiplication by `17` yields `17X_18<289n^2<300n^2`, proving the critical
compiler. At threshold `57`, the profile `I_inv=19,I_aff=19`, equivalently
`P=19,R=18`, is admitted, so the integer `56` is sharp among uniform score
caps used to imply `(PAIR-RECT)`. It is not equivalent to `(PAIR-RECT)` when
`I_inv>19`. QED.
