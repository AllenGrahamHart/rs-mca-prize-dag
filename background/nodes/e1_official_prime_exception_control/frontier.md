# Frontier: exact route-uniform E1 collision control

Status: TARGET.

The collision mechanism and almost-all-primes density statement are proved.
The finite target is now explicit: on every admissible clean-anchor row with
quotient-generated field `B=F_p(Q)` satisfying
`|B|>=b_pair_min=ceil((K+B*+1)/3)`, at quotient order `N=256` or `512`, prove

```text
P <= A_2(N,ell)-B*-1
```

for the unordered reduced-value collision-pair count `P`. The six RowC/prize
allowances are printed and independently replayed in
`e1_clean_anchor_exact_collision_allowance`.

The generated-field axis is closed on this branch. Every proper subfield of
an official field has size below `2^128`, while every printed `b_pair_min`
exceeds `2^133`; pair feasibility therefore forces `F_p(Q)=F`. The remaining
extension-degree axis is closed as well. Exact perfect-power interval checks
force `F=F_p` and `p=1 mod N`. The remaining issue is pointwise collision
control over those primes in the ambient field itself.

The first collision bands are also closed analytically. Folding antipodes and
using Parseval over the odd conjugates proves that `N=256` collisions have
swap distance at least five, while `N=512` collisions have distance at least
two. The crude `(2s)^phi(N)` bound should no longer be used for those bands.
The first surviving `N=256` band reduces to folded coefficient profiles
`(4,2,0),(3,4,0)` at `s=5`. In the square-mass-16 profile `(3,4,0)`, an
exact logarithmic deficit removes `V=0` and every `V>=136`; a
sparse-autocorrelation refinement removes `112<=V<=134`, leaving
positive even `V<=110`. A subfield norm argument also removes every vector
in either profile whose support differences have a nontrivial gcd with
`256`. Thus all live first-band vectors have full conductor. This does not
classify the low-variance residual: a certified full-conductor vector already
occurs at `V=36`. Total ramification of two gives an independent
cofactor gate: the four-singleton reduction in `(3,4,0)` has root
multiplicity at most five at one, while the two singleton exponents in
`(4,2,0)` are not congruent modulo 32. The low-variance profile is
also non-Sidon in a signed sense: its repeated-chord cross sum is at most
`-7`, forcing a three-term progression or four-point parallelogram.
Local reciprocity sharpens its norm interface further: every collision norm is
exactly `2^mu p` for one of `mu=1,...,5`. In `(4,2,0)`,
the formerly broad cofactor window contracts to 419 explicit values.
At `N=512,s=2`, exact negacyclic variance
excludes `(0,4,0)`, while a complete 129540-state interval-resultant
certificate excludes `(1,2,0)`. The entire band is closed, so the `N=512`
ledger begins at `s=3`. The profile entries count opposite pairs,
singletons, and same-sign pairs.

The old `o(1)` language was not a finite `2^-128` certificate. Likewise, the
old named `N'=128,256` no-vector experiments are background evidence: `128`
does not match a live clean quotient order, `512` is absent, and finite
exhibits do not prove the row-family quantifier.

The complementary field range has two proved route cuts. If `|B|<=B*`, direct
E1 is impossible because the complete value set lies in `B`. If
`B*<|B|<b_pair_min`, direct E1 may work, but this pair-loss compiler cannot:
its balanced-fiber minimum already exceeds the allowance. Both remain
obligations of the universal unsafe router, not of this target.

The next route-deciding attack is algebraic. Either:

- prove the exact pointwise pair-incidence bound from the norm-divisor
  structure over every prime `p=1 mod N` in the two exact intervals, beginning
  with the full-conductor portions of the surviving `N=256,s=5` profiles
  after the 2-adic cofactor screen. In `(3,4,0)`, use the signed
  three-term-progression/parallelogram templates forced by `C<=-13`.
  Its odd norm part must itself be the row prime, so test that exact object
  rather than a 63-integer cofactor window. Treat the `N=512,s=3` band
  independently;
- construct an exact pair-feasible candidate-class row above its allowance and
  retire this target;
- provide a total per-input image/collision certifier theorem; or
- bypass E1 with another direct value family. The complete-support first-
  moment cut has already eliminated averaged occupancy at these anchors.

Birthday scans and almost-all-primes estimates remain evidence only.
