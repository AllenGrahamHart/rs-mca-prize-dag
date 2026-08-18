# Shifted-inversion product-energy ledger

- **status:** PROVED
- **scope:** the shifted quadratic output of the quadratic survivor router

For nonzero `tau,kappa in F_p`, put

```text
R(tau,kappa)=#{(x,y) in H^2:(x+tau)(y+tau)=kappa},
F(tau,kappa)=#{x in H:(x+tau)^2=kappa},
I(tau,kappa)=R(tau,kappa)-F(tau,kappa).
```

Then `I` is the number of ordered nonfixed graph points and `I/2` is the
number of two-cycle fibers. Let `z_tau=1` when `-tau in H` and zero otherwise.
The exact first moments are

```text
sum_(kappa!=0) R(tau,kappa)=(N-z_tau)^2,
sum_(kappa!=0) F(tau,kappa)=N-z_tau,
sum_(kappa!=0) I(tau,kappa)=(N-z_tau)(N-z_tau-1).      (PE1)
```

Writing `A_tau=(H+tau)\{0}`, the exact second moment is

```text
sum_(kappa!=0) R(tau,kappa)^2=E_x(A_tau),             (PE2)
```

the multiplicative energy of the shifted subgroup. For every `h in H`,

```text
R(h*tau,h^2*kappa)=R(tau,kappa),
F(h*tau,h^2*kappa)=F(tau,kappa),
I(h*tau,h^2*kappa)=I(tau,kappa).                      (PE3)
```

Thus a complete parameter search reduces the shift to 1016 multiplicative
`H`-cosets, while `lambda=kappa/tau^2` is invariant.

If `A=tau^2-kappa` is nonzero, coordinatewise inversion on `H^2` gives

```text
R(tau,kappa)=R(tau/A,kappa/A^2),
F(tau,kappa)=F(tau/A,kappa/A^2),                      (PE4)
```

and preserves `lambda`. If `A=0`, inversion instead gives the affine
reflection equation

```text
u+v=-1/tau.                                           (PE5)
```

These are exact reductions, not a bound on the general shifted class.

## Falsifier

A mismatch between graph points and product representations, an odd `I`, a
first moment different from `(PE1)`, a second moment different from
multiplicative energy, failure of scaling or inversion, or any claim that an
energy asymptotic controls the maximum without an additional argument.
