
## WAVE-15 ADDENDUM (2026-07-20; fiber-two path residue)

The direct equal-complete-fiber residue in both path-plus-singleton chambers
is now empty at common fiber size two. For the three tight-triangle blocks,
write their completed locators as `H_i(X^2)` and their deleted roots as
`r_i`. Then

```text
H_i(Y)=(Y-r_i^2)K_i(Y),       A_i=(X+r_i)K_i(X^2).
```

Separating odd and even powers in the nondegenerate three-term relation
forces all `K_i` to be scalar multiples of one common polynomial `K`. At
official half-degree `s=d/2=2^38`, `K(X^2)` is nonconstant and divides all
three locators, contradicting the disjoint omitted-triple blocks. Combined
with the Vandermonde exclusion for `m>=3`, every direct common-map path
construction with equal complete fibers of size `m>=2` is excluded.

The structure-free `m=1` case, mixed quotient maps, partial fibers, primitive
locators, and the four-cycle fiber-two branch remain open. This is a chamber
reduction, not an adjacent-crossing theorem.

---

## WAVE-16 ADDENDUM (2026-07-20; fiber-two cycle embedding)

The direct common-`X^2` four-cycle residue now has an exhaustive
quartic-pencil router. The completion roots are automatically distinct:
coincidence would put their common negative in two disjoint block locators.
Writing `d=2s` and `Y=X^2`, its four completed blocks give

```text
H_i(Y)=(Y-rho_i^2)G_i(Y),
D_* product_i G_i=Y^(2d)-1,
sum_i lambda_iG_i=sum_i lambda_i rho_iG_i=0,
```

The `G_i` are pairwise coprime monic degree-`s-1` polynomials spanning a
two-dimensional pencil, and `D_*` is squarefree of degree four. If `c` is
the number of antipodal pairs among the deleted roots, then `c in {0,1,2}`.
For `c=0`,

```text
D_*=product_i(Y-rho_i^2),
d_ant=2d=4s,       a_i=rho_i,       b_i=rho_i^2,
```

so this matched stratum is exactly the existing antipodal descent equation.
For `c=1,2`, respectively one or two repeated coefficient-square roots are
replaced by squares of residual antipodal pairs in the exceptional set.
These are explicit denominator-mismatch strata, not instances of the matched
norm equation.

All three strata have a Möbius weld, primitive rational-map degree
`2^38-1`, and lower pencil degree at least `2^37-2` at quotient order `2^40`.
The matched stratum also inherits the direct four-coset exclusion.

The matched primitive census and both mismatch censuses remain open. Mixed
maps, partial fibers, and primitive locators outside the direct completion
model are also not covered. This router does not locate the adjacent crossing.

---

## WAVE-17 ADDENDUM (2026-07-20; doubled-order boundary transfer)

All three fiber-two cycle quartic-pencil strata now inherit the
parameter-uniform boundary compiler through the canonical span identity. At
quotient order `N=2^40`, put `s=2^38` and `r=s-1`. On the generic and
intermediate minimum-degree boundaries respectively,

```text
q=2: v=2^37-2,       h=2^37+1,       deg T=1,
q=3: v=(2^39-5)/3,   h=(2^38+2)/3,   deg T=1.
```

The intermediate residual is linear at this doubled order, rather than
quadratic as at order `2^39`. Both boundaries have the same primary gap

```text
a_(2^38)=a_(2^38+1)=0,       a_(2^38+2)!=0.
```

The generic secondary gaps are at indices `2^37-1,2^37`, and the exact
two-window square has `h=2^37+1` and lower polynomial degree at most
`2^37-2`. If the roots of `D_*` form two antipodal pairs, the parity router
has `M=2^36` and torsion order `8M=2^39`. On the pure outer stratum,
`deg V=2^38-2` with the existing linear Wronskian residual.

