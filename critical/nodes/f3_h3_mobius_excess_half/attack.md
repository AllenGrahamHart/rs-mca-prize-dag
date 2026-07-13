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

The proved `f3_h3_shifted_product_sidon` theorem removes a characteristic-zero
degeneracy from all three routes. For dyadic roots over `C`, every product
collision is equal or a swap. Therefore every record in `S_ns` at a finite
row is a genuine `p`-specific norm-gate event: its lifted nonzero obstruction

```text
alpha=(1-x)(1-y)-(1-u)(1-v)
```

has norm divisible by `p`. A norm-divisor attack may now aggregate only these
finite-characteristic accidents. The theorem is per collision, so summing its
individual norm bounds is not yet a per-prime estimate.

The same theorem proves nonidentity quotient uniqueness in characteristic
zero and gives the exact finite split

```text
S_ns = sum_(t!=1,R(t)>0) Q(t)
     + sum_(t!=1) Q(t)(R(t)-1)_+.
```

The first term is a single-accident ledger. The second is the genuinely joint
double-accident ledger. This is a proved decomposition, not a claim that the
two norm obstructions are independent modulo `p`.

The exact falsifier is an official row with `17X_18>300n^2`. Partial computation
must return a rigorous lower bound before it can falsify.

## Preferred moment reduction

The proved background node `f3_h3_cutoff18_nonswap_compiler` removes equal and
swapped product representations exactly and discards every product fiber below
the actual cutoff. It reduces this leaf to the sufficient estimate

```text
S_ns^rich
  =sum_(t!=1,P(t)>=19) [P(t)(P(t)-2)+D(t)]R(t)
  <=1200n^2,
```

where `D(t)=#{a in A:a^2=t}`.  Equivalently, bound quadruples
`(lambda,a,b,c)` for which

```text
a, lambda*a, b, b/lambda, c, a*b*c in A,
lambda != 1, lambda != b/a, ab != 1, P(ab)>=19.
```

This is preferable to the older `FM69` target because it deletes the
unavoidable swap family, observed to contribute `0.990925729n^2` at the
boundary row. An unspecified six-variable incidence estimate with a logarithmic
loss does not close the leaf; the needed task is a constants-explicit
bound for this four-variable constrained system. The former full `S_ns`
moment is a valid but strictly stronger envelope and is no longer the preferred
target.

The proved `f3_h3_line_star_moment_identity` gives a second exact form. For

```text
C_m={a in A:ma in A},       |C_m|=R(m),
```

one has

```text
S_ns^rich=sum_(m!=1) sum_(a!=a' in C_m, m*a*a'!=1,
                          P(m*a*a')>=19) R(m*a*a').
```

This exposes the missing input as source-line/target-line correlation: each
ordered chord on the populated line of slope `m` emits slope `m*a*a'`. A
Mitkin tail for source or target populations alone does not control this
directed moment. The proved unrestricted line-star identity supplies this by
restriction. The bounded symbolic search in that packet also rejects the
natural monomial ansatz for a canonical non-base target point.

At the boundary row `(n,p)=(8192,67657729)`, exact Modal replay
`ap-yTeGirrfOykwHEmzAcuamR` gives `S_ns=65810428` but
`S_ns^rich=720`, with only two rich targets and `R=1` on both. This large
separation selects a rich-locus theorem over further work on the full moment;
it is evidence, not a corridor-wide estimate.

## Distinct fifth-orbit route

The proved `f3_h3_fifth_orbit_moment_compiler` gives a second cutoff-aware
target. If `U(t)=(P(t)+D(t))/2` is the number of swap-orbits of product
representations, then

```text
X_18 <= (2/231) sum_(t!=1,P(t)>=19) binom(U(t),5)R(t).
```

The coefficient is sharp at `(P,D,U)=(22,0,11)`. Therefore it is enough to
prove

```text
sum_(t!=1,P(t)>=19) binom(U(t),5)R(t) <= (34650/17)n^2.
```

This moment has no equal, swap, repeated-representation, or low-fiber strata:
one record is a rich target, five distinct unordered product representations,
and one oriented quotient representation. Its `2038.235...n^2` allowance
makes it a plausible direct multivariate Stepanov target. The estimate itself
remains open.

A second complete symbolic fence rejects all `720` direct assignments of the
six subgroup variables to the classical collinear-triple equation `T(H)`.
Consequently the published `T(H) << n^4 log n` route cannot be divided by an
orbit factor and applied to `S_ns` by coordinate relabelling. A nontrivial
rational incidence map could still revive that route, but it must be proved.

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
`3.824218750n^2`; the truncated moment is smaller still. The global paired
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
