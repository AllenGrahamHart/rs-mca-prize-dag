# Proof

## Source-pencil equivalence

Write the inner map as `h=[H_0:H_1]`, where the coprime binary forms have
degree `m`. The proved divisor adapter partitions the 12 source points into
complete blocks `S_i` of size `m` and exceptional blocks `R_j` of size
`m/5`. If `A_E` denotes the split locator of a block, pullback of the outer
pole divisor gives

```text
A_(S_i) in <H_0,H_1>,       A_(R_j)^5 in <H_0,H_1>. (KBSP-2)
```

The outer numerator gives `V_act=P(H_0,H_1)` for a binary form `P` of
degree `n=60/m`, which is `(KBSP-1)`.

Conversely, suppose one coprime pencil satisfies `(KBSP-1)--(KBSP-2)`.
Choose target linear forms whose pullbacks are the displayed source forms,
take their fifth powers for complete blocks and first powers for exceptional
blocks, and multiply them to form the outer denominator `Q`. Then

```text
Q(H_0,H_1)=A^5,       P(H_0,H_1)=V_act
```

up to nonzero scalars. Coprimality of `V_act,A` prevents cancellation, so
`f=(P/Q) composed h`. This proves the equivalence.

## Challenge-field descent

Choose two distinct outer-zero fibers. Their points are individually in
`K`, so their split locators `L_0,L_infinity` lie in `K[T_0,T_1]`. The
divisor identity gives

```text
h_0=L_0/L_infinity in K(T),                         (KBSP-3)
```

and `h_0` is a target Mobius transform of `h`. Write `f=F_0(h_0)`. For
every `sigma in Gal(Kbar/K)`, one has `f=F_0^sigma(h_0)`. Substitution
`Kbar(Y)->Kbar(T)`, `Y->h_0(T)`, is injective, hence `F_0^sigma=F_0` and
`F_0 in K(Y)`.

## Degree thirty

The two simple outer poles pull back to `5R_0,5R_infinity`, where each
reduced divisor has degree six. If `P_0,P_infinity` are their coprime
locators, then

```text
div(h)=5R_0-5R_infinity
      =div((P_0/P_infinity)^5).
```

Thus `h` is a target scalar times the fifth power of the degree-six map
`r=P_0/P_infinity`, and `f` already has an inner-degree-six decomposition.

## Degree twelve

Here the unique source block is all of `A`, so the pencil is `<A,N>` and

```text
V_act=c_0 A^5+c_1 A^4N+...+c_5 N^5,       c_5!=0.  (KBSP-4)
```

The descent above permits coefficients in `K`. Since fifth power is
bijective on `K`, rescale `N` so `c_5=1`. Modulo split squarefree `A`, fifth
power is coordinatewise bijective on `K[T]/(A)=K^12`; therefore

```text
N_0^5=V_act mod A
```

has one residue of degree below 12. Every degree-12 lift is `N_0+cA`, which
defines the same pencil. Equation `(KBSP-4)` is therefore equivalent to the
printed six-dimensional membership test.

## Degree two and the conditional carrier gate

The unique deck involution exchanges the two points of every active fiber.
Three such rational pairs determine it, so it lies in `PGL_2(K)`.

For the separate conditional carrier statement, let
`D={x in F_p^*:x^N=1}`, `N=2^21<p`, and let
`gamma(x)=(ax+b)/(cx+d)` preserve `D`. Then

```text
(aX+b)^N-(cX+d)^N=C(X^N-1).                         (KBSP-5)
```

Every intermediate binomial coefficient is nonzero modulo `p`. Comparing
two adjacent intermediate coefficients excludes four nonzero matrix
entries; the remaining invertible cases are diagonal or antidiagonal.
Thus `gamma(x)=kappa x` or `kappa/x`, with `kappa in D`. A nonidentity
diagonal involution is `x->-x`; a reciprocal involution has no fixed point
on `D` exactly when `kappa` is a nonsquare in `D`. This proves all stated
claims without identifying the endpoint and carrier variables. QED.
