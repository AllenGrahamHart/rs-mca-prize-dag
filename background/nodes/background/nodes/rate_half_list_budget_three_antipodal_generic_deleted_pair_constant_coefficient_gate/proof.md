# Proof

The normalized square-root lifts are `(1,iota,r,iota r)`. Squaring them gives
the two deleted antipodal pairs `(1,-1)` and `(r^2,-r^2)`, so in the original
coordinate `x=Y^2` their monic deleted quadratic is

```text
D_0=(x-1)(x-r^4)=(x-1)(x-t).                         (1)
```

In particular `D_0(0)=t`, while `A(0)=0`. Evaluating `(CCG1)` at zero gives

```text
T(0)=R(0)=Q(0)=-1/t.                                 (2)
```

We next prove the coefficient formula. Since `A` is monic of degree `a` and
`S` has degree `s`, reversal of `R=AS+T` gives

```text
R_rev=A_rev S_rev+z^(a+s)T(z^(-1)),
S_rev=z^sS(z^(-1)).                                  (3)
```

The Euclidean remainder has degree below `a`, so the last term in `(3)` has
order at least `s+1`. Also `A_rev(0)=1`. Therefore

```text
S_rev=R_rev/A_rev mod z^(s+1).                       (4)
```

The coefficient of `z^s` in `S_rev` is `S(0)`, proving `(CCG2)`.

Finally evaluate the three cleared scalar identities `(NFR7)` at the
polynomial coordinate `x=0`, use `(2)`, and write `sigma=S(0)`. They become

```text
-4(chi-1)^2/t=sigma^2,
-4(chi+2)^2/t=(chi-2)^2sigma^2,
-4(chi-4)^2/t=chi^2sigma^2.                          (5)
```

Multiplication by `t` and rearrangement gives exactly the three equations in
`(CCG3)`. QED.
