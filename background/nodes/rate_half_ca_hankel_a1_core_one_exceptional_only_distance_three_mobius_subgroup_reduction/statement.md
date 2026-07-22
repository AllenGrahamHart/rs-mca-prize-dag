# `A=1` core-one distance-three Mobius subgroup reduction

- **status:** PROVED
- **closure:** proof using a published subgroup-curve bound
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_pair_locator_mobius_dichotomy`,
  `rate_half_residual_prime_field_collapse`

Retain the official rank-two pair-locator branch. Thus

```text
N=2^41,       e=2^38-1,       H=mu_N subset F_p^*,
p>2^167,      N|(p-1),
```

and one Mobius involution pairs the `2e` exceptional roots in `H`. Write its
pair equation as

```text
beta xy+alpha(x+y)=gamma,
alpha^2+beta gamma!=0.                               (MSR1)
```

Then the involution is necessarily one of the two dihedral forms

```text
y=-x,                                                (MSR2)
xy=c       for one c in H.                           (MSR3)
```

Equivalently, every non-dihedral rank-two pair-locator packet is empty on
the official row. The theorem does not exclude the antipodal or
constant-product pairings in `(MSR2)--(MSR3)`.
