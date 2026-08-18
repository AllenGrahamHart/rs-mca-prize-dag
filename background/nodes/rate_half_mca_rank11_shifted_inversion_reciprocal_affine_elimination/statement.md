# Reciprocal-affine shifted-inversion elimination

- **status:** PROVED
- **scope:** the quadratic shifted-inversion survivor with at least 4370
  disjoint official-domain fibers

Retain the alternatives from the quadratic survivor router. In the shifted
branch write

```text
(x+tau)(y+tau)=kappa,       tau,kappa!=0,
lambda=kappa/tau^2.
```

Then

```text
lambda!=1.                                             (RA1)
```

Indeed, the reciprocal degeneration `lambda=1` is a nonzero affine
reflection after coordinatewise inversion. It has at most `2308` nonfixed
graph points and at most `1154` disjoint fibers, while the synchronized
survivor requires at least `8740` graph points and `4370` fibers.

The remaining exact route is therefore:

1. an admissible packet has `chi>=2299571`;
2. the synchronized survivor has degree `1,3,...,11`;
3. its quadratic involution is antipodal or constant-product; or
4. it is shifted inversion with `tau,kappa!=0`, `lambda!=1`, and at least
   `8740` nonfixed graph points.

No remaining class is paid.

## Falsifier

Failure of inversion to preserve the official subgroup or disjointness;
failure of `kappa=tau^2` to become `u+v=-1/tau`; an affine-reflection cap
above 1154 fibers; or omission of any unpriced alternative.
