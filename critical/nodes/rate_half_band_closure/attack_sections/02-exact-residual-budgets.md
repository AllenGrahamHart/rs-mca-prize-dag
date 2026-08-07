
## Exact residual branches

Write `m=2^37`. The split-pencil and minimal-index theorems reduce `(K5-CA)`
to the following disjoint moving-kernel profiles.

### Strict budget `B=2^39=4m`

The locator radius is `r=4m-1`. Full-column-rank pencils and every deficient
profile with `A>=5` are proved. The residue is exactly

```text
A=3,       rho=r=4m-1,       s=0,
m<=e<=floor((4m-1)/3),       target T<=4m.
```

The first endpoint `e=m` can fail only at `T=4m+1`; it has the proved
rational-normal, norm-defect, component-chamber, and Hankel/apolar routers.
Those routers do not exclude it. For `e>m`, the slope-slack ledger writes

```text
T=4e+1-h,       0<=h<=4(e-m)
```

for every possible failure.

### Half-distance budget `B=2^39+1=4m+1`

The locator radius is `r=4m`. Profiles with `A>=5` are proved. The residue is
the union of

```text
A=3: rho=4m-1, s=0,
     m+1<=e<=floor((4m-1)/3), target T<=4m+1;

A=1: rho=4m, s in {0,1,2},
     m+1<=e<=floor((4m-s)/(1+s)), target T<=4m+1.
```

The `A=1,s=1,e=2m-1` sharp-cap face has the deepest current reduction. Its
distance-three branch is now closed by the PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_external_split_design_exclusion`:
the pair-crossing gate sends every exact design into the all-deficient
quartic-support branch, and the residual-discriminant theorem makes that
branch empty. The live `A=1` work is the high quotient-distance tail and the
other component faces. The strict and half-distance `A=3` profiles also
remain theorem work.

For the high quotient-distance tail, the PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_first_jet_transversality`
adds the first constraint not visible in the endpoint resultant matrix. At
every clean selected incidence `(gamma,y)`, with domain order `M=2^41` and
corrected-square exponent `N_sq=M+r-3`,

```text
F_t U W_vee=-P_cl' E y^N_sq,
dot y=-(P_cl'E/M)y^(r-2)(1-sy)(1-x_0y)/W_vee.
```

All factors are nonzero. Hence a live endpoint attack must classify the two
printed incidence profiles together with these prescribed first jets. A
resultant-multiplicity replay alone is route-incomplete.
The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_w_interpolation_normal_form`
then removes the global `W_vee` biform as a free object. Its clean-fiber
values determine one canonical `W_0` of parameter degree below
`deg P_cl`, and every survivor has

```text
W_vee=W_0+P_cl(t A_W+B_W),       deg A_W,deg B_W<=r-1.
```

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_unit_triangular_affine_reconstruction`
then eliminates both corrections. In ascending `Y`-degree, the unit equation
computes one canonical residue

```text
rho_k=-C_k^0(l_0P_cl)^(-1) mod f_0,       f_0=E q_bar.
```

Every survivor must have `deg rho_k<=1`; that affine representative uniquely
gives `(a_k,b_k)`, and exact division gives the next coefficient of `S`.
Thus a non-affine `rho_k` is an exact rejection certificate. A surviving
packet has a unique `W_vee` and must pass only the final exact-division,
degree-box, and Hankel checks. The next endpoint attack should classify those
deterministic checks; do not allocate a dense `W_vee` or correction
polynomials.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_unit_bezout_remainder_gate`
simplifies this further. Since `l_0P_cl+f_0a_minus=1`, write only

```text
C_k^0=f_0d_k+r_k,       deg r_k<e.
```

Then `rho_k=-r_k` and `s_k=d_k+a_minus r_k`. Therefore each stage is one
Euclidean division and survives exactly when `deg r_k<=1`; neither modular
inversion nor a second division should appear in a classifier.

There is now an independent clean-fiber check. The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_second_jet_hermite_gate`
differentiates the reversed first complement twice along every selected root.
It reconstructs `W_vee,t(gamma,Y)` on each clean fiber and normalizes it to

```text
D_gamma=(W_vee,t(gamma,Y)-W_0,t(gamma,Y))/P_cl'(gamma).
```

