# Cycle 66: clean resultant saturation and Picard dichotomy (2026-08-10)

## Cycle pins

```text
our start:       7c2721981
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   38 PRs; #1159 remains the newest and is non-overlapping K3
critical open:   28
```

## Boundary saturation

The top coefficient of the domain complement proves

```text
deg_z W=T,       deg_z V=3m+1,
q_inf nu+P_sat omega=1.
```

Thus `W` is a unit at every point of the parameter-infinity fibre. The full
resultant allocation and dual-complement degree are forced:

```text
Res_z(Q,W)=c_W(X-x_0)^(m-1),
Res_z(Q,B)=c_B q_inf^(T+b)(X-x_0),
deg_X B=N.
```

This is
`rate_half_ca_hankel_clean_endpoint_resultant_boundary_saturation`. It
refutes the boundary-free `J_B=1` shortcut.

## Hankel interface

After a generic parameter-basis choice, the `m+1` independent coefficient
vectors of `Q` form a common totally isotropic plane for the four top/bottom
endpoint Hankel forms. Each form has rank `rho`; its endpoint radical is
`q_0` or `q_m=q_inf`. Equivalently the coefficient evaluations satisfy four
exact diagonal rank-one frame cancellations. This is
`rate_half_ca_hankel_clean_endpoint_four_hankel_biisotropic_frame`.

## Two-axis Picard pin

A generic domain-coordinate normalization gives the reciprocal resultants

```text
Res_X(Q,B)=constant*S,
Res_X(Q,W)=constant*a^(deg_X W+N-1)A_0.
```

The complete `Q`--`B` intersection divisor is therefore

```text
div_C(B)=P_*+(T+b)Y_inf,
O_C(N,-T)=O_C(P_*),       degree=Nm-T*rho=1.
```

This is
`rate_half_ca_hankel_clean_endpoint_two_axis_resultant_picard_pin`.

## Injectivity audit and exact correction

The point section is the kernel of

```text
H^1(O(N-rho,-T-m)) -> H^1(O(N,-T)),
```

whose dimensions are `60m^2+10m` and `64m^2+4m`. Relatively its kernel
bundle has rank `m` and degree `m(5-4m)`. This exact bridge is
`rate_half_ca_hankel_clean_endpoint_picard_multiplication_injectivity_reduction`.

Adversarial audit then refutes the tempting injectivity proof. Exact finite
pushforward gives

```text
pi_*O_C=O + O(-rho)^(m-1),
K_Q=pi_*O_C(P_*),
```

so `K_Q` is a length-one positive elementary modification and has exactly
two possible splittings:

```text
O(1)+O(-rho)^(m-1),
O+O(1-rho)+O(-rho)^(m-2).
```

This route fence is
`rate_half_ca_hankel_clean_endpoint_picard_kernel_elementary_modification_dichotomy`.

The first splitting has two degree-one sections and makes `C` isomorphic to
`P^1`. That contradicts the positive adjunction genus
`(4m-2)(m-1)` of a smooth bidegree-`(4m-1,m)` divisor for `m>1`. The proved
node `rate_half_ca_hankel_clean_endpoint_rational_elementary_branch_exclusion`
therefore leaves only

```text
K_Q=O+O(1-rho)+O(-rho)^(m-2),       h^0(K_Q)=1.
```

## Burn-down

```text
result:                  NARROWED; one Picard branch CLOSED
DAG delta:               +6 PROVED leaves, +8 req edges, +6 ev edges
critical status delta:   none
upstream terminal delta: none; no live PR overlap
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The sole clean branch is now the unique-section elementary modification,
subject simultaneously to the saturated two-axis resultants and the
four-Hankel frame. The next route-deciding action is to derive a second
degree-one section from the Hankel data, or prove that the unique-section
modification is incompatible with the supported-locator incidence. Positive
`O` remains separate. No critical status changes.
