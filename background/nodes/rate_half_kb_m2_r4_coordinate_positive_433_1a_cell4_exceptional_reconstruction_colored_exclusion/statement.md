# KoalaBear positive 433-1a cell-4 exceptional reconstruction exclusion

- **status:** PROVED
- **scope:** the exceptional signed-pair reconstruction chart `L=M=0` in
  common cell `4`, signs `(-1,-1)`, over `F_2130706433`; source symmetry
  transports the result to cell `7`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_cell4_exceptional_coefficient_projection_decomposition`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_cell4_genus1_plane_kernel_reduction`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_universal_target_elimination_compiler`,
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient`
- **consumer:** `rate_half_band_closure`

The exceptional coefficient projection theorem leaves only the irreducible
curve `H(w0,t)=0`; its zero-dimensional residual has no admissible deployed
point.  On the generic linear-`b` lift, put

```text
x=Q_1D_0-Q_0D_1,
Q_j=z_j B_1(w_j),  w_j=z_j^2.                    (KBC4HX-1)
```

The signed `DE+/DE-` equations and the guards `N_0D_0D_1!=0` force `x!=0`.
Eliminating `w2` from two necessary colored equations, reducing by the plane,
then reducing by `H` and the linear `b` lift gives exactly

```text
T(t) x^4 C(w0,t)=0,                              (KBC4HX-2)
```

away from the recorded pseudo-division scales.  Here `C` has bidegree
`(7,2047)` and `16368` terms.  The exact eliminant

```text
E(t)=Res_w0(H,C)
```

has degree `16248` and `16021` terms.  Its Frobenius gcd
`gcd(E,t^p-t)` has degree `15` and splits into fifteen distinct linear
factors.  Five roots are the original `t=0,+/-1,+/-i` guards.  Direct
specialization of the other ten roots gives only four generic lifted
`(t,w0)` points satisfying the squared signed pair; every one has `D_0=0`.

The two admissible roots removed with the content `T(t)` are

```text
t=1231496538, 1620586492.                        (KBC4HX-3)
```

At each value `H(w0,t)` is a product of two irreducible quadratics, each
with multiplicity two, so it has no deployed `w0` root.

Finally, all six scales in the pseudo-subresultant construction of the
linear `b` lift are classified exactly: the leading coefficient of `H`, the
first subresultant leading coefficient, the quadratic content and leading
coefficient, the linear content, and the final coefficient `A`.  Their union
on `H(F_p)` contains `19` points.  Direct replay of the original
`P,L,M,F` equations at every point leaves no admissible exception: after the
original `t` guards, two points have no deployed `b` root and every deployed
`b` root has `D_0=0`.

Therefore the necessary `DE+/DE-/BE` family is empty on the whole
exceptional chart `L=M=0`.  This excludes that chart in cells `4` and `7`.
It does not exclude the main `L!=0` component, close orbit `[4,7]`, the
positive route, K3, LIST, MCA, or either Prize problem.

## Falsifier

A missed deployed Frobenius root, an admissible content fiber, a scale-zero
point with a guard-valid original lift, an actual signed/colored realization
with `x=0`, or a valid exceptional reconstruction outside the recorded
projection decomposition.
