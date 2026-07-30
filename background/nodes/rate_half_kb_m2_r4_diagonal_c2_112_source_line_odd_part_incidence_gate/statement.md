# KoalaBear m2 r4 diagonal c2 (1,1,2) source-line odd-part incidence gate

- **status:** PROVED
- **scope:** saturated `(1,1,2)` packets in the source-line branch
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_saturated_defect_classifier` and
  `rate_half_kb_m2_r4_diagonal_c2_square_fiber_linear_cut`
- **consumer:** `rate_half_band_closure`

Let `{z,z^(-1)} subset K` be the unique internal common-`K` orbit. This
orbit is unramified for the source double cover. At either fiber, the two
pure `J_0-J_0` stars are distinct and share exactly one endpoint `a in J_0`.
In source-line coordinates this gives

```text
U(a,z)=V(a,z)=0,       U(a^(-1),z^(-1))=V(a^(-1),z^(-1))=0. (KBOI-1)
```

Suppose additionally that the forced square orbit is unramified. Orient the
reciprocal internal pair so that its common endpoint `a` is finite, let the
forced quotient label be `w`, and put in the resulting affine chart

```text
q(T)=P_(J_1)(T)=q_0+q_1 T+q_2 T^2,
epsilon in {+1,-1},
F=q_0-epsilon*w*q_2,
G=epsilon*q_2-w*q_0,
M=q_1(1-epsilon*w).
```

Deck distinction makes `V` nonzero. The square-fiber cut and reciprocal
symmetry therefore pin its projective class to

```text
V_(epsilon,w,q)(T,W)=
  (F+GW)+M(1+epsilon W)T+epsilon(G+FW)T^2.         (KBOI-2)
```

For the common endpoint `a` in `(KBOI-1)`, define

```text
N_epsilon(a)=F+Ma+epsilon*G*a^2,
D_epsilon(a)=G+epsilon*Ma+epsilon*F*a^2.
```

Then `D_epsilon(a)` is nonzero and every actual packet satisfies the exact
incidence equation

```text
z=-N_epsilon(a)/D_epsilon(a).                      (KBOI-3)
```

Thus each unramified forced-square packet has only two sign choices and two
`J_0`-orbit choices to test before full interpolation. Failure of all four
printed tests deletes the packet. The theorem does not delete the ramified
forced-square branch, either aligned or near-aligned quotient system, the
biquadratic branch, the exceptional orbit, the `(1,1,2)` row, an owner,
payment, row, or Prize result.

## Falsifier

A saturated source-line packet with a ramified internal `K` orbit, two
disjoint pure stars over one internal fiber, a zero odd part, or an
unramified forced-square packet violating `(KBOI-2)--(KBOI-3)`.
