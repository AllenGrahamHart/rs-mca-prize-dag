# Dihedral quotient pencils survive the twenty-fiber SPI interface

- **status:** PROVED
- **closure:** explicit inversion-quotient construction
- **consumer:** `rate_half_band_crossing_location` (evidence)
- **dependency:**
  `rate_half_mca_rank11_heavy_ruling_exception_split_pencil_normal_form`

Let `D=mu_N`, where `N` is a power of two, and let
`d in {1,2,4}` divide `N`. Put `M=N/d` and choose a nonsquare
`a in mu_M`. The involution

```text
iota(z)=a/z
```

has no fixed point on `mu_M`. For each of its `M/2` orbits
`{z,a/z}`, define

```text
u(X)=X^(2d)+a,       v(X)=X^d,
gamma_z=-(z+a/z).
```

Then

```text
u+gamma_z v=(X^d-z)(X^d-a/z).                       (DQ1)
```

Both factors split into `d` distinct roots in `mu_N`. Distinct involution
orbits give distinct slopes and disjoint root sets. Consequently the pencil
has exactly

```text
N/(2d)
```

pairwise-disjoint split squarefree fibers of degree `e=2d`. Moreover
`gcd(u,v)=1`, `max(deg u,deg v)=e`, and the locator scalar is the constant
one. Thus this is an exact instance of the bounded exception-SPI interface.

For the official `N=2^21` domain, degrees `e=2,4,8` give respectively

```text
1048576, 524288, 262144
```

disjoint fibers. In particular, the power-map examples are not the only
abstract survivors. A closing classification must include dihedral/Dickson
pullbacks as well as cyclic power pullbacks, or exclude their heavy-ruling
lifts using retained factor-owner, denominator, received-line, or chronology
semantics.

This is an algebraic route fence, not an actual MCA counterexample or a
construction of a received pair.

## Falsifier

Failure of `(DQ1)`; a fixed point of `z -> a/z` for nonsquare `a`; two
different involution orbits with the same slope; a root outside `mu_N`; a
repeated or shared root; or failure of the pinned official counts.
