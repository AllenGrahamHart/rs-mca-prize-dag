# Proof: sharp rate-half FPC5 locator flat is gcd-trivial

Write `m=ell-3`. The cofactor pairs

```text
(A_1,A_2)=(L_0,0),       (A_1,A_2)=(0,L_0)
```

both satisfy the congruence in (GT1) and obey the degree bound. Their locator
images are nonzero scalar multiples of

```text
L_0L_1       and       L_0L_2.
```

Since `L_0,L_1,L_2` are pairwise coprime, every common divisor of `V_F`
therefore divides `L_0`.

It remains to avoid every linear factor of `L_0`. Fix a root `y` of `L_0`.
Take `A_1=1`. On the `m` roots `z` of `L_0`, prescribe

```text
A_2(z)=c_2 L_1(z)/(c_1 L_2(z)).                       (GT3)
```

The denominators are nonzero because the three locators are pairwise
coprime. Interpolation gives a polynomial `A_2` of degree at most `m-1`
(with the empty-background case immediate), so `(1,A_2)` belongs to the
congruence kernel. At the selected root `y`, (GT3) gives

```text
F(y)
 = (L_1(y)-L_2(y)A_2(y))/(c_2-c_1)
 = -L_1(y)/c_1
 != 0.
```

Thus no root of the split squarefree polynomial `L_0` is common to all of
`V_F`. Since every common divisor was already shown to divide `L_0`, the
maximal common gcd is `1`. QED.
