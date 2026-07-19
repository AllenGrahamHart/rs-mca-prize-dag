# Proof

Because `e_1=e_2=0`, expansion of the quotient pencil gives `(IRG2)`. Put

```text
S=DV^3K.
```

The identity `DF=Y^d-1` becomes

```text
DU^4=Y^d-1-S.                                        (1)
```

Multiply `(IRG3)` by `U^3` and add `d`:

```text
P=dDU^4-Y(DU^4)'+d.                                  (2)
```

Substitute `(1)` into `(2)`. The Euler expression of `Y^d-1` cancels:

```text
d(Y^d-1)-Y(Y^d-1)'+d=0.
```

Consequently

```text
P=YS'-dS
 =V^2(3YDV'K+YVD'K+YVDK'-dDVK).                     (3)
```

This proves `V^2|P` without a squarefreeness assumption on `V`.

Differentiate the definition of `P`:

```text
P'=T'U^3+3TU^2U'=U^2(T'U+3TU')=U^2W.                (4)
```

Moreover `P` is congruent to the nonzero field element `d` modulo `U`, so
`gcd(P,U)=1`. Equation `(4)` therefore gives the monic identity
`gcd(P,P')=gcd(P,W)`. Since `V^2|P`, also `V|P'`; the proved
`gcd(U,V)=1` and `(4)` then give `V|W`. This proves `(IRG5)--(IRG6)`.

Put

```text
A=4YDT'+3T(dD-YD').                                  (5)
```

The definition of `T` gives

```text
4YDU'=(dD-YD')U-T.
```

Consequently

```text
4YDW=4YDT'U+12YDTU'=UA-3T^2.                        (6)
```

Let `G=gcd(P,W)`. Modulo `G`, equations `(IRG4)` and `(6)` give

```text
TU^3=-d,       UA=3T^2.                              (7)
```

Cube the second congruence and multiply by `T`. Substitution of the first
congruence yields

```text
dA^3+27T^7=0 mod G.                                  (8)
```

Thus `G|J` for `J=dA^3+27T^7`.

Write `delta_4` and `t_2` for the nonzero leading coefficients of `D` and
`T`. Since their degrees are four and two, respectively, the leading
coefficient of `A` is

```text
delta_4 t_2(3d-4).                                   (9)
```

It is nonzero. In positive characteristic `p>d=2^39`, the odd prime `p`
cannot divide

```text
3d-4=4(3*2^37-1),
```

because `0<3*2^37-1<d<p`; the characteristic-zero case is immediate.
Therefore `deg A=6`. The first term of `J` has degree `18`, whereas
`deg T^7=14`, and `d` is nonzero. Hence `deg J=18`, proving `(IRG8)`.
Together with `(IRG6)` and `v>18`, this excludes the intermediate boundary.

On this boundary `deg T=2` and `U` is monic of degree `r`. Hence
`deg P=3r+2`. If `t_2` is the nonzero leading coefficient of `T`, the leading
coefficient of `W` is

```text
(2+3r)t_2.
```

The characteristic exceeds `d>3r+2`, so it is nonzero and `deg W=r+1`.
Finally `r=3h-2` and `v=2h-2`, giving `(r+1)-v=h+1` and `(IRG9)`. QED.
