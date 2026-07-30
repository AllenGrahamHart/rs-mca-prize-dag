# KoalaBear m2 r2 dihedral degree-six common-pole exclusion

- **status:** PROVED
- **scope:** the residual `n=6` profile inside the actual KoalaBear
  `(m,r,delta)=(2,2,4)` row
- **dependencies:**
  `rate_half_kb_m2_r2_dihedral_outer_factor_reduction` and
  `rate_half_kb_m2_r2_dihedral_residual_source_cover_twist_classifier`
- **consumer:** `rate_half_band_closure`

Normalize a degree-six dihedral quotient by

```text
D_6(x)=x^6-6x^4+9x^2-2.
```

In the `n=6` pole profile, the six poles of the common degree-30 function
form one unramified fiber of each of the two degree-six quotients. Put

```text
P_c(x)=x^6-6x^4+9x^2-c,       c notin {0,4}.
```

The two pole-fiber structures give two fixed-point-free projective
involutions on `Z(P_c)`. Their perfect matchings either coincide, generate
`V4`, or generate `S3`. Exact binary-sextic coefficient comparison gives:

1. in the coincident case, the relative coordinate is `+/-x`, except for
   `c=27/8`, where `+/-3/(2x)` is also possible;
2. the distinct commuting case also forces `c=27/8`, but its second
   fixed-point-free involution does not carry any Dickson-six fiber;
3. the order-three case forces `c=756/125` and relative coordinate

```text
+/-g_t(x),       +/-g_t^2(x),
g_t(x)=t(x+t)/(t-3x),       5t^2+27=0.
```

For `n=6`, the source-cover classifier has `a=1`, `d^2=3`, and requires

```text
ell^(-1)({2,b})=roots(x^2-b*d*x+b^2-1).             (KBM6-1)
```

None of the six possible relative coordinates above satisfies `(KBM6-1)`.
The normalizer cases reduce to two elementary incompatible equations or a
nonzero univariate resultant. The order-three cases reduce to one exact
resultant chain whose final norm is

```text
71132574457861006005 = 1274367339 mod 2130706433 != 0.
```

Therefore the `n=6` profile is empty. Among the full-V4 residual dihedral
profiles, only `n=3` remains.

This theorem constructs no `n=3` profile or owner, moves no payment, and
closes no `m=2` type, endpoint row, KoalaBear row, or Prize problem.

## Falsifier

A second unramified Dickson-six structure outside the printed projective
atlas, a vanishing exceptional resultant in KoalaBear characteristic, or an
allowed relative coordinate satisfying `(KBM6-1)`.
