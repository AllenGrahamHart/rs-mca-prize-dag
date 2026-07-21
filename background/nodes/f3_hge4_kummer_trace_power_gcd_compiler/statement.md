# HGE4 Kummer trace-power gcd compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_hge4_norm_gate_count`
- **dependency:** `f3_hge4_kummer_midpoint_trace_power_gate`

Let `m>=8` be dyadic, let `p` be prime with `m|(p-1)`, and put

```text
q=(p-1)/m.
```

Define the Dickson polynomials and trace quotient by

```text
C_0=2,       C_1=X,       C_(j+1)=X C_j-C_(j-1),
C_m(X)-2=(X^2-4)Q_m(X)^2.                         (KTG1)
```

Then `Q_m` is monic, squarefree, has degree `m/2-1`, and its roots in `F_p`
are exactly

```text
{x+x^(-1):x in mu_m\{+1,-1}}.                    (KTG2)
```

Use the square-ratio refinement by setting

```text
M=m       if q is even,
M=m/2     if q is odd,
A(X)=-(X+2)/8,
G_(m,p)=gcd(Q_M(X), A(X)^q-1) in F_p[X],          (KTG3)
```

where the power is reduced modulo `Q_M` before the gcd. The exact number of
trace IDs passing every scalar gate from the dependency is

```text
N_trace(m,p)=deg G_(m,p).                          (KTG4)
```

The corresponding number of ordered endpoint ratios `x` is `2deg G_(m,p)`.
Factoring `G_(m,p)` into its linear factors recovers every passing trace.
Thus the complete scalar prefilter needs one degree-at-most-`m/2-1` modular
power and gcd, rather than midpoint, necklace, or support enumeration.

The gcd may be nonconstant. In particular the exact controls

```text
(m,p,N_trace)=(8,137,1),(16,593,1),(32,1249,1)
```

show that the trace-power gate is not a universal emptiness theorem. The
compiler counts only endpoint traces, not primitive pencils or HGE4 orbits.
