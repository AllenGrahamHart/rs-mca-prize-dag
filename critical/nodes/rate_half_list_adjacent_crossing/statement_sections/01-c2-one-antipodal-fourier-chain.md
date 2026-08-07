
## WAVE-32 ADDENDUM (2026-07-20; one-antipodal canonical-cell Fourier ladder)

After the secondary gap and canonical-span gates, the one-antipodal `c=2`
branch has a second exact attack surface. Put `R=2^37`, `H=R+1`, and
`r=2R-1`. The punctured subgroup quotient factors as

```text
Q=(1-z^(2^40))/E=product_(i=1)^4(B+w_i z^H C),
mu_(2^40)\{1,-1,c,d}=A_1 disjoint_union ... disjoint_union A_4,
|A_i|=r.
```

The four canonical cells have an exact flat Fourier prefix through degree
`H-1`. More generally, weights orthogonal to `1,w,...,w^s` annihilate cell
moments below `(s+1)H` for `s=0,1,2`. Under negation, a nonzero weighted
coloring in the `s=1` kernel changes on at least `2H+2=2R+4` points, while
the `s=2` kernel changes on at least `3H+1=3R+4`; the alternative is exact
negation invariance. These are proved Vandermonde bounds. Classification of
the invariant and large-mismatch colorings, with the outer Mobius match
retained, remains open.

## WAVE-33 ADDENDUM (2026-07-20; barycentric negation syndrome)

The invariant alternative is impossible in one canonical direction. For

```text
Phi(W)=product_i(W-w_i),       lambda_i=1/Phi'(w_i),
```

the weighted cell coloring minus its negation has exactly `3H` initial zero
Fourier moments and first syndrome `-2H` at degree `3H`. Consequently its
support is unconditionally at least `3H+1=3R+4`. If equality holds, the
support polynomial `Psi` is even and the coloring values are exactly
`-2H/Psi'(a)` at its roots. The remaining task is to exclude or classify
these derivative-weighted supports together with the outer Mobius match.

## WAVE-34 ADDENDUM (2026-07-20; barycentric support-polynomial compiler)

The barycentric mismatch no longer requires explicit root cells. Define

```text
Theta=HBC+z(BC'-B'C),
J=(1-Sz+Pz^2)C(z)^2Theta(z)
  +(1+Sz+Pz^2)C(-z)^2Theta(-z).
```

Then `J` is even of degree at most `5H-11`, and the pointwise mismatch at
`x in mu_(2^40)` is a fixed nonzero scalar multiple of
`x^(-3H)(1-x^(-2))J(x^(-1))`. Minimum support `3H+1` is therefore
equivalent to `J` having full degree, dividing
`(z^(2^40)-1)/(z^2-1)`, and avoiding `+/-1`. The split-divisor gate and all
larger-support cases remain open.

## WAVE-35 ADDENDUM (2026-07-21; minimum-support barycentric collision router)

The generic outer quartic is now excluded from the minimum-support branch.
If `lambda_i=1/Phi'(w_i)` are all distinct, every one of the `5H-11`
split-divisor roots forces the odd-degree rational map `-B/(z^H C)` to
agree with its negation.  The resulting numerator has degree at most
`4H-7`, so the map would factor through `z^2` and have even degree, a
contradiction.  Hence two barycentric weights coincide.  This forces

```text
(4gamma-alpha^2)^3=8alpha^3 beta^2.
```

Triple collisions are impossible because they force `alpha=0`, whereas the
primary gap gives `alpha=4c!=0`; two-pair and fourfold collisions are also
impossible.  Thus exactly one pair collides.  With `y=s^2/alpha` for its
root-sum parameter, the remaining completion coupling is

```text
32z_t(z_t-36)^2
 =(3y-4)^2(3y+2)(z_t+12)^3.
```

The exact one-pair collision locus and all larger-support cases remain open.
They are recorded as scoped contributor requests rather than authorized
local Modal runs.

## WAVE-36 ADDENDUM (2026-07-21; minimum-support collision branch compiler)

The normalized one-pair curve factors without an official-order expansion.
Writing `z=z_t`, every minimum-support survivor lies in the union

```text
L: y(z+12)=2z-8,
Q: [y(z+12)-16]^2=64z.
```

The branches meet only at `(y,z)=(0,4),(4/3,36)`; a disjoint census assigns
those two points to `L` and uses `Q=0,L!=0` for the other shard.

The selected denominator roots are squares.  Thus `z=x^2` for a base-field
trace `x=rho+rho^(-1)`, and the two apparent signs on `Q` are exchanged by
`rho -> -rho`.  Both outer quadratics split exactly when the one scalar

