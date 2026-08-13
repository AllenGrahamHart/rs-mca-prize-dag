# Cycle 196: MCA K-to-K+1 badness-transport counterexample (2026-08-12)

The shared route-comparison dossier asked whether the upstream pole-line
record at `d1=67473`, computed with source dimension `K=k+1`, can be used
silently in the actual degree-`<k` MCA witness problem.  Upstream `#1159`
already retained `(u,v)=(1_E,X^k)` as a mutation control.  Elevating that
control to an exact semantic theorem gives a counterexample to unguarded
transport.

On the deployed KoalaBear row, take the order-`2^21` subgroup, the prefix
`E` of length `67473`, the following support `S` of size `m=1116048`, and

```text
u=1_E,  v=X^k,  slope=0.
```

For `RS[F,D,k]`, `u` has the degree-`<k` explanation zero on `S`, while no
degree-`<k` polynomial can agree with `X^k` on `m>k` points.  The slope is
therefore support-wise MCA-bad.  For `RS[F,D,k+1]`, `(0,X^k)` simultaneously
explains the same received pair on the same support.  Badness and first-owner
semantics are consequently not invariant under the dimension substitution.

This is a route cut, not a terminal obstruction.  A repaired `SEM-QBC` or
whole-line-selector adapter may retain `K=k` or explicitly carry and recheck
the original degree-`<k` explanation and pair-noncontainment guards.  That
guarded adapter remains open, as does assignment of the pole-line record to
Q or BC.

```text
start:                   2607c6fa7
result:                  PROVED counterexample to unguarded K-to-k+1 transport
DAG delta:               +1 PROVED background node, +1 evidence edge
critical status delta:   none
upstream terminal delta: exact hostile regression for #1159/#1163 lineage
delta-star movement:     none
compute:                 exact integer and polynomial-root arithmetic only
next route action:       run the #1160-line P_BC rejection regression, then
                         formulate the guarded K-adapter contract if it survives
```
