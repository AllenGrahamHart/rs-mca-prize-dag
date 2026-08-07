# Proof: guarded LS6 pair-determinant router

## 1. Primitive quotient coordinates

The proved multiplier gate gives `e>=a`. Leading degrees in `(PD1)` then
give `deg Q_i=e-a` and `lc(Q_i)=lc(E)`. Since every `D_i` divides the core
locator while `M` is supported on disjoint petals, `gcd(D_i,M)=1`.
Reduction of `(PD1)` modulo `D_i` gives

```text
V_i==-M Q_i mod D_i,
```

and therefore

```text
gcd(D_i,V_i)=gcd(D_i,MQ_i)=gcd(D_i,Q_i).
```

The guarded LS6 condition proves `(PD2)`.

## 2. Cross determinant

Multiply the equation for candidate two by `D_1`, the equation for candidate
one by `D_2`, and subtract. The `E D_1D_2` terms cancel, giving

```text
M(D_1Q_2-D_2Q_1)=D_2V_1-D_1V_2.                     (1)
```

The right side has degree at most

```text
j+s=3ell-2a.
```

After division by the degree-`2ell` polynomial `M`, equation `(1)` proves
the degree bound in `(PD4)`.

If `H_12=0`, then `D_1Q_2=D_2Q_1`. The primitive conditions `(PD2)` imply
that `D_1,D_2` are associates. Both are monic of degree `j`, so `D_1=D_2`;
then `(PD1)` gives `Q_1=Q_2` and `V_1=V_2`. Thus distinct candidates have
`H_12!=0`.

Every common divisor of `D_1,D_2` divides `(PD3)`. Since the determinant is
nonzero, `(PD5)` follows. Split squarefree locators identify gcd degree with
root-set intersection, proving `(PD6)`.

## 3. Fixed-base injection

Fix `(D_1,Q_1)`. If candidates two and three have the same determinant,
then

```text
D_1(Q_2-Q_3)=Q_1(D_2-D_3).                            (2)
```

Primitivity gives `gcd(D_1,Q_1)=1`, so `D_1` divides `D_2-D_3`. The latter
has degree below `j` because both locators are monic of degree `j`; hence it
vanishes. Equation `(2)` then gives `Q_2=Q_3`. The map is injective, and
there are `|K|^(ell-2a+1)-1` nonzero polynomials of degree at most
`ell-2a`, proving the slightly stronger version of `(PD7)`.

## 4. Distance fence

Direct expansion gives

```text
(2ell-a)^2-(4ell+b-2)(ell-2a)
 =ell(4a-b+2)+a^2+2ab-4a.
```

This is exactly the live parameter `J`, proving `(PD8)`. The ordinary
constant-weight Johnson argument needs this denominator to be positive.
Since the target branch has `J<=0`, `(PD5)` alone supplies no polynomial
upper bound. QED.