```text
-2alpha/(z+12)
```

is a nonzero square.  The value `z=-12` is impossible.  If the selected pair
is the unique antipodal pair, then `z=0` forces

```text
y=4/3,       12gamma=11alpha^2,
27beta^2=64alpha^3,       J=0.
```

The two constant-degree branches still need to be combined with the
coefficient gaps and support divisor; no Modal run is authorized.

## WAVE-37 ADDENDUM (2026-07-21; minimum-support Euler divisor gate)

There is now an outer-coefficient-free test before the `L/Q` split. Define

```text
T=NEB-z(E'B+4EB'),       P=TB^3-N.
```

Every complete canonical packet has `V=z^H C` dividing `P`. The primary
double gap supplies the stronger automatic factor `z^(2H)`, so the actual
remainder has a derivative-free form. With `c_0=a_(2H)` and
`b_0=a_(2H-3)`, put

```text
T_0=(H-1)EB+Hc_0z^(2H)-(H-1)E_4b_0z^(2H+1).
```

Then the actual condition is

```text
C divides z^(-2H)(T_0B^3-(H-1)).
```

At minimum barycentric support, full support-polynomial degree forces
`deg C=H-3=2^37-2`. Resultant multiplicativity then gives

```text
Res(C_sharp,T_0)Res(C_sharp,B)^3=(H-1)^(H-3),
```

where `C_sharp=C/lc(C)` is monic. Thus `Res(C_sharp,T_0)` is a nonzero
base-field cube. This gate uses only `E,B,C` and must be applied before any
collision-branch search. Its official-degree evaluation remains open and is
not authorized locally.

## WAVE-38 ADDENDUM (2026-07-21; minimum-support endpoint torsion gate)

The split-divisor endpoint now supplies a scalar torsion test. Write

```text
m=H-3,       r=2H-3,
Delta_inf=b_(r-1)c_m-b_rc_(m-1),
Xi=H/(P c_m^2 Delta_inf).
```

Minimum support forces `Delta_inf!=0`. The support compiler polynomial has
constant coefficient `2H` and leading coefficient
`2P c_m^2 Delta_inf`, so `Xi` is the product of all its roots. The polynomial
is even and its roots are distinct elements of `mu_N`; each negation-pair
product is a square in `mu_N`. Therefore

```text
Xi^(N/2)=1,       N/2=2^39.
```

This constant-size test uses only the complementary source product and four
top canonical coefficients. It must precede any full split-divisor or `L/Q`
search. No official coefficient evaluation or torsion sweep is authorized.

## WAVE-39 ADDENDUM (2026-07-21; minimum-support infinity-cell torsion gate)

Minimum support also exposes a constant-degree torsion packet at infinity.
Put `b=[z^(2H-3)]B`, `c=[z^(H-3)]C`, and

```text
ell_i=b+cw_i,
O_inf(X)=product_i(X-ell_i)
        =(X-b)^4+alpha c^2(X-b)^2
          +beta c^3(X-b)+gamma c^4.
```

The split canonical cells prove that the four distinct `ell_i` lie in
`mu_N`, their product is the inverse complementary-source product, and
`O_inf` divides `X^N-1`. Thus forty squarings modulo this quartic must send
`X` to `1`. Moreover

```text
O_inf'(ell_i)=c^3 Phi'(w_i),
```

so the unique derivative-weight collision persists at infinity. On the
selected-antipodal shard, the centered infinity quartic also has `J_inf=0`.
This is a mandatory constant-degree prefilter, not an exclusion or a claim
that every such subgroup quartet is antipodal.

## WAVE-40 ADDENDUM (2026-07-21; selected-antipodal affine intersection)

The fixed selected-antipodal infinity quartet has a one-variable normal
form. Choose `q^2=-alpha/6`, put `a=s/(2q)`, and define

```text
tau=ell_4,       y=ell_3/ell_4,       a^2=-2,
A_a(y)=(a+2)y-(a+1),
B_a(y)=(a-1)y+(2-a).
```

Then `y!=1` and the four infinity roots, divided by `tau`, are exactly

```text
A_a(y), B_a(y), y, 1.
```

Thus this shard requires `tau,y,A_a(y),B_a(y) in mu_N` and

```text
tau^4 y A_a(y)B_a(y)=P_src^(-1).
```

Eliminating the scale gives the sharper scalar condition

```text
Z_inf=P_src y A_a(y)B_a(y)=tau^(-4),
Z_inf^(N/4)=1,       N/4=2^38.
```

