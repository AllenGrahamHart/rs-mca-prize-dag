# Proof

Put

```text
r=5406977=256*21121+1,       g=3,
u=g^42242=3758939 mod r,
omega=g^256=2166434 mod r.
```

Exact trial division proves that `r` and `ell=21121` are prime. The checks

```text
g^(r-1)=1,
g^((r-1)/2)!=1,
g^((r-1)/ell)!=1                 mod r
```

show that `g` has order `r-1`. Hence `u` has order 128 and `omega` has
order `ell`.

For `s=1,3,...,63`, let `phi_s` be reduction at the degree-one prime of
`Q(zeta_128)` above `r` defined by `zeta_128 -> u^s`. On elements nonzero at
these primes define

```text
Psi(x)=product_(s=1,3,...,63) phi_s(x)^256 in mu_ell(F_r).   (RO2)
```

This is a multiplicative character. Since `r-1=256*ell`, it kills every
`ell`th power. It also kills every root of unity of `Q(zeta_128)`.

By `e1_conductor128_full_unit_circular_basis`, it remains to check the 31
units

```text
eta_a=zeta^((1-a)/2)(1-zeta^a)/(1-zeta),
a=3,5,...,63.
```

Direct modular arithmetic gives

```text
Psi(eta_a)=1                         for every a=3,5,...,63. (RO3)
```

Thus `Psi` kills the full global unit group.

Finally reduce the 32 Jacobi sums `(SR2)` directly through each `phi_s`,
form the ratios with their conjugates, and use the 32 exponents `(SR5)`.
No Jacobi factor vanishes modulo `r`, and exact arithmetic gives

```text
Psi(alpha)=500235=omega^20582 != 1 mod r.             (RO4)
```

The repository verifier recomputes `(RO3)--(RO4)` from the defining
character sums; it does not import a class-group coordinate or a discrete
logarithm transcript.

The Stickelberger relation gives `(alpha)=I^(2ell)`. If `I=(delta)` were
principal, then

```text
alpha/delta^(2ell)
```

would be a global unit. All terms would be nonzero at the 32 auxiliary
primes, so applying `Psi` would give `Psi(alpha)=1`, contrary to `(RO4)`.
Therefore `I` is nonprincipal. If `J_63` were principal, then
`I=J_63/bar(J_63)` would be principal, so `J_63` is nonprincipal as well.
QED.