The canonical outer quartic must be fractional-linearly matched to the cycle
completion roots `rho_i`. For `c=0` this is the old square-root-lift matching.
For `c=1,2`, matching to arbitrary square-root lifts of all denominator roots
is incorrect; a new scalar/Möbius coupling is required before importing the
old norm gates. No boundary is excluded by this transfer.

---

## WAVE-18 ADDENDUM (2026-07-20; matched cycle lift field router)

The two-antipodal-denominator subbranch of the matched `c=0` generic boundary
at `M=2^36` has no genuinely quadratic top-lift shard. Put `N=8M=2^39`.
Replaying the signed-cell cyclotomic resultant at this order leaves only

```text
q_field=p^2,       p=1 mod 2N=2^40.
```

This congruence already puts the root cells, `B_0,C_0`, `lambda,mu`, and all
four outer roots in `F_p`. A normalized source lift ratio satisfies

```text
r^(4N)=1,       r^4=t!=1.
```

In the nonsplit residue class `p=1+2N mod 4N`, Frobenius sends `r` to
`r^(2N)r`. If this is `-r`, conjugating each of the three exact
Mobius-ratio equations gives either `r^2=-1`, or forces both `r^2` and the
outer ratio into `X^2+6X+1=0`; their incompatible `N`th powers exclude both
possibilities. Thus every surviving normalized source quadruple and its
Mobius matching descend to `F_p`, whether or not `p=1 mod 2^41`.

The remaining work on this matched parity subbranch is the doubled-order
transfer of the constant, scalar, Jacobi, and norm gates. Other matched
denominator geometries and the `c=1,2` completion-root couplings remain
separate, and no cycle boundary is excluded here.

---

## WAVE-19 ADDENDUM (2026-07-20; matched post-field compiler)

The matched `c=0` two-antipodal-denominator generic branch is now
nonharmonic at `M=2^36`. The old exact characteristic packet excluded source
trace levels `1,...,38`. A bounded 16-shard Modal extension checked the only
new level `39` over all `2,247,720` split official congruence classes and
found no hit, before imposing primality.

The complete nonharmonic post-field classifier transfers with one necessary
repair. Put `N=2^39`, form the unique constant-ODE direction `U_0`, and
divide

```text
R=(x^N-1)/D_0-(xU_0^2)^2=(xU_0^2)S+T.
```

For one of the three printed source pairings, completion is equivalent to
the scalar identity, outer trace, and final square conditions

```text
deg S=2^37-2,       4b_jT=a_jS^2,
y_(m+1)=y_m^2-2,       y_39=2,
q_out^2-y_0q_out+1=0,       T/q_out=W^4,
deg W=2^36-1.
```

Both reciprocal roots for `q_out` give the same fourth-power verdict. The
quotient by `q_out` is essential: `p=1 mod 2^40` makes every outer ratio a
square, but not always a fourth power. In the nonsplit field class with
`q_out` of exact order `2^39`, the old test `T=W^4` would falsely reject the
correct quartic coset.

The constant/Legendre first gate transfers at coefficient index `2^38-1`,
the source trace depth is `41`, and every accepted branch satisfies the
corrected gcd floor `deg gcd(S,P)>=2^36-1`. The later trace-Jacobi and
cyclotomic-norm endpoint remains to be transferred before a contributor run
is coverage-equivalent. No branch is proved empty by these necessary gates.

---

## WAVE-20 ADDENDUM (2026-07-20; matched trace-Jacobi norm transfer)

The trace/Jacobi exclusion interface now transfers to the matched parity
branch at

```text
M=2^36,       L=2^37,       N=2^39.
```

For each fixed `epsilon`, the Chebyshev/Gegenbauer sign router gives six exact
one-variable trace gcds of degree at most `L`. The quadratic even-Jacobi
transform replaces these by a coverage-equivalent six-gcd packet of degree at
most `M`, with primary polynomial

```text
J_M^(-1/4,-1/2)(w).
```

