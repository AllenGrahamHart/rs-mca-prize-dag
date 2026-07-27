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
`(4,2,0),(3,4,0)` at `s=5`. At `N=512,s=2`, exact negacyclic
autocorrelation variance excludes the four-singleton profile `(0,4,0)`, so
only `(1,2,0)` remains. The entries count opposite pairs, singletons, and
same-sign pairs.

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
  with the surviving `s=5` profiles and the sole `N=512,s=2` profile
  `(1,2,0)`;
- construct an exact pair-feasible candidate-class row above its allowance and
  retire this target;
- provide a total per-input image/collision certifier theorem; or
- bypass E1 with another direct value family. The complete-support first-
  moment cut has already eliminated averaged occupancy at these anchors.

Birthday scans and almost-all-primes estimates remain evidence only.
