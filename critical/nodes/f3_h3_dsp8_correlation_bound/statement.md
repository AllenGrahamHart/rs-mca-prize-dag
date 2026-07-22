# DSP8: the split-pencil / line-fiber correlation bound

- **status:** TARGET (minted 2026-07-19 at the C36 amber ceremony; alt leaf, gate=any)
- **consumer:** `f3_h3_mobius_excess_half` (alt)

At every official row in the open range `n^2<=p<=6^(n/4)`, put

```text
S_A=sum_(t antipodal,P(t)>=25)R(t),
Q_n=(n-1)(n-2).
```

The live target-sensitive primitive shift-pair correlation is

```text
10K_25^0+17K_25^A+68S_A+(867/4)n^(5/3)
 <=750n^2-255Q_n.                                  (DSP8)
```

Here `K_25^0,K_25^A` count the decorated disjoint split members of
`Q_(t,r)(X)=X^2-(1+r-t)X+r`, paired with the affine line fiber, in the
proved primitive-SP normalization. The pin is
`(X-r)Q_(t,s)-(X-s)Q_(t,r)=t(s-r)X`. The proved antipodal quotient-mass
and global overlap-cover payments show that `(DSP8)` closes the exact `E=6`
residual and hence the C36 red on the analytic route.

The target-independent estimate

```text
160(10K_25^0+17K_25^A)<=76599n^2                   (DSP8-U)
```

is sufficient for `(DSP8)`. It supersedes the former stronger sufficient
constants `29031/80` and `223`; the latter is equivalent to the former
`10J_25^0+17J_25^A<=892n^2` target.

PRE-REGISTERED F-ROUND 1 (completed against the former stronger bound):
measure `J_25^0,J_25^A` exactly at analogue rows across at least three
scales. It survived vacuously because no measured row reached `P>=25`.
FALSIFIER for the live leaf: one official row violating `(DSP8)`. Such a row
falsifies this sufficient analytic route; it need not falsify C36 itself.

PROVED PRIMITIVE-SP ADAPTER: write `K_25^0,K_25^A` for decorated ordered
degree-three/depth-one shift-pair records after forgetting the two internal
root orders at each endpoint. The adapter proves

    J_25^c = 4 K_25^c = 8 D_6,25^c

and every such cubic pair is coefficient-primitive because `n` is a power of
two and `gcd(n,3)=1`. The formerly selected stronger estimate was

    10 K_25^0 + 17 K_25^A <= 223 n^2.

The proved antipodal quotient-mass and global overlap-cover payments replace
it by `(DSP8)` and the uniform sufficient estimate `(DSP8-U)`. This is an
equal-constant
primitive-SP subclass with the quotient-line weight retained.
Quotient-pullback deletion cannot reduce it, and an unweighted SP count does
not prove the required correlation.

PROVED UNIT-PRODUCT TRACE NORMAL FORM: write the distinguished roots as
`R,S`, let `q^3=RS`, and divide all six cubic roots by `q`. Cubing is
bijective on the dyadic subgroup, and the decoration forces

    q=rs,       ruv=sxy=1,
    sigma=r+u+v=s+x+y,
    t=1+rs(r+s-sigma).

Conversely these data reconstruct the decorated pair with no free subgroup
scale. The residual split conditions are exactly

    T^2-(sigma-r)T+r^(-1),
    T^2-(sigma-s)T+s^(-1)

splitting over `H`, together with the retained class predicates and
`1-w=t(1-z)`. Thus generic cubic-SP all-pairs enumeration, of ambient order
`n^6`, is not a closing route. The open content is the normalized
trace/split/quotient-line correlation with its exact class weights.

PROVED ANTIPODAL CAYLEY-PRODUCT ROUTER: for an antipodal target
`t=1-a^2`, put

    C(h)=(1+h)/(1-h),       B=C(H\{1,-1}),
    M_a=#{(alpha,beta) in B^2:alpha beta=C(a)}.

