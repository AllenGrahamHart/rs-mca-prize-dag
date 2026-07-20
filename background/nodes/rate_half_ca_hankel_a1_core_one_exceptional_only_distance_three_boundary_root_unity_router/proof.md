# Proof

At an external slope, the pair-Lagrange formula and monic normalization give

```text
G_z(a)=
 B(a)(lambda_i/xi_i)L_i(z)(A/D_i)(a)/q_bar(z)        (1)
```

for either root `a` of pair `i`. Taking the ratio of `(1)` at the two roots
removes every slope-dependent factor. Multiplying over the `3e` external
slopes and using `(BRU1)` gives

```text
(C(a)/C(b))^e=U_(a,b)^(3e).                          (2)
```

At a root of `A`, differentiation of `P_X=ABC` gives

```text
P_X'(a)=A'(a)B(a)C(a).                               (3)
```

Since the matched quadratic is `D_i=(X-a)(X-b)`,

```text
A'(a)=(a-b)(A/D_i)(a),
A'(b)=-(a-b)(A/D_i)(b).                              (4)
```

Equations `(3)--(4)` imply

```text
C(a)/C(b)=-[P_X'(a)/P_X'(b)]/U_(a,b).                (5)
```

Substituting `(5)` into `(2)` gives `(BRU3)`.

At a triple root `t`, the normalized external value is

```text
G_z(t)=A(t)Phi(z)/(z q_bar(z)).                      (6)
```

Taking the ratio at `t,u`, multiplying over all external slopes, and using
`(BRU1)` yields

```text
(C(t)/C(u))^e=(A(t)/A(u))^(3e)=V_(t,u)^(3e).         (7)
```

Differentiation at a root of `B` gives

```text
P_X'(t)=A(t)B'(t)C(t),
C(t)/C(u)=[P_X'(t)/P_X'(u)]/(V_(t,u)W_(t,u)).        (8)
```

Substitution in `(7)` proves `(BRU5)`.

Finally, on the multiplicative domain,

```text
P_X(X)=(X^N-1)/((X-s)(X-x_0)).                       (9)
```

At any retained domain point `x`, the derivative of the numerator is
`N x^(N-1)=N x^(-1)`, while the denominator is nonzero. This proves `(BRU6)`
and completes the proof. QED.
