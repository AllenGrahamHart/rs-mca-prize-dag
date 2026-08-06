
## Official first-checkpoint closure

The minimum coarse characteristic-width endpoint is now an exact finite
router. `l1_official_first_checkpoint_split_pencil_reduction` proves that
every `t=p` collision at `p<=d<=2p-2` consists of two complete fibers of
`Z^p+Q`, with `deg Q<=2p-d-1`; a ratio-set bound removes the final
`r_*(p,n)=floor((p(p-1)-1)/(n-1))` depths. For each surviving normalized
`Q`, `l1_official_split_pencil_value_capacity` recovers all split values as
one squarefree remainder gcd of degree at most `floor(n/p)<=23`.

The arithmetic atlas contains exactly 59 official `(n,p)` checkpoint pairs.
All 33 rows with `floor(n/p)=1` are empty. Of the ten rows with
`floor(n/p)=2`, six are empty and four have exactly `n/2` antipodal pairs.
For the 16 rows of multiplicity at least three, the complement census makes
the maximal split-value degree empty at every depth. Frobenius closure of the
balanced signed Fourier word then removes all seven rows with remainder
`n-p floor(n/p)>16` entirely. The only unresolved minimum-width rows are the
nine Mersenne-shape tuples

```text
n=m(p+1),       m in {4,8,16},       2<=deg G_Q<=m-1.
```

`l1_mersenne_checkpoint_cyclotomic_normal_form` now describes the full
residual Fourier closure. Writing `N=p+1` and every frequency as `qN+b`, its
membership is decided by two residue classes modulo `gcd(2b,m)`. In
particular all `N` frequencies `0,...,N-1` vanish, so the signed collision
word belongs to an explicit BCH-type low-weight window
`N+1<=weight=2N-2<2(N+1)`. The nonofficial `(32,7,4)` analogue exhausts all
seven-subsets and has 16 `h=2` pencils but no `h>=3` pencil; this is evidence,
not an official-row exclusion.

The observed two-fiber family is now proved uniformly.
`l1_mersenne_checkpoint_embedded_m2_family` partitions every surviving
domain into `m/2` cosets of order `2(p+1)` and embeds the exact antipodal
`m=2` construction in each. This gives exactly `n/2` explicit unordered
pairs at depths `p,p+1`. It is a necessary polynomial payload, not an
exhaustive classification of `h=2`; the exclusion frontier is `h>=3` plus
any nonembedded two-fiber records. The embedded inner polynomial is odd, so
its split values come in nonzero sign pairs. Together with maximal-degree
emptiness, this makes every embedded `m=4` pencil exactly `h=2`; the
`m=4,h=3` branch is wholly nonembedded.

That cubic branch is now exactly re-encoded by
`l1_m4_h3_colored_cyclic_equivalence`. Since every official `m=4`
characteristic is `1 mod 3`, color the three fibers by
`1,omega,omega^2`. Both the colored word and its coefficientwise square must
lie in the explicit Mersenne cyclic code, and this condition is also
sufficient. Its coefficientwise cube is the union indicator with exactly
`p+4` zero positions. The remaining theorem is emptiness or a row-sharp
component bound for this two-Schur section, not a generic `Q` enumeration.

The first analytic component compression is now proved in
`l1_m4_h3_mason_defect_budget`. Writing the depressed factorization as
`(R^3+aR+b)D=X^n-alpha`, one necessarily has `a!=0` and
`nu=ord_0(R) in {0,1,2,3,4}`. The radical deficits of `UD` and of the second
reduced Mason summand total at most `4-nu`. The Wronskian also gives the
explicit nonzero eliminant
`3XU'D+XUD'-(n-3nu)UD` of degree at most `4-nu`, and the full defect factor
divides it. The Cartier refinement
`l1_m4_h3_cartier_resonance_reduction` excludes `nu=4` and lowers the
remaining eliminant degrees to `3,2,1,0` for `nu=0,1,2,3`. Thus all
exceptional roots lie among at most three points and the cubic branch is a
finite low-defect classification problem, not an unrestricted cyclic-code
search. The companion `l1_m4_h3_euler_quotient_factorization` proves
`D(2aR+3b)(nu U+XU')=Hg(R)-4alpha U`, pins `H(0)!=0`, and makes the Euler
derivative degree exactly `p+deg(H)-4`. Evaluating its tangent factor gives
`l1_m4_h3_tangent_radical_exclusion`: `nu=3` is empty and positive valuation
is reduced to `(nu,deg H)=(1,2),(2,1)`. In the second stratum, the tangent
radical is an exact cubic and its multiplicity factor is `nu U+XU'`. The
four `nu=0` eliminant degrees remain separate.