Before building the signed norm polynomials, every survivor must enter one
of two torsion resultants. The `epsilon=-1` packet is one cyclotomic norm at
order `8M=2^39`; it can occur only in the fully split field class. The
`epsilon=1` packet is exactly the 37-level tower

```text
2^2,2^3,...,2^38.
```

The complete interface therefore has two six-gcd packets, at most twelve
signed branches total. Equivalent trace factorizations keep every modular
polynomial degree at most `2^36`, including the two conjugate `sqrt(2)`
factors of the minus packet.
If no official characteristic divides either torsion resultant, this matched
parity branch is empty. A compatible divisor is only a first-rejection
survivor: it must still pass one signed Jacobi norm and the corrected
`T/q_out=W^4` post-field gate.

No official norm has been evaluated. Dense degree-`2^36` polynomials and
explicit integer resultants are out of scope; the remaining task is a
compressed algorithm, pilot, checker, and costed contributor campaign.

---

## WAVE-21 ADDENDUM (2026-07-20; mismatch invariant coupling)

The `c=1,2` denominator-mismatch strata now have an exact completion-root
coupling. Factor the already split quartic `D_*` and let `Omega` be its four
roots. For `c=1`, choosing the repeated completion square, the residual
exceptional square, and one relative sign gives exactly `4*3*2=24` candidate
source quartics. For `c=2`, choosing the two completion-pair squares gives
exactly `binom(4,2)=6` candidates.

For a binary quartic with classical invariants `I,J`, each candidate matches
the canonical outer quartic exactly when

```text
I_out^3 J_src^2=I_src^3 J_out^2.
```

Thus the missing Mobius derivation is replaced by a union of 30 root-
permutation-free scalar tests. Every passing test reconstructs its
base-field PGL map. No test is yet proved impossible, and the matched
trace-Jacobi norm gates do not automatically apply to these mismatch
packets.

---

## WAVE-22 ADDENDUM (2026-07-20; mismatch trace resolvent)

The `24+6` mismatch packet now has a radical-free constant-degree
elimination. For `c=2`, a selected denominator pair `{A,B}` enters only
through

```text
z=(A+B)^2/(AB).
```

The six pair traces are the roots of one explicit symmetric degree-six
resolvent `R_D(z)`, while outer matching is the degree-three equation

```text
4I_out^3 z(z-36)^2-J_out^2(z+12)^3=0.
```

Thus the whole `c=2` packet is exactly one degree-`6`/degree-`3` resultant.
For `c=1`, reducing the sign test in `F[u]/(u^2-BD)` and taking its
quadratic norm replaces the 24 lift-sign tests by twelve explicit
base-field equations. These thirteen radical-free gates can be substituted
directly into the doubled-order gap and canonical-span equations.

This is a symbolic elimination, not an emptiness theorem. Reconstructing the
Mobius pole gives no additional condition: the canonical converse already
reconstructs the locator relations from any passing PGL match. Pairing the
four pencil factors also gives Pell-type identities, but those are automatic
rewrites of the reconstructed `U,V` packet and do not reduce its variables.
Neither route authorizes an official-order computation.

---

## WAVE-27 ADDENDUM (2026-07-20; c=1 parity harmonic close)

The two residual harmonic `c=1` parity classes are now excluded. The
denominator-only cyclotomic field bound transfers and leaves exactly

```text
q_field=p^2,       p=1+k*2^40,
29058991<=k<33554432.
```

Both source lifts descend to `F_p`. Their torsion conditions are exactly
41 trace updates from `8/5` and 40 updates from `16`, respectively.

A preregistered 32-shard Modal campaign checked all `4,495,441` integer
moduli in the interval, including composites. All shards completed with
exact contiguous coverage, rolling digests replay, the longest took 3.121
seconds, and neither trace had a hit. Therefore

```text
q_out!=-1
```

on the generic `c=1` two-antipodal-denominator chamber. The six
nonharmonic trace tests and the nonparity normalized chamber remain open.

