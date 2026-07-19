# Proof

The characteristic hypothesis from the dependency makes every integer from
one through `d` invertible. Since `E(0)=1`, there is a unique fourth root with
constant term one, and hence a unique `A=E^(-1/4)` in the formal power-series
ring.

First construct a monic degree-`r` polynomial from the truncation

```text
B_*(z)=sum_(m=0)^r a_m z^m,
U_*(Y)=Y^r B_*(Y^-1).                                  (1)
```

The identity `EA^4=1` gives

```text
E'A+4EA'=0.                                             (2)
```

Since `B_*-A=O(z^(r+1))`, equations `(1),(2)` imply

```text
K_*=E'B_*+4EB_*'=O(z^r).                               (3)
```

The reverse-residual identity proved in the dependency is

```text
K_*(z)=z^(r+3)T_*(z^-1).                               (4)
```

Therefore `(3),(4)` give `deg T_*<=3`.

This polynomial is unique. Suppose two monic degree-`r` polynomials have
residual degree at most three, and let their difference be a nonzero
polynomial `Q` of degree `s<=r-1`. Linearity of `(FRG2)` gives the residual
of `Q`. Its leading coefficient is

```text
[d-(4+4s)] lc(Q)=4(r-s)lc(Q),                          (5)
```

and its degree is `s+4>=4`. The coefficient in `(5)` is nonzero because the
characteristic is zero or greater than `d`. This contradicts the degree-three
bound. Hence `U=U_*`, proving `(FRG3)`.

For completeness, compare coefficients of `z^(m-1)` in `(2)`. If
`E=sum_(j=0)^4 eta_jz^j` with `eta_0=1`, then

```text
sum_(j=0)^4 [4(m-j)+j]eta_j a_(m-j)=0.
```

Separating the `j=0` term gives `(FRG4)`. Its division by `4m` is valid for
all indices used here.

Now restore the quartic norm equation. The dependency proves that

```text
H=EB^4-1
```

has exact order `qh` at zero. By `(FRG3)` and `EA^4=1`,

```text
H=E(B^4-A^4)
 =E(B-A)(B^3+B^2A+BA^2+A^3).                          (6)
```

The first and last factors on the right of `(6)` are units, the last having
constant term four. Consequently

```text
ord_0 H=ord_0(B-A)
 =min{m>=r+1:a_m!=0}.                                  (7)
```

The exact order `qh` in `(7)` is precisely `(FRG5)`.

On the official generic boundary, `q=2` and
`qh=2(2^36+1)=r+3`. On the intermediate boundary, `q=3` and
`qh=r+2`. Substitution into `(FRG5)` proves `(FRG6),(FRG7)`. QED.
