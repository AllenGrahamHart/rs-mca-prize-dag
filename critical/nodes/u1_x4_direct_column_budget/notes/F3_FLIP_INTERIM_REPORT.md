# F3 flip interim report

Status: IN-PROGRESS REPORT, NOT A FLIP DOSSIER.

This is the current evidence map for the F3 flip brief.  It records what is
proved, what is only conditionally compiled, and what still blocks promotion of
`u1_x4_direct_column_budget` to `PROVED`.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digest:

```text
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

The replay runs only lightweight local verifiers.  It does not launch Modal.

## Current claims

### h=2

The h=2 stratum is closed by the external Cochrane-Pinner input already cited in
the node.  The in-house rich-coset reconstruction remains valuable because it
now has explicit constants:

```text
E(H) <= 22111 h^(5/2)
```

This in-house chain covers official powers of two from `2^23` upward.  Without
the external import, the remaining finite midrange is exactly `2^19..2^22`;
`2^13..2^18` are the rows estimated as feasible for exact certificates under
the `<2000` shard policy.

### h=3

The char-zero classification and norm-gate mechanism are banked.  The current
hyperbola identity is now locally replayed: same-fiber pairs of
`F(T)=T^3+aT^2+bT+c` satisfy `G_F(u,v)=XY-Delta` after the explicit
`omega`-coordinate change.  The per-row compiler consumes the corrected
activation statement:

```text
H3-ACT(C): A_3(n,p) <= C n
```

where `A_3(n,p)` counts actual non-toral common-root activations at primitive
`n`th roots, not rational norm-gcd coincidences.  If `C=16`, then

```text
T_3 < n^3 for every n >= 17.
```

The `n=96` all-core aggregate has maximum oriented per-prime activation count
`92 < 96`.  The new orbit deduplication reduces the same banked activation list
to `167` affine/Galois pair-orbits, with maximum per-prime deduped count
`27 < 96` and no repeated canonical orbit across threshold primes.  This is
evidence at the right scale but not a proof.  The remaining h=3 proof debt is
exact:

The activation symmetry packet proves the algebra behind that deduplication:
unit-affine exponent maps and side swap preserve the h=3 activation predicate
when the primitive-root embedding is transformed contragrediently.  The replay
checks this over finite-field samples and all `720` banked activation records.
This is a bridge-side symmetry lemma, not an activation bound.

The hyperbola-line degeneracy packet classifies one of the bridge exclusions
exactly.  In the same `omega`-coordinates,

```text
Delta = a^2/3 - b.
```

Thus the `3 | q-1` rational-line cell is precisely `b=a^2/3`, where
`G_F(u,v)` splits into the two translated asymptote lines.  For
`Delta != 0`, the conic `XY=Delta` is irreducible over the coefficient field.
This is a theorem-statement repair for the bridge/rank theorem, not an
activation-count proof.

The official degeneracy ledger removes one named exception from the actual F3
rows.  The char-zero theorem says the toral h=3 column exists only when
`3 | n`, with count `binom(n/3,2)`.  Since every official row is `n=2^s`,
`13 <= s <= 41`, the toral term is zero on the rows that matter for the F3
floor.  The remaining official degeneracy cells for the repaired rank theorem
are the constant-ratio cells and the hyperbola-line cell `b=a^2/3`.

The conic-chart packet makes the bridge setup field-rational.  Given any
row-field point `(u0,v0)` on the same-fiber conic
`u^2+uv+v^2+a(u+v)+b=0`, the line-through-point chart gives

```text
U(t), V(t), W(t) = -a-U(t)-V(t)
```

with numerator and denominator degrees at most `2`, and
`F0(U)=F0(V)=F0(W)` for `F0(T)=T^3+aT^2+bT`.  Thus the h=3 same-fiber
membership conditions land in the exact degree-2 rational-map class consumed by
the rich-curve compiler, without adjoining a cube root.  This does not prove
the rank-good minor theorem or the geometric batching theorem.

The local fiber-count bridge fixes the multiplicity on each same-`(e1,e2)`
ledger.  If `N(s1,s2)` is the number of unordered triples in `H` with those
elementary data, and `R(s1,s2)` is the number of ordered pairwise-distinct
same-fiber triples, then

```text
R(s1,s2) = 6 N(s1,s2),
local activated pairs = binom(N(s1,s2),2).
```

Equivalently, the conic chart counts ordered triple points, and the bridge must
pay the exact sixfold ordering multiplicity before quotienting activated
triple-pairs.  This is a local counting identity, not the global
rank-capacity batching theorem.

The dilation-lift packet justifies the normalization factor in the activation
compiler.  If `A_3(n,p)` counts activated unordered shape-pair orbits modulo
common multiplication by `H`, then the raw unnormalized shape-pair count is at
most

```text
n A_3(n,p).
```

This is an orbit-stabilizer upper bound, not a freeness assertion: finite rows
can have side-swap stabilizers, and those only make the raw orbit smaller.
This supports the existing `T_3 <= toral + poisson_boundary + n A_3(n,p)`
compiler term.

The conic-chart ratio guard closes another bridge-side degeneracy ambiguity.
After excluding the hyperbola-line cell `a^2=3b`, none of the three
field-rational chart maps

```text
U(t), V(t), W(t)
```

has a constant ratio with another.  Therefore the constant-ratio collapse
handled by the generic rich-curve degeneracy filter cannot occur inside a
repaired nondegenerate same-fiber conic chart.  This is a standalone replay,
not part of the default aggregate, because the aggregate is already close to
the 60 second cap.

The conic-chart H-point coverage packet pins the additive loss between the
affine chart count and ordered same-fiber triples.  For fixed `(e1,e2)`, if
`T_chart` counts finite parameters `t` with `U(t),V(t),W(t) in H`, then the
ordered triple count satisfies

```text
R = T_chart + epsilon,    epsilon in {0,1}.
```

The only possible missing point is the vertical/projective mate of the chosen
base point.  This lets the rich-curve chart count control the local ordered
fiber count up to one point per conic, but it still does not prove global
rank-capacity batching.

The conic base-point equivalence packet prevents overcharging this ledger.
Different ordered triples in the same nondegenerate same-`(e1,e2)` fiber give
different line-through-point parametrizations, but they have the same
projective conic image and recover the same ordered `H`-triple set after adding
the one vertical mate.  Thus incidence bookkeeping may choose one base point
per nonempty conic fiber; it should not pay one geometric curve image per
ordered triple.

The rank-normalization invariance packet has now been strengthened to remove
the remaining parametrization caveat: source Mobius reparametrizations preserve
the cleared `RC-RANK` substitution rank after homogeneous denominator
clearing.  Therefore changing the base point on a nondegenerate conic does not
change the rank target.  This still does not prove the rank-good minor theorem
itself.

The pair-count compiler now makes the remaining local arithmetic explicit.
For charts `z` with finite counts `T_z`, vertical losses `epsilon_z`, and
ordered triple counts `R_z=T_z+epsilon_z`,

```text
P_z = binom(R_z/6,2) = R_z(R_z-6)/72.
```

Thus a chart ledger with `T_z <= M`, `sum_z T_z <= S`, and at most `Z` charts
has

```text
P_total <= (M+1)(S+Z)/72.
```

A sufficient normalized h=3 target condition is therefore

```text
(M+1)(S+Z) <= 1152 n       =>       P_total <= 16 n.
```

This is standalone bridge bookkeeping, not an activation proof.  Its main
message is that a linear chart-mass estimate alone cannot close `H3-ACT(16)`;
the global bridge must also supply a max-fiber cap, a dyadic level-set theorem,
or an equivalent rank-capacity batching bound.

The L2/level-set bridge compiler weakens that sufficient condition to the
native quadratic ledger.  For ordered same-fiber triple counts `R_z`, the
normalized target is equivalent to

```text
sum_z R_z(R_z-6) <= 1152 n.
```

Equivalently, with `N_z=R_z/6` and tail counts
`L_m = #{z : N_z >= m}`,