---

## WAVE-26 ADDENDUM (2026-07-20; c=1 parity Mobius router)

If the normalized `c=1` denominator has two antipodal root pairs, its
completion inventory has exactly two role patterns:

```text
R: X_R=(1,-1,r,iota r),       unused square -1,
P: X_P=(1,-1,iota,iota r),   unused square r^2,
iota^2=-1,       r^(2^41)=1,       r^4!=1.
```

The even canonical outer quartic has ratio trace

```text
tau_O=(alpha^2-2gamma)/gamma.
```

For each of the three perfect-matching cross ratios `z` of each source
tuple, completion matching is exactly

```text
tau_O=4((z+1)/(z-1))^2-2.
```

Thus there are six scalar tests and no outer-root or permutation search.
Each candidate outer trace also obeys the 39-step recurrence
`y_(m+1)=y_m^2-2,y_39=2`.

At harmonic outer trace `-2`, the six equations reduce to four symmetry
classes. The class `r=-1` contradicts distinctness. The class
`r^2=-iota` gives parity parameter `t=-1`, where the required primary
coefficient is the nonzero scalar `(1/4)_M/M!`. Only

```text
r^2+3(1+iota)r+iota=0,
5r-4+3iota=0
```

remain up to sign and conjugation. No claim of their exclusion is made.

---

## WAVE-25 ADDENDUM (2026-07-20; normalized c=1 torsion chamber)

Canonical covariance removes the common scale and the root-role union from
the generic `c=1` mismatch packet. Normalize its repeated square `A` to
one and write

```text
b=B/A,       d=D/A,       c=C/A,
S=b+d,       P=bd,
D_A(Y)=(Y-1)(Y-c)(Y^2-SY+P).
```

At `h=2^37+1`, the canonical outer invariants become
`I_A=A^(-4h)I,J_A=A^(-6h)J`, and the normalized radical-free norm is
`A^(-(24h+12))` times the old one. Thus its zero verdict is unchanged.

Membership of all three normalized roots in `mu_(2^40)` is exactly the
forty-step scalar recurrence

```text
T_0=S,       P_0=P,       c_0=c,
T_(j+1)=T_j^2-2P_j,       P_(j+1)=P_j^2,
c_(j+1)=c_j^2,
(T_40,P_40,c_40)=(2,1,1).
```

Together with the printed split, square, distinctness, coefficient-gap, and
canonical-span conditions, every survivor and only a survivor is represented
by one role-labelled triple `(S,P,c)`. The normalization is not a proof
that the chamber is empty.

---

## WAVE-24 ADDENDUM (2026-07-20; c=1 coefficient resultant)

The twelve radical-free `c=1` mismatch norms now form one coefficient-only
constant-degree resultant. If `A` is the repeated completion square and
`C` the unused residual square, put

```text
S=e_1-A-C,       P=e_4/(AC),
Nhat(A,C)=(AC)^6 N(A;S,P),
H(A,C)=(D_*(C)-D_*(A))/(C-A).
```

Then `Nhat` is polynomial of degree at most 18 in each variable and the
whole packet passes exactly when

```text
Res_A(D_*(A),Res_C(H(A,C),Nhat(A,C)))=0.
```

The scalar is `e_4^36` times the product of the twelve old norms. The
divided quartic removes the forbidden diagonal `A=C`, while ordered pairs
retain the distinction between the repeated and unused roots. This compiles
the coupling without factoring `D_*`; it does not prove the resultant
nonzero on the canonical gap locus.

---

## WAVE-23 ADDENDUM (2026-07-20; c=2 outer torsion trace)

Every `c=2` mismatch survivor now passes an outer-only dyadic trace gate.
For a selected completion-square pair put

```text
t=A/B,       z=t+t^(-1)+2,
K_O(Z)=4I_out^3 Z(Z-36)^2-J_out^2(Z+12)^3.
```

