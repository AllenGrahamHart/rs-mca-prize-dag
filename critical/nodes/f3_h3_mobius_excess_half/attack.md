# Attack surface

The target is a truncated correlation estimate. One may decompose

```text
X_18=sum_(j>=0) sum_(18+2^j <= P < 18+2^(j+1)) (P-18)R
```

and seek a constants-explicit bound for the simultaneous rich-product and
rich-quotient locus. A marginal bound for `P` alone or `R` alone is unlikely
to suffice; the observed largest product fibers have quotient multiplicity
one.

Candidate mechanisms:

1. pair a Stepanov/Mitkin tail for the line fibers `R` with a product-fiber
   sublevel estimate;
2. retain the oriented phases in the exact multiplicative-character sum;
3. classify only parameters for which both `P` and `R` are rich.

The exact falsifier is an official row with `17X_18>300n^2`. Partial computation
must return a rigorous lower bound before it can falsify.

## Preferred moment reduction

The proved background node `f3_h3_nonswap_moment_68` removes equal and swapped
product representations exactly.  It reduces this leaf to the sufficient
estimate

```text
sum_(t!=1) [P(t)(P(t)-2)+D(t)]R(t) <= 1200n^2,
```

where `D(t)=#{a in A:a^2=t}`.  Equivalently, bound quadruples
`(lambda,a,b,c)` for which

```text
a, lambda*a, b, b/lambda, c, a*b*c in A,
lambda != 1, lambda != b/a, ab != 1.
```

This is preferable to the older `FM69` target because it deletes the
unavoidable swap family, observed to contribute `0.990925729n^2` at the
boundary row. An unspecified six-variable incidence estimate with a logarithmic
loss does not close the leaf; the needed task is a constants-explicit
bound for this four-variable constrained system.

## Cheap paired sufficient condition

The pointwise implication

```text
P(t)>=19 and R(t)>0  =>  R(t)<=17
```

would already close the leaf, because

```text
X_18 <= 17 sum_t P(t) < 17n^2,
17X_18 < 289n^2 < 300n^2.
```

This is an attack criterion, not a new premise. It asks only for exclusion of
the simultaneous rich rectangle `P>=19, R>=18`, but it remains a pointwise
constant-intersection statement and is not supplied by the audited literature.

## Paired PGL2 route

The proved `f3_h3_pgl2_pair_identity` retains the quotient-support condition
pointwise. It writes

```text
P(t)=#{x in H : 1+t/(x-1) in H},
R(t)+1=#{z in H : 1+t(z-1) in H}.
```

Thus the simultaneous estimate

```text
I_inv(t)+2 I_aff(t) <= 39
```

for every official row and nonidentity parameter would imply `P(t)<=35`
whenever `R(t)>0`, hence close the stronger M35 route and this critical leaf.
It is stronger than necessary but packages the support restriction into two
PGL2 intersections sharing the same parameter. Boundary measurements give
`max(I_inv+2I_aff)<=30` on the first twelve `n=8192` rows and first four
`n=16384` rows. These measurements are route evidence only.

A wider bounded sweep (`ap-bHp1Epb9jC5BdW4xeXfB7l`) exhaustively checked
7,090 admissible rows at powers of two `64<=n<=4096`. The largest paired score
was `I_inv+2I_aff=34`, no row had `X_35>0`, and the largest non-swap moment was
`3.824218750n^2`, against the sufficient `1200n^2` target. The global paired
extremizer has nine unordered product pairs and seven quotient pairs rather
than the earlier one-pair telescoping pattern. This keeps the pointwise route
alive but selects the aggregate moment as the primary analytic target. Exact
ranges and witnesses are in
`background/nodes/f3_h3_pgl2_pair_identity/smallrow_sweep_result.md`.

The primary-source scope audit is recorded in
`background/nodes/f3_h3_pgl2_pair_identity/literature_audit.md`. Existing
shifted-energy, additive-intersection, product-set containment, and ratio-set
non-equality theorems do not imply the pointwise constant 39. In particular,
a rich fiber is a matching graph, not the Cartesian product required by the
sharp shifted-product theorem.

The shifted-energy alternative is audited in
`background/nodes/f3_h3_nonswap_moment_68/energy_constant_audit.md`. Its known
`O(n^2 log n)` shape could close C36' only after a new constants-explicit
argument; the published implicit constants do not yield the required finite
constant.