```text
P_total = sum_{m >= 2} (m-1)L_m.
```

Thus a future bridge can close h=3 either by proving this exact L2 ledger, or
by proving the equivalent weighted level-set tail bound.  The earlier
`(M+1)(S+Z)` condition is only a convenient corollary via
`sum R_z^2 <= max(R_z) sum R_z`.

The earlier exact pair-coprimality pilot is now included in the aggregate
replay.  On the seven-prime n=96 ladder it finds three activated shapes, each
activating at exactly one threshold prime; the common obstruction norm factors
are `{1153,9601}`, `{97,13249}`, and `{18433}`, so below-threshold rational
norm factors do not create extra threshold activations.

The h=3 rich-curve setup guards are now in the aggregate replay.  The
denominator compiler verifies the cleared degree bound

```text
deg <= (A - 1) + 6h(B - 1)
```

for degree-2 rational maps.  The degeneracy audit and filter replay the known
constant-ratio obstruction: collapsed `r_i/r_j in H` cases can have `T=h`, so
the eventual `RC-RANK` theorem must explicitly exclude or pay multiplicative
dependence cells before applying the rank-form nonvanishing target.

```text
RC-RED(13)              => banked by the log-jet reduction
RC-RANK/RC-NV + constants => rich-curve Stepanov theorem
rich-curve theorem      => H3-ACT(C)
H3-ACT(C)               => T_3 < n^3
```