Then `t^(2^40)=1` and `K_O(z)=0`. Starting with `Q_0=Z-2` in the
cubic quotient algebra and iterating

```text
Q_(j+1)=Q_j^2-2 mod K_O
```

for forty steps gives the necessary gate

```text
gcd(K_O,Q_40-2)!=1.
```

Every remainder has degree at most two. This tests the official torsion
order with forty small polynomial reductions rather than a dense
degree-`2^40` trace polynomial. Passage is not sufficient: the common trace
still has to arise from an actual pair of roots of `D_*` and pass canonical
span. No `c=2` survivor is asserted to exist or to be excluded.

---

## WAVE-24 ADDENDUM (2026-07-20; c=2 joint pair-torsion selector)

The outer torsion trace and denominator-pair tests now meet at the same trace
value. With `R_D` the degree-six actual-pair resolvent and `Q_40` the trace
recurrence above, put

```text
G_2=gcd(K_O,R_D mod K_O,Q_40-2).
```

This gcd is nonconstant exactly when an actual denominator pair `{A,B}` has
both the required outer invariant coupling and `(A/B)^(2^40)=1`. Its distinct
zeros are precisely the passing pair traces, and `deg(G_2)<=3`. This removes
the outer-only false-positive caveat from the previous addendum. Canonical
span, the doubled-order coefficient gaps, and full cycle reconstruction remain
open for every selected pair.

---

## WAVE-25 ADDENDUM (2026-07-20; c=2 normalized pair chamber)

Every pair printed by `G_2` now enters one role-labelled normalized chamber.
After scaling one selected root `A` to one, write

```text
D_A(Y)=(Y-1)(Y-t)(Y^2-SY+P).
```

The selected-pair coupling is `K_A((1+t)^2/t)=0`. Torsion of `t` and both
complementary roots is compiled by forty scalar updates of `t`, their sum,
and their product. Reversing the selected-pair orientation is exactly

```text
(t,S,P) -> (t^(-1),S/t,P/t^2).
```

Consequently later elimination should use this one chamber modulo the
involution, not six labelled denominator-pair cases. The split and square
conditions, primary and secondary gaps, canonical span, and cycle closure
remain required.

---

## WAVE-26 ADDENDUM (2026-07-20; c=2 normalized gap-span interface)

The normalized `c=2` chamber now has one exact gap/span compiler. Write

```text
E(z)=(1-z)(1-tz)(1-Sz+Pz^2)=sum_(j=0)^4 E_jz^j.
```

The coefficients of `E^(-1/4)=sum a_nz^n` satisfy

```text
4n a_n=-sum_(j=1)^min(4,n)(4n-3j)E_j a_(n-j).
```

At `H=2^37+1`, the primary gap is
`a_(2H-2)=a_(2H-1)=0`, `c=a_(2H)!=0`; the secondary gap is the exact
two-window square `LT=cC^2 mod z^H`, with `C(0)=1` and `deg C<=H-3`.
Canonical span then reconstructs the outer coefficients uniquely, beginning
with `alpha=4c`. The selected-pair coupling is the single scalar invariant
equation at `z_t=(1+t)^2/t`.

This is now an exact single-chamber decision interface, but not a rejection
or a cheap official-order algorithm. A future computation must compress this
recurrence/span system and satisfy pre-request `CR-002-C2N`; naive dense
evaluation is not authorized.

---

## WAVE-27 ADDENDUM (2026-07-20; c=2 pure fourth-root exclusion)

The pure fourth-root denominator geometry is now excluded at the official
row. After common scaling it has

```text
E(z)=1-z^4,
E(z)^(-1/4)=sum_(j>=0)((1/4)_j/j!)z^(4j).
```

For `H=2^37+1`, the first required primary zero is at
`2H-2=2^38=4*2^36`, where the coefficient is

```text
(1/4)_(2^36)/(2^36)!=0.
```

