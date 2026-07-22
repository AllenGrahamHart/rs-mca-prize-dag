# L1 tame fixed-petal refinement census

- **status:** PROVED
- **role:** remove tame quotient-polynomial multiplicity from the fixed-petal
  smaller-fiber branch
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Refinement contract

Let `K` be a finite field of characteristic `p`, let `H subset K` be the
evaluation domain, and fix one maximal sunflower source with pairwise
disjoint petals

```text
T_1,...,T_(M_src),       |T_i|=ell.                    (TR1)
```

For a divisor `s|ell`, put `r=ell/s`. A degree-`s` fixed-petal refinement is
the additive-shift class of a monic polynomial `P in K[X]` of degree `s` for
which one `T_i` is a disjoint union of `r` complete level fibers of `P`, each
of size `s`. If their distinct labels form `A subset K`, then

```text
L_(T_i)(X)=product_(a in A)(P(X)-a)=F_A(P(X)),
F_A(Z)=product_(a in A)(Z-a).                           (TR2)
```

Thus `F_A` is monic, split, and squarefree of degree `r`.

## Tame uniqueness theorem

If

```text
p does not divide r=ell/s,                              (TR3)
```

then a fixed source petal carries at most one additive-shift class of
degree-`s` refinements. Consequently all tame fixed-petal refinement
partitions in one source number at most

```text
M_src tau(ell) <= M_src ell <= n.                       (TR4)
```

This removes quotient-polynomial supply from the tame fixed-petal branch,
including smaller-fiber scales. It does not by itself pay complete-fiber role
assignments: one degree-`s` partition can have `n/s` fibers, so the raw bound
`3^(n/s)` is not polynomial when `s` is small. Growing polarity, arbitrary
petal locators, unanchored maps, small-scale role payment, and wild divisors
with `p|ell/s` remain open.

## Wild boundary

The characteristic guard in `(TR3)` is load-bearing for a purely polynomial
decomposition argument. Over `K=F_(p^2)`, the squarefree split polynomial

```text
L(X)=X^(p^2)-X
```

has `p+1` inequivalent monic degree-`p` right components, one for each
one-dimensional `F_p`-subspace of `K`. They all have zero constant term, so
they are not related by additive shifts. The verifier checks the exact
`F_9` instance, which has four classes.

This counterfixture is not asserted to be an admissible multiplicative-domain
source petal. It proves that removing `(TR3)` requires additional domain
geometry; coefficient triangularity alone cannot do it.