The reduced-condition side of the rich-curve theorem is now banked as
`RC-RED(13)`: derivative order `j < D` is over-imposed by coefficient
vanishing of a polynomial of degree `< A + 12D`, independent of `hB`.  The
remaining h=3 theorem gate is the rank form of nonvanishing: prove that the
cleared substitution image over the repaired curve family has rank larger than
the log-jet condition count.  Full injectivity of the `A B^3` coefficient box
is dimensionally impossible in some compiler rows, so the next theorem must be
rank-aware.  The rational norm-coprimality version should not be used; it is
already refuted by the random norm sample.

The finite-field rank sample supports this target without proving it.  At
`p=769, h=32, A=5, B=4, D=1`, the constant-ratio collapsed control has rank
`50 < 78` and fails `RC-RANK`, while a deterministic repaired random degree-2
curve has full coefficient rank `320 > 78`.  Since that rank is the whole
coefficient dimension, any direct-sum family containing this repaired curve
passes the same toy rank inequality for `Z <= 4`; `Z=5` is impossible with the
same parameters because `5*78 > 320`.

The rank stress packet extends this exact toy row.  It verifies that
private-divisor, shifted-polynomial, and shared-denominator non-collapsed
curves pass the weaker `RC-RANK` inequality even with rank below full
coefficient rank:

```text
private-divisor rational: rank 293 > 78
shifted polynomial:       rank 247 > 78
shared denominator:       rank 247 > 78
```

It also records a family-level warning by the diagonal duplicate-image rank:
repeating the private-divisor curve twice still passes (`293 > 156`), but
repeating it four times fails (`293 < 312`).  Thus the geometric batching
theorem must count repaired inequivalent curve images, not raw multiplicity.

The rank-effective bridge packet converts this warning into a precise
interface.  In the same toy row, a curve image of rank `r` has capacity

```text
floor((r-1)/78)
```

raw copies under `RC-RANK`.  The pinned capacities are:

```text
collapsed: 0
private-divisor / shifted / shared-denominator: 3
full-rank random: 4
```

Therefore the bridge theorem needed downstream is not raw `|Z| <= Z_budget`,
but rank-effective capacity consumption `<= Z_budget`.

The small-`H` rank guardrail prevents overstatement of the future theorem.  In
the same private-divisor toy family and Stepanov box, varying only the subgroup
order gives exact ranks

```text
H=4:  rank 41   degree_dim 41   fails RC-RANK
H=8:  rank 77   degree_dim 77   fails RC-RANK by one
H=16: rank 149  degree_dim 149  passes
H=32: rank 293  degree_dim 293  passes
H=64: rank 320  degree_dim 581  full coefficient rank
```

The same verifier checks the model formula
`rank = min(A B^3, A + 3H(B - 1))` for this private-linear control, so the
small-rank failures are explained by degree-space dimension rather than by a
new degeneracy.

So non-collapse plus private divisors do not imply a uniform tiny-`H`
`RC-RANK` theorem.  The future large-row theorem must print an `H` floor, or
route the tiny rows to finite certificates.  This is a theorem-statement
guardrail, not an official-row obstruction.

The model-lemma packet separates the algebraic part of that guardrail from the
unproved rank lower bound.  Constant-ratio collapsed curves have exact rank

```text
| { a + Hs : 0 <= a < A, 0 <= s <= 3(B-1) } |,
```

