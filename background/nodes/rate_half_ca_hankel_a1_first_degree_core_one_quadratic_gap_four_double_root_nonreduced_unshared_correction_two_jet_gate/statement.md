# `A=1` quadratic nonreduced unshared-correction two-jet gate

- **status:** PROVED
- **closure:** exact two-scalar obstruction to the cubic quotient at an unshared double correction root
- **consumer:** `rate_half_band_crossing_location`

Retain the double-root extremal profile and suppose

```text
S_B=c_S ell_tau^2,       g_*(tau)!=0.               (HNJ1)
```

Let `z=ell_tau` be a local base parameter. Then

```text
ord_tau Q(t,x_*)=6,
ord_tau D_1=4.                                      (HNJ2)
```

For the canonical divided heavy row and moments `F_i` of `(HSJ2)`,

```text
z^2 divides F_0.                                    (HNJ3)
```

Define the two obstruction jets

```text
kappa_2=[z^2]F_0,
kappa_3=[z^3]F_0.                                   (HNJ4)
```

The exact recurrence gives, for `s=2,3`,

```text
[z^s]F_i=x_*^i kappa_s.                            (HNJ5)
```

Moreover,

```text
kappa_2=kappa_3=0
 iff D_1 divides F_0 locally at tau
 iff D_1 divides every F_i locally at tau.         (HNJ6)
```

On the vanishing branch the degree-at-most-three cubic quotient extends
through `tau`, and the regular local Smith type is `[4]`. Otherwise the
first nonzero one of `kappa_2,kappa_3` is the exact obstruction to the
canonical quotient.

## Scope

The theorem does not prove either jet vanishes. It treats an unshared
nonreduced correction root only; a root also lying on `g_*` has a different
determinant order. No branch structure of the normalized correction divisor
is assumed.
