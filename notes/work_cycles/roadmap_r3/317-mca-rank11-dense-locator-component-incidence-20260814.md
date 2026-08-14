# Cycle 317: MCA rank-11 dense-locator component incidence (2026-08-14)

The new PROVED node
`rate_half_mca_rank11_dense_locator_component_incidence_dichotomy` turns the
component frontier into a quantified aggregate incidence statement.

Remove the eighteen dense-pair slopes and normalize every remaining
deviation by their locator:

```text
R_gamma=(h_gamma'-a_0'-gamma b_0')/q(gamma) in V',
deg q=18.
```

The normalized vectors still span `V'`. Rich agreement at coordinate `x`
is linear in `R` and degree 18 in the slope. Eleven coordinate equations on
`P^1 x P^10` therefore have isolated-point Bezout number

```text
(18H_Z+H_R)^11=198 H_Z H_R^10.
```

Generic perturbation bounds isolated multiplicity by 198 even in the
presence of excess components. Summing over coordinate tuples gives the
uniform endpoint

```text
ceil(198*C(n',11)/C(m',11))
 <=2526815879272440,
```

with the maximum at shortened dimension `K'=10`.

After deducting the exact near charge and eighteen anchors, an unsafe family
has at least `274980728111260126` normalized records. Consequently at least
`990810934/10^9` of all record/eleven-subset incidences lie on a
positive-dimensional component through the rich point. Full evaluation rank
gives an affine-owner clone; deficient rank gives a kernel fiber. One lane
carries at least `495405467/10^9` of all incidences.

The theorem deliberately does not turn incidence density into record or
component density. Overlap multiplicity is the next exact target.

Focused verification:

```text
RATE_HALF_MCA_RANK11_DENSE_LOCATOR_COMPONENT_INCIDENCE_DICHOTOMY_PASS
  isolated=2526815879272440 component_ppb=990810934 controls=7/7
RATE_HALF_MCA_RANK11_DENSE_LOCATOR_COMPONENT_INCIDENCE_DICHOTOMY_AUDIT_PASS
  isolated=2526815879272440 component_ppb=990810934 controls=5/5
```

No Modal computation was used.

```text
start:                   e30d06ff5
DAG delta:               +1 PROVED incidence dichotomy,
                         +4 requirement edges, +1 evidence edge
critical status delta:   none
upstream terminal delta: aggregate rank-eleven obstruction split into
                         quantified owner and kernel incidence lanes
delta-star movement:     none
compute:                 constant-size exact binomial arithmetic only
next route action:       bound component overlap multiplicity in the
                         owner or kernel lane
```