so the toy `A=5,B=4,H=32` collapsed rank is exactly `50`, giving zero
`RC-RANK` capacity against the `78` conditions.  For private-linear curves,
degree alone gives the one-curve ceiling

```text
rank <= min(A B^3, A + 3H(B - 1)).
```

Thus even a perfect private-linear degree-space theorem needs an explicit
`H` floor; in the toy box the first possible one-curve pass is `H=9`.  The
remaining theorem is the lower bound, namely degree-space fullness under
explicit repaired/private-divisor hypotheses.

The private-linear one-factor rank lemma proves the local version of that
lower-bound target.  For one generator `(X-alpha)/(X-beta)`, the span of
`X^a (X-alpha)^(Hb)(X-beta)^(H(B-1-b))` has exact dimension
`min(A B, A+H(B-1))` by the `alpha`-adic valuation filtration.  Thus any
remaining private-linear rank loss must be a genuinely three-generator
interaction, not a defect of a single private-linear level.

The two-factor guardrail rules out a naive induction from that lemma.  Already
at `A=1,B=3,H=2` with distinct private pairs `(2,3)` and `(5,7)`, the
two-factor span has exact rational rank `8`, while
`min(A B^2,A+2H(B-1))=9`.  The full private-linear theorem therefore needs a
global multigenerator argument, not a factor-by-factor valuation iteration.

The bad-prime guardrail prevents a second overstatement.  In a three-factor
private-linear model with `A=1,B=5,H=9`, the integer coefficient matrix has
full degree-space rank `109` over Q, witnessed by rank `109` modulo `1013`, but
the same matrix drops to rank `108` modulo `1009`.  Thus even
characteristic-zero degree-space fullness must be paired with a finite-row
minor nonvanishing argument at the actual row prime.

The generic-open packet converts that lower-bound target into an algebraic
avoidance problem.  For fixed Stepanov parameters, `rank >= r` is equivalent to
nonvanishing of some `r x r` minor of the universal cleared-substitution
matrix.  The private-linear witness

```text
(X-2)/(X-3), (X-5)/(X-7), (X-11)/(X-13)
```

has exact rank `293 = A + 3H(B-1)` over `F_769`, so the private-linear
degree-space-fullness open set is nonempty in the toy box.  The remaining
`RC-RANK` theorem can now be stated as a rank-good minor avoidance theorem for
the actual repaired F3 signature-curve parameter image, with rank-effective
capacity accounting for repeated images.  The same generic-open verifier also
uses the deterministic repaired degree-2 random curve from the rank sample,
whose exact rank is `320 = A B^3`, proving that the full coefficient-rank
degree-2 open set is nonempty in the toy box.

The normalization-invariance packet proves two harmless rank symmetries for
that future theorem.  Source Mobius changes
`X -> (alpha X + beta)/(gamma X + delta)` preserve the cleared coefficient
rank after homogeneous denominator clearing; affine source changes are the
special case `gamma=0`.  Nonzero target coordinate scalings only rescale
columns, while target permutations and target inversions only permute the
multi-index columns.  Thus `RC-RANK` is unchanged by these normalizations.  This
lets the eventual `F3-RANK-AVOID` theorem quotient repaired representatives by
source Mobius changes and the listed target operations.

The private-linear compiler guard prevents a wrong shortcut from this point.
All current official non-diagonal h=3 bridge witnesses use the degree-2
denominator room `A + 6n(B-1)`: for every row `s=13..41`, the per-curve
condition count is larger than the private-linear degree room
`A + 3n(B-1)`.  Therefore a theorem proving only private-linear degree-space
fullness cannot be plugged into the current compiler unchanged.  The route
splits:

```text
degree-2 rank theorem        => keep the current non-diagonal compiler;
private-linear rank theorem  => rerun a private-linear compiler with L_private.
```

The guard also verifies representative private-linear retuned boxes at
`s in {13,16,20,23,32,41}`, so the private-linear track is not ruled out; it
just needs its own maximality compiler.

The private-linear compiler now supplies the full retuned official-row table.
Using `L_private=(A-1)+3n(B-1)`, it proves maximal private-linear
rank-capacity budgets for `s=13..41`:

