# Proof

Fix source signs, target signs, and `xi in {0,2}`. On the proved cell-12
four-basis tower, the first two pairs of canonical matching `3` give
quadratics `P_u(u)` and `P_v(v)`, where `u=df` and `v=ef`. Put `de=m` and
`eta=1` for `xi=0`, and `de=-m` and `eta=-1` for `xi=2`. The deleted
record's squared-sum equation is

```text
H(u,v)=de*(u+eta*v)^2-S*u*v=0.                    (RS12-DE3)
```

The pinned compiler takes the quadratic resultant of `H` and `P_u` in `u`,
then a division-free pseudo-remainder modulo `P_v`. The resulting linear
common-root cut is normed through `1,t,b,bt`; leading-coefficient drops are
retained rather than divided away.

The cell-12 adapter runs all 32 source-sign/target-lane/`xi` rows. It unions
every field root of the norm numerator, norm denominator, and all inversion
guards, then lifts through the exact tower and compact kernel. The ledger has
544 case-labeled roots and 752 guarded source points. Its 96 compatible
`(u,v)` lifts satisfy (RS12-DE3). Solving `f^2=uv/de` gives 144 final rows:
48 have `f=0` and hit the explicit target boundary, while the other 96 have
a nonzero third colored-pair cut. Thus no colored solution, witness, or
unresolved branch survives. A separate SymPy/Galois-tools root certificate
and local direct replay check each step independently.

The exact generic label quotient sends direct `(0,3)` through the two record
involutions to `(0,6),(1,3),(1,6)`, and sends `(2,3)` to `(2,6)`. These are
six labels in two disjoint generic orbits. QED.
