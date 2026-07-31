# Proof

Put `q(T)=T^2+tT+p`. The ramified complete-source repair gives

```text
U(T,0) in <q>,       V(T,0) in <q> minus {0}.
```

Normalize `V(T,0)=q(T)`. The internal-star reconstruction and the q-slice
gate remain valid at `w=0`. Write the positive reciprocal form as

```text
U_0=x_0+x_1W+x_2W^2,
U_1=x_3(1+W^2)+x_4W,
U_2=x_2+x_1W+x_0W^2.
```

Modulo `q`, define the coefficient pairs

```text
L=(x_2-px_0, x_3-tx_0),
C=((1-p)x_1, x_4-tx_1),
Gamma=lambda(1-p^2, t(1-p)).
```

Direct reduction gives

```text
(U^2-WV^2)/W^2
  = L^2 W^2 + (2LC-Gamma^2)W + C^2       modulo q.       (1)
```

Unique factorization has exactly three ways to allocate the two roots of
the aligned target quadratic to the two residual quadratics: `same`,
`swap`, and `mixed`. Applying those three allocation formulas to the three
pairs in `(1)` gives four polynomial equations per allocation.

The corrected fraction-free reconstruction retains the relative `U/V`
scale. Its normalization equation is linear in `lambda` and factors as

```text
lambda = 3(2b-1)(p-1)(p+2t+4)                    (fixed),
lambda = -3(b^2-1)(p-1)(p+2t+4)(5p+4t+5)        (moving). (2)
```

The replay independently compares the reconstructed coefficient vector to
an exact `5 x 5` solve and checks `(1)` before using `(2)`.

For fixed-moving, substitute `(2)`, divide the common proved-nonzero
factors, and call the resulting equations `E_1,...,E_4`. Saturate by

```text
F_f = b(b-2)(2b-1)(b-1)(b+1)
      *p(p-1)(p-t+1)(p+t+1)
      *(p+2t+4)(4p+2t+1)(5p+4t+5)(t^2-4p)
      *(b^2+tb+p)(1+tb+pb^2).                    (3)
```

Every factor in `(3)` is an endpoint zero, endpoint/J0 collision,
reciprocal or fixed-point collision, q-root collision, discriminant,
incidence, or reconstruction denominator already forbidden by the parent
gates. For each allocation, the exact deployed-field basis of

```text
<E_1,E_2,E_3,E_4, yF_f-1>
```

is `<1>`.

For moving-moving, all four equations after `(2)` are reciprocal quartics
in `b`. Divide by `b^2` and put `s=b+1/b`; this is an exact quadratic trace
descent. The product of the two endpoint/J0 collision tests descends to

```text
Q_b=p(s^2-2)+t(1+p)s+1+t^2+p^2.
```

Use

```text
F_m=(s-2)(s+2)(2s-5)
     *p(p-1)(p-t+1)(p+t+1)
     *(p+2t+4)(4p+2t+1)(5p+4t+5)(t^2-4p)Q_b.    (4)
```

For `same`, `swap`, and `mixed`, respectively, the exact basis of the four
trace equations together with `yF_m-1` is again `<1>` over
`F_2130706433`.

A unit ideal over the base field has no point over its algebraic closure,
and therefore none over `F_(2130706433^6)`. The six cases exhaust both
internal templates and all residual allocations, proving the claim. QED.