The positive branch is now empty. The exact value-coset certificate first
excluded it for `p=8191,131071` and reduced the two larger characteristics
to `a^3+8b^2=0`. In the `(nu,deg H)=(2,1)` stratum, the intermediate Belyi
normal form and fixed-point certificate produced a scalar-free divisibility
test. The stronger local theorem
`l1_m4_h3_positive_tangent_multiplicity_exclusion` supersedes that search on
both `(1,2)` and `(2,1)`: every repeated tangent multiplicity `e` is the
local order of the cubic `X^nu H-kappa`, and at most three tangent roots
would again force `p<=9`. The Belyi artifacts remain valid conformance
reductions, but their parent stratum is theorem-empty. Before the final
zero-`b` exclusion below, the row split is:

```text
p=8191,131071:               empty;
p=524287,2147483647:         nu=0,b=0 with deg H in {0,1,2,3} only.
```

Every `nu=0` stratum now has a canonical three-scalar Frobenius kernel:
after multiplying by `X^(p-4)`, the reduced triple splits through one sparse
cubic `Q=q_3X^3+q_2X^2+q_1X`. On the `b!=0` arm, tangent localization
excludes `deg H=1,2`; `deg H=0` has one exact scalar relation, while
`deg H=3` has only two or three tangent roots. After the packet exclusion
and tangent-multiplicity exclusions below, no nonzero-`b` endpoint remains.
Thus the live `nu=0` split consists only of the four `b=0` degrees at
`p=524287,2147483647`. They obey
`a^2+3aR(0)^2+R(0)^4=0`. All share the cubic kernel. The zero-`b` arm is
exactly empty at `p=8191,131071` by its 16-case value-coset certificate.

The nonzero-`b`, `deg H=0` endpoint is now projectively finite. Factoring its
zero-point scalar equation and comparing local orders removes the component
`2aR(0)+3b=0`. The remaining component satisfies
`9bR(0)=4a^2+6aR(0)^2`. Intersecting its shifted fiber-product ratios with
all 16 Frobenius quarter pairs gives the complete necessary table

```text
p=8191,131071,524287:       (a/R(0)^2,b/R(0)^3)=(6,20);
p=2147483647:               (6,20), or
                             (844833809,2002167159).
```

The universal packet `(6,20)` is then excluded without computation. Its Euler
identity makes

```text
X^n(R-4R(0))/(D(R-R(0))^4)
```

a `p`th power, but the resulting root multiplicities cannot sum to degree
`p`. Hence the nonzero-`b`, `deg H=0` endpoint is empty for
`p=8191,131071,524287`; only the exceptional packet on `p=2147483647`
remains a necessary possibility.

Finally, exact local degree accounting proves that the squarefree complement
of any exceptional lift would be precisely the radicals of the two auxiliary
fibers `R-R(0)` and `R-(2A/3)R(0)`. Their root products force the normalized
shifted cubic to divide `W^(4(p+1))-1`. For the exceptional packet, the exact
remainder is the nonzero constant `876663072`. It is therefore impossible as
well, and the entire nonzero-`b`, `deg H=0` endpoint is empty on all four
characteristics.

The cubic nonzero-`b` endpoint is empty as well.
`l1_m4_h3_nu0_h3_tangent_multiplicity_exclusion` applies the Euler quotient
identity locally at a tangent root of multiplicity `e`. The rational map
`4 alpha Y/g(Y)` has nonzero derivative at the tangent value, while the
Euler correction has order at least `2e-1`; hence every repeated tangent
root forces `ord(H-kappa)=e`. The tangent fiber has only two or three roots
and `H-kappa` is cubic, which would give `p<=9`. This contradicts every
official characteristic. Consequently the complete `nu=0,b!=0` branch is
now closed, and the two `m=4` rows with characteristics `8191` and `131071`
are empty in full.

The zero-`b` residue on the two larger characteristics is also impossible.
`l1_m4_h3_nu0_zero_b_euler_exclusion` cancels `R` from the Euler quotient
identity. On all `p` roots of the complete split fiber `R=0`, comparison
with the derivative of the domain identity forces `H=12 alpha/a`.
Evaluation at zero then gives `a/R(0)^2=-3/2`, contradicting the proved
zero-`b` invariant unless the characteristic is five. Thus the complete
official `m=4,h=3` branch is empty on all four rows.
`l1_m4_h3_official_emptiness` records the exhaustive aggregate theorem and
its complete dependency subgraph as one green node.

The complete scalar-free conformance censuses at `p=7,31,127` leave zero
divisibility witnesses; at `p=31,127` the sign gate first reduces `65,1281`
triples to `3,19`. This is useful evidence and compiler calibration, not an
official exclusion.

This closes `m=4,h=3`, not the full first-checkpoint endpoint. The exact
residual is nonembedded `m=4,h=2`, the `m=8` rows with `2<=h<=7`, and the
single `m=16` row with `2<=h<=15`, after prepaying every embedded antipodal
pair.

