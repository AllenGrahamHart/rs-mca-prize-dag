# `A=1` exceptional quotient-distance sharp ceiling

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_minimal_support_packing`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_distance_ceiling`

Retain the official exceptional-only high-distance branch with

```text
e=2^38-1,       r=2e+1,       h=delta_A(h_1).
```

For the `4e` ordinary clean locators, put

```text
a_z=|G_z intersect R_A|,       w_z=|G_z\R_A|=r-a_z.
```

Then the former ceiling sharpens by one:

```text
h<=3(e+1)/2-1=412316860415.                            (QSC1)
```

At equality, write

```text
H=3(e+1)/2,       h=H-1.
```

Exactly one of the following two complement/intersection profiles occurs.

1. No ordinary complement is minimal:

   ```text
   w_z=H,       a_z=(e-1)/2       for every z.          (QSC2)
   ```

2. One ordinary complement is minimal. Then one other complement has size
   `H+1`, and

   ```text
   {w_z}={H-1,H+1,H^(4e-2)},
   {a_z}={(e+1)/2,(e-3)/2,((e-1)/2)^(4e-2)}.           (QSC3)
   ```

The minimal complement in case 2 is one of the quotient leaders and its
fiber consumes `h-1` exceptional cancellations. This theorem does not
exclude the new endpoint or the lower high-distance interval.
