# KoalaBear m2 r2 residual source-cover twist classifier

- **status:** PROVED
- **scope:** the residual `Q_(a,b)` families with their actual second endpoint
- **dependency:**
  `rate_half_kb_m2_r2_dihedral_residual_quartic_singularity_atlas`
- **consumer:** `rate_half_band_closure`

Put the regular dihedral action in the form

```text
u(r)=1/r,       v(r)=lambda/r,       mu^2=lambda,
a=lambda+lambda^(-1),       d=mu+mu^(-1).
```

Then `d^2=a+2`. Let `Z_0=r/mu+mu/r` be the standard quotient by `v`, and
write the actual second endpoint coordinate as `Z=ell(Z_0)` for a projective
map `ell`.

Equality of the normalized coefficient quotient and actual endpoint source
covers forces

```text
ell^(-1)({2,b}) = roots of
Q_b(z)=z^2-b*d*z+b^2+d^2-4.                        (KBMT-1)
```

The quadratic is squarefree for every allowed parameter. Moreover,

```text
Q_b(2)=(b-d)^2,       Q_b(-2)=(b+d)^2.             (KBMT-2)
```

The source V4 branch passports therefore determine the source genus exactly:

```text
g(Gamma)=0  iff  b^2=a+2,
g(Gamma)=1  iff  b^2!=a+2.                         (KBMT-3)
```

Thus the relative second-endpoint twist no longer carries an unclassified
branch regime. Both regimes remain geometrically possible. This theorem
does not impose the common degree-30 function, six pole fibers, or complete
source locators, and closes no profile, owner, payment, row, or Prize problem.

## Falsifier

A cover with square-class ratio nonsquare, a root set in `(KBMT-1)` different
from the two endpoint branch preimages, or an actual source genus violating
`(KBMT-3)`.
