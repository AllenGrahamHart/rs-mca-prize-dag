# Proof

Let an error be supported on `E subset D`, with `|E|=e<=r`, and pad `E` to an
`r`-set `E' subset D`. Write

```text
Lambda(X)=prod_{x in E'}(X-x)=sum_{j=0}^r lambda_j X^j.
```

For every `0<=i<R-r`,

```text
sum_{j=0}^r lambda_j y_{i+j}
 =sum_{x in E} e(x)v_x x^i Lambda(x)=0.
```

Thus the coefficient vector of `Lambda` lies in `ker M_r(y)`.

Conversely, suppose a monic `Lambda` in that kernel has distinct roots
`E' subset D`, `|E'|=r`. Solve the Vandermonde system

```text
y_i=sum_{x in E'} a_x x^i,       0<=i<r.
```

The solution is unique. Both the given moment sequence and the sequence on
the right obey the recurrence with characteristic polynomial `Lambda`,
because `M_r(y)lambda=0` and `Lambda(x)=0` for every root. Since their first
`r` values agree, induction gives agreement for all `0<=i<R`. Setting
`e(x)=a_x/v_x` produces an error supported on `E'` with syndrome `y`.
This proves `(HS1)`.

If a pair is within one column error set `E` of size at most `r`, pad `E` to
an `r`-set. Its locator annihilates both syndrome sequences. Conversely, a
split locator in both kernels represents both syndromes on its same root set,
so the pair is within `r` columns of `C^2`. This proves `(HS2)`.

Finally, the syndrome at slope `gamma` is `y_0+gamma y_1`, and the Hankel map
is linear. For a column-far pair, every close slope is CA-bad and every CA-bad
slope is close. Applying `(HS1)` gives `(HS3)`. QED.