The official characteristic bound makes every displayed factor nonzero.
This closes only the scaled fourth-root quartet. It does not claim that the
primary or secondary gaps force that geometry: primary-only rigidity is
false in bounded smooth rows, while official-torsion primary-plus-secondary
rigidity remains an unpromoted theorem route under active falsification.

---

## WAVE-28 ADDENDUM (2026-07-20; c=2 parity trace/Jacobi router)

On a two-antipodal `c=2` denominator, normalize

```text
Omega={1,-1,r,-r},       tau=r^2.
```

The six selected pairs have exactly three trace classes, each twice:

```text
0,       2+r+r^(-1),       2-r-r^(-1).
```

The zero class couples exactly when the canonical outer invariant `J` is
zero. The two cross classes combine into one orientation-free quadratic norm
of `K`. The denominator primary/torsion packet is the same degree-`2^36`
Jacobi packet used by matched `c=0` and generic `c=1` parity, so this chamber
shares the existing CR-002 norm pair and needs no new norm campaign.

This theorem assumes parity; it does not prove that the combined gaps force
it. The minimal structural target is now primary-plus-secondary parity
forcing. The stronger pure-fourth-root conclusion would close `c=2`
immediately, while parity forcing reduces all remaining cases to the shared
CR-002 interface.

---

## WAVE-29 ADDENDUM (2026-07-20; gap-only parity counterexample)

Parity forcing cannot be proved from the two gap packets alone. Over `F_53`
at `H=8`, the split squarefree quartic

```text
E(z)=1+z+11z^2+34z^3+43z^4
```

has `a_14=a_15=0`, `a_16=2`, and

```text
LT/2=(1+22z+49z^2+3z^3+16z^4)^2 mod z^8,
```

but its roots `{2,24,46,48}` are not two-antipodal. Their orders are
`52,13,13,52` and their quadratic characters are mixed, so this does not
touch the official order-`2^40` chamber. It proves that the live parity target
must retain root torsion. Splitting and common square class are now known to
follow from that torsion on the official row. The two-window differential
identity by itself is insufficient.

---

## WAVE-30 ADDENDUM (2026-07-20; secondary differential certifier)

The exact gap interface no longer requires the high window through degree
`3H-1`. With `B=sum_(n=0)^(2H-3)a_nz^n`, `b=a_(2H-3)`,
`c=a_(2H)`, and `kappa=E_4b/c`, the primary gap gives

```text
E'B+4EB'=-8Hc z^(2H-1)+8(H-1)E_4b z^(2H).
```

The secondary gap is equivalent to `C(0)=1`, `deg C<=H-3`, and

```text
z^H divides
  zE'C^2+4HEC^2+4zECC'-(4H-4(H-1)kappa z)B.
```

The dividend has degree at most `2H-2`. Sufficiency follows coefficientwise
from the nonzero diagonal factors `2n+4H`. This is an exact compiler, not a
parity claim; official root torsion remains the live structural input.

---

## WAVE-31 ADDENDUM (2026-07-20; c=2 torsion-field router)

The official scalar torsion gate absorbs two formerly separate side
conditions. Its terminal equations imply `c^(2^40)=d^(2^40)=1`. Since
`2^41 | q-1`, all normalized denominator roots therefore lie in `F_q` and
are squares. Splitting and common square class are not independent axes of
`C2-PAR`; only distinctness remains separate.

The maximal field collapse also gives one exact field split. Either all
normalized torsion parameters lie in `F_p`, or `q=p^2`,
`p=-1 mod 2^40`, and

```text
x^p=x^(-1)       for x in {t,c,d},
E_j^p=E_(4-j)/E_4.
```

The latter is coefficientwise reciprocal Frobenius. It does not identify a
packet with its conjugate or with selected-pair orientation reversal, so it
does not prove parity. It does reduce a symbolic attack or contributed
certificate to fixed and unitary reciprocal chambers.

---