Then `P(1-a^2)=2+M_a` exactly; the two extra records are the two orders of
`{a,-a}`. Hence the DSP8 richness filter is `M_a>=23`, equivalently
`M_a>=24` by the proved antipodal parity theorem. If `E_a`
counts ordered signed-disjoint edges among the corresponding small-generic
factor pairs and `L_a=R(1-a^2)`, then

    K_25^A=sum_(a canonical, M_a>=24) E_a L_a.

This isolates the expensive class as quotient-weighted restricted
multiplicative energy in the Cayley image. It does not bound that energy or
decorrelate it from `L_a`; either omission changes the consumer.

PROVED QUOTIENT ANHARMONIC / ANTIPODAL-TWIN SYMMETRY: the quotient weight is
constant on

    {t,1/t,1-t,1/(1-t),t/(t-1),(t-1)/t}.

On an antipodal target `t=1-a^2`, the involution `tau(t)=t/(t-1)=1-a^(-2)`
also preserves the exact product richness `P(t)`. Thus antipodal candidate
evaluation may canonicalize `tau`-orbits while retaining multiplicity. The
same theorem proves that class-A richness begins at `P=26`, not `P=25`.
The signed-disjoint edge count is not invariant: an exact `F_97`, order-32
control has equal `(P,R)=(6,9)` at `t=23,76` but edge counts `0,1`. Hence
the symmetry cannot merge the DSP8 summands or close the target.

PROVED UNIT-TRACE CURVE GEOMETRY: the normalized product-one triple
`(r,u,(ru)^(-1))` lies on

    C_sigma: X^2Y+XY^2-sigma XYZ+Z^3=0.

In characteristic different from `2,3`, this is a smooth geometrically
irreducible genus-one curve unless `sigma^3=27`; at those at most three trace
values it has one ordinary node and geometric genus zero. Raw ordered
curve-point records satisfy `G_25^c=4K_25^c=J_25^c`, so the live target is
also

    10G_25^0+17G_25^A+272S_A+867n^(5/3)
      <=3000n^2-1020Q_n.

The upstream same-`(e1,e2)` rational-conic chart is therefore not a consumer
map for DSP8, which fixes `(e1,e3)=(sigma,1)`. The open content is a
signed-disjoint, rich, quotient-weighted subgroup point-pair estimate on this
mostly elliptic family.

PROVED NODAL PARAMETER ROUTER AND MARGINAL BARRIER: the `sigma^3=27` fibers
have the rational parameterization

    r=-c/[theta(1+theta)],
    u=-c theta^2/(1+theta),
    v= c(1+theta)^2/theta.

Their subgroup points lie in at most three affine coset-pair branches. The
optimized one-fiber Stepanov theorem proves each branch, and every quotient
line fiber, has fewer than `4n^(2/3)` points. Hence

    N_sigma<12n^(2/3)+1,
    G_sing^0+G_sing^A
      <12n^(2/3)(12n^(2/3)+1)^2.

This reaches the correct `O(n^2)` exponent, but after the class weight its
leading coefficient is `29376`, versus a target-sensitive allowance whose
uniform lower envelope is `76599/40`. The
pair target has an exact four-factor rational form recorded in the proved
node. Thus the nodal locus is not deleted: closing it requires its richness,
signed-disjointness, or target/quotient correlation, not another marginal
point bound.

PROVED CUBE-PREIMAGE COMPRESSION AND SHARPENED NODAL ENVELOPE: put
`g=gcd(3,p-1)` and

    K={x:x^3 in H},       |K|=gn.

Across all singular traces at once, the nonnode subgroup points are exactly
the parameters `theta in K` with `1+theta in K`, after removing the tangent
parameters. An exact Stepanov optimization for subgroup orders `n,3n` gives

    #{x:L_1(x),L_2(x) in K} <(51/16)|K|^(2/3).

Consequently the worst-class weighted nodal contribution is below

    552n^2   if p=2 (mod 3),
    2387n^2  if p=1 (mod 3).

This supersedes the branchwise constant `29376`. The one-cubic-root nodal
slice cannot itself falsify DSP8, but the smooth slice still needs a disjoint
budget; in the three-cubic-root case even the sharpened nodal envelope remains
above `76599/40`. The target-divisor pruning node separately retains the exact
signed-disjoint live residual.