At the two next-to-maximal degrees, consume
`l1_mersenne_next_to_maximal_exceptional_reduction`. For `m=8,h=7` and
`m=16,h=15`, every generic tangent branch and both possible binomial outer
forms are empty. A survivor must have `nu=0`, a nonzero constant Euler
eliminant `H=q`, and `qG(y)=m alpha y` at every nonzero root of
`T=hG-YG'`; those tangent values are simple and every `R-y` is squarefree
and disjoint from the complement. Degree comparison further forces
`deg T=h-2`, `deg(XR')=p-m`, and the printed leading-scalar relation. This
also leaves only `ord_0(T) in {0,1}` and a quadratic quotient of
`G-(m alpha/q)Y` containing `R(0)`. The two quotient fibers exactly exhaust
the complement and ramification ledgers. This is a strict reduction, not an
emptiness theorem. Equivalently, the residue is a degree-`p` polynomial
Belyi map with critical values `0,1` and both fibers supported on the
official domain, so the endpoint degrees remain in the residual.

The shifted-value gate
`l1_mersenne_next_to_maximal_belyi_shifted_value_gate` further proves that
the monic degree-`h` polynomial whose roots are
`(beta_i-R(0))/(z-R(0))` divides `W^n-1`. If `z!=0`, no passport survives
when both projective invariants `z/R(0)` and
`2[Y^(h-2)]G/(R(0)z)` lie in `F_p`; a rational `p`th-power valuation ledger
would force an impossible uniform multiplicity. Thus the exact endpoint
residue is genuinely non-prime-field normalized; the `z=0` chamber is also
empty by a direct local-order contradiction.
The same gate pins `W(W-1)P'` to one constant at every nonzero root of the
shifted polynomial. In the zero-free outer chamber this is an exact linear-
quotient differential equation for `P`, leaving a one-parameter degree-`h`
cyclotomic problem rather than a free coefficient search.

The coefficient-level successor
`l1_mersenne_next_to_maximal_hypergeometric_normal_form` makes that reduction
explicit. In the zero-free chamber,

```text
P_s(W)=sum_(r=0)^h binom(s+r-1,r)W^(h-r),
s=h/(z/R(0)-1) notin F_p,
```

and survival is exactly `P_s | W^n-1`. In the order-one chamber, all outer
coefficients are generated from `(A,c)` by one top-down recurrence, its last
equation is the hypergeometric curve
`[t^h](1-t)^(c rho)(1-ct)^(-rho)=0`, and the known zero split value
forces `(c-1)^n=1`. Thus the remaining next-to-maximal outer classification
is low-dimensional, but neither intersection is yet proved empty and no
inner degree-`p` lift is supplied.

The order-zero Frobenius successor
`l1_mersenne_hnf_frobenius_reciprocal_gate` takes
`Q_s(Z)=Res_W(P_s(W),Z-W^m)`. Since every `m`th-power root has norm one to
`F_p`, every survivor obeys

```text
Q_s(0)Q_(s^p)(Z)=Z^hQ_s(1/Z).
```

Introducing `t=s^p` gives a bounded-degree two-variable coefficient system
depending only on `m,h`, with `t!=s`. An exact unit saturation by `t-s`
would close the whole order-zero chamber. The identity is only necessary,
so retained components still require the original cyclotomic and inner
tests.

The order-one successor
`l1_mersenne_hnf_order_one_frobenius_gate` discretizes the remaining large
Frobenius image. With `d=c-1`, every survivor has

```text
zeta=d^(p+1) in mu_m,       c^p=1+zeta/d.
```

For each of these `m` torsion chambers, the Frobenius transform of the
hypergeometric curve and a reciprocal resultant identity form a
bounded-degree system in `(rho,rho^p,c,zeta)`. The known zero split value
contributes an automatic factor, which is cancelled before saturation; the
resultant system therefore has degree `h-1`, not `h`. A unit saturation by
the printed nonzero factors closes the order-one chamber before a
degree-`n` remainder. Again, retained components are necessary candidates
only.

The order-zero colored classification has one further exact deletion.
`l1_mersenne_hnf_order_zero_linear_color_exclusion` proves that its
interpolant cannot have degree one. A linear color map would send the
`h=m-1` roots injectively onto all but one member of `mu_m`, making `P_s` an
affine image of a punctured cyclotomic polynomial. Its first three
coefficients force `s=1` or `s=-m`, contradicting `s notin F_p`. Combined
with the same theorem's constant case, the live order-zero color degrees
begin at two. No higher degree or endpoint is closed.

At the first live degree,
`l1_mersenne_hnf_order_zero_quadratic_collision_router` controls repeated
colors. Two repeated colors force the quadratic collision center to zero;
otherwise Frobenius would be an affine identity or reflection, and both are
excluded. On all four `m=8,h=7` rows, two antipodal pairs are also impossible,
so seven locator roots use at least six distinct colors. On the
`m=16,h=15` row, a quadratic with multiple repeats must be even. The
collision-free, single-collision, and `m=16` even chambers remain open.

