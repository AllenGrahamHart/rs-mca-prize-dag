# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one generic fully-proportional exceptional-E quadratic router

From (FCR1),

```text
K_*=240bq(b-6)-P
   =-40b(b^2-6b+27)
     +(240b^2-1902b-630)q.                         (1)
```

Since `E_G=K_*-720bq^2`, equation (1) proves (FEQ1). Multiplying
`E_G=e_2q^2+e_1q+e_0` by `a_2` and subtracting `e_2F_b` cancels the
quadratic term and gives (FEQ2)--(FEQ3).

Assume `a_2S_1!=0`. On `F_b=E_G=0`, equation (FEQ3) reconstructs
`q=-S_0/S_1`. Substitution in `F_b`, followed by multiplication by `S_1^2`,
gives exactly `V=0`. Conversely, `V=0` and the reconstructed `q` recover
`F_b=0`; equation (FEQ3) then recovers `E_G=0` because `a_2!=0`.

The polynomial `X_*` has `q`-degree at most three, so (FEQ5) clears every
denominator. Under `S_1!=0`, `X_E=0` is equivalent to `X_*=0`. This proves
(FEQ6). If `S_1=0`, equation (FEQ3) forces `S_0=0`; conversely (FEQ7) and
`a_2!=0` recover `E_G=0`. The `a_2=0` branch is the retained linear chart
(FBF6), proving (FEQ8).

For (FEQ9), the coefficient degrees in (FQR1) are `(2,4,6)`, while those in
(FEQ1) are `(1,2,3)`. Hence `deg S_1<=5`, `deg S_0<=7`, and every term of
`V` has degree at most 16. Finally `X_*` has total degree at most five and
`q`-degree at most three. If `X_*=[q^j]` is expanded by powers of `q`, the
term of degree `j` in (FEQ5) has degree at most

```text
(3-j)deg(S_1)+j deg(S_0)+(5-j)<=20+j<=23.
```

This proves the last bound. QED.