```text
s=13: Z_private=23
s=14: Z_private=29
s=15: Z_private=37
s=16: Z_private=47
s=17: Z_private=59
s=18: Z_private=75
s=19: Z_private=94
s=20: Z_private=119
s=21: Z_private=150
s=22: Z_private=189
s=23: Z_private=238
s=24: Z_private=300
s=25: Z_private=378
s=26: Z_private=477
s=27: Z_private=601
s=28: Z_private=757
s=29: Z_private=954
s=30: Z_private=1202
s=31: Z_private=1514
s=32: Z_private=1908
s=33: Z_private=2404
s=34: Z_private=3029
s=35: Z_private=3816
s=36: Z_private=4809
s=37: Z_private=6058
s=38: Z_private=7633
s=39: Z_private=9617
s=40: Z_private=12117
s=41: Z_private=15267
```

For each row, the replay checks a pinned passing witness and scans the exact
finite `B` cap for `Z+1` to prove the next budget fails.  This is still
conditional on a future private-linear rank theorem and the matching
private-linear bridge/rank-capacity theorem.

The rank-avoidance interface packet now pins the exact theorem pair needed to
close h=3 through the current compiler:

```text
F3-RANK-AVOID + H3-BRIDGE-RANKCAP(Z_budget(s)) => H3-ACT(16)
```

It now also records the private-linear alternate route:

```text
F3-PRIVATE-LINEAR-RANK-AVOID
  + H3-BRIDGE-PRIVATE-RANKCAP(Z_private(s)) => H3-ACT(16)
```

Both arithmetic tables cover every official exponent `s=13..41`, with
`Z_budget(13)=16`, `Z_budget(41)=10795`, `Z_private(13)=23`, and
`Z_private(41)=15267`.  This is still conditional: neither rank-good minor
avoidance theorem nor the geometric bridge/rank-capacity assignment is proved.

The rank-form parameter compiler gives the current conditional constants for
representative repaired curve-family sizes.  Under `RC-RANK`, the diagonal
`A=D` boxes give, for example:

```text
n=2^23, |Z|=64:   sum_z T(z) <= 65,729,374  (about 7.84 n)
n=2^32, |Z|=128:  sum_z T(z) <= 6,380,025,160 (about 1.49 n)
n=2^41, |Z|=256:  sum_z T(z) <= 619,017,527,995 (about 0.282 n)
n=2^41, |Z|=512:  sum_z T(z) <= 1,422,138,529,491 (about 0.647 n)
```

This is arithmetic slack for high rows, not `H3-ACT(C)`: the missing pieces are
still the rank theorem and the F3 geometric batching/charging from activated
shape pairs to repaired curve families.

The bridge-budget compiler turns that geometry gap into an explicit contract.
If, on row `n=2^s`, activated shape pairs batch into a repaired curve family of
size at most `Z_budget(s)`, then `RC-RANK` plus the current diagonal arithmetic
implies `H3-ACT(16)`.  Replayed budgets include:

```text
s=13: Z_budget=11
s=20: Z_budget=58
s=23: Z_budget=116
s=32: Z_budget=927
s=39: Z_budget=4674
s=40: Z_budget=5889
s=41: Z_budget=7420
```

For each printed row the replay now verifies a pinned passing diagonal-box
witness at `Z_budget`, and exhaustively scans the same `B_max=50000` diagonal
search at `Z_budget+1` to verify failure.  Monotonicity in `|Z|` therefore
makes the table maximal inside the stated diagonal search box.  This still does
not prove the geometric batching contract, `RC-RANK`, or impossibility under
other Stepanov parameter families.

The first non-diagonal parameter pass improves the low/middle official rows
`s=13..35`.  It uses the same compiler inequalities, but chooses the least
admissible `A` for each `(B,D)` instead of imposing `A=D`.  The aggregate replay
now verifies that the improved `Z` passes and `Z+1` fails up to the exact
analytic `B` cap for any possible passing box:

```text
s=13:  11 -> 16
s=14:  14 -> 21
s=15:  18 -> 26
s=16:  23 -> 33
s=17:  29 -> 42
s=18:  36 -> 53
s=19:  46 -> 67
s=20:  58 -> 84
s=21:  73 -> 106
s=22:  92 -> 134
s=23: 116 -> 168
s=24: 146 -> 212
s=25: 184 -> 267
s=26: 232 -> 337
s=27: 292 -> 425
s=28: 368 -> 535
s=29: 463 -> 674
s=30: 584 -> 850
s=31: 736 -> 1071
s=32: 927 -> 1349
s=33: 1168 -> 1700
s=34: 1472 -> 2142
s=35: 1855 -> 2699
```

