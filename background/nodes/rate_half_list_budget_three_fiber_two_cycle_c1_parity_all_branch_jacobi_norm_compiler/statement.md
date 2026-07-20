# Budget-three fiber-two c=1 parity all-branch Jacobi-norm compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_c1_parity_nonharmonic_scalar_compiler`,
  `rate_half_list_budget_three_fiber_two_cycle_c1_parity_frobenius_router`,
  `rate_half_list_budget_three_fiber_two_cycle_c1_parity_r0_jacobi_norm_transfer`

Retain the full nonharmonic `c=1` two-antipodal parity packet. Use

```text
M=2^36,       L=2M=2^37,
a=(r+r^(-1))/2,       x=2a^2-1=(r^2+r^(-2))/2,
epsilon=r^(8L) in {1,-1},
C=C_L^(1/4)(x),       P=P_(2L-1)(x).                (AJC1)
```

For a source cross ratio `z_Xj`, put

```text
h_Xj=(z_Xj+1)/(z_Xj-1).                             (AJC2)
```

The constant gate on branch `(X,j)` is equivalent to

```text
h_Xj=sP,       s^2=-epsilon,                        (AJC3)
```

where the two choices of `s` cover both square-root signs. All denominators
in the six rational functions `h_Xj` are nonzero on `r^4!=1`.

Put `v=sP` and eliminate `r` against

```text
r^4-2xr^2+1=0.                                     (AJC4)
```

Up to nonzero scalar factors, the six resultants collapse to four polynomials:

```text
N_R0=v^4-2v^2+x^2,                                  (AJC5)

N_R12=v^4(x^2-1)+4v^3(x^2-1)
      +6v^2x^2+58v^2+4vx^2-132v+x^2+63,            (AJC6)

N_P0=v^4(x-1)+2v^2(x+3)+x-1,                       (AJC7)

N_P12=v^4(x+1)-4v^3(x+1)
      +14v^2x-18v^2-20vx+44v+25x-7.                (AJC8)
```

Here `R1,R2` give the same `N_R12`, while `P1,P2` give the same `N_P12`.
Thus no source lift remains.

The even-Jacobi transform removes the remaining sign of `x`. Put

```text
w=2x^2-1,       z=(w+1)/2=x^2,
J=J_M^(-1/4,-1/2)(w),
Q=J_(L-1)^(0,1/2)(w) mod J,       q_s=sQ.           (AJC9)
```

After substituting `P=xQ`, each `N` has the form `A+xB`. Define

```text
A_R=q_s^4z^3-q_s^4z^2+6q_s^2z^2+58q_s^2z+z+63,
B_R=4q_s(q_s^2z^2-q_s^2z+z-33),                    (AJC10)

A_P0=-q_s^4z^2+6q_s^2z-1,
B_P0=(q_s^2z+1)^2,                                  (AJC11)

A_P=q_s^4z^2-4q_s^3z^2-18q_s^2z-20q_sz-7,
B_P=q_s^4z^2-4q_s^3z+14q_s^2z+44q_s+25,            (AJC12)

F_R=A_R^2-zB_R^2,
F_P0=A_P0^2-zB_P0^2,
F_P=A_P^2-zB_P^2,                                   (AJC13)

F_R0,epsilon=(1+epsilon zQ^2)^2+z-1.               (AJC14)
```

For the torsion factors

```text
K_-=T_L(w),       K_+=U_(L-1)(w),                   (AJC15)
```

the complete primary/torsion/constant packet has exactly seven tests for
each fixed `epsilon`:

```text
gcd(J,K_epsilon,F_R0,epsilon)!=1,

gcd(J,K_epsilon,F_R(s))!=1,
gcd(J,K_epsilon,F_P0(s))!=1,
gcd(J,K_epsilon,F_P(s))!=1,                         (AJC16)
```

where the last three are run for both roots `s^2=-epsilon` and every input is
reduced modulo `J`. Every representative consequently has degree less than
`M=2^36`.

All fourteen tests share the same torsion-only norm pair `R_-,R_+` already
assigned to CR-002: the order-`2^39` minus norm and the 37-level plus tower.
If no official characteristic divides either norm, the entire generic
two-antipodal `c=1` parity packet is empty. A compatible divisor must still
pass its relevant test in `(AJC16)` and the Euclidean
twisted-fourth-power/gcd gates.

This theorem does not evaluate the shared norms, prove any of the fourteen
gcds trivial, cover nonparity `c=1`, or close adjacent crossing.

