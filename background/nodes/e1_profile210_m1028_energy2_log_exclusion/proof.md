# Proof

Use the notation

```text
y_u=|F(zeta_256^u)|^2=18+x_u,
E=sum_(d=1)^63 A_d^2,
```

over the 64 positive-half conjugate pairs. Conductor-256 orthogonality gives

```text
sum_u x_u=0,
sum_u x_u^2=128E,
Norm(F(zeta_256))=product_u(18+x_u).                 (1)
```

Since the autocorrelations `A_d` are integers,

```text
sum_d |A_d|<=sum_d A_d^2=E.
```

At `E=2` this gives

```text
|x_u|<=2 sum_d |A_d|<=4.                            (2)
```

We claim that

```text
log(1+x/18)>=x/18-x^2/549             (-4<=x<=4).   (3)
```

Let `h(x)` be the left side minus the right side. Then `h(0)=0` and

```text
h'(x)=x(2/549-1/(18(18+x))).                        (4)
```

The only nonzero critical point in the interval is `x=-11/4`. Thus the
minimum is attained at `-4` or `0`. At the negative endpoint, the positive
atanh series with parameter `1/8` gives

```text
log(9/7)
 =2 sum_(j>=0) 1/((2j+1)8^(2j+1))
 <1/4+1/756
 =95/378
 <46/183
 =2/9+16/549.                                       (5)
```

For the tail in `(5)`, replace every `2j+1`, `j>=1`, by `3` and sum the
resulting geometric series. Therefore `h(-4)>0`, proving `(3)`.

Summing `(3)` and using `(1)` gives

```text
log Norm(F(zeta_256))
 >=64 log(18)-(1/549)sum_u x_u^2
 =64 log(18)-256/549.                               (6)
```

Put `z=256/549`. Since `exp(-z)>1-z=293/549`, exact integer arithmetic gives

```text
18^64*(293/549)>1028*p_max.                         (7)
```

Equations `(6)` and `(7)` imply

```text
Norm(F(zeta_256))>1028*p_max.
```

This is incompatible with `Norm(F(zeta_256))=1028*p` for an official row
prime `p<=p_max`. Hence energy two is impossible. QED.
