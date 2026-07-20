# `A=1` core-one exceptional quotient-distance router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quadratic_moment_pin`

Retain the exceptional polynomial

```text
A(X)=Q(gamma_0;X),       deg A=r-1,
```

its squarefree root set `R_A` in the residual evaluation domain, and the
first-order moment vector

```text
h_1=(h^(1)_0,...,h^(1)_(2r)).
```

For a residual-domain point `x`, put

```text
c(x)=(1,x,...,x^(2r))^T,
W_A=span{c(a):a in R_A}.
```

Define the quotient support distance

```text
delta_A(h_1)=min{|T|: T subset D_res\R_A,
                         h_1 in W_A+span{c(x):x in T}}.       (QDR1)
```

Then

```text
delta_A(h_1)>=3.                                           (QDR2)
```

If equality holds, the supporting triple

```text
T={x_0,x_1,x_2}
```

is unique. Modulo `W_A`, its coefficients are also unique and equal to

```text
omega_i=Theta_2 /
        (A(x_i)^2 product_(j!=i)(x_i-x_j)),       i=0,1,2.  (QDR3)
```

Equivalently, with `eta_i=omega_i A(x_i)^2`,

```text
eta_i=Theta_2/product_(j!=i)(x_i-x_j),
sum_i eta_i=sum_i x_i eta_i=0,
sum_i x_i^2 eta_i=Theta_2!=0.                         (QDR4)
```

Thus every exceptional-only first-order packet lies in the exhaustive
dichotomy

```text
one canonical three-point quotient chart,       or       delta_A(h_1)>=4.
                                                                    (QDR5)
```

This is a source-intrinsic sparsity router. It does not reconstruct the
lower Hankel chain or exclude either branch.
