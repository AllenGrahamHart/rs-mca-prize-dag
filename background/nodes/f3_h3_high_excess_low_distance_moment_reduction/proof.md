# Proof

Write `e=P(t)-18>=15`. The rich-excess degree ladder supplies

```text
m>=7+ceil(e/2)                                     (1)
```

small coefficient vectors and the total low-distance edge-weight bound

```text
W(t)>=ceil(m(m-4)/2).                              (2)
```

The right side of `(2)` is nondecreasing in `m`, so substitute the lower
bound `(1)`. For odd `e=2r-1`, the same `m=7+r` occurs at the next even excess
`2r`, so the ratio `e/W` is smaller than in that even case. It is therefore
enough to take `e=2r`, `r>=8`, and prove

```text
ceil((r+7)(r+3)/2) >= 83r/8.                      (3)
```

At `r=8`, the left side is `83`, giving equality in `(3)`. For `r>=9`, the
unrounded difference is

```text
(r+7)(r+3)/2-83r/8=(4r^2-43r+84)/8>0.
```

The quadratic is increasing for `r>=9` and has value `21` in its numerator
at `r=9`. Thus `(3)` holds for every `r>=8`. Rearranging proves `(HLM2)`.

Multiply `(HLM2)` by `R(t)` and sum over `P(t)>=33`:

```text
X_18^>14 <= (16/83)M_33.                           (4)
```

If `(HLM3)` holds, then `(4)` gives

```text
17X_18^>14
 <=(272/83)M_33
 <=300n^2-238(n-1)(n-2).
```

This is exactly the `E=14` sufficient target from the proved excess-budget
tradeoff, so C36' follows.

For the conservative display, replace the exact right side of `(HLM3)` by
`83*62n^2` and divide by `272`. Since `83*62/272=2573/136`, `(HLM4)` follows.
Finally `(HLM5)` is the definition of `W(t)` summed against `R(t)`. QED.
