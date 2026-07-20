# Proof

Put

```text
w=(z+z^(-1))/2.
```

Since `J` has degree `M`, multiplying by `z^M` clears every negative power.
The resulting `H_M` has degree `2M` and satisfies

```text
H_M(z)=z^(2M)H_M(z^(-1)).                            (1)
```

In particular, for every nonzero `z`,

```text
H_M(z)H_M(z^(-1))=J(w)^2.                           (2)
```

The first-kind trace identity gives

```text
T_(2M)(w)=(z^(2M)+z^(-2M))/2.                       (3)
```

Thus `T_(2M)(w)=0` exactly when `z^(4M)=-1`. Because `M` is a power of two,

```text
z^(4M)+1=Phi_(8M)(z).                               (4)
```

Its `4M` roots occur in inverse pairs, and none is `+/-1`. The map
`z |-> (z+z^(-1))/2` sends each pair to one simple root of `T_(2M)`.
Multiplying `(2)` over the pairs therefore gives

```text
Res_z(Phi_(8M),H_M)
 =product_(T_(2M)(w)=0)J(w)^2.                      (5)
```

The leading coefficient of `T_(2M)` is `2^(2M-1)`. The root formula for the
resultant, followed by squaring, says

```text
R_-^2
 =2^(2M(2M-1)) product_(T_(2M)(w)=0)J(w)^2.         (6)
```

Equations `(5)--(6)` prove `(TCN3)`.

For the second kind, the trace identity is

```text
U_(2M-1)(w)=(z^(2M)-z^(-2M))/(z-z^(-1)).            (7)
```

Its roots correspond two-to-one to

```text
z^(4M)=1,       z notin {+1,-1}.                    (8)
```

Applying `(2)` to these inverse pairs gives

```text
Res_z((z^(4M)-1)/(z^2-1),H_M)
 =product_(U_(2M-1)(w)=0)J(w)^2.                    (9)
```

The leading coefficient of `U_(2M-1)` is also `2^(2M-1)`, so the squared
root formula for `R_+` and `(9)` prove `(TCN4)`. Squaring removes the harmless
resultant sign when `M` is odd.

Every divisor of the dyadic integer `4M` is a power of two. Removing the
orders one and two gives the monic factorization

```text
(z^(4M)-1)/(z^2-1)
 =product_(4<=d<=4M, d a power of two)Phi_d(z).      (10)
```

Multiplicativity of the resultant in its first argument proves `(TCN5)`.

Finally, the generalized-binomial formula for a Jacobi polynomial has
2-adically rational parameters here. For every odd prime, those binomial
coefficients are integral in `Z_p`; equivalently, their rational
denominators are powers of two. Substitution in `(TCN1)` preserves that
property. Taking the odd-prime valuation of `(TCN3)--(TCN5)` removes the
displayed powers of two and proves `(TCN6)--(TCN7)`.

The Chebyshev doubling identity gives

```text
U_(2n-1)=2T_nU_(n-1).                                (11)
```

Starting at `n=M` and iterating through the dyadic chain down to `U_0=1`
proves

```text
U_(2M-1)=2^(s+1) product_(j=0)^s T_(2^j)
         =2M product_(j=0)^s T_(2^j).                (12)
```

The resultant is multiplicative in its second polynomial, and multiplying
that polynomial by `2M` multiplies the resultant by `(2M)^M`. Applying these
facts to `(12)` proves `(TCN8)--(TCN9)`.

Finally, the roots of `Phi_(4m)` occur in inverse pairs under the trace map,
and those pairs map exactly to the roots of `T_m`. The same calculation as
`(2)--(6)`, now using the leading coefficient `2^(m-1)` of `T_m`, gives

```text
Res_z(Phi_(4m),H_M)
 =Res_w(J,T_m)^2/2^(2M(m-1)).                        (13)
```

This is `(TCN10)`. Since `2M` is a power of two, `(TCN9)` also proves the
printed odd-prime divisibility equivalence for the trace factors.

Let `theta^2=2`. Chebyshev doubling factors as

```text
T_(2M)=2T_M^2-1=(theta T_M-1)(theta T_M+1).          (14)
```

Multiplicativity of the resultant gives `R_-=S_-S_+`. The nontrivial
automorphism `sigma` of `Q(theta)` sends

```text
theta T_M-1 |-> -theta T_M-1=-(theta T_M+1).
```

Since `J` has degree `M`, scaling the second resultant input by `-1`
multiplies it by `(-1)^M`. Hence

```text
sigma(S_-)=(-1)^M S_+,
Norm(S_-)=S_-sigma(S_-)=(-1)^M R_-.                 (15)
```

This proves `(TCN11)--(TCN12)`. On the official branch, `8M` divides the
base-field multiplicative-group order. The trace of a primitive eighth root
supplies `theta`, so both factors are defined over the official field.

At `M=2^35`, the orders in `(TCN3)` and `(TCN5)` are respectively `2^38`
and `2^2,...,2^37`, the latter containing `36` levels. QED.
