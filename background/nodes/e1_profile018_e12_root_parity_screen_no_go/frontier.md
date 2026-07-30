# Frontier

Do not attempt to close profile `(0,18)` by an autocorrelation-only
energy/parity/root/positivity screen: the explicit energy-twelve target
survives all four conditions.

The exact norm of the displayed target is below the official interval, so
exact norm is already selective. The other missing gate is coefficient
realization:

```text
F has 18 distinct coefficients in {+1,-1},
F(X)F(X^-1)-18 has the retained autocorrelation,
F has local multiplicity one.
```

For a broad autocorrelation generator, exact resultants may be screened before
realization. For a coefficient generator, compute them only after a genuine
singleton state is found. In either order, group survivors by the common
quotient `p=Norm(F)/514`.