Every survivor must have `D_gamma=gamma A_W+B_W`. Any two slopes reconstruct
the pair, all other slopes must lie on the same affine line, and that pair
must equal the unit-remainder reconstruction. These are exact comparison
gates before the remaining Hankel checks.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_jet_quotient_ring_compiler`
makes both jet inputs root-free. In the quotient ring by `F(gamma,Y)`, all
needed denominators are units and the smooth-domain identity reduces
`Y^N_sq,Y^(N_sq-1)` to `Y^(r-3),Y^(r-4)`. Canonical modular representatives
are exactly `W_vee(gamma,Y)` and `W_vee,t(gamma,Y)`. This avoids selected-root
enumeration and huge exponents, but it does not authorize dense official
degree-`r` arrays; any scale-up needs compressed locator arithmetic.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_unit_resultant_log_trace_gate`
extracts an earlier scalar check from the same data. If
`q_0=[X^0]Q=[Y^r]F`, then every clean slope must satisfy

```text
Tr((W_vee,t+W_vee,Y dot y)/W_vee)
 =(N_sq+1)E'/E+N_sq q_bar'/q_bar-(r-1)q_0'/q_0.
```

The actual `X`-degree of `W` cancels. A trace mismatch rejects before the
full affine-Hermite comparison or any Hankel work.

The remaining Hankel constraints are now compressed by the PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_coefficient_biisotropic_plane`.
If `q(z)=sum_(i=0)^e z^i q_i`, then the `q_i` are independent and their
span has dimension `e+1`, with

```text
q_i^T M_0 q_j=q_i^T M_1 q_j=0       for all i,j.
```

This common isotropic plane meets `ker M_0` only in the exceptional locator
line and `ker M_1` only in the top coefficient line. The next endpoint proof
should classify this plane jointly with the trace/Hermite gates; it should
not allocate separate quadratic moment equations.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_coefficient_rank_one_flag`
adds `v=Xq_0` and identifies

```text
H_q=W_q+span{v}=W_q^(perp M_0)=W_q^(perp M_1).
```

