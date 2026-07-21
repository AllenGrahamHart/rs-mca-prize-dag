# Provenance snapshot (2026-07-21): statement.md immediately before the
# w18-C1 DSP8 parity supersession, maintainer-ratified this date.
# Preserved per custody #104 (merge-not-replace). The parity package
# strictly sharpens the constants; see WAVE18_AUDIT_FINDINGS.md.

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

PROVED JOINT-STAR / QUOTIENT-DEPTH PARETO COMPILER: using disjoint
distance-six edges directly gives six independently sufficient moment routes
on the rectangles

```text
(P,R)>=(25,12),(27,10),(29,8),(31,6),(33,4),(35,2).
```

Their product packets strengthen from a degree-two free star to
degree-eight/six class-sensitive stars, while the anchored quotient packet
shrinks from eleven spokes to one. In particular, the coordinate-minimal last
corner is

```text
Dbar_16^0+(29/22)Dbar_16^A <=(319/153)n^2,
Dbar_16^c=sum_(t in class c,P(t)>=35)
                 N_6^disj(t)(R(t)-1)_+.
```

Every survivor there has a degree-eight or degree-six pure product star and a
two-lift quotient packet, odd-locally equivalent to one nonzero coupling
anchor plus one quotient-collision spoke. This is an alternative sufficient
route to C36', not a proof of the displayed inequality or of `(DSP8)` itself.
