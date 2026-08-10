# Preregistration: quartic FR countermodel biform lift

Date: 2026-08-10

## Question

The proved incidence-only `(FR)` route fence uses four copies of
`F_257^*`.  Under the natural smooth-domain identification

```text
(i,x) |-> tau_i x in mu_1024,
```

can its block-incidence rows be the roots of a biform of parameter degree
`m=64` and locator degree at most `rho=255`, up to arbitrary nonzero row
scales?

## Registered outcome test

For each of the three copies untouched by the single deleted incidence, the
monic parameter row is

```text
P_(i,x)(Gamma)=(Gamma-x)^m-c_i.
```

If a lift exists, its leading two parameter coefficients give polynomials
`A,B` of locator degree at most `rho` satisfying

```text
B(tau_i x)=x A(tau_i x)
```

on three full cosets of `mu_256`.

- **Survival:** exhibit nonzero `A,B` satisfying these equations.
- **Obstruction:** prove the equations force `A=B=0` for every choice of
  multiplicative coset representatives `tau_i`.

## Scope discipline

An obstruction rules out only coset-preserving embeddings of this quartic
countermodel.  It does not prove `(FR)`, rule out an arbitrary permutation
of the incidence points, or close either rate-half budget.  A survival does
not by itself give a Hankel pencil; Hankel compatibility would remain to be
checked.
