# Budget-three antipodal harmonic-torsion characteristic sieve

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_pure_harmonic_fermat_router`

Let `N=2^k` with `k>=3`. Over a characteristic-zero field, take

```text
a_0,a_1,a_2,a_3 in mu_N
```

with pairwise distinct squares. Then the four lifts cannot be harmonic:

```text
cr(a_0,a_1;a_2,a_3) != -1.                            (HTS1)
```

In particular, the harmonic lift condition `(HFR2)` has no nondegenerate
characteristic-zero point at the official pure boundary `N=2d=2^40`.
Therefore the pure harmonic-Fermat packet is empty in characteristic zero,
before its degree-`2^39` Fermat decomposition is considered.

There is an exact finite-characteristic certificate endpoint. Normalize
`a_0=1`, put `(x,y,w)=(a_1,a_2,a_3)`, and define

```text
h=2x+2yw-y-xy-w-xw,                                   (HTS2)

f_1=x^2-1,          f_2=y^2-1,          f_3=w^2-1,
f_4=x^2-y^2,        f_5=x^2-w^2,        f_6=y^2-w^2.  (HTS3)
```

For the official `N=2^40`, the integer ideal

```text
I_H=(x^N-1,y^N-1,w^N-1,h,u_1f_1-1,...,u_6f_6-1)      (HTS4)
```

has no characteristic-zero point and is the unit ideal over `Q`. Hence there
are a nonzero integer `Delta_H` and integer polynomials `H_j` with

```text
Delta_H=sum_j H_j E_j,                                (HTS5)
```

where the `E_j` are the generators in `(HTS4)`. Every finite characteristic
supporting a nondegenerate official harmonic lift divides any checked
`Delta_H`.

The powers in `(HTS4)` have a sparse presentation. For each
`z in {x,y,w}`, introduce `z_1,...,z_39` and impose

```text
z_1=z^2,       z_(t+1)=z_t^2 (1<=t<39),       z_39^2=1. (HTS6)
```

Together with `(HTS2)` and the six inverse equations in `(HTS3)`, this gives
exactly `126` variables and `127` equations, all of total degree at most
three. This sparse ideal is scheme-isomorphic to `(HTS4)`.

Finite-characteristic harmonic lifts genuinely occur at small orders, so
this theorem does not promote the rate-half target. Computing and factoring
`Delta_H`, then excluding its official compatible characteristics, remains
open. No Fermat decomposition or dense official-degree polynomial is needed
unless a characteristic survives this earlier sieve.