On this `(e+2)`-plane, `M_0` is zero and `M_1` has rank one, with its only
nonzero Gram entry `v^TM_1v`. Thus the regular Kronecker line is already in
the original coefficient coordinates and must not be reintroduced as a
solver block.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_exceptional_self_dual_evaluation_code`
passes this flag to the exceptional roots. Evaluation kills exactly
`span{q_0,Xq_0}` and produces an `e`-dimensional code of length `2e` that is
self-dual under the nonzero exceptional weights. Its bases occur in
complementary pairs, with the exact weighted minor law

```text
Delta_J^2 product_J beta=(-1)^e Delta_I^2 product_I beta.
```

This is the current discrete Hankel interface for classifying the two
high-distance endpoint profiles.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_exceptional_split_incidence_self_dual_frame`
makes that interface explicit. Each exceptional column is the coefficient
vector of `g_a(z)=Q(z;a)/z`, a split degree-`e-1` polynomial whose roots are
its ordinary incidences. The `2e` columns form a weighted self-dual frame on
the `4e` clean slopes with exactly the flat or swapped replication ledger.
An exact `e=3,F_101` flat frame with six disjoint root pairs and nonzero
self-dual weights survives. Therefore the frame axioms alone are fenced;
the next exclusion must use official Forney values, smooth-domain placement,
or genuinely large-`e` structure.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_residue_self_dual_algebra`
now installs the Forney values. Normalize each `g_a` by its nonzero constant
`q_1(a)` and work in `R_A=F[X]/(A)`. The normalized coefficient space `U_q`
has dimension `e`, contains `1`, and is self-dual for the residue pairing
represented by

```text
C=q_1 Phi/B_T mod A.
```

Its product span satisfies `dim U_q^2<=2e-1`. At equality, the frame
determines `C` up to scalar and must match the Forney class; lower dimension
is a separate degeneracy branch. This product-space dichotomy is the current
Hankel endpoint target.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_mds_schur_router`
sharpens that split. If the normalized exceptional code is MDS, its Schur
square has dimension exactly `2e-1`, so the frame uniquely determines the
Forney class up to scalar. Otherwise there is an `e`-set of exceptional
columns and its complement whose two determinants both vanish. The next
proof should compare the unique class on the MDS branch, or exploit the
paired split-polynomial dependence on the non-MDS branch.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_mds_half_dimension_non_grs_route_fence`
blocks a tempting overpromotion of the first branch. An exact `[8,4,5]`
Euclidean self-dual code over `F_11` has square dimension seven but is not
GRS, certified by the absence of linear syzygies among its three quadrics.
This is exactly the `n=2k` exception to ordinary Schur-square rigidity. The
official MDS branch must therefore use its split-incidence columns, Forney
normal, or smooth-domain placement; abstract MDS plus self-duality plus
minimal square does not yield a rational-normal curve.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_non_mds_annihilating_pair_router`
replaces the complementary-minor description on the other branch by a
quotient-algebra target. Non-MDS yields independent nonzero `u,v in U_q`
and complementary exceptional halves `I,J` with `u|_I=0`, `v|_J=0`, hence
`uv=0 mod A`. The next non-MDS proof should exclude this annihilating pair
using the official split coefficients or Forney residue form; it should not
enumerate the `binom(2e,e)` maximal minors. Canonical gcds give a sharper
dichotomy: either one element has at least `e+1` exceptional zeros, or
`A=D_uD_v` is an exact factorization into complementary degree-`e` zero
locators. These are the two non-MDS subbranches to exclude. Because `q_1`
is a unit, each `D` is the gcd of `A` with a direct linear combination of
`q_1,...,q_e`; no quotient-ring inverse is part of the certificate. If the
two half-restrictions have deficiency `d`, weighted self-duality makes the
deficiencies equal and supplies `d`-dimensional annihilator spaces on both
halves, with `d<=floor(e/2)`.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_non_mds_support_residue_gate`
adds the first support-side obstruction to either subbranch. Put
`K=H_lambda H_nu/A`. Hankel `M_1` isotropy and the Forney support weights
force

```text
[X^(h-1)] rem_(B_T)(Phi K A^(-1))=0.
```

In the exact-half branch `K=R_uR_v`; the excess branch retains its overlap
factor. Any nonzero top coefficient rejects the annihilator pair before
further Hankel reconstruction. Equivalently, a global-residue transfer gives

```text
sum_(A(a)=0) beta_a q_1(a)K(a)
 =0                         if deg K<=2e+1,
 =Theta_2 lc(K)             if deg K=2e+2.
```

This alternate form avoids reduction modulo the huge support locator when
the exceptional/source representation is the compressed side available.
For deficiency `d`, both forms hold entrywise for the full `d`-by-`d` matrix
of cross annihilators; a checker must not discard these extra equations.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_norm_discriminant_square_gate`
adds a router-independent scalar obstruction. Both branches must satisfy

```text
Res(A,q_1) Res(A,Phi)
---------------------  in (F_field^x)^2.
 Res(A,B_T) Disc(A)
```

Thus a nonsquare candidate is rejected before MDS classification or minor
enumeration. However, the PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_norm_square_cancellation_fence`
shows that after the full Forney/self-dual packet is imposed this expression
is exactly

```text
(-1)^e Norm_A(Beta) Res(A,q_1)^2,
```

and the first factor is already square by weighted self-duality. Directly
computing this quantity from a complete packet is therefore an audit, not a
new endpoint attack. It can exclude a profile only through an independent
profile-level formula that forces the opposite class.

The PROVED
`rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_endpoint_derivative_resultant_reciprocity`
already performs the first such extraction. In the flat profile it gives

```text
Res(A,q_1)/Res(A,q_e)=P_ord(0)^k_0,
```

and the swapped profile adds the factor `z_min/z_max`. Since the official
`k_0=2^37-1` is odd, this pins the square class of the ratio from three
printed field elements. This ratio occurs squared in the cancelled norm
gate, so its remaining value is instead a structural invariant of the top
normalized coefficient `p_(e-1)=q_e/q_1`. The live routes remain the
MDS/non-MDS structural split or a genuinely independent smooth-domain
identity, not a standalone norm computation.

Paying both displayed budgets would extend the exact adjacent determination
through `q<(2^39+2)2^128`. It would not close this whole TARGET node: the
larger-budget rate-half bracket recorded in `statement.md` would remain.
