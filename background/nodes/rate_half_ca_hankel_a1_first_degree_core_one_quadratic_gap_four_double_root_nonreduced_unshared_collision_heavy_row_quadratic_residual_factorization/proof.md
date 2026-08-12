# Proof

The split biform is bihomogeneous of parameter degree `e-2`. Its
specialization at the projective point `x_*` is nonzero and therefore is a
binary form

```text
R(t):=G(t,x_*)
```

of exact projective degree `e-2` and exact order two at `tau` by the
barycentric split-jet gate.

For an assigned center `gamma`, the three-center source partition gives

```text
ell_gamma divides g_*       iff r_gamma=1.
```

Since `sum_(gamma in A)r_gamma=d_A`, the center part of `g_*` is exactly

```text
J_*=gcd(Lambda,g_*),       deg J_*=d_A.            (1)
```

Let `delta` be a root of `g_off=g_*/J_*`. It is a supported noncenter
slope, hence an off-line supported slope at which `x_*` is padded-heavy.
The all-excess vertical-fiber factorization contains the complete padded
factor:

```text
G(delta,X)=zeta_delta A_delta(X)H_delta(X)R_delta(X).
                                                               (2)
```

Thus `G(delta,x_*)=0`. The form `g_off` is squarefree, so all of its
`e-6-d_A` roots divide `R` and

```text
R=g_off K_(4+d_A),       deg K_(4+d_A)=4+d_A.     (3)
```

Unsharedness gives `g_*(tau)!=0`, and the collision parameter is not a
center, so `g_off(tau)!=0`. Therefore the exact order two of `R` at `tau`
is the exact order two of `K_(4+d_A)`. The degree-two form `S_B` has divisor
`2[tau]`, so

```text
K_(4+d_A)=S_BT_(2+d_A),
deg T_(2+d_A)=2+d_A,       T_(2+d_A)(tau)!=0.      (4)
```

This proves `(HQR1)--(HQR3)`; the gcd assertion follows because `S_B` has
no root other than `tau`.

The barycentric gate identifies `R` with `R_lambda`, giving
`(HQR4)--(HQR5)`. Polynomial remainder is linear, so

```text
rem_(H_row)(R_lambda)
 =sum_(x in X)b_x lambda_x rem_(H_row)(P_x)
 =B_row lambda.                                    (5)
```

Since `deg H_row=(e-6-d_A)+2=e-4-d_A`, its remainder has that many
coefficients. Equation `(5)` proves `(HQR6)--(HQR7)`. QED.
