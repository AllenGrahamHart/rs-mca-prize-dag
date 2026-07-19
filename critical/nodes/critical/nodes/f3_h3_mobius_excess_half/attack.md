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

The proved `f3_h3_rich_fiber_norm_cutoff` packet closes the entire branch
`p>6^(n/4)`: ten unordered representations at `P(t)>=19` force a nonzero
collision obstruction of norm at most `6^(n/4)`. Every remaining attack may
therefore assume

```text
n^2<=p<=6^(n/4).
```

At fixed `n`, the proved low-distance ideal-star router strengthens this
interval to a finite candidate union. A rich row prime must divide a
normalized two-generator ideal norm

```text
N(((beta_F-beta_E)/pi^2,(beta_G-beta_E)/pi^2)),
```

where both collisions have one common center and squared Parseval distance at
most six; all three coefficient vectors have squared norm at most three. The
ideal norm divides the gcd of the two normalized principal norms. A complete
rooted-star certificate followed by exact checks at the surviving primes
would prove the whole fixed order. The contributor request is specified in
`notes/PRIZE_COMPUTE_REQUESTS.md`; incomplete factor sweeps are evidence only.
The old raw single-norm enumeration is no longer selected: its restricted
`n=8192` family already has at least `530,590,075` orbits, while the new
theorem supplies the stronger collision selector it lacked. The next gate is
an algebraic official-scale candidate generator coupled to the proved exact
common-prime-ideal alignment criterion. Complete `n=32,64` pilots show why:
rational gcd screening removes no relevant primes, whereas prime-ideal
alignment compresses the lists by factors `5.72` and `13.13` without
enumerating rooted stars. The proved 2-primary exclusion removes every
distance-two obstruction first, leaving only distance four and six in the
algebraic candidate generator and forcing at least six low edges among the
seven selected vectors.

Use the proved weighted-multistar strengthening in the final sieve. The exact
centroid ledger is `2N_4+N_6>=11` inside each selected rich fiber, so one
center has incident weight at least four. Screen for that condition rather
than merely two low-distance leaves; it corresponds to a normalized ideal
with two to four generators and can only shrink the prime union. It does not
remove the need for a complete algebraic principal-prime generator.
The complete toy screens improve `103 -> 18 -> 4` at `n=32` and
`2,127 -> 162 -> 67` at `n=64`, where the middle term is the old two-leaf
screen and the final term is weighted degree four.

Stratify that sieve by the actual excess. The proved degree ladder requires
center weight `L(7+ceil((P-18)/2))`, not merely four. Separate the two weak
boundary profiles `(P,D)=(19,1),(20,2)` from the tail: excess at least three
forces weight six, and excess at least seven forces weight eight. Any ideal or
factor ledger should preserve this increasing number of common generators.

Use the proved excess-budget tradeoff before launching a fixed-order
certificate. The default interface is `E=14`: pay every target with `P<=32`
by total quotient mass, then prove

```text
17 sum_(t!=1,P(t)>=33) (P(t)-18)R(t)
  <=300n^2-238(n-1)(n-2).
```

Every retained target has center weight at least twelve. The alternative
Pareto cutoffs `E=2,6,10` remain available if a degree-6, 8, or 10 algebraic
generator is substantially simpler, but do not combine their budgets.

The selected analytic interface is the exact low-distance edge–quotient
moment

```text
M_33=sum_(P(t)>=33)(2N_4(t)+N_6(t))R(t),
272M_33<=83(300n^2-238(n-1)(n-2)).
```

Use the canonical incidence router. In both lanes
`v=(x+y-xy-u)/(1-u)` and `w=1-(1-x)(1-y)(1-z)` are the two subgroup
membership tests. Distance four eliminates one free root through its proved
cross-overlap/antipodal equations; distance six does not. A proof should
retain the `P>=33` filter and the factor two on distance-four edges.

The fiberwise distance-four degree cap supersedes that mixed target for the
selected route. Prove only

```text
M_6,33=sum_(P(t)>=33)N_6(t)R(t),
136M_6,33<=21(300n^2-238(n-1)(n-2)).
```

