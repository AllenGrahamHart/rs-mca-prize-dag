# Elimination of the nonzero affine-reflection rational branch

- **status:** PROVED
- **scope:** the official dense-anchor branch after anchor-exchange
  synchronization

Suppose one rational exception packet has degree `e=2` and, after its
allowed affine slope normalization, its split fibers pair domain roots by

```text
x -> c-x,       c!=0.                                (AR2)
```

Then the dense-anchor route emits a packet with

```text
chi>=2299571.
```

Indeed, if no base or one-swap packet is high complexity, exchange
synchronization puts all `5524` pairwise-disjoint anchor exception locators
in the same pencil. One fiber of `(AR2)` has roots `x,y in H subset F_p`, so
`c=x+y in F_p^*`. The exact official census allows at most `1154` nonfixed
fibers for this `c`, contradicting `5524`.

This is a router into the existing high-complexity output, not a payment of
that output. The antipodal case `c=0`, other fractional involutions,
nonquadratic pencils, and primitive/nonaffine classes are not eliminated.

## Falsifier

Failure of global anchor synchronization, a nonzero affine reflection with
more than `1154` official-domain fibers, fewer than `5524` synchronized
anchor locators, or a claim that `c` need not lie in the base field despite
one split fiber having both roots in the base-field domain.
