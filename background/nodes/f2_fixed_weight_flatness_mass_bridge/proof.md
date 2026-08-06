# Proof

Write `N(v)=sum_b N_b(v)`. The collision identity and Minkowski's
inequality give

```text
2^(S/2) sqrt(Z(A))
  = (sum_v N(v)^2)^(1/2)
  <= sum_b (sum_v N_b(v)^2)^(1/2).
```

Since `sum_v N_b(v)=B_b` and `N_b(v)<=M_b`,

```text
sum_v N_b(v)^2 <= M_b B_b.                          (FW-4)
```

For a bad weight, the trivial estimate `M_b<=B_b` makes its contribution
to the last Minkowski sum at most `B_b`; all bad weights therefore
contribute at most `T_G`. For a good weight, `(FW-1)` and
`sqrt(x+y)<=sqrt(x)+sqrt(y)` give

```text
sqrt(M_b B_b) <= sqrt(L)(sqrt(B_b)+B_b/sqrt(Q)).
```

Now

```text
sum_b sqrt(B_b) <= sqrt((S+1) sum_b B_b)
                 = sqrt((S+1)2^S),
sum_b B_b=2^S.
```

Hence

```text
2^(S/2) sqrt(Z(A))
 <= T_G + sqrt(L)(sqrt((S+1)2^S)+2^S/sqrt(Q)).       (FW-5)
```

Squaring and using `(a+b+c)^2<=3(a^2+b^2+c^2)` proves `(FW-2)`.
When `T_G=0`, `(a+b)^2<=2(a^2+b^2)` proves `(FW-3)`.

For complementation, let `a=A(1,...,1)`. The map `x -> 1-x` sends a
weight-`b` vector of syndrome `v` to a weight-`S-b` vector of syndrome
`a-v`. Thus `N_(S-b)(a-v)=N_b(v)` pointwise, proving both symmetry
claims. The asymptotic consequence follows directly from `(FW-2)`. QED.