PROVED NODAL TRACE-ORBIT ENERGY ROUTER: restrict each singular trace to its
internally signed-distinct ordered point presentations and write their counts
as `N_c`. Every unordered triple has exactly six presentations, while a
signed-disjoint pair cannot use two presentations of the same triple. Hence
the class-blind nodal square sharpens to

    E_tr=sum_c N_c(N_c-6),
    10G_sing^0+17G_sing^A<(867/16)n^(2/3)E_tr.

When `p=1 (mod 3)`, the trace class of a nodal parameter `theta` is the class
of `theta(1+theta)` in the order-three quotient `K/H`. If `S` is the
corresponding cubic-character sum and `N=sum_c N_c`, then exactly

    E_tr=(N^2+2|S|^2)/3-6N,
    N<(51/16)(3n)^(2/3).

Thus `E_tr<=(51066/1445)n^(4/3)` pays the full uniform nodal allowance. The
distribution-free gate `N<=(59/10)n^(2/3)` already implies that energy cap,
while the proved point theorem gives `N<(106131/16000)n^(2/3)`. Cubic trace
balance is therefore relevant only in the narrow interval between those two
coefficients. The
more transparent sufficient condition `|S|<=4N/5` puts the nodal payment
below `1812n^2`, leaving more than `103n^2` for smooth traces. Neither
condition is proved: sparse nodal sets can have full cubic bias, so this is
an exact Pareto router rather than an equidistribution claim.

PROVED NODAL STEPANOV CONSTANT BARRIER: every parameter choice in the current
one-auxiliary-polynomial ansatz satisfies

    (A+2mB)/D > 2^(5/3)m^(2/3).

Using that ansatz for both the order-`n` quotient line and order-`3n`
cube-preimage intersection forces a class-blind leading coefficient above
`2176`, already larger than `76599/40`. Retuning the Stepanov integers cannot
close the three-cubic-root nodal lane. A signed-disjoint nodal antipodal
control at `(n,p)=(64,7937)` shows that replacing weight `17` by `10` without
the richness gate is also false. The live routes are target/richness/
disjointness correlation, trace-sensitive distribution, or a genuinely
stronger multi-fiber theorem.

PROVED NODAL DECORATION CLASS-DISCOUNT NO-GO: over `F_769` with the
order-256 subgroup, one exact signed-disjoint singular pair has all nine
decorations in the live `P>=25,R>0` locus, but seven of the nine targets are
antipodal. Thus neither a `4/9`, `5/9`, nor `2/3` class-A fraction cap follows
from the decoration packet, signed disjointness, richness, and quotient
support alone. This fixture has `p<n^2`, so it does not falsify DSP8 or a
field-size-dependent official estimate. It rules out using a universal
decoration-mix discount to repair the three-cubic-root nodal constant; a
successful discount must consume `p>=n^2` or a genuine cross-target
correlation.

PROVED RICH FACTORIAL MOMENT COMPILER: define

```text
F_25^c=sum_(t in class c,P(t)>=25)P(t)(P(t)-2)R(t),
M_21=sum_(t!=1)P(t)(P(t)-1)R(t).
```

Counting all pairs of generic vertices before imposing signed disjointness
gives

```text
10K_25^0+17K_25^A
 <=(1/4)(10F_25^0+17F_25^A)<=(17/4)M_21.
```

Therefore either `40(10F_25^0+17F_25^A)<=76599n^2` or the stronger
unweighted estimate `680M_21<=76599n^2` closes DSP8. The latter permits
`M_21<=(76599/680)n^2`, so the older `FM69` conjecture is substantially
stronger than this consumer requires. No factorial-moment estimate is proved.

PROVED BI-STAR AND DISJOINT-SIX GATES: the rich-excess degree ladder applies
at the DSP8 cutoff with `e=P-18>=7`. Every retained product fiber has at least
eleven small coefficient vectors and two distinct centers of incident
distance-deficit weights at least eight and six. Their normalized stars plus
one cross-center generator form a same-target common-prime `(8,6)` bi-star.

