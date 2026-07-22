# `A=1` distance-three bounded-error Pade-circuit reduction

- **status:** PROVED
- **closure:** proof plus exact official integer certificate
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_bounded_tail_dihedral_row_codegree`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_degree_two_tail_rigidity`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_external_split_design_saturation`

Let `Gamma` be the `3e` external slopes. For each exceptional locator `D_i`
define its involution norm, with quotient coordinate `U`, by

```text
N_i(U)=D_i(x)D_i(-x)                    (antipodal),
N_i(U)=c^(-1)D_i(x)D_i(c/x)             (constant product). (QPCIR0)
```

Every `N_i` is a nonzero quadratic. On a good involution pair it is
`(U-u_i)^2`; on a tail pair it need not be a square. Put
`mu_i=P_Z(xi_i)/lambda_i^2` and define the degree-below-`e` interpolation
polynomials by

```text
U^2M_0(xi_i)-2UM_1(xi_i)+M_2(xi_i)=mu_iN_i(U).
```

For every nonidentical full outside
`tau`-orbit with coordinate `u`, let `g_u` be the monic gcd of its two row
polynomials, put `d_u=deg g_u<=t`, and define the squarefree complement

```text
K_u=P_Z g_u/(Q_xQ_tau(x)),       deg K_u=e+d_u.     (QPCIR1)
```

There is a polynomial `A_u` of degree at most `d_u` such that

```text
K_u=I A_u+chi(u)g_u
       [u^2M_0-2uM_1+M_2].                          (QPCIR2)
```

For `gamma in Gamma`, put

```text
q_gamma(U)=
 [U^2M_0(gamma)-2UM_1(gamma)+M_2(gamma)]/I(gamma). (QPCIR3)
```

For every `S={gamma_1,...,gamma_s} subset Gamma`, where
`s=2(t+1)`, define the Pade-circuit determinant

```text
Delta_S(U)=det(
 [1,gamma,...,gamma^t,
  q_gamma(U),gamma q_gamma(U),...,gamma^t q_gamma(U)]
 )_(gamma in S).                                    (QPCIR4)
```

Then `deg Delta_S<=2(t+1)`. If `S` is contained in the roots of `K_u`,
then `Delta_S(u)=0`. Consequently a nonzero `Delta_S` can be selected by at
most `2(t+1)` outside orbit coordinates.

Let `N` be the number of nonidentical full outside involution-orbits, and
let `D_t` count the `s`-subsets for which `Delta_S` is identically zero.
The exact incidence inequality is

```text
N binom(e,s)
 <=N D_t+2(t+1)[binom(3e,s)-D_t].                   (QPCIR5)
```

On the official row `e=2^38-1`, the tail and boundary counts give

```text
antipodal:       t=6, s=14, N>=3e-8,
constant product:t=8, s=18, N>=3e-11.              (QPCIR6)
```

Substitution in `(QPCIR5)` forces

```text
D_6 > (9999/10000) binom(e,14),
D_8 > (991/1000) binom(e,18).                       (QPCIR7)
```

Thus any surviving bounded-tail packet forces almost every indicated subset
of an `e`-sized complement to be an identically singular Pade circuit. The
remaining degree-two task is to classify or upper-bound those identically
singular circuits; a generic nonzero-determinant census cannot close it.
