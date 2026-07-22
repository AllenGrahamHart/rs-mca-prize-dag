# Claim contract - L1 tame fixed-petal refinement census

## Inputs

- a finite field `K` of characteristic `p`;
- one fixed source with `M_src` disjoint `ell`-point petals;
- a divisor `s|ell`, with `r=ell/s`;
- a monic degree-`s` polynomial whose complete fibers partition one whole
  source petal;
- the tame guard `p` does not divide `r`.

## Output

For each `(petal,s)`, there is at most one refinement partition up to additive
shift. Across the source there are at most `M_src tau(ell)<=n` tame classes.

## Falsifier

Two monic degree-`s` right components of the same source-petal locator, not
related by an additive constant, with `p` not dividing `ell/s`; or failure of
the stated owner count.

## Nonclaims

No polynomial count of small-scale fiber-role assignments, no wild-divisor
uniqueness, no admissible-domain exclusion of the additive counterfixture,
and no payment for unanchored or arbitrary-locator cells is claimed.