The collision-free option is now removed by
`l1_mersenne_hnf_order_zero_quadratic_collisionfree_exclusion`. Pairing each
root with its quadratic reflection produces a degree-`h` polynomial in
`U=W(W-S)`. Its first three coefficients are
`binom(s+r-1,r)(1-S)^r`, so an injective color map is the already impossible
punctured-cyclotomic linear template. Consequently the exact live quadratic
frontier is: exactly one repeated color for `m=8`; exactly one repeated color
or an even multi-repeat for `m=16`. Neither retained system is classified.

The `m=8` retained system is now empty by
`l1_mersenne_hnf_m8_order_zero_quadratic_exclusion`. After normalizing its
unique double color, the two omitted colors give 21 patterns. Three centered
moments place `s` on one explicit quadratic per pattern, while
`P_s|W^n-1` forces `binom(s+6,7)^n=1`. Exact coprimality in
`F_p(mu_8)[s]`, independently replayed as 84 nonzero resultants, excludes
every pattern on all four official rows. Thus the live `m=8` order-zero
color degree begins at three. The `m=16` exactly-one-repeat and even
multi-repeat quadratic systems remain unclassified.

The exactly-one-repeat `m=16` system is now also empty by
`l1_mersenne_hnf_m16_order_zero_single_collision_exclusion`. Its 105
normalized pairs of omitted sixteenth-root colors obey the same
centered-moment equation, and every resulting quadratic is coprime to
`binom(s+14,15)^131072-1` over `F_8191(mu_16)`. Therefore the sole live
quadratic color system across all five endpoint rows is the even `m=16`
multi-repeat chamber, with at least two antipodal repeated-color pairs.

That last quadratic system is empty by
`l1_mersenne_hnf_m16_order_zero_even_quadratic_exclusion`. Writing
`P_s(W)=W O_s(W^2)+V_s(W^2)`, two antipodal pairs would force
`deg gcd(O_s,V_s)>=2`. The two coefficients of the first subresultant can
vanish together only when
`s in {0,1,2,3,-1,-2,...,-11} subset F_8191`, contradicting the HNF
condition `s notin F_p`. Constant, linear, and quadratic colored Frobenius
degrees are now empty on all five endpoint rows; the live order-zero degree
starts at three.

The degree split is no longer needed on the four `m=8,h=7` rows.
`l1_mersenne_hnf_m8_order_zero_reciprocal_elimination` uses the first three
coefficient equations of the bounded reciprocal gate. Two eliminants of
degrees 1320 and 1760 have degree-1032 gcd

```text
s^176(s-1)^4(s+1)^176(s+2)^168(s+3)^162
(s+4)^152(s+5)^128(s+6)^64(s+7)^2,
```

so every common solution has `s in F_p`, a contradiction. The complete
order-zero outer chamber is therefore empty on all four `m=8` rows,
including every color degree.

The remaining order-zero endpoint is now also empty.
`l1_mersenne_hnf_m16_order_zero_reciprocal_elimination` applies the same
first three reciprocal equations at `(m,h,p)=(16,15,8191)`. Its two exact
eliminants have degrees `11472` and `15296`; their degree-`9912` gcd has
squarefree radical

```text
s(s-1) product_(j=1)^15(s+j).
```

Every common solution therefore has `s in F_8191`, contradicting the HNF
condition. Thus all five official next-to-maximal order-zero outer chambers
are closed. The first-checkpoint endpoint still retains order one, lower
value degrees, nonembedded `m=4,h=2`, inner lifts, and the global payment.

The order-one hypergeometric curve has also been narrowed exactly.
`l1_mersenne_hnf_order_one_involution_component_exclusion` factors
`h!*Phi_h` by `rho*c*(c-1)*(c+1)`. The first three factors are already
saturated, and the complete `c=-1` component is impossible by the official
torsion equation. Thus order-one work starts on `Psi_7=0` of bidegree
`(2,4)` and `Psi_15=0` of bidegree `(6,12)`, not on the unreduced curve.
These two residual curves remain open.

The reciprocal equations on those curves no longer require a generic
`m`th-power resultant. The proved
`l1_mersenne_hnf_order_one_newton_reciprocal_reduction` identifies them
exactly with Newton equalities between the star-root and inverse-root power
sums. The first three necessary equations use powers `8,16,24` at `m=8`
and `16,32,48` at `m=16`. Their parameter elimination remains open.

These theorems concern only the `t=p` first-checkpoint endpoint. They do not
pay wider exchanges, the primitive coprime split-pencil census, or the full
L1 exact shell, so this node remains TARGET.
