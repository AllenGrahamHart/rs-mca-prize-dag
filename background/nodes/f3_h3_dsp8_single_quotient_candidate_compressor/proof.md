# Proof

For a fixed base vertex `E_0`, put

```text
alpha_i=(beta_i-beta_0)/pi^2.                      (1)
```

Every `alpha_i` is integral by the product-star dependencies. Rebase at
`E_k`. Its generators are

```text
(beta_i-beta_k)/pi^2=alpha_i-alpha_k,
(beta_0-beta_k)/pi^2=-alpha_k.                    (2)
```

Equations `(1)--(2)` show both inclusions `J_k subset J_0` and
`J_0 subset J_k`, proving `J_k=J_0`.

Since `C` is divisible by `pi`, the coupling difference is integral and
satisfies

```text
lambda_k-lambda_0
  =(beta_k-beta_0)C/pi
  =pi C alpha_k.                                   (3)
```

Thus `lambda_k` lies in `(J_0,lambda_0)`. Reversing the roles of `0,k`
gives the opposite inclusion, so `(3)` proves `I_k=I_0` exactly.

Distinct star vertices are distinct unordered shifted-root pairs. The
dyadic shifted-product Sidon theorem therefore makes every nontrivial
`beta_i-beta_k` nonzero. Since `d>=1`, each `J_k`, and hence each `I_k`, is a
nonzero integral ideal whether or not `lambda_k` vanishes.

At an official survivor, all product vertices reduce to the same target and
the selected quotient lift reduces to that target. The row-prime ideal
therefore contains every product difference and every coupling numerator.
The element `pi` is a unit modulo an odd degree-one row prime, so it contains
the normalized generators in `(SQC1)`. This proves `I_k subset mathfrak p`.
Norm reverses ideal inclusion and `Norm(mathfrak p)=p`, proving `(SQC3)`.

Now specialize the proved quotient-algebra Fitting support compiler to
`c=35`; this is legal because every official order has `n-1>35`. Its support
identity gives

```text
p divides s_(n,35)^X
 iff X_35=sum_(t!=1)(P(t)-35)_+R(t)>0.             (4)
```

The sum in `(4)` is positive exactly when some nonidentity target has
`P(t)>=36` and `R(t)>=1`. The single-quotient endpoint compiler proves that
every such target has a positive class-sensitive disjoint-six contribution,
while every term of `Dbar_17^0+Dbar_17^A` has those two inequalities.
This proves both equivalences in `(SQC5)`.

Finally, in the quotient algebra let `I_c^X` denote the derivative ideal.
Adding derivatives gives

```text
I_18^X subset I_35^X.                              (5)
```

Intersect `(5)` with `Z[1/2]`. By definition the resulting principal ideals
are `(s_(n,18)^X)` and `(s_(n,35)^X)`, so

```text
(s_(n,18)^X) subset (s_(n,35)^X).
```

For the chosen positive odd generators, this is exactly the divisibility in
`(SQC6)`. QED.
