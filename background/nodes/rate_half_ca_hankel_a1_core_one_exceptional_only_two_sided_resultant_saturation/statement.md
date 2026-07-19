# `A=1` core-one exceptional-only two-sided resultant saturation

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_infinity_coefficient_rigidity`

Retain the exceptional-only corrected square. Put

```text
n_X=deg P_X=D_0-1,       P=P_cl E,
deg P=T,                 deg_X Q=r,       deg_parameter Q=e. (ERS1)
```

Use the monic-first resultant conventions

```text
Res_t(P,F)=product_(gamma:P(gamma)=0)F(gamma;X),
Res_X(P_X,F)=product_(x:P_X(x)=0)F(t;x).              (ERS2)
```

There are nonzero field scalars `c_t,c_X` such that

```text
Res_t(P,Q)=c_t P_X^e,
Res_t(P,A_1)=c_t^(-1) P_X^(T-e),                      (ERS3)

Res_X(P_X,Q)=c_X P_cl^r E^(r-1),
Res_X(P_X,V)=c_X^(-1) P_cl^(n_X-r) E^(n_X-r+1).      (ERS4)
```

On the official profile the complementary exponents are

```text
T-e=3e+1,       n_X-r=6e+5,       n_X-r+1=6e+6.     (ERS5)
```

Thus both resultants of `Q` and both complementary resultants are pure
powers of the printed split locators; there is no unrecorded residual factor.
The constants occur in inverse pairs because

```text
Q A_1=P_X       at every root of P,
Q V=P           at every root of P_X.                (ERS6)
```

These identities are exact necessary certificates for the corrected square.
They do not imply that a biform with the prescribed resultants satisfies the
Hankel chain, the coefficient identities, or irreducibility, and they do not
close the exceptional-only profile.
