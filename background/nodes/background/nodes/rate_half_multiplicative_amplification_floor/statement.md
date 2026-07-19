# Rate-half cap-row multiplicative-amplification floor

- **status:** PROVED
- **consumer:** `rate_half_band_closure`
- **scope:** the current rate-half cap proxy `n=2^41`, `k=2^40`, box charge
  `2^256`, trigger `2^216`, and `sigma*=8,592,912,738`.

For a power-of-two quotient scale `c=2^e`, put

```text
N_e = n/c,
d_e = ceil(sigma*/c),
F_e = C(N_e,N_e/2+d_e) / 2^(256(d_e-1)).
```

Among every scale `1<=e<=40`,

```text
F_e <= C(128,65),
```

with equality at `e=34`.  Therefore any proposed averaged construction whose
only effect is to multiply one of these one-scale floor counts by an integer
factor `L` needs

```text
L >= floor(2^216/C(128,65)) + 1
```

before it can cross the strict cap-row trigger.  This is about `2^92` shared
mass.  The theorem does not exclude a genuinely joint construction that
changes the box exponent, creates new slopes, or is not a multiplicative
amplification of a single-scale floor.
