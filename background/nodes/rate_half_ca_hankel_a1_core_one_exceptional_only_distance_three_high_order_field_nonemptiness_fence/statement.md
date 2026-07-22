# `A=1` distance-three high-order field nonemptiness fence

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_dihedral_boundary_order_router`

Put

```text
N=2^41,       e=2^38-1,       r=2^39-1,       B=2^39+1.
```

Both field-order strata retained by the dihedral boundary-order router occur
inside the exact adjacent-row interval. Explicitly, the integers

```text
p_(e/3)=187072209578695855896992631304045809902474217127937,
p_e    =187072209578695855896992636341236724945103917940737
```

are prime and satisfy

```text
floor(p_g/2^128)=B,       N | (p_g-1),
gcd(e,p_g-1)=g,           gcd(r,p_g-1)=1
                           for g in {e/3,e}.          (HOF1)
```

Thus the two high-order field strata are arithmetically nonempty even where
the dual `r`th-power residue gate is automatic. Field-order congruences,
primality, and that residue gate alone cannot exclude the surviving rank-two
branch. This fence does not construct a distance-three support packet over
either field.
