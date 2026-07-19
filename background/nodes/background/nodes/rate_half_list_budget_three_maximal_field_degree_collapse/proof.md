# Proof

The characteristic is odd because `2^41` divides `q-1`. Also `p>2`, so
`p^e>2^e`; `(MFC3)` gives `e<130` and hence `v_2(e)<=7`.

Suppose first that `e>=4`. If `e` is odd, the elementary odd-exponent LTE
identity gives

```text
v_2(p^e-1)=v_2(p-1)>=41,
```

so `p>2^41`. If `e` is even, LTE gives

```text
v_2(p^e-1)=v_2(p-1)+v_2(p+1)+v_2(e)-1.             (1)
```

Exactly one of `v_2(p-1),v_2(p+1)` equals one. Therefore the other is at
least

```text
41-v_2(e)>=34,
```

and again `p>=2^34-1>2^33`. In both parity cases,

```text
q=p^e>2^(33e)>=2^132,
```

contradicting `(MFC3)`. Thus `e<=3`.

If `e=3`, odd-exponent LTE gives `p=1 mod 2^41`; write

```text
p=c*2^41+1.
```

The interval `(MFC3)` forces `c=5`. Indeed, if `c<=4`, then
`p<(9/2)2^41`, whose cube is less than
`(729/8)2^123<96*2^123=3*2^128`. If `c>=6`, then
`p^3>216*2^123>128*2^123=4*2^128`. Both contradict `(MFC3)`.
But

```text
5*2^41+1=10995116277761=0 mod 7,
```

because `2^41=2^2=4 mod 7`. This number is larger than seven and is not
prime, excluding `e=3`.

For `e=1`, divisibility of `p-1=q-1` gives the first line of `(MFC2)`. For
`e=2`,

```text
v_2(p^2-1)=v_2(p-1)+v_2(p+1)>=41.
```

One summand is exactly one, so the other is at least forty. Equivalently
`p=+/-1 mod 2^40`, proving the second line. QED.
