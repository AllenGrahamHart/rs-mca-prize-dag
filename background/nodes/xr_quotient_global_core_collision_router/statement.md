# XR quotient images route by their global fiber core

- **status:** PROVED
- **closure:** proof
- **consumers:** `xr_tangent_support_mismatch_bridge`,
  `xr_highcore_collision_count`
- **dependencies:** `xr_quotient_max_agreement_first_match_owner`,
  `xr_target_budget_audit`

Let `C=RS[F,D,k]` have `n=|D|` and rate `k/n<=1/4`. Fix an initial
agreement `A_0=k+t_0` with `t_0>=1`, and consider rate-preserving quotient
scales `c|gcd(n,k)`. Let `Z_Q` be the distinct maximum-agreement quotient
slopes encountered by the agreement induction from `A_0`, first-matched
across thresholds and scales as in
`xr_quotient_max_agreement_first_match_owner`.
All supports in this quotient currency are support-wise noncontained: no
codeword pair explains both received words on the whole support.

If `z in Z_Q` is paid at maximum agreement `B=k+t_z` and scale `c`, activity
gives `t_z<c`. Its full agreement support therefore has the form

```text
S_z=K_z union T_z,
|K_z|=k,       K_z is a union of k/c complete c-fibers,
|T_z|=t_z<c.                                             (QCR1)
```

Use a fixed scale order and group slopes by the global key `(c,K_z)`. Let
`Z_single` contain slopes whose key occurs once, and let `Z_collision`
contain all slopes whose key occurs at least twice. Then

```text
|Z_single|
 <= sum_(c|gcd(n,k), c>t_0) C(n/c,k/c)
 <= B_quot_ub(A_0).                                     (QCR2)
```

Every still-live generic-branch slope in `Z_collision` shares a size-`k`
core with another live slope and is therefore in the exact class quantified
by `xr_highcore_collision_count` (P-A). On the complementary nongeneric
branch it is retained by `xr_tangent_support_mismatch_bridge`; it is no
longer an independent quotient-image currency.

Thus the existing conservative quotient slot pays every globally singleton
fiber core once. Quotient multiplicity is routed into the already named
common-core residual rather than multiplied by thresholds, tails, or support
counts.

This theorem does not prove the P-A bound, aggregate the nongeneric
common-core branch, prove a generic-chart bound, or close XR.
