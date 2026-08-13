# Large-clone Mobius and rank-one owner router

- **status:** PROVED
- **scope:** the unique clone class `C` of size `c>=m` left by the proved
  owner-pencil subcritical-clone payment

Write the owner pencil as

```text
(Q_tau,A_tau,B_tau)=(Q_0,A_0,B_0)+tau(Q_1,A_1,B_1)
```

and put

```text
F_x(gamma,tau)
 = A_tau(x)+gamma B_tau(x)-Q_tau(x)(r_0(x)+gamma r_1(x)).
```

Suppose the nonzero coordinate curves for all `x in C` contain one common
irreducible bidegree-`(1,1)` component

```text
F_*(gamma,tau)=a+b gamma+c tau+d gamma tau,
Delta=ad-bc != 0.
```

Then `F_x=lambda_x F_*` for `x in C`. On the component use

```text
tau=-(a+b gamma)/(c+d gamma)
```

projectively and define

```text
Qhat(gamma)=(c+d gamma)Q_0-(a+b gamma)Q_1,
Nhat(gamma)=(c+d gamma)(A_0+gamma B_0)
             -(a+b gamma)(A_1+gamma B_1).
```

The denominator has slope degree at most one, the numerator has slope
degree at most two, and coefficientwise on `C`

```text
Nhat(gamma,x)=Qhat(gamma,x)(r_0(x)+gamma r_1(x)).       (LC1)
```

This is the exact Mobius split-pencil normal form of the large clone.

Let `q_0,q_1` be the constant and linear slope coefficients of `Qhat`.
If their polynomial span has dimension one, write projectively

```text
Qhat=ell(gamma) Q_*.
```

There is one projective zero `gamma_0` of `ell`. At that point `(LC1)` says
that the degree-at-most-`m` polynomial `Nhat(gamma_0,X)` vanishes on `C`.
Consequently:

1. if `c>=m+1`, then `Nhat(gamma_0,X)=0`, `ell` divides `Nhat`, and after
   cancellation the clone has one fixed owner

   ```text
   (A_*(X)+gamma B_*(X))/Q_*(X);
   ```

   every rational atom point on the component belongs to this coherent
   owner (or to its globally affine degeneration), while `gamma_0` is not a
   rational-denominator point;
2. if `c=m`, then either the same cancellation holds or

   ```text
   Nhat(gamma_0,X)=mu Lambda_C(X),       mu != 0,       (LC2)
   ```

   where `Lambda_C=product_(x in C)(X-x)`.

Thus a rank-one large clone is absorbed into the rational-owner route except
for the exact boundary residue `(LC2)`. The complete unpriced large-clone
frontier is:

```text
MOVING_DENOMINATOR_RANK_TWO
or
EXACT_M_CLONE_LOCATOR_REMAINDER.
```

No bound for either residual is asserted.
