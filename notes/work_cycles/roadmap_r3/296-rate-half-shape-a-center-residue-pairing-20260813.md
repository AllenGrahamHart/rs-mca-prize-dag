# Cycle 296: rate-half Shape-A center residue-pairing router

## Result

The three locator-interpolation maps now have one exact common language.
For each center `gamma`, the symmetric residue form

```text
beta_gamma(f,h)=sum_(x in M_gamma)
 R_gamma(x)f(x)h(x)/[G(gamma,x)L_Mgamma'(x)]
```

has rank `n` on `S_n` and radical exactly `G(gamma,X)`. Its restriction
to the common coefficient space `W_X` is the class map `T_gamma`, up to a
nonzero scalar.

If

```text
kappa=dim(intersection_gamma ker T_gamma),
```

then

```text
rank T=n+1-kappa,
r>=ceil((5e-3-2kappa)/6).
```

At the current lower rank boundary `r=(e+1)/2`, survival requires
`kappa>=e-3=183251937960`. Proving `kappa<=e-4` raises that floor by one.

**Cycle-300 correction:** the Padé-parity quotient theorem subsequently
proved `kappa=e-3+xi` with `xi>=0`. The upper-bound sentence is therefore a
counterfactual calibration; it is not a live dimension-only route.

## Audit

The large class uses the full two-dimensional dual-RS parity space and
the proved coprimality of `X-x_*` with `G(gamma_0,X)`. The constant-size
finite-field replay checks rank, radical, restricted rank, and a
zero-common-kernel control. The latter is a route guard: the residue forms
alone do not force the official macroscopic intersection.

## Status

```text
new node:               PROVED
critical status effect: none
compute:                local constant-size only
next exact target:      bound kappa using the primitive source-pencil
                        relation and retained Hankel/source-Gram packet
```