This reduces the low/middle-row batching burden but still remains conditional
on the same two open h=3 gates: `RC-RANK` and the actual geometric batching
theorem.

The aggregate replay now extends the same non-diagonal search to `s=36..41`:

```text
s=36: 2337 -> 3400
s=37: 2944 -> 4284
s=38: 3710 -> 5397
s=39: 4674 -> 6800
s=40: 5889 -> 8568
s=41: 7420 -> 10795
```

The high-row replay again checks a pinned passing witness at the improved `Z`
and an exhaustive `Z+1` failure up to the exact analytic `B` cap for any
possible passing box.  The largest cap is `B <= 61923` at `s=41`, so this is
still lightweight enough for the default local replay.

A tempting shortcut for the rank theorem is already refuted.  Private
zeros/poles for `X,r_1,r_2,r_3` do not imply full coefficient-rank
injectivity: the toy curve
`(X-2)/(X-3), (X-5)/(X-7), (X-11)/(X-13)` has private zeros but exact rank
`293 < 320`.  It still satisfies the weaker toy `RC-RANK` inequality
`78 < 293`, so the refutation only kills the overstrong proof route.

### h=4

The structural dichotomy is already proved in the DAG:

```text
h4_terminal_dichotomy: PROVED
x83_uniform_square_shift_obstruction_gate: PROVED
```

So h=4 has no hidden third mechanism.  The live work is certificate/norm-gate
exclusion, not a new classification theorem.

### h=5

The h=5 structural classification is reduced.  Since `5` is not a power of two,
`x24_char0_dyadic_descent` excludes char-zero dyadic trades, and
`x83_uniform_square_shift_obstruction_gate` says every finite-row h=5 survivor
must be a p-specific norm-gate event.  Thus h=5 no longer has an unlocalized
classification gap; it has a norm-gate exclusion/certificate gap.

The h=5 row evidence is strong but not a theorem.  Complete zero certificates
exist for:

```text
n=32: 402 primes (all admissible primes through p=65537)
n=64: 179 primes (contiguous admissible prefix through p=60161, plus high selected rows)
n=96: boundary prime 9601
n=128: boundary prime 17921 plus 6 nearby primes
```

The coverage audit is now in the aggregate replay.  It verifies `589` complete
zero rows and `3,164,030,779` total right-side probes.  It also prints the
remaining coverage limitation: up to the largest certified primes, the current
bank misses `0` admissible primes for `n=32` and `515` admissible primes for
`n=64`, while the current `n=96` and `n=128` banks are still only
boundary/nearby windows.

The missing h=5 theorem is exactly a symbolic norm-gate incompatibility or a
maintainable per-row certificate family for all official `p = 1 mod n`,
`p >= n^2` rows.

The certificate scaling frontier explains why the current finite-certificate
format is not that maintainable family.  The banked n=128 Modal rows use
`32` shards, but each shard rebuilds the full `binom(127,4)=10,334,625`
left table.  At n=256 the same format has a `binom(255,4)=172,061,505`
record left table, at least `5.13 GiB` before metadata; at n=512 the left
table is at least `83.68 GiB` and the right side needs about `35,836` shards
at the n=128 right-probe rate.  Thus h=5 needs a symbolic norm-gate theorem or
a redesigned certificate join, not blind extension of the current shard format.

### h=6 and h=7

The local replay verifies the banked h=6 and h=7 certificates.  The h=6
extra-prime row at `p=4993` has six anchored nontoral witnesses under the coarse
classifier, but the square-lift analysis classifies them as paid h=3 lifts.
They do not threaten the direct-column budget.

### h=8

The h=8 n=32 row is complete at six primes.  The h=8 n=64 rows remain partial:

```text
boundary_n64_h8_p193
q3_n64_h8
```

The x83 radius-three shells at `p=4289` and `p=262337` are complete and have
`full_zero = 0`.  The support-to-trade reduction is proved on banked rows: a
support-level x83 certificate is enough to recover the trade split.

