# Attack surface

The unrestricted assertion that a nondegenerate Mobius transform has only
constantly many points on `H x H` is a known hard subgroup-intersection
problem. This node is narrower in three ways: `n` is a power of two, the
official regime has `p>n^2`, and only parameters `t in A/A` are consumed.

Promising routes:

1. build a Stepanov auxiliary polynomial for the simultaneous product and
   quotient fibers, preserving `t in A/A`;
2. use the four subgroup points defining `t` to turn a rich Mobius fiber into
   a cross-ratio rigidity configuration;
3. derive a constants-explicit rich-fiber incidence tail strong enough to
   rule out level `36`.

The published `E_x(H+1) << n^2 log n` estimate has an implicit constant and
does not prove `(M35)`. Characteristic-zero lifting only handles
`p>8^(n/4)` and does not cover the official polynomial-field corridor.

An exact falsifier is one official `(n,p,t)` with `t!=1`, `R(t)>0`, and
`P(t)>=36`.