After subtracting the proved distance-four pseudoforest and every
support-overlap edge, an antipodal-free target still has at least eleven
disjoint distance-six edges and therefore a two-leaf pure distance-six star.
An antipodal target has at least two such edges; adding one cross-edge target
generator gives a same-target two-edge ideal. On the separate `P>=33` tail,
the two classes contain pure distance-six stars with at least seven and five
leaves. These are the preferred CR-001 template families. They do not bound
the number of ideal-norm survivors or their quotient weights.

PROVED NODAL/SMOOTH HIGH-TAIL DOMINATION: on a fixed target, the nodal graph
on generic product representations has maximum degree three. Combining this
with the disjoint-six multiplicity lower bound gives

    D_nod(t) <= D_sm(t)

whenever `P(t)>=33` off the antipodal class or `P(t)>=35` on it. Therefore
the full disjoint high tail is at most twice its smooth part, target by target
and with the same quotient weight. The only untreated low portions of this
router are the bounded multiplicity bands `25<=P<=32` off the antipodal class
and `25<=P<=34` on it. This removes nodal traces as an independent high-tail
budget, but it does not estimate either low band or the smooth quotient-
weighted moment.

PROVED ACCIDENT-DEPTH COMPILER: put `rho_L(t)=(R(t)-L)_+`. Fixing one
denominator proves `sum rho_L(t)<=(n-2)^2`. Paying `L` quotient layers and
product excess through `E` leaves an exact positive budget whenever
`L+E=17`. Therefore exclusion of any one rectangle

```text
(P,R)>=(19,18),(21,16),(25,12),(29,8),(33,4)
```

proves C36'. The original fixed-order endpoint uses `rho_3=(R-3)_+`:

```text
Mbar_(3),6,33^0+(53/42)Mbar_(3),6,33^A
 <=(583/272)n^2 <2.144n^2.
```

The wider `rho_1` analytic alternative retains constant `2385/272`. Every
positive selected summand has `R>=4`, so its degree-seven or
degree-five pure distance-six star can be batched with four distinct quotient
lifts at the same row-prime ideal, at least three of whose normalized
product-to-quotient couplings are nonzero. The complete four-coupling batch is
odd-locally equivalent to one nonzero coupling anchor and the three-spoke
quotient-collision star. Rows outside `P>=33,R>=4` require no fixed-order
survivor certificate on this route. The reduced moment and joint-ideal
survivor bound remain open.

PROVED JOINT-STAR / QUOTIENT-DEPTH PARETO COMPILERS: using disjoint
distance-six edges directly gives twelve independently sufficient moment
routes, one at every integer corner

```text
(P,R)>=(25,12),(26,11),...,(34,3),(35,2),(36,1).
```

Their product packets strengthen from a degree-two free star to
degree-eight/six class-sensitive stars, while the anchored quotient packet
shrinks from eleven spokes to none. At the five odd cutoffs
`E=7,9,11,13,15`, swap parity confines the last paid low-excess unit to
diagonal targets. The affine subgroup-line bound therefore raises their
uniform allowances to

```text
E=7:   (89023/43520)n^2
E=9:   (72837/27200)n^2
E=11:  (72837/21760)n^2
E=13:  (72837/19040)n^2
E=15:  (380371/87040)n^2.
```

Each also has a stronger row-sensitive budget that subtracts its measured
diagonal quotient-depth mass:

```text
S_(D,E)=sum_(t!=1,D(t)>0)(R(t)-(17-E))_+,
B_par,E=300n^2-17(17-E)(n-1)^2
                 -17(E-1)(n-2)^2-17S_(D,E).
```

The packet shapes and survivor rectangles are unchanged. The last corner has
the row-sensitive form

```text
Dbar_17^0+(29/22)Dbar_17^A <=(29/153)B_par(n),
B_par(n)=300n^2-272(n-1)(n-2)-17S_D,
S_D=sum_(t!=1,D(t)>0)R(t),
Dbar_17^c=sum_(t in class c,P(t)>=36)
                 N_6^disj(t)R(t).
```

The uniform fallback replaces the right side by
`(234697/48960)n^2`.

Every survivor there has a degree-eight or degree-six pure product star and
one quotient lift. For a fixed lift, at most two star vertices lie on the
classified zero-coupling locus, so one of the at least nine or seven vertices
supplies a nonzero coupling anchor. No second quotient or quotient-collision
spoke is needed. Swap parity and the diagonal-target affine payment make this
allowance more than `2.29` times the former value. The preceding,
incomparable `(35,2)` corner keeps the older allowance

