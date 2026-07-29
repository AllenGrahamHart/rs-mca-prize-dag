# Proof

Write the positive-half autocorrelation coefficients as `A_d` and put

```text
E=sum_d A_d^2=10,       L=sum_d |A_d|=8.
```

For one representative from each positive conjugate pair, set

```text
y_u=F(zeta_256^u)F(zeta_256^-u)>0.
```

The conductor-256 moment dictionary gives

```text
mean_u y_u=18,
mean_u y_u^2=18^2+20,
mean_u y_u^3=18^3+3*18*20+M_3,                    (1)
```

where `M_3` is the signed cubic relation index of the autocorrelation.

## The exact cubic cap

Expand the absolute full autocorrelation into its two nested symmetric
layers. Their sizes are

```text
s_1=2(n_1+n_2)=14,       s_2=2n_2=2.              (2)
```

If `R(U,W,Z)` counts ordered zero-sum triples from three symmetric layers,
choosing two entries determines the third. Opposite pairs force the missing
zero entry, so

```text
R(U,W,Z)<=min{|U||W|-|U intersect W|,
               |U||Z|-|U intersect Z|,
               |W||Z|-|W intersect Z|}.           (3)
```

Applying `(3)` to the eight ordered layer triples gives

```text
|M_3| <= 182 + 3*26 + 3*2 + 2 = 268.              (4)
```

There is a discrete improvement. Every relation triple has entries in the
nonzero symmetric support modulo 128. A triple with three distinct entries
has a permutation orbit of size six. A triple with two equal entries has a
permutation orbit of size three, paired with a disjoint negated orbit of size
three. An all-equal relation would require `3d=0 mod 128`, hence `d=0`, which
is absent. Products are constant on each orbit. Therefore

```text
M_3=0 mod 6.                                             (5)
```

Equations `(4)--(5)` imply `M_3<=264`.

## Cubic Hermite majorant

Let `p` be the cubic interpolant matching `log y` and its first derivative at

```text
a=33/2,       b=65/2.
```

The Hermite remainder is

```text
log y-p(y)=-(y-a)^2(y-b)^2/(4 xi^4)<=0             (6)
```

for some positive `xi`, so `p` is a global majorant on `y>0`. Its leading
coefficient is

```text
gamma=(1568-2145 log(65/33))/4392960>0.            (7)
```

Using `(1)` and `M_3<=264`, exact simplification gives

```text
mean_u log y_u
 <= (14971/16384) log(33/2)
    +(1413/16384) log(65/2)
    +7819/1098240
 < (1/64) log(514*p_min).                          (8)
```

The verifier proves both strict inequalities in `(7)--(8)` with 96-term
rational atanh intervals. The positive margin in `(8)` has numerator and
denominator bit lengths `27800` and `27814`, respectively. Thus

```text
Norm(F)=product_u y_u < 514*p_min,
```

contradicting a cofactor-`514` prize-row collision. QED.
