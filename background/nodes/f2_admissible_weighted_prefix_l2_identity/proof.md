# Proof

Write a ternary word uniquely as

```text
eps=1_A-1_B,  A,B subset H,  A intersect B empty.
```

It lies in the class kernel exactly when `Phi(A)=Phi(B)`.  Conversely, any
ordered collision `(A_0,B_0)` has the unique decomposition

```text
A=A_0\B_0,  B=B_0\A_0,  C=A_0 intersect B_0,
```

where `(A,B)` is disjoint, has the same moment difference, and `C` is an
arbitrary subset of the `S-wt(eps)` unused coordinates.  Thus a fixed
kernel word contributes exactly `2^(S-wt(eps))` ordered collisions.  Summing
over the kernel gives

```text
sum_v N(v)^2 = 2^S sum_eps 2^-wt(eps) = 2^S Z_1,
```

which proves `(L2-1)`.

Finite Fourier inversion on `F_p^R` gives

```text
sum_v N(v)^2
 = p^-R sum_u |sum_(A subset H) chi(<u,Phi(A)>)|^2
 = p^-R sum_u |prod_(y in H)(1+chi(f_u(y)))|^2.
```

Since `|1+exp(2 pi i a/p)|^2=4 cos^2(pi a/p)`, division by `2^S`
proves `(L2-2)`.  The diagonal pairs `A_0=B_0` give
`sum_v N(v)^2>=2^S`.  Cauchy--Schwarz and `sum_v N(v)=2^S` give
`sum_v N(v)^2>=4^S/p^R`.  These are `(L2-3)`, and the final equivalence is
immediate from `(L2-1)`. QED.
