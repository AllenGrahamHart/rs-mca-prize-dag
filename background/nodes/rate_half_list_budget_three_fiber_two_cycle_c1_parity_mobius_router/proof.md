# Proof

After repeated-root normalization, a two-antipodal-pair denominator has roots
`{1,-1,x,-x}`. Choose `r^2=x`. The cycle lift inventory gives
`r^(4L)=1`, and distinctness gives `r^4!=1`. If the unused root is
`-1`, the two unpaired completion squares are `x,-x`, giving `X_R`.
If the unused root is one of `x,-x`, conjugation and relabeling reduce to
the second line of `(CPM2)`. Independent lift signs are absorbed by
`r -> -r` and `iota -> -iota`. This proves completeness of the two
role patterns.

The even-factorization theorem is parameter-uniform in the denominator
quartic. At the doubled cycle order its factor roots lie in `mu_L`, so its
leading-coefficient argument gives `q=mu/lambda in mu_L`. Since
`lambda+mu=alpha` and `lambda mu=gamma`,

```text
q+q^(-1)=(lambda^2+mu^2)/(lambda mu)
         =(alpha^2-2gamma)/gamma.                    (1)
```

The outer roots are distinct and nonzero, so `gamma!=0` and `q!=1`.

For four ordered points write

```text
cr(A,B;C,D)=((A-C)(B-D))/((A-D)(B-C)).                (2)
```

An antipodal target `(1,-1,y,-y)`, with `q=y^2`, has cross ratio
`((1-y)/(1+y))^2`. Eliminating the orientation gives

```text
(z-1)^2(1+q)^2=4q(z+1)^2.                            (3)
```

Divide `(3)` by the nonzero scalar `q(z-1)^2`. The result is exactly

```text
q+q^(-1)=tau(z).                                     (4)
```

Conversely, reversing this calculation shows that `(4)` gives one of the
two target orientations. Cross-ratio equality is necessary and sufficient
for a PGL match.

The three perfect matchings of a tuple `(x_0,x_1,x_2,x_3)` are represented
by

```text
cr(x_0,x_1;x_2,x_3),
cr(x_0,x_2;x_1,x_3),
cr(x_0,x_3;x_1,x_2).                                 (5)
```

Substitution of `X_R,X_P` in `(5)` gives `(CPM5)--(CPM6)`.
Equations `(1),(4)--(5)` prove the exact six-test criterion `(CPM7)`.

If `y_0=q+q^(-1)`, induction gives
`y_m=q^(2^m)+q^(-2^m)`. Hence `q^L=1` implies `y_39=2`.
Conversely, the terminal equation gives
`(q^L-1)^2/q^L=0`, so both reciprocal roots have order dividing `L`.
The condition `y_0!=2` removes `q=1`. This proves `(CPM8)`.

For `q=-1`, equation `(3)` is equivalent to `z=-1`. Adding one to
each rational expression in `(CPM5)--(CPM6)` and clearing its nonzero
denominator gives, up to nonzero scalar factors, exactly the six expressions
in `(CPM9)--(CPM10)`.

The `P0` conclusion is immediate. On `R0`,
`r^2=-iota`, hence `r^4=-1`. At parity parameter `t=-1`,

```text
((1-x)(1+x))^(-1/4)=(1-x^2)^(-1/4).
```

Its coefficient at index `2M` is `(1/4)_M/M!`. The official
characteristic exceeds `16M`, so every numerator and denominator factor
is nonzero. This contradicts the required primary zero
`F_(2M)(t)=0`, proving `(CPM11)`.

Finally, `r -> -r` exchanges `R1,R2` and conjugating `iota`
exchanges `P1,P2`. Thus `(CPM12)` is the complete unresolved harmonic
list. QED.

