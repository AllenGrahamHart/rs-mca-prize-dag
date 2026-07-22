# Claim contract - L1 interior BC floor routes to higher-shell Q

## Inputs

- strict-interior profile `d_1>=m-k+2`;
- the identity-prefix witness construction at `m'=k-1+d_1`;
- support-moment inversion and the complete-agreement gcd guard.

## Outputs

- every floor codeword has complete agreement exactly `m'>m`;
- all `binom(m',m)` level-`m` sub-supports fail the gcd guard;
- exact cancellation from `Z_m` under binomial inversion;
- unique routing to the higher shell `Z_m'`;
- identification of that higher shell as boundary Q.

## Consumer rule

Delete the realized `M_B^disc` floor rays before posing the L1
strict-interior count.  Do not impose `M_B^soft` as an unavoidable exact-L1
baseline: it is a soft raw-census model, not identified concrete mass.  Count
each floor codeword once at its complete level `m'` under boundary Q.  Do not
budget its sub-support multiplicity in both Q and BC.

## Nonclaims

The remaining guarded interior BC cell may be nonempty and field-sensitive.
No upper bound on it or on boundary Q is supplied.

## Falsifier

A floor codeword of degree at least `k`, a floor codeword with complete
agreement other than `m'`, a retained proper sub-support, nonzero inversion
contribution at `m`, or a higher-shell profile not equal to boundary Q.
