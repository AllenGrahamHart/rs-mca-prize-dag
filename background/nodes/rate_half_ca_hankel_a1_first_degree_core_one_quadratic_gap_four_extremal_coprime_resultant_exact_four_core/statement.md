# `A=1` quadratic extremal coprime-resultant exact four-core

- **status:** PROVED
- **closure:** all extensive intersection mass removed, leaving degree four
- **consumer:** `rate_half_band_crossing_location`

Retain the extremal profile and its nonzero parameter resultant `R_QG`.
Let

```text
P_R(X)=product_(delta off the center line)R_delta(X),
deg P_R=e-6-d_A.                                   (EFC1)
```

Then there is a nonzero polynomial `W_4(X)` with

```text
d_A=0:
R_QG(X)=L_M(X)^(e-2)(X-x_circ)^(e-3)P_R(X)W_4(X),

d_A=1:
R_QG(X)=L_M(X)^(e-2)P_R(X)W_4(X),                 (EFC2)

deg W_4<=4.                                        (EFC3)
```

There is also an exact projective statement. Let `C_Q,C_G` be the two
curves in `P^1 times P^1`, and subtract one copy of every common root of
`A_delta R_delta` over every off-line supported slope. The resulting
effective intersection cycle `Z_4` satisfies

```text
deg Z_4=4.                                         (EFC4)
```

On every off-line supported fiber, the complete common-root polynomial is
exactly `A_delta R_delta`; the residual `H_delta` is coprime to the
outside-support locator `B_delta`. Thus `W_4` carries no further common
point over a supported off-line slope. It can only carry excess local
intersection multiplicity at a mandatory root or common points over the
center-line, unsupported, or projective-infinity parameter fibers. Since
all actual-support roots are transverse, their excess charge is zero.

## Scope

The affine resultant quotient `W_4` can have degree below four when part of
`Z_4` projects to domain infinity. The projective residual cycle itself has
degree exactly four. The theorem does not classify those four units.
