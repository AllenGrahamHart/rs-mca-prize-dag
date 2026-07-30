# KoalaBear m2 r4 diagonal c2 (1,1,2) source-line colored quotient compiler

- **status:** PROVED
- **scope:** saturated `(1,1,2)` packets in the diagonal source-line branch
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_saturated_defect_classifier` and
  `rate_half_kb_m2_u2_colored_source_resultant_split_compiler`
- **consumer:** `rate_half_band_closure`

Let

```text
K_Lc={k in K: tau(k) in L^c},       Omega=tau(K_Lc).
```

Then `|K_Lc|=|Omega|=2`. All four component stars over the two complete
`K_Lc` source fibers are `J_0-J_1`. Individual-star equivariance transports
them to the four `I-J` stars, which are exactly the two complete source
fibers over `Omega`. Therefore

```text
C_H(X) ~ chi_Omega(psi(X)),       div(chi_Omega)=Omega. (KBQ2-1)
```

Both fibers over `Omega` are unramified, because the universal colored
divisor `C_H` is squarefree. The quotient pair is explicit:

```text
L=I:    Omega=J_1;
L!=I:   Omega={xi,ell},
```

where in the second line `tau(eta) in K` and `ell` is the other crossing
label in `J intersect L^c`.

Let `K_5(W)` and `R_7(W)` be the quotient locators on `K` and its
seven-label complement. The universal partial resultants descend to binary
forms `Q_J,Q_I` on the `W`-line with

```text
Q_J(W) ~ K_5(W)^2 chi_Omega(W),
chi_Omega(W) Q_I(W) ~ R_7(W)^2.                    (KBQ2-2)
```

This converts every saturated source-line `(1,1,2)` packet to one printed
quotient-quadratic system. It does not assert that `chi_Omega` is
`tau`-invariant in the near-aligned case, import coordinate-branch
`I,J` invariance, delete any packet or row, apply to the biquadratic branch
or exceptional orbit, or prove an owner, payment, row, or Prize result.

## Falsifier

A saturated source-line packet with `|K_Lc|!=2`, an `I-J` star outside the
two complete `Omega` fibers, a ramified `Omega` fiber, or partial resultants
violating `(KBQ2-2)`.