The choice `q -> -q` induces
`(a,y,tau)->(-a,y^(-1),tau y)`, merely swapping roots within the two pairs.
This reduces the infinity classification to three affine subgroup tests in
one variable plus one fixed scale; it does not assert that the intersection
is empty or that a passing infinity packet extends canonically.

## WAVE-41 ADDENDUM (2026-07-21; selected-antipodal affine Stepanov cap)

The one-variable affine packet has a rigorous all-field candidate cap. For

```text
mathcal Y_a={y in mu_N:A_a(y),B_a(y) in mu_N},
```

the in-house Stepanov construction, specialized at

```text
A_0=D_0=79896510,       B_0=12902,
A_0+NB_0=14185899101462462,
```

proves

```text
#mathcal Y_a<=355106851<2^29.
```

This covers prime and quadratic official fields. The sparse nonvanishing
argument needs only `A_0+NB_0<p`; the maximal-row field theorem gives the
uniform bound `p>=31950697969885030204`. The result is a candidate cap before
the quarter-order, scale, gap, and source gates. It is not an emptiness
theorem or authorization for exhaustive local or unpriced remote search.

## WAVE-42 ADDENDUM (2026-07-21; collision-or-high-support router)

The one-pair geometry is no longer confined to exact minimum support. If all
four barycentric weights are distinct, every ordinary mismatch zero is a
root of

```text
D(z)=B(z)V(-z)-B(-z)V(z),       deg D<=4H-7.
```

This polynomial is nonzero because `-B/V` has exact odd degree `2H-3` and
cannot factor through `z^2`. The ordinary zero set is negation-stable, so its
even size is at most `4H-8`. Including the two automatic zeros `+/-1` gives

```text
|supp u|>=4H-2.
```

If the weights are not distinct, the barycentric moment identities and
`alpha!=0` exclude triple, two-pair, and fourfold collisions without using
support minimality. Exactly one pair is equal, and the packet obeys the same
`L/Q` equations, square-class gate, and selected-antipodal specialization as
the former equality branch. Hence every packet with
`|supp u|<=4H-4` lies on `L/Q`. The remaining generic outer geometry is now
a quantified high-support branch; neither side is yet excluded or paid.

## WAVE-43 ADDENDUM (2026-07-21; degree-defect global gate router)

Canonical degree and support defect are now separated. Put

```text
e=H-3-deg C,       epsilon_e=1_(e even),
d_e=5H-10-3e-epsilon_e.
```

If `r_J` counts the ordinary subgroup roots of the even support polynomial
and `eta=d_e-r_J`, then `eta` is a nonnegative even integer and

```text
|supp u|=3H+3e+epsilon_e+eta.
```

Thus the first degree floors are `3H+1`, `3H+3`, and `3H+7` for
`e=0,1,2`. More importantly, `e=0` is the actual hypothesis needed for the
Euler and infinity-cell calculations. At every support in that branch,
`C` passes the derivative-free Euler remainder and cube-resultant gate, and
the four top cell coefficients form a subgroup quartet dividing `X^N-1`.
On a collision packet its derivative weights have exactly one equal pair.

If the selected pair is antipodal, the same maximal-degree packet also has
the affine quartet

```text
tau*{(a+2)y-(a+1),(a-1)y+(2-a),y,1},       a^2=-2,
```

with the quarter-order product gate and the all-field cap `355106851<2^29`.
The support split-divisor and endpoint `Xi` tests remain equality-only. This
globalization narrows every maximal-degree collision packet but does not
exclude either the degree-deficient or maximal-degree branch.

## WAVE-44 ADDENDUM (2026-07-21; reciprocal affine collapse)

The selected-antipodal affine intersection is now exact in the reciprocal
quadratic-field chamber. For `q=p^2`, `p=-1 mod N`, Frobenius sends
`a -> -a` and every `N`-torsion value to its inverse. Hence the three affine
subgroup conditions force

```text
y=(7+4a)/9,
r=(2a-1)/3,
A_a(y)=r,       B_a(y)=-r,       y=-r^2.
```

They are equivalent to `r^N=1`, checked over `F_p` by forty squarings from

```text
R_0=-2/3,       R_(j+1)=R_j^2-2,       R_40=2.
```

The complete maximal-row interval contains exactly `4,495,442` progression
values `p=k*2^40-1` before primality. A registered 16-shard exact screen
covered every one, including composites, and found no terminal hit. Hence
the reciprocal maximal-degree selected-antipodal collision shard is empty.
The fixed-field, degree-deficient, and non-selected-antipodal shards remain
outside this exclusion.

---
