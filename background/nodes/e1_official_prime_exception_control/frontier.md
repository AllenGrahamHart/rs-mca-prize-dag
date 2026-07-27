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
sparse-autocorrelation refinement removes `78<=V<=134`. Four exact
quotient-Schur packets remove `V=76,74,72,70`; complete endpoint chains remove
`V=68,66,64,62`, leaving positive even `V<=60`. At `V=64`, exact slack, cubic, and
parity arithmetic leaves only autocorrelation profiles `(4,7)`, `(0,8)`, and
`(3,5,1)`. The zero-odd profile `(0,8)` is empty by a complete six-template
light census; the two four-odd profiles share exactly 148 affine light
templates, all with one repeated wedge and no light diameter. Independent
joint censuses exclude `(3,5,1)` at exact `M_3=1392<1517`; `(4,7)` alone
has full-conductor census maximum 1524. Complete FLINT and independent PARI
resultant ledgers put all 60,148 such norms below `2^250`, closing the profile
and endpoint. At `V=62`, exact slack gives `L<=17`; parity leaves only
`(3,7)`, `(2,5,1)`, and `(1,3,2)` on 960 normalized light supports in eight
affine odd-unit orbits. Folded-chord and direct-negacyclic engines each cover
158,783,488 representative signed vectors. Exact unrestricted maxima 1068
and 1122 close `(2,5,1)` and `(1,3,2)`; the full-conductor maximum 1206 closes
that part of `(3,7)` below the `M_3=1302` cutoff, and the conductor theorem
closes its complement. At `V=60`, exact slack gives `L<=18`, the exact cubic
cutoff is `M_3=1087`, and parity leaves eight profiles. A complete mod-16
allocation ledger closes `(0,3,2)`, `(6,2,0,1)`, and `(3,0,3)`. Two
independent 87-template censuses scan 1,726,770,432 representative vectors and
close `(1,5,1)` below the cubic cutoff; independent FLINT and PARI ledgers put
all 28,114 full-conductor `(2,7)` norms below `2^250`. The conductor theorem
handles both complements. A subsequent 1,234-mask structured relaxation has
only three profile-`(4,2,2)` assignments above the cutoff; actual-vector
censuses reduce them to six vectors, and conductor plus exact norms exclude
all six. A second structured relaxation covers 2,924,654,040 profile-
`(5,4,1)` assignments; independent exceptional censuses cover 6,371,187,456
actual vectors per engine and reduce the primitive residue to 86 vectors.
Independent FLINT/PARI norms exclude all 86. For the final profile `(6,6)`,
independent relaxations cover 44,779,702,968 assignments and identify 1,191
exceptional masks. Independent actual-vector engines agree after
23,638,891,776 vectors each, leaving 1,232 primitive exceptions; independent
exact norms exclude all 1,232. Thus `V=60` is empty and the live positive even
frontier is `V<=58`. At `V=58`, exact slack gives `L<=17`, the cubic cutoff is
`M_3=872`, and diameter parity leaves eight profiles. Their complete relevant
light atlas has 264 one-odd and 14,400 five-odd supports in 111 affine
templates. Folded-chord and direct-negacyclic engines agree after
2,203,120,896 vectors each, finding 4,812 cubic exceptions. The conductor
theorem removes 3,992. FLINT and PARI agree on all 820 primitive norms, whose
247-bit maximum satisfies `9*N_max<2^250<10*N_max`. Hence `V=58` is empty and
the live positive even frontier is `V<=56`. At `V=56`, exact slack gives
`L<=16`, the exact cubic cutoff is `M_3=658`, and parity leaves eight profiles
on six zero-odd and 148 four-odd affine templates. Two complete independent
censuses agree after 3,056,582,144 vectors each and leave 12,638 cubic
exceptions. Conductor removes 8,266; FLINT and PARI agree on all 4,372
primitive norms, with `6*N_max<2^250<7*N_max`. Hence `V=56` is empty and the
live frontier is `V<=54`. At `V=54`, exact slack gives `L<=15`, the cubic
cutoff is `M_3=443`, and parity leaves six profiles on eight three-odd affine
templates. Two independent censuses agree after 158,783,488 vectors each and
leave 2,000 cubic exceptions. Conductor removes 1,596; FLINT and PARI agree on
all 404 primitive norms, whose 247-bit maximum satisfies
`10*N_max<2^250<11*N_max`. Hence `V=54` is empty and the live frontier is
`V<=52`. At `V=52`, exact slack gives `L<=16`, the exact cubic cutoff is
`M_3=228`, and parity leaves six two-odd and four six-odd profiles. Complete
independent censuses close all six two-odd profiles after 1,726,770,432
vectors per engine. Of 17,624 cubic exceptions, conductor removes 9,564;
FLINT and PARI agree on all 8,060 primitive norms, whose 249-bit maximum
satisfies `2*N_max<2^250<3*N_max`. The live endpoint is therefore exactly the
four six-odd profiles `(6,5)`, `(5,3,1)`, `(4,1,2)`, and `(6,1,0,1)` on 1,234
affine light templates. Their direct-census floor is 24,492,353,024 vectors
per engine, so the next attack must exploit odd-mask, quotient, or norm
structure rather than enumerate the undifferentiated chamber. A subfield norm
argument also
removes every vector
in either folded profile whose support differences have a nontrivial gcd with
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
  after the 2-adic cofactor screen. In `(3,4,0)`, the exact `V=52` reduction
  and complete two-odd exclusion are banked. Attack only the four six-odd
  profiles, beginning with structural odd-mask, quotient, and norm filters;
  do not launch their 24,492,353,024-vector direct census. Every `V>=54`
  chamber is closed and must not be rerun. Compare the E26 residual against
  the 419 exact cofactor classes in `(4,2,0)`. Treat the `N=512,s=3` band
  independently;
- construct an exact pair-feasible candidate-class row above its allowance and
  retire this target;
- provide a total per-input image/collision certifier theorem; or
- bypass E1 with another direct value family. The complete-support first-
  moment cut has already eliminated averaged occupancy at these anchors.

Birthday scans and almost-all-primes estimates remain evidence only.
