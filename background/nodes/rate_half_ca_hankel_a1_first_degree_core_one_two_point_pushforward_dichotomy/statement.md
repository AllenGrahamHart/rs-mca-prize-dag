# `A=1` core-one two-point pushforward dichotomy

- **status:** PROVED
- **closure:** rank-two elementary modification over the domain projection
- **consumer:** `rate_half_band_crossing_location`

Retain the two-point normal form and let

```text
pi:C -> P^1_X,       d=3e-2,
L_2=O_C(rho+2,-e-1)=O_C(P_alpha+P_beta).              (TPD1)
```

Both points lie over `x_*`. The finite flat pushforward satisfies

```text
pi_*O_C=O direct_sum O(-d)^(e-1),                     (TPD2)
```

and `K_2=pi_*L_2` is a rank-two positive elementary modification at `x_*`:

```text
0 -> O direct_sum O(-d)^(e-1)
  -> K_2 -> k_(x_*)^2 -> 0.                           (TPD3)
```

Exactly one of the following splittings occurs:

```text
PENCIL:
K_2=O(1) direct_sum O(1-d)
          direct_sum O(-d)^(e-2),       h^0(K_2)=2;

CANONICAL:
K_2=O direct_sum O(1-d)^2
          direct_sum O(-d)^(e-3),       h^0(K_2)=1.   (TPD4)
```

In the first branch, `L_2` has a degree-at-most-two pencil after removing
its common base divisor. In the second, its only section up to scalar is the
canonical section cutting out `P_alpha+P_beta`.

## Scope

The theorem does not exclude either splitting on the reduced mixed kernel
curve. In particular, negative total degree of the kernel of the relative
multiplication map is not an injectivity proof.