```text
Dbar_16^0+(29/22)Dbar_16^A <=(319/153)n^2,
Dbar_16^c=sum_(t in class c,P(t)>=35)
                 N_6^disj(t)(R(t)-1)_+.
```

Its two-lift quotient packet is odd-locally equivalent to one nonzero coupling
anchor plus one quotient-collision spoke. These are alternative sufficient
routes to C36', not proofs of either displayed inequality or of `(DSP8)`
itself.

PROVED SINGLE-QUOTIENT CANDIDATE COMPRESSOR: for the `(36,1)` packet, the
ideal generated by a product star and one coupling is exactly independent of
the chosen star center. It is nonzero even when the selected coupling is zero,
so the canonical center may be used without a zero-locus test. The official
prime support of this endpoint is exactly

```text
p divides s_(n,35)^X
  iff some t!=1 has P(t)>=36,R(t)>=1
  iff Dbar_17^0+Dbar_17^A>0,
```

and `s_(n,35)^X` divides the cutoff-18 scalar annihilator. This removes the
quotient index and anchor designation from candidate generation. It does not
compute or bound the annihilator or the retained moment.

PROVED QUOTIENT GALOIS-ORBIT DECOMPOSITION: for `n=2^s`, the ordered
nonidentity quotient lifts form `3(n-s-1)` odd-Galois orbits, with
`3(2^j-1)` orbit polynomials of degree `2^j`. The radical support of
`s_(n,35)^X` is exactly the union of the orbitwise scalar-annihilator
supports. At `n=8192`, the candidate computation therefore has `24,534`
independent blocks of degree at most `4,096`, rather than one rank-`67,084,290`
algebra. The total degree and the open `Dbar_17` moment are unchanged.

PROVED CANONICAL RESULTANT MANIFEST: the orbit blocks are generated without
orbit enumeration by three unique `(j,sign,w)` families. For
`L=2^(j+1)` and `S_w=1+Z+...+Z^(w-1)`, each plus block is
`Res_Z(Z^(2^j)+1,T-S_w)`, while each even-`w` minus block is its monic
power-of-two-normalized reciprocal. This supplies reproducible block IDs and
polynomials, not an elimination algorithm or an identification of candidate
support between reciprocal blocks.

PROVED THREE-RESULTANT CANDIDATE SCREEN: for each canonical block `q_O`,
the resultants against the first three product Hasse derivatives are not all
zero, and the exact cutoff-35 block scalar divides their positive odd gcd
`g_O`. Thus all official `(36,1)` candidates occur among the prime factors
of `73,602` ordinary resultants at `n=8192`. Complete factorization and exact
row filtering can replace exact scalar elimination. The gcd support is only
a superset: different derivatives may meet different roots modulo a prime.

PROVED TAYLOR-CONTENT EXACT SUPPORT: the coefficient content of
`Res_T(q_O,sum_(i=0)^35 Pcal_n^[i](T)X^i)` has exactly the odd prime radical
of the block scalar annihilator. Thus one polynomial resultant per block is
an exact support-level alternative to Smith elimination and removes the
three-resultant screen's false positives. Its maximum `X`-degree is `143,360`
at `n=8192`; coefficient growth and computational cost remain open.

PROVED TAYLOR CUTOFF LADDER: the same exact content theorem holds for every
`c>=2`, with prime supports descending as `c` increases. Any `c<=35` is a
complete pre-screen for `(36,1)`. At `c=2`, the screen exactly detects
quotient-supported triple product collisions, excludes different-root scalar
resultant false positives, and has maximum `X`-degree `8,192` at `n=8192`.
Exact filtering must still remove genuine multiplicities `3<=P<=35`.

PROVED UNORDERED-PRODUCT CUTOFF-12 COMPILER: for the separate vacuous-DSP8
satellite, quotient support is unnecessary. The monic unordered product
polynomial satisfies

```text
Ucal_n^2=Pcal_n Delta_n,       deg Ucal_n=n(n-1)/2,
```

