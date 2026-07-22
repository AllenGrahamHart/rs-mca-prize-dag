# Proof

Both `H_lambda` and `H_nu` are linear combinations of
`q_1,...,q_e`, hence belong to the common Hankel-isotropic coefficient plane.
The `M_1` source form of that isotropy is

```text
sum_(A(a)=0) alpha_a H_lambda(a)H_nu(a)
 +sum_(B_T(t)=0) omega_t H_lambda(t)H_nu(t)=0.        (1)
```

The annihilating-pair router gives `A | H_lambda H_nu`, so the first sum in
`(1)` vanishes. The Forney normal form gives

```text
omega_t=Phi(t)/(A(t)^2B_T'(t)).                      (2)
```

Substitute `H_lambda H_nu=AK_lambda,nu` and `(2)` into the remaining sum in
`(1)`. One factor of `A(t)` cancels, proving `(HNR2)`.

The support is disjoint from the exceptional roots, so `A` is a unit modulo
`B_T`. Put

```text
R=rem_(B_T)(Phi K_lambda,nu A^(-1)).                 (3)
```

The Lagrange leading-coefficient identity for the monic squarefree
degree-`h` polynomial `B_T` says

```text
[X^(h-1)]R=sum_(B_T(t)=0) R(t)/B_T'(t).              (4)
```

At a support root, `(3)` evaluates to
`Phi(t)K_lambda,nu(t)/A(t)`. Thus `(4)` is exactly the left side of
`(HNR2)`, proving `(HNR3)`. In the exact-half branch, cancellation of
`D_uD_v=A` gives the displayed specialization.

For completeness, apply the global residue theorem to

```text
Phi(X)K_lambda,nu(X)/(A(X)B_T(X)) dX.                (5)
```

The numerator has degree at most
`(h-3)+(2e+2)=h+2e-1`, while the monic denominator has degree `h+2e`.
The residues at the support roots sum to zero by `(HNR2)`. At an exceptional
root, `(QFN5)` turns the residue into

```text
Phi(a)K(a)/(A'(a)B_T(a))=beta_a q_1(a)K(a).         (6)
```

The sum of all finite residues of `(5)` is the coefficient of
`X^(h+2e-1)` in `Phi K`. This proves `(HNR4)`. Since `deg Phi=h-3` and
`lc(Phi)=Theta_2`, the coefficient is zero for `deg K<=2e+1` and is
`Theta_2 lc(K)` at degree `2e+2`, proving `(HNR5)`. Every cross pair from
the two shortening spaces has zero product on the exceptional roots, so the
same argument applies entrywise and proves `(HNR6)`. QED.
