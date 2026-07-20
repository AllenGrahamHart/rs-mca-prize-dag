# Budget-three fiber-two c=1 parity R0 lift-free compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_c1_parity_frobenius_router`,
  `rate_half_list_budget_three_fiber_two_cycle_c1_parity_nonharmonic_scalar_compiler`

Retain the sole `c=1` parity source pattern on which an anti-invariant lift
can remain. Put

```text
u=r^2 in F_p,       t=u^2=r^4!=1,
K_t(Y)=t(Y-2)^2+4(t-1)^2.                            (R0C1)
```

The two possible `R0` unordered source traces above the fixed denominator
parameter `t` are exactly the two roots of `K_t`. The polynomial is separable.
Consequently the source lift can be removed from the outer-torsion gate.
In `F_p[Y]/(K_t)`, define

```text
C_0=Y,       C_(m+1)=C_m^2-2 mod K_t.               (R0C2)
```

An `R0` source trace lies in the outer `mu_L` trace locus, `L=2^39`, if and
only if

```text
deg gcd(K_t,C_39-2)>=1.                              (R0C3)
```

Now retain the Euclidean data `R=AS+T` from the nonharmonic scalar compiler.
Existence of an `R0` trace satisfying the scalar identity

```text
S^2=(Y+2)T                                           (R0C4)
```

is equivalent to the lift-free polynomial identity

```text
t(S^2-4T)^2+4(t-1)^2T^2=0.                          (R0C5)
```

To require the same trace to pass both `(R0C3)` and `(R0C4)`, take the gcd
of `K_t`, `C_39-2`, and every coefficient in `x` of
`S^2-(Y+2)T`; the combined scalar/torsion gate passes exactly when this gcd
has positive degree. Thus neither `r` nor a lift-sign branch remains.

There is also a new constant first-rejection gate. With

```text
H=H_(4M-1)(t),       M=2^36,
```

every `R0` survivor satisfies

```text
4t(1+tH^2)^2+(t-1)^2=0.                             (R0C6)
```

This theorem is an exact lift-free compiler through the source-trace,
scalar, and constant gates. It does not discharge the twisted fourth-power
or gcd gate, prove uniform rejection, or provide a compressed evaluation of
the official Legendre coefficient.

