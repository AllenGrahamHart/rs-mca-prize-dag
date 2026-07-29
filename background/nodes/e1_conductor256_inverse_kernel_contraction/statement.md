# Conductor-256 inverse-kernel contraction

- **status:** PROVED
- **closure:** directed interval arithmetic and Fourier inversion
- **dependency:** `e1_conductor256_character_eigenvalue_preflight`
- **consumer:** `e1_official_low_square_mass_pair_budget` (evidence)

Use `kappa_j`, `lambda`, and the zero-sum integer exponent vector `xi` from
the conductor-256 character router. Define the real inverse kernel

```text
q_r=(1/64) sum_(j=1)^63 exp(-2 pi i j r/64)/kappa_j,
                                                   r in Z/64Z.       (IKC1)
```

Certified outward intervals for all 64 entries have digest

```text
cea9045128e02103e878ef6a4694840fa97aa5a00cfd524da46f0b26347febbe
```

at 30 decimal places. They give

```text
min_r q_r > -0.057805,       max_r q_r < 0.031594,
(max q-min q)/2 < 0.044700,
sum_r |q_r| < 0.802.                                      (IKC2)
```

Fourier inversion and `sum_s lambda_s=0` imply, for every real constant `c`,

```text
xi_t=sum_s (q_(t+s)-c) lambda_s.                          (IKC3)
```

Taking the midpoint of the range in the coordinate estimate and `c=0` in
the aggregate estimate gives

```text
max_t |xi_t| < 0.044700 ||lambda||_1,
sum_t |xi_t| < 0.802 ||lambda||_1.                        (IKC4)
```

On the universal prize body `||lambda||_1<77.202`, so

```text
max_t |xi_t| < 3.451,       sum_t |xi_t| < 61.92.         (IKC5)
```

Because `xi` is integral and zero-sum, its `L1` norm is even. Hence every
live fixed-cofactor associate exponent satisfies the sharper exact bounds

```text
max_t |xi_t| <= 3,       sum_t |xi_t| <= 60.              (IKC6)
```

The prior Euclidean bound `sum_t xi_t^2<=101` remains available. These are
necessary filters only. They do not count associates, prove the 367-orbit
cap, pay lower profiles, or close E1.

## Falsifier

A live same-cofactor associate with an exponent outside `(IKC6)`, an inverse
kernel entry outside its certified interval, or a disagreement with `(IKC3)`.