Conservatively the allowance is `(651/68)n^2<9.574n^2`. Use the `I_6`
branch of the incidence router: four free subgroup roots `(x,y,u,z)`, with
`v=(x+y-xy-u)/(1-u)` and `w=1-(1-x)(1-y)(1-z)` also in the subgroup.
No distance-four estimate is required unless this selected route is abandoned.

Prefer the refined antipodal split. The antipodal-free lane has the larger
allowance coming from `P-18<=(16/53)N_6`. In the relatively weighted antipodal
lane, use the canonical root `x` and the three membership tests

```text
v=(x^2-u)/(1-u),
b=(x^2-a)/(1-a),
w=x^2+(1-x^2)z.
```

The exact target is
`136(42M_6,33^0+53M_6,33^A)<=1113(300n^2-238(n-1)(n-2))`.
Do not discard the third test and then charge the antipodal records uniformly.

For a direct incidence proof, compare the two proved lower-cutoff targets:

```text
4(10M_6,25^0+17M_6,25^A)<=5B_(n,6),
17(8M_6,29^0+11M_6,29^A)<=22B_(n,10).
```

Their conservative weighted allowances are `24.75n^2` and
`(715/34)n^2`, versus `(1643/136)n^2` at `E=14`. Do not move the fixed-order
candidate generator away from `E=14` merely because the analytic allowance is
larger: its degree-twelve sieve is the reason that computation is posed.

For direct incidence work, use the proved support-overlap payment on the
`E=6` interface. The remaining target is only

```text
D_6,25^0+(17/10)D_6,25^A <=(223/20)n^2,
```

with six disjoint signed atoms on every retained edge. The two overlapping
generic families and both antipodal-edge families have already been charged
to exact quotient mass. Do not restore those exceptional strata to a
four-variable Stepanov system.

Treat distances four and six as separate algebraic lanes. Complete toy-order
norm censuses find only `4` and `67` relevant distance-four factors, versus
`103` and `2,127` at distance six. The former is a four-term cyclotomic
classification problem; the latter is the generic six-term bottleneck.

For distance four, use the proved router before any norm enumeration. The
generic edge has `uv=-y` and

```text
x=(u^2-y)/(u(1-y)).
```

Attack the condition that this value lies in `H`, together with the separate
antipodal condition `x^2=u+v-uv`. Both are two-variable subgroup incidences.
Do not restore a four-exponent search.

The complete distance-four edge ledger is already paid at
`(3n^2+n)/2`. Use this globally: a rich target with no distance-six edge
consumes at least six distance-four edges, so there are at most
`floor((3n^2+n)/12)` such targets. The remaining missing step is to couple
this target count to `R(t)` or route the target through distance six.

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

The proved `f3_h3_rich_fiber_ideal_batching` theorem gives the first genuine
same-fiber aggregation. If several distinct unordered representations lift to
`beta_i` and have one common product modulo the selected prime `P`, their
difference ideal satisfies

```text
J=(beta_i-beta_0)_i subset (1-zeta)^2 P,
4p | N(J) | gcd_i |Norm(beta_i-beta_0)|.
```

At the complete rich locus of the boundary row
`(n,p)=(8192,67657729)`, each of the two ten-pair fibers saturates the lower
bound: the first two differences already generate `(1-zeta)^2 P`. This turns
the next arithmetic question into an ideal-index or ideal-multiplicity bound,
not independent accounting of nine principal norms.

The same certificate fences a tempting shortcut. After the exact rational
polynomial gcd is removed from the first two obstruction polynomials, their
ordinary resultant has a non-`p` cofactor of 2880 or 3455 bits. Thus raw
ordinary resultants do not isolate the row prime on the measured hardest row;
any resultant method must retain the cyclotomic ideal or exploit additional
same-fiber structure.

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

A targeted norm-concentration adversary is recorded in
`fermat_factor_adversary_result.md`. It uses prime factors of `F_12` for which
the order-8192 subgroup is generated by the integer `2`. Both rows have empty
rich loci. Thus a successful norm-divisor attack must exploit more than the
height of one chosen subgroup generator.

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
