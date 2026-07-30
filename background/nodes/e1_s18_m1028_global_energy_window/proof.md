# Proof

Choose one element from each positive conjugate pair and write

```text
y_u=F(zeta_256^u)F(zeta_256^-u)>0.
```

Odd-character orthogonality and autocorrelation Parseval give

```text
sum_u y_u=64*18,
sum_u (y_u-18)^2=128E=64V,
Norm(F(zeta_256))=product_u y_u,                    (1)
```

where `V=2E`.

## Energies zero and one

At `E=0`, equation `(1)` gives `Norm=18^64`, whose 2-adic valuation is 64.
A cofactor-1028 collision has valuation two because `1028=4*257` and the row
prime is odd. Thus energy zero is impossible.

At `E=1`, exactly one positive-half autocorrelation is `epsilon in {+1,-1}`
at a lag `d`. Modulo two, the autocorrelation polynomial is

```text
X^d+X^-d.
```

Its multiplicity at one is `2^(1+v_2(d))`. It is also twice the local
multiplicity of `F`, namely four, so `v_2(d)=1`. Every conjugate square is

```text
18+epsilon(zeta_256^(ud)+zeta_256^(-ud)).           (2)
```

For the integer Lucas sequence

```text
L_0=2,  L_1=18,  L_n=18L_(n-1)-L_(n-2),
```

the exact resultant of `(2)` is `L_32^2`, independently of `epsilon`, with

```text
L_32=13354478338703157414450712387359637585922,
L_32^2 mod 1028=452.
```

It is therefore not divisible by 1028, excluding energy one.

## Energies seven and above

At fixed `V>0`, the positive product maximum under `(1)` has at most two
levels. If the lower level occurs `j` times, it is

```text
a_(V,j)=18-sqrt(V(64-j)/j),
b_(V,j)=18+sqrt(Vj/(64-j)),
M_(V,j)=a_(V,j)^j b_(V,j)^(64-j).                  (3)
```

For each fixed feasible `j`,

```text
d/dV log M_(V,j)
 =sqrt(j(64-j))/(2sqrt(V))*(1/b_(V,j)-1/a_(V,j))<0. (4)
```

It therefore suffices to check `V=14`, or `E=7`. Exactly `j=3,...,63` are
feasible. Enclosing every square root in `(3)` between adjacent rationals of
denominator `2^192` gives 61 exact upper bounds, all strictly below

```text
1028*B_P*2^128.                                    (5)
```

The closest chamber is `j=63`. Equations `(1)--(5)` exclude every `E>=7`.
The lower rational bound in chamber `(V,j)=(12,63)` is still above the same
threshold, so the envelope asserts no exclusion at `E=6`. Together with the
low-energy cases, only energies two through six remain. QED.