derivatives, together with the inverse selector `(T-1)Y=1`, has exactly the
odd-prime support of rows with nonidentity unordered product multiplicity at
least `13`. Every nonidentity `P(t)>=25` row is retained. The selector removes
the potentially large identity fiber. The only selected cutoff-boundary
overcandidate is `U(t)=13,D(t)=2,P(t)=24`, which exact row replay removes. At
`n=8192` this reduces degree `67,092,481` and twenty-five ordered generators
to degree `33,550,336` and thirteen unordered generators. It is an exact
candidate compiler, not a measured elimination algorithm or a proof that the
candidate support is empty.

PROVED NONIDENTITY P24 GCD CERTIFICATE: over one split row, let `G_12` be
the monic gcd of `Ucal_n` and its first twelve Hasse derivatives, remove its
complete `T=1` factor, and put `H_D=gcd(Delta_n,Delta_n^[1])`. Then

```text
max_(t!=1)P(t)<=24  iff  G_12^neq divides H_D.
```

At target `t` the two gcd valuations are exactly `(U(t)-12)_+` and
`(D(t)-1)_+`. Divisibility therefore says that every retained nonidentity
root has exactly `U=13,D=2,P=24`; it simultaneously rejects multiplicity 14
and the `U=13,D<=1` boundary. This is the exact PASS certificate for the
vacuous-DSP8 satellite. It does not construct the official polynomial or
prove the divisibility on any row.

PROVED NONIDENTITY P25 SUBRESULTANT SCALAR: there is also an exact
sparse-input route. Put

```text
F_n(X)=((1-X)^n-1)/X,
G_n(T,X)=X^(n-1)F_n(T/X).
```

At `T=t`, their gcd degree is exactly `P(t)`. Therefore the coefficient ideal
of polynomial subresultants `0,...,24`, saturated by `(T-1)Y=1`, has a scalar
annihilator whose odd-prime support is exactly the characteristics admitting
some nonidentity `P(t)>=25`. This route has no unordered/diagonal boundary
overcandidate and begins with two degree-`n-1` binomial polynomials. Its
zeroth subresultant is still the degree-`(n-1)^2` global product resultant, so
no official-scale complexity or factorization claim follows.

PROVED P25 QUADRATIC DIVISOR TOWER: a nonidentity `P>=25` fiber can also be
represented without constructing either global product polynomial. Select a
monic degree-25 common divisor `Q`, invert `X,T,T-1`, and square the residues
`1-X` and `(X-T)/X` through `s=log_2(n)` levels modulo `Q`. Terminal value one
is equivalent to 25 distinct ordered product representations. With explicit
quotient variables, the complete system has

```text
98s+30 variables,       98s+54 quadratic equations,
```

at most `4,048` by `4,072` over the official band. It is empty in
characteristic zero. This is a bounded-degree contributor interface, not a
claim that a four-thousand-variable Nullstellensatz calculation is feasible.

PROVED P25 ORDERED-ROOT TOWER: selecting 25 explicit distinct first
coordinates reduces the quadratic presentation further. Each coordinate has
one inverse and two scalar squaring towers; a quadratic prefix product
inverts all `binom(25,2)=300` pairwise differences. The exact size is

```text
50s+328 variables,       50s+352 equations,
```

at most `2,378` by `2,402`. This is equivalent to nonidentity `P>=25`, but a
generic fiber has `25!` ordered presentations. The lower dimension is
therefore an implementation alternative, not evidence that elimination is
cheaper than the symmetric divisor or univariate routes.

PROVED SMOOTH-TRACE SUBSTAR ROUTER: for fixed target `t` and one product
vertex parameter `r`, a second vertex `s` is nodal only when

```text
(1+r+s-t)^3=27rs.
```

This is a cubic in `s`, so every nodal edge graph has maximum degree three.
The `(35,2)` and `(36,1)` degree-eight/degree-six stars therefore contain, at
the same centers, smooth-trace substars of degrees at least five and three.
Their explicit nonzero trace discriminants may be used as saturation factors
in the fixed-order candidate ideals. This strengthens the template-survivor
route but supplies no moment or survivor bound.
