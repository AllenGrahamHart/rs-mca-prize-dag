# Budget-three fiber-two matched-cycle post-field compiler

- **status:** PROVED
- **closure:** proof plus exact arithmetic certificate
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_matched_lift_field_router`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_ode`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_harmonic_exclusion`

Retain a complete survivor on the two-antipodal-denominator subbranch of the
matched `c=0` generic fiber-two cycle boundary. Put

```text
M=2^36,       N=8M=2^39,       q_field=p^2,
p=1 mod 2N,       r^(4N)=1,       t=r^4!=1.          (PFC1)
```

The doubled-order harmonic outer ratio is impossible:

```text
q_out!=-1.                                           (PFC2)
```

This uses the old exact levels `1,...,38` and a new complete level-`39`
screen of all `2,247,720` split official congruence classes. No modulus in
the exact interval is a hit, even before primality filtering.

The parameter-uniform constant ODE transfers with

```text
D_0=(x-1)(x-t),       deg U_0=2M-1=2^37-1,
(16M-4)D_0U_0-2xD_0'U_0-8xD_0U_0'=kappa!=0.         (PFC3)
```

For a fixed `D_0`, at most one monic `U_0` passes this equation. Put

```text
Q=(x^N-1)/D_0,       A=xU_0^2,       R=Q-A^2,
R=AS+T,       deg T<deg A.                            (PFC4)
```

For the three source pairings define

```text
a_0=r^2,             b_0=(r^2-r+1)^2,
a_1=(r-1)^4,         b_1=(r+1)^4,
a_2=(r^2+1)^2,       b_2=(r^2-4r+1)^2.               (PFC5)
```

The complete square pencil and completion-root matching exist if and only if
at least one `j in {0,1,2}` passes all of

```text
deg S=2M-2=2^37-2,       4b_jT=a_jS^2,               (PFC6)

y_0=4b_j/a_j-2 notin {2,-2},
y_(m+1)=y_m^2-2,       y_39=2,                        (PFC7)

q_out^2-y_0q_out+1=0,
T/q_out=W^4,       W!=0,       deg W=M-1=2^36-1.     (PFC8)
```

Both roots of the reciprocal quadratic in `(PFC8)` lie in
`mu_N\{1,-1}`. The fourth-power verdict is independent of which root is
used, so `q_out` is not a search variable.

The quotient in `(PFC8)` is essential. Under `p=1 mod 4N`, or whenever
`q_out^(N/2)=1`, it is equivalent to the old condition that `T` itself is a
fourth power. In the nonsplit field class an outer ratio of exact order `N`
instead has `q_out^(N/2)=-1`; then `T` lies in the nontrivial quartic coset
and the old unscaled fourth-power test would falsely reject a valid input.

Two necessary first-rejection gates also transfer. With

```text
H_n(t)=[z^n]((1-z)(1-tz))^(-1/2),       H=H_(4M-1)(t),
chi=r+r^(-1),       chi_41=2,                          (PFC9)
```

one selected branch must satisfy

```text
j=0:       tH^2+(chi-1)^2=0,
j=1:       t(chi-2)^2H^2+(chi+2)^2=0,
j=2:       tchi^2H^2+(chi-4)^2=0.                    (PFC10)
```

The coefficient sequence has its usual width-two recurrence. If `kappa` is
from `(PFC3)` and

```text
P=2N+kappa x^2U_0^3,                                 (PFC11)
```

then every accepted branch also satisfies

```text
W divides P,       S divides P^2,
deg gcd(S,P)>=M-1=2^36-1.                            (PFC12)
```

This theorem is a coverage-equivalent compiler through the scalar,
twisted-fourth-power, constant/Legendre, and gcd gates. It does not prove
uniform rejection, transfer the later trace-Jacobi norm endpoint, cover other
matched denominator geometries or `c=1,2`, or authorize a large computation.
