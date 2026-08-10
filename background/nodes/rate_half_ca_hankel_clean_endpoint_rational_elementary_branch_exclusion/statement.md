# Clean-endpoint rational elementary branch exclusion

- **status:** PROVED
- **closure:** adjunction genus contradiction
- **consumer:** `rate_half_band_crossing_location`

Retain the elementary-modification dichotomy for the absolutely irreducible
clean curve of bidegree

```text
(rho,m)=(4m-1,m),       m>1.
```

The two-section splitting

```text
K_Q=O(1) direct_sum O(-rho)^(m-1)                   (REB1)
```

is impossible. Consequently every clean endpoint failure must have the
unique-section splitting

```text
K_Q=O direct_sum O(1-rho)
    direct_sum O(-rho)^(m-2),                        (REB2)
h^0(K_Q)=h^0(C,O_C(P_*))=1.                         (REB3)
```

## Scope

This closes the smooth-rational elementary-modification branch. It does not
exclude `(REB2)`, which is now the sole clean Picard branch and still carries
the four-Hankel frame and saturated two-axis resultants.
