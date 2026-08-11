# `A=1` core-free cubic squarefree gap-one correction normal forms

- **status:** PROVED
- **closure:** unique corrected row and exact vertical/contact normal forms
- **consumer:** `rate_half_band_crossing_location`

Retain the core-free cubic scalar branch at `u=1` with three distinct heavy
roots `x_1,x_2,x_3`. For row `i`, let `c_i` be its deficit, `epsilon_i` its
extra excess multiplicity, and `t_i` its number of excess roots outside the
minimal locator. Put `w=Delta-C_tot`. Then exactly one of

```text
(I_0,w,sum epsilon_i)=(0,1,0),(0,0,1),(1,0,0)         (SGN1)
```

occurs, and

```text
sum c_i=e+2+I_0,       sum t_i=e-w.                   (SGN2)
```

Define the row correction

```text
q_i=c_i+epsilon_i-t_i.                               (SGN3)
```

Then there is a unique index `h` such that

```text
q_h=3,       q_i=0 for i!=h.                         (SGN4)
```

Let `R_i` be the reduced distinguished divisor on the fibre over `x_i`,
and let `N_i<=R_i` be its reduced divisor of new roots. If `epsilon_i=0`,
there is an effective vertical degree-`q_i/3` divisor `P_i` with

```text
V_i=R_i+N_i+3P_i,       D_i=R_i+P_i.                 (SGN5)
```

Here `V_i` is the complete vertical divisor and `D_i` is the contact
divisor on that fibre. If `epsilon_i=1`, let `J` be the augmented incidence.
When `J in N_i`,

```text
V_i=R_i+N_i-J+3P_i,       D_i=R_i+P_i,               (SGN6)
deg P_i=q_i/3.
```

When `J notin N_i`, necessarily `q_i=3`, and

```text
V_i=R_i+N_i+2J,       D_i=R_i+J.                     (SGN7)
```

Consequently there is a unique degree-one contact correction `P_h` such
that

```text
div(s_F)=R_1+R_2+R_3+P_h+I_0R_0.                    (SGN8)
```

Writing `Z_i=V_i-R_i`, the resulting Picard identity is

```text
O_C(rho+4,-e-1)=O_C(Z_1+Z_2+Z_3-P_h-I_0R_0),        (SGN9)
deg O_C(rho+4,-e-1)=e+1.                             (SGN10)
```

## Scope

The theorem classifies the correction row and its local divisor types. It
does not enumerate the positive deficit partitions in `(SGN2)`, exclude a
packet, or turn `(SGN9)` into a bounded-degree Picard obstruction.
