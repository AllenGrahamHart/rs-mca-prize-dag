# L1 Mersenne HNF m=8 order-one cubic coefficient-field degree-eight router

- **status:** PROVED
- **dependencies:** `l1_mersenne_next_to_maximal_belyi_shifted_value_gate`,
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_common_quadratic_compiler`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the four official `(m,h)=(8,7)` order-one cubic rows

Write an official row as

```text
p=2^t-1,       t in {13,17,19,31},
n=8(p+1)=2^(t+3).                                  (CFR1)
```

Then

```text
ord_n(p)=8.                                         (CFR2)
```

Consequently every normalized split value in the order-one HNF polynomial
`P=(W+1/d)L`, and every coefficient of a monic factor of `L`, lies in

```text
K=F_(p^8).                                          (CFR3)
```

In the cubic `3+2+1` common-quadratic compiler, write

```text
G=W^3+g_1W^2+g_2W+g_3,       x=dg_1,
b=4x-15,                      z=b^2.                (CFR4)
```

The known root `-1/d` and all roots of `G` lie in `K`, so

```text
d,g_1,x,b,z in K.                                   (CFR5)
```

Let `f in F_p[B]` be irreducible. It can contain an official value of `b`
as a root if and only if

```text
deg f divides 8,       equivalently deg f in {1,2,4,8}. (CFR6)
```

Therefore a complete common-gcd factorization in the univariate `b` packets
may discard every factor whose degree is not in `{1,2,4,8}`, in addition to
factors on separately excluded denominator charts. If no legal factor of
one of those four degrees remains, the corresponding official chart is
empty.

This is a field-of-definition router only. It asserts no gcd value, no role
or norm lift, no cyclotomic converse, no inner lift, and no critical close.