The x83 obstruction interface and the one-exchange shell are now also in the
aggregate replay.  The interface verifies that all paid antipodal lifts are
x83-zero at `p in {193,4289,262337}` and that deterministic non-antipodal
samples at `p=4289,262337` have no full zero.  The one-exchange shell checks
`5,376` supports around each paid branch at both boundary-style primes, again
with `full_zero = 0`.  The same standalone verifier also pins the complete
two-exchange shells at both primes:

```text
p=4289:   947,520 supports, first_obstruction_zero=1504, full_zero=0
p=262337: 947,520 supports, first_obstruction_zero=1344, full_zero=0
```

Those radius-two replays run under the per-task 60-second cap one prime at a
time, but they are not included in the default aggregate because the aggregate
must remain laptop-safe.

The antipodal x83 quotient packet proves the algebra behind the paid branch:
if a 16-support in `mu_64` is antipodal, its locator has the form
`L_R(X)=M_A(X^2)` for an 8-support in `mu_32`, and the h=8 forced-root
obstruction is exactly the h=4 quotient obstruction with zeros inserted in odd
degrees.  Therefore antipodal x83 full-zero supports are paid by the h=4
quotient ledger.  The primitive h=8 residual is genuinely non-antipodal.

The locator parity packet makes this branch split intrinsic to the support
polynomial.  A 16-support in `mu_64` is antipodal if and only if all odd
coefficients of its monic locator vanish.  Therefore any primitive
non-antipodal support has a nonzero odd locator coefficient, and an even
locator is routed directly to the h=4 quotient ledger.

The remaining support universe is now exactly compiled.  Anchored 16-supports
with exponent `0` have size

```text
binom(63,15) = 122,131,734,269,895.
```

After removing antipodal supports

```text
binom(31,7) = 2,629,575,
```

the anchored non-antipodal residual contains

```text
122,131,731,640,320
```

supports.  The seven-support paid-branch radius `<= 3` shell workload is only
`68,753,223`, about `0.562943` parts per million of that non-antipodal universe.
Thus the radius-three certificates are strong local evidence around the paid
branch, but not a substitute for a global support-level x83 certifier.

The safe rotation symmetry `R -> cR` is also exactly compiled.  It preserves the
x83 support condition, but only reduces the global non-antipodal support target
to

```text
7,633,233,227,520
```

rotation orbits.  The non-antipodal aperiodicity packet proves this is not
hiding a separate periodic branch: any 16-support fixed by a nontrivial
rotation is necessarily antipodal, because its stabilizer contains the
half-turn.  Therefore every non-antipodal orbit has size `64`, and the
anchored non-antipodal count is exactly `16` times the rotation-orbit count.
Rotation canonicalization alone is still not a feasible global certifier.

The x83 split-rotation equivariance packet proves the support-to-trade
reduction is compatible with that quotient: if an x83 full-zero support is
rotated, the forced square root and the recovered `S_R +/- alpha` split rotate
with it, up to swapping the two sides.  A future orbit certifier can therefore
canonicalize supports under rotation without losing the recovered h=8 trade
split.

The tempting larger exponent-unit quotient is refuted.  At `p=193`, a banked
x83 full-zero support maps under `e -> 3e mod 64` to a support with obstruction
vector `[0, 180, 0, 60, 0, 20, 0]` and nonsquare `lambda = 30`.  The same banked
support maps under reflection `e -> -e mod 64` to obstruction vector
`[0, 64, 0, 82, 0, 87, 0]` and nonsquare `lambda = 125`.  Thus arbitrary unit
maps, including dihedral reflection, are not symmetries of the x83 condition
and cannot be used for certifier canonicalization without rechecking the
classifier.

The honest h=8 residual is:

```text
certify every non-antipodal h=8 n=64 x83 support, or build an external/sharded
signature join that avoids the blind binom(63,7) left table.
```

## Promotion blocker

`u1_x4_direct_column_budget` cannot be promoted from `TARGET` to `PROVED` yet.
The concrete blockers are:

1. h=3: prove `H3-ACT(C)` through the remaining rank-form `RC-NV` gate plus
   constants, or replace it with a complete official-row certificate family.
   The reduced-condition gate is banked as `RC-RED(13)`.
2. h=5: exclude or certify the p-specific x83 norm-gate branch uniformly.
3. h=8: close the n=64 non-antipodal x83 support branch.

Everything else currently looks like arithmetic/certificate engineering rather
than an unlocalized mathematical unknown.
