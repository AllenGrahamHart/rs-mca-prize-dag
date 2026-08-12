# Proof

The split biform is bihomogeneous of parameter degree `e-2`. Its
specialization at the projective point `x_*` is nonzero and therefore is a
binary form of exact degree `e-2`. Thus

```text
R(t):=G(t,x_*)
```

has exact projective degree `e-2` and exact order two at `tau`
by the barycentric split-jet gate.

Let `delta` be a root of `g_*`. By definition, `delta` is a supported
slope at which `x_*` is padded-heavy. The all-excess vertical-fiber
factorization contains the complete padded factor:

```text
G(delta,X)=zeta_delta A_delta(X)H_delta(X)R_delta(X).
                                                               (1)
```

Hence `G(delta,x_*)=0`. The form `g_*` is squarefree, so all of its
`e-6` roots divide `R` and

```text
R=g_*K_4,       deg K_4=4.                        (2)
```

Unsharedness gives `g_*(tau)!=0`. Therefore the exact order two of `R` at
`tau` is also the exact order two of `K_4`. The degree-two form `S_B` has
divisor `2[tau]`, so

```text
K_4=S_BT_2,       deg T_2=2,        T_2(tau)!=0.  (3)
```

This proves `(HQR2)--(HQR3)`; the gcd assertion follows because `S_B` has
no root other than `tau`.

The barycentric gate identifies `R` with `R_lambda`, giving `(HQR4)--
(HQR5)`. Polynomial remainder is linear, so

```text
rem_(H_NR)(R_lambda)
 =sum_(x in X)b_x lambda_x rem_(H_NR)(P_x)
 =B_NR lambda.                                     (4)
```

Since `deg H_NR=(e-6)+2=e-4`, its remainder has `e-4` coefficients.
Equation `(4)` proves `(HQR6)--(HQR7)`. QED.
