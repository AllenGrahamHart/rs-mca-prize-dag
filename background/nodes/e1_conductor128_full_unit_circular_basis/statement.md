# Conductor-128 full-unit circular basis

- **status:** PROVED
- **closure:** descent from Miller's conductor-256 theorem plus the
  Kummer-Sinnott unit-index formula

Put

```text
K=Q(zeta),        zeta=zeta_128,
R=Z[zeta].
```

For every odd `a` with `3<=a<=63`, define

```text
eta_a=zeta^((1-a)/2) (1-zeta^a)/(1-zeta).           (C128U1)
```

Then

```text
R^x = mu_128 x <eta_3,eta_5,...,eta_63>.            (C128U2)
```

Equivalently, every unit has a unique representation

```text
u=zeta^j product_(a=3,5,...,63) eta_a^x_a,
j mod 128,       x_a in Z.                          (C128U3)
```

The product in `(C128U2)` is internal after quotienting by `mu_128`.

## Falsifier

A unit outside the displayed subgroup, or a nontrivial integral relation
among the 31 displayed classes modulo roots of unity.
